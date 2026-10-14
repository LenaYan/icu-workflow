# Evals — 病例分析质量回归测试

> 起源：2026-10（基线轮）对同一例 HTG-AP（P1，入科 D4）病例，分别用 ima 客户端 / kimi-code / kimi client 三条链路产出分析，再做三方对比。对比中发现的问题没有机制保证不复发，本目录把那次对比固化为可重复执行的回归测试，并配套 lint 与计算工具。
> 对比原始记录：`sessions/` 未归档时见该次会话；三份被测文档在 `~/Downloads/`（P1_男29岁_HTG-AP会诊记录_20261014-ima.md 等）。

---

## 1. 那次 eval 发现的问题（优化动机）

| # | 问题 | 出现在 | 后果 |
|---|---|---|---|
| P1 | 剂量/阈值主张无 `[N]` 引用、无核对状态标注，直接下医嘱 | ima 版（整篇无编号参考文献）；kimi-client 版部分条目 | 违反 AGENTS.md §7 引用纪律，关键数字不可追溯 |
| P2 | 参考文献著录不完整（"经 ima 检索归纳"，无期刊年卷期页） | kimi-client 版 | 无法回核 |
| P3 | 可计算的指标没算：ROX 有数据却写"无法计算" | kimi-code 版 | 漏掉对"HFNC 目前安全"的量化论证 |
| P4 | 建议超出证据字面范围：PE 追加门槛低于共识、24h 负平衡目标偏激进且无上限依据 | kimi-client 版 | 越界推荐混入指南推荐，难以识别 |
| P5 | 输出缺 Red flags 段（交班最实用的一段） | kimi-code 版、ima 版 | 模板缺该节 |
| P6 | sub-agent 步骤被静默跳过的风险（client 版如实声明了偏差，属合规降级） | kimi-client 版 | 需要 lint 认可"声明过的降级"，防止静默缺步 |
| P7 | 多文档对比时抹平分歧为"共识"、对比结论未回原文验证（4 处事实错误） | ima 生成的对比文档 | 对比类产出本身需要规则 |

## 2. 优化方案与落点对照

| 问题 | 机制 | 落点 |
|---|---|---|
| P1/P2/P5/P6 | **lint**：`scripts/check_case_doc.py`，机械校验剂量-引用距离、参考文献核对状态三态标记、必备章节、流程块二选一 | 本目录 + `scripts/` |
| P3 | **计算前置**：`scripts/clinical_calc.py` 增加 rox / gik / uf / pf / ca-correct；skill 强制"先算后写，数据存疑做敏感性分析" | `scripts/clinical_calc.py`、`.kimi-code/skills/case-deep-analysis/` |
| P4 | **建议-证据对齐**：每条处置建议标注 `指南原文 / 指南外推 / 推理`；引用回核 sub-agent 增加"主张强度 ≤ 证据强度"职责 | `.kimi-code/skills/case-deep-analysis/SKILL.md`、`cases/_templates/case-analysis.md` |
| P5 | 模板补「Red flags（立即升级）」段 | `cases/_templates/case-analysis.md` |
| P7 | 新 skill `analysis-compare`：对比结论回原文验证、分歧禁止收敛、逐值归属来源 | `.kimi-code/skills/analysis-compare/` |
| 全部 | **evals 回归**：fixture + 金标准，skill/模板改动后重跑 | 本目录 |

## 3. 目录结构

```
evals/
├── README.md                       # 本文件
└── fixtures/
    └── p1-htg-ap-d4/
        ├── input.md                # 脱敏病例输入（2026-10 基线轮三方 eval 的原始输入）
        ├── gold-key.md             # 金标准：必算项 / 必抓项 / 越界项 / 引用项
        └── rubric.md               # 评分细则
```

## 4. 用法

**对新产出的病例分析跑 lint**：

```bash
python3 scripts/check_case_doc.py cases/2026-10/P1-HTG-AP-xxx.md
# 或批量
python3 scripts/check_case_doc.py cases/2026-10/
```

**回归流程**（改了 skill / 模板 / 计算脚本后）：

1. 用 `fixtures/<case>/input.md` 作为输入，走一遍 `case-deep-analysis` 流程产出新分析
2. `check_case_doc.py` 跑 lint（应 0 error）
3. 人工或 sub-agent 按 `gold-key.md` 逐条核对：必算项是否都算、必抓项召回率、有无越界项
4. 按 `rubric.md` 打分，与基线对比

**基线成绩**（2026-10 基线轮三方 eval，详见 `fixtures/p1-htg-ap-d4/gold-key.md` 末尾）：kimi-code 版召回最高但漏 ROX 实算；kimi-client 版有 2 处越界推荐；ima 版引用纪律全项不达标。

## 5. 新增 fixture 的规范

- 病例必须已去标识化（规则见 `cases/README.md`）
- `input.md` 只含模型当时可见的输入，不混入事后信息
- `gold-key.md` 的必抓项必须有指南/试验依据，越界项必须写明对应的证据边界
- fixture 命名：`p<N>-<病种>-<阶段>`
