---
name: guideline-lookup
description: 指南速查——ICU 临床问题快速检索指南共识库，输出带推荐等级和出处页码的推荐意见，并对照国际指南与国内共识差异。查房前、会诊中、家属谈话前使用。
whenToUse: 查房前、会诊中、家属谈话前需要指南推荐意见 + 推荐等级 + 出处时
---

本 skill 的完整流程定义在项目文件 `ima-skills/01-指南速查.md`。**先读取该文件，再严格按其中的适用场景、工作流程、输出格式与安全边界执行。**

本地化适配（正文中「知识库」一词按以下规则理解）：

- 「知识库」指 ima 云端库，通过 `mcp__ima__` 工具访问：先 `list_knowledge_bases_full` 解析目标库（指南共识库 / 药物库 / 文献库）的 cookie_knowledge_base_id，再用 `ask_knowledge_base` 检索，单次只查一个库
- MCP 报 600001（cookie 过期）时：提示用户按 `AGENTS.md` §7 重抓 cookie 并运行 `python3 snippets/update_ima_cookie.py "<新 cookie>"`；在此之前降级为检索本地 `guidelines/` 笔记（Read/Grep），并在输出中声明证据强度降级
- 真实病例资料（即使脱敏）不发送给 ima 工具；凡需向 ima 提问的内容先做 PHI 检查（规则见 `cases/README.md`）
