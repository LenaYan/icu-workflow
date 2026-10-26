---
name: kb-ingest
description: 指南/文献入 ima 知识库编排——分类判断、查 folder_id、查重、上传归档到正确子目录；无匹配类别时先问用户再建目录并回填 ID 表
whenToUse: 有新指南 PDF、文献、网页或微信文章需要收入 ima 知识库时
---

1. **分类判断**：按本地路径与内容判断类别（指南共识 / 药物 / 文献 / 科室 SOP / 教学）。
2. **取 folder_id**：读 `ima-skills/kb-folder-ids.md` 对照表，取目标子目录的 folder_id。
3. **查重**：文件类上传前先 `mcp__ima__check_repeated_names`；已存在则告知用户并询问是否仍要上传。
4. **上传归档**：本地文件用 `mcp__ima__upload_file`，网页/微信文章用 `mcp__ima__import_urls`（1–10 个）；**必须传 folder_id**，禁止落在知识库根目录。
5. **无匹配类别**：先问用户是否新建子目录；同意后用 `python3 scripts/ima_kb_admin.py mkdir` 创建，并把新 folder_id 回填 `ima-skills/kb-folder-ids.md`。
6. **凭证异常**：报 600001 时提示按 `AGENTS.md` §7 重抓 cookie，运行 `python3 snippets/update_ima_cookie.py "<新 cookie>"` 一次性同步三个项目的配置；改完需新开会话生效。
7. **整理已有条目**：MCP 无 move/delete/mkdir 接口，用 `scripts/ima_kb_admin.py`（kbs/folders/ls/mv/mkdir/rm）。
8. **红线**：真实病例资料（即使脱敏）不入 ima；科室 SOP 库不通过 MCP 暴露。
