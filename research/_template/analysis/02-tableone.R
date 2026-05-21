# 02-tableone.R — Table 1（基线特征）
# 输出：output/table1.{csv,docx}

source(here::here("analysis", "00-setup.R"))

cohort <- readRDS(file.path(DATA_DERIVED, "cohort.rds"))

# ---- 暴露 / 分组变量 ----
GROUP_VAR <- "exposure"  # 改成你的暴露变量

# ---- 变量分类 ----
vars_cont  <- c("age", "bmi", "apache2", "sofa_d0", "lactate_d0",
                "pf_ratio", "los_icu", "los_hosp")
vars_cat   <- c("sex", "age_grp", "ards_severity",
                "mech_vent", "vasopressor", "crrt")
vars_nonnormal <- c("apache2", "sofa_d0", "lactate_d0",
                    "los_icu", "los_hosp")   # 非正态用中位数

all_vars <- c(vars_cont, vars_cat)

# ---- tableone ----
t1 <- CreateTableOne(
  vars = all_vars,
  strata = GROUP_VAR,
  data = cohort,
  factorVars = vars_cat,
  addOverall = TRUE,
  test = TRUE,
  smd = TRUE          # standardized mean difference（PSM 前后必报）
)

# 打印（控制台）
print(t1, nonnormal = vars_nonnormal, smd = TRUE, quote = FALSE, noSpaces = TRUE)

# 导出 CSV
t1_mat <- print(t1, nonnormal = vars_nonnormal, smd = TRUE,
                quote = FALSE, noSpaces = TRUE, printToggle = FALSE)
write.csv(t1_mat, file.path(OUTPUT_DIR, "table1.csv"))

# ---- gtsummary 版（更适合发表） ----
t1_gt <- cohort |>
  select(all_of(c(all_vars, GROUP_VAR))) |>
  tbl_summary(
    by = all_of(GROUP_VAR),
    type = list(all_of(vars_cont) ~ "continuous"),
    statistic = list(
      all_continuous() ~ "{median} ({p25}, {p75})",
      all_categorical() ~ "{n} ({p}%)"
    ),
    missing = "no"
  ) |>
  add_overall() |>
  add_p() |>
  add_difference() |>
  modify_header(label = "**Variable**") |>
  bold_labels()

t1_gt |> as_flex_table() |> flextable::save_as_docx(
  path = file.path(OUTPUT_DIR, "table1.docx")
)

cat("Table 1 written to output/table1.csv and table1.docx\n")
