---
name: drug-dose-check
description: 药物剂量核对——根据药名、肝肾功能、CRRT 模式，从药物库（NMPA 说明书、医保目录、TDM 共识、CRRT 剂量综述）核对负荷量、维持量、剂量调整、TDM 目标与医保类别。开具或核对医嘱时使用。
whenToUse: 开具或核对医嘱，需要按肝肾功能 / CRRT 核对剂量、TDM 目标与医保类别时
---

本 skill 的完整流程定义在项目文件 `ima-skills/02-药物剂量核对.md`。**先读取该文件，再严格按其中的适用场景、工作流程、输出格式与安全边界执行。**

本地化适配（正文中「知识库」一词按以下规则理解）：

- 「知识库」指 ima 云端库，通过 `mcp__ima__` 工具访问，用 `ask_knowledge_base` 检索，单次只查一个库；**目标库的 cookie_knowledge_base_id 直接查 `ima-skills/kb-registry.md`**（剂量类按「医学知识库 → 医院AI药师/药典ima」顺序），不必每次重新 `list_knowledge_bases_full`
- **引用纪律（强制，细则见 `kb-registry.md` 检索总规则）**：剂量（负荷量/维持量/肝肾或 CRRT 调整/TDM 目标）必须原文引用并标注来源；关键数字用 references 中的 `media_id` 调 `get_media_info` 回原文核对，拿不到原文的标注「未核对原文」；禁止凭记忆补剂量
- **双源核对（剂量类强制）**：剂量结论需两个独立来源一致（如 ima 说明书 + 本地 `snippets/` 速查或第二 ima 库）；不一致时并列呈现差异，由用户裁决，不自行二选一
- MCP 报 600001（cookie 过期）时：提示用户按 `AGENTS.md` §7 重抓 cookie 并运行 `python3 snippets/update_ima_cookie.py "<新 cookie>"`；在此之前降级为检索本地 `guidelines/` 笔记（Read/Grep），并在输出中声明证据强度降级
- 真实病例资料（即使脱敏）不发送给 ima 工具；凡需向 ima 提问的内容先做 PHI 检查（规则见 `cases/README.md`）
