#!/usr/bin/env python3
"""Create a branded pandoc reference.docx (indigo/purple AutoAgentAI styling).

Starts from pandoc's default reference doc and recolours the title/heading styles.
Usage: python3 tools/export/make_reference.py <base_reference.docx> <out_reference.docx>
"""
import sys
import docx
from docx.shared import RGBColor, Pt

base, out = sys.argv[1], sys.argv[2]
d = docx.Document(base)

# (style name, hex colour, size pt, bold)
BRAND = [
    ("Title",      "4F46E5", 28, True),
    ("Subtitle",   "7C3AED", 14, False),
    ("Heading 1",  "4F46E5", 20, True),
    ("Heading 2",  "5B21B6", 15, True),
    ("Heading 3",  "6D28D9", 12.5, True),
]

for name, hexcol, size, bold in BRAND:
    try:
        f = d.styles[name].font
    except KeyError:
        continue
    f.color.rgb = RGBColor.from_string(hexcol)
    f.size = Pt(size)
    f.bold = bold

# Base body font a touch more modern/readable.
try:
    nf = d.styles["Normal"].font
    nf.name = "Calibri"
    nf.size = Pt(11)
except KeyError:
    pass

d.save(out)
print("wrote branded reference:", out)
