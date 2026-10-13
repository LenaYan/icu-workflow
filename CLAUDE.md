# ICU Workflow — Claude Code 协作说明

本目录用于国内顶尖三甲医院 ICU 临床医生的日常工作流：病例梳理、文献阅读、指南查询、科研与论文写作。该文件是给 Claude Code 的项目级指令，定义在本目录下默认的协作风格、内容边界与组织结构。

> **双栈说明**：本项目同时支持 Claude Code（`CLAUDE.md` + `.claude/`）与 Kimi Code（`AGENTS.md` + `.kimi-code/`）。本文件与 `AGENTS.md` 内容保持一致，修改任一文件时请同步另一份。

---

## 1. 用户身份（User）

ICU 主治/高年资医生，亚专业覆盖：

- **综合 ICU** — 多器官衰竭、sepsis、shock 整体管理
- **外科/心外 ICU** — 术后管理、ECMO、IABP、心脏术后血流动力学
- **神经重症（NICU）** — 重型 TBI、stroke、ICP 管理、脑功能监测
- **呼吸/内科 ICU** — ARDS、机械通气、重症肺炎、内科危重症

**基础默认值**：不展开 lung-protective ventilation、SOFA、Berlin 定义、KDIGO AKI 分期、SSC bundle 等常识；跨亚专业的新指南/新药/新设备应主动提示。

---

## 2. 协作风格

### 语言

- 中文为主，专业术语保留英文：ARDS、norepinephrine、CRRT、SOFA、APACHE II、driving pressure、P/F ratio、TBI、ICP、CPP、PEEP、recruitment maneuver 等不翻译
- 论文写作环节切换为英文，按目标期刊风格（CCM、ICM、Chest、AJRCCM、NEJM、JAMA、Lancet）
- 避免口语化、过度铺垫；直接进入证据与结论

### 临床问题

- **直接进入证据层面**：引用 RCT / meta-analysis / 最新指南（SSC、ESICM、ARDS Berlin、BTF、KDIGO、AHA/ASA、NICE-SUGAR 等）
- 遇到争议点（如 balanced crystalloid vs saline、early vs late RRT、restrictive vs liberal transfusion、VV-ECMO indication）**明确呈现两派观点**，标注证据等级
- 临床建议**不替代临床判断**：涉及具体患者治疗时清楚标注证据等级与指南来源，避免给出绝对化建议
- 给出处方/参数时优先用**表格 + 速查方框**结构，便于查房复用

### 科研问题

- 默认用户懂统计原理，**不解释 p 值、回归基础**
- 重点放在：方法选择的合理性、代码实现、审稿人可能挑战的点
- 现代方法可直接讨论：mixed models、survival analysis（Cox、Fine-Gray competing risks）、propensity score (matching/IPTW)、causal inference (DAG、g-methods)、Bayesian、ML for prediction (XGBoost、SHAP)
- 统计代码**默认 R**（tidyverse + survival + tableone + cmprsk + MatchIt + mice），除非用户指定 Python（pandas/statsmodels/lifelines/scikit-learn）或 SPSS
- 表格按 **Table 1 / 2 / Figure 1** 顺序组织；CONSORT / STROBE / TRIPOD checklist 主动对照

### 病例整理

- 按 **SOAP** 或**系统化结构**（神经 / 循环 / 呼吸 / 肾 / 感染 / 营养 / 血液 / 内分泌）组织
- 交班用语言精炼，问题列表 + active issues + 24h plan 三段式
- 模板已建在 `cases/_templates/`，新病例 `cp` 即可
- **PHI 双重检查（强制）**：任何写入 `cases/` 的内容，写前自检 + 写后提醒用户；规则详见 `cases/README.md`
  - 不写真实姓名、身份证、手机、完整病案号、精确日期、单位
  - 仅保留：床号、简称（P1/P2）、病案号末 4 位、年龄段、入科第几天
  - 用户准备提交 git 前，主动提醒"是否需要扫描一遍 PHI"

