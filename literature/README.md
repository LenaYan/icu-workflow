# literature/ — 文献阅读

## 目录
```
literature/
├── README.md
├── _templates/
│   ├── single-paper-PICO.md   # 单篇 RCT/队列/meta 笔记
│   ├── topic-review.md        # 主题综述
│   └── journal-club.md        # 期刊俱乐部讨论稿
├── notes/                      # 单篇文献笔记 — 按 PMID 或 trial-name 命名
│   └── {trial-name}-{year}.md
└── topics/                     # 主题汇总 — 按主题命名
    └── {ARDS-vent | sepsis-resuscitation | …}.md
```

## 命名约定
- 单篇：`{TRIAL-NAME}-{Year}.md`（首选） / `{PMID}-{first-author}.md`
- 主题：`{亚专题}-{细分}.md`，如 `ARDS-vent.md`、`sepsis-fluid.md`

## 工作流
1. **读完即记**：用 `_templates/single-paper-PICO.md` 在 `notes/` 写 1 份
2. **每 3–5 篇**：同主题归并到 `topics/<主题>.md`
3. **每月 1 次**：journal club 用 `_templates/journal-club.md` 选 1 篇精读
4. 笔记里互链：`[[trial-name]]`，便于反向导航

## 与 Claude 协作
> "按 PICO + 方法学 + 影响整理 PMID 36...."
> "把 ARDS-vent topic 下的笔记重新整理为一份综述"
> "对比 EOLIA 和 CESAR 的方法学差异"
