"""clinical_calc.py 金标准回归测试（纯标准库 unittest）。

期望值均为手算/公式独立推导，不从脚本输出反推。病例文档中的数值直接取自本脚本，
公式或阈值改动必须先让这里的用例通过。

运行：python3 -m unittest discover -s tests -v
"""

import subprocess
import sys
import unittest
from pathlib import Path

CALC = Path(__file__).resolve().parent.parent / "scripts" / "clinical_calc.py"


def run(*args) -> str:
    r = subprocess.run([sys.executable, str(CALC), *map(str, args)], capture_output=True, text=True)
    if r.returncode != 0:
        raise AssertionError(f"clinical_calc {' '.join(map(str, args))} 失败：\n{r.stderr}")
    return r.stdout


class TestPBW(unittest.TestCase):
    def test_male_175(self):
        out = run("pbw", "--sex", "male", "--height", 175)
        self.assertIn("= 70.5 kg", out)          # 50 + 2.3×(175/2.54 − 60) = 70.47
        self.assertIn("Vt 6 mL/kg PBW = 423 mL", out)

    def test_female_160(self):
        out = run("pbw", "--sex", "female", "--height", 160)
        self.assertIn("= 52.4 kg", out)          # 45.5 + 2.3×(62.99 − 60) = 52.38


class TestCrCl(unittest.TestCase):
    def test_male_umol(self):
        out = run("crcl", "--age", 65, "--weight", 70, "--scr", 120, "--sex", "male")
        self.assertIn("= 53.7 mL/min", out)      # 75×70 / (72×120/88.4)

    def test_female_factor(self):
        out = run("crcl", "--age", 65, "--weight", 70, "--scr", 120, "--sex", "female")
        self.assertIn("= 45.7 mL/min", out)      # ×0.85

    def test_obese_uses_adjusted_bw(self):
        out = run("crcl", "--age", 50, "--weight", 120, "--scr", 1.0, "--scr-unit", "mg",
                  "--sex", "male", "--ibw", 70)
        self.assertIn("adjusted BW 90.0 kg", out)  # 70 + 0.4×(120−70)
        self.assertIn("= 112.5 mL/min", out)       # 90×90 / 72

    def test_non_obese_keeps_actual_bw(self):
        out = run("crcl", "--age", 50, "--weight", 85, "--scr", 1.0, "--scr-unit", "mg",
                  "--sex", "male", "--ibw", 70)
        self.assertIn("实际体重 85.0 kg", out)     # 85 < 1.3×70 = 91


class TestVent(unittest.TestCase):
    def test_dp_compliance(self):
        out = run("vent", "--pplat", 28, "--peep", 10, "--vt", 360, "--pbw", 60)
        self.assertIn("= 18 cmH2O", out)
        self.assertIn("Vt/PBW = 6.0", out)
        self.assertIn("静态顺应性 = Vt/DP = 20", out)
        self.assertNotIn("Pplat > 30", out)

    def test_pplat_warning(self):
        self.assertIn("Pplat > 30", run("vent", "--pplat", 32, "--peep", 10))


class TestAcidBase(unittest.TestCase):
    def test_ag_albumin_delta(self):
        out = run("ag", "--na", 140, "--cl", 105, "--hco3", 18, "--albumin", 25)
        self.assertIn("AG = Na - Cl - HCO3 = 17.0", out)
        self.assertIn("白蛋白校正 AG = 20.8", out)  # 17 + 2.5×1.5 = 20.75
        self.assertIn("= 1.46", out)                # (20.75−12)/(24−18)
        self.assertIn("单纯高 AG", out)

    def test_ag_hco3_not_low_no_crash(self):
        out = run("ag", "--na", 140, "--cl", 100, "--hco3", 24)
        self.assertIn("Delta ratio 不适用", out)

    def test_alk_comp_double_alkalosis(self):
        out = run("alk-comp", "--hco3", 31.2, "--paco2", 33)
        self.assertIn("预期 PaCO2 = 40 + 0.7×(31.2 - 24) = 45", out)  # 45.04
        self.assertIn("双重碱血症", out)

    def test_alk_comp_simple(self):
        self.assertIn("单纯代碱", run("alk-comp", "--hco3", 34, "--paco2", 47))  # 预期 47


class TestElectrolytes(unittest.TestCase):
    def test_na_correct_mmol(self):
        out = run("na-correct", "--na", 132, "--glucose", 30)
        self.assertIn("= 139.0 mmol/L", out)      # 132 + 1.6×(540−100)/100

    def test_ca_correct_g_per_l(self):
        out = run("ca-correct", "--ca", 8.0, "--albumin", 25)
        self.assertIn("= 9.20 mg/dL", out)        # 8 + 0.8×(4.0−2.5)


class TestOxygenation(unittest.TestCase):
    def test_rox_case_value_and_sensitivity(self):
        out = run("rox", "--spo2", 95, "--fio2", 0.41, "--rr", 19, "--rr-max", 30)
        self.assertIn("= 12.2", out)              # (95/0.41)/19 = 12.19
        self.assertIn("ROX 12.2-7.7", out)        # RR 30 → 7.72
        self.assertIn("低风险", out)

    def test_rox_thresholds(self):
        # (SpO2/FiO2)/RR：构造恰好落在各阈值的组合
        self.assertIn("灰区", run("rox", "--spo2", 77, "--fio2", 1.0, "--rr", 20))       # 3.85
        self.assertIn("高危", run("rox", "--spo2", 57, "--fio2", 1.0, "--rr", 20))       # 2.85
        self.assertIn("应考虑插管", run("rox", "--spo2", 56, "--fio2", 1.0, "--rr", 20))  # 2.80

    def test_pf_berlin(self):
        self.assertIn("178  → 中度 ARDS", run("pf", "--pao2", 73, "--fio2", 0.41))
        self.assertIn("轻度 ARDS", run("pf", "--pao2", 120, "--fio2", 0.5))   # 240
        self.assertIn("重度 ARDS", run("pf", "--pao2", 90, "--fio2", 1.0))    # 90


class TestInfusions(unittest.TestCase):
    def test_gik_rate(self):
        out = run("gik", "--insulin", 8, "--volume", 500, "--rate", 25, "--weight", 70)
        self.assertIn("= 0.016 U/mL", out)
        self.assertIn("实际速率 = 0.40 U/h", out)
        self.assertIn("= 0.006 U/kg/h", out)      # 0.4/70 = 0.0057

    def test_uf_intensity(self):
        out = run("uf", "--net-uf", 100, "--weight", 60)
        self.assertIn("= 1.67 mL/kg/h", out)
        self.assertIn("24h 净平衡 = 2400 mL", out)
        self.assertIn("1.01-1.75", out)
        self.assertIn("警告", run("uf", "--net-uf", 120, "--weight", 60))  # 2.0


if __name__ == "__main__":
    unittest.main()