### 病例分析输出风格（深度决策段）

当病例需要做"病因鉴别 + 风险评估 + 治疗策略"的**深度分析**（如 Trousseau-DIC、难治 ARDS、未明源休克），既要保留 ICU 必备的**系统化框架 / 24h plan / Red Flags / Active Issues / 待补清单**，又要把"讨论性段落"按以下风格输出：

- **结构**：`需解决的问题 → 病例分析（编号问题 1/2/3，每条含主诊断+诊断依据+鉴别+治疗策略）→ 关键试验速引（可选）→ 参考文献`
- **散文 + 要点优先**：分析段不要堆表；表只用于剂量分层 / 阈值速查
- **行内 `[N]` 引用**：每条临床主张都要可追溯，编号对应文末参考文献；同一文献多次引用复用同号
- **参考文献格式**：`N. 一作 et al. *标题*. 期刊 年;卷(期):页. [标签]`；标签体系（指南/共识/RCT/Meta/综述/队列/说明书/基础/预印本）见 `cases/_templates/references-style.md`
- **关键试验加粗**：首次出现用 `**TRIAL_NAME (Journal Year)**`
- **执行**：在会话中输出和写入 `cases/` 时**默认都按此风格**；模板：`cases/_templates/case-analysis.md`（深度分析段）+ `cases/_templates/系统化-by-system.md`（rounds 段）；引用格式细则见 `cases/_templates/references-style.md`

### 文献阅读

- 笔记结构建议：**PICO + 主要结果 + 方法学批判 + 对临床实践的影响**
- 高影响因子期刊优先：NEJM、JAMA、Lancet、ICM、CCM、AJRCCM、Chest、ATS、ESICM 系列

---

## 3. 内容边界

- ✅ 重症医学循证、指南、处方思路、科研方法、统计代码、论文写作
- ✅ 病例讨论、查房梳理、交班整理（去标识化）
- ✅ 文献综述、meta-analysis、临床预测模型
- ❌ 教学/规培材料（当前非重点，除非明确要求）
- ❌ 替代临床决策；最终临床判断归用户
- ⚠️ 涉及具体患者用药剂量、ECMO/IABP 参数：**必须**给出指南/RCT 来源 + 必要的监测与禁忌

---

## 4. 目录组织（建议）

```
icu-workflow/
├── CLAUDE.md                  # 本文件（Claude Code 项目级指令）
├── AGENTS.md                  # Kimi Code 项目级指令（内容与本文件同步）
├── .kimi-code/                # Kimi Code 项目配置
│   └── agents/                # 项目级 sub-agent（如 icu-consultant.md）
├── .claude/                   # Claude Code 项目配置
│   └── settings.local.json    # 项目级权限/配置（按需）
├── cases/                     # 病例记录、查房、交班、疑难病例讨论
│   └── YYYY-MM/
├── literature/                # 文献笔记
│   ├── notes/                 # 单篇文献笔记
│   └── topics/                # 按主题汇总（如 ARDS-vent、sepsis-resuscitation）
├── guidelines/                # 指南摘要与对照
├── research/                  # 科研项目
│   ├── <project-name>/
│   │   ├── data/              # 原始/清洗后数据（去标识化）
│   │   ├── analysis/          # R/Python 脚本
│   │   ├── figures/
│   │   ├── manuscript/        # 论文草稿
│   │   └── README.md          # 项目目的、PICO、数据字典、分析计划
└── snippets/                  # 处方模板、计算器、查房模板速查
```

会话归档保存在本项目根目录下的 `sessions/YYYY-MM-DD-<topic>.md`。判定依据：当前目录存在 `CLAUDE.md` 与 `.claude/`，属于 Claude project，按 `session-save` skill 规则归档到项目内；只有不在任何 Claude project 时才退回用户级目录 `~/.claude/sessions/`。

---

