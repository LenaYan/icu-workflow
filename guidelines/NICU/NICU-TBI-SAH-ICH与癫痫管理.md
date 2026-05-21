# 神经重症 — TBI / SAH / ICH / 状态癫痫管理

Date: 2026-05-20
References: BTF 4th 2016 (+ updates)、SIBICC consensus 2019、AHA/ASA SAH 2023、AHA/ASA ICH 2022、ATACH-2、INTERACT-2/3、ENRICH、SUGAR-ICH、COBI、ESETT、RESCUEicp/DECRA、TTM2

---

## 一、TBI

### Brain Trauma Foundation 4th edition 阈值

| 参数 | 目标 |
|---|---|
| ICP | < 22 mmHg |
| CPP | 60–70 mmHg |
| PbtO₂ (脑氧) | > 20 mmHg（BOOST-3 阴性，未取代 ICP） |
| Glucose | 140–180 mg/dL |
| Na⁺ | 145–155 mmol/L（HTS 治疗中） |
| Temp | 正常体温（35.5–37.5），治疗性低温不常规推荐（POLAR 阴性） |
| SBP | ≥ 110 (15–49y / ≥ 70y)；≥ 100 (50–69y) |

### SIBICC tier-based management（共识 2019）

```
Tier 0：基础治疗
  ├ 头高 30°、ETT 固定不压颈静脉
  ├ 镇静（propofol / dex / fentanyl），目标 RASS −2 到 −4
  ├ MAP/CPP 维持，避免低氧
  ├ 体温正常化
  ├ Na 145–155，避免低钠
  └ ICP 监测（EVD 可同时引流脑脊液）

Tier 1：ICP > 22 持续 > 5 min
  ├ 加深镇静、镇痛
  ├ EVD 引流 CSF
  ├ Mannitol 0.25–1 g/kg（适合容量过负荷者）或 3% NaCl bolus 250 mL
  ├ PaCO₂ 35–38（避免 < 30 长期）
  └ 排除新发病变（CT）

Tier 2：Tier 1 失败
  ├ NMBA 持续输注（cisatracurium）
  ├ 持续 3% NaCl 输注，目标 Na 150–155
  ├ MAP 提升以维持 CPP 60–70
  └ 反复 CT 排除新发

Tier 3：refractory ICP
  ├ Barbiturate coma（pentobarbital，EEG burst-suppression）
  ├ Decompressive craniectomy（RESCUEicp 60% 死亡率↓ 22% → 但严重残疾↑）
  ├ Therapeutic hypothermia（POLAR 阴性，仅 ICP 难控时考虑）
  └ NIRS / PbtO₂ 指导精细化
```

### 关键试验
- **DECRA 2011**：早期 craniectomy（ICP > 20，1 h）→ 死亡率↓但 unfavorable outcome↑ — 不推荐"预防性"使用
- **RESCUEicp 2016**：refractory ICP → 死亡率 26.9% vs 48.9%，但 vegetative 状态↑
- **POLAR 2018**：预防性低温（33–35℃）→ 阴性
- **CRASH-3 2019**：TBI + GCS 9–15，3 h 内 TXA 1 g + 1 g → 头部相关死亡↓
- **BEST TRIP 2012**：ICP 监测 vs 临床/CT 指导 → 无差异（南美设置，受质疑）
- **SYNAPSE-ICU 2021** 观察：ICP 监测 + treatment intensity 改善结局

### 高渗治疗：3% NaCl vs Mannitol

| 药 | 优势 | 劣势 |
|---|---|---|
| 3% NaCl | 容量扩张、低血压少、Na 监测明确；refractory ICP 一线 | 中心静脉、AKI（Na > 160）、高氯酸中毒 |
| Mannitol | 外周可用、CSF 减少 | 利尿 → 低血压；反复使用反弹；尿渗压差 > 20 提示再次给药安全 |

**COBI 2021**：连续 HTS 输注预防性使用 → 无获益。HTS 仍是 ICP crisis 首选 bolus。

