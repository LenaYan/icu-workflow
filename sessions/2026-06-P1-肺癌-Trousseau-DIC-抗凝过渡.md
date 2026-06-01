# Session: P1 病例分析 — 肺癌 + Trousseau / 慢性 DIC + 抗凝过渡决策
Date: 2026-06

## Background / Context

用户提供 4 张医院 HIS 截屏（含真实 PHI），请求分析一例复杂病例：

**P1, F, 70-75y**（去标识化），肺癌靶向治疗背景下，2 个月内先后双下肢 DVT、外院置入下腔静脉滤网 + 利伐沙班抗凝；过程中反复鼻出血、咯血、头痛；头颅 MRI 提示"左顶枕叶强化灶 / 蛛网膜下腔出血"，停利伐沙班 2 天后转入我科 ICU。

**关键检验（D5）**：PLT **34 ↓↓**、Fib **0.81 ↓↓**、TT **24.31 ↑**、PT/APTT 正常；血小板功能 AA 通路聚集 ↓、ATP 释放 18.18 ↓↓；Hb 103 ↓、中性 79.2 ↑。

会话围绕：(1) 病例梳理与鉴别诊断，(2) 输血支持 + 抗凝过渡的具体床旁医嘱，(3) 入库去标识化病例文件。

## Key Decisions

1. **首要工作假设**：Trousseau syndrome / cancer-associated overt DIC（估算 ISTH ≥ 6 分，D-dimer 待补）
2. **抗凝路径取决于头颅 CT**：
   - 路径 A（证实/进展性 ICH）→ 暂停所有抗凝，IVC 滤网作机械保护，7-14 d 复查影像
   - 路径 B（无新发出血）→ PLT ≥ 50 + Fib ≥ 1.5 + 24 h 无活动出血后启动 **LMWH**
3. **不再回归 DOAC**：本患者已多部位出血 + 疑似脑转移 / SAH → CAT 长期抗凝改 LMWH（CLOT / CARAVAGGIO 证据）
4. **TXA 禁用**（除鼻腔局部填塞）：cancer 高凝 + 双 VTE + IVC 滤网，全身用药有微血栓 / 滤网血栓风险
5. **必须排 HIT**（4Ts 评分）：若 ≥ 4 立即停肝素类、换阿加曲班，不等抗体结果
6. **PHI 处理**：原图含真实姓名/病案号/出生地/精确日期，不入 git；病例文件按 `cases/README.md` 规则去标识化为 P1 / ICU-18 / MR ****7548 / 月份 + 相对 Day 计数
7. **入库**：`cases/2026-06/P1-lung-ca-Trousseau-DIC.md`（已创建，PHI 扫描通过）

## Generated Plan / Solution

### 一、出血支持（next 6h，立即执行）

**血小板**
```
单采血小板 1 治疗量 ivgtt st!
目标：无 ICH → PLT ≥ 50；ICH/SAH → PLT ≥ 100
输前/输后 1h PLT 评估 CCI；CCI < 7.5 警惕 HIT / ITP
```

**纤维蛋白原**（目标：ICH ≥ 2.0 g/L；其他大出血 ≥ 1.5 g/L）
- 首选：**人纤维蛋白原 4 g ivgtt st!**（50 kg 估算）；Δ Fib ≈ 给药剂量(g)/0.04/体重(kg)
- 次选：冷沉淀 10 U（1 U/10 kg）

**FFP**：仅在 PT/APTT > 1.5× ULN 且伴出血时使用，10-15 mL/kg

**红细胞**：Hb < 70（一般），< 80-90（缺血/SAH 痉挛期）

**TXA**：❌ 禁用（除鼻腔局部）

**利伐沙班逆转**（危及生命大出血）：
- andexanet alfa（国内未普及）
- **4F-PCC 50 IU/kg ivgtt**（首选可及；50 kg → 2500 IU）
- 维生素 K1 10 mg iv（经验性）

### 二、抗凝过渡决策树

```
              头颅 CT（≤24h 必做）+ 神经查体
                          │
            ┌─────────────┴─────────────┐
   证实/进展性 ICH                 无新发/稳定颅内出血
            │                            │
   路径 A：暂停抗凝              路径 B：PLT≥50+Fib≥1.5
   • IVC 滤网保护                 + 24h 无活动出血 → LMWH
   • 7-14d 复影像                 • 不回 DOAC
```

### 三、LMWH 方案（路径 B）

| 选择 | 剂量（50 kg） | 肾调整 |
|---|---|---|
| 达肝素（CLOT） | 首月 10,000 IU sc QD；2-6 月 7,500 IU QD | CrCl 20-30 减 25%，< 20 改 UFH |
| 依诺肝素 | 50 mg sc q12h | CrCl 15-30 → 1 mg/kg QD；< 15 UFH |
| 那屈肝素 | 4,300 IU sc q12h（0.4 mL） | CrCl < 30 减 25-33% |
| UFH 泵入 | 18 IU/kg/h，无 bolus | APTT q6h 目标 50-80s |

监测：抗-Xa 峰值（注射后 4h）0.5-1.0 IU/mL；UFH 用 APTT 或抗-Xa 0.3-0.7。

### 四、HIT 处理（4Ts ≥ 4 时）

```
立即停所有肝素
阿加曲班 2 μg/kg/min iv（肝功不全 0.5 起）
APTT 1.5-3.0× baseline；注意延长 INR 影响华法林转换
替代：磺达肝癸钠 7.5 mg sc QD（出血状态慎用）
```

