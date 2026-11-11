#!/usr/bin/env python3
"""Deterministically publish Job Route research backlogs as Markdown + DOCX.

Run: python scripts/build_backlog_docx.py --all --output-root research/backlogs/2026
Only a research backlog, never emits route.json or falsely publishes pages.
"""
from __future__ import annotations
import argparse
import collections
import json
import re
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

NAVY=RGBColor(14,40,59); TEAL=RGBColor(12,123,113); SLATE=RGBColor(91,108,122)
WHITE=RGBColor(255,255,255)
CATS=['military','judicial','government','public-safety','education','healthcare','technology','business','public-service']
CAT_DESCRIPTIONS={
'military':'区分现役军官、军士与军队文职。军衔、文职等级与工作岗位不能互换。',
'judicial':'区分法律职业资格、执业许可、司法机关辅助人员、企业法务及司法行政岗位。',
'government':'公务员招录、干部组织任用、职务与职级，以及事业单位聘任制度分别说明。',
'public-safety':'公安、海警、海事、消防和司法行政警察属于不同制度体系。',
'education':'教师资格、事业编招聘、职称评聘、高校行政管理各走各的制度。',
'healthcare':'医师资格、执业注册、专业培训、卫生职称和企业岗位不能一概等同。',
'technology':'企业技术职位通常基于技能和成果，并非拥有统一的国家职业资格证即自动晋升。',
'business':'公司内部岗位、执业资格、监管登记和管理授权需要单独建模。',
'public-service':'社会组织、事业单位与合同制服务岗位的雇佣身份存在差异。'}

def font(style,size=9,bold=False,color=NAVY):
    style.font.name='Noto Sans CJK SC'
    style.font.size=Pt(size);style.font.bold=bold;style.font.color.rgb=color
    r=style._element.get_or_add_rPr();rf=r.rFonts
    if rf is None:rf=OxmlElement('w:rFonts');r.insert(0,rf)
    for a in ('ascii','hAnsi','eastAsia','cs'):rf.set(qn('w:'+a),'Noto Sans CJK SC')

def shade(cell,fill):
    tcPr=cell._tc.get_or_add_tcPr();el=OxmlElement('w:shd');el.set(qn('w:fill'),fill);tcPr.append(el)

def nosplit(row,header=False):
    trPr=row._tr.get_or_add_trPr();el=OxmlElement('w:cantSplit');trPr.append(el)
    if header:
        v=OxmlElement('w:tblHeader');v.set(qn('w:val'),'true');trPr.append(v)

def ctxt(cell,text,size=7.65,bold=False,color=NAVY):
    cell.text='';p=cell.paragraphs[0];p.paragraph_format.space_after=Pt(0);p.paragraph_format.line_spacing=1.15
    run=p.add_run(str(text));run.font.name='Noto Sans CJK SC';run.font.size=Pt(size);run.font.bold=bold;run.font.color.rgb=color
    run._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'),'Noto Sans CJK SC')
    cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER

def table(doc,heads,rows,widths,sz=7.65):
    t=doc.add_table(rows=1,cols=len(heads));t.style='Table Grid';t.autofit=False;t.alignment=WD_TABLE_ALIGNMENT.CENTER
    for j,(h,w) in enumerate(zip(heads,widths)):
        t.columns[j].width=Inches(w);c=t.rows[0].cells[j];c.width=Inches(w);shade(c,'133A4A');ctxt(c,h,7.4,True,WHITE)
    nosplit(t.rows[0],True)
    for i,vs in enumerate(rows):
        r=t.add_row();nosplit(r)
        for j,(val,w) in enumerate(zip(vs,widths)):
            c=r.cells[j];c.width=Inches(w);ctxt(c,val,sz,j==0)
            if i%2:shade(c,'F0F7F6')
    doc.add_paragraph().paragraph_format.space_after=Pt(0)
    return t

