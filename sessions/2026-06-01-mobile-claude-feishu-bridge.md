# Session: 移动端协作 Claude 的工作流设计（含飞书桥接方案）
Date: 2026-06-01

## Background / Context

用户场景：ICU 临床医生，医院工作时不方便随时使用电脑，但希望能在手机上：
1. 把病例数据随时更新到 `icu-workflow` 工作目录
2. 获得 Claude 的及时反馈和诊断建议
3. 两端（手机 / 家中 Mac）共用同一个工作目录、共享 Claude 的项目上下文（CLAUDE.md / memory / skills / sessions / snippets / literature）

本会话围绕三轮方案演进，最终聚焦在"飞书机器人桥接"架构。后续实现方案待用户回复 Mac 型号 + 飞书应用类型后细化。

---

## 演进过程与关键决策

### 第一轮：基础路径选型

提出三条路径：
- **A. Obsidian Mobile + 同步**（vault 已是 Obsidian，git log 显示 `init obsidian`）— 同步可选 Obsidian Sync / iCloud / Working Copy + git
- **B. Tailscale + SSH 到家 Mac，手机端跑 Claude Code**（Blink/Termius + mosh + tmux）
- **C. 纯 claude.ai App + 回桌面归档**

用户倾向 **A**，但指出关键问题：
> "claude app 工作的时候没有办法遵循 icu-workflow 工作目录的 claude 配置（agent 和 memory, skill, 已有记录, 知识库等本地资源）"

→ **决策**：Obsidian 同步只解决文件层，不解决 Claude 上下文层。需要 Claude 真正在 Mac 上运行才能继承项目配置。

### 第二轮：项目上下文如何带到移动端

提出两个方案：
- **A. 手机当瘦客户端，Claude Code 跑在家 Mac**（Tailscale + Blink + tmux + `claude`）—— 完整继承所有项目配置，写文件落到真 vault
- **B. claude.ai Projects 上传 CLAUDE.md / memory / 关键 snippets 作为 Project knowledge**—— 模拟 ~70% 上下文，但不能写文件、memory 不会自动更新、skills 完全没有

用户**没有直接选**，而是提出新方向："想从手机 Claude 客户端往家 Mac Claude 客户端发消息，触发任务执行，并能简单交互状态/确认"

→ **决策**：从"手机直接操作 Claude"转向"手机 → 家 Mac 消息桥"架构。

### 第三轮：消息桥架构选型

提出三个架构（按成熟度排序）：
- **A. Telegram Bot 桥**（推荐项）：BotFather 建 bot + Mac 上 Python 守护（`python-telegram-bot` + Claude Agent SDK 或 `claude -p`），双向聊天 + 确认 + 文件回传，~80 行代码
- **B. iOS Shortcuts + SSH + tmux send-keys**：零代码、无守护，但交互体验是"单向贴"而非聊天
- **C. ntfy.sh + 简单 webhook**：开源可自托管，介于 A 和 C 之间

PHI 红线强调：所有过云方案都必须在手机端**先脱敏**（床号 + P1/P2 + 末 4 位 + 年龄段 + 入科第 N 天）。

### 第四轮（最终选定方向）：飞书桥接

用户问"基于飞书能实现吗"。结论：**可以，而且对这个场景比 Telegram 更顺**。

三个核心优势：
1. **飞书 SDK 原生支持长连接模式（WebSocket / Long Connection）**——Mac 无需暴露公网端口，不用 Tailscale Funnel / ngrok / Cloudflare Tunnel，守护脚本出向连接即可
2. **互动卡片对"确认/选择"场景原生友好**——可发结构化卡片（标题/字段/按钮），比 Telegram inline keyboard 更接近"病例查房卡片"语义；支持富文本病例分析、附件 markdown、自动生成飞书文档
3. **国内网络稳，无 GFW 焦虑**——医院 WiFi 直连，无梯子需求

唯一代价：飞书 SDK 比 telegram-bot-sdk 略繁琐（签名、加密配置项更多），但长连接省掉的麻烦远超此成本。

---

## Generated Plan / Solution（飞书桥接架构）