### 五、肿瘤治疗调整（MDT 决策）

| 用药 | 建议 |
|---|---|
| EGFR/ALK/ROS1 TKI | 与肿瘤科商定继续 vs 暂停；疑血液毒性 → 暂停 1-2 周 |
| 贝伐单抗 / VEGF 抑制剂 | **立即停**（出血明确风险） |
| 化疗（铂类等） | 暂停，待 PLT > 75、Hb > 90、ANC > 1.5 |
| 免疫检查点抑制剂 | 排除免疫性血小板减少 |

### 六、支持治疗要点

- **神经**：床头 30°，SBP 130-160，对乙酰氨基酚 0.5 g po q6h prn（禁 NSAIDs），渗透治疗仅 ICP crisis（3% NaCl 优于甘露醇），SAH/皮层受累考虑 levetiracetam 500 mg q12h × 7d
- **SUP**：泮托拉唑 40 mg iv QD
- **机械 VTE 预防**（抗凝停期间）：IPC ≥ 18h/d + 弹力袜
- **营养**：24-48h EN 滋养性 10-20 mL/h 起，目标 25-30 kcal/kg/d、蛋白 1.2-1.5 g/kg/d
- **血糖**：7.8-10 mmol/L
- **感染**：完善 PCT/CRP/G/GM/培养，不经验性抗生素

### 七、监测计划

| 频率 | 项目 |
|---|---|
| q1h | 神志 + GCS + 瞳孔 + 出血部位 + vitals |
| q4h | 神经专科查体（NIHSS） |
| q6-12h | PLT、Fib、PT、APTT、D-dimer、Hb |
| q24h | 全血常规、生化、LDH、外周血涂片 |
| 24h、72h、加重时 | 头颅平扫 CT |
| 入科 24h | 双下肢血管 US + IVC 滤网影像 + 胸部 CT |

### 八、Red Flags

- GCS ↓ ≥ 2 / 瞳孔不等大 → 紧急头颅 CT + 神外
- 咯血 > 100 mL/次 或 > 200 mL/24h → 气道保护 + 支气管镜 + BAE
- SBP > 180 → 尼卡地平 5 mg/h iv
- PE 征象 → TTE + CTPA + 权衡半剂量溶栓
- PLT 输注 CCI < 7.5 → 复评 HIT / ITP
- Fib 输注后无升 → AT-III 替代（< 50%，200-300 IU iv）

### 九、缺失信息清单（待用户补齐）

1. 肺癌病理类型 / 分子分型 / 当前靶向药剂量 / 最近影像
2. 头颅 MRI 原报告：单/多发、水肿、出血信号（SWI/T2*）
3. 抗凝史：利伐沙班具体剂量与停药时间；既往 UFH/LMWH 暴露（HIT 关键）
4. IVC 滤网类型（永久 vs 可回收）、置入影像、滤网血栓
5. 当前查体：GCS / 瞳孔 / 肌力 / 脑膜刺激征 / 出血部位与量
6. 体重 / 身高 / Cr / eGFR — 精算剂量
7. 化疗史 / 激素史 — PJP 风险

## Action Items

- [ ] 用户：删除或加密保管 `~/Downloads/pics/` 下原图（含 PHI）
- [ ] 用户：补齐"缺失信息清单"9 项，反馈后精算剂量并更新病例文件
- [ ] Claude（按需）：出 `literature/topics/trousseau-syndrome-CAT.md` 综述
- [ ] Claude（按需）：出 `snippets/DIC-bedside-card.md` + `snippets/anticoag-reversal-card.md` 床旁速查卡

## Notes

### 引用证据 / 关键试验

| 试验 / 指南 | 要点 |
|---|---|
| **CLOT (Lee NEJM 2003)** | LMWH (达肝素) > VKA for CAT |
| **CATCH (JAMA 2015)** | 替奈普素优于 VKA |
| **Hokusai-VTE Cancer (NEJM 2018)** | 依度沙班 non-inferior，GI 出血↑（GI/GU 肿瘤慎用） |
| **SELECT-D (JCO 2018)** | 利伐沙班 VTE 复发↓但 CRNMB↑ |
| **CARAVAGGIO (NEJM 2020)** | 阿哌沙班 non-inferior，大出血未增（不含脑癌/急性白血病） |
| **ITAC 2022 / ASH 2021 / ASCO 2023** | 高出血风险 → LMWH 优先 |
| **ISTH DIC 2013 / EHA-ISTH 2024** | overt DIC 评分；治疗以原发病为本 |
| **AABB 2015 / BSH 2017** | PLT 阈值：一般 <10；操作 <50；ICH <100 |
| **BCSH 2022** | Fib：大出血 ≥ 1.5；产科/ICH ≥ 2.0 |
| **PREPIC2 (JAMA 2015)** | IVC 滤网 + 抗凝 vs 单纯抗凝无获益；可回收滤网 3 月内取出 |
| **NICE-SUGAR (NEJM 2009)** | ICU 血糖 7.8-10 mmol/L |

### 工作流要点

- 原图 4 张含真实姓名、病案号、出生地、精确日期 → 严格 PHI 处理
- 病例文件入库路径：`cases/2026-06/P1-lung-ca-Trousseau-DIC.md`
- PHI 扫描脚本（grep 真实标识符）通过
- 用户随后对入库文件做了表格格式微调（linter / 手动），核心内容保留
