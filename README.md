# ICU Workflow — 工作流入口

> 这是给**人**看的入口文档。AI 协作指令：Claude Code 读 `CLAUDE.md`，Kimi Code 读 `AGENTS.md`（两份内容保持同步）。

---

## 一、目录速览

| 路径 | 用途 | 典型动作 |
|---|---|---|
| `CLAUDE.md` / `AGENTS.md` | 项目级 AI 协作指令（Claude Code / Kimi Code，内容同步） | 协作风格、内容边界 |
| `.claude/settings.local.json` | Claude Code 项目权限白名单 | 已配置 R/Python/git/常用 shell |
| `.kimi-code/agents/` | Kimi Code 项目级 sub-agent（icu-consultant） | 床旁会诊式提问可指定 |
| `cases/_templates/` | 6 个病例模板（SOAP / 系统化 / 交班 / MDT / 死亡讨论 / 转科） | `cp` 即用 |
| `cases/YYYY-MM/` | 病例记录、查房、交班、疑难病例讨论（**严格去标识化**，见 `cases/README.md`） | 新病例按月放 |
| `literature/_templates/` | 3 个文献模板（单篇 PICO / 主题综述 / Journal Club） | 读文献起手 |
| `literature/notes/` | 单篇文献笔记 | |
| `literature/topics/` | 主题汇总 | |
| `guidelines/<topic>/` | **完整循证指南** + 24h 处方模板 + RCT 速查表 | 系统学习 / 查房参考 |
| `snippets/` | **床旁速查** — 阈值、参数、检查清单 | 床旁随手翻 |
| `research/_template/` | **完整科研脚手架**：PICO/数据字典/R 分析全套/Rmd 论文/STROBE-CONSORT-TRIPOD/PHI checklist | `cp -r _template <new-project>` |
| `research/<project>/` | 科研项目 | 论文写作 |
| `.gitignore` | 拦截数据文件 / `.DS_Store` / 中间产物 | 已配置 |

会话归档在本目录 `sessions/YYYY-MM-DD-<topic>.md`（AI 工具的自带会话历史由各自 CLI 管理）。

---

## 二、已有内容（按亚专题）

| 亚专题 | 完整指南 | 床旁速查 |
|---|---|---|
| **CRRT** | `guidelines/CRRT/2026-05-20-CRRT-治疗模式及处方调整.md` | `snippets/CRRT-处方速查.md` |
| **ARDS** | `guidelines/ARDS/ARDS-机械通气与综合管理.md` | `snippets/ARDS-呼吸机速查.md` |
| **Sepsis** | `guidelines/sepsis/Sepsis-识别复苏与抗感染.md` | `snippets/Sepsis-复苏速查.md` |
| **AKI** | `guidelines/AKI/AKI-诊断分期与防治.md` | `snippets/AKI-分期与处置速查.md` |
| **NICU** | `guidelines/NICU/NICU-TBI-SAH-ICH与癫痫管理.md` | `snippets/NICU-神经重症速查.md` |
| **CV / Cardiac** | `guidelines/CV-Cardiac/2026-05-22-心源性休克-ECMO-IABP-Impella.md` | `snippets/ECMO-IABP-速查.md` |

每个指南文件结构统一：定义/分期 → 评估 → 治疗阶梯 → 关键 RCT 证据表 → 24h 处方模板 → 试验速查表。

---

## 三、典型使用场景

### 查房 / 床旁
→ 直接打开对应 `snippets/<topic>速查.md`，看阈值、处方模板、检查清单。

### 系统学习 / 跨亚专业更新
→ 打开 `guidelines/<topic>/` 下完整文档；末尾"关键试验速查表"可快速找证据。

### 整理病例 / 写交班
→ 让 Claude 用 **SOAP** 或**系统化**结构（神经/循环/呼吸/肾/感染/营养/血液/内分泌）梳理；交班三段式（问题列表 + active issues + 24h plan）。

