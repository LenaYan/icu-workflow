---
name: guideline-lookup
description: 指南速查——ICU 临床问题快速检索指南共识库，输出带推荐等级和出处页码的推荐意见，并对照国际指南与国内共识差异。查房前、会诊中、家属谈话前使用。
whenToUse: 查房前、会诊中、家属谈话前需要指南推荐意见 + 推荐等级 + 出处时
---

本 skill 的完整流程定义在项目文件 `ima-skills/01-指南速查.md`。**先读取该文件，再严格按其中的适用场景、工作流程、输出格式与安全边界执行。**

本地化适配（正文中「知识库」一词按以下规则理解）：

- 「知识库」指 ima 云端库，通过 `mcp__ima__` 工具访问，用 `ask_knowledge_base` 检索，单次只查一个库；**目标库的 cookie_knowledge_base_id 直接查 `ima-skills/kb-registry.md`**（自有「医学知识库」为一级源，订阅指南库为二级源，按表中检索顺序执行），不必每次重新 `list_knowledge_bases_full`
- **引用纪律（强制，细则见 `kb-registry.md` 检索总规则）**：推荐意见与推荐等级按原文引用，标注来源（库名 + 文档名 + 页码/章节）；关键内容用 references 中的 `media_id` 调 `get_media_info` 回原文核对，拿不到原文的标注「未核对原文」；检索不到的写「知识库未覆盖，建议查原文」，禁止凭记忆补全
- 指南类问题至少完成「自有库 + 1 个订阅指南库」两库交叉；结论冲突时并列呈现并提示用户
- MCP 报 600001（cookie 过期）时：提示用户按 `AGENTS.md` §7 重抓 cookie 并运行 `python3 snippets/update_ima_cookie.py "<新 cookie>"`；在此之前降级为检索本地 `guidelines/` 笔记（Read/Grep），并在输出中声明证据强度降级
- 真实病例资料（即使脱敏）不发送给 ima 工具；凡需向 ima 提问的内容先做 PHI 检查（规则见 `cases/README.md`）
