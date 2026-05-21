# 00-setup.R — 环境与包加载
# 用法：source("analysis/00-setup.R") 在每个分析脚本最顶端调用

# ---- 版本锁定（推荐用 renv） ----
# 首次：renv::init()
# 协作者：renv::restore()  从 renv.lock 还原
# 新装包后：renv::snapshot()

# ---- 包加载 ----
suppressPackageStartupMessages({
  library(tidyverse)      # dplyr / ggplot2 / tidyr / readr / purrr
  library(here)           # here() 跨平台路径
  library(janitor)        # clean_names()
  library(lubridate)      # 时间处理

  # ICU 临床研究常用
  library(tableone)       # Table 1
  library(survival)       # Cox, KM
  library(survminer)      # ggsurvplot
  library(cmprsk)         # competing risks (Fine-Gray)
  library(MatchIt)        # PSM
  library(WeightIt)       # IPTW
  library(cobalt)         # balance diagnostics (love plot)
  library(mice)           # multiple imputation
  library(broom)          # tidy()
  library(gtsummary)      # 出版级表格
  library(rms)            # nomogram / 限制性立方样条
  library(pROC)           # ROC
  library(PredictABEL)    # 校准
})

# ---- 路径常量 ----
DATA_RAW       <- here("data", "raw")
DATA_DERIVED   <- here("data", "derived")
ANALYSIS_DIR   <- here("analysis")
FIGURES_DIR    <- here("figures")
OUTPUT_DIR     <- here("output")
dir.create(DATA_DERIVED, showWarnings = FALSE)
dir.create(FIGURES_DIR,  showWarnings = FALSE)
dir.create(OUTPUT_DIR,   showWarnings = FALSE)

# ---- 全局选项 ----
options(
  digits = 3,
  scipen = 999,
  knitr.kable.NA = ""
)

# ---- 颜色（统一图表风格） ----
PALETTE <- c(
  intervention = "#1f77b4",
  control      = "#d62728",
  neutral      = "#7f7f7f"
)

# ---- 随机种子（保证可复现） ----
set.seed(20260520)

# ---- Session info（写入日志） ----
sessionInfo() |> capture.output() |>
  writeLines(file.path(OUTPUT_DIR, "session-info.txt"))

message("Setup complete. Packages loaded, paths set.")
