"""Semantic validator regression cases."""
import json
import pathlib
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/"scripts"))
from validate import ROOT, load_routes, validate_all, validate_route
from smoke import LinkParser

class TestRoutes(unittest.TestCase):
    def test_html_entity_encoded_source_link(self):
        parser = LinkParser()
        parser.feed('<a href="https://example.com/jobs?a=1&amp;b=2">Source</a>')
        self.assertIn("https://example.com/jobs?a=1&b=2", parser.hrefs)

    def test_live_examples(self):
        self.assertEqual(validate_all(),[])
        self.assertGreaterEqual(len(load_routes()),3)

    def test_every_route_has_path_to_target(self):
        for p in load_routes():
            r=json.loads(p.read_text(encoding="utf-8"))
            for way in r["pathways"]:
                self.assertIn(r["target"], way["node_ids"])

    def test_rejects_bad_source_id(self):
        original=load_routes()[0]
        r=json.loads(original.read_text(encoding="utf-8"))
        r["nodes"][0]["source_ids"]=["source_does_not_exist"]
        with tempfile.TemporaryDirectory() as tmp:
            folder=pathlib.Path(tmp)/r["category"]/r["id"]
            folder.mkdir(parents=True)
            target=folder/"route.json"
            target.write_text(json.dumps(r,ensure_ascii=False),encoding="utf-8")
            shutil.copy(original.parent/"report.md",folder/"report.md")
            problems=validate_route(target)
            self.assertTrue(any("missing source" in x for x in problems),problems)

    def test_rejects_unconnected_path(self):
        original=load_routes()[0]
        r=json.loads(original.read_text(encoding="utf-8"))
        r["pathways"][0]["node_ids"]=[r["entry_points"][0],r["target"]]
        with tempfile.TemporaryDirectory() as tmp:
            folder=pathlib.Path(tmp)/r["category"]/r["id"]
            folder.mkdir(parents=True)
            target=folder/"route.json"
            target.write_text(json.dumps(r,ensure_ascii=False),encoding="utf-8")
            shutil.copy(original.parent/"report.md",folder/"report.md")
            problems=validate_route(target)
            self.assertTrue(any("missing edge" in x for x in problems),problems)

if __name__=="__main__":
    unittest.main()
