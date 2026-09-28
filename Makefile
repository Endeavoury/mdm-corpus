TECTONIC ?= tectonic
.PHONY: all prepare audit clean
all: prepare
	$(TECTONIC) -k --keep-logs paper.tex
	python scripts/audit_paper.py
prepare:
	python scripts/prepare_paper.py
	python review/finish_review_artifacts.py
audit:
	python scripts/audit_paper.py
clean:
	rm -f paper.aux paper.bbl paper.blg paper.log paper.out paper.toc paper.synctex.gz
