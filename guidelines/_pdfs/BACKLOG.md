# Guideline & Drug Label Library — Backlog

Gaps remaining after the 2026-10-09/10/11 download rounds. Source library index: `INDEX.md`.

Scope note (2026-10-13): sections 1–4 track the guideline/drug-label PDF library; sections 5–6 track non-guideline knowledge assets identified in the 2026-10-13 knowledge-base review (ima 医学知识库 currently holds 47,818 items; subscribed third-party KBs trimmed to 青禾重症 / 医院AI药师 / 临床医学教材第十版 as the actively queried set).

When you obtain a file: save it under the target folder below using the
`YYYY-ORG-topic.pdf` naming convention, verify it is a real PDF with the expected
title, then update `INDEX.md` (add to Inventory, remove from this backlog).

## 1. Paywalled international guidelines — hospital library / institutional access

Springer/ICM, confirmed paywalled on 2026-10-10 (EUR 39.95 per article; the earlier
script failures were bot challenges in front of a paywall, not free-to-read content):

| Document | DOI | Target folder |
|---|---|---|
| ESICM fluid therapy Part 3: fluid removal at de-escalation (2025) | 10.1007/s00134-025-08058-x | hemodynamics-fluids/ |

Obtained 2026-10-13 via EUR/Erasmus repository versions (no longer needed): ESICM 2025
circulatory shock guideline, ESICM fluid therapy Part 1 (2024) and Part 2 (2025).

Also paywalled / not OA (lower priority):
- NCS 2023 aneurysmal SAH guideline — 10.1007/s12028-023-01713-5 → neuro-TBI/
- NCS 2025 ICH seizure prophylaxis — 10.1007/s12028-024-02183-z → neuro-TBI/
- Berlin ARDS definition 2012 (JAMA) — 10.1001/jama.2012.5669 → ARDS-ventilation/
- ESAIC severe peri-operative bleeding 2023 — 10.1097/EJA.0000000000001803 → transfusion-coagulation/
- ASPEN/SCCM nutrition 2016 — 10.1177/0148607115621863 → nutrition/ (ASPEN 2022 obtained 2026-10-13)
- ABCDEF bundle / ICU Liberation (CCM 2019) — 10.1097/CCM.0000000000003482 → general-ICU/
- CIRCI guideline 2017 (ICM version) — 10.1007/s00134-017-4919-5 → hemodynamics-fluids/
- SCCM clinical deterioration outside ICU 2024 — 10.1097/CCM.0000000000006072 → general-ICU/

## 2. Chinese originals — yiigle / CMA journals (institutional account)

| Document | DOI | Target folder |
|---|---|---|
| CRRT replacement/dialysate fluid guideline 2026 — HTML full-text archive saved 2026-10-13 (`china-consensus/2026-CRRT-prescription-fluid-guideline-CN.html`, all 22 recommendations); journal-layout PDF still wanted (medlive 38729 / yiigle institutional) | 10.3760/cma.j.cn112137-20260108-00083 | china-consensus/ |
| Sepsis-induced coagulopathy consensus 2024 (PLA Med J; may be free in browser) | 10.11855/j.issn.0577-7402.1189.2024.0918 | china-consensus/ |
| Chinese emergency sepsis-DIC consensus 2017 | 10.3760/cma.j.issn.2095-4352.2017.07.001 | china-consensus/ |
| Sepsis-induced immunosuppression consensus 2020 (Chinese original; 2022 English OA version already in library) | 10.3760/cma.j.cn121430-20201123-00719 | china-consensus/ |
| Vancomycin TDM guideline 2020 (Chinese Pharmacological Society; CID, not OA) | 10.1093/cid/ciaa1536 | china-consensus/ |
| Critical care ultrasound consensus; hemodynamic therapy consensus; CSCCM ARDS ventilation consensus | Not verified — search yiigle (中华内科杂志 / 中华危重病急救医学) | china-consensus/ |

Obtained 2026-10-13 (via public mirror/repost sites, verified against journal layout):
CSCCM ICU analgesia & sedation 2018, Chinese AKI guideline 2023, CRE consensus 2026,
antimicrobial PK/PD consensus 2018 (**scanned PDF, replace with text version if found**),
CRRT antimicrobial dosing consensus 2024.

Free-in-browser but bot-blocked (retry via browser):
- CRGNB infection guideline 2023 (JMII English original, OA; ScienceDirect Cloudflare managed challenge did not clear in headed Chrome on 2026-10-11 — Chinese version already in library as china-consensus/2024-CRGNB-infection-guideline-CN.pdf) — 10.1016/j.jmii.2023.01.017 → china-consensus/
- ERS/ESICM/ESCMID/ALAT HAP/VAP 2017 (ERJ) — 10.1183/13993003.00582-2017 → infection-antimicrobials/

