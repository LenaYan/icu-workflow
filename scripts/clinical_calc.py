#!/usr/bin/env python3
"""ICU 床旁常用计算（纯标准库，无第三方依赖）。

用途：病例分析/处方中所有可计算的数值一律由本脚本产出，模型不口算。
用法示例：
  python3 scripts/clinical_calc.py pbw --sex male --height 175
  python3 scripts/clinical_calc.py crcl --age 65 --weight 70 --scr 120 --sex male
  python3 scripts/clinical_calc.py vent --pplat 28 --peep 10 [--pbw 60 --vt 360]
  python3 scripts/clinical_calc.py ag --na 140 --cl 105 --hco3 18 [--k 4.5] [--albumin 25]
  python3 scripts/clinical_calc.py na-correct --na 132 --glucose 30
  python3 scripts/clinical_calc.py rox --spo2 95 --fio2 0.41 --rr 19 [--rr-max 30]
  python3 scripts/clinical_calc.py pf --pao2 73 --fio2 0.41
  python3 scripts/clinical_calc.py gik --insulin 8 --volume 500 --rate 50
  python3 scripts/clinical_calc.py uf --net-uf 100 --weight 70
  python3 scripts/clinical_calc.py ca-correct --ca 2.0 --albumin 25
  python3 scripts/clinical_calc.py alk-comp --hco3 31.2 --paco2 33
"""

import argparse


def cmd_pbw(a):
    """Devine 公式 PBW（IBW），并给 Vt 4/6/8 mL/kg 参考。"""
    inches_over_5ft = (a.height / 2.54) - 60.0
    base = 50.0 if a.sex == "male" else 45.5
    pbw = base + 2.3 * inches_over_5ft
    print(f"PBW (Devine, {a.sex}, {a.height} cm) = {pbw:.1f} kg")
    for per_kg in (4, 6, 8):
        print(f"  Vt {per_kg} mL/kg PBW = {per_kg * pbw:.0f} mL")


def cmd_crcl(a):
    """Cockcroft-Gault CrCl (mL/min)。Scr 默认 umol/L，--scr-unit mg 时为 mg/dL。"""
    scr_mg = a.scr / 88.4 if a.scr_unit == "umol" else a.scr
    weight = a.weight
    if a.ibw:
        # 实际体重 >130% IBW 时用 adjusted BW
        if weight > 1.3 * a.ibw:
            weight = a.ibw + 0.4 * (weight - a.ibw)
            note = f"adjusted BW {weight:.1f} kg（实际体重 >130% IBW）"
        else:
            note = f"实际体重 {weight:.1f} kg"
    else:
        note = f"体重 {weight:.1f} kg（未提供 IBW，肥胖患者建议加 --ibw）"
    crcl = (140 - a.age) * weight / (72 * scr_mg)
    if a.sex == "female":
        crcl *= 0.85
    print(f"CrCl (Cockcroft-Gault) = {crcl:.1f} mL/min  [{note}, Scr {scr_mg:.2f} mg/dL]")


def cmd_vent(a):
    """Driving pressure = Pplat - PEEP；可选静态顺应性与 mL/kg PBW。"""
    dp = a.pplat - a.peep
    print(f"Driving pressure = {a.pplat} - {a.peep} = {dp:.0f} cmH2O  (目标 ≤15)")
    if a.pplat > 30:
        print("  警告：Pplat > 30 cmH2O")
    if a.vt and a.pbw:
        print(f"  Vt/PBW = {a.vt / a.pbw:.1f} mL/kg PBW  (目标 4-8，ARDS 6)")
        print(f"  静态顺应性 = Vt/DP = {a.vt / dp:.0f} mL/cmH2O" if dp > 0 else "  DP ≤ 0，请检查输入")


def cmd_ag(a):
    """阴离子间隙 + 白蛋白校正 + delta ratio。白蛋白单位 g/L（40 g/L 为正常）。"""
    ag = a.na - a.cl - a.hco3
    k_note = ""
    if a.k is not None:
        ag_k = a.na + a.k - a.cl - a.hco3
        k_note = f"；含 K AG = {ag_k:.1f}"
    print(f"AG = Na - Cl - HCO3 = {ag:.1f} mmol/L（参考 8-12，不含 K{k_note}）")
    ag_corr = ag
    if a.albumin is not None:
        ag_corr = ag + 2.5 * (40 - a.albumin) / 10
        print(f"白蛋白校正 AG = {ag_corr:.1f}（Alb {a.albumin} g/L，每低 10 g/L 补 2.5）")
    delta = (ag_corr - 12) / (24 - a.hco3)
    interp = (
        "<0.4：合并正常 AG 代谢性酸中毒" if delta < 0.4 else
        "0.4-0.8：可合并正常 AG 酸中毒" if delta < 0.8 else
        "0.8-2.0：单纯高 AG 代谢性酸中毒" if delta <= 2.0 else
        ">2.0：合并代谢性碱中毒或慢性呼酸代偿"
    )
    print(f"Delta ratio = (corrAG - 12)/(24 - HCO3) = {delta:.2f}  → {interp}")


