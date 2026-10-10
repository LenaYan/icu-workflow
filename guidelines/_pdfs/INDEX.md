# ICU Guideline & Drug Label PDF Library — Index

Last updated: 2026-10-09. PDFs are local only (git-ignored); this index is tracked.

Purpose: source library for the ima knowledge bases ("Guidelines & Consensus" and
"Drug Labels") and for local lookup by the `icu-consultant` agent.

## Upload rules for ima

| Folder | Upload to ima? | Reason |
|---|---|---|
| Topic folders (sepsis, ARDS-ventilation, …) | Yes | Current versions |
| `china-consensus/` | Yes | Most are English OA versions — note `-EN` suffix |
| `drug-labels/{antimicrobials,anticoagulants,…}/` (`-CN`) | Yes | NMPA-approved Chinese labels |
| `drug-labels/_FDA-reference-only/` | **No** | US labels; doses, units and indications differ from NMPA (see caveats) |
| `_superseded/` | **No** | Replaced by newer versions; would pollute RAG retrieval |

## Inventory (57 PDFs current + 3 superseded)

### Sepsis
| File | Pages | Source |
|---|---|---|
| — | — | **SSC 2026 adult & pediatric not yet downloaded** — see manual list |

### ARDS & ventilation
| File | Pages | DOI |
|---|---|---|
| ARDS-ventilation/2023-ESICM-ARDS-guideline.pdf | 33 | 10.1007/s00134-023-07050-7 |
| ARDS-ventilation/2024-ATS-ARDS-management-guideline-update.pdf | 13 | 10.1164/rccm.202311-2011ST |
| ARDS-ventilation/2024-Global-ARDS-definition.pdf | 11 | 10.1164/rccm.202303-0558WS |

### Kidney / AKI / CRRT
| File | Pages | DOI / URL |
|---|---|---|
| kidney-AKI-CRRT/2012-KDIGO-AKI-guideline.pdf | 141 | kdigo.org (2026 update in public review; final not yet released) |
| kidney-AKI-CRRT/2020-KDIGO-controversies-in-AKI-conference.pdf | 32 | 10.1016/j.kint.2020.04.020 |
| kidney-AKI-CRRT/2024-KDIGO-CKD-guideline.pdf | 199 | kdigo.org |
| kidney-AKI-CRRT/2026-ADQI-ECMO-AKI-fluid-CRRT-consensus.pdf | 21 | 10.1007/s00134-026-08440-3 |

### Neuro / TBI
| File | Pages | DOI / URL |
|---|---|---|
| neuro-TBI/2016-BTF-severe-TBI-4th-ed.pdf | 244 | braintrauma.org (still current) |
| neuro-TBI/2016-BTF-severe-TBI-4th-ed-executive-summary.pdf | 10 | braintrauma.org |
| neuro-TBI/2019-SIBICC-severe-TBI-ICP-algorithm.pdf | 12 | 10.1007/s00134-019-05805-9 |
| neuro-TBI/2020-SIBICC-TBI-brain-oxygen-ICP-algorithm.pdf | 11 | 10.1007/s00134-019-05900-x |

### Sedation / delirium
| File | Pages | DOI |
|---|---|---|
| sedation-delirium/2018-SCCM-PADIS-guideline.pdf | 50 | 10.1097/CCM.0000000000003299 (2025 focused update not downloaded) |

### Hemodynamics / fluids
| File | Pages | DOI |
|---|---|---|
| hemodynamics-fluids/2026-SRLF-SFC-cardiogenic-shock-expert-recommendations.pdf | 19 | 10.1016/j.aicoj.2026.100038 |

### Nutrition
| File | Pages | DOI |
|---|---|---|
| nutrition/2019-ESPEN-ICU-nutrition-guideline.pdf | 32 | 10.1016/j.clnu.2018.08.037 |
| nutrition/2023-ESPEN-ICU-nutrition-guideline-update.pdf | 19 | 10.1016/j.clnu.2023.07.011 |

### Transfusion / coagulation
| File | Pages | DOI |
|---|---|---|
| transfusion-coagulation/2020-ESICM-transfusion-critically-ill-guideline.pdf | 24 | 10.1007/s00134-019-05884-8 |
| transfusion-coagulation/2025-CHEST-RBC-transfusion-critically-ill-guideline.pdf | 13 | 10.1016/j.chest.2024.09.016 |
| transfusion-coagulation/2025-CHEST-plasma-platelet-transfusion-critically-ill-guideline.pdf | 16 | 10.1016/j.chest.2025.02.029 |
| transfusion-coagulation/2023-European-trauma-major-bleeding-coagulopathy-guideline-6th-ed.pdf | 45 | 10.1186/s13054-023-04327-7 |

