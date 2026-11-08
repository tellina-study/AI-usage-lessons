import json, os, sys, time, urllib.parse, urllib.request

API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")
HOST = "https://n8n.lessons.tellian.io"


def post_form(webhook, fields):
    boundary = "----s10boundary"
    parts = []
    for i, val in enumerate(fields):
        parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="field-{i}"\r\n\r\n{val}\r\n')
    parts.append(f'--{boundary}--\r\n')
    body = "".join(parts).encode("utf-8")
    req = urllib.request.Request(f"{HOST}/form/{webhook}", data=body, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_execution(exec_id):
    req = urllib.request.Request(f"{API}/executions/{exec_id}?includeData=true",
                                  headers={"X-N8N-API-KEY": KEY})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def call_raw(url, body_dict, node_name="OpenRouter raw", timeout=90, sleep=1.0):
    """Один сырой вызов через вебхук s10-raw-openrouter. Не ждёт разрешения
    формы (completion-узел висит в waiting до GET formWaitingUrl, см.
    sem-07/stend/README.md «Прогон с экраном результата висит в waiting») —
    опрашивает execution до появления runData нужного узла, как
    sem-09/.../kesh_stend.py."""
    t0 = time.time()
    resp = post_form("s10-raw-openrouter", [url, json.dumps(body_dict, ensure_ascii=False)])
    waiting = resp.get("formWaitingUrl", "")
    exec_id = urllib.parse.urlparse(waiting).path.rstrip("/").split("/")[-1]
    deadline = time.time() + timeout
    out, node_ms, status = None, None, None
    while time.time() < deadline:
        time.sleep(sleep)
        try:
            ex = get_execution(exec_id)
        except Exception:
            continue
        run = ex.get("data", {}).get("resultData", {}).get("runData", {})
        if node_name in run:
            entry = run[node_name][0]
            node_ms = entry.get("executionTime")
            try:
                out = entry["data"]["main"][0][0]["json"]
            except Exception:
                out = {"_no_json": True, "_entry_error": entry.get("error")}
            status = "done"
            break
    return {"exec_id": exec_id, "node_ms": node_ms,
            "wall_s": round(time.time() - t0, 2), "response": out, "status": status}


if __name__ == "__main__":
    r = call_raw(
        "https://openrouter.ai/api/v1/chat/completions",
        {"model": "openai/gpt-4o-mini", "messages": [{"role": "user", "content": "Скажи одно слово: тест"}]},
    )
    print(json.dumps(r, ensure_ascii=False, indent=2)[:2000])
