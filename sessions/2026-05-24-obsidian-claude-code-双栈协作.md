# Session: icu-workflow agent 与 Obsidian 双栈协作

Date: 2026-05-24

## Background / Context

用户询问当前的 `icu-workflow` 仓库（Claude Code project）如何与 Obsidian 结合使用。
经查仓库已是「同一目录、双栈共用」布局：

- `/Users/raymanyan/Claude/icu-workflow/` 根目录同时是 Obsidian vault（含 `.obsidian/`）和 Claude Code project（含 `CLAUDE.md`）
- 已开启 Obsidian 核心插件：`file-explorer / global-search / graph / backlink / tag-pane / templates / daily-notes / outline / properties / bookmarks / sync / bases`
- `snippets/obsidian-templates/` 已存 4 个 Templater 脚本：`sbar.md` / `progress-note-7lines.md` / `shift-skeleton.md` / `trigger-block.md`（Templater 语法 `<%* … %>`，需社区插件）
- 最近提交 `23fa590 init obsidian`

## Key Decisions

- **分工原则**：Claude 负责"生成与重构内容"，Obsidian 负责"消费与串联"
- 床旁/查房路径完全可离线（Templater 不依赖 Claude）
- PHI 红线在 Obsidian 端同样成立（Sync 是端到端加密，但仍不能写真名/完整病案号/精确日期）
- 数据文件由 `.gitignore` 拦截，Obsidian 可见但不进 git，是设计而非 bug

## Generated Plan / Solution

### 一、两边的分工矩阵

| 场景 | 在 Obsidian 里做 | 在 Claude Code 里做 |
|---|---|---|
| 床旁/查房 | 打开 `snippets/*速查.md`、Templater 快键写 SBAR / 7 行复评 | — |
| 病例录入 | 用 `cases/_templates/` cp 出空壳，写主观字段 | 按 SOAP / 系统化结构梳理、生成 24h plan、PHI 自检 |
| 指南/速查 | 阅读、加 backlink、graph 串联 | 「按 CRRT 那套整理 [话题]」生成完整指南 + 24h 处方 + RCT 速查 |
| 文献 | `literature/notes/` 翻阅、按 tag/topic 聚合 | 「按 PICO + 方法学 + 影响整理 [DOI]」 |
| 科研/写作 | 看 `manuscript/` 草稿、跳引用 | 写统计代码、跑分析、改稿、STROBE/TRIPOD 对照 |
| 跨笔记串联 | `[[…]]`、`#topic/…`、graph view | 生成内容时主动加 wikilink |

### 二、推荐具体动作

1. **让 Claude 输出 Obsidian-friendly 内容**：明确请求加 wikilink 与 frontmatter tag
   - 例："…末尾加 [[Sepsis-识别复苏与抗感染]] 和 [[Sepsis-复苏速查]] 的链接，frontmatter 加 `tags: [topic/sepsis, topic/抗感染]`"
2. **Daily Notes 作为会话索引**：每天 daily note 里贴一句"今天和 Claude 讨论了 X → [[…]]"，比翻 `~/.claude/sessions/` 快
3. **Templater 快键（建议手动绑定）**：
   - `Cmd+Shift+S` → SBAR 草稿
   - `Cmd+Shift+P` → 7 行病程
   - `Cmd+Shift+H` → shift-skeleton
   - `Cmd+Shift+T` → trigger-block
4. **tag 命名约定（建议统一）**：
   - `#topic/<ARDS|sepsis|AKI|…>`
   - `#evidence/<RCT|guideline|meta>`
   - `#case/<active|discharged>`
   - `#research/<project>`

### 三、注意事项

- **PHI 红线**：Obsidian Sync 虽 E2EE，但 `cases/` 仍**绝不能**写真名 / 完整病案号 / 精确日期（与 `CLAUDE.md` §2 一致）
- **`.gitignore` 拦数据文件**：研究数据放 `research/<project>/data/` 在 Obsidian 可见但不进 git
- **避免双方同时写同一文件**：Claude 写文件前，先在 Obsidian 关掉对应 tab
- **Templater ≠ Templates**：`<%* %>` 脚本需装 Templater 社区插件，否则原样显示

### 四、最小可用工作流（一天）

1. 早 Daily Note 开张 → 列今日 active patient（用代号）
2. 床旁 → Templater 快键写 SBAR / 7 行复评 → 存 `cases/2026-05/`
3. 下班路上 → Claude Code 里说「把今天 P3 那个 case 按系统化结构梳理 + 提 PHI 风险」
4. 周末 → Claude「按 CRRT 那套整理脓毒症相关性 AKI 的最新证据」→ 落到 `guidelines/AKI/`，Obsidian 里加 backlink 串到 sepsis 指南

## Action Items

- [ ] 在 Obsidian 中确认是否已安装 **Templater 社区插件**（否则 `snippets/obsidian-templates/` 的 4 个脚本不可用）
- [ ] 手动绑定 4 个 Templater 快键（SBAR / 7 行病程 / shift-skeleton / trigger-block）
- [ ] 决定 tag 命名约定是否写入 `CLAUDE.md`（待用户确认）
- [ ] 决定是否在 `README.md` 增补"Obsidian 使用约定"一节（待用户确认）
- [ ] （可选）启用 daily-notes 模板，加"今日 Claude 讨论"字段

## Notes

- 仓库现状：`.obsidian/core-plugins.json` 中 `templates: true`、`sync: true`、`bases: true`、`canvas: true`；社区插件状态未检查
- 现有 6 个亚专题（CRRT / ARDS / Sepsis / AKI / NICU / CV-Cardiac）每个都已配「完整指南 + 床旁速查」双文档结构，适合用 backlink 串
- 用户身份：顶尖三甲 ICU 医生，全亚专业覆盖，自带 R/Python/SPSS 科研能力（来自 memory）