def link(p,text,url):
    rid=p.part.relate_to(url,'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',is_external=True)
    h=OxmlElement('w:hyperlink');h.set(qn('r:id'),rid)
    run=OxmlElement('w:r');props=OxmlElement('w:rPr')
    col=OxmlElement('w:color');col.set(qn('w:val'),'137F78');props.append(col)
    u=OxmlElement('w:u');u.set(qn('w:val'),'single');props.append(u)
    run.append(props);txt=OxmlElement('w:t');txt.text=text;run.append(txt);h.append(run);p._p.append(h)

def markdown(obj):
    volume=obj['volume'];rs=obj['roles']; sources=obj['sources']; cats=obj['categories']
    p=[]
    p.append(f'# Job Route Atlas — 第{volume}批100种职业发展路线研究目录（2026）')
    p.append('')
    p.append('> **性质**：职业发展研究候选清单／批次生产计划；不是100份已完成的职业路径报告。')
    p.append('> **研究基准**：2026-11-11；以中国大陆为主。后续实际研究须逐岗核对现行法规、地域与机构。')
    p.append(f'> **编号**：{obj["range"]}；本文件与其他批次按 slug 和研究目标去重。')
    p.append('')
    p+=['## 执行摘要','']
    if volume==1:
        p.append('第一批100个研究选题保留原始编号 JR-001—JR-100；包括3个已经在仓库有完整路线的基线案例（部队政委、法院法警、县长），其余需逐岗深研。该目录与原始Word的职业条目、路径草案、分类和批次保持一致。')
    else:
        p.append('第二批100个研究选题使用 JR-101—JR-200，全部与第一批职业标题及唯一slug去重。共有9个分类，分为 B11—B20 共10个可独立执行批次。部分目标是特定组织岗位、专业细分岗位而非《职业分类大典》里的独立职业编码。')
    p+=['','**证据边界**：本目录的“入口候选”“路线草案”和“核验问题”属于预研，不是已完成法定任职资格认定；领域级参考链接仅用于下一轮研究起点，不可直接当作每条晋升箭头的证据。','']
    p+=['## 与国家职业分类体系的关系','']
    p.append('《中华人民共和国职业分类大典（2022年版）》保持八大职业大类、收录1639种职业。Job Route 的九类是研究主题分类，不代表官方职业编码体系。[{}]'.format('R01' if volume==1 else 'S01'))
    p.append('取得职业资格、执业注册、机关招录、职级、职称、企业任命及依法选举属于不同事件；不能互相推断。')
    p+=['','## 九大领域总览','', '| 分类ID | 领域 | 数量 | P0 | P1 | P2 |','|---|---|---:|---:|---:|---:|']
    for c in cats:
        rr=[r for r in rs if r['cat']==c['id']]
        p.append(f'| `{c["id"]}` | {c["name"]} | {len(rr)} | {sum(r["priority"]=="P0" for r in rr)} | {sum(r["priority"]=="P1" for r in rr)} | {sum(r["priority"]=="P2" for r in rr)} |')
    p.append(f'| **合计** | | **{len(rs)}** | **{sum(r["priority"]=="P0" for r in rs)}** | **{sum(r["priority"]=="P1" for r in rs)}** | **{sum(r["priority"]=="P2" for r in rs)}** |')
    p+=['','优先级含义：P0＝入职资格／制度边界优先核验；P1＝标准研究；P2＝行业长尾与高差异岗位研究。它们不代表岗位社会价值、晋升概率或政治评价。','']
    p+=['## 100 个岗位逐项研究目录','']
    for c in cats:
        arr=[r for r in rs if r['cat']==c['id']]
        p+= [f'### {c["name"]}（{len(arr)}项）','',CAT_DESCRIPTIONS[c['id']],'', '| ID / 研究目标 | 入职或进入候选 | 路线草案（示意） | 必须核验 | 排期与参考 |','|---|---|---|---|---|']
        for r in arr:
            title=f'**{r["id"]} {r["title"]}**  `'+r['slug']+'`'
            meta=f'B{r["batch"]:02d} / {r["priority"]} / '+', '.join(r['refs'])
            values=[title,r['entry'],r['route'],r['gate'],meta]
            p.append('| '+' | '.join(x.replace('|','／').replace('\n',' ') for x in values)+' |')
        p+=['','_路线均为供后续核验的示例；缺乏来源时不得直接复制为已发布 route.json。_','']
    p+=['## 批次排期（每批10项）','']
    batches=sorted(set(r['batch'] for r in rs))
    for b in batches:
        rr=[r for r in rs if r['batch']==b]
        p+= [f'### B{b:02d} · {len(rr)}项','']
        p.append('；'.join(f'{r["id"]} {r["title"]}' for r in rr))
        if volume==2:
            p.append('交付策略：先完成条款核验和证据账本；不满足证据阈值的选题保留草稿，由备用选题补位。')
        p+=['']
    p+=['## SKILL 批量生产规范','', '每批从10个目标开始，不应把100个规划条目一次性标记为“已发布”。执行步骤：','']
    p+=['1. 阅读仓库 `AGENTS.md`、`skills/job-route/SKILL.md`、`schema/career-route.schema.json` 与本批 Markdown。',
        '2. 按目标职位确认国家／地区／机构、适用年度、身份类型与职位性质，检索现行官方法规和当年公告。',
        '3. 逐条建立来源账本；标记 `normative`、`official_description`、`illustrative`、`conditional`；证据不足不补造晋升边。',
        '4. 生成 `data/<category>/<slug>/route.json` 与引用 `![路线图](./route.svg)` 的 `report.md`，由生成器派生 `.mmd` 与 `.svg`。',
        '5. 执行 Schema、来源交叉引用、路径连通性、生成漂移、回归测试、站点 smoke test；合格后提 PR。',
        '6. 合并后分别核查 CI 和 Pages 实际状态，报告新增发布数、待复核数、引用来源数、Commit 与 PR URL。','']
    p+=['```bash','python -m pip install -r requirements.txt','node scripts/generate.mjs --write','python scripts/validate.py','node scripts/generate.mjs --check','python -m unittest discover -s tests -v','python scripts/build.py','python scripts/smoke.py','```','']
    p+=['### 可复制的任务 Prompt','', '```text',f'在 1998x-stack/job-route 中处理本目录 B{{BATCH_ID}} 的10个职业目标（第{volume}批研究目录）。',
        '读取 AGENTS.md、SKILL.md、JSON Schema 和对应条目；联网核验现行官方资料，区分国家与地方规定。',
        '每岗输出证据账本、带来源和适用范围的 route.json、Markdown报告、生成的 Mermaid SVG。',
        '禁止编造资格、年龄、转任条件、职称、内部名额、薪酬、成功概率或来源网址。',
        '证据不足的保留 drafts；运行CI全部质量门禁并经PR提交。',
        '报告包括职业清单、具体法规来源、CI结果、Pages上线状态及未验证内容。','```','']
    p+=['## 参考文献与权威检索入口','']
    p.append('以下为领域级起始来源；每个岗位正式发布前必须重新阅读相关条文并确认现行效力：')
    p.append('')
    for s in sources:
        p.append(f'- **[{s["id"]}]** [{s["title"]}]({s["url"]}) — {s["publisher"]}；{s["published"]}。范围：{s["scope"]}。')
    p+=['','## 文档与仓库状态','', '本目录旨在安排待研究职业，不会自动生成网站正式职业条目。请勿将此Markdown放入 `data/*/*/route.json` 以绕开审核。保持结构化名单供后续批次去重和维护。','']
    return '\n'.join(p)