---

## 二、自发性 SAH（aSAH）

### AHA/ASA 2023 关键

- **早期治疗动脉瘤**：< 24–72 h，coiling 优先（ISAT 长期随访）；coiling 不可行时 clipping
- **Nimodipine** 60 mg PO q4h × 21d（**唯一**改善结局药物，机制可能非血管痉挛本身）
- **血压**：动脉瘤未处理 → SBP < 160（或 MAP < 110）；处理后宽松
- **EVD**：急性脑积水必备；后续考虑 VPS
- **预防性抗癫痫**：不再常规推荐（短期 < 7d 可考虑高危）

### 血管痉挛 / DCI 管理
- 监测：TCD（MCA 平均流速 > 120 cm/s 或 Lindegaard 比值 > 3）、CTA/CT 灌注、连续 NIHSS
- **Triple-H** 已被弃用，改为 **euvolemia + induced hypertension**（NE 升 SBP 20%）
- **IA verapamil / nicardipine / milrinone** 动脉内介入：refractory 血管痉挛
- **Cisternal magnesium / statins / endothelin antagonists**（clazosentan）：MASH 系列阴性；clazosentan REACT 阳性，区域批准 中

### 监测
- 每日 NIHSS、TCD（POD 3–14）
- 钠：avoid hyponatremia（cerebral salt wasting vs SIADH 鉴别，常先用 HTS + 容量复苏）

---

## 三、ICH（自发脑出血）

### BP 控制
- **INTERACT-2 2013**：SBP < 140 vs < 180 → 主要终点 mRS shift 阴性，但功能结局趋势改善
- **ATACH-2 2016**：SBP 110–139 vs 140–179 → 阴性 + 肾不良事件 ↑
- **AHA/ASA 2022**：急性期 **SBP < 140**（1.5 h 内），避免过快降至 < 110；个体化 130–150 区间

### 早期外科
- **STICH I/II**：常规外科 vs 保守 → 阴性
- **MISTIE-III 2019**：微创血肿穿刺 + tPA → 主要终点阴性，技术性达标亚组获益
- **ENRICH 2024**：minimally invasive parafascicular surgery（lobar/basal ganglia <60 mL） → utility-weighted mRS 改善

### 抗凝逆转
- Warfarin：4F-PCC（25–50 IU/kg 按 INR）+ vit K 10 mg IV
- DOAC（dabigatran）：**Idarucizumab** 5 g IV
- DOAC（apixaban/rivaroxaban）：**Andexanet alfa**（贵且可及性差）/ 4F-PCC 50 IU/kg
- Heparin：protamine 1 mg/100 U
- Antiplatelet：**PATCH 2016** 提示输 plt 反而有害；不推荐常规输注（仅术前可考虑）

### 其他
- **SUGAR-ICH**：血糖目标 110–180（NICE-SUGAR 外推安全）
- **DVT 预防**：机械 24 h 内；药物 24–96 h 后稳定再启动
- 颅内压监测：GCS ≤ 8 或临床恶化考虑

---

## 四、Status epilepticus

### 分阶段处理

```
Stage 1（< 5 min）：开始处理
  └ 监测气道、循环、血糖、电解质

Stage 2（5–20 min）：First-line 苯二氮䓬
  ├ Lorazepam 0.1 mg/kg IV（最多 4 mg）
  ├ Midazolam 10 mg IM（无 IV 时）
  └ Diazepam 0.15 mg/kg IV

Stage 3（established，20–40 min）：Second-line（ESETT）
  ├ Levetiracetam 60 mg/kg（max 4.5 g）
  ├ Fosphenytoin 20 mg PE/kg
  └ Valproate 40 mg/kg
  → ESETT 三药等效

Stage 4（refractory，> 40 min）：麻醉
  ├ Midazolam infusion 0.05–2 mg/kg/h
  ├ Propofol infusion 1.5–10 mg/kg/h
  ├ Pentobarbital 1–5 mg/kg/h
  → 目标 EEG burst-suppression × 24–48 h
  → 持续 EEG 监测

Stage 5（super-refractory，> 24 h 麻醉无效）：
  ├ Ketamine 1.5 mg/kg load + 0.3–7.5 mg/kg/h
  ├ Inhaled isoflurane
  └ 寻找潜在病因（autoimmune、抗体相关、PRES、ICH、感染）
```

