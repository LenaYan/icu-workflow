# AKI — 诊断、分期、防治

Date: 2026-05-20
References: KDIGO AKI 2012、KDIGO 2020 update、STARRT-AKI、AKIKI/AKIKI2、ELAIN、IDEAL-ICU、PRESERVE、AMACING、PrevAKI、PrevAKI-Multicenter

> CRRT 处方与抗凝详见 `guidelines/CRRT/`。

---

## 一、定义与分期（KDIGO 2012）

| 标准 | 内容 |
|---|---|
| **诊断** | SCr ≥ 0.3 mg/dL (≈ 26.5 μmol/L) ↑ 48 h 内；或 SCr ≥ 1.5× baseline 7d 内；或尿量 < 0.5 mL/kg/h × 6 h |
| **Stage 1** | SCr 1.5–1.9× 或 ↑ ≥ 0.3 mg/dL；尿量 < 0.5 × 6–12 h |
| **Stage 2** | SCr 2.0–2.9×；尿量 < 0.5 ≥ 12 h |
| **Stage 3** | SCr ≥ 3.0× 或 ≥ 4.0 mg/dL；或启动 RRT；或 eGFR < 35（< 18 岁）；尿量 < 0.3 ≥ 24 h 或无尿 ≥ 12 h |

**基线肌酐**：用近 3–12 月内稳定值；缺失时用 MDRD eGFR 75 反推（KDIGO 建议）。

---

## 二、病因鉴别（前/肾/后）

```
Pre-renal
  ├ 容量不足（出血、脱水、第三间隙）
  ├ 低有效循环（心衰、肝硬化 HRS、sepsis）
  └ 肾血管（RAS、AAA、ACEI/ARB、NSAIDs）

Intrinsic
  ├ ATN（缺血、毒物：氨基糖苷、两性 B、顺铂、造影剂）
  ├ AIN（药物：β-lactam、PPI、NSAID、ICI）
  ├ GN（PR3/MPO、抗 GBM、IgA、LN）
  └ TMA（HUS/TTP、恶性 HTN、DIC、APS）

Post-renal
  ├ 双侧梗阻或单肾梗阻
  └ 神经源性膀胱、前列腺、肿瘤压迫
```

**床旁鉴别**：
- 尿沉渣：muddy brown casts → ATN；RBC casts → GN；WBC casts + eosinophil → AIN
- FENa（无利尿剂下）：< 1% pre-renal；> 2% ATN；GN/contrast/myoglobin 不可靠
- FEUrea（用利尿剂时）：< 35% pre-renal
- 肾 US：排除梗阻 + 评估慢性指标（皮质回声、CMD）
- 蛋白尿、血尿、补体、ANCA、抗 GBM、PLA2R → 怀疑 GN 时

---

## 三、生物标志物（新一代）

| 标志物 | 意义 | 状态 |
|---|---|---|
| **NGAL** | 早期肾小管损伤 | 早期识别，临床有限可及 |
| **TIMP-2 × IGFBP-7** (NephroCheck) | "细胞周期阻滞" | FDA 批准，ICU 中预测 AKI |
| **Cystatin C** | GFR 替代标志，独立于肌肉量 | 老年/肝硬化/肌少症更可靠 |
| **KIM-1** | 近端小管损伤 | 研究为主 |
| **urinary [TIMP-2]×[IGFBP-7]** | PrevAKI bundle 入选标准 | 临床决策辅助 |

**Renal angina index (RAI)**：儿科起源，成人外推，结合 risk + injury 信号，三级预警。

**Furosemide stress test (FST)**：呋塞米 1.0–1.5 mg/kg IV → 2 h 尿量 < 200 mL 提示进展至 stage 3 / 需 RRT，**阴性预测值好**。

---

## 四、预防（高风险患者 bundle）

**KDIGO bundle**（PrevAKI / PrevAKI-Multicenter 验证，心外科为主）：

- [ ] 停用肾毒性药物（NSAIDs、ACEI/ARB 围术期、aminoglycoside、IV contrast 择期可缓）
- [ ] 维持容量与血流动力学（避免过/不足，individualized MAP — 慢性 HTN 65–80）
- [ ] 避免高血糖（140–180 mg/dL）
- [ ] 避免造影剂（必要时低渗、最小剂量、IV NS 水化；**N-acetylcysteine 不推荐** — PRESERVE/AMACING）
- [ ] 评估再灌注/手术时机

**对比剂相关 AKI (CA-AKI)**：
- **PRESERVE (NEJM 2018)**：IV NaHCO₃ vs NS、NAC vs placebo → 全阴性
- **AMACING (Lancet 2017)**：低-中危患者预防性水化 vs 无水化 → 无差异
- 实践：仅高危（eGFR < 30、糖尿病肾病、心衰）水化 IV NS 1 mL/kg/h × 12 h 前后；造影剂用量最小化

**心外科 / 大手术**：goal-directed therapy + KDIGO bundle 应用证据相对最强

---

## 五、容量与血压管理

