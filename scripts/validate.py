#!/usr/bin/env python3
"""Strict structural and cross-reference checks for published routes."""
from __future__ import annotations
import json
import pathlib
import sys
from collections import defaultdict
from datetime import date
from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schema/career-route.schema.json").read_text(encoding="utf-8"))
TAXONOMY = json.loads((ROOT / "taxonomy/categories.json").read_text(encoding="utf-8"))
CATEGORIES = {x["id"] for x in TAXONOMY["categories"]}

def load_routes():
    return sorted((ROOT / "data").glob("*/*/route.json"))

def validate_route(file: pathlib.Path) -> list[str]:
    errors = []
    try:
        r = json.loads(file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{file}: invalid JSON: {exc}"]
    validator = Draft202012Validator(SCHEMA, format_checker=FormatChecker())
    for e in validator.iter_errors(r):
        errors.append(f"{file}: schema {'.'.join(map(str,e.path))}: {e.message}")
    if errors:
        return errors
    if r["category"] not in CATEGORIES or file.parent.parent.name != r["category"]:
        errors.append(f"{file}: category must match taxonomy and folder")
    if file.parent.name != r["id"]:
        errors.append(f"{file}: directory must match route id")
    if date.fromisoformat(r["last_verified"]) > date.today():
        errors.append(f"{file}: last_verified must not be in the future")
    nodes = {n["id"]: n for n in r["nodes"]}
    sources = {s["id"] for s in r["sources"]}
    if len(nodes) != len(r["nodes"]):
        errors.append(f"{file}: duplicate node id")
    if len(sources) != len(r["sources"]):
        errors.append(f"{file}: duplicate source id")
    if len({p["id"] for p in r["pathways"]}) != len(r["pathways"]):
        errors.append(f"{file}: duplicate pathway id")
    if r["target"] not in nodes or nodes[r["target"]]["kind"] != "target":
        errors.append(f"{file}: target must identify a target-kind node")
    for entry in r["entry_points"]:
        if entry not in nodes or nodes[entry]["kind"] != "entry":
            errors.append(f"{file}: entry_points reference non-entry: {entry}")
    adjacency = defaultdict(set)
    edge_keys = set()
    for e in r["edges"]:
        pair = (e["from"],e["to"])
        if pair in edge_keys:
            errors.append(f"{file}: duplicate edge {pair}")
        edge_keys.add(pair)
        if e["from"] not in nodes or e["to"] not in nodes:
            errors.append(f"{file}: missing edge node {pair}")
        if e["from"] == e["to"]:
            errors.append(f"{file}: self transition {pair}")
        adjacency[e["from"]].add(e["to"])
        cited = e.get("source_ids",[])
        if e["evidence"] in {"normative","official_description"} and not cited:
            errors.append(f"{file}: {pair} requires a public source")
        if not set(cited).issubset(sources):
            errors.append(f"{file}: missing source in edge {pair}")
    for n in r["nodes"]:
        if not set(n.get("source_ids",[])).issubset(sources):
            errors.append(f"{file}: missing source in node {n['id']}")
    for p in r["pathways"]:
        ids = p["node_ids"]
        if ids[0] not in r["entry_points"]:
            errors.append(f"{file}: pathway {p['id']} must start with an entry")
        if r["target"] not in ids:
            errors.append(f"{file}: pathway {p['id']} never reaches target")
        for a,b in zip(ids,ids[1:]):
            if a not in nodes or b not in adjacency.get(a,set()):
                errors.append(f"{file}: pathway {p['id']} missing edge {a}->{b}")
    report = file.parent / "report.md"
    if not report.is_file():
        errors.append(f"{file}: report.md required")
    else:
        body = report.read_text(encoding="utf-8")
        if "](./route.svg)" not in body:
            errors.append(f"{file}: report.md must embed ./route.svg")
        for s in r["sources"]:
            if s["url"] not in body:
                errors.append(f"{file}: report.md missing cited source {s['id']}")
    return errors

def validate_all() -> list[str]:
    errors = []
    Draft202012Validator.check_schema(SCHEMA)
    paths = load_routes()
    if not paths:
        errors.append("No published route.json files")
    slugs = set()
    for p in paths:
        errors.extend(validate_route(p))
        if p.parent.name in slugs:
            errors.append(f"{p}: duplicate route slug across categories")
        slugs.add(p.parent.name)
    return errors

if __name__ == "__main__":
    problems = validate_all()
    if problems:
        print("\n".join("ERROR: "+x for x in problems),file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {len(load_routes())} published routes, source references, pathways and Markdown SVG links")
