# Job Route Atlas · 200 Career Research Targets

> Research backlog only — not 200 independently verified career pathways.

| Volume | IDs | Careers | Batches | Word | Markdown | Structured JSON |
|---|---|---:|---|---|---|---|
| 01 · Initial 100 | JR-001—JR-100 | 100 | B01–B10 | [DOCX](Job_Route_Careers_Volume_01_2026.docx) | [MD](Job_Route_Careers_Volume_01_2026.md) | [JSON](volume-01.json) |
| 02 · New 100 | JR-101—JR-200 | 100 | B11–B20 | [DOCX](Job_Route_Careers_Volume_02_2026.docx) | [MD](Job_Route_Careers_Volume_02_2026.md) | [JSON](volume-02.json) |

Both volumes are based on the same nine research categories listed in [taxonomy](../../../taxonomy/categories.json). The second volume is de-duplicated against the first by **role title and stable slug**. The datasets are future production queues, **not** published `route.json` files. A role moves into the website only after it meets [AGENTS.md](../../../AGENTS.md) and [the job-route SKILL](../../../skills/job-route/SKILL.md).

## Publication process

1. Select one batch (10 targets).
2. Search current official source material. Verify institution, eligibility, dates, regulatory effect, location and the exact job.
3. Write a citation-supported `route.json` and `report.md` with a relative SVG embed.
4. Generate Mermaid/SVG through the repository generator.
5. Validate schema, connectivity, citations and diagrams; run unit tests and site smoke tests.
6. Review PR, merge, then confirm CI *and* GitHub Pages separately.

`scripts/build_backlog_docx.py` rebuilds these two Word files from the JSON datasets and verifies Markdown synchronization. [Word-generation workflow](../../../.github/workflows/backlog-word.yml) runs on PRs and, once merged, commits the generated binary files into `main`.

**Evidence standard:** domain-level references are only starting points. They must not be reused as proof of every node or promotion edge. Proposed occupations (notably 2026 public consultation) must stay labeled *proposed* until formally released.

## Local build

```bash
python -m pip install 'python-docx>=1.1,<2'
python scripts/build_backlog_docx.py --check-markdown --output-root research/backlogs/2026
python scripts/build_backlog_docx.py --all --output-root research/backlogs/2026
```