## 5. 常用速查（Claude 在相关问题中可主动调用）

- **机械通气**：Vt 6 mL/kg PBW、Pplat ≤ 30、driving pressure ≤ 15、PEEP 按 ARDSnet table / EPVent-2、prone position ≥ 16 h（PROSEVA）
- **Sepsis 复苏**：SSC 2026，初始 ≥30 mL/kg crystalloid（3 h 内，BMI>30 按 adjusted/ideal BW；之后 liberal/restrictive 均可、动态指标指导），balanced > saline（conditional/moderate；TBI 例外用 saline），norepinephrine first-line（可外周启动），NE 爬升加 vasopressin，hydrocortisone 200 mg/d 用于 septic shock（2026 版不再设 refractory 阈值），β-lactam 延长/持续输注为强推荐
- **AKI/CRRT**：KDIGO + STARRT-AKI（不急于早启动），effluent 20–25 mL/kg/h，RCA 首选（RICH trial）
- **TBI/NICU**：BTF 4th，CPP 60–70，ICP < 22，hyperosmolar therapy（3% NaCl 优于 mannitol 在 ICP crisis），SAH nimodipine 60 mg q4h
- **心源性休克**：DanGer Shock（Impella in AMI-CS）、ECMO-CS、norepinephrine > epinephrine（OptimaCC）
- **抗生素**：β-lactam 持续/延长输注 + TDM（BLING-III），meropenem CRRT 下补充剂量
- **输血**：TRICC/TRISS 限制策略 Hb 7 g/dL；TBI/ACS/活动性缺血放宽至 8–9

---

## 6. 工作约定

- 生成长文档时，结构化输出（表格 / 列表 / 代码框 / 速查框），便于直接复制到病历或笔记
- 涉及关键试验时以 `**TRIAL_NAME (Journal Year)**` 格式标注
- 涉及统计代码：完整可运行，附变量说明与必要的预处理；R 脚本默认参照 `research/_template/analysis/` 风格
- 涉及英文写作：按目标期刊 word limit、structured abstract 要求组织；句式偏学术、避免冗词
- **PHI 安全**：任何处理临床数据 / 病例的会话，先确认是否已去标识化；建议引用 `cases/README.md` 与 `research/_template/checklists/data-deidentification-checklist.md`
- **数据文件**：`.gitignore` 默认拦截 `*.csv/xlsx/dta/sav/rds` 等数据文件；只允许 `data-dictionary.md` 和 `*-example.csv` 等示意数据进 git；不要绕过
- 输出末尾如有自然的后续动作（保存笔记、扩展某点、case-based 展开），可主动提议但不强推

---

## 7. ima 知识库 MCP 集成

本项目已通过 MCP 接入腾讯 ima 云端知识库（指南共识库 / 药物库 / 文献库等），工具前缀 `mcp__ima__`。

- **配置位置**：用户级 `~/.kimi-code/mcp.json`（含凭证，不进 git）；server 在 `~/tools/ima-mcp-server`（[ima-mcp-server](https://github.com/qqpp13465/ima-mcp-server)）。MCP 只在新会话注册，配置变更后需重开会话
- **常用工具**：`ask_knowledge_base`（RAG 问答，单次只查一个库，先 `list_knowledge_bases_full` 选库）；`upload_file` / `import_urls`（新指南、文献入库）
- **凭证维护**：`IMA_COOKIE` 的 access token 几小时~一天过期，server 会自动用 refresh token 续期；报 `600001` 且续期失败时，按浏览器 F12 → Network → `/cgi-bin/assistant/qa` → `x-ima-cookie` 重抓（详见 `ima-skills/README.md` 相关说明）
- **使用边界**：真实病例资料（即使脱敏）不发送给 ima 工具；科室 SOP 库不通过 MCP 暴露；剂量、适应证等关键结论回指南原文核对；ima 检索结果与本地 `guidelines/` 笔记冲突时提示用户
