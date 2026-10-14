---
name: session-archive
description: 会话纪要归档——把有产出的工作会话整理为可长期复用的纪要，写入 sessions/YYYY-MM-DD-<topic>.md
whenToUse: 一个有产出的工作会话结束、需要沉淀纪要时
---

1. **归档位置**：仅当会话在本项目目录下工作时写入 `sessions/`；否则写到项目外并说明原因。
2. **纪要内容**：目标 → 关键结论 → 决策与理由 → 产出文件路径 → 待办/后续动作；提炼可复用部分，去掉过程噪音（失败的尝试只留结论）。
3. **命名**：`sessions/YYYY-MM-DD-<topic>.md`，日期取当天，topic 用短横线连接的关键词。
4. **PHI**：纪要涉及病例内容时同样过 PHI 自检（规则见 `cases/README.md`）。
5. **完成后**：告知用户归档路径；提醒 Kimi Code 自带的会话恢复（`kimi --session` / `/sessions`）与归档纪要互补，不互相替代。
