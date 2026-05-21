# 99-figures.R — 论文图表（统一风格）
# 目标期刊：CCM/ICM/Chest/AJRCCM —— 单栏 86mm / 双栏 178mm

source(here::here("analysis", "00-setup.R"))

cohort  <- readRDS(file.path(DATA_DERIVED, "cohort.rds"))

# ---- 全局 ggplot 主题 ----
theme_paper <- function(base = 9) {
  theme_bw(base_size = base) +
  theme(
    panel.grid.minor = element_blank(),
    strip.background = element_blank(),
    legend.position  = "top",
    legend.title     = element_blank()
  )
}

# ---- Fig 1：CONSORT / STROBE flow ----
# 推荐手画 + 用 DiagrammeR / Lucid → 导出 PDF 放进 figures/

# ---- Fig 2：KM curve ----
library(survminer)
fit_km <- survfit(Surv(time_to_event, death_28d) ~ exposure, data = cohort)

p_km <- ggsurvplot(
  fit_km, data = cohort,
  risk.table = TRUE, conf.int = TRUE,
  palette = unname(PALETTE[c("intervention", "control")]),
  xlab = "Days from ICU admission",
  ylab = "Survival probability",
  break.time.by = 7, xlim = c(0, 28),
  legend.labs = c("Control", "Intervention"),
  ggtheme = theme_paper()
)
ggsave(file.path(FIGURES_DIR, "fig2-km.pdf"),
       plot = p_km$plot, width = 86 / 25.4, height = 70 / 25.4,
       device = cairo_pdf)

# ---- Fig 3：亚组 forest ----
fd <- read_csv(file.path(OUTPUT_DIR, "subgroup-forest.csv"))

p_forest <- fd |>
  mutate(label = paste0(subgroup_var, ": ", level, " (n=", n, ")")) |>
  ggplot(aes(x = OR, xmin = lo, xmax = hi, y = label)) +
  geom_vline(xintercept = 1, linetype = "dashed", color = "grey50") +
  geom_pointrange() +
  scale_x_log10() +
  labs(x = "OR (95% CI)", y = NULL) +
  theme_paper()

ggsave(file.path(FIGURES_DIR, "fig3-forest.pdf"),
       plot = p_forest, width = 178 / 25.4, height = 100 / 25.4,
       device = cairo_pdf)

# ---- Fig 4：校准曲线（预测模型） ----
# library(rms); 用 calibrate() + plot()

# ---- 全部导出：同时存 PDF + PNG（编辑要求） ----
export_fig <- function(p, name, w_mm = 86, h_mm = 70) {
  ggsave(file.path(FIGURES_DIR, paste0(name, ".pdf")),
         plot = p, width = w_mm / 25.4, height = h_mm / 25.4,
         device = cairo_pdf)
  ggsave(file.path(FIGURES_DIR, paste0(name, ".png")),
         plot = p, width = w_mm / 25.4, height = h_mm / 25.4,
         dpi = 600)
}
