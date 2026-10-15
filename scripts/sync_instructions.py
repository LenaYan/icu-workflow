#!/usr/bin/env python3
"""双栈单源生成：shared/*.src.md → Claude Code / Kimi Code 两套文件（纯标准库）。

源文件语法（标记独占一行，顺序固定 claude → kimi → end，任一段可为空）：
  <!--@claude-->
  仅 Claude 版的内容
  <!--@kimi-->
  仅 Kimi 版的内容
  <!--@end-->
标记外的内容两边共用。

用法：
  python3 scripts/sync_instructions.py           # 重新生成全部目标文件
  python3 scripts/sync_instructions.py --check   # 只校验，未同步则退出码 1（pre-commit 用）
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TARGETS = {
    "shared/INSTRUCTIONS.src.md": {"claude": "CLAUDE.md", "kimi": "AGENTS.md"},
    "shared/agents/icu-consultant.src.md": {
        "claude": ".claude/agents/icu-consultant.md",
        "kimi": ".kimi-code/agents/icu-consultant.md",
    },
}

SWITCH = re.compile(r"^<!--@claude-->\n(.*?)^<!--@kimi-->\n(.*?)^<!--@end-->\n", re.S | re.M)
MARKER = re.compile(r"<!--@(claude|kimi|end)-->")


def render(src: str, stack: str, src_path: str) -> str:
    out = SWITCH.sub(lambda m: m.group(1) if stack == "claude" else m.group(2), src)
    if MARKER.search(out):
        raise SystemExit(f"{src_path}：存在未闭合或顺序错误的 @claude/@kimi/@end 标记")
    notice = f"<!-- 由 {src_path} 生成，勿直接编辑；改源文件后运行 python3 scripts/sync_instructions.py -->\n"
    if out.startswith("---\n"):
        end = out.index("\n---\n", 4) + len("\n---\n")
        return out[:end] + notice + out[end:]
    return notice + out


def main(argv):
    check = "--check" in argv
    stale = []
    for src_rel, outs in TARGETS.items():
        src = (ROOT / src_rel).read_text(encoding="utf-8")
        for stack, out_rel in outs.items():
            want = render(src, stack, src_rel)
            out_path = ROOT / out_rel
            have = out_path.read_text(encoding="utf-8") if out_path.exists() else None
            if have == want:
                continue
            if check:
                stale.append(out_rel)
            else:
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(want, encoding="utf-8")
                print(f"已生成 {out_rel}")
    if stale:
        print("以下文件与 shared/ 源文件不同步（可能被直接编辑）：")
        for f in stale:
            print(f"  - {f}")
        print("请把改动移到 shared/*.src.md，再运行 python3 scripts/sync_instructions.py")
        return 1
    if check:
        print("双栈指令已同步")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
