# Guideline & Drug Label Library — Backlog

Gaps remaining after the 2026-10-09/10/11 download rounds. Source library index: `INDEX.md`.

When you obtain a file: save it under the target folder below using the
`YYYY-ORG-topic.pdf` naming convention, verify it is a real PDF with the expected
title, then update `INDEX.md` (add to Inventory, remove from this backlog).

## 1. Paywalled international guidelines — hospital library / institutional access

Springer/ICM, confirmed paywalled on 2026-10-10 (EUR 39.95 per article; the earlier
script failures were bot challenges in front of a paywall, not free-to-read content):

| Document | DOI | Target folder |
|---|---|---|
| ESICM 2025 circulatory shock & hemodynamic monitoring (Monnet, ICM 51:1971) | 10.1007/s00134-025-08137-z | hemodynamics-fluids/ |
| ESICM fluid therapy Part 1: choice of resuscitation fluids (2024) | 10.1007/s00134-024-07369-9 | hemodynamics-fluids/ |
| ESICM fluid therapy Part 2: volume of resuscitation fluids (2025) | 10.1007/s00134-025-07840-1 | hemodynamics-fluids/ |
| ESICM fluid therapy Part 3: fluid removal at de-escalation (2025) | 10.1007/s00134-025-08058-x | hemodynamics-fluids/ |

Also paywalled / not OA (lower priority):
- NCS 2023 aneurysmal SAH guideline — 10.1007/s12028-023-01713-5 → neuro-TBI/
- NCS 2025 ICH seizure prophylaxis — 10.1007/s12028-024-02183-z → neuro-TBI/
- Berlin ARDS definition 2012 (JAMA) — 10.1001/jama.2012.5669 → ARDS-ventilation/
- ESAIC severe peri-operative bleeding 2023 — 10.1097/EJA.0000000000001803 → transfusion-coagulation/
- ISTH DIC definition update 2025 — 10.1016/j.jtha.2025.03.038 → transfusion-coagulation/
- ASPEN/SCCM nutrition 2016 — 10.1177/0148607115621863; ASPEN 2022 — 10.1002/jpen.2267 → nutrition/
- ABCDEF bundle / ICU Liberation (CCM 2019) — 10.1097/CCM.0000000000003482 → general-ICU/
- CIRCI guideline 2017 (ICM version) — 10.1007/s00134-017-4919-5 → hemodynamics-fluids/
- SCCM clinical deterioration outside ICU 2024 — 10.1097/CCM.0000000000006072 → general-ICU/

## 2. Chinese originals — yiigle / CMA journals (institutional account)

| Document | DOI | Target folder |
|---|---|---|
| CSCCM adult ICU analgesia & sedation guideline 2018 | 10.3760/cma.j.issn.2095-4352.2018.06.001 | china-consensus/ |
| Chinese AKI clinical practice guideline 2023 (Natl Med J China) | 10.3760/cma.j.cn112137-20230802-00133 | china-consensus/ |
| CRRT replacement/dialysate fluid guideline 2026 | 10.3760/cma.j.cn112137-20260108-00083 | china-consensus/ |
| CRE microbiological diagnosis & treatment consensus 2026 | 10.3760/cma.j.cn112137-20260128-00313 | china-consensus/ |
| Sepsis-induced coagulopathy consensus 2024 (PLA Med J; may be free in browser) | 10.11855/j.issn.0577-7402.1189.2024.0918 | china-consensus/ |
| Antimicrobial PK/PD clinical application expert consensus 2018 (Chinese J Tuberc Respir Dis 41(6):409-446; yiigle returns 401 安全验证 for scripts, tried 2026-10-11) | 10.3760/cma.j.issn.1001-0939.2018.06.004 | china-consensus/ |
| CRRT antimicrobial dosing optimization expert consensus 2024 (中华肾脏病杂志; no English OA version; Chinese original only) | 10.3760/cma.j.cn441217-20230906-00906 | drug-reference/ |
| Chinese emergency sepsis-DIC consensus 2017 | 10.3760/cma.j.issn.2095-4352.2017.07.001 | china-consensus/ |
| Sepsis-induced immunosuppression consensus 2020 (Chinese original; 2022 English OA version already in library) | 10.3760/cma.j.cn121430-20201123-00719 | china-consensus/ |
| Vancomycin TDM guideline 2020 (Chinese Pharmacological Society; CID, not OA) | 10.1093/cid/ciaa1536 | china-consensus/ |
| Critical care ultrasound consensus; hemodynamic therapy consensus; CSCCM ARDS ventilation consensus | Not verified — search yiigle (中华内科杂志 / 中华危重病急救医学) | china-consensus/ |

Free-in-browser but bot-blocked (retry via browser):
- CRGNB infection guideline 2023 (JMII English original, OA; ScienceDirect Cloudflare managed challenge did not clear in headed Chrome on 2026-10-11 — Chinese version already in library as china-consensus/2024-CRGNB-infection-guideline-CN.pdf) — 10.1016/j.jmii.2023.01.017 → china-consensus/
- ERS/ESICM/ESCMID/ALAT HAP/VAP 2017 (ERJ) — 10.1183/13993003.00582-2017 → infection-antimicrobials/

Optional extras noted during download:
- 中国重症医学科建设与管理指南 2025 (J Intensive Med, PMC12925910) — administrative, not clinical
- Pfizer China also has linezolid tablets (id=14482) and voriconazole tablets/oral suspension (id=14450) labels
- IDSA 2026 AMR Gram-negative guidance is HTML-only: idsociety.org/practice-guideline/amr-guidance/ (no full PDF published)

## 3. NMPA Chinese drug labels — CDE 中国上市药品目录集 / hospital pharmacy / manufacturer medical affairs

14 drugs still only have FDA reference versions (in `drug-labels/_FDA-reference-only/`,
do NOT upload to ima). Get the label for the manufacturer actually stocked by the hospital:

- Antimicrobials: meropenem (住友 美平), imipenem-cilastatin (MSD 泰能),
  piperacillin-tazobactam (辉瑞 特治星), vancomycin, polymyxin B, caspofungin (MSD 科赛斯)
- Vasoactive/sedation: norepinephrine, pituitrin / terlipressin (verify whether AVP
  itself has NMPA approval), dobutamine, levosimendan (no FDA label exists either —
  check Orion Simdax or domestic makers 恒瑞/齐鲁), dexmedetomidine (恒瑞 艾贝宁),
  propofol (费卡 竟安/静安), remifentanil
- Anticoagulants: heparin sodium, argatroban (田边三菱 诺保思泰), bivalirudin (信立泰 泰加宁)

Note: CDE website has a JS anti-bot challenge that defeated both curl and headless
Chrome on 2026-10-09; a manual browser session works.

## 4. Watch list — upcoming versions

- **KDIGO AKI guideline**: 2026 revision finished public review (closed 2026-05-11);
  final not yet released. Replace `kidney-AKI-CRRT/2012-KDIGO-AKI-guideline.pdf` when published.
- BTF severe TBI: 4th ed (2016) still current; BTF 2026 published Penetrating TBI 2nd ed
  (10.1227/neu.0000000000003738) — separate guideline, consider adding if relevant.
