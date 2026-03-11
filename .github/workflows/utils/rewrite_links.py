"""Rewrite .ipynb links in notebook markdown cells to ../filename.md for MkDocs."""

#!/usr/bin/env python3

import re
import sys
from pathlib import Path

import nbformat

if len(sys.argv) != 2:
    print("Usage: rewrite_links.py <notebook_directory>")
    sys.exit(1)

notebook_dir = Path(sys.argv[1])

if not notebook_dir.is_dir():
    print(f"Error: {notebook_dir} is not a directory.")
    sys.exit(1)

for nb_path in notebook_dir.glob("*.ipynb"):
    print(f"Processing {nb_path}")
    nb = nbformat.read(nb_path, as_version=4)

    for cell in nb.cells:
        if cell.cell_type != "markdown":
            continue

        def rewrite_link(match):
            """Rewrite .ipynb link to ../filename."""
            text, href = match.group(1), match.group(2)
            new_href = re.sub(r"^(?!\.\./|https?://|/)([^)]+)\.ipynb$", r"../\1", href)
            if new_href != href:
                print(f"  Rewrote {href} -> {new_href}")
            return f"[{text}]({new_href})"

        cell.source = re.sub(r"\[([^\]]*)\]\(([^)]+)\)", rewrite_link, cell.source)

    nbformat.write(nb, nb_path)
