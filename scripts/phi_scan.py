#!/usr/bin/env python3
"""PHI 扫描（纯标准库）——pre-commit 钩子与手动全量扫描共用。

规则依据 `cases/README.md`：
  P1 手机号            11 位 1[3-9] 开头
  P2 身份证号          18 位（末位可 X）
  P3 完整病案/住院号    病案号/住院号/MRN/ID 后跟 ≥5 位未打码数字（只允许末 4 位）
  P4 姓名字段          「姓名：张三」形式（"某"打码除外）
  P5 精确日期（正文）   YYYY-MM-DD / YYYY年M月D日 —— 仅 cases/ 与 evals/fixtures/
                       （说明书核准/修订、文献发表等出版物日期行豁免）
  P6 精确日期（文件名） cases/ 下文件名；sessions/ 下含 P<N> 病例标识的文件名

扫描范围：cases/ sessions/ evals/ research/ 下的文本文件。
行内豁免：在该行写 `phi-ok`（需人工确认后才可使用）。

用法：
  python3 scripts/phi_scan.py --staged        # 扫描暂存区（pre-commit 用，读取 index 内容）
  python3 scripts/phi_scan.py --all           # 扫描范围内所有已跟踪文件
  python3 scripts/phi_scan.py <file> [...]    # 扫描指定文件
退出码：命中为 1，否则 0。
"""

import re
import subprocess
import sys
from pathlib import PurePosixPath

SCOPES = ("cases/", "sessions/", "evals/", "research/")
TEXT_EXT = {".md", ".txt", ".csv", ".tsv", ".r", ".py", ".qmd", ".rmd", ".json", ".yaml", ".yml"}

DATE = r"(?:19|20)\d{2}(?:-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[12]\d|3[01])|年\s*(?:0?[1-9]|1[0-2])\s*月\s*(?:0?[1-9]|[12]\d|3[01])\s*日)"
DATE_RE = re.compile(rf"(?<!\d){DATE}(?!\d)")
FILENAME_DATE_RE = re.compile(r"(?:19|20)\d{2}-[01]\d-[0-3]\d")
PATIENT_TAG_RE = re.compile(r"(?:^|[-_])P\d+(?:[-_]|$)")
PUBLICATION_CTX = re.compile(r"说明书|核准|修订|发布|发表|出版|版本|Published|accessed|检索于|epub|doi", re.I)

LINE_RULES = [
    ("P1 手机号", re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")),
    ("P2 身份证号", re.compile(r"(?<!\d)\d{17}[\dXx](?![\dXx])")),
    ("P3 完整病案号", re.compile(r"(?:病案号|住院号|门诊号|MRN|MR|ID号)\s*[:：#]?\s*\d{5,}", re.I)),
    ("P4 姓名字段", re.compile(r"姓名\s*[:：]\s*[\u4e00-\u9fa5]{2,4}")),
]
MASKED_NAME = re.compile(r"某|[*＊xX□]")


def in_scope(path: str) -> bool:
    p = PurePosixPath(path)
    return path.startswith(SCOPES) and p.suffix.lower() in TEXT_EXT


def date_body_scope(path: str) -> bool:
    if path.startswith("evals/fixtures/"):
        return True
    return path.startswith("cases/") and "/_templates/" not in path and not path.endswith("README.md")


def check_filename(path: str):
    name = PurePosixPath(path).name
    if not FILENAME_DATE_RE.search(name):
        return None
    if path.startswith("cases/"):
        return "P6 文件名含精确日期（改用 D 数/年-月，见 cases/README.md）"
    if path.startswith("sessions/") and PATIENT_TAG_RE.search(PurePosixPath(path).stem):
        return "P6 病例会话文件名含精确日期（改用 sessions/YYYY-MM-P<N>-<topic>.md）"
    return None


def scan_text(path: str, text: str):
    hits = []
    fn = check_filename(path)
    if fn:
        hits.append((0, fn, PurePosixPath(path).name))
    check_dates = date_body_scope(path)
    for i, line in enumerate(text.splitlines(), 1):
        if "phi-ok" in line:
            continue
        for name, pat in LINE_RULES:
            m = pat.search(line)
            if m and not (name.startswith("P4") and MASKED_NAME.search(m.group(0))):
                hits.append((i, name, m.group(0)))
        if check_dates and not PUBLICATION_CTX.search(line):
            m = DATE_RE.search(line)
            if m:
                hits.append((i, "P5 精确日期", m.group(0)))
    return hits


def git(*args) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def staged_files():
    out = git("diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
    return [f for f in out.split("\0") if f and in_scope(f)]


def read_staged(path: str) -> str:
    return subprocess.run(["git", "show", f":{path}"], check=True, capture_output=True).stdout.decode("utf-8", "replace")


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        sys.exit(__doc__)
    if argv[0] == "--staged":
        targets = [(f, read_staged(f)) for f in staged_files()]
    elif argv[0] == "--all":
        files = [f for f in git("ls-files", "-z").split("\0") if f and in_scope(f)]
        targets = [(f, open(f, encoding="utf-8", errors="replace").read()) for f in files]
    else:
        targets = [(f, open(f, encoding="utf-8", errors="replace").read()) for f in argv]

    total = 0
    for path, text in targets:
        hits = scan_text(path, text)
        if hits:
            print(f"\n== {path} ==")
            for line_no, rule, snippet in hits:
                where = f"第{line_no}行" if line_no else "文件名"
                print(f"  PHI  {rule}｜{where}：{snippet}")
            total += len(hits)
    print(f"\nPHI 扫描：{len(targets)} 个文件，{total} 处命中")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
