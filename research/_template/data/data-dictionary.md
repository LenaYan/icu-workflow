# 数据字典 — {project}

> 一次写好，分析期间锁定。新增变量必须 append 并标注引入日期。

## 元信息
- 数据源：
- 时间范围：
- 提取日：
- 提取方式：SQL / 导出 / API
- 去标识化：完成日 / 责任人

## 主键
- 患者：`pid`（脱敏后的整数 ID）
- 入科记录：`stay_id`
- 时间戳基准：以入 ICU 为 t=0

## 变量

| 变量名 | 类型 | 单位 | 允许范围 | 描述 | 来源表 / 字段 | 缺失处理 | 备注 |
|---|---|---|---|---|---|---|---|
| `pid` | int | | | 脱敏患者 ID | | 不允许 | 主键 |
| `stay_id` | int | | | 入科记录 ID | | 不允许 | |
| `age` | int | y | 18–110 | 入科年龄 | | 不允许 | |
| `sex` | factor | | M/F | | | 不允许 | |
| `bmi` | num | kg/m² | 12–60 | | | median impute | |
| `apache2` | int | | 0–71 | 入科 24h APACHE II | | exclude if 缺 | |
| `sofa_d0` | int | | 0–24 | 入科 SOFA | | exclude | |
| `lactate_d0` | num | mmol/L | 0–25 | 入科 4h 内 | | LOCF | 多次取最大 |
| `mech_vent` | bool | | 0/1 | 入科 24h 内机械通气 | | as 0 | |
| `vasopressor` | bool | | 0/1 | 任何 NE/E/vaso 使用 | | as 0 | |
| `crrt` | bool | | 0/1 | 住 ICU 任何 CRRT | | as 0 | |
| `death_icu` | bool | | 0/1 | ICU 死亡 | | exclude if 不明 | primary outcome |
| `death_28d` | bool | | 0/1 | 28d 全因死亡 | | exclude if 失访 | |
| `los_icu` | num | d | | ICU 住院天数 | | | |
| `los_hosp` | num | d | | 全院住院天数 | | | |
| `…` | | | | | | | |

## 复合变量定义

### Sepsis-3
- 感染（培养阳性或临床诊断）+ SOFA Δ ≥ 2

### ARDS (Berlin)
- 起病 ≤ 7d + 双肺浸润（非心源性）+ P/F ≤ 300 on PEEP ≥ 5

### AKI (KDIGO)
- 见 `guidelines/AKI/`

## 时间窗 / 锁定
- 基线变量：入 ICU **前 6h** 至 **后 24h** 取最坏值
- 暴露窗：入 ICU 后 ?? h
- 结局窗：

## 修订记录
| 日期 | 修订人 | 内容 |
|---|---|---|
| YYYY-MM-DD | | 初版 |
