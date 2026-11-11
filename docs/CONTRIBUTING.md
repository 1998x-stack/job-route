# Contributing a career route

1. Check `taxonomy/categories.json`. Make one career per directory under `data/<category>/<career-slug>/`.
2. Read `AGENTS.md`, canonical `skills/job-route/SKILL.md` and the research references.
3. Use `python scripts/new_route.py --category <category> --slug <kebab-slug> --title "职业名称"` to start in `drafts/`. Drafts never appear on Pages.
4. Research official sources; replace all `TODO` markers and verify effective dates. Move the complete route directory into `data/` only after meeting the evidence threshold.
5. Run `node scripts/generate.mjs --write` and `python scripts/validate.py`; render site using `python scripts/build.py` and check `python scripts/smoke.py`.
6. Commit JSON, Markdown, Mermaid and SVG together and open a PR describing the source checks, alternatives and uncertainties.

## Review checklist
- [ ] Correct target, jurisdiction, time, institution and population
- [ ] Every normative / official transition cites a genuinely relevant official source
- [ ] No fake percentages, fixed promotion timelines or unsupported legal assertions
- [ ] Distinct ranks, leadership positions and office appointment procedures
- [ ] All pathway edges exist; all source IDs resolve
- [ ] Markdown embeds SVG and links to all source URLs
- [ ] Generator check, semantic validator, unit tests and site smoke test pass
- [ ] SVG, Mermaid, JSON, Markdown all appear in the PR
- [ ] No secrets, sensitive employee details or unlicensed media

## GitHub Pages
On initial setup, enable **Settings → Pages → Build and deployment → Source → GitHub Actions**; this cannot be assumed from merely committing a workflow. `.github/workflows/pages.yml` deploys on main changes. Open `https://1998x-stack.github.io/job-route/` only after successful deployment.
