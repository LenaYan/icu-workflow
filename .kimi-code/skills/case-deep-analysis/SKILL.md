---
name: case-deep-analysis
description: 深度病例分析编排——对疑难 active issue（未明源休克、出血-血栓两难、难治 ARDS、Trousseau-DIC 等）执行"脱敏确认 → 独立会诊交叉验证 → 模板化深度输出 → 引用核查 → PHI 自检 → 归档"全流程
whenToUse: 某个 active issue 需要病因鉴别 + 风险评估 + 治疗策略的深度讨论时
---

按以下步骤执行，缺步要在输出中说明原因：

1. **脱敏确认**：检查输入是否含 PHI（真实姓名、身份证、手机、完整病案号、精确日期、单位）。若有，先提醒用户并替换为 P1/床号/病案号末 4 位/年龄段/入科第几天；规则见 `cases/README.md`。
2. **独立会诊（疑难病例推荐）**：派 `icu-consultant` sub-agent 做独立评估，与主线分析交叉验证；结论分歧点如实呈现，不和稀泥。
3. **组织输出**：
   - rounds 段按 `cases/_templates/系统化-by-system.md`（神经/循环/呼吸/肾/感染/营养/血液/内分泌）
   - 深度决策段按 `cases/_templates/case-analysis.md`：需解决的问题 → 病例分析（编号问题，每条含最可能诊断 + 诊断依据 + 按可能性排序的鉴别 + 治疗策略分层）→ 关键试验速引表 → 参考文献
   - 风格底线：散文 + 要点，表只用于剂量/阈值速查；每条临床主张带行内 `[N]` 引用；关键试验首次出现用 `**TRIAL_NAME (Journal Year)**`
4. **参考文献**：格式与标签按 `cases/_templates/references-style.md`；同一文献复用同一编号；禁止编造文献与剂量，依赖近期指南或具体剂量时用 WebSearch 核实。
5. **PHI 双重自检**：写入前自检 + 写后提醒用户，逐项过 `case-analysis.md` 末尾清单。
6. **归档**：写入 `cases/YYYY-MM/`（按月目录），文件名体现主题与入科阶段。
