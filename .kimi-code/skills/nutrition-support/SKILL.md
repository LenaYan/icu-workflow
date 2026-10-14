---
name: nutrition-support
description: 营养支持——根据体重、疾病状态与喂养耐受，给出目标热量与蛋白、肠内启动与加量路径、不耐受处理流程和监测方案。入科第 2-3 天启动营养、肠内不耐受时使用。
whenToUse: 启动营养支持、目标热量蛋白计算、肠内不耐受处理时
---

本 skill 的完整流程定义在项目文件 `ima-skills/10-营养支持.md`。**先读取该文件，再严格按其中的适用场景、工作流程、输出格式与安全边界执行。**

本地化适配（正文中「知识库」一词按以下规则理解）：

- 「知识库」指 ima 云端库，通过 `mcp__ima__` 工具访问：先 `list_knowledge_bases_full` 解析目标库（指南共识库 / 药物库 / 文献库）的 cookie_knowledge_base_id，再用 `ask_knowledge_base` 检索，单次只查一个库
- MCP 报 600001（cookie 过期）时：提示用户按 `AGENTS.md` §7 重抓 cookie 并运行 `python3 snippets/update_ima_cookie.py "<新 cookie>"`；在此之前降级为检索本地 `guidelines/` 笔记（Read/Grep），并在输出中声明证据强度降级
- 真实病例资料（即使脱敏）不发送给 ima 工具；凡需向 ima 提问的内容先做 PHI 检查（规则见 `cases/README.md`）
