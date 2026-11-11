# B15 · 10 条职业路线深度调查与发布审计

> **核验日期**：2026-11-11 · 任务源：[Vol 02 研究候选清单](../../backlogs/2026/Job_Route_Careers_Volume_02_2026.md) · **状态**：10项独立研究，待 CI 验收后合并发布

本批次延续 [Job Route SKILL](../../../skills/job-route/SKILL.md)，将十个待研究职业转为正式机器可读证据图谱。每个 `data/<category>/<slug>/` 包含四件套：`route.json` (Schema & sources)、`report.md` (引用SVG)、`route.mmd`、`route.svg`。路径均为条件性示意，不是保证升迁。

## 1. 职业研究目录

| 编号 | 主题 | 岗位 | 数据 | 调研报告 | 矢量图 | Mermaid |
|---|---|---|---|---|---|---|
| JR-102 | military | 海军舰艇指挥军官 | [JSON](../../../data/military/naval-ship-command-officer/route.json) | [Markdown](../../../data/military/naval-ship-command-officer/report.md) | [SVG](../../../data/military/naval-ship-command-officer/route.svg) | [MMD](../../../data/military/naval-ship-command-officer/route.mmd) |
| JR-109 | judicial | 法律援助律师 | [JSON](../../../data/judicial/legal-aid-lawyer/route.json) | [Markdown](../../../data/judicial/legal-aid-lawyer/report.md) | [SVG](../../../data/judicial/legal-aid-lawyer/route.svg) | [MMD](../../../data/judicial/legal-aid-lawyer/route.mmd) |
| JR-124 | government | 县自然资源局局长 | [JSON](../../../data/government/county-natural-resources-director/route.json) | [Markdown](../../../data/government/county-natural-resources-director/report.md) | [SVG](../../../data/government/county-natural-resources-director/route.svg) | [MMD](../../../data/government/county-natural-resources-director/route.mmd) |
| JR-140 | public-safety | 危险化学品安全监管人员 | [JSON](../../../data/public-safety/hazmat-safety-regulator/route.json) | [Markdown](../../../data/public-safety/hazmat-safety-regulator/report.md) | [SVG](../../../data/public-safety/hazmat-safety-regulator/route.svg) | [MMD](../../../data/public-safety/hazmat-safety-regulator/route.mmd) |
| JR-146 | education | 高校实验技术人员 | [JSON](../../../data/education/university-lab-technician/route.json) | [Markdown](../../../data/education/university-lab-technician/report.md) | [SVG](../../../data/education/university-lab-technician/route.svg) | [MMD](../../../data/education/university-lab-technician/route.mmd) |
| JR-148 | education | 高校学院院长 | [JSON](../../../data/education/university-dean/route.json) | [Markdown](../../../data/education/university-dean/report.md) | [SVG](../../../data/education/university-dean/route.svg) | [MMD](../../../data/education/university-dean/route.mmd) |
| JR-162 | healthcare | 公共营养师 | [JSON](../../../data/healthcare/public-nutritionist/route.json) | [Markdown](../../../data/healthcare/public-nutritionist/report.md) | [SVG](../../../data/healthcare/public-nutritionist/route.svg) | [MMD](../../../data/healthcare/public-nutritionist/route.mmd) |
| JR-180 | technology | 储能系统集成工程师 | [JSON](../../../data/technology/energy-storage-systems-engineer/route.json) | [Markdown](../../../data/technology/energy-storage-systems-engineer/report.md) | [SVG](../../../data/technology/energy-storage-systems-engineer/route.svg) | [MMD](../../../data/technology/energy-storage-systems-engineer/route.mmd) |
| JR-189 | business | 用户增长运营负责人 | [JSON](../../../data/business/growth-operations-lead/route.json) | [Markdown](../../../data/business/growth-operations-lead/report.md) | [SVG](../../../data/business/growth-operations-lead/route.svg) | [MMD](../../../data/business/growth-operations-lead/route.mmd) |
| JR-199 | public-service | 自然保护地生态巡护员 | [JSON](../../../data/public-service/protected-area-ranger/route.json) | [Markdown](../../../data/public-service/protected-area-ranger/report.md) | [SVG](../../../data/public-service/protected-area-ranger/route.svg) | [MMD](../../../data/public-service/protected-area-ranger/route.mmd) |

