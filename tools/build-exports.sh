#!/usr/bin/env bash
# Build the combined documentation exports (Word + full PDF with diagrams).
#
# Requirements: pandoc, python3 + python-docx, node + playwright (Chromium).
# Run from the repository root:  bash tools/build-exports.sh   (or: make exports)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
BUILD="$ROOT/build/export"
OUT="$ROOT/docs/exports"
MERMAID="$BUILD/mermaid.min.js"
MERMAID_VER="11.6.0"
mkdir -p "$BUILD" "$OUT"

echo "==> [1/5] Branded Word reference"
pandoc --print-default-data-file reference.docx > "$BUILD/reference-base.docx"
python3 tools/export/make_reference.py "$BUILD/reference-base.docx" "$BUILD/reference.docx"

echo "==> [2/5] Combined markdown (Word + HTML variants)"
python3 tools/export/preprocess.py --mode text --out "$BUILD/combined.md"
python3 tools/export/preprocess.py --mode keep --out "$BUILD/combined-mermaid.md"

echo "==> [3/5] Word document"
pandoc "$BUILD/combined.md" --from markdown --toc --toc-depth=1 \
  --reference-doc "$BUILD/reference.docx" \
  -o "$OUT/AutoAgentAI-Documentation.docx"

echo "==> [4/5] Full HTML (for PDF)"
{ echo '<style>'; cat tools/export/pdf.css; echo '</style>'; } > "$BUILD/header.html"
pandoc "$BUILD/combined-mermaid.md" --from markdown --to html5 --standalone \
  --toc --toc-depth=1 --no-highlight \
  --include-in-header "$BUILD/header.html" \
  -o "$BUILD/full.html"

echo "==> [5/5] Full PDF with rendered diagrams"
if [ ! -f "$MERMAID" ]; then
  curl -sSL "https://cdn.jsdelivr.net/npm/mermaid@${MERMAID_VER}/dist/mermaid.min.js" -o "$MERMAID"
fi
node tools/export/render_pdf.js "$BUILD/full.html" "$OUT/AutoAgentAI-Full-Documentation.pdf" "$MERMAID"

# Keep the one-page exec summary alongside the other downloads.
if [ -f "docs/assets/AutoAgentAI-Executive-Summary.pdf" ]; then
  cp -f docs/assets/AutoAgentAI-Executive-Summary.pdf "$OUT/AutoAgentAI-Executive-Summary.pdf"
fi

echo "==> Done. Exports in docs/exports/:"
ls -la "$OUT"