### Infection / antimicrobials
| File | Pages | DOI |
|---|---|---|
| infection-antimicrobials/2016-ATS-IDSA-HAP-VAP-guideline.pdf | 51 | 10.1093/cid/ciw353 |
| infection-antimicrobials/2023-ERS-ESICM-ESCMID-ALAT-severe-CAP-guideline.pdf | 18 | 10.1007/s00134-023-07033-8 |
| infection-antimicrobials/2020-ESICM-antimicrobial-TDM-position-paper.pdf | 27 | 10.1007/s00134-020-06050-1 |

### General ICU
| File | Pages | DOI |
|---|---|---|
| general-ICU/2017-SCCM-family-centered-care-ICU-guideline.pdf | 114 | 10.1097/CCM.0000000000002169 (accepted manuscript) |
| general-ICU/2024-ESICM-end-of-life-palliative-care-ICU-guideline.pdf | 27 | 10.1007/s00134-024-07579-1 |

### Chinese guidelines & consensus (`china-consensus/`)
| File | Pages | Society | DOI |
|---|---|---|---|
| 2018-CMDA-EM-sepsis-septic-shock-emergency-CN.pdf | 22 | CMDA Emergency Physicians | 10.13201/j.issn.1009-5918.2018.09.001 |
| 2022-CRHA-sepsis-immunosuppression-monitoring-treatment-EN.pdf | 18 | CRHA Shock & Sepsis | 10.1186/s40779-022-00430-y |
| 2024-CSCCM-ICU-nutrition-assessment-monitoring-EN.pdf | 23 | CSCCM | 10.1016/j.jointm.2023.12.002 |
| 2023-CSCCM-BP-management-critically-ill-EN.pdf | 19 | CSCCM | 10.1016/j.jointm.2023.06.001 |
| 2022-CNexperts-glycemic-management-critically-ill-EN.pdf | 15 | Chinese expert panel | 10.1016/j.jointm.2022.06.001 |
| 2023-CMDA-EM-CRRT-regional-citrate-anticoagulation-EN.pdf | 19 | CMDA Emergency Physicians | 10.1186/s40779-023-00457-9 |
| 2020-PLA-CCM-thrombocytopenia-adult-ICU-EN.pdf | 19 | PLA Critical Care | 10.1186/s40779-020-00244-w |
| 2021-CSCCM-albumin-critically-ill-EN.pdf | 16 | CSCCM | 10.1097/cm9.0000000000001661 |
| 2024-CSCCM-neurocritical-sedation-analgesia-EN.pdf | 3 | CSCCM + NCQC | 10.1097/cm9.0000000000003084 (short form; full text in supplement) |
| 2015-CSN-neurosurgical-critical-care-management-EN.pdf | 16 | CSN | 10.4103/0366-6999.156146 |
| 2026-CSCCM-CLABSI-part1-diagnosis-prevention-EN.pdf | 10 | CSCCM | 10.1016/j.jointm.2025.10.008 |
| 2026-CSCCM-CLABSI-part2-treatment-EN.pdf | 17 | CSCCM | 10.1016/j.jointm.2025.10.009 |

### Drug labels — NMPA Chinese (`drug-labels/`)
| File | Pages | Last revised |
|---|---|---|
| antimicrobials/ceftazidime-avibactam-Pfizer-Zavicefta-2025-CN.pdf | 36 | 2025-12-25 |
| antimicrobials/linezolid-injection-Pfizer-Zyvox-2025-CN.pdf | 30 | 2025-07-01 |
| antimicrobials/tigecycline-Pfizer-Tygacil-2026-CN.pdf | 36 | 2026-06-08 |
| antimicrobials/voriconazole-injection-Pfizer-Vfend-2026-CN.pdf | 33 | 2026-07-28 |
| anticoagulants/enoxaparin-Sanofi-Clexane-2026-CN.pdf | 26 | 2026-08-12 |
| anticoagulants/dalteparin-Pfizer-Fragmin-2025-CN.pdf | 10 | 2025-07-01 |

### Drug labels — FDA reference only (`drug-labels/_FDA-reference-only/`, do not upload)
meropenem, imipenem-cilastatin, piperacillin-tazobactam (premixed solution label),
vancomycin, polymyxin B, caspofungin, norepinephrine, vasopressin, dobutamine,
dexmedetomidine, propofol, remifentanil, heparin, argatroban, bivalirudin (15 files).

