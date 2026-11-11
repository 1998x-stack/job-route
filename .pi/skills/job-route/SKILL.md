---
name: job-route
description: Research and publish a verified career development route as structured JSON, Mermaid, SVG and a sourced Markdown report in the Job Route Atlas repository.
---

# Job Route — Evidence-grounded career route authoring

## When to use
Use when someone asks **how to become a specific professional**, grow into a leadership role, compare job entry pathways, or create/update a career route in `1998x-stack/job-route`. Read root `AGENTS.md` first and follow its constraints.

## Required output contract
For each accepted career, deliver a complete folder:
- `data/<category>/<slug>/route.json` — strict JSON Schema Draft 2020-12 and semantic graph.
- `data/<category>/<slug>/report.md` — professional, sourced and time-scoped research, embedding `![职业路线](./route.svg)`.
- `data/<category>/<slug>/route.mmd` — automatically generated Mermaid graph.
- `data/<category>/<slug>/route.svg` — automatically generated accessible vector diagram.
- GitHub Pages catalog/detail routes should discover them from data automatically.

## Execution procedure
1. **Scope the career**: target role, country/jurisdiction, year, institution, entry population; distinguish closely related titles. Search web for *current* official documents and any superseding policies; record precise URLs, title, publisher, publication/effective date.
2. **Build an evidence ledger**: each key requirement or public institutional fact → source ID and supporting section; separate binding qualifications from organizational descriptions, typical biographies and conditional transitions.
3. **Research alternate routes**: different legal entry mechanisms, geographic/agency limitations, necessary qualifications, exams or selections, intermediate roles, possible transfers and downstream appointment/election. Never invent missing internal rules.
4. **Construct route.json**: use `schema/career-route.schema.json`; all IDs stable snake_case, slug kebab-case, `entry_points` marked as entry, single target marked target, pathways are chains of actual graph edges reaching target, sources referenced by IDs. Declare evidence for every edge.
5. **Draft report.md**: scope + verification date, SVG embed near top, position definition, entry paths, role descriptions, eligibility and decision mechanisms, institutional differences, caveats, numbered official hyperlinks. Claims must agree with route.json.
6. **Generate and verify**:
   ```bash
   python -m pip install -r requirements.txt
   python scripts/validate.py
   node scripts/generate.mjs --write
   node scripts/generate.mjs --check
   python -m unittest discover -s tests -v
   python scripts/build.py
   python scripts/smoke.py
   ```
   Re-run `python scripts/validate.py` after final editing.
7. **Inspect and deliver**: verify mobile/desktop site, all routes show, SVG is genuine vector, Markdown links resolve, cite changes with commit/PR URLs; CI and public Pages must be separately checked. Provide limitations rather than claimed success without evidence.

## Research guardrails
- **Normative** = exact legal / binding regulatory statement with cited source.
- **Official description** = supported by official institution, not necessarily a universal rule.
- **Illustrative** = a useful example, not a required step.
- **Conditional** = eligible only if selection/appointment/transfer requirements are satisfied.
- Avoid fabricating source URLs, eligibility ages, insider criteria, promotion times, success rates or guaranteed outcomes.
- A **rank**, **title**, **office**, **employment identity** and **civil-service grade** are not interchangeable.
- Explicitly mark older normative texts for current-validity verification. No secret data or speculative allegations.
- If no credible source is available, keep the work as a draft; do not publish invented route nodes.

## On-demand supporting material
Read as needed:
- `skills/job-route/references/research-method.md`: source ranking, conflict resolution and evidence ledger.
- `skills/job-route/references/data-contract.md`: JSON, edges and semantic model.
- `skills/job-route/references/visual-publication.md`: diagram, accessibility, UI, CI/Pages publishing.

## Example invocation
“请研究中国大陆『如何在部队担任政治委员』的典型职业方向，调查最新官方法规和招录制度；按 Job Route Schema 生成 JSON 与 Markdown，并由生成器输出 Mermaid / SVG；运行校验和静态站点构建，提交可审核 PR。”

The SKILL is a procedure, not a claim of tool access. Only publish through actual available GitHub tools.
