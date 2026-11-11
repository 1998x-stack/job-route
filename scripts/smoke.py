#!/usr/bin/env python3
"""Verify the built site has every route, vector and cited report."""
from __future__ import annotations
import json
from html.parser import HTMLParser
from validate import ROOT, TAXONOMY, load_routes

OUT=ROOT/"dist"

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__();self.hrefs=[];self.images=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=="a" and "href" in d:self.hrefs.append(d["href"])
        if tag=="img" and "src" in d:self.images.append(d["src"])

def check():
    index=(OUT/"index.html").read_text(encoding="utf-8")
    assert "id=\"route-search\"" in index and "data-filter" in index, "search & filters missing"
    assert (OUT/"assets/style.css").stat().st_size>5000, "site stylesheet missing"
    assert (OUT/"assets/app.js").stat().st_size>500, "site interactions missing"
    assert (OUT/".nojekyll").exists(), "missing Pages nojekyll marker"
    assert (OUT/"sitemap.xml").exists(), "missing sitemap"
    names={c["id"] for c in TAXONOMY["categories"]}
    routes=[json.loads(p.read_text(encoding="utf-8")) for p in load_routes()]
    for r in routes:
        assert r["category"] in names
        home=f"./routes/{r['id']}/"
        assert home in index, f"missing card: {r['id']}"
        folder=OUT/"routes"/r["id"]
        detail=(folder/"index.html").read_text(encoding="utf-8")
        parser=LinkParser();parser.feed(detail)
        assert "./route.svg" in parser.images, f"SVG embedded incorrectly in {r['id']}"
        for name in ["route.svg","route.mmd"]:
            assert (folder/name).is_file(), f"missing {r['id']}/{name}"
        svg=(folder/"route.svg").read_text(encoding="utf-8")
        assert svg.startswith("<svg") and "<title" in svg and "<desc" in svg, f"invalid vector in {r['id']}"
        for s in r["sources"]:
            assert s["url"] in parser.hrefs, f"unlinked source {s['id']} in {r['id']}"
    manifest=json.loads((OUT/"catalog.json").read_text(encoding="utf-8"))
    assert len(manifest)==len(routes)
    print(f"PASS: {len(routes)} route pages, navigational cards, accessible SVGs, Mermaid files and source hyperlinks")

if __name__=="__main__":
    check()
