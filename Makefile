.PHONY: help serve build exports count clean

help:
	@echo "AutoAgentAI docs — make targets:"
	@echo "  make serve    - live-preview the docs site (mkdocs serve)"
	@echo "  make build    - build the static site into ./site"
	@echo "  make exports  - build docs/exports/ (Word .docx + full PDF with diagrams)"
	@echo "  make count    - word & line counts for the docs"
	@echo "  make clean    - remove build artifacts (site/, build/)"

serve:
	mkdocs serve

build:
	mkdocs build --strict

exports:
	bash tools/build-exports.sh

count:
	@echo "Per-file (words):"
	@find docs -name '*.md' | sort | while read -r f; do \
		printf "  %6s  %s\n" "$$(wc -w < "$$f")" "$$f"; done
	@printf "TOTAL: %s words across %s pages\n" \
		"$$(find docs -name '*.md' | xargs cat | wc -w)" \
		"$$(find docs -name '*.md' | wc -l)"

clean:
	rm -rf site build
