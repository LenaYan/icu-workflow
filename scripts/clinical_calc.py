#!/usr/bin/env python3
"""ICU 床旁常用计算（纯标准库，无第三方依赖）。

用途：病例分析/处方中所有可计算的数值一律由本脚本产出，模型不口算。
用法示例：
  python3 scripts/clinical_calc.py pbw --sex male --height 175
  python3 scripts/clinical_calc.py crcl --age 65 --weight 70 --scr 120 --sex male
  python3 scripts/clinical_calc.py vent --pplat 28 --peep 10 [--pbw 60 --vt 360]
  python3 scripts/clinical_calc.py ag --na 140 --cl 105 --hco3 18 [--k 4.5] [--albumin 25]
  python3 scripts/clinical_calc.py na-correct --na 132 --glucose 30
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

    args = p.parse_args()
    args.f(args)


if __name__ == "__main__":
    main()
