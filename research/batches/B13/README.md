# B13｜职业研究与发布验收索引

> **状态**：10 项完成研究并转入职业图谱 · 2026-11-11。对应 [Volume 02 backlog](../../backlogs/2026/Job_Route_Careers_Volume_02_2026.md)。

本轮依据 `skills/job-route/SKILL.md`，从官方法律、主管部门文件、标准平台和公开雇主职位示例核查职业入口与适用制度，生成与仓库 JSON Schema 兼容的职业数据、Mermaid、SVG 和引用 SVG 的 Markdown 报告。**职业箭头均是条件性路径，不是保证晋升。**

## B13 全部职业目录

| 编号 | 领域 | 职业 | 结构化数据 | 研究报告 | Mermaid | SVG |
|:--|:--|:--|:--|:--|:--|:--|
| JR-104 | military | 军队医疗岗位军医 | [JSON](../../../data/military/military-physician/route.json) | [Markdown](../../../data/military/military-physician/report.md) | [MMD](../../../data/military/military-physician/route.mmd) | [SVG](../../../data/military/military-physician/route.svg) |
| JR-111 | judicial | 企业合规经理 | [JSON](../../../data/judicial/corporate-compliance-manager/route.json) | [Markdown](../../../data/judicial/corporate-compliance-manager/report.md) | [MMD](../../../data/judicial/corporate-compliance-manager/route.mmd) | [SVG](../../../data/judicial/corporate-compliance-manager/route.svg) |
| JR-126 | government | 县卫生健康局局长 | [JSON](../../../data/government/county-health-commission-director/route.json) | [Markdown](../../../data/government/county-health-commission-director/report.md) | [MMD](../../../data/government/county-health-commission-director/route.mmd) | [SVG](../../../data/government/county-health-commission-director/route.svg) |
| JR-128 | government | 人社部门公务员 | [JSON](../../../data/government/human-resources-government-officer/route.json) | [Markdown](../../../data/government/human-resources-government-officer/report.md) | [MMD](../../../data/government/human-resources-government-officer/route.mmd) | [SVG](../../../data/government/human-resources-government-officer/route.svg) |
| JR-139 | public-safety | 消防监督执法人员 | [JSON](../../../data/public-safety/fire-prevention-enforcement-officer/route.json) | [Markdown](../../../data/public-safety/fire-prevention-enforcement-officer/report.md) | [MMD](../../../data/public-safety/fire-prevention-enforcement-officer/route.mmd) | [SVG](../../../data/public-safety/fire-prevention-enforcement-officer/route.svg) |
| JR-150 | education | 学科竞赛指导教师 | [JSON](../../../data/education/subject-competition-coach/route.json) | [Markdown](../../../data/education/subject-competition-coach/report.md) | [MMD](../../../data/education/subject-competition-coach/route.mmd) | [SVG](../../../data/education/subject-competition-coach/route.svg) |
| JR-155 | healthcare | 口腔执业医师 | [JSON](../../../data/healthcare/dentist-physician/route.json) | [Markdown](../../../data/healthcare/dentist-physician/report.md) | [MMD](../../../data/healthcare/dentist-physician/route.mmd) | [SVG](../../../data/healthcare/dentist-physician/route.svg) |
| JR-178 | technology | FPGA逻辑设计工程师 | [JSON](../../../data/technology/fpga-design-engineer/route.json) | [Markdown](../../../data/technology/fpga-design-engineer/report.md) | [MMD](../../../data/technology/fpga-design-engineer/route.mmd) | [SVG](../../../data/technology/fpga-design-engineer/route.svg) |
| JR-185 | business | 供应链规划经理 | [JSON](../../../data/business/supply-chain-planning-manager/route.json) | [Markdown](../../../data/business/supply-chain-planning-manager/report.md) | [MMD](../../../data/business/supply-chain-planning-manager/route.mmd) | [SVG](../../../data/business/supply-chain-planning-manager/route.svg) |
| JR-195 | public-service | 社区养老服务运营主管 | [JSON](../../../data/public-service/community-eldercare-operations-lead/route.json) | [Markdown](../../../data/public-service/community-eldercare-operations-lead/report.md) | [MMD](../../../data/public-service/community-eldercare-operations-lead/route.mmd) | [SVG](../../../data/public-service/community-eldercare-operations-lead/route.svg) |

## 制度研究要点

- **军队医疗岗位**：2027军医院直招军官与2026医师资格考试及执业注册分属不同流程。军官、文职和医师执业资格不可直接互换；不把2000年的历史注册机构名称当成2026年现行内部程序。
- **企业合规**：国资委中央企业规章与通用推荐性GB/T标准分别建模；企业合规经理不等于统一法定执业证。
- **县卫健局局长**：干部选拔与本级人大常委会任命分开，不以医生证书直接替代公务员领导任用。
- **人社公务员**：行政机关、社保经办事业单位和企业HRBP身份分别识别。
- **消防监督**：法定监督检查需合法机构身份、消防执法岗位和行政执法证件；不能向第三方机构外包行政检查。
- **竞赛教师**：教师资格、学校聘用与竞赛指导能力不等同；教育部2025—2028学年赛事清单必须遵守。
- **口腔医师**：按医师资格考试、资格取得、2026年修订注册办法逐步区分，与牙科技工不同。
- **FPGA工程**：RTL开发、功能验证、综合时序和板级调试由具体企业岗位资料支持，不宣称存在统一法定执业许可。
- **供应链规划**：以公开招聘资料区分S&OP、需求预测、库存计划和企业经理职位。
- **社区养老运营**：2026年养老服务师是水平评价类职业资格，与社区养老项目运营主管的雇主任用独立。

## 完整质量门禁

```bash
python -m pip install -r requirements.txt
python scripts/validate.py
node scripts/generate.mjs --check
python -m unittest discover -s tests -v
python scripts/build.py
python scripts/smoke.py
```

站点从 `data/*/*/route.json` 自动发现新增路线；本批次 `manifest.json` 是审计清单，不覆盖原候选 backlog。所有最新职位要求仍以正式当年公告为准。
