---
name: deidentify-evidence-search
description: 去标识化 + 循证检索——双功能：含 PHI 的病历文本脱敏为 P1/床号格式后可安全上传云端；临床问题转 PICO 后检索指南库，按证据金字塔分级输出带推荐等级的答案。上传病历前脱敏、快速拉证据时使用。
whenToUse: 病历文本上传云端前需要脱敏，或临床问题需要转 PICO 快速检索分级证据时
---

本 skill 的完整流程定义在项目文件 `ima-skills/13-去标识化与循证检索.md`。**先读取该文件，再严格按其中的适用场景、工作流程、输出格式与安全边界执行。**

本地化适配（正文中「知识库」一词按以下规则理解）：

- 脱敏规则与 `cases/README.md` 保持一致：仅保留床号、简称（P1/P2）、病案号末 4 位、年龄段、入科第几天
- 「知识库」指 ima 云端库，通过 `mcp__ima__` 工具访问：先 `list_knowledge_bases_full` 解析目标库的 cookie_knowledge_base_id，再用 `ask_knowledge_base` 检索，单次只查一个库
- MCP 报 600001（cookie 过期）时：提示用户按 `AGENTS.md` §7 重抓 cookie 并运行 `python3 snippets/update_ima_cookie.py "<新 cookie>"`；在此之前降级为检索本地 `guidelines/` 笔记（Read/Grep），并在输出中声明证据强度降级
- 注意项目铁律：真实病例资料**即使脱敏也不发送给 ima 工具**——脱敏后的文本可用于会话内分析与本地归档，但 `ask_knowledge_base` 的提问只含抽象化的临床问题（PICO），不含病例叙述