def cmd_na_correct(a):
    """高血糖校正血钠：血糖每高 5.6 mmol/L（100 mg/dL），Na +1.6 mmol/L。"""
    glucose_mg = a.glucose * 18 if a.glucose_unit == "mmol" else a.glucose
    corrected = a.na + 1.6 * (glucose_mg - 100) / 100
    print(f"校正 Na = {a.na} + 1.6 x ({glucose_mg:.0f} - 100)/100 = {corrected:.1f} mmol/L")


def cmd_rox(a):
    """ROX = (SpO2/FiO2)/RR。>4.88 低风险；3.85-4.87 密切监测；<3.85 高危；<2.85 考虑插管。
    RR 存疑时用 --rr-max 做敏感性分析，禁止以"RR 不准"为由跳过计算。"""
    def rox(rr):
        return a.spo2 / a.fio2 / rr
    def grade(v):
        return ("低风险（>4.88）" if v > 4.88 else
                "灰区，密切监测（3.85-4.87）" if v >= 3.85 else
                "高危，准备插管（2.85-3.85）" if v >= 2.85 else
                "应考虑插管（<2.85）")
    print(f"ROX = ({a.spo2}/{a.fio2})/{a.rr} = {rox(a.rr):.1f}  → {grade(rox(a.rr))}")
    if a.rr_max:
        print(f"敏感性：RR {a.rr}-{a.rr_max} → ROX {rox(a.rr):.1f}-{rox(a.rr_max):.1f}")
    print("  注意：阈值为 HFNC 后 12h 验证时点，各研究切点有异质性，动态趋势优先于单点")


def cmd_pf(a):
    """P/F = PaO2/FiO2，Berlin 分层。"""
    pf = a.pao2 / a.fio2
    tier = ("正常（>300）" if pf > 300 else
            "轻度 ARDS（200-300）" if pf > 200 else
            "中度 ARDS（100-200）" if pf > 100 else
            "重度 ARDS（≤100）")
    print(f"P/F = {a.pao2}/{a.fio2} = {pf:.0f}  → {tier}")


def cmd_gik(a):
    """GIK 实际胰岛素速率（U/h）= 胰岛素总量(U) / 液体量(mL) × 泵速(mL/h)。"""
    per_ml = a.insulin / a.volume
    uh = per_ml * a.rate
    print(f"胰岛素浓度 = {a.insulin}/{a.volume} = {per_ml:.3f} U/mL")
    print(f"实际速率 = {uh:.2f} U/h（泵速 {a.rate} mL/h）")
    if a.weight:
        print(f"= {uh / a.weight:.3f} U/kg/h  （HTG-AP 共识降脂剂量 0.1-0.3 U/kg/h）")


def cmd_uf(a):
    """CRRT 净超滤强度 mL/kg/h。队列证据：1.01-1.75 区间 28 天死亡率最低；>1.75 与肾恢复延迟相关。"""
    r = a.net_uf / a.weight
    print(f"净超滤强度 = {a.net_uf}/{a.weight} = {r:.2f} mL/kg/h")
    print(f"  24h 净平衡 = {a.net_uf * 24:.0f} mL")
    if r > 1.75:
        print("  警告：>1.75 mL/kg/h，与肾脏恢复延迟相关，应降速")
    elif r > 1.0:
        print("  处于 1.01-1.75 区间上限，注意灌注与电解质")
    else:
        print("  ≤1.0 mL/kg/h，温和区间")


def cmd_ca_correct(a):
    """白蛋白校正总钙（mg/dL）：corrCa = Ca + 0.8×(4.0 - Alb g/dL)。Alb 单位 g/L 自动换算。"""
    alb_gdl = a.albumin / 10 if a.albumin > 10 else a.albumin
    corr = a.ca + 0.8 * (4.0 - alb_gdl)
    print(f"校正 Ca = {a.ca} + 0.8×(4.0 - {alb_gdl:.1f}) = {corr:.2f} mg/dL（参考 8.5-10.5）")
    print("  ICU 患者优先用游离钙，校正值仅供无游离钙时参考")