- 容量复苏：balanced crystalloid 优先（SMART、PLUS）
- 避免容量过负荷（**> 10% accumulation 与 AKI 进展/死亡相关**）
- MAP 个体化：慢性 HTN 患者 MAP ≥ 75–80（SEPSISPAM 子分析）
- 利尿剂：仅用于容量管理，不"治疗 AKI"或"逆转"

---

## 六、肾毒性药物管理

| 药物 | 备注 |
|---|---|
| Aminoglycosides | 单日给药、TDM、疗程最短化 |
| Vancomycin | TDM（AUC/MIC > trough），CRRT 时 SC 0.8 调整 |
| Polymyxin | 强肾毒，TDM、与碳青霉烯联用减剂量 |
| 两性霉素 B | 改用脂质体形式 |
| 顺铂 / methotrexate / aciclovir | 预水化 + 监测尿酸/晶体 |
| NSAIDs | 围术期及 AKI 期避免 |
| ACEI/ARB/SGLT2i | 急性期暂停；SGLT2i 长期肾保护，恢复期可重启 |
| ICI（PD-1/PD-L1） | AIN，需肾穿 + 类固醇 |

---

## 七、肾替代治疗时机（与 CRRT 文档协同）

| 试验 | 结论 |
|---|---|
| **ELAIN 2016** | 早 vs 延迟（KDIGO 2 vs 3）：早 ↓ 死亡（单中心，外科） |
| **AKIKI 2016** | 早 vs 延迟：无差异 |
| **IDEAL-ICU 2018** | sepsis 中早启动无获益 |
| **STARRT-AKI 2020** | 加速 vs 标准：90d 死亡率无差异，加速组依赖透析↑ |
| **AKIKI2 2021** | 更延迟启动反而不利 |

**实践**：紧急指征 **AEIOU** 立即启动；无紧急指征观察 + 优化，但不拖到 KDIGO 3 期 > 72 h。

---

## 八、特殊情景

### 心衰 / 心肾综合征（CRS）
- **CARRESS-HF**：ultrafiltration vs stepped diuretic → diuretic 优势
- 实践：足量袢利尿剂（continuous infusion）+ thiazide 联合 → 失败再 UF/CRRT

### 肝肾综合征（HRS-AKI，新定义 2019）
- **Terlipressin**（CONFIRM）：HRS-1 逆转率↑，但呼衰风险，慎选患者
- Albumin 1 g/kg day1，再 20–40 g/d
- 评估 TIPS / LT

### 横纹肌溶解
- 大量晶体复苏，目标尿量 200–300 mL/h
- 碱化尿液（pH > 6.5）证据有限
- CRRT 仅在 AKI 已发生且需肾替代时；高 cut-off 膜清除 myoglobin

### Tumor lysis syndrome
- 预防：水化、rasburicase / allopurinol、避免碱化
- 监测 K/Phos/Ca/UA q6h

### 妊娠相关 AKI
- HELLP / AFLP / TMA 鉴别；产科会诊；不延迟分娩

---

## 九、AKI 恢复与远期

- **AKI → CKD progression**：≥ 25% 进展至 CKD，**3 月内 nephrology follow-up**
- SGLT2i 恢复期开始（除非禁忌）— DAPA-CKD / EMPA-KIDNEY 肾保护证据
- ACEI/ARB 重启评估
- 复测 SCr / eGFR / 蛋白尿，3–6 月内追踪

---

## 十、24h 诊疗清单（新发 KDIGO 2，70 kg）

```
诊断
  ├ 复查 SCr q12h，KDIGO 分期更新
  ├ 尿沉渣 + FENa（或 FEUrea 若用利尿剂）+ UPCR/UACR
  ├ 肾 US 排除梗阻
  └ 评估病因（药物、容量、感染、心功能）

治疗
  ├ 停 NSAIDs / 推迟 ACEI-ARB / 评估造影剂用量
  ├ Vancomycin TDM；β-lactam CRRT 下调整
  ├ 容量目标：avoid > 10% accumulation
  ├ MAP 65（慢 HTN 75–80），监测乳酸 / CRT / 尿量
  └ FST 评估 RRT 风险（呋塞米 1.0 mg/kg → 2 h 尿量）

监测
  ├ 尿量 q1h，SCr q12h，K/Phos/Ca/HCO₃ q6–12h
  ├ AEIOU 任一阳性 → 启动 CRRT
  └ 评估 nephrology 会诊（怀疑 GN / AIN / TMA）
```

---

## 十一、关键试验速查

| 主题 | 试验 | 结论 |
|---|---|---|
| RRT 时机 | ELAIN / AKIKI / IDEAL-ICU / STARRT-AKI / AKIKI2 | 不急于早启动 |
| Contrast AKI | PRESERVE / AMACING | NaHCO₃ / NAC / 预防性水化在低-中危无效 |
| 心肾 | CARRESS-HF | diuretic > UF |
| HRS | CONFIRM | terlipressin 有效，但呼衰风险 |
| 心外科 AKI 预防 | PrevAKI / PrevAKI-MC | KDIGO bundle 减 AKI |
| FST | Chawla 2013 | 阴性预测 RRT 进展好 |
| 平衡液 | SMART / PLUS / BaSICS | balanced 倾向获益 |
