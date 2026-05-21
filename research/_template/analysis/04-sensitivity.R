# 04-sensitivity.R — 敏感性分析
# 审稿人最常问：你的结论稳健吗？

source(here::here("analysis", "00-setup.R"))

cohort <- readRDS(file.path(DATA_DERIVED, "cohort.rds"))

EXPOSURE <- "exposure"
OUTCOME  <- "death_28d"
covars   <- c("age", "sex", "apache2", "sofa_d0", "lactate_d0")

# =============================================================
# 1. 不同入排标准
# =============================================================
sens_inex <- list(
  full        = cohort,
  excl_early  = cohort |> filter(los_icu >= 2),   # 排除早期死亡
  excl_dnr    = cohort |> filter(is.na(dnr) | dnr == 0),
  high_sev    = cohort |> filter(sofa_d0 >= 6)
)

# =============================================================
# 2. E-value（未测量混杂的最小强度）— EValue 包
# =============================================================
# install.packages("EValue")
library(EValue)
# 例：OR = 1.6, 95% CI 1.2–2.1
evalues.OR(est = 1.6, lo = 1.2, hi = 2.1, rare = FALSE)

# =============================================================
# 3. 多重插补 (MICE)
# =============================================================
imp <- mice(cohort |> select(all_of(c(OUTCOME, EXPOSURE, covars))),
            m = 20, seed = 20260520, printFlag = FALSE)

fit_mi <- with(imp,
  glm(as.formula(paste(OUTCOME, "~", EXPOSURE, "+",
                       paste(covars, collapse = "+"))),
      family = binomial)
)
pool_mi <- summary(pool(fit_mi), conf.int = TRUE, exponentiate = TRUE)
print(pool_mi |> filter(term == EXPOSURE))

# =============================================================
# 4. 不同 PSM 参数（caliper / ratio）
# =============================================================
sens_psm <- list()
for (cal in c(0.1, 0.2, 0.3)) {
  for (ratio in c(1, 2, 3)) {
    m <- matchit(as.formula(paste(EXPOSURE, "~", paste(covars, collapse = "+"))),
                 data = cohort, method = "nearest",
                 distance = "logit", caliper = cal, ratio = ratio)
    md <- match.data(m)
    fit <- glm(as.formula(paste(OUTCOME, "~", EXPOSURE)),
               data = md, family = binomial, weights = weights)
    tidy_fit <- broom::tidy(fit, exponentiate = TRUE, conf.int = TRUE) |>
      filter(term == EXPOSURE)
    sens_psm[[paste0("cal", cal, "_r", ratio)]] <- tidy_fit
  }
}
bind_rows(sens_psm, .id = "spec") |> print()

# =============================================================
# 5. 主结局亚组（事先指定）— Forest plot
# =============================================================
subgroups <- list(
  age_grp  = c("18-40", "41-60", "61-75", "76+"),
  sex      = c("F", "M"),
  ards_severity = c("mild", "moderate", "severe")
)

forest_data <- map_dfr(names(subgroups), function(var) {
  map_dfr(subgroups[[var]], function(lev) {
    sub <- cohort |> filter(.data[[var]] == lev)
    if (nrow(sub) < 30) return(NULL)
    fit <- glm(as.formula(paste(OUTCOME, "~", EXPOSURE)),
               data = sub, family = binomial)
    tidy <- broom::tidy(fit, exponentiate = TRUE, conf.int = TRUE) |>
      filter(term == EXPOSURE)
    tibble(subgroup_var = var, level = lev, n = nrow(sub),
           OR = tidy$estimate, lo = tidy$conf.low, hi = tidy$conf.high,
           p = tidy$p.value)
  })
})
write_csv(forest_data, file.path(OUTPUT_DIR, "subgroup-forest.csv"))