### 读文献
→ 让 Claude 用 **PICO + 主要结果 + 方法学批判 + 对临床影响** 四段式笔记，存到 `literature/notes/`。

### 做研究 / 写论文
→ 在 `research/<project>/` 下分 `data/ analysis/ figures/ manuscript/`；告诉 Claude PICO 与数据字典，统计代码默认 R（tidyverse + survival + tableone + cmprsk + MatchIt + mice）。

### 启动新会话
→ Claude Code 自动读 `CLAUDE.md`；Kimi Code 自动读 `AGENTS.md`（两份内容同步）。新会话直接进入正题即可。

---

## 四、和 Claude 协作的快捷指令

| 想做的事 | 怎么问 |
|---|---|
| 调指南某一节做床旁参考 | "查 ARDS prone 启动指征" |
| 把某话题整理为完整指南 | "按 CRRT/ARDS 那套整理 [话题]" |
| 处理具体患者 | "70 kg 男性，sepsis + ARDS P/F 80，给一份 24h 处方思路" |
| 病例整理 | "按系统化结构梳理这个 case" |
| 读文献 | "按 PICO + 方法学 + 影响整理这篇 [DOI/PMID]" |
| 启动科研项目 | "新研究：PICO 是 …，帮我搭骨架" |
| 保存当前会话 | 直接说"保存会话" |

---

## 五、关键试验快速指针

| 领域 | 必知试验 |
|---|---|
| ARDS | ARMA、PROSEVA、EOLIA、DEXA-ARDS、Amato (ΔP)、ART、FACTT |
| Sepsis | Sepsis-3、SSC 2021、SMART/PLUS/BaSICS、CLASSIC/CLOVERS、ADRENAL/APROCCHSS、LOVIT、ANDROMEDA-SHOCK |
| AKI / CRRT | KDIGO、ELAIN、AKIKI/AKIKI2、IDEAL-ICU、STARRT-AKI、RENAL、ATN、RICH、PRESERVE、AMACING |
| NICU | BTF 4th、SIBICC、PROSEVA-外推、DECRA/RESCUEicp、POLAR、CRASH-3、COBI、INTERACT-2/ATACH-2、ENRICH、ESETT、TTM/TTM2 |
| CV / MCS | SHOCK、SOAP II、IABP-SHOCK II、OptimaCC、DOREMI、CHEETAH、ECMO-CS、ECLS-SHOCK、**DanGer Shock 2024**、EOLIA、CESAR |

---

## 六、扩展建议（按需添加）

### 已完成（2026-05-22 一次扩展）
- ✅ CV/Cardiac 完整指南 + ECMO/IABP/Impella 床旁速查
- ✅ 病例模板 6 套（SOAP / 系统化 / 交班 / MDT / 死亡讨论 / 转科）
- ✅ 文献模板 3 套（单篇 PICO / 主题综述 / Journal Club）
- ✅ research/_template/ 完整脚手架（数据字典 + R 分析全流程 + Rmd 论文 + 报告 checklist）
- ✅ .gitignore + PHI 去标识化规范

### 待补
- **未覆盖亚专题**：营养（NUTRIREA 系列、ESPEN 2023、EFFORT）、Delirium/Sedation（PADIS、MENDS2、SEDCOM）、Endocrine emergencies（DKA、myxedema、adrenal crisis）、Liver failure / ACLF（HRS-AKI、CONFIRM）、抗微生物深化（BLING-III、CRRT 剂量）
- **床旁速查**：床旁公式表（PBW / A-a / FENa / Winters / Henderson）、血管活性药滴定 μg/kg/min ↔ mL/h、抗生素肾功能/CRRT 剂量表、镇静镇痛快表、影像速查 (POCUS RUSH / BLUE / lung US)
- **科研工具**：共享 R 函数库（tableone_helper / psm / competing-risks / forest）、CSL 期刊样式包

需要哪一块直接说，按 CRRT / ARDS / sepsis / CV-Cardiac 那套一致风格补齐。
