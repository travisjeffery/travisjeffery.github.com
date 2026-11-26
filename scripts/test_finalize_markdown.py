#!/usr/bin/env python3
"""Unit tests for scripts/finalize-markdown.py."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPT_PATH = Path(__file__).with_name("finalize-markdown.py")
SPEC = importlib.util.spec_from_file_location("finalize_markdown", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
mod = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = mod
SPEC.loader.exec_module(mod)


class FinalizeMarkdownTests(unittest.TestCase):
    def test_headings_normalized_and_code_blocks_preserve_lang(self) -> None:
        html = """
        <div id="outline-container-1" class="outline-3">
          <h3>The system</h3>
          <div class="outline-text-3">
            <p>Install via:</p>
            <div class="src src-bash"><div class="highlight"><pre tabindex="0"><code class="language-bash" data-lang="bash"><span style="display:flex"><span>npm config <span style="color:#6639ba">set</span> registry http://localhost:8080/npm/
</span></span><span style="display:flex"><span>export GOPROXY=http://localhost:8080/go</span></span></code></pre></div></div>
            <h4>Details</h4>
            <div class="src src-text"><div class="highlight"><pre><code class="language-text" data-lang="text"><span>a -&gt; b</span></code></pre></div></div>
          </div>
        </div>
        """
        out = mod.html_to_markdown(html, base_url="https://travisjeffery.com/example/")
        expected = (
            "## The system\n\n"
            "Install via:\n\n"
            "```bash\n"
            "npm config set registry http://localhost:8080/npm/\n"
            "export GOPROXY=http://localhost:8080/go\n"
            "```\n\n"
            "### Details\n\n"
            "```\n"
            "a -> b\n"
            "```"
        )
        self.assertEqual(out, expected)

    def test_example_block_and_backticks_in_code(self) -> None:
        html = '<pre class="example">\nline 1\n```nested```\nline 3\n</pre>'
        out = mod.html_to_markdown(html)
        self.assertEqual(out, "````\nline 1\n```nested```\nline 3\n````")

    def test_inline_formatting_and_code_backticks(self) -> None:
        html = (
            '<p>Use <code class="verbatim">~/.config/app/config.toml</code> and '
            "<code>`backtick`</code> with <strong>bold </strong>and <em>italic</em> "
            'and <a href="https://example.com">link</a>.</p>'
        )
        out = mod.html_to_markdown(html)
        self.assertEqual(
            out,
            "Use `~/.config/app/config.toml` and `` `backtick` `` with **bold** and *italic* and [link](https://example.com).",
        )

    def test_nested_list_inside_ordered_list(self) -> None:
        html = """
        <ol>
          <li><strong>Step one.</strong> Do A.</li>
          <li><strong>Step two.</strong>
            <ul>
              <li><strong>Sub A:</strong> first</li>
              <li><strong>Sub B:</strong> second</li>
            </ul>
          </li>
        </ol>
        """
        out = mod.html_to_markdown(html)
        expected = (
            "1. **Step one.** Do A.\n"
            "2. **Step two.**\n"
            "   - **Sub A:** first\n"
            "   - **Sub B:** second"
        )
        self.assertEqual(out, expected)

    def test_blockquote_with_hard_breaks(self) -> None:
        html = (
            "<blockquote><p>alice: hello?<br>bob: yes.<br>"
            "[deleted]: nice</p></blockquote>"
        )
        out = mod.html_to_markdown(html)
        expected = (
            "> alice: hello?  \n"
            "> bob: yes.  \n"
            "> [deleted]: nice"
        )
        self.assertEqual(out, expected)

    def test_gfm_table_and_pipe_escaping(self) -> None:
        html = """
        <table>
          <thead><tr><th>Piece</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td><code>cli</code></td><td>Uses a | b</td></tr>
          </tbody>
        </table>
        """
        out = mod.html_to_markdown(html)
        expected = (
            "| Piece | Notes |\n"
            "| --- | --- |\n"
            r"| `cli` | Uses a \| b |"
        )
        self.assertEqual(out, expected)

    def test_images_and_video_resolve_relative_urls(self) -> None:
        html = (
            '<p><img src="images/screenshot.png" alt="images/screenshot.png" title="images/screenshot.png"></p>'
            '<video controls class="img-fluid"><source src="images/karaoke.mov" type="video/mp4"></video>'
        )
        out = mod.html_to_markdown(html, base_url="https://travisjeffery.com/demo/")
        expected = (
            "![screenshot.png](https://travisjeffery.com/demo/images/screenshot.png)\n\n"
            "[Video: karaoke.mov](https://travisjeffery.com/demo/images/karaoke.mov)"
        )
        self.assertEqual(out, expected)

    def test_finalize_markdown_text_and_directory(self) -> None:
        sample = (
            '---\n'
            'title: "Test Post"\n'
            'date: 2026-01-23\n'
            'url: "https://travisjeffery.com/test-post/"\n'
            '---\n\n'
            '# Test Post\n\n'
            '<!-- HUGO_ORG_HTML_START -->\n'
            '<p>Hello <a href="https://example.com">world</a>.</p>\n'
            '<!-- HUGO_ORG_HTML_END -->\n'
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            p = root / "test-post" / "index.md"
            p.parent.mkdir(parents=True)
            p.write_text(sample, encoding="utf-8")

            total, converted = mod.finalize_directory(root)
            self.assertEqual((total, converted), (1, 1))
            result = p.read_text(encoding="utf-8")
            self.assertNotIn("HUGO_ORG_HTML_START", result)
            self.assertIn("Hello [world](https://example.com).", result)

    def test_unpaired_marker_raises(self) -> None:
        with self.assertRaises(ValueError):
            mod.finalize_markdown_text("<!-- HUGO_ORG_HTML_START -->\n<p>oops</p>")


if __name__ == "__main__":
    unittest.main()
