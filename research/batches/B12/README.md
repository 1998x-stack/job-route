# B12 · 新一轮10项职业路线（2026-11-11）

> **状态：published** · 对应第二卷《100个新增岗位目录》的 B12 研究任务，独立于 B11；采用 [job-route SKILL](../../../skills/job-route/SKILL.md)。

本批次将原先候选清单中的10个岗位转成了与仓库现行 Schema 一致的职业研究档案。每个岗位包含一份结构化 JSON、源文件 Mermaid、可访问 SVG 和引用矢量图的 Markdown 报告；用官方资料解释准入制度，所有路径边均为条件性关系，**不代表个人升迁保证**。

## 十项正式职业研究

| ID | 主题 | 岗位 | JSON | 研究报告 | SVG | Mermaid |
|---|---|---|---|---|---|---|
| JR-101 | military | 军队飞行员 | [JSON](../../../data/military/military-pilot/route.json) | [Markdown](../../../data/military/military-pilot/report.md) | [SVG](../../../data/military/military-pilot/route.svg) | [Mermaid](../../../data/military/military-pilot/route.mmd) |
| JR-116 | judicial | 基层法律服务工作者 | [JSON](../../../data/judicial/grassroots-legal-service-worker/route.json) | [Markdown](../../../data/judicial/grassroots-legal-service-worker/report.md) | [SVG](../../../data/judicial/grassroots-legal-service-worker/route.svg) | [Mermaid](../../../data/judicial/grassroots-legal-service-worker/route.mmd) |
| JR-117 | judicial | 行政复议办案人员 | [JSON](../../../data/judicial/administrative-review-officer/route.json) | [Markdown](../../../data/judicial/administrative-review-officer/report.md) | [SVG](../../../data/judicial/administrative-review-officer/route.svg) | [Mermaid](../../../data/judicial/administrative-review-officer/route.mmd) |
| JR-123 | government | 乡镇党委组织委员 | [JSON](../../../data/government/township-organization-committee-member/route.json) | [Markdown](../../../data/government/township-organization-committee-member/report.md) | [SVG](../../../data/government/township-organization-committee-member/route.svg) | [Mermaid](../../../data/government/township-organization-committee-member/route.mmd) |
| JR-142 | public-safety | 司法行政强制隔离戒毒警察 | [JSON](../../../data/public-safety/judicial-detox-police/route.json) | [Markdown](../../../data/public-safety/judicial-detox-police/report.md) | [SVG](../../../data/public-safety/judicial-detox-police/route.svg) | [Mermaid](../../../data/public-safety/judicial-detox-police/route.mmd) |
| JR-145 | education | 国际中文教育教师 | [JSON](../../../data/education/international-chinese-teacher/route.json) | [Markdown](../../../data/education/international-chinese-teacher/report.md) | [SVG](../../../data/education/international-chinese-teacher/route.svg) | [Mermaid](../../../data/education/international-chinese-teacher/route.mmd) |
| JR-166 | healthcare | 医疗器械注册事务专员 | [JSON](../../../data/healthcare/medical-device-regulatory-affairs/route.json) | [Markdown](../../../data/healthcare/medical-device-regulatory-affairs/report.md) | [SVG](../../../data/healthcare/medical-device-regulatory-affairs/route.svg) | [Mermaid](../../../data/healthcare/medical-device-regulatory-affairs/route.mmd) |
| JR-168 | technology | 大模型应用工程师 | [JSON](../../../data/technology/llm-application-engineer/route.json) | [Markdown](../../../data/technology/llm-application-engineer/report.md) | [SVG](../../../data/technology/llm-application-engineer/route.svg) | [Mermaid](../../../data/technology/llm-application-engineer/route.mmd) |
| JR-192 | business | 企业可持续发展经理 | [JSON](../../../data/business/corporate-sustainability-manager/route.json) | [Markdown](../../../data/business/corporate-sustainability-manager/report.md) | [SVG](../../../data/business/corporate-sustainability-manager/route.svg) | [Mermaid](../../../data/business/corporate-sustainability-manager/route.mmd) |
| JR-198 | public-service | 公益基金会项目官员 | [JSON](../../../data/public-service/nonprofit-foundation-program-officer/route.json) | [Markdown](../../../data/public-service/nonprofit-foundation-program-officer/report.md) | [SVG](../../../data/public-service/nonprofit-foundation-program-officer/route.svg) | [Mermaid](../../../data/public-service/nonprofit-foundation-program-officer/route.mmd) |

## 研究关键结论

- **军队飞行员**：2026年度区域空军招飞包含高中毕业生和符合条件的军校应届青年学员；军队岗位、飞行等级、民航执照不是同一事物。
- **基层法律服务**：须有司法行政机关核准的执业证；持法律职业资格的申请渠道不意味着无需实习或无需执业核准。
- **行政复议人员**：2023年修订法第六条明确首次从业须有国家统一法律职业资格并参加职前培训。
- **乡镇党委组织委员**：党委委员的党内选举与其组织工作分工不同，均不能视为公务员职级自动增长。
- **司法行政强制隔离戒毒警察**：江苏2027专项招录条件属于地方年度例子，和法院法警、公安民警不同。
- **国际中文教育教师**：《国际中文教师证书》是能力证明而非国际通用执业许可；2026证书考试仍按具体通知开展。
- **医疗器械注册事务**：医疗器械产品注册人是企业或研制机构等法定主体，员工岗位不等于产品注册责任人。
- **大模型应用**：RAG、工程集成、合规评测是企业能力体系，法律对于向公众提供生成式AI服务有特定适用范围。
- **企业可持续发展经理**：上交所2026披露编制规则针对适用上市公司，不是个人ESG经理执照。
- **基金会项目官员**：基金会法人义务和捐赠项目管理分别处理，普通雇员不因此自动成为理事或法定代表人。

## 再生、校验与交付

```bash
python -m pip install -r requirements.txt
python scripts/validate.py
node scripts/generate.mjs --check
python -m unittest discover -s tests -v
python scripts/build.py
python scripts/smoke.py
```

所有职业数据按 `data/<category>/<slug>/route.json` 自动被站点构建器发现，GitHub Pages 通过主分支 CI 成功后触发独立部署工作流。原始候选 backlog 不覆盖，正式产出以本批次 manifest 和职业目录为准。
