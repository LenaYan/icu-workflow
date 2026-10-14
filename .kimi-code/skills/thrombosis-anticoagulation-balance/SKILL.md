---
name: thrombosis-anticoagulation-balance
description: 血栓与抗凝平衡——结构化评估血栓风险与出血风险，给出 VTE 预防/治疗策略、药物与剂量、术后或脑出血后重启抗凝时机及逆转方案。抗凝决策与权衡时使用。
whenToUse: 抗凝决策、血栓与出血风险权衡、术后 / 脑出血后重启抗凝时机判断时
---

本 skill 的完整流程定义在项目文件 `ima-skills/11-血栓与抗凝平衡.md`。**先读取该文件，再严格按其中的适用场景、工作流程、输出格式与安全边界执行。**

本地化适配（正文中「知识库」一词按以下规则理解）：

- 「知识库」指 ima 云端库，通过 `mcp__ima__` 工具访问：先 `list_knowledge_bases_full` 解析目标库（指南共识库 / 药物库 / 文献库）的 cookie_knowledge_base_id，再用 `ask_knowledge_base` 检索，单次只查一个库
- MCP 报 600001（cookie 过期）时：提示用户按 `AGENTS.md` §7 重抓 cookie 并运行 `python3 snippets/update_ima_cookie.py "<新 cookie>"`；在此之前降级为检索本地 `guidelines/` 笔记（Read/Grep），并在输出中声明证据强度降级
- 真实病例资料（即使脱敏）不发送给 ima 工具；凡需向 ima 提问的内容先做 PHI 检查（规则见 `cases/README.md`）