**EEG**：所有持续 SE / 镇静中怀疑 NCSE → 持续 cEEG。

---

## 五、心脏骤停后管理（与 NICU 重叠）

### TTM2 (NEJM 2021) 后实践
- **目标体温 33 vs 37.5（avoid fever）**：TTM2 → 33 不优于 normothermia + active fever control
- **AHA 2024 / ERC 2024**：TTM 32–36 选择，**严格避免 fever ≥ 37.7 × 72 h**
- 早期 ROSC + 浅昏迷：normothermia + fever control 趋势成为主流
- 持续昏迷 / 严重缺氧损伤：33–34 仍是合理选择

### 神经预后评估
- 至少 72 h 后（无 sedation 残留）
- 多模态：临床（瞳孔、角膜、运动）、SSEP（N20 缺失）、EEG（burst-suppression、status myoclonus）、NSE、MRI（DWI）
- 单一指标不足以宣告差预后

---

## 六、镇静与镇痛（神经重症调整）

- **Propofol**：首选短效，便于神经评估窗
- **Dexmedetomidine**：不抑制呼吸，便于评估；但单用对 ICP↑控制弱
- **Fentanyl / remifentanil**：镇痛
- **避免长 BZD**（除 SE 治疗）
- **Pentobarbital coma**：refractory ICP 终极手段，监测心功能、低血压

---

## 七、24h ICU 神经监测清单

```
全部
  ├ GCS / FOUR score q1h（清醒/浅镇静时）
  ├ 瞳孔反应（自动 pupillometer 优先）q1h
  ├ Na、Glucose、Lactate q4–6h
  ├ 头高 30°、ETT 不压颈
  ├ 容量与 CPP/MAP 目标
  └ DVT 机械预防 + 药物时机评估

TBI / 大面积梗死 / ICH
  ├ ICP / CPP 实时（如有监测）
  ├ PbtO₂ / NIRS（如有）
  └ EVD 引流（如有），高位 0 点对齐外耳道

SAH
  ├ TCD POD 3–14
  ├ NIHSS q4–6h
  └ Nimodipine 60 mg q4h × 21d

SE / 昏迷不明
  └ cEEG，目标背景反应性 / 排除 NCSE
```

---

## 八、关键试验速查

| 主题 | 试验 | 结论 |
|---|---|---|
| TBI craniectomy 早 | DECRA 2011 | unfavorable↑ |
| TBI refractory craniectomy | RESCUEicp 2016 | 死亡率↓，vegetative↑ |
| TBI 低温 | POLAR 2018 | 阴性 |
| TBI TXA | CRASH-3 2019 | 头部相关死亡↓ |
| TBI HTS 持续 | COBI 2021 | 无获益 |
| ICH BP（积极） | INTERACT-2 / ATACH-2 | < 140 安全，结局阴性 |
| ICH 早期外科 | STICH I/II | 阴性 |
| ICH 微创 | MISTIE-III 2019 | 主要终点阴性，达标亚组获益 |
| ICH ENRICH | 2024 | 微创平行分支外科获益 |
| ICH antiplatelet | PATCH 2016 | 输 plt 有害 |
| SAH coil vs clip | ISAT 2002 / 长期 | coil 优 |
| SAH nimodipine | BRANT 经典 | 改善结局 |
| Cardiac arrest TTM | TTM 2013 / TTM2 2021 | 33 不优于 37.5 + fever control |
| SE Stage 3 | ESETT 2019 | LEV/FOS/VPA 三药等效 |
