#!/usr/bin/env python3
"""Build a dependency-light, accessible and fully static GitHub Pages site."""
from __future__ import annotations
import html
import json
import pathlib
import shutil
from datetime import date
from urllib.parse import quote
from markdown_it import MarkdownIt
from validate import ROOT, load_routes, validate_all, TAXONOMY

OUT = ROOT / "dist"
BASE = "https://1998x-stack.github.io/job-route/"
md = MarkdownIt("commonmark", {"html": False, "linkify": False}).enable("table")
e = html.escape

def shell(title, description, body, relative="./", extra=""):
    canonical = BASE + ("" if relative == "./" else extra)
    return f"""<!doctype html>
<html lang="zh-CN"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#081d30">
<meta name="description" content="{e(description,quote=True)}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title,quote=True)}">
<meta property="og:description" content="{e(description,quote=True)}">
<link rel="canonical" href="{e(canonical,quote=True)}">
<link rel="stylesheet" href="{relative}assets/style.css">
<title>{e(title)} · Job Route Atlas</title>
</head><body>
<a class="skip" href="#main">跳至正文</a>
<header class="topbar"><div class="wrap nav">
<a class="brand" href="{relative}" aria-label="Job Route 首页"><span class="brand-mark">◈</span><span>JOB<span class="brand-slash">/</span>ROUTE<small>CAREER ATLAS</small></span></a>
<nav aria-label="主导航"><a href="{relative}#routes">路线图谱</a><a href="{relative}#method">研究规范</a><a href="https://github.com/1998x-stack/job-route" target="_blank" rel="noopener noreferrer">GitHub ↗</a></nav>
</div></header>
{body}
<footer class="footer"><div class="wrap footer-inner"><div><strong>◈ JOB / ROUTE</strong><p>把职业发展的可能性，画成可追溯的知识图谱。</p></div><div><span>Evidence-led · Open-source · Versioned</span><p>内容仅用于制度研究，不构成录用或晋升保证。</p></div></div></footer>
</body></html>
"""

