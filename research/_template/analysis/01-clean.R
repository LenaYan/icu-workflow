# 01-clean.R — 数据清洗
# 输入：data/raw/*.csv （不进 git）
# 输出：data/derived/cohort.rds

source(here::here("analysis", "00-setup.R"))

# ---- 1. 读入原始数据 ----
raw <- read_csv(file.path(DATA_RAW, "extract.csv"),
                show_col_types = FALSE) |>
  janitor::clean_names()

cat("Raw rows:", nrow(raw), "\n")

# ---- 2. 入排筛选（生成 CONSORT/STROBE flow） ----
flow <- tibble(step = character(), n = integer())
flow <- bind_rows(flow, tibble(step = "原始提取", n = nrow(raw)))

cohort <- raw |>
  filter(age >= 18)
flow <- bind_rows(flow, tibble(step = "≥18 岁", n = nrow(cohort)))

cohort <- cohort |>
  filter(!is.na(stay_id), !duplicated(stay_id))   # 一人一次首次入科
flow <- bind_rows(flow, tibble(step = "首次入科去重", n = nrow(cohort)))

# 例：排除 ICU 停留 < 24h
cohort <- cohort |> filter(los_icu >= 1)
flow <- bind_rows(flow, tibble(step = "ICU ≥ 24h", n = nrow(cohort)))

# 排除关键变量缺失
cohort <- cohort |>
  filter(!is.na(apache2), !is.na(sofa_d0))
flow <- bind_rows(flow, tibble(step = "APACHE II / SOFA 完整", n = nrow(cohort)))

write_csv(flow, file.path(OUTPUT_DIR, "flow.csv"))

# ---- 3. 派生变量 ----
cohort <- cohort |>
  mutate(
    sex      = factor(sex, levels = c("F", "M")),
    age_grp  = cut(age, breaks = c(17, 40, 60, 75, Inf),
                   labels = c("18-40", "41-60", "61-75", "76+")),
    bmi_grp  = cut(bmi, breaks = c(0, 18.5, 25, 30, Inf),
                   labels = c("<18.5", "18.5-25", "25-30", "≥30")),
    sofa_grp = cut(sofa_d0, breaks = c(-Inf, 5, 10, 15, Inf),
                   labels = c("0-5", "6-10", "11-15", "≥16")),
    pf_ratio = pao2 / fio2,
    ards_severity = case_when(
      pf_ratio <= 100 ~ "severe",
      pf_ratio <= 200 ~ "moderate",
      pf_ratio <= 300 ~ "mild",
      TRUE ~ "none"
    ) |> factor(levels = c("none", "mild", "moderate", "severe"))
  )

# ---- 4. 缺失值 quick check ----
miss <- cohort |>
  summarise(across(everything(), ~ mean(is.na(.x)) * 100)) |>
  pivot_longer(everything(), names_to = "var", values_to = "miss_pct") |>
  arrange(desc(miss_pct))

write_csv(miss, file.path(OUTPUT_DIR, "missing.csv"))

cat("Variables with >20% missing:\n")
print(miss |> filter(miss_pct > 20))

# ---- 5. 保存 ----
saveRDS(cohort, file.path(DATA_DERIVED, "cohort.rds"))
cat("Final cohort:", nrow(cohort), "rows saved to data/derived/cohort.rds\n")
