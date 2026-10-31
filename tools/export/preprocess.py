#!/usr/bin/env python3
"""Combine the docs/ markdown pages into one file for export.

Usage:
  python3 tools/export/preprocess.py --mode text --out build/combined.md
  python3 tools/export/preprocess.py --mode keep --out build/combined-mermaid.md

--mode text : Mermaid blocks become labelled plain-text code (for Word/.docx).
--mode keep : Mermaid fences are preserved (for HTML/PDF, where they render).

In both modes: MkDocs admonitions become labelled blockquotes, and internal
.md/.pdf cross-links are flattened to plain text.
"""
import argparse, os, re

ORDER = [
    ("index.md", "Home"),
    ("audiences/executive-summary.md", "Executive Summary"),
    ("audiences/investor-pitch.md", "Investor Pitch"),
    ("audiences/technical-overview.md", "Technical Overview"),
    ("audiences/for-sales-managers.md", "For Sales Managers"),
    ("vision.md", "Vision"),
    ("problem-motivation.md", "Problem & Motivation"),
    ("concepts-glossary.md", "Concepts & Glossary"),
    ("architecture.md", "Architecture"),
    ("customer-integration.md", "Customer Integration"),
    ("insights-engine.md", "Insights Engine"),
    ("behaviour-models.md", "Behaviour Models"),
    ("decision-making.md", "Decision Making"),
    ("agent-loop.md", "The AutoAgent Loop"),
    ("use-cases.md", "Use Cases"),
    ("deployment/on-prem-ai-hardware.md", "On-Prem AI & Hardware"),
    ("deployment/privacy-pii-future-proofing.md", "Privacy, PII & Future-Proofing"),
    ("deployment/cloud-vs-onprem-risks.md", "Cloud vs On-Prem Risks"),
    ("deployment/local-models-are-enough.md", "Local Models Are Enough"),
    ("perspectives/raw-data-to-action.md", "Raw Data to Action"),
    ("perspectives/reinventing-the-salesperson.md", "Reinventing the Salesperson"),
    ("perspectives/why-salespeople-cant-capture-this.md", "Why Salespeople Can't Capture This"),
    ("perspectives/the-most-valuable-data-in-autos.md", "The Most Valuable Data in Autos"),
    ("perspectives/how-valuable-this-data-is.md", "How Valuable This Data Is"),
    ("perspectives/automotive-data-closing-the-loop.md", "Closing the Loop to the OEM"),
    ("perspectives/the-closed-loop.md", "The Closed Loop"),
    ("roadmap.md", "Roadmap"),
    ("specs/index.md", "Specifications"),
    ("assets/diagrams/FIGURE_SPECS.md", "Figure Specs"),
]

PAGEBREAK_DOCX = '\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'
PAGEBREAK_HTML = '\n\n<div class="page-break"></div>\n\n'


def delink(text):
    return re.sub(
        r'\[([^\]]+)\]\((?:\.{0,2}/)?[^)]*\.(?:md|pdf)(?:#[^)]*)?\)',
        r'\1', text)


def convert_mermaid(lines, mode):
    if mode == "keep":
        return lines
    out, i = [], 0
    while i < len(lines):
        if re.match(r'^\s*```mermaid\s*$', lines[i]):
            body, i = [], i + 1
            while i < len(lines) and not re.match(r'^\s*```\s*$', lines[i]):
                body.append(lines[i]); i += 1
            i += 1
            out += ["*Diagram (Mermaid source — renders on the live site):*", "",
                    "```text", *body, "```"]
        else:
            out.append(lines[i]); i += 1
    return out


def convert_admonitions(lines):
    out, i = [], 0
    adm = re.compile(r'^([!?]{3})\s+(\w+)(?:\s+"([^"]*)")?\s*$')
    while i < len(lines):
        m = adm.match(lines[i])
        if m:
            label = m.group(3) or m.group(2).capitalize()
            i += 1
            body = []
            while i < len(lines):
                ln = lines[i]
                if ln.strip() == "":
                    body.append(""); i += 1; continue
                if ln.startswith("    "):
                    body.append(ln[4:]); i += 1; continue
                break
            while body and body[-1] == "":
                body.pop()
            out += ["", f"> **{label}**", ">"]
            out += [">" if b == "" else "> " + b for b in body]
            out.append("")
        else:
            out.append(lines[i]); i += 1
    return out


def process(text, mode):
    text = delink(text)
    lines = text.split("\n")
    lines = convert_mermaid(lines, mode)
    lines = convert_admonitions(lines)
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["text", "keep"], required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--docs", default="docs")
    args = ap.parse_args()

    pb = PAGEBREAK_HTML if args.mode == "keep" else PAGEBREAK_DOCX
    parts = [
        "---",
        'title: "AutoAgentAI — Full Documentation"',
        'subtitle: "Combined export of the documentation site"',
        'date: "2026-10-31"',
        "---", "",
        "> **About this document**", ">",
        "> Combined export of the AutoAgentAI documentation site, assembled into one",
        "> file for review and editing. The source of truth remains the GitHub repo;",
        "> edits here can be merged back. Regenerate with `make exports`.", "",
    ]
    for idx, (rel, _t) in enumerate(ORDER):
        with open(os.path.join(args.docs, rel), encoding="utf-8") as f:
            txt = f.read()
        if idx > 0:
            parts.append(pb)
        parts.append(process(txt, args.mode))

    combined = "\n".join(parts)
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(combined)
    print(f"wrote {args.out} ({len(combined)} chars, {len(ORDER)} sections, mode={args.mode})")


if __name__ == "__main__":
    main()
