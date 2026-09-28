# Repository Guidelines

## Project Structure

This directory contains a Dutch-language research dossier about a Semantic Master Data Product for Dutch base registries, organized as Design Science Research.

- `research-design.md`: research questions, conceptual framework, requirements, and evaluation plan.
- `proposed-paper-outline.md`: proposed paper structure; not a completed paper.
- `standards-matrix.csv`: standards, frameworks, versions, scope, and primary sources.
- `literature-matrix.csv`: publications, methods, findings, and evidence limitations.
- `claims-register.csv`: claims, source references, requirements, and proposed tests.

All deliverables currently reside at the root. There are no application sources, test directories, or asset pipelines.

## Development and Validation

No build system, runtime, formatter, or testing framework is configured. Edit the Markdown and CSV files directly. Use `rg 'R17|S33' *.md *.csv` to locate related requirements and sources before making changes.

Check CSV structure with Python's standard library:

```bash
python - <<'PY'
import csv
from pathlib import Path
for path in Path('.').glob('*.csv'):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    assert rows and all(None not in row and
        all(value is not None for value in row.values()) for row in rows)
    print(path.name, len(rows))
PY
```

Also verify unique IDs, resolvable source references, local Markdown links, and agreement between requirements and evaluation tests. No numerical test-coverage target exists.

## Style and Naming

Keep research prose in Dutch, with clear Markdown headings and concise tables. Preserve CSV headers, comma delimiters, quoting, and UTF-8 BOM encoding. Use `csv.DictWriter` for structured edits.

Preserve existing identifiers: `Sxx`, `Lxx`, `C-Sxx`, `C-Lxx`, `Rxx`, `Gxx`, and `Txx`. Add unused IDs; update dependent references together.

## Evidence and Research Boundaries

Cite primary sources for material claims. Record versions, access dates, source locations, and evidence limitations. Distinguish source facts, design inferences, and untested hypotheses. Never invent citations or obligations.

Follow the conceptual distinctions in `research-design.md`. OntoUML is not a Dutch government standard. The prototype is research context, not evidence that an architecture is correct; do not evaluate it or write the full paper without extending the current scope.

## Commits and Pull Requests

No Git repository or commit history is currently available. If version control is introduced, use concise imperative messages such as `Clarify provenance requirements`. Describe changed evidence, affected IDs, validation performed, and remaining uncertainties in each pull request.