def cmd_alk_comp(a):
    """代碱代偿预期 PaCO2 = 40 + 0.7×(HCO3-24)，判断是否存在呼碱/呼酸叠加。"""
    expect = 40 + 0.7 * (a.hco3 - 24)
    print(f"预期 PaCO2 = 40 + 0.7×({a.hco3} - 24) = {expect:.0f} ±2")
    diff = a.paco2 - expect
    if abs(diff) <= 2:
        print(f"实测 {a.paco2} 在预期范围内 → 单纯代碱，呼吸代偿合适")
    elif diff < -2:
        print(f"实测 {a.paco2} 低于预期 {diff:.0f} → 代碱合并呼碱（双重碱血症）")
    else:
        print(f"实测 {a.paco2} 高于预期 +{diff:.0f} → 代碱合并呼酸")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("pbw", help="理想体重（Devine）与潮气量参考")
    s.add_argument("--sex", choices=["male", "female"], required=True)
    s.add_argument("--height", type=float, required=True, help="身高 cm")
    s.set_defaults(f=cmd_pbw)

    s = sub.add_parser("crcl", help="Cockcroft-Gault 肌酐清除率")
    s.add_argument("--age", type=float, required=True)
    s.add_argument("--weight", type=float, required=True, help="实际体重 kg")
    s.add_argument("--scr", type=float, required=True, help="血肌酐")
    s.add_argument("--scr-unit", choices=["umol", "mg"], default="umol")
    s.add_argument("--sex", choices=["male", "female"], required=True)
    s.add_argument("--ibw", type=float, help="理想体重 kg（提供后自动判断是否用 adjusted BW）")
    s.set_defaults(f=cmd_crcl)

    s = sub.add_parser("vent", help="驱动压 / 静态顺应性 / mL/kg PBW")
    s.add_argument("--pplat", type=float, required=True, help="平台压 cmH2O")
    s.add_argument("--peep", type=float, required=True, help="PEEP cmH2O")
    s.add_argument("--vt", type=float, help="潮气量 mL")
    s.add_argument("--pbw", type=float, help="理想体重 kg")
    s.set_defaults(f=cmd_vent)

    s = sub.add_parser("ag", help="阴离子间隙 / 白蛋白校正 / delta ratio")
    s.add_argument("--na", type=float, required=True)
    s.add_argument("--cl", type=float, required=True)
    s.add_argument("--hco3", type=float, required=True)
    s.add_argument("--k", type=float)
    s.add_argument("--albumin", type=float, help="白蛋白 g/L")
    s.set_defaults(f=cmd_ag)

    s = sub.add_parser("na-correct", help="高血糖校正血钠")
    s.add_argument("--na", type=float, required=True)
    s.add_argument("--glucose", type=float, required=True, help="血糖")
    s.add_argument("--glucose-unit", choices=["mmol", "mg"], default="mmol")
    s.set_defaults(f=cmd_na_correct)

    s = sub.add_parser("rox", help="ROX 指数（HFNC 成败预测），支持 RR 敏感性分析")
    s.add_argument("--spo2", type=float, required=True, help="SpO2 %")
    s.add_argument("--fio2", type=float, required=True, help="FiO2 小数（如 0.41）")
    s.add_argument("--rr", type=float, required=True, help="呼吸频率 /min")
    s.add_argument("--rr-max", type=float, help="RR 存疑时的上限，用于敏感性区间")
    s.set_defaults(f=cmd_rox)

    s = sub.add_parser("pf", help="氧合指数 P/F 与 Berlin 分层")
    s.add_argument("--pao2", type=float, required=True)
    s.add_argument("--fio2", type=float, required=True, help="FiO2 小数")
    s.set_defaults(f=cmd_pf)

    s = sub.add_parser("gik", help="GIK 实际胰岛素速率（U/h 与 U/kg/h）")
    s.add_argument("--insulin", type=float, required=True, help="胰岛素总量 U")
    s.add_argument("--volume", type=float, required=True, help="液体量 mL")
    s.add_argument("--rate", type=float, required=True, help="泵速 mL/h")
    s.add_argument("--weight", type=float, help="体重 kg（提供则算 U/kg/h）")
    s.set_defaults(f=cmd_gik)

    s = sub.add_parser("uf", help="CRRT 净超滤强度 mL/kg/h 与 24h 净平衡")
    s.add_argument("--net-uf", type=float, required=True, help="净超滤 mL/h")
    s.add_argument("--weight", type=float, required=True, help="体重 kg")
    s.set_defaults(f=cmd_uf)

    s = sub.add_parser("ca-correct", help="白蛋白校正总钙")
    s.add_argument("--ca", type=float, required=True, help="总钙 mg/dL")
    s.add_argument("--albumin", type=float, required=True, help="白蛋白 g/L")
    s.set_defaults(f=cmd_ca_correct)

    s = sub.add_parser("alk-comp", help="代碱代偿预期 PaCO2，判断双重碱血症")
    s.add_argument("--hco3", type=float, required=True)
    s.add_argument("--paco2", type=float, required=True)
    s.set_defaults(f=cmd_alk_comp)

    args = p.parse_args()
    args.f(args)


if __name__ == "__main__":
    main()