## 2. 法规与官方依据更新矩阵

| 领域 | 核查结果 | 时效与适用范围 | 排除的误解 |
|---|---|---|---|
| 海军舰艇指挥军官 | 国防部2025-2026招生改革；军校士兵招生办法2024生效；大连舰艇学院2026招生 | 按当年地区、院校与培养目标 | 不能用旧“指挥类”标签推断岗位、舰艇类别或军衔 |
| 法律援助律师 | 《律师法》2026年8月第四次修正、《法律援助法》及2023法援办案程序 | 全国法律与特定指派办理规则 | 法律职业资格≠律师执业证，值班律师服务≠自动成为辩护人 |
| 县自然资源局局长 | 2022地方组织法，2026县人大常委会任免与县自然资源职责 | 地区机构规格和干部管理权限 | 专业执业证、土地岗位与部门领导任用是不同资格 |
| 危化品监管人员 | 2025年《危险化学品安全法》，2026-05-01起施行；2026应急检查清单 | 部门分工、执法人员证件及至少两人 | 企业注册安全工程师不自带行政检查权 |
| 高校实验技术人员 | 2021实验技术职称改革、2022北京细则及事业单位招聘 | 事业单位不同岗位聘用 | 正高级实验师、教授和实验中心主任并不等价 |
| 高校学院院长 | 2026修订高校领导人员办法，二级内设负责人按干部权限参照选任；各校章程 | 公办、民办与不同学校章程差异 | 教授资历不保证院长任用，不能把校级领导全部资历机械套用 |
| 公共营养师 | 人社部2021职业技能标准，四级至一级能力体系 | 职业技能评价，不是医疗执照 | 培训/技能证不能替代医生执业资格与临床诊疗权限 |
| 储能系统集成工程师 | GB/T 36558-2023于2024实施；部分DL/T 2026标准至12月26日才生效 | 已发布≠已实施；推荐性国标与技术合同不同 | 储能电站运维管理员≠系统集成工程师；不创造个人职业许可证 |
| 用户增长运营负责人 | 2024正式新职业“用户增长运营师”，2026-04已颁布国家职业标准 | 技能评价与企业聘用分别管理 | 国标职业不等于企业部门负责人行政身份 |
| 自然保护地巡护员 | 2025年《国家公园法》于2026-01施行，2026《自然保护区条例》于03-15施行；地方巡护员劳务制度 | 国家公园、自然保护区、护林员不同制度 | 合同巡护员≠林草行政执法公务员 |

## 3. 研究方法与证据门槛

1. **版本效力优先**：核对通过、发布与生效时间，发现新法时不用旧法取代新法（如2026危化法与2026自然保护区条例）。
2. **身份权责拆分**：报名入口、法定许可、学校/机关聘用、专业技术职称、行政任命独立成节点。
3. **来源分层**：权威法律和主管机关原文为首选；具体学校章程/岗位公告仅支持特定机构的结论。
4. **风险声明**：关于军队、危险化学品和生态保护的研究仅提供职业与合规资料，不提供战术、操作捷径或敏感保护地位置。
5. **可追溯**：引用链接、机构名称及发布日期嵌入每条 `route.json` 和 `report.md`，SVG和Mermaid按 JSON 生成，不手工维护图形。

## 4. 开发与验收

```bash
python -m pip install -r requirements.txt
python scripts/validate.py
node scripts/generate.mjs --check
python -m unittest discover -s tests -v
python scripts/build.py
python scripts/smoke.py
```

CI 成功、合并到 `main` 后由独立 Pages workflow 自动发布。原始 B15 候选清单保持历史不变，以本目录的 manifest 作正式完成的索引。
