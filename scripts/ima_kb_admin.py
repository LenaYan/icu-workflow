#!/usr/bin/env python3
"""ima 知识库目录管理工具（Cookie 认证，走网页端 cgi-bin 接口）。

弥补 ima-mcp-server 没有的能力：列知识库、列文件夹、列条目、批量移动。
凭证从 ~/.kimi-code/mcp.json 的 mcpServers.ima.env.IMA_COOKIE 读取，
access token 过期时自动用 refresh token 续期。日志不输出 cookie/token。

用法：
    python3 ima_kb_admin.py kbs                              # 列知识库（名称 + cookie KB id）
    python3 ima_kb_admin.py folders <kb_id>                  # 列库根目录下的文件夹
    python3 ima_kb_admin.py ls <kb_id> [folder_id]           # 列条目（默认根目录；自动翻页）
    python3 ima_kb_admin.py mv <kb_id> <dst_folder_id> <media_id> [media_id...]
    python3 ima_kb_admin.py mv <kb_id> <dst_folder_id> --all-from <src_folder_id|root>
    python3 ima_kb_admin.py mkdir <kb_id> <parent_folder_id|root> <名称>   # 新建文件夹
    python3 ima_kb_admin.py rm <kb_id> <media_id> [media_id...]            # 删除（不可逆）

医学知识库的 folder_id 对照见 ima-skills/kb-folder-ids.md。
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

MCP_JSON = os.path.expanduser("~/.kimi-code/mcp.json")
BASE = "https://ima.qq.com/cgi-bin"
PAGE_LIMIT = 50  # 接口上限，超过会报「参数错误」
AUTH_ERROR_CODES = {600001, 600002, 600003, 41, 110031}


class ImaClient:
    def __init__(self):
        cfg = json.load(open(MCP_JSON))["mcpServers"]["ima"]
        self.cookie = cfg["env"]["IMA_COOKIE"]
        m = re.search(r"IMA-BKN=([^;\s]+)", self.cookie)
        self.bkn = m.group(1) if m else ""
        self.uid = re.search(r"IMA-UID=([^;]+)", self.cookie).group(1)
        rt = re.search(r"IMA-REFRESH-TOKEN=([^;]+)", self.cookie)
        self.refresh_token = urllib.parse.unquote(rt.group(1)) if rt else None
        self.token = None
        self.refresh()

    def refresh(self):
        """用 refresh_token 换新 access token，注入 cookie 与 Authorization 头。"""
        body = {"user_id": self.uid, "refresh_token": self.refresh_token, "token_type": 14}
        req = urllib.request.Request(
            f"{BASE}/auth_login/refresh",
            data=json.dumps(body).encode(),
            headers={"Content-Type": "application/json", "x-ima-cookie": self.cookie,
                     "User-Agent": "Mozilla/5.0"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as r:
            resp = json.loads(r.read().decode())
        if resp.get("code") != 0 or not resp.get("token"):
            sys.exit(f"token 刷新失败 [{resp.get('code')}]：{resp.get('msg')}，"
                     "请重抓 IMA_COOKIE（见 AGENTS.md §7）")
        self.token = resp["token"]
        if "IMA-TOKEN=" in self.cookie:
            self.cookie = re.sub(r"IMA-TOKEN=[^;]+", f"IMA-TOKEN={self.token}", self.cookie)
        else:
            self.cookie += f"; IMA-TOKEN={self.token}"

    def _headers(self):
        h = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "From_browser_ima": "1",
            "Referer": "https://ima.qq.com/wikis",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36 Chrome/131.0.0.0 Safari/537.36",
            "x-ima-cookie": self.cookie,
            "authorization": f"Bearer {self.token}",
        }
        if self.bkn:
            h["x-ima-bkn"] = self.bkn
        return h

    def post(self, path, body, retry=True):
        req = urllib.request.Request(f"{BASE}/{path}", data=json.dumps(body).encode(),
                                     headers=self._headers(), method="POST")
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                resp = json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            detail = e.read().decode()[:200]
            raise RuntimeError(f"{path} HTTP {e.code}：{detail}")
        if retry and resp.get("code") in AUTH_ERROR_CODES:
            self.refresh()
            return self.post(path, body, retry=False)
        return resp

    def post_sse(self, path, body):
        """调用 SSE 接口（如 move_knowledge），返回 [(event, data_dict), ...]。"""
        req = urllib.request.Request(f"{BASE}/{path}", data=json.dumps(body).encode(),
                                     headers=self._headers(), method="POST")
        with urllib.request.urlopen(req, timeout=300) as r:
            raw = r.read().decode()
        events, cur = [], None
        for line in raw.splitlines():
            if line.startswith("event:"):
                cur = line[6:].strip()
            elif line.startswith("data:") and cur:
                payload = line[5:].strip()
                try:
                    payload = json.loads(payload)
                except ValueError:
                    pass
                events.append((cur, payload))
        return events

    # ── 业务接口 ──────────────────────────────────────────────
    def list_kbs(self):
        resp = self.post("knowledge_tab_reader/get_home_page_data",
                         {"knowledge_base_id": "", "need_folder_number": True})
        # 结构：results[] 为分类（自建/订阅等），每个分类下 knowledge_base_list
        categories = resp.get("results") or []
        out = []
        for category in categories:
            for kb in category.get("knowledge_base_list") or []:
                info = kb.get("basic_info", {})
                out.append({"id": kb.get("id"), "name": info.get("name")})
        return out

    def list_folders(self, kb_id):
        resp = self.post("knowledge_tab_reader/get_home_page_data",
                         {"knowledge_base_id": kb_id, "need_folder_number": True})
        fr = resp.get("folder_rsp") or {}
        return fr.get("folder_list") or []

    def list_items(self, kb_id, folder_id=""):
        """folder_id='' 表示根目录。返回 (files, subfolders)，自动翻页。"""
        files, subfolders, cursor = [], [], ""
        while True:
            resp = self.post("knowledge_tab_reader/get_knowledge_list",
                             {"knowledge_base_id": kb_id, "folder_id": folder_id,
                              "cursor": cursor, "limit": PAGE_LIMIT})
            if resp.get("code") != 0:
                sys.exit(f"get_knowledge_list 失败 [{resp.get('code')}]：{resp.get('msg')}")
            for it in resp.get("knowledge_list") or []:
                (subfolders if it.get("folder_info") else files).append(it)
            if resp.get("is_end"):
                break
            cursor = resp.get("cursor") or ""
            if not cursor:
                break
        return files, subfolders

    def move(self, kb_id, dst_folder_id, media_ids):
        events = self.post_sse("knowledge_tab_sse/move_knowledge", {
            "src_knowledge_base_id": kb_id,
            "dst_knowledge_base_id": kb_id,
            "dst_folder_id": dst_folder_id,
            "media_ids": media_ids,
            "action": 0,  # 0=Default，重名时由服务端弹冲突事件
        })
        return events

    def create_folder(self, kb_id, parent_folder_id, title):
        resp = self.post("knowledge_tab_writer/create_folder", {
            "knowledge_base_id": kb_id,
            "folder_id": parent_folder_id,  # 父目录；库根目录传 kb_id 本身
            "title": title,
        })
        if resp.get("code") != 0:
            sys.exit(f"create_folder 失败 [{resp.get('code')}]：{resp.get('msg')}")
        return resp.get("knowledge") or {}

    def delete(self, kb_id, media_ids):
        """删除条目（文件或文件夹，文件夹用其 folder_id 作 media_id）。不可逆，谨慎。"""
        resp = self.post("knowledge_tab_writer/del_knowledge", {
            "knowledge_base_id": kb_id,
            "media_ids": media_ids,
        })
        if resp.get("code") != 0:
            sys.exit(f"del_knowledge 失败 [{resp.get('code')}]：{resp.get('msg')}")
        results = resp.get("results") or {}
        return [mid for mid, r in results.items() if r.get("ret_code") == 0]


def cmd_kbs(client):
    for kb in client.list_kbs():
        print(f'{kb["id"]}\t{kb["name"]}')


def cmd_folders(client, kb_id):
    for f in client.list_folders(kb_id):
        print(f'{f["folder_id"]}\tfiles={f["file_number"]}\t{f["name"]}')


def cmd_ls(client, kb_id, folder_id=""):
    files, subfolders = client.list_items(kb_id, folder_id)
    for it in subfolders:
        fi = it["folder_info"]
        print(f'[dir]  {fi["folder_id"]}\tfiles={fi["file_number"]}\t{fi["name"]}')
    for it in files:
        print(f'[file] {it["media_id"]}\t{it.get("title", "")}')


def cmd_mv(client, kb_id, dst_folder_id, media_ids=None, all_from=None):
    if all_from is not None:
        src = "" if all_from == "root" else all_from
        files, _ = client.list_items(kb_id, src)
        media_ids = [it["media_id"] for it in files]
        print(f"从 {'根目录' if all_from == 'root' else all_from} 收集到 {len(media_ids)} 个文件")
    if not media_ids:
        sys.exit("没有要移动的文件")
    events = client.move(kb_id, dst_folder_id, media_ids)
    names = [e for e, _ in events]
    print(f"事件序列: {names}")
    for ev, data in events:
        if ev in ("COMPLETE", "SAMENAME"):
            print(f"{ev}: {json.dumps(data, ensure_ascii=False)[:500]}")
    if "COMPLETE" not in names:
        sys.exit("未收到 COMPLETE 事件，请在 ima 客户端核对结果")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)
    client = ImaClient()
    cmd, rest = args[0], args[1:]
    if cmd == "kbs":
        cmd_kbs(client)
    elif cmd == "folders" and len(rest) == 1:
        cmd_folders(client, rest[0])
    elif cmd == "ls" and 1 <= len(rest) <= 2:
        cmd_ls(client, rest[0], rest[1] if len(rest) == 2 else "")
    elif cmd == "mv" and len(rest) >= 3:
        kb_id, dst = rest[0], rest[1]
        if rest[2] == "--all-from" and len(rest) == 4:
            cmd_mv(client, kb_id, dst, all_from=rest[3])
        else:
            cmd_mv(client, kb_id, dst, media_ids=rest[2:])
    elif cmd == "mkdir" and len(rest) == 3:
        kb_id, parent, title = rest
        parent = "" if parent == "root" else parent
        knowledge = client.create_folder(kb_id, parent or kb_id, title)
        fi = knowledge.get("folder_info") or {}
        print(f'已创建: {fi.get("folder_id", knowledge.get("media_id", "?"))}\t{fi.get("name", title)}')
    elif cmd == "rm" and len(rest) >= 2:
        kb_id, media_ids = rest[0], rest[1:]
        removed = client.delete(kb_id, media_ids)
        print(f"已删除 {len(removed)}/{len(media_ids)} 个条目")
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
