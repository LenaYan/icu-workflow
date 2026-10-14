---
name: medical-record-drafting
description: 病历文书生成——把关键临床信息转换为符合国内病历书写规范、可直接粘贴进 HIS 的文本（交班报告、SOAP 病程、会诊意见、阶段小结、抢救记录）。写交班和病程时使用。
whenToUse: 写交班、SOAP 病程、会诊意见、阶段小结、抢救记录等需要规范病历文本时
---

本 skill 的完整流程定义在项目文件 `ima-skills/12-病历文书生成.md`。**先读取该文件，再严格按其中的适用场景、工作流程、输出格式与安全边界执行。**

本地化适配：

- 本 skill 不依赖知识库检索；如需对照科室模板，可参考 `snippets/` 与 `cases/_templates/`
- 涉及其他「知识库」表述时：指 ima 云端库，通过 `mcp__ima__` 工具访问（先 `list_knowledge_bases_full` 解析库 ID，再 `ask_knowledge_base`）；MCP 报 600001 时按 `AGENTS.md` §7 处理
- 输出用于 HIS 的文本不得含需要隐去的 PHI 之外的造假信息；写入 `cases/` 的内容仍须过 PHI 自检（规则见 `cases/README.md`）
