# AGENTS.md — Job Route engineering and research contract

Scope: **entire repository**. Mission: publish evidence-based, reproducible career route research, not speculative promotion plans.

## 1. Source of truth and change boundaries

- One career = `data/<taxonomy-category>/<kebab-slug>/` containing `route.json`, `report.md`, generated `route.mmd` and `route.svg`.
- `route.json` is the canonical machine-readable graph. Markdown is its documented human interpretation. SVG and Mermaid are deterministic generated artifacts.
- Edit JSON + Markdown, then **regenerate** graphics. Never hand-edit generated files as the source of truth.
- `taxonomy/categories.json` is the canonical category list. Empty categories have READMEs, not dummy route objects.
- Read `schema/career-route.schema.json` before adding fields. Schema changes require migration plan and tests.

## 2. Mandatory evidence workflow

1. **Define the question**: jurisdiction, institution, period, actual target job and population.
2. **Research**: prioritize current statutes, ministry/court/government publications, original recruitment notices, authoritative institutional documents; secondarily reliable media or published case histories. Search for superseding rules.
3. **Cross-check**: confirm effective dates and distinguish official requirements from illustrative sequences and observations. Do not claim unsupported probability or fastest route.
4. **Model**: identify entry nodes, identity milestones, role nodes and target. Label **every edge** normative / official_description / illustrative / conditional. Normative and official_description transitions require source IDs.
5. **Document**: report.md starts with scope + date and **embeds `![...](./route.svg)`**. Explain eligibility, alternatives, institutional decision points, uncertainty and source links.
6. **Validate**: run all commands in Section 4, inspect vector graph and site preview, and give exact result summaries.
7. **Publish via PR**: summarize changes, evidence and test results; never describe Pages deployment as successful until confirmed via Actions and public URL.

## 3. Factual and content safety

- Do not conflate job title, legal office, administrative level, police/military rank, professional grade, salary or employment status.
- A possible path is **not** a mandatory one. Never imply selection, election, promotion, transfer or appointment is guaranteed.
- Cite primary authoritative URLs with titles, publishers, publication dates. Verify source is actually about the claim. Do not invent articles or quotes.
- Old official materials must be labeled historical or subject to current-effectiveness recheck.
- Respect public/private boundaries: do not include personal identifying records, nonpublic HR profiles, internal security arrangements or speculative allegations.
- Do not add secrets, API keys, tracking scripts, opaque remote dependencies or unlicensed imagery.
- Use neutral, factual tone for military, political, legal and judicial careers.

## 4. Quality gates (required on every route PR)

```bash
python -m pip install -r requirements.txt
python scripts/validate.py
node scripts/generate.mjs --write
node scripts/generate.mjs --check
python -m unittest discover -s tests -v
python scripts/build.py
python scripts/smoke.py
git diff --exit-code -- data/
```

`--write` deliberately regenerates generated files; commit generated changes before CI. CI checks drift without modifying tracked source. The dedicated `ci.yml` workflow gates quality independently from `pages.yml` deployment; the latter needs Pages enabled in Settings.

## 5. UI and accessibility

- Responsiveness: desktop + mobile; functional navigation, search and category filtering; accessible focus and labels; semantic heading hierarchy.
- SVG: include `title`, `desc`, text readable without color cues; maintain source and report linkage.
- No runtime network dependency for route data or rendering. The website must work under GitHub project Pages subpath `/job-route/`.
- Each published career must appear automatically in catalog, detail pages, downloadable Mermaid and SVG.

## 6. Required reviewer output

Every PR should state: sources added/checked, jurisdiction and date, schema validity, edge labels, new SVG / report, local tests, Pages workflow result, unresolved uncertainty.
