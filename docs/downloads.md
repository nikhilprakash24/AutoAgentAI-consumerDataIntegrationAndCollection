# Downloads

Shareable, offline copies of the documentation — for sending to collaborators,
investors, or anyone who'd rather read or edit outside GitHub.

| File | Format | Best for |
|---|---|---|
| **[Full Documentation (Word)](exports/AutoAgentAI-Documentation.docx)** | `.docx` | **Editing** — hand to anyone; open in Word, Google Docs, or Pages. ~19k words, all 29 sections, table of contents. |
| **[Full Documentation (PDF)](exports/AutoAgentAI-Full-Documentation.pdf)** | `.pdf` | **Reading / sharing** — the whole site as a polished, print-ready PDF with every diagram rendered (82 pages). |
| **[Executive Summary (PDF)](exports/AutoAgentAI-Executive-Summary.pdf)** | `.pdf` | **One-pager** — the whole pitch on a single page, ready to send. |

## Editing and round-tripping

- The **Word doc** is the one to edit. Internal cross-links are flattened to plain
  text and diagrams appear as labelled Mermaid source (they render as pictures in
  the PDF and on the live site). Send edits back and they can be merged into the
  markdown so the live site stays the source of truth.
- These are **point-in-time** exports. They don't auto-update when the site changes.

## Regenerating

From the repository root:

```bash
make exports      # rebuilds docs/exports/ (Word + full PDF with diagrams)
make count        # word & line counts
make serve        # live-preview the site
```

Requires `pandoc`, `python3` + `python-docx`, and `node` + `playwright` (Chromium)
for the diagram-rendering step. See `tools/build-exports.sh`.
