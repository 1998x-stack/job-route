# B14｜10种职业路线深度调查与可复现发布

> 核验于 2026-11-11 · 从 [Volume 02 Backlog](../../backlogs/2026/Job_Route_Careers_Volume_02_2026.md) 选定的 B14 批次 · 10 职业 × 4 可视化研究交付物

本批次比 B11—B13 更强调 **证据效力、条文时间版本、职业名称是否为法定资格、政府部门机构隶属以及招聘实例的地区边界**。职业路线图为**条件性示意**，不是对某个人的任用承诺。

## 一、职业目录

| ID | 类别 | 研究对象 | JSON | 报告 | SVG | Mermaid |
|---|---|---|---|---|---|---|
| JR-107 | military | 军队院校文职教员 | [JSON](../../../data/military/military-academy-civilian-instructor/route.json) | [Markdown](../../../data/military/military-academy-civilian-instructor/report.md) | [SVG](../../../data/military/military-academy-civilian-instructor/route.svg) | [MMD](../../../data/military/military-academy-civilian-instructor/route.mmd) |
| JR-110 | judicial | 企业法务经理 | [JSON](../../../data/judicial/corporate-legal-manager/route.json) | [Markdown](../../../data/judicial/corporate-legal-manager/report.md) | [SVG](../../../data/judicial/corporate-legal-manager/route.svg) | [MMD](../../../data/judicial/corporate-legal-manager/route.mmd) |
| JR-125 | government | 县教育局局长 | [JSON](../../../data/government/county-education-director/route.json) | [Markdown](../../../data/government/county-education-director/report.md) | [SVG](../../../data/government/county-education-director/route.svg) | [MMD](../../../data/government/county-education-director/route.mmd) |
| JR-134 | public-safety | 公安网络安全执法民警 | [JSON](../../../data/public-safety/cybercrime-enforcement-police/route.json) | [Markdown](../../../data/public-safety/cybercrime-enforcement-police/report.md) | [SVG](../../../data/public-safety/cybercrime-enforcement-police/route.svg) | [MMD](../../../data/public-safety/cybercrime-enforcement-police/route.mmd) |
| JR-135 | public-safety | 公安出入境管理民警 | [JSON](../../../data/public-safety/immigration-management-police/route.json) | [Markdown](../../../data/public-safety/immigration-management-police/report.md) | [SVG](../../../data/public-safety/immigration-management-police/route.svg) | [MMD](../../../data/public-safety/immigration-management-police/route.mmd) |
| JR-144 | education | 职业院校实训指导教师 | [JSON](../../../data/education/vocational-practice-instructor/route.json) | [Markdown](../../../data/education/vocational-practice-instructor/report.md) | [SVG](../../../data/education/vocational-practice-instructor/route.svg) | [MMD](../../../data/education/vocational-practice-instructor/route.mmd) |
| JR-160 | healthcare | 专科护士 | [JSON](../../../data/healthcare/specialist-nurse/route.json) | [Markdown](../../../data/healthcare/specialist-nurse/report.md) | [SVG](../../../data/healthcare/specialist-nurse/route.svg) | [MMD](../../../data/healthcare/specialist-nurse/route.mmd) |
| JR-167 | technology | 云平台工程师 | [JSON](../../../data/technology/cloud-platform-engineer/route.json) | [Markdown](../../../data/technology/cloud-platform-engineer/report.md) | [SVG](../../../data/technology/cloud-platform-engineer/route.svg) | [MMD](../../../data/technology/cloud-platform-engineer/route.mmd) |
| JR-184 | business | 商业数据分析师 | [JSON](../../../data/business/business-intelligence-analyst/route.json) | [Markdown](../../../data/business/business-intelligence-analyst/report.md) | [SVG](../../../data/business/business-intelligence-analyst/route.svg) | [MMD](../../../data/business/business-intelligence-analyst/route.mmd) |
| JR-196 | public-service | 残疾人就业辅导员 | [JSON](../../../data/public-service/disability-employment-counselor/route.json) | [Markdown](../../../data/public-service/disability-employment-counselor/report.md) | [SVG](../../../data/public-service/disability-employment-counselor/route.svg) | [MMD](../../../data/public-service/disability-employment-counselor/route.mmd) |

## 二、深搜证据审计结论

| 课题 | 关键来源 | 生效或发布边界 | 需要避免的误读 |
|---|---|---|---|
| 军校文职教员 | 国防部《文职人员条例》、军队人才网2027招考公告 | 2023年1月生效；2026年11月4日发布招考公告 | 军官与文职、文员等级与专业技术岗位等级不同 |
| 企业法务经理 | 人社部等三部门2014年通知、海尔2026年公开招聘 | 2014年已取消企业法律顾问准入类职业资格 | 法务经理不是法定执业证，企业岗位条件不全国通用 |
| 县教育局局长 | 2022年地方组织法、2019年干部选任条例 | 部门局长由县长提名、人大常委会任命 | 不能把校长职称或教师资格当作直接升任局长的资格 |
| 公安网安民警 | 山东、北京2027年度人民警察职位公告 | 2026年11月地方年度招录资料 | 技术证书不是公安民警身份，省份条件不能互换 |
| 公安出入境民警 | 出境入境管理法、国家移民管理局2027年度公告 | 2013年实施法律；2018年机构改革后 | 地方公安出入境业务与国家移民局垂管边检系统不可混同 |
| 职业学校实训教师 | 教师资格条例、2022年职业教育法及双师型标准 | 适用中职和高职需分别判定教师资格类别 | 双师型评价不是替代教师资格的执照 |
| 专科护士 | 护士条例、2021修订注册办法、2026地区培训 | 专业培训有地区和专科差异 | 地方培训年限并非全国统一，专科证书非独立护士执照 |
| 云平台工程师 | 人社部2019职业定义与2021技术技能标准 | 云计算工程技术人员职业编码2-02-10-12 | 职业标准、厂商认证与企业职位不互相自动替代 |
| 商业数据分析师 | 2024年人社部与商务部职业标准 | 商务数据分析师编码4-07-02-05 | 商务职业技能等级不等于企业BI Manager领导职务 |
| 残疾人就业辅导员 | 国办2025—2027行动方案、2026残疾人事业规划 | 鼓励各地建设专业服务队伍 | 就业辅导员非统一临床心理师执照或公务员身份 |

## 三、证据分级与限界

- **法律、行政法规和现行部门规章**：用于界定法定资格、权责与任命程序，需核对修订时间及适用范围。
- **官方年度岗位公告**：仅支持所标年度、地域、院校或企业用人条件，不推广为全国要求。
- **国家职业技术/技能标准**：提供职业活动与评价框架，不自动代表企业具体任职职级。
- **企业与行业实例**：支持工作内容与可能职业经历，不作为法定强制入职资格。
- **所有路线边**：均使用 `conditional`，需独立满足资格、岗位空缺或聘任要求。

## 四、质量门禁

```bash
python -m pip install -r requirements.txt
python scripts/validate.py
node scripts/generate.mjs --check
python -m unittest discover -s tests -v
python scripts/build.py
python scripts/smoke.py
```

合并到 main 后由独立的 Pages 工作流发布。下一次政策替代或招聘年度变化时，应同步更新 `route.json` 与 `report.md`、重生成 Mermaid/SVG 并重新执行上述校验。
