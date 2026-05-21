---
project: 
PI: 
status: planning | data-cleaning | analysis | writing | revision | submitted | published
target_journal: 
ethics_approval: 
registration: 
last_updated: 
---

# {项目名称}

> 一句话说清楚这个项目要回答什么问题、对谁有意义。

## 1. PICO

| | 内容 |
|---|---|
| **P**opulation | 入组定义 / 排除 / 预期 n |
| **I**ntervention | （或暴露 / 表型） |
| **C**omparator | |
| **O**utcome | Primary / Secondary / Safety |
| **T**ime frame | follow-up 时长 |
| **S**etting | 单中心 / 多中心 / 数据库 (MIMIC-IV / eICU-CRD / 本院 ICU) |

## 2. 研究设计
- 类型：RCT / cohort (prospective/retrospective) / case-control / nested / cross-sectional / meta / 预测模型
- 主要分析方法：Cox / competing risks (Fine-Gray) / mixed model / PSM-IPTW / Bayesian / ML
- 主要 estimand（PATE / ATT / ATE / direct effect）：
- 报告规范：STROBE / CONSORT / TRIPOD / PRISMA / SPIRIT （对应 checklist 在 `checklists/`）

## 3. 样本量
- 假设的效应量与依据：
- α / power：
- 计算工具与代码：`analysis/00-sample-size.R`

## 4. 数据来源
- 数据来源：
- 时间范围：
- 入组流程图 (Fig 1)：`figures/flowchart.pdf`
- 数据字典：`data/data-dictionary.md`

### PHI / 伦理
- [ ] 伦理批准号：
- [ ] 知情同意 / 豁免：
- [ ] 数据去标识化已完成（参见 `checklists/data-deidentification-checklist.md`）
- [ ] 数据存储位置（不进 git）：

## 5. 分析计划（pre-spec）

### Primary
- 分析方法：
- 调整变量（事先确定，避免 data dredging）：
- 缺失值处理：MICE / complete case / 敏感性
- 软件 / 包版本：见 `renv.lock` 或 `requirements.txt`

### Secondary / Sensitivity
- 

### 亚组（事先指定）
- 

### 多重比较
- 

## 6. 进度

| 阶段 | 状态 | 完成日 | 文件 |
|---|---|---|---|
| Protocol / IRB | | | |
| 数据提取 | | | |
| 数据清洗 | | | `analysis/01-clean.R` |
| Table 1 | | | `analysis/02-tableone.R` |
| 主分析 | | | `analysis/03-primary.R` |
| 敏感性分析 | | | `analysis/04-sensitivity.R` |
| 图表 | | | `analysis/99-figures.R` |
| 草稿 | | | `manuscript/main.Rmd` |
| 内部审 | | | |
| 投稿 | | | |
| Revision | | | |

## 7. 作者贡献（ICMJE）
| 作者 | 贡献（4 项：构思/数据/分析/写作） | 顺位 | 通讯 |
|---|---|---|---|
| | | | |

## 8. 关键文献（live list）
- 
- 

## 9. 复现说明
```bash
# R
Rscript analysis/00-setup.R      # 装包，从 renv.lock 还原环境
Rscript analysis/01-clean.R
Rscript analysis/02-tableone.R
Rscript analysis/03-primary.R
Rscript analysis/04-sensitivity.R
Rscript analysis/99-figures.R

# 渲染论文
Rscript -e 'rmarkdown::render("manuscript/main.Rmd")'
```

## 10. 联系
- PI：
- 数据 / 统计：
- 通讯作者：