Optional extras noted during download:
- 中国重症医学科建设与管理指南 2025 (J Intensive Med, PMC12925910) — administrative, not clinical
- Pfizer China also has linezolid tablets (id=14482) and voriconazole tablets/oral suspension (id=14450) labels
- IDSA 2026 AMR Gram-negative guidance is HTML-only: idsociety.org/practice-guideline/amr-guidance/ (no full PDF published)

## 3. NMPA Chinese drug labels — CDE 中国上市药品目录集 / hospital pharmacy / manufacturer medical affairs

13 drugs obtained 2026-10-13 as **MD transcriptions** from public label databases
(yaozh.com, manufacturer pages; NMPA approval numbers recorded), now under
`drug-labels/*/` as `*-NMPA-CN.md`: meropenem, imipenem-cilastatin,
piperacillin-tazobactam, cefoperazone-sulbactam, vancomycin, norepinephrine, propofol,
dexmedetomidine, midazolam, fentanyl, remifentanil, heparin, argatroban.
These are interim — replace with official label PDFs when available (meropenem MD lacks
the PK section; vancomycin PK tables were images).

Still nothing (only FDA reference versions in `drug-labels/_FDA-reference-only/`,
do NOT upload to ima):

- Antimicrobials: polymyxin B, caspofungin (MSD 科赛斯)
- Vasoactive/sedation: pituitrin / terlipressin (verify whether AVP
  itself has NMPA approval), dobutamine, levosimendan (no FDA label either —
  check Orion Simdax or domestic makers 恒瑞/齐鲁)
- Anticoagulants: bivalirudin (信立泰 泰加宁)

Note: CDE website has a JS anti-bot challenge that defeated both curl and headless
Chrome on 2026-10-09; a manual browser session works.

## 4. Watch list — upcoming versions

- **KDIGO AKI guideline**: 2026 revision finished public review (closed 2026-05-11);
  final not yet released. Replace `kidney-AKI-CRRT/2012-KDIGO-AKI-guideline.pdf` when published.
- BTF severe TBI: 4th ed (2016) still current; BTF 2026 published Penetrating TBI 2nd ed
  (10.1227/neu.0000000000003738) — separate guideline, consider adding if relevant.

## 5. 院内知识资产（非指南类；2026-10-13 知识库盘点新增）

ima 医学知识库目前只有"通用证据层"（指南/说明书），缺"本院实践层"。按高频 × 高风险排序，均为科室/院内渠道获取，不涉及 PHI：

| 资产 | 用途 | 获取途径 | 优先级 |
|---|---|---|---|
| **本院药敏谱**（年度 antibiogram + ICU 病区分离株数据） | 经验性抗感染方案的地基；指南给通用方案，本院耐药谱决定起手药 | 检验科/院感科年度报告 | ★★★ 最高 |
| **静配/输注手册**（浓度、相容性、输注速度、避光、配伍禁忌） | 夜班高频问题；护士执行核对 | 静配中心/药剂科 | ★★★ |
| **设备操作卡**（本院在用机型的呼吸机、CRRT、ECMO、IABP、超声：操作、报警、排障） | 指南不覆盖"这台机器报警怎么办" | 设备科/厂家随机手册 | ★★ |
| **科室 SOP**（镇静镇痛、CRRT 抗凝、ECMO 路径、转入转出标准） | 统一科室实践；新入科培训 | 科室内部文件 | ★★ |
| 医保/DRG 本院文件（限制用药审批、ICU 分组规则） | 医嘱的真实约束 | 医保办 | ★ 可选 |

注意：科室 SOP 两个前提——院内规定允许外传至云端 + 只入私有库（不接第三方 skill 广场、不共享）。药敏谱为聚合数据、无 PHI，脱敏（去院名可选）后可入 ima。

## 6. 文献精读库（landmark trials；2026-10-13 知识库盘点新增）

ima 侧"文献库"分库未建，本地 `literature/notes/` 为空。指南回答"做什么"，原文回答"证据有多硬"——会诊被挑战、做科研设计时靠后者。按亚专科的起点清单（NEJM/JAMA/Lancet/ICM/CCM 原文 PDF）：