def build_index(routes):
    categories = TAXONOMY["categories"]
    cat_names = {c["id"]:c["name"] for c in categories}
    chips = ['<button class="chip active" data-filter="all" aria-pressed="true">全部路线 <span>'+str(len(routes))+'</span></button>']
    for c in categories:
        count = sum(r["category"]==c["id"] for r in routes)
        chips.append(f'<button class="chip" data-filter="{e(c["id"])}" aria-pressed="false">{e(c["name"])} <span>{count}</span></button>')
    cards=[]
    for r in routes:
        slug=e(r["id"],quote=True)
        href=f"./routes/{slug}/"
        cards.append(f"""<article class="route-card" data-card data-category="{e(r['category'],quote=True)}" data-search="{e((r['title']+' '+r['subtitle']+' '+r['summary']+' '+cat_names[r['category']]).lower(),quote=True)}">
<a href="{href}" class="card-hit" aria-label="查看{e(r['title'],quote=True)}"><div class="card-visual"><img src="{href}route.svg" alt="{e(r['title'],quote=True)}的路线缩略图" loading="lazy"></div>
<div class="card-content"><div class="eyebrow"><span class="dot"></span>{e(cat_names[r['category']])}<span class="card-date">{e(r['last_verified'])}</span></div>
<h3>{e(r['title'])}</h3><p>{e(r['summary'])}</p><div class="card-bottom"><span>{len(r['pathways'])} 条路径 · {len(r['sources'])} 项来源</span><span class="arrow">↗</span></div></div></a></article>""")
    body=f"""<main id="main">
<section class="hero"><div class="wrap hero-grid"><div class="hero-text">
<div class="overline"><span class="pulse"></span> OPEN CAREER KNOWLEDGE GRAPH <span class="overline-line"></span> 2026 EDITION</div>
<h1>职业路线，<br><em>不再靠猜。</em></h1>
<p class="lead">从准入资格到岗位转换，从制度规定到真实约束。<br>每条路线都有证据来源，每个箭头都有边界说明。</p>
<div class="hero-actions"><a class="primary-action" href="#routes">探索职业图谱 <span>↗</span></a><a class="secondary-action" href="#method">了解研究标准 ↓</a></div>
</div><div class="hero-panel"><div class="panel-top"><span>PATH INTELLIGENCE / LIVE CATALOG</span><span class="live-indicator">● VERIFIED DATA</span></div>
<div class="panel-graphic"><span class="panel-node p1">ENTRY <b>进入渠道</b></span><span class="panel-line l1"></span><span class="panel-node p2">EXPERIENCE <b>岗位历练</b></span><span class="panel-line l2"></span><span class="panel-node p3">TARGET <b>目标职位</b></span></div>
<div class="panel-bottom"><div><strong>{len(routes):02d}</strong><span>已发布路线</span></div><div><strong>{sum(len(r["pathways"]) for r in routes):02d}</strong><span>研究路径</span></div><div><strong>{len(categories):02d}</strong><span>职业领域</span></div></div></div></div></section>
<section class="catalog wrap" id="routes"><div class="section-top"><div><p class="kicker">01 / ROUTE LIBRARY</p><h2>职业路线图谱<span class="accent-dot">.</span></h2><p>跨越不同制度、行业与人生阶段的公开职业发展研究。</p></div><div class="count" id="result-count" aria-live="polite">显示 {len(routes)} 条路线</div></div>
<div class="search-container"><label for="route-search" class="sr-only">搜索职业、机关或关键词</label><span class="search-icon">⌕</span><input id="route-search" type="search" placeholder="搜索职业、机关、岗位或关键词..." autocomplete="off"><kbd>/</kbd></div>
<div class="chiplist" role="group" aria-label="职业领域筛选">{''.join(chips)}</div>
<div class="card-grid" id="card-grid">{''.join(cards)}</div><div class="no-results" id="no-results" hidden>没有匹配的职业路线。试试其他关键词或分类。</div></section>
<section class="method" id="method"><div class="wrap"><div class="section-top"><div><p class="kicker">02 / THE METHODOLOGY</p><h2>每一条线，都有依据<span class="accent-dot">.</span></h2></div></div>
<div class="method-grid"><article><div class="method-index">01</div><h3>研究先于图形</h3><p>法律法规、官方招录与可靠公开资料优先。注明适用地区、发布日期与核验日期。</p></article><article><div class="method-index">02</div><h3>区分事实与推断</h3><p>法定资格、公开职责、典型经历、条件性交流均有独立证据标签，不以箭头暗示必然晋升。</p></article><article><div class="method-index">03</div><h3>一份数据，多端生成</h3><p>JSON Schema 校验、跨引用审查、Mermaid 与 SVG 由同一份路线数据派生；CI 自动阻止格式漂移。</p></article></div>
<div class="method-foot">建议先看职业路线研究，再打开对应官方来源核验报考年度与地区差异。 <a href="https://github.com/1998x-stack/job-route/blob/main/AGENTS.md">贡献规范 ↗</a></div></div></section>
</main>
<script defer src="./assets/app.js"></script>"""
    return shell("职业发展路线图谱","公开法规、岗位发展与可验证职业路线。",body)

