#!/usr/bin/env python3
import os
import re
from pathlib import Path
from datetime import datetime

# Paths
src_blog_dir = Path('/home/tj/Sync/code/travisjeffery.github.com/src/b')
dest_blog_dir = Path('/home/tj/Sync/code/travisjeffery.github.com/content/posts')

# Create destination directory if it doesn't exist
dest_blog_dir.mkdir(parents=True, exist_ok=True)

def convert_markdown_file(src_file):
    """Convert a markdown file from Metalsmith format to Hugo format."""
    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse front matter (YAML between ---)
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            body = parts[2].lstrip('\n')
        else:
            return None
    else:
        return None

    # Parse frontmatter
    metadata = {}
    for line in frontmatter.strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            # Remove quotes if present
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            metadata[key] = value

    # Convert to Hugo format
    hugo_frontmatter = '---\n'
    hugo_frontmatter += f'title: "{metadata.get("title", "Untitled")}"\n'

    # Parse date and convert
    if 'date' in metadata:
        date_str = metadata['date']
        try:
            # Try parsing the metalsmith date format
            date_obj = datetime.strptime(date_str.split()[0], '%Y-%m-%d')
            hugo_frontmatter += f'date: {date_obj.isoformat()}Z\n'
        except:
            pass

    # Add draft status
    draft = metadata.get('draft', 'false').lower() == 'true'
    if draft:
        hugo_frontmatter += 'draft: true\n'

    # Add tags if collection is present
    if 'collection' in metadata:
        hugo_frontmatter += f'tags: ["{metadata["collection"]}"]\n'

    # Add external link if medium_link is present
    if 'medium_link' in metadata:
        hugo_frontmatter += f'externalLink: "{metadata["medium_link"]}"\n'

    hugo_frontmatter += '---\n'

    return hugo_frontmatter + body

# Convert all markdown files
count = 0
errors = 0
for md_file in src_blog_dir.rglob('*.md'):
    # Skip non-post files
    if md_file.name in ['emacs.md']:
        continue

    # Get the filename
    filename = md_file.name

    # Convert the file
    converted = convert_markdown_file(md_file)
    if converted is None:
        print(f"Error converting {md_file}")
        errors += 1
        continue

    # Write to destination
    dest_file = dest_blog_dir / filename
    with open(dest_file, 'w', encoding='utf-8') as f:
        f.write(converted)

    count += 1
    print(f"Converted: {filename}")

print(f"\nTotal converted: {count}")
if errors:
    print(f"Errors: {errors}")
