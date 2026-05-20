# CRRT 处方速查（成人）

> 详细证据与争议见 `guidelines/CRRT/2026-05-20-CRRT-治疗模式及处方调整.md`

## 默认处方（70 kg 示例）

```
模式：CVVHDF
Qb：200 mL/min
Effluent：25 mL/kg/h → 1750 mL/h
  ├ Pre-replacement：500 mL/h
  ├ Post-replacement：500 mL/h
  └ Dialysate：750 mL/h
Net UF：0–100 mL/h（按 hemodynamics 动态调，上限 1.5 mL/kg/h）
抗凝：RCA（首选）
  ├ 4% 枸橼酸钠泵入血路前段
  ├ 目标滤后 iCa²⁺ 0.25–0.40 mmol/L
  └ 静脉补 CaCl₂ / 葡糖酸钙，目标外周 iCa²⁺ 1.0–1.2 mmol/L
```

## 监测

| 频率 | 项目 |
|---|---|
| q6h | 血气 + iCa（外周 / 滤后）+ 电解质 + 全 Ca |
| q12h | 凝血 + Mg + Phos |
| qd  | delivered dose（机器累计 effluent / 实际运行时间 / 体重）|

## 警示阈值

| 指标 | 阈值 | 含义 |
|---|---|---|
| Total Ca / iCa | > 2.5 | citrate accumulation（肝衰风险）|
| Lactate | > 8 mmol/L + 休克 | RCA 相对禁忌 |
| Filtration fraction | > 25% | 后稀释比例过高，凝血风险 |
| Net UF | > 1.75 mL/kg/h | 不良结局相关 |

## 启动指征（AEIOU）

- **A**cidosis — 难治性代酸（pH < 7.15）
- **E**lectrolyte — K⁺ > 6.5 mmol/L 难治
- **I**ntoxication — 中毒（lithium、metformin、salicylate、valproate）
- **O**verload — 难治性容量过负荷
- **U**remia — 尿毒症并发症（脑病、心包炎、出血）

无紧急指征：综合 STARRT-AKI / AKIKI / AKIKI2，不急于早启动；但不拖到 KDIGO 3 期 > 72 h。

## 特殊高剂量场景

| 场景 | 处方调整 |
|---|---|
| 高血氨（>150–200 μmol/L，肝衰/UCD）| initial 50–60 mL/kg/h，对流为主 |
| 横纹肌溶解（myoglobin）| 高 cut-off 膜（EMiC2 / Theranova）+ 对流 |
| Tumor lysis | 短期高剂量 + 监测 K⁺/Phos/UA |
| 中毒 | IHD 更快，血流动力学不允许时高剂量 CVVHDF |

## 终止

自主尿量 > 400 mL/d（不依赖利尿剂）+ 肌酐自发下降 + 电解质稳定 → 试停