### 总架构图

```
手机飞书私聊 bot
   ↓ (飞书事件订阅，WebSocket 长连接)
家 Mac 守护脚本 (lark-oapi)
   ↓ 收到消息，PHI 自检
   ↓ subprocess: claude -p "$message"  (cwd=icu-workflow)
Claude Code (继承 CLAUDE.md / memory / skills)
   ↓ 写 cases/, 调用工具, git commit
   ↓ 关键节点 → 飞书互动卡片(确认/选择)
   ↓ 完成 → 富文本结果 + 附件 .md
手机飞书收到结果
```

### 一次性配置步骤（~30 分钟）

1. **open.feishu.cn 建"自建应用"**，开启机器人能力
2. **事件订阅勾选** `im.message.receive_v1`，**模式选"长连接"**
3. 拿到 `app_id` / `app_secret`，存入 Mac 本地 keychain
4. 写 `feishu-icu-bot.py`（约 120 行），launchd 守护开机自启
5. 飞书里把 bot 拉进一个**只有自己的私聊群**

### 守护脚本核心职责（待实现）

- 长连接模式接收消息（无需公网回调）
- **PHI 过滤层硬编码在最前面**：命中常见姓氏+名字字符 / 18 位身份证 / 11 位手机号 / 完整病案号 / 精确出生日期 → 拒绝处理 + 提示脱敏后重发
- 把消息当 prompt 喂给 `claude -p`，**cwd 锁定** `~/Claude/icu-workflow`（自动继承 CLAUDE.md / memory / skills）
- Claude 输出用飞书富文本卡片回送
- 关键操作走互动卡片确认（按钮回调）
- 任务归档到 `sessions/YYYY-MM-DD-feishu-<topic>.md`，与现有 session-save 风格一致

### PHI 安全约束

- 飞书数据在飞书云（个人版字节服务器、企业版可走私有部署），**对国内医疗数据合规理论上比 Telegram 更可接受**（不出境），但**未必合规**：严格意义上医院 PHI 不应进任何商业 IM
- 真正的患者识别信息**永远不进飞书消息**，只发：床号 / P1-Pn / 末 4 位 / 年龄段 / 入科第 N 天
- 守护脚本里的 PHI 过滤层是兜底强制执行 `CLAUDE.md` 的去标识化规则

---

## Action Items

- [ ] 用户回复细节后，Claude 给出完整模板：
  - [ ] `feishu-icu-bot.py`（长连接模式 + PHI 过滤层 + cwd 锁定 + 卡片回送）
  - [ ] `launchd` plist（开机自启）
  - [ ] 配置步骤清单（含飞书后台勾选项说明）
- [ ] 用户需回复以确认实现细节：
  - [ ] **Mac 型号**：Apple Silicon 还是 Intel？（影响 Python 环境建议）
  - [ ] **飞书应用类型**：自建应用（个人）还是企业自建应用？（个人通常用自建应用放进个人单聊即可；企业版体验略好但需管理员审批）

---

## Notes

### 备选方案保留

如果后续飞书路线不顺，前面讨论过的三条 fallback 仍可用：
- **Telegram Bot 桥**：跨国/境外场景，PHI 风险等同
- **iOS Shortcuts + SSH + tmux**：最轻量，零守护进程，但是"单向贴"非真聊天
- **ntfy.sh webhook**：开源自托管，介于上述两者

### 与现有项目约定的契合

- 会话归档路径遵循 `CLAUDE.md` 第 4 节："`sessions/YYYY-MM-DD-<topic>.md`"
- 守护脚本所有 Claude 调用 cwd 锁定项目根，自动继承：
  - `CLAUDE.md`（协作风格、PHI 规则、深度分析输出风格）
  - `memory/MEMORY.md`（用户角色记忆）
  - `.claude/`（项目配置 / 可能的 skill）
  - `cases/_templates/`（病例模板：case-analysis.md / 系统化-by-system.md / references-style.md）
  - `snippets/`（处方模板、查房速查）
- 与 `cases/README.md` 的 PHI 双重检查规则一致：写前过滤 + 写后提醒
