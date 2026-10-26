#!/usr/bin/env python3
"""Synchronize IMA_COOKIE across the three project-level MCP configurations.

The ima MCP credential expires frequently. Update all three independent files
together so CLI and desktop sessions in these projects use the same cookie:

  1. icu-workflow/.kimi-code/mcp.json
  2. pubmed-crawler/.kimi-code/mcp.json
  3. medical/.kimi-code/mcp.json

Usage:
    python3 snippets/update_ima_cookie.py "PLATFORM=H5; ...full IMA_COOKIE..."
    python3 snippets/update_ima_cookie.py  # Interactive paste mode

See AGENTS.md section 7 for cookie recovery instructions. MCP configuration is
registered at session startup, so open a new session after updating it.
"""

from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PATHS = [
    PROJECT_ROOT / ".kimi-code" / "mcp.json",
    PROJECT_ROOT.parent / "pubmed-crawler" / ".kimi-code" / "mcp.json",
    PROJECT_ROOT.parent / "medical" / ".kimi-code" / "mcp.json",
]

# 允许用环境变量覆盖路径（测试用）
if os.environ.get("IMA_MCP_PATHS"):
    DEFAULT_PATHS = [Path(p) for p in os.environ["IMA_MCP_PATHS"].split(os.pathsep)]


def mask(cookie: str) -> str:
    """日志里只露头和尾，避免凭证进终端历史/日志。"""
    cookie = cookie.strip()
    if len(cookie) <= 24:
        return cookie[:6] + "..."
    return f"{cookie[:24]}...{cookie[-12:]}"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {"mcpServers": {}}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"[错误] {path} 不是合法 JSON：{e}（请人工检查，脚本未做任何修改）")


def atomic_write(path: Path, data: dict) -> None:
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(tmp, path)
    except BaseException:
        os.unlink(tmp)
        raise


def get_cookie() -> str:
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:]).strip()
    print("请粘贴新的 IMA_COOKIE（x-ima-cookie 的值），回车结束：")
    return sys.stdin.readline().strip()


def main() -> None:
    cookie = get_cookie()
    if not cookie:
        sys.exit("[错误] cookie 为空，未做任何修改。")
    if "IMA-TOKEN" not in cookie and "IMA-REFRESH-TOKEN" not in cookie:
        print(f"[警告] cookie 中未见 IMA-TOKEN / IMA-REFRESH-TOKEN，仍将继续：{mask(cookie)}")

    configs = {p: load_json(p) for p in DEFAULT_PATHS}

    # 若某份配置缺 ima server，从另一份复制整个 server 块
    for path, cfg in configs.items():
        if "ima" not in cfg.get("mcpServers", {}):
            donor = next(
                (c for p, c in configs.items() if p != path and "ima" in c.get("mcpServers", {})),
                None,
            )
            if donor is None:
                sys.exit(f"[错误] {path} 中没有 ima server，且找不到可复制的来源配置。")
            cfg.setdefault("mcpServers", {})["ima"] = donor["mcpServers"]["ima"]
            print(f"[提示] {path.name}（{path.parent.name}）原本没有 ima，已从另一份复制配置块")

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    ok, fail = [], []
    for path, cfg in configs.items():
        old = cfg["mcpServers"]["ima"].setdefault("env", {}).get("IMA_COOKIE", "")
        cfg["mcpServers"]["ima"]["env"]["IMA_COOKIE"] = cookie
        try:
            backup = path.with_suffix(path.suffix + f".bak-{stamp}")
            if path.exists():
                shutil.copy2(path, backup)
            atomic_write(path, cfg)
            # 回读校验
            reread = json.loads(path.read_text(encoding="utf-8"))
            assert reread["mcpServers"]["ima"]["env"]["IMA_COOKIE"] == cookie
        except Exception as e:  # noqa: BLE001
            fail.append((path, str(e)))
            continue
        changed = "已更新" if old != cookie else "原本就是该值"
        ok.append((path, changed, backup if path.exists() else None))

    for path, changed, _ in ok:
        print(f"[OK] {path}\n     -> {changed}")
    for path, err in fail:
        print(f"[失败] {path}\n       {err}", file=sys.stderr)

    print()
    print(f"cookie: {mask(cookie)}")
    if fail:
        sys.exit(1)
    print("Three project configurations synchronized. Open a new session, then verify: list_knowledge_bases_full")
    print("Rollback: restore the .bak-<timestamp> files beside the configurations.")


if __name__ == "__main__":
    main()
