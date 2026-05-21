# Obsidian Templater 模板（ICU 夜班）

> **用途**：把 `night-shift-handover.md` 中的 SBAR / 病程记录 / 触发阈值 / 接班脚本变成"按热键 → 弹窗填空 → 生成正文"的工作流
> **依赖**：Obsidian 1.5+，Templater 插件 ≥ 2.0

---

## 1. 安装与配置（一次性）

1. Obsidian → Settings → Community plugins → Browse → 搜索 **Templater** → 安装并启用
2. Templater 设置中：
   - **Template folder location**：选一个文件夹（例如 `99-templates/`），把本目录下 4 个 `.md` 复制进去
   - **Trigger Templater on new file creation**：关（避免新建笔记被随机触发）
   - **Enable folder templates**：可选（如果想"在某文件夹建文件时自动套模板"）
3. **配置热键**（Settings → Hotkeys → 搜索 "Templater"）：
   - `Templater: Open Insert Template modal` → 推荐 `Ctrl/Cmd + T`
   - `Templater: Replace templates in active file` → 在已有文件中触发模板
4. （可选）为每个模板单独绑热键：Templater 设置 → Template Hotkeys → 选模板文件 → 设快捷键
   - 建议：`Cmd+Shift+S` → SBAR；`Cmd+Shift+P` → 病程记录；`Cmd+Shift+R` → 触发阈值；`Cmd+Shift+N` → 接班骨架

---

## 2. 文件清单

| 文件 | 用途 | 输入字段数 | 预计耗时 |
|---|---|---|---|
| `sbar.md` | 给上级电话前生成 SBAR 草稿 | 7 | 60–90 秒 |
| `progress-note-7lines.md` | 夜班高危复评 7 行病程记录 | 7（多行） | 90–120 秒 |
| `trigger-block.md` | 在床位卡里插入触发阈值块 | 1 + 3 个 cursor 跳位 | 15–30 秒 |
| `shift-skeleton.md` | 接班时生成整夜的笔记骨架 | 3 | 30 秒 |

---

## 3. 典型使用流程（一夜）

```
21:00 接班
  ├─ Cmd+Shift+N → 生成《夜班 2026-05-20》骨架
  ├─ 完成 30 min 床旁扫描
  └─ 对每个高危床：Cmd+Shift+R → 插入触发阈值块（6 选 1 → 微调）

夜里出事
  ├─ Cmd+Shift+P → 7 行进展记录（边查边填）
  └─ Cmd+Shift+S → SBAR → 复制 → 打电话 / 发企业微信

07:00 交班
  └─ 在骨架最下方"交班给白班"段落填写
```

---

## 4. 红线（写进模板的提示语里）

- **不写真实病案号 / 姓名**。床号或代号即可。
- **不传 PHI 上云**。Obsidian 默认本地 vault；若用 Sync，注意同步路径在你认可的合规云
- **草稿不是医嘱**。SBAR / 病程记录从模板生成后 → 自行复核 → 才写入电子病历系统
- **触发阈值需个性化**。模板给的是默认骨架（来自 `night-shift-handover.md §4`），每个患者要手动改

---

## 5. 后续可加

- iOS 快捷指令版（不依赖 Obsidian，在通知中心一点直达）
- 把"复评时间"字段接 Obsidian Reminder 插件 → 到点弹窗
- 把"触发阈值"块连 dataview，做夜班最后一页"未闭环"清单（处理后没复评的）
