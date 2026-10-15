---
name: rounds-handover
description: 查房与交班编排——把查房信息整理为系统化 rounds 笔记或 SOAP 病程，并生成"问题列表 + active issues + 24h plan"三段式交班
whenToUse: 日常查房梳理、交接班、夜班 handover 时
---

1. **脱敏确认**：检查输入 PHI，规则见 `cases/README.md`；发现问题先提醒再处理。
2. **rounds 笔记**：默认按 `cases/_templates/系统化-by-system.md`（神经/循环/呼吸/肾/感染/营养/血液/内分泌）；用户要求 SOAP 时改用 `cases/_templates/SOAP.md`。
3. **交班三段式**：按 `cases/_templates/handover-3段.md` 组织——问题列表 → active issues → 24h plan；语言精炼到可口头交接，每项 plan 可执行、有监测点。
4. **参数与医嘱核对**：呼吸机 / CRRT / 血管活性药 / 镇静等参数优先对照 `snippets/` 速查框；剂量结论给指南或说明书来源，高警示药品标注双人核对。
5. **PHI 自检 + 归档**：写入 `cases/YYYY-MM/`（文件名用 `P<N>-<病种>-D<N>-<主题>`，禁止精确日期）；写后提醒用户提交 git 前可再扫一遍 PHI。
