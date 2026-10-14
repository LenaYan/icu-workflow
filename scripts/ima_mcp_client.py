#!/usr/bin/env python3
"""Minimal stdio MCP client for the local ima-mcp-server.

Reads server config (command/args/env) from ~/.kimi-code/mcp.json so that
credentials are never printed. Usage:

    python3 ima_mcp_client.py tools
    python3 ima_mcp_client.py call <tool> '<json-args>'
"""
import json, subprocess, sys, threading, queue, os

MCP_JSON = os.path.expanduser("~/.kimi-code/mcp.json")

def start_server():
    cfg = json.load(open(MCP_JSON))["mcpServers"]["ima"]
    env = dict(os.environ)
    env.update(cfg.get("env", {}))
    proc = subprocess.Popen(
        [cfg["command"], *cfg.get("args", [])],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env=env, text=True, bufsize=1,
    )
    return proc

def main():
    proc = start_server()
    out_q, err_lines = queue.Queue(), []
    def reader():
        for line in proc.stdout:
            out_q.put(line)
    def err_reader():
        for line in proc.stderr:
            err_lines.append(line)
    threading.Thread(target=reader, daemon=True).start()
    threading.Thread(target=err_reader, daemon=True).start()

    msg_id = 0
    pending = {}

    def send(method, params=None):
        nonlocal msg_id
        msg_id += 1
        proc.stdin.write(json.dumps({"jsonrpc": "2.0", "id": msg_id, "method": method, "params": params or {}}) + "\n")
        proc.stdin.flush()
        return msg_id

    def wait_response(want_id, timeout=120):
        import time
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                line = out_q.get(timeout=max(0.1, deadline - time.time()))
            except queue.Empty:
                break
            try:
                m = json.loads(line)
            except json.JSONDecodeError:
                continue
            if m.get("id") == want_id:
                return m
            pending[m.get("id")] = m
        return None

    # handshake
    send("initialize", {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "ima-cli", "version": "0.1"}})
    # drain until we see the init response (server may send requests first)
    init = None
    import time
    deadline = time.time() + 30
    while time.time() < deadline and init is None:
        try:
            line = out_q.get(timeout=1)
            m = json.loads(line)
            if m.get("id") == 1:
                init = m
            elif m.get("method"):
                # respond to server->client requests (e.g. roots/list)
                if "id" in m:
                    proc.stdin.write(json.dumps({"jsonrpc": "2.0", "id": m["id"], "result": {}}) + "\n")
                    proc.stdin.flush()
        except queue.Empty:
            pass
        except json.JSONDecodeError:
            pass
    if not init:
        print("INIT FAILED", file=sys.stderr)
        print("".join(err_lines[-30:]), file=sys.stderr)
        sys.exit(2)
    proc.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n")
    proc.stdin.flush()

    mode = sys.argv[1] if len(sys.argv) > 1 else "tools"
    if mode == "tools":
        rid = send("tools/list")
        r = wait_response(rid)
        for t in r["result"]["tools"]:
            print(f"- {t['name']}: {t.get('description','')[:100]}")
    elif mode == "call":
        tool, args = sys.argv[2], json.loads(sys.argv[3])
        rid = send("tools/call", {"name": tool, "arguments": args})
        r = wait_response(rid, timeout=300)
        if r is None:
            print("TIMEOUT; stderr:", "".join(err_lines[-20:]), file=sys.stderr)
            sys.exit(3)
        if "error" in r:
            print(json.dumps(r["error"], ensure_ascii=False, indent=2))
            sys.exit(1)
        for c in r["result"]["content"]:
            if c.get("type") == "text":
                print(c["text"])
            else:
                print(f"[{c.get('type')}]")
    proc.terminate()

if __name__ == "__main__":
    main()
