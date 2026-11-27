#!/usr/bin/env python3
"""Finalize Hugo-generated Markdown outputs by converting embedded Org HTML blocks to clean Markdown."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import urljoin, urlparse

START_MARKER = "<!-- HUGO_ORG_HTML_START -->"
END_MARKER = "<!-- HUGO_ORG_HTML_END -->"

VOID_ELEMENTS = frozenset(
    {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    }
)

BLOCK_TAGS = frozenset(
    {
        "address",
        "article",
        "aside",
        "blockquote",
        "dd",
        "details",
        "div",
        "dl",
        "dt",
        "figcaption",
        "figure",
        "footer",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "hr",
        "li",
        "main",
        "nav",
        "ol",
        "p",
        "pre",
        "section",
        "table",
        "ul",
        "video",
    }
)


@dataclass
class Element:
    tag: str
    attrs: dict[str, str] = field(default_factory=dict)
    children: list[Element | str] = field(default_factory=list)


class _DOMBuilder(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Element("root")
        self._stack: list[Element] = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attr_map = {k.lower(): (v if v is not None else "") for k, v in attrs}
        elem = Element(tag=tag, attrs=attr_map)
        self._stack[-1].children.append(elem)
        if tag not in VOID_ELEMENTS:
            self._stack.append(elem)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attr_map = {k.lower(): (v if v is not None else "") for k, v in attrs}
        self._stack[-1].children.append(Element(tag=tag, attrs=attr_map))

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in VOID_ELEMENTS:
            return
        for idx in range(len(self._stack) - 1, 0, -1):
            if self._stack[idx].tag == tag:
                del self._stack[idx:]
                break

    def handle_data(self, data: str) -> None:
        if data:
            self._stack[-1].children.append(data)


def _parse_html(html_text: str) -> Element:
    builder = _DOMBuilder()
    builder.feed(html_text)
    builder.close()
    return builder.root


def _collect_raw_text(node: Element | str) -> str:
    if isinstance(node, str):
        return node
    if node.tag == "br":
        return "\n"
    return "".join(_collect_raw_text(child) for child in node.children)


def _min_heading_level(node: Element | str) -> int | None:
    if isinstance(node, str):
        return None
    best: int | None = None
    if len(node.tag) == 2 and node.tag[0] == "h" and node.tag[1] in "123456":
        best = int(node.tag[1])
    for child in node.children:
        sub = _min_heading_level(child)
        if sub is not None and (best is None or sub < best):
            best = sub
    return best


def _extract_lang_from_classes(classes: str) -> str:
    for token in classes.split():
        if token.startswith("language-"):
            return token[len("language-") :]
        if token.startswith("src-") and token != "src":
            return token[len("src-") :]
    return ""


def _resolve_url(href: str, base_url: str) -> str:
    href = href.strip()
    if not href or not base_url:
        return href
    if href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return href
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc:
        return href
    return urljoin(base_url, href)


def _format_inline_code(text: str) -> str:
    runs = [len(m.group(0)) for m in re.finditer(r"`+", text)]
    delim = "`" * (max(runs, default=0) + 1)
    if text and (
        text.startswith("`")
        or text.endswith("`")
        or (text.startswith(" ") and text.endswith(" ") and text.strip())
    ):
        return f"{delim} {text} {delim}"
    return f"{delim}{text}{delim}"


def _format_fenced_code(code: str, lang: str) -> str:
    if code.startswith("\n"):
        code = code[1:]
    code = code.rstrip("\n")
    runs = [len(m.group(0)) for m in re.finditer(r"`+", code)]
    fence = "`" * max(3, max(runs, default=0) + 1)
    info = "" if lang in ("", "text", "nil") else lang
    if code:
        return f"{fence}{info}\n{code}\n{fence}"
    return f"{fence}{info}\n{fence}"


def _wrap_emphasis(text: str, marker: str) -> str:
    if not text.strip():
        return text
    match = re.match(r"^(\s*)(.*?)(\s*)$", text, re.S)
    assert match is not None
    lead, body, trail = match.groups()
    return f"{lead}{marker}{body}{marker}{trail}"


def _normalize_inline_ws(text: str) -> str:
    lines = text.split("\n")
    cleaned: list[str] = []
    for idx, line in enumerate(lines):
        if idx > 0:
            line = line.lstrip(" \t")
        if idx < len(lines) - 1:
            # Preserve intentional Markdown hard line breaks ("  \n").
            if line.endswith("  "):
                line = re.sub(r"[ \t]+$", "", line[:-2]) + "  "
            else:
                line = line.rstrip(" \t")
        cleaned.append(line)
    return "\n".join(cleaned).strip()


class _MarkdownRenderer:
    def __init__(self, base_url: str, heading_shift: int) -> None:
        self.base_url = base_url
        self.heading_shift = heading_shift

    def render_blocks(self, nodes: list[Element | str]) -> str:
        blocks: list[str] = []
        inline_buf: list[Element | str] = []

        def flush_inline() -> None:
            if not inline_buf:
                return
            rendered = _normalize_inline_ws(self.render_inline_nodes(inline_buf))
            inline_buf.clear()
            if rendered:
                blocks.append(rendered)

        for node in nodes:
            if isinstance(node, Element) and node.tag in BLOCK_TAGS:
                flush_inline()
                rendered = self.render_block(node)
                if rendered:
                    blocks.append(rendered)
            else:
                inline_buf.append(node)
        flush_inline()
        return "\n\n".join(blocks)

    def render_block(self, node: Element) -> str:
        tag = node.tag

        if len(tag) == 2 and tag[0] == "h" and tag[1] in "123456":
            level = max(2, min(6, int(tag[1]) + self.heading_shift))
            text = _normalize_inline_ws(self.render_inline_nodes(node.children))
            text = text.replace("\n", " ")
            return f"{'#' * level} {text}" if text else ""

        if tag == "p":
            return _normalize_inline_ws(self.render_inline_nodes(node.children))

        if tag == "hr":
            return "---"

        if tag == "pre":
            return self._render_pre(node, inherited_lang="")

        if tag == "div":
            lang = _extract_lang_from_classes(node.attrs.get("class", ""))
            pre = self._find_single_pre(node)
            if pre is not None:
                return self._render_pre(pre, inherited_lang=lang)
            return self.render_blocks(node.children)

        if tag == "blockquote":
            inner = self.render_blocks(node.children)
            if not inner:
                return ""
            out_lines = [f"> {line}" if line else ">" for line in inner.splitlines()]
            return "\n".join(out_lines)

        if tag in ("ul", "ol"):
            return self._render_list(node)

        if tag == "table":
            return self._render_table(node)

        if tag == "dl":
            return self._render_dl(node)

        if tag == "video":
            return self._render_video(node)

        if tag == "figure":
            return self.render_blocks(node.children)

        if tag == "figcaption":
            text = _normalize_inline_ws(self.render_inline_nodes(node.children))
            return _wrap_emphasis(text, "*") if text else ""

        return self.render_blocks(node.children)

    def _find_single_pre(self, div: Element) -> Element | None:
        non_ws = [c for c in div.children if not (isinstance(c, str) and not c.strip())]
        if len(non_ws) != 1 or not isinstance(non_ws[0], Element):
            return None
        only = non_ws[0]
        if only.tag == "pre":
            return only
        if only.tag == "div" and "highlight" in only.attrs.get("class", "").split():
            return self._find_single_pre(only)
        return None

    def _render_pre(self, pre: Element, inherited_lang: str) -> str:
        lang = inherited_lang
        if not lang:
            lang = _extract_lang_from_classes(pre.attrs.get("class", ""))
        for child in pre.children:
            if isinstance(child, Element) and child.tag == "code":
                code_lang = child.attrs.get("data-lang", "") or _extract_lang_from_classes(
                    child.attrs.get("class", "")
                )
                if code_lang:
                    lang = code_lang
                    break
        raw = _collect_raw_text(pre)
        return _format_fenced_code(raw, lang.strip().lower())

    def _render_list(self, list_elem: Element) -> str:
        ordered = list_elem.tag == "ol"
        start = 1
        if ordered:
            try:
                start = int(list_elem.attrs.get("start", "1"))
            except ValueError:
                start = 1

        items = [c for c in list_elem.children if isinstance(c, Element) and c.tag == "li"]
        rendered_items: list[tuple[str, bool]] = []
        any_loose = False

        for idx, item in enumerate(items, start=start):
            marker = f"{idx}. " if ordered else "- "
            content, is_loose = self._render_list_item(item)
            if is_loose:
                any_loose = True
            if not content:
                rendered_items.append((marker.rstrip(), is_loose))
                continue
            indent = " " * len(marker)
            lines = content.splitlines()
            formatted = [f"{marker}{lines[0]}"]
            for line in lines[1:]:
                formatted.append(f"{indent}{line}" if line else "")
            rendered_items.append(("\n".join(formatted), is_loose))

        sep = "\n\n" if any_loose else "\n"
        return sep.join(text for text, _ in rendered_items)

    def _render_list_item(self, item: Element) -> tuple[str, bool]:
        blocks: list[tuple[str, str]] = []
        inline_buf: list[Element | str] = []

        def flush_inline() -> None:
            if not inline_buf:
                return
            rendered = _normalize_inline_ws(self.render_inline_nodes(inline_buf))
            inline_buf.clear()
            if rendered:
                blocks.append(("inline", rendered))

        for child in item.children:
            if isinstance(child, Element) and child.tag in BLOCK_TAGS:
                flush_inline()
                rendered = self.render_block(child)
                if rendered:
                    blocks.append((child.tag, rendered))
            else:
                inline_buf.append(child)
        flush_inline()

        if not blocks:
            return "", False

        non_list_blocks = [kind for kind, _ in blocks if kind not in ("ul", "ol")]
        is_loose = len(non_list_blocks) > 1

        parts: list[str] = []
        for idx, (kind, text) in enumerate(blocks):
            if idx == 0:
                parts.append(text)
            elif kind in ("ul", "ol") and not is_loose:
                parts.append("\n" + text)
            else:
                parts.append("\n\n" + text)
        return "".join(parts), is_loose

    def _render_table(self, table: Element) -> str:
        header_rows: list[list[str]] = []
        body_rows: list[list[str]] = []

        def render_row(tr: Element) -> tuple[list[str], bool]:
            cells: list[str] = []
            all_th = True
            for cell in tr.children:
                if isinstance(cell, Element) and cell.tag in ("th", "td"):
                    if cell.tag != "th":
                        all_th = False
                    text = _normalize_inline_ws(self.render_inline_nodes(cell.children))
                    text = re.sub(r"\s*\n\s*", " ", text)
                    text = text.replace("|", r"\|")
                    cells.append(text)
            return cells, (bool(cells) and all_th)

        for section in table.children:
            if not isinstance(section, Element):
                continue
            if section.tag == "thead":
                for row in section.children:
                    if isinstance(row, Element) and row.tag == "tr":
                        cells, _ = render_row(row)
                        if cells:
                            header_rows.append(cells)
            elif section.tag in ("tbody", "tfoot"):
                for row in section.children:
                    if isinstance(row, Element) and row.tag == "tr":
                        cells, all_th = render_row(row)
                        if not cells:
                            continue
                        if not header_rows and all_th:
                            header_rows.append(cells)
                        else:
                            body_rows.append(cells)
            elif section.tag == "tr":
                cells, all_th = render_row(section)
                if not cells:
                    continue
                if not header_rows and all_th:
                    header_rows.append(cells)
                else:
                    body_rows.append(cells)

        if not header_rows and body_rows:
            header_rows.append(body_rows.pop(0))
        if not header_rows:
            return ""

        header = header_rows[0]
        extra_headers = header_rows[1:]
        all_rows = [header, *extra_headers, *body_rows]
        ncols = max(len(r) for r in all_rows)

        def fmt_row(row: list[str]) -> str:
            padded = row + [""] * (ncols - len(row))
            return "| " + " | ".join(padded) + " |"

        lines = [
            fmt_row(header),
            "| " + " | ".join(["---"] * ncols) + " |",
        ]
        for row in extra_headers + body_rows:
            lines.append(fmt_row(row))
        return "\n".join(lines)

    def _render_dl(self, dl: Element) -> str:
        entries: list[str] = []
        current_term = ""
        for child in dl.children:
            if not isinstance(child, Element):
                continue
            if child.tag == "dt":
                current_term = _normalize_inline_ws(self.render_inline_nodes(child.children))
            elif child.tag == "dd":
                defn = self.render_blocks(child.children)
                if current_term:
                    entries.append(f"- **{current_term}**: {defn}" if defn else f"- **{current_term}**")
                    current_term = ""
                elif defn:
                    entries.append(f"- {defn}")
        if current_term:
            entries.append(f"- **{current_term}**")
        return "\n".join(entries)

    def _render_video(self, video: Element) -> str:
        src = video.attrs.get("src", "").strip()
        if not src:
            for child in video.children:
                if isinstance(child, Element) and child.tag == "source":
                    src = child.attrs.get("src", "").strip()
                    if src:
                        break
        if not src:
            return ""
        resolved = _resolve_url(src, self.base_url)
        label = Path(urlparse(src).path).name or src
        return f"[Video: {label}]({resolved})"

    def render_inline_nodes(self, nodes: list[Element | str]) -> str:
        return "".join(self.render_inline(n) for n in nodes)

    def render_inline(self, node: Element | str) -> str:
        if isinstance(node, str):
            return re.sub(r"[ \t\r\n]+", " ", node)

        tag = node.tag
        if tag == "br":
            return "  \n"
        if tag in ("strong", "b"):
            return _wrap_emphasis(self.render_inline_nodes(node.children), "**")
        if tag in ("em", "i"):
            inner = self.render_inline_nodes(node.children)
            marker = "_" if "*" in inner else "*"
            return _wrap_emphasis(inner, marker)
        if tag in ("del", "s", "strike"):
            return _wrap_emphasis(self.render_inline_nodes(node.children), "~~")
        if tag == "code":
            return _format_inline_code(_collect_raw_text(node))
        if tag == "a":
            href = node.attrs.get("href", "").strip()
            text = _normalize_inline_ws(self.render_inline_nodes(node.children))
            if not href:
                return text
            resolved = _resolve_url(href, self.base_url)
            label = text or resolved
            return f"[{label}]({resolved})"
        if tag == "img":
            raw_src = node.attrs.get("src", "").strip()
            if not raw_src:
                return ""
            resolved = _resolve_url(raw_src, self.base_url)
            alt = node.attrs.get("alt", "").strip()
            if not alt or alt == raw_src:
                alt = Path(urlparse(raw_src).path).name or raw_src
            alt = alt.replace("[", r"\[").replace("]", r"\]")
            title = node.attrs.get("title", "").strip()
            if title and title not in (alt, raw_src):
                escaped_title = title.replace('"', r"\"")
                return f'![{alt}]({resolved} "{escaped_title}")'
            return f"![{alt}]({resolved})"
        if tag == "video":
            return self._render_video(node)
        if tag == "sup":
            inner = self.render_inline_nodes(node.children)
            return f"^{inner}" if inner else ""
        return self.render_inline_nodes(node.children)


def html_to_markdown(html_fragment: str, base_url: str = "") -> str:
    root = _parse_html(html_fragment)
    min_h = _min_heading_level(root)
    shift = (2 - min_h) if (min_h is not None and min_h > 2) else 0
    renderer = _MarkdownRenderer(base_url=base_url, heading_shift=shift)
    return renderer.render_blocks(root.children).strip()


def _extract_frontmatter_url(content: str) -> str:
    if not content.startswith("---\n"):
        return ""
    end_idx = content.find("\n---\n", 4)
    if end_idx == -1:
        return ""
    frontmatter = content[4:end_idx]
    match = re.search(r'^url:\s*"([^"]+)"\s*$', frontmatter, re.M)
    if match:
        return match.group(1)
    match = re.search(r"^url:\s*(\S+)\s*$", frontmatter, re.M)
    return match.group(1) if match else ""


def finalize_markdown_text(content: str, source_label: str = "<input>") -> tuple[str, bool]:
    has_start = START_MARKER in content
    has_end = END_MARKER in content
    if not has_start and not has_end:
        return content, False
    if has_start != has_end:
        raise ValueError(f"{source_label}: unpaired Org HTML conversion marker")

    base_url = _extract_frontmatter_url(content)
    pattern = re.compile(
        re.escape(START_MARKER) + r"(.*?)" + re.escape(END_MARKER),
        re.S,
    )

    def _replace(match: re.Match[str]) -> str:
        return html_to_markdown(match.group(1), base_url=base_url)

    updated, count = pattern.subn(_replace, content)
    if count == 0 or START_MARKER in updated or END_MARKER in updated:
        raise ValueError(f"{source_label}: failed to expand all Org HTML markers cleanly")

    updated = re.sub(r"\n{3,}", "\n\n", updated).rstrip() + "\n"
    return updated, True


def finalize_directory(public_dir: Path) -> tuple[int, int]:
    if not public_dir.is_dir():
        raise FileNotFoundError(f"Output directory not found: {public_dir}")

    total_md = 0
    converted = 0
    for md_path in sorted(public_dir.rglob("*.md")):
        total_md += 1
        original = md_path.read_text(encoding="utf-8")
        updated, changed = finalize_markdown_text(original, source_label=str(md_path))
        if changed:
            md_path.write_text(updated, encoding="utf-8")
            converted += 1
    return total_md, converted


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert embedded Hugo Org-HTML blocks in generated .md files into clean Markdown."
    )
    parser.add_argument(
        "public_dir",
        nargs="?",
        default="public",
        help="Path to the Hugo output directory (default: public)",
    )
    args = parser.parse_args(argv)

    total_md, converted = finalize_directory(Path(args.public_dir))
    print(f"Finalized Markdown outputs in {args.public_dir}: {converted} converted ({total_md} total .md files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