def make_word(obj,out):
    rs=obj['roles'];cats=obj['categories'];sources=obj['sources'];v=obj['volume']
    doc=Document();sec=doc.sections[0]
    sec.page_width=Inches(8.27);sec.page_height=Inches(11.69)
    sec.left_margin=Inches(.66);sec.right_margin=Inches(.66);sec.top_margin=Inches(.68);sec.bottom_margin=Inches(.64)
    sec.header_distance=Inches(.29);sec.footer_distance=Inches(.29);sec.different_first_page_header_footer=True
    font(doc.styles['Normal'],9)
    doc.styles['Normal'].paragraph_format.line_spacing=1.22;doc.styles['Normal'].paragraph_format.space_after=Pt(5)
    for n,size in [('Title',26),('Heading 1',16),('Heading 2',12),('Heading 3',10.4)]:
        st=doc.styles[n];font(st,size,True);st.paragraph_format.space_before=Pt(17);st.paragraph_format.space_after=Pt(8);st.paragraph_format.keep_with_next=True
    for name,size,color,bold in [('Eyebrow',8.2,TEAL,True),('Footnote Meta',7.7,SLATE,False)]:
        if name not in doc.styles:
            st=doc.styles.add_style(name,WD_STYLE_TYPE.PARAGRAPH);font(st,size,bold,color)
            st.paragraph_format.space_after=Pt(3)
    h=sec.header.paragraphs[0];h.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    run=h.add_run(f'◈  JOB ROUTE ATLAS   /   VOLUME {v:02d}   /   100 CAREER BACKLOG')
    run.font.size=Pt(7.5);run.font.bold=True;run.font.color.rgb=SLATE
    f=sec.footer.paragraphs[0];f.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    run=f.add_run(f'RESEARCH BACKLOG / 2026.11  ·  未逐岗完成研究     |     ');run.font.size=Pt(7.0);run.font.color.rgb=SLATE
    fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');f._p.append(fld)
    # cover
    doc.add_paragraph(f'RESEARCH ATLAS   /   SERIES 02   /   VOLUME {v:02d}',style='Eyebrow')
    title=doc.add_paragraph();title.paragraph_format.space_before=Pt(52)
    r=title.add_run(f'100 种职业发展路线\n第{v}批研究目录');r.bold=True;r.font.size=Pt(28);r.font.color.rgb=NAVY
    p=doc.add_paragraph();p.paragraph_format.space_before=Pt(12)
    rr=p.add_run('JOB ROUTE  /  RESEARCH & PUBLICATION BACKLOG');rr.bold=True;rr.font.size=Pt(12);rr.font.color.rgb=TEAL
    doc.add_paragraph('采用仓库九分类体系，逐项登记职业入口候选、路线草案、主要核验问题与未来10批生产安排。')
    for s in [f'文档版本  v2.0    |    研究基准  2026-11-11',f'岗位编号  {obj["range"]}    |    研究范围  中国大陆为主', '交付定位  候选职业研究清单，不是100条已经发布的职业路线']:
        doc.add_paragraph(s,style='Footnote Meta')
    doc.add_paragraph().paragraph_format.space_after=Pt(33)
    nums=[('09','研究领域'),('100','岗位目标'),('10','执行批次'),('27' if v==2 else '24','资料入口')]
    t=doc.add_table(rows=1,cols=4);t.autofit=False
    for j,(n,lab) in enumerate(nums):
        c=t.cell(0,j);shade(c,'E6F4F0');c.text='';p=c.paragraphs[0];p.alignment=WD_ALIGN_PARAGRAPH.CENTER
        r=p.add_run(n);r.bold=True;r.font.size=Pt(23);r.font.color.rgb=TEAL
        q=c.add_paragraph(lab);q.alignment=WD_ALIGN_PARAGRAPH.CENTER;q.runs[0].font.size=Pt(8.5)
    doc.add_paragraph().paragraph_format.space_after=Pt(30)
    doc.add_paragraph('出版原则：真实来源优先；明确职业类别与具体岗位不是同一层级；职业发展“箭头”不是保证录用或晋升。',style='Footnote Meta')
    doc.add_page_break()
    doc.add_heading('执行摘要',1)
    intro= ('本卷保留第一批JR-001—JR-100的全部岗位、候选入口和路线信息，包括政委、法院法警、县长三个已有仓库基线。它是系统化研究排期，不等于全部已经完成逐条法规核验。' if v==1 else '本卷新增JR-101—JR-200共100个独立研究目标，与第一批通过岗位名称和slug双重去重；覆盖9个研究领域，以B11—B20开展每批10项的可控生产。')
    doc.add_paragraph(intro)
    doc.add_paragraph('官方2022版职业分类大典为八大类、1639个职业。仓库九大类是便于研究和网页展示的主题分类；职位、职业和法定执业资格并非一一对应。')
    doc.add_heading('证据等级与发布边界',2)
    table(doc,['对象','研究阶段','发布要求'],[
        ('领域级资料','可确定职业存在性或制度背景','不能支持某一岗位的全部晋升箭头'),
        ('路线草案','入口→经验→任职候选的示意链','需逐条标记evidence、source_ids与条件'),
        ('正式职业页面','可复查的JSON、Markdown、SVG、Mermaid','通过CI且满足来源审核之后才发布')],[1.3,2.55,3.05],8.3)
    doc.add_heading('范围及优先级说明',2)
    for s in ['P0：制度边界与准入核验优先；P1：常规研究；P2：长尾及机构差异大的岗位。此排序不是职业价值或政治人物优劣排名。',
        '涉及考试、执业注册、警衔、军衔、职称、行政职级、领导职务和人大选举时分别建立节点。',
        '本批所有“路线草案”均需后续检索当前生效的主管机关规章和具体地区公告。']:
        p=doc.add_paragraph(style='List Bullet');p.add_run(s)
    doc.add_heading('九大分类与规模',2)
    rows=[]
    for c in cats:
        r=[x for x in rs if x['cat']==c['id']]
        rows.append((c['name'],c['id'],len(r),sum(x['priority']=='P0' for x in r),sum(x['priority']=='P1' for x in r),sum(x['priority']=='P2' for x in r)))
    table(doc,['类别','ID','岗位','P0','P1','P2'],rows,[1.7,1.8,.7,.8,.8,.8],8.2)
    doc.add_heading('100个岗位研究清单',1)
    doc.add_paragraph('以下“路线”是未来研究候选。未核验前不能以实线表达法律上的自动晋升，也不能把领域参考资料误认为逐条岗位资格证据。',style='Footnote Meta')
    for c in cats:
        arr=[x for x in rs if x['cat']==c['id']]
        doc.add_paragraph('CATALOG / '+c['id'].upper(),style='Eyebrow')
        doc.add_heading(f'{c["name"]}  ·  {len(arr)}个研究目标',1)
        doc.add_paragraph(CAT_DESCRIPTIONS[c['id']],style='Footnote Meta')
        rows=[]
        for r in arr:
            rows.append((f'{r["id"]}\n{r["title"]}',r['entry'],r['route'],r['gate'],f'B{r["batch"]:02}\n{r["priority"]}\n'+','.join(r['refs'])))
        table(doc,['ID / 目标','入口候选','路线草案（非必经）','待核验的关键点','批次 / 资料'],rows,[1.37,1.29,1.8,1.60,.83],sz=8.03)
    doc.add_heading('分批生产计划 · 每批10项',1)
    for b in sorted({r['batch'] for r in rs}):
        arr=[r for r in rs if r['batch']==b]
        doc.add_heading(f'B{b:02}  /  {len(arr)}个目标',2)
        doc.add_paragraph('　·　'.join(f'{r["id"]} {r["title"]}' for r in arr))
        doc.add_paragraph('合格交付：每项完成当前证据账本、严格JSON、包含SVG的Markdown、由生成器派生的Mermaid与SVG；PR和CI通过；Pages单独核对。',style='Footnote Meta')
    doc.add_heading('自动化 SKILL 生产契约',1)
    for t in ['阅读AGENTS.md、SKILL.md和schema；选定本卷Bxx共10项，明确国家、地区、部门、目标职位。',
              '逐岗检索官方现行法规、职位公告和资格标准；核对发布日期、是否废止和适用人群。',
              '为每条晋升或岗位转换标记规范性、官方说明、示例或条件性，并绑定真正支持该陈述的来源。',
              'JSON与Markdown为研究交付物；Mermaid和SVG必须从同一JSON自动生成；报告引用相对路径./route.svg。',
              '执行Schema、来源、连通性、图形漂移、回归测试、站点构建和smoke校验；证据不足保留drafts。',
              '合并时报告实际新增发布数量、未解决问题、PR、Commit、CI及Pages状态，不预测个人晋升结果。']:
        p=doc.add_paragraph(style='List Number');p.add_run(t)
    doc.add_heading('可复制的 Agent Prompt',2)
    prompt=(f'在 github.com/1998x-stack/job-route 中，严格按研究规范处理本卷 B{{BATCH_ID}} 的10个职位。\n'
            '研究现行官方法规与当年招聘规则；拒绝虚构资格和快速晋升承诺。\n'
            '输出 route.json、report.md(包含 ./route.svg)、自动生成的 Mermaid 与 SVG。\n'
            '运行全部质量门禁，并通过PR交付；报告实际来源、CI、Pages及未核实事项。')
    p=doc.add_paragraph();p.paragraph_format.left_indent=Inches(.17)
    run=p.add_run(prompt);run.font.size=Pt(8);run.font.name='Noto Sans CJK SC'
    shd=OxmlElement('w:shd');shd.set(qn('w:fill'),'EBF4F2');p._p.get_or_add_pPr().append(shd)
    doc.add_heading('领域级资料入口与法律核验索引',1)
    doc.add_paragraph('以下参考文献只构成未来逐岗研究的起始点。引用到具体职业时，必须再打开原文核对相应事实和现行效力；不支持一条含混“资历→晋升”箭头。')
    for s in sources:
        p=doc.add_paragraph();p.paragraph_format.space_before=Pt(5);p.paragraph_format.space_after=Pt(0)
        rr=p.add_run(f'[{s["id"]}] {s["title"]}');rr.font.bold=True;rr.font.size=Pt(8.9)
        doc.add_paragraph(f'{s["publisher"]} · {s["published"]} · {s["scope"]}',style='Footnote Meta')
        line=doc.add_paragraph(style='Footnote Meta');link(line,'访问原始资料 ↗',s['url'])
    doc.add_heading('结语',1)
    doc.add_paragraph('建议按已定义的10项批次迭代，每次把“可验证职业路线条目”作为验收目标，而不是仅以网页生成数量考核。保持来源覆盖率、图谱连通性、资格边界和事实可追溯性。')
    doc.core_properties.title=f'Job Route Atlas — 第{v}批100种职业发展路线研究目录'
    doc.core_properties.subject='九大分类、100个岗位、10个批次与证据研究规范'
    doc.core_properties.author='Job Route Research'
    doc.core_properties.keywords='Job Route,career atlas,JSON,Mermaid,SVG,SKILL,GitHub'
    doc.core_properties.comments='候选研究目录；非100份已发布正式职业路线。'
    out.parent.mkdir(parents=True,exist_ok=True)
    doc.save(out)
    print('DOCX',out, out.stat().st_size)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output-root',default='research/backlogs/2026')
    ap.add_argument('--all',action='store_true')
    ap.add_argument('--check-markdown',action='store_true')
    args=ap.parse_args()
    root=Path(args.output_root); root.mkdir(parents=True,exist_ok=True)
    datasets=[]
    for v in (1,2):
        p=root/f'volume-0{v}.json';obj=json.loads(p.read_text(encoding='utf-8'))
        assert len(obj['roles'])==100 and len({r['slug'] for r in obj['roles']})==100
        assert all(r['cat'] in CATS for r in obj['roles'])
        assert set(x['id'] for x in obj['sources'])>=set(i for r in obj['roles'] for i in r['refs'])
        assert len({r['id'] for r in obj['roles']})==100
        datasets.append(obj)
    assert not ({r['slug'] for r in datasets[0]['roles']} & {r['slug'] for r in datasets[1]['roles']})
    assert not ({r['title'] for r in datasets[0]['roles']} & {r['title'] for r in datasets[1]['roles']})
    for obj in datasets:
        v=obj['volume'];basename=f'Job_Route_Careers_Volume_0{v}_2026'
        md=root/(basename+'.md');content=markdown(obj)+'\n'
        if args.check_markdown:
            assert md.exists() and md.read_text(encoding='utf-8')==content,f'{md} is out of sync'
        else:
            md.write_text(content,encoding='utf-8')
        if args.all and not args.check_markdown:
            make_word(obj,root/(basename+'.docx'))
        print('MD',md, len(content),'chars')
    print('PASS: 200 total unique roles; nine categories; 20 x 10 planned batches')

if __name__=='__main__':main()