Known high-risk differences vs. NMPA labels:
- Norepinephrine: US labels dose as base; Chinese labels as bitartrate (~2x conversion).
- Polymyxin B: US label is outdated; dosing differs substantially from Chinese label and 2019 international consensus.
- Argatroban: US indication is HIT; China indication includes acute ischemic stroke.
- Remifentanil: US label includes ICU sedation content; China indication is general anesthesia only.

Not found at all: levosimendan (not FDA-approved; no public Chinese label PDF located).

### Superseded (`_superseded/`, do not upload)
| File | Replaced by |
|---|---|
| 2021-SSC-adult-sepsis-guideline.pdf | SSC 2026 adult |
| 2020-SSC-pediatric-sepsis-guideline.pdf | SSC 2026 pediatric |
| 2014-ESICM-circulatory-shock-hemodynamic-monitoring-consensus.pdf | ESICM 2025 circulatory shock guideline |

## Manual download list (browser or institutional access)

Priority A — current core guidelines, publisher free-to-read but blocked for scripts:
| Document | DOI |
|---|---|
| SSC 2026 adult (ICM / CCM) | 10.1007/s00134-026-08361-1 · 10.1097/CCM.0000000000007075 |
| SSC 2026 pediatric (ICM / PCCM) | 10.1007/s00134-026-08360-2 · 10.1097/PCC.0000000000003927 |
| ESICM 2025 circulatory shock & hemodynamic monitoring | 10.1007/s00134-025-08137-z |
| ESICM fluid therapy Part 1 (2024) / Part 2 (2025) / Part 3 (2025) | 10.1007/s00134-024-07369-9 · 10.1007/s00134-025-07840-1 · 10.1007/s00134-025-08058-x |
| SCCM PADIS 2025 focused update | 10.1097/CCM.0000000000006574 |
| SCCM/ESICM corticosteroids 2024 focused update | 10.1097/CCM.0000000000006172 |

Priority B — international, secondary:
| Document | DOI / URL |
|---|---|
| Sepsis-3 (JAMA 2016) | 10.1001/jama.2016.0287 |
| AHA/ASA aSAH 2023 | 10.1161/STR.0000000000000436 |
| AHA/ASA ICH 2022 | 10.1161/STR.0000000000000407 |
| ERS/ESICM/ESCMID/ALAT HAP/VAP 2017 | 10.1183/13993003.00582-2017 |
| ASPEN/SCCM critical care nutrition 2016 / ASPEN 2022 | 10.1177/0148607115621863 · 10.1002/jpen.2267 |
| ISTH DIC definition update 2025 | 10.1016/j.jtha.2025.03.038 |
| ABCDEF bundle / ICU Liberation (CCM 2019) | 10.1097/CCM.0000000000003482 |
| CIRCI guideline 2017 (ICM version, bronze OA) | 10.1007/s00134-017-4919-5 |
| IDSA 2026 AMR Gram-negative guidance (HTML only) | idsociety.org/practice-guideline/amr-guidance/ |

Priority C — Chinese originals (yiigle / CMA journals; institutional access):
| Document | DOI |
|---|---|
| CSCCM adult ICU analgesia & sedation guideline 2018 | 10.3760/cma.j.issn.2095-4352.2018.06.001 |
| Chinese AKI clinical practice guideline 2023 (Natl Med J China) | 10.3760/cma.j.cn112137-20230802-00133 |
| CRRT replacement/dialysate fluid guideline 2026 | 10.3760/cma.j.cn112137-20260108-00083 |
| CRE microbiological diagnosis & treatment consensus 2026 | 10.3760/cma.j.cn112137-20260128-00313 |
| Sepsis-induced coagulopathy Chinese consensus 2024 (PLA Med J; may be free in browser) | 10.11855/j.issn.0577-7402.1189.2024.0918 |
| CRGNB infection guideline 2023 (JMII, OA in browser) | 10.1016/j.jmii.2023.01.017 |
| Polymyxin B TDM Chinese consensus 2023 (PMC10260281, OA in browser) | 10.1631/jzus.b2200466 |
| Critical care ultrasound / hemodynamic therapy / ARDS ventilation CSCCM consensus | Not verified — search yiigle |

Drug labels — NMPA Chinese versions still needed (CDE "中国上市药品目录集", hospital pharmacy, or manufacturer medical affairs):
meropenem, imipenem-cilastatin, piperacillin-tazobactam, vancomycin, polymyxin B,
caspofungin, norepinephrine, pituitrin / terlipressin (verify AVP NMPA status),
dobutamine, levosimendan, dexmedetomidine, propofol, remifentanil, heparin,
argatroban, bivalirudin. Prefer the manufacturer actually stocked by the hospital.