- **ARDS/机械通气**：ARMA、PROSEVA、EOLIA、EPVent-2、DEXA-ARDS、ART
- **Sepsis**：ProCESS/ARISE/ProMISe、CLOVERS、CLASSIC、SMART/BaSICS/PLUS、ADRENAL/APROCCHSS、ANDROMEDA-SHOCK(-2)、BLING III、BALANCE、ADAPT-Sepsis、LOVIT
- **AKI/CRRT**：STARRT-AKI、AKIKI/AKIKI2、ELAIN、IDEAL-ICU、RENAL、ATN、RICH
- **NICU**：CRASH-3、DECRA、RESCUEicp、POLAR、INTERACT-2/ATACH-2、ENRICH、TTM/TTM2、ESETT
- **CV/MCS**：DanGer Shock、ECLS-SHOCK、ECMO-CS、IABP-SHOCK II、OptimaCC、SOAP II
- **镇静/谵妄**：PADIS 相关原始试验、MENDS2、SEDCOM、SPICE III
- **营养**：NUTRIREA-2/3、EFFORT、EPaNIC、CALORIES
- **输血**：TRICC、TRISS、FOUNT（如已发表）

工作流：拿到 PDF → 传 ima 文献库（待建分库）→ 本地用 `literature/_templates/single-paper-PICO.md` 写笔记存 `literature/notes/`（命名 `{TRIAL-NAME}-{Year}.md`）→ 每 3–5 篇同主题归并到 `literature/topics/`。多数为付费墙文献，走医院图书馆/机构访问。

## 7. ECG 参考资料缺口（2026-10-15 心电分析工具建库轮）

本轮已入 `ecg/`（26 份，见 INDEX.md）。以下为缺口：

### 7.1 浏览器手动可下（站点 OA 但 WAF/反爬拦脚本）

| 文档 | 出处 / DOI | 途径 |
|---|---|---|
| 中英文标准化心电图首要诊断术语中国专家共识 | 中国循环杂志 2023;38(2):141-145；10.3969/j.issn.1000-3614.2023.02.004 | chinacirculation.org 浏览器打开文章页免费下（阿里云 WAF acw_sc__v2 拦 curl） |
| 心肌梗死心电图诊断标准和报告规范中国专家共识 | 中国循环杂志 2025;40(12):1189-1198；10.3969/j.issn.1000-3614.2025.12.005 | 同上 |
| 2013 HRS/EHRA/APHRS 遗传性心律失常综合征共识 | Heart Rhythm 2013;10(12):1932-63；10.1016/j.hrthm.2013.05.014（bronze OA） | 浏览器：heartrhythmjournal.com/article/S1547527113005523/pdf 或 escardio.org 静态附件 |

### 7.2 需机构权限（万方/CNKI/yiigle/medlive）

| 文档 | 出处 / DOI |
|---|---|
| 心电图危急值2017中国专家共识 | 临床心电学杂志 2017;26(6):401-402 |
| 浙江省心电图危急值标准（2021 修订版） | 心电与循环 2021;40(6)；10.12124/j.issn.2095-3933.2021.6.2021-4775 |
| 远程心电图质量控制中国专家共识（2026 版） | 中国心血管杂志 2026;31(1):4-14；10.3969/j.issn.1007-5410.2026.01.002 |
| 中国心房颤动管理指南（2025） | 中国心脏起搏与心电生理杂志 2025;39(4):273-343 / 中华心律失常学杂志 2025;29(4):265-338 |
| 室性心律失常中国专家共识（2020 主共识；基层版已入库） | 中华心律失常学杂志 2020;24(3):188-258 |

### 7.3 待 ima 服务端恢复后重跑（2026-10-15 20:15 起 ask_knowledge_base 全局"模型失效"）

从自有库拉回 `ecg/papers-own-kb/`（流程已验证可行，27982266 已成功）：42743531（高危 ACS 心电图判读）、40960600（重症超声指导 ICU 房颤）、41965515（ICU 新发房颤 ECG 定义）、34854319（多模态致命性心律失常报警）。

### 7.4 专著/教材（版权书，无合法公开源，不入本 backlog 的下载队列）

黄宛临床心电图学(6版)、301临床心电图学(2版)、Marriott 实用心电图学(11版)、危急重症心电图学(何方田 2021)、心电图解析之路、起搏心电图系列等——订阅库「心电图专家/心电共识/临床心电」内有扫描版，可在 ima 客户端逐份查看/导出（心电图专家库已禁成员看原文）；正版途径为人民卫生出版社等纸质/电子书。判读基准已由 §7 已入库的测量/术语/报告/标准化文件覆盖，专著仅作延伸阅读。
