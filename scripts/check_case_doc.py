#!/usr/bin/env python3
"""病例分析文档 lint（纯标准库）。

机械校验 AGENTS.md 引用纪律与 case-analysis 模板契约：
  E1 必备章节：需解决的问题 / 病例分析 / Active Issues / 24h plan / Red flags / 参考文献 / PHI 自检
  E2 流程块二选一：独立会诊交叉验证 或 流程偏差说明
  E3 引用闭环：行内 [N] 均在参考文献列表定义；列表条目均被引用
  E4 参考文献条目：带标签（[指南]/[RCT] 等）+ 核对状态三态（已回核/未核对原文/部分支持）
  W1 剂量/阈值无引用：剂量单位后 100 字符内无 [N]（warning，速览/治疗清单类章节除外）

用法：
  python3 scripts/check_case_doc.py <file.md | dir>
退出码：有 error 为 1，仅 warning 为 0。
"""

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = {
    "E1a 需解决的问题": re.compile(r"^#{1,3}.*需解决的问题", re.M),
    "E1b 病例分析": re.compile(r"^#{1,3}.*病例分析", re.M),
    "E1c Active Issues": re.compile(r"^#{1,3}.*(active\s*issues|问题列表)", re.M | re.I),
    "E1d 24h plan": re.compile(r"(24\s*h\s*(plan|must-do)|24h\s*计划)", re.I),
    "E1e Red flags": re.compile(r"red\s*flags?|红线|立即升级", re.I),
    "E1f 参考文献": re.compile(r"^#{1,3}.*参考文献", re.M),
    "E1g PHI 自检": re.compile(r"PHI\s*自检|去标识化自检", re.I),
}

FLOW_BLOCK = re.compile(r"独立会诊|交叉验证|流程偏差说明")

REF_HEADING = re.compile(r"^#{1,3}.*参考文献\s*$", re.M)
REF_ENTRY = re.compile(r"^\s*(\d+)\.\s+\S", re.M)
INLINE_CITE = re.compile(r"\[(\d{1,2})\]")
REF_TAG = re.compile(r"\[(指南|共识|RCT|Meta|综述|队列|说明书|基础|预印本)\]")
CHECK_STATUS = re.compile(r"已回核|未核对原文|未读全文|部分支持")

DOSE = re.compile(
    r"\d+(?:\.\d+)?\s*(?:mg|μg|mcg|g|U|IU|mL|ml)\s*/\s*(?:h|kg|min)|"
    r"\d+(?:\.\d+)?\s*(?:IU|U)\b|"
    r"\d+(?:\.\d+)?\s*U/kg"
)
SKIP_D1_HEADING = re.compile(
    r"速览|治疗清单|关键趋势|基本信息|医嘱清单|可复制|"
    r"rounds|active\s*issues|问题列表|24\s*h|must-do|red\s*flags|待补",
    re.I,
)

CITE_WINDOW = 100


def strip_code_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def section_skipped(lines, idx):
    """任一上级标题命中跳过模式即跳过（rounds 摘要的子系统段落同样豁免）。"""
    for j in range(idx, -1, -1):
        m = re.match(r"^#{1,3}\s+(.*)", lines[j])
        if m and SKIP_D1_HEADING.search(m.group(1)):
            return True
    return False


def check_file(path: Path):
    text = path.read_text(encoding="utf-8")
    body = strip_code_fences(text)
    errors, warnings = [], []

    for name, pat in REQUIRED_SECTIONS.items():
        if not pat.search(body):
            errors.append(f"{name}：缺失必备章节")

    if not FLOW_BLOCK.search(body):
        errors.append("E2：缺「独立会诊交叉验证」或「流程偏差说明」（缺步须显式声明）")

    ref_match = REF_HEADING.search(body)
    defined, ref_lines = set(), []
    if ref_match:
        ref_region = body[ref_match.end():]
        next_h = re.search(r"^#{1,3} ", ref_region, re.M)
        if next_h:
            ref_region = ref_region[: next_h.start()]
        for line in ref_region.splitlines():
            m = REF_ENTRY.match(line)
            if m:
                defined.add(int(m.group(1)))
                ref_lines.append(line)

    cited = set(int(n) for n in INLINE_CITE.findall(body))
    # 参考文献区内的 [N] 提及（如证据来源说明里的"条目 [1]"）同样视为有效引用，不做剔除

    for n in sorted(cited - defined):
        errors.append(f"E3a：行内引用 [{n}] 在参考文献列表中无对应条目")
    for n in sorted(defined - cited):
        errors.append(f"E3b：参考文献 [{n}] 定义后从未被行内引用")

    for line in ref_lines:
        m = REF_ENTRY.match(line)
        n = m.group(1)
        if not REF_TAG.search(line):
            errors.append(f"E4a：参考文献 [{n}] 缺标签（[指南]/[RCT]/[Meta] 等）")
        if not CHECK_STATUS.search(line):
            errors.append(f"E4b：参考文献 [{n}] 缺核对状态（已回核/未核对原文/部分支持）")

    lines = body.splitlines()
    for i, line in enumerate(lines):
        if REF_ENTRY.match(line) or section_skipped(lines, i):
            continue
        for m in DOSE.finditer(line):
            window = line[max(0, m.start() - CITE_WINDOW): m.end() + CITE_WINDOW]
            if not INLINE_CITE.search(window):
                warnings.append(f"W1 第{i + 1}行：剂量「{m.group(0)}」前后 {CITE_WINDOW} 字符内无 [N] 引用")

    return errors, warnings


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    target = Path(sys.argv[1])
    files = sorted(target.glob("**/*.md")) if target.is_dir() else [target]
    total_err = 0
    for f in files:
        errors, warnings = check_file(f)
        total_err += len(errors)
        if errors or warnings:
            print(f"\n== {f} ==")
            for e in errors:
                print(f"  ERROR  {e}")
            for w in warnings:
                print(f"  WARN   {w}")
    print(f"\n{len(files)} 个文件，{total_err} 个 error")
    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
