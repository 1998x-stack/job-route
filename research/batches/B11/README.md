# B11 · 第一轮10项职业路线正式研究批次

> **来源清单**：[第二卷职业研究目录](../../backlogs/2026/Job_Route_Careers_Volume_02_2026.md) · 研究日期 **2026-11-11** · 涵盖9大主题分类。

本批次执行仓库 `skills/job-route/SKILL.md`，对原先“逐岗待核验”的10个研究目标完成来源核验与结构化发布。**每项职业都包含：JSON、Markdown研究报告、Mermaid、SVG**，并由站点生成器自动发现。

## 正式交付目录

| Backlog ID | 职业研究目标 | JSON | 研究报告 | Mermaid | SVG |
|:--|:--|:--|:--|:--|:--|
| JR-105 | 军队管理类文职人员 | [route.json](../../../data/military/military-civilian-administrative/route.json) | [report.md](../../../data/military/military-civilian-administrative/report.md) | [route.mmd](../../../data/military/military-civilian-administrative/route.mmd) | [route.svg](../../../data/military/military-civilian-administrative/route.svg) |
| JR-106 | 军队专业技术类文职人员 | [route.json](../../../data/military/military-civilian-technical/route.json) | [report.md](../../../data/military/military-civilian-technical/report.md) | [route.mmd](../../../data/military/military-civilian-technical/route.mmd) | [route.svg](../../../data/military/military-civilian-technical/route.svg) |
| JR-112 | 司法鉴定人 | [route.json](../../../data/judicial/forensic-appraiser/route.json) | [report.md](../../../data/judicial/forensic-appraiser/report.md) | [route.mmd](../../../data/judicial/forensic-appraiser/route.mmd) | [route.svg](../../../data/judicial/forensic-appraiser/route.svg) |
| JR-121 | 街道办事处主任 | [route.json](../../../data/government/subdistrict-office-director/route.json) | [report.md](../../../data/government/subdistrict-office-director/report.md) | [route.mmd](../../../data/government/subdistrict-office-director/route.mmd) | [route.svg](../../../data/government/subdistrict-office-director/route.svg) |
| JR-133 | 公安特警 | [route.json](../../../data/public-safety/police-special-tactics-officer/route.json) | [report.md](../../../data/public-safety/police-special-tactics-officer/report.md) | [route.mmd](../../../data/public-safety/police-special-tactics-officer/route.mmd) | [route.svg](../../../data/public-safety/police-special-tactics-officer/route.svg) |
| JR-143 | 特殊教育学校教师 | [route.json](../../../data/education/special-education-teacher/route.json) | [report.md](../../../data/education/special-education-teacher/report.md) | [route.mmd](../../../data/education/special-education-teacher/route.mmd) | [route.svg](../../../data/education/special-education-teacher/route.svg) |
| JR-154 | 中医执业医师 | [route.json](../../../data/healthcare/traditional-chinese-medicine-physician/route.json) | [report.md](../../../data/healthcare/traditional-chinese-medicine-physician/report.md) | [route.mmd](../../../data/healthcare/traditional-chinese-medicine-physician/route.mmd) | [route.svg](../../../data/healthcare/traditional-chinese-medicine-physician/route.svg) |
| JR-169 | AI智能体应用开发工程师 | [route.json](../../../data/technology/ai-agent-application-engineer/route.json) | [report.md](../../../data/technology/ai-agent-application-engineer/report.md) | [route.mmd](../../../data/technology/ai-agent-application-engineer/route.mmd) | [route.svg](../../../data/technology/ai-agent-application-engineer/route.svg) |
| JR-190 | 人力资源业务伙伴（HRBP） | [route.json](../../../data/business/hr-business-partner/route.json) | [report.md](../../../data/business/hr-business-partner/report.md) | [route.mmd](../../../data/business/hr-business-partner/route.mmd) | [route.svg](../../../data/business/hr-business-partner/route.svg) |
| JR-197 | 儿童福利机构督导员 | [route.json](../../../data/public-service/child-welfare-supervisor/route.json) | [report.md](../../../data/public-service/child-welfare-supervisor/report.md) | [route.mmd](../../../data/public-service/child-welfare-supervisor/route.mmd) | [route.svg](../../../data/public-service/child-welfare-supervisor/route.svg) |

## 证据制度核验的关键判断

- **军队文职**：管理类文员等级、专业技术类岗位等级与现役军官军衔互相独立；按2022年修订文职条例及2027年招考公告建模。
- **司法鉴定人**：需要符合专业条件、机构申请、省级司法行政机关审核登记，不能将医师、刑事技术岗位或学历自动等同于鉴定执业证。
- **街道办主任**：街道办是政府派出机关，地区机构规格与党政职务不同，需经正式干部选任及任命。
- **公安特警**：以实际公务员职位表、专项标准为准；2027北京招录仅作地方实例，不能跨省推断。
- **特教教师**：教师资格与公办学校招聘分别管理，没有全国独立统一“特教教师资格”证书。
- **中医执业医师**：依法取得医师资格，并按照2026年修订注册规则执业；师承／确有专长路径须依独立法定考试和考核条件。
- **AI智能体应用开发**：2026年9月“智能体开发员”已正式发布为**新工种**，而“AI智能体应用开发工程师”是企业岗位名称；不是全国统一法定执业许可。
- **HRBP**：企业职位与国家职业标准中“企业人力资源管理师”并不完全等价。
- **儿童福利机构督导**：MZ/T 167—2021是推荐性行业标准；学历、社工证、儿童社会工作实务和采购项目要求应分别核验。

## 可复现验收

```bash
python -m pip install -r requirements.txt
python scripts/validate.py
node scripts/generate.mjs --check
python -m unittest discover -s tests -v
python scripts/build.py
python scripts/smoke.py
```

### 版本与修订原则

原始 backlog 维持作为候选选题的历史记录；正式研究结果以本表链接的 `route.json` 与 `report.md` 为准。新政策替代原规则时，必须同步更改源链接、数据、Markdown和重生成的图形，不能把“示例路径”解释成必经晋升路线。各职业路径依地区、机构和当年职位公告适用。