def build_detail(r,category_name):
    route_dir=OUT/"routes"/r["id"]
    route_dir.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(ROOT/"data"/r["category"]/r["id"]/"route.svg",route_dir/"route.svg")
    shutil.copyfile(ROOT/"data"/r["category"]/r["id"]/"route.mmd",route_dir/"route.mmd")
    report=(ROOT/"data"/r["category"]/r["id"]/"report.md").read_text(encoding="utf-8")
    article=md.render(report)
    sources="".join(f'<li><a href="{e(s["url"],quote=True)}" target="_blank" rel="noopener noreferrer">{e(s["title"])} ↗</a><small>{e(s["publisher"])} · {e(s["published"])}</small></li>' for s in r["sources"])
    body=f"""<main id="main" class="detail-page"><div class="wrap">
<div class="breadcrumbs"><a href="../../">全部路线</a><span>/</span><span>{e(category_name)}</span><span>/</span><span>{e(r['title'])}</span></div>
<div class="detail-hero"><span class="detail-overline">CAREER INTELLIGENCE / {e(r['category'].upper())}</span><h1>{e(r['title'])}</h1><p>{e(r['subtitle'])}</p>
<div class="detail-tags"><span>◈ {e(category_name)}</span><span>◷ 核验于 {e(r['last_verified'])}</span><span>◇ {len(r['pathways'])} 条研究路径</span></div>
<div class="detail-links"><a href="./route.svg" target="_blank" rel="noopener">查看完整 SVG ↗</a><a href="./route.mmd" download>下载 Mermaid ↓</a><a href="https://github.com/1998x-stack/job-route/blob/main/data/{e(r['category'])}/{e(r['id'])}/route.json">查看 JSON ↗</a></div></div>
<div class="article-grid"><article class="prose">{article}</article>
<aside class="sidebar"><div class="side-box"><p class="side-overline">RESEARCH FACTS</p><div class="fact-row"><span>适用范围</span><strong>{e(r['jurisdiction'])}</strong></div><div class="fact-row"><span>职业节点</span><strong>{len(r['nodes'])}</strong></div><div class="fact-row"><span>职业路径</span><strong>{len(r['pathways'])}</strong></div><div class="fact-row"><span>资料来源</span><strong>{len(r['sources'])}</strong></div></div>
<div class="side-box"><p class="side-overline">PRIMARY SOURCES</p><ol class="sources">{sources}</ol></div><div class="side-alert">⚑ <strong>职业说明不等于晋升保证。</strong><p>不同地区、部门和年份以官方公告及现行法规为准。</p></div></aside></div>
<div class="back-bottom"><a href="../../#routes">← 返回全部职业路线</a></div></div></main>"""
    (route_dir/"index.html").write_text(shell(r["title"],r["summary"],body,relative="../../",extra=f"routes/{quote(r['id'])}/"),encoding="utf-8")

def main():
    problems=validate_all()
    if problems:
        raise SystemExit("\n".join(problems))
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT/"site/assets",OUT/"assets")
    (OUT/".nojekyll").write_text("",encoding="utf-8")
    routes=[json.loads(p.read_text(encoding="utf-8")) for p in load_routes()]
    cat_names={x["id"]:x["name"] for x in TAXONOMY["categories"]}
    for r in routes:
        for suffix in ("route.svg","route.mmd"):
            if not (ROOT/"data"/r["category"]/r["id"]/suffix).is_file():
                raise SystemExit(f"Generated asset missing: {r['id']}/{suffix}")
        build_detail(r,cat_names[r["category"]])
    (OUT/"index.html").write_text(build_index(routes),encoding="utf-8")
    (OUT/"404.html").write_text(shell("页面未找到","此职业路线尚未发布",'<main id="main" class="wrap notfound"><p class="kicker">404 / NOT FOUND</p><h1>这条路线还没有收录。</h1><p>您可以返回目录浏览已经发布的职业路线。</p><a class="primary-action" href="./">返回目录 ↗</a></main>'),encoding="utf-8")
    (OUT/"robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: "+BASE+"sitemap.xml\n",encoding="utf-8")
    urls=[BASE]+[BASE+"routes/"+quote(r["id"])+"/" for r in routes]
    sitemap='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f"<url><loc>{e(url)}</loc></url>" for url in urls)+"</urlset>"
    (OUT/"sitemap.xml").write_text(sitemap,encoding="utf-8")
    (OUT/"catalog.json").write_text(json.dumps([{"id":r["id"],"title":r["title"],"category":r["category"],"updated":r["last_verified"]} for r in routes],ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"Built {len(routes)} careers in {OUT}")
if __name__ == "__main__":
    main()
