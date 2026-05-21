# 03-primary.R — 主分析
# 默认骨架：Cox + competing risks + PSM/IPTW
# 按你的设计删除/保留对应模块

source(here::here("analysis", "00-setup.R"))

cohort <- readRDS(file.path(DATA_DERIVED, "cohort.rds"))

EXPOSURE <- "exposure"
OUTCOME  <- "death_28d"        # 主结局（二元）
TIME     <- "time_to_event"    # 时间-事件型
CR_EVENT <- "event_type"       # 0=censored, 1=event, 2=competing

# 协变量（事先指定 — pre-specified）
covars <- c("age", "sex", "apache2", "sofa_d0",
            "lactate_d0", "mech_vent", "vasopressor")

# =============================================================
# 1. 描述性 — primary outcome 粗发生率
# =============================================================
cohort |>
  group_by(.data[[EXPOSURE]]) |>
  summarise(
    n = n(),
    events = sum(.data[[OUTCOME]] == 1),
    rate = mean(.data[[OUTCOME]] == 1)
  ) |>
  print()

# =============================================================
# 2. Logistic（如结局是二元、随访时间一致）
# =============================================================
fml_logit <- as.formula(
  paste(OUTCOME, "~", EXPOSURE, "+", paste(covars, collapse = "+"))
)
m_logit <- glm(fml_logit, data = cohort, family = binomial)

logit_tbl <- broom::tidy(m_logit, exponentiate = TRUE, conf.int = TRUE) |>
  filter(term == EXPOSURE)
print(logit_tbl)

# =============================================================
# 3. Cox（如有时间-事件）
# =============================================================
fml_cox <- as.formula(
  paste("Surv(", TIME, ",", OUTCOME, ") ~",
        EXPOSURE, "+", paste(covars, collapse = "+"))
)
m_cox <- coxph(fml_cox, data = cohort)

# PH 假设
ph <- cox.zph(m_cox); print(ph)
# 如违反 PH：考虑分层、时间相关协变量、parametric flexible models

cox_tbl <- broom::tidy(m_cox, exponentiate = TRUE, conf.int = TRUE) |>
  filter(term == EXPOSURE)
print(cox_tbl)

# =============================================================
# 4. Competing risks (Fine-Gray)
# 例：ICU 死亡 vs 出院（死亡是竞争事件影响 RRT 撤离）
# =============================================================
if (CR_EVENT %in% names(cohort)) {
  fg_cov <- model.matrix(
    as.formula(paste("~", EXPOSURE, "+", paste(covars, collapse = "+"))),
    data = cohort
  )[, -1]

  m_fg <- crr(
    ftime  = cohort[[TIME]],
    fstatus = cohort[[CR_EVENT]],
    cov1 = fg_cov,
    failcode = 1, cencode = 0
  )
  print(summary(m_fg))
}

# =============================================================
# 5. Propensity Score Matching (PSM)
# =============================================================
ps_formula <- as.formula(paste(EXPOSURE, "~", paste(covars, collapse = "+")))

m_match <- matchit(
  ps_formula, data = cohort,
  method = "nearest", distance = "logit",
  caliper = 0.2, ratio = 1, replace = FALSE
)

# Balance diagnostic
bal.tab(m_match, un = TRUE, m.threshold = 0.1)
love.plot(m_match, threshold = 0.1, abs = TRUE,
          var.order = "unadjusted") |>
  ggsave(file.path(FIGURES_DIR, "love-plot.pdf"),
         plot = _, width = 6, height = 6)

matched <- match.data(m_match)

# 匹配后再跑主模型
m_logit_psm <- glm(fml_logit, data = matched, family = binomial,
                   weights = weights)
broom::tidy(m_logit_psm, exponentiate = TRUE, conf.int = TRUE) |>
  filter(term == EXPOSURE) |> print()

# =============================================================
# 6. IPTW（用 WeightIt 更稳健）
# =============================================================
w <- weightit(ps_formula, data = cohort, method = "ps",
              estimand = "ATE", stabilize = TRUE)

# Balance
bal.tab(w, un = TRUE, m.threshold = 0.1, v.threshold = 1.25)

cohort$iptw <- w$weights
m_iptw <- glm(fml_logit, data = cohort, family = quasibinomial,
              weights = iptw)
broom::tidy(m_iptw, exponentiate = TRUE, conf.int = TRUE) |>
  filter(term == EXPOSURE) |> print()

# =============================================================
# 7. 汇总主结果表（适合直接搬到 Table 2）
# =============================================================
results <- bind_rows(
  broom::tidy(m_logit,    exponentiate = TRUE, conf.int = TRUE) |>
    filter(term == EXPOSURE) |> mutate(model = "Crude/MV logistic"),
  broom::tidy(m_cox,      exponentiate = TRUE, conf.int = TRUE) |>
    filter(term == EXPOSURE) |> mutate(model = "Cox PH"),
  broom::tidy(m_logit_psm, exponentiate = TRUE, conf.int = TRUE) |>
    filter(term == EXPOSURE) |> mutate(model = "PSM 1:1"),
  broom::tidy(m_iptw,     exponentiate = TRUE, conf.int = TRUE) |>
    filter(term == EXPOSURE) |> mutate(model = "IPTW (ATE)")
)
write_csv(results, file.path(OUTPUT_DIR, "primary-results.csv"))
