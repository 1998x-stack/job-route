#!/usr/bin/env python3
"""Create a research draft without publishing unverifiable route placeholders."""
import argparse
import json
import pathlib
import re
from validate import ROOT, CATEGORIES

def main():
    p = argparse.ArgumentParser(description="Scaffold an unpublished career research draft")
    p.add_argument("--category", required=True, choices=sorted(CATEGORIES))
    p.add_argument("--slug", required=True)
    p.add_argument("--title", required=True)
    args = p.parse_args()
    if not re.fullmatch(r"[a-z][a-z0-9-]{2,79}", args.slug):
        p.error("slug must be kebab-case, 3-80 chars")
    folder = ROOT / "drafts" / args.category / args.slug
    if folder.exists() or any((ROOT / "data").glob(f"*/{args.slug}/route.json")):
        p.error("career slug already exists as draft or published route")
    folder.mkdir(parents=True)
    data = {
        "_draft_note": "UNPUBLISHED / NOT SCHEMA VALID. Research before moving to data/. Remove this key.",
        "schema_version": "1.0.0",
        "id": args.slug,
        "title": args.title,
        "subtitle": "TODO: precise institution, audience and goal",
        "category": args.category,
        "jurisdiction": "TODO: geographic and institutional scope",
        "last_verified": "YYYY-MM-DD",
        "status": "draft",
        "summary": "TODO: summarize sourced institutional requirements and alternate career routes",
        "target": "target_role",
        "entry_points": ["entry_role"],
        "nodes": [
            {"id": "entry_role", "label": "TODO 入口", "kind": "entry", "description": "TODO: verify legal entry and eligibility"},
            {"id": "target_role", "label": args.title, "kind": "target", "description": "TODO: verify target job and appointment procedure"}
        ],
        "edges": [
            {"from": "entry_role", "to": "target_role", "label": "需核实", "evidence": "conditional", "note": "TODO: verify intermediate roles; this shortcut is a draft placeholder"}
        ],
        "pathways": [{"id": "first_route", "title": "待核实路线", "description": "TODO: research all intermediate steps", "node_ids": ["entry_role", "target_role"]}],
        "requirements": ["TODO: verify current eligibility"],
        "caveats": ["Not published: no evidenced transition yet"],
        "sources": []
    }
    (folder / "route.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (folder / "report.md").write_text(
        f"# {args.title}\n\n> **DRAFT ONLY** · 研究完成前不发布。\n\n![职业路线](./route.svg)\n\n"
        "## 研究范围与核验日期\n\nTODO\n\n## 法定入口与资格\n\nTODO\n\n"
        "## 典型路径和条件限制\n\nTODO\n\n## 官方资料与适用性\n\nTODO\n",
        encoding="utf-8"
    )
    print("Draft created:", folder.relative_to(ROOT))
    print("Research and replace all TODOs, set status=published, remove _draft_note, add official sources,")
    print("then MOVE the folder to data/<category>/<slug>/ and regenerate diagrams.")
if __name__ == "__main__":
    main()
