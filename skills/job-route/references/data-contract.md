# Data contract / JSON graph model

**Schema**: `schema/career-route.schema.json` (JSON Schema Draft 2020-12; `additionalProperties: false`).

## Field semantics
- `id`: stable kebab-case slug and directory name, unique across all categories.
- `category`: must exist in `taxonomy/categories.json` and match folder.
- `jurisdiction`: geographic and institutional applicability.
- `last_verified`: ISO date when sources were actually checked, not an arbitrary freshness assertion.
- `nodes`: `entry` (legal entrance), `milestone` (identity/training), `role` (position), `target` (focus).
- `edges`: distinct `from` + `to` and explicit `evidence`. Normative / official_description require `source_ids`; illustrative/conditional still need clear notes.
- `pathways`: explicitly enumerated actual edges, start with an `entry_points` element and include `target`.
- `sources`: real public HTTPS URLs and original publication dates.
- `report.md`: must include linked SVG `![...](./route.svg)` and all source URLs.

## Semantic validation beyond JSON Schema
Check duplicate IDs, category, target kind, valid entry kinds, missing graph node references, self edges, duplicated edges, missing source references, missing report, actual path connectivity, target reachability in pathways and cross-career slug collisions.

The YAML/Markdown author must not bypass validation by describing a direct job transfer that has no actual JSON edge. An edge is not equivalent to eligibility; label conditions.

## Regeneration
`node scripts/generate.mjs --write` regenerates deterministic `route.mmd` and `route.svg`. `--check` fails if the committed generated assets differ. `python scripts/build.py` produces fresh HTML under ignored `dist/` directly from published data.
