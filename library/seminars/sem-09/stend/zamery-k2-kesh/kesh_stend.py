#!/usr/bin/env python3
"""Стенд для замера кэширования промта, Кейс 2 Семинара 9 (issue #303).

ЗАЧЕМ НОВЫЙ СТЕНД, А НЕ `zamery-k2/harness.py`. Прежний стенд ходил к модели через узел
`@n8n/n8n-nodes-langchain.chainLlm`: этот узел отдаёт наружу только текст ответа и
`executionTime`, то есть ЛАТЕНТНОСТЬ. Поэтому замер A в `zamery-k2/README.md` мерил
латентность — и ничего про кэш измерить не мог в принципе, независимо от результата.
Метрики кэша живут в поле `usage` ответа провайдера, и чтобы их увидеть, нужен сырой
HTTP-вызов. Этот стенд — один узел `httpRequest` на `POST
https://openrouter.ai/api/v1/chat/completions`, тело запроса приходит целиком с
python-стороны, ответ провайдера возвращается целиком и читается из execution.

Ключ OpenRouter НЕ проходит через этот процесс: узел использует
`authentication: predefinedCredentialType` + `nodeCredentialType: openRouterApi`, то есть
n8n подставляет ключ на своей стороне из credential `VbxiQn8TbqA4R2mw` (тот же, что везде
на стенде Семинара 9). Ни одно значение ключа здесь не читается, не печатается и не
логируется — тот же приём, что в `zamery-k5-k6/sborka.py`.

Usage:
    source /home/harness/.n8n-lab-credentials && set -a && \
        source /home/harness/.n8n-lab-credentials && set +a
    python3 kesh_stend.py --push
    python3 kesh_stend.py --selftest
"""
import argparse
import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")
HOST = "https://n8n.lessons.tellian.io"
WEBHOOK = "s9-k2-kesh"
WF_NAME = "С9 · замер K2 — кэш промта (сырой вызов OpenRouter)"

OPENROUTER_CRED = {"openRouterApi": {"id": "VbxiQn8TbqA4R2mw", "name": "OpenRouter account"}}


def build_workflow():
    return {
        "name": WF_NAME,
        "nodes": [
            {
                "id": "kesh_trigger", "name": "Request body in",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-180, 0], "webhookId": WEBHOOK,
                "parameters": {
                    "path": WEBHOOK,
                    "formTitle": "Замер кэша Кейса 2 — тело запроса целиком",
                    "formDescription": "Служебный стенд, не форма студента",
                    "formFields": {"values": [{
                        "fieldLabel": "Тело", "fieldType": "textarea",
                        "requiredField": True}]},
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "kesh_http", "name": "OpenRouter raw",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [60, 0],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/v1/chat/completions",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": "={{ $json['Тело'] }}",
                    "options": {"response": {"response": {"neverError": True}},
                                "timeout": 120000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "kesh_result", "name": "Result",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [300, 0],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Готово",
                    "completionMessage": "ok",
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Request body in": {"main": [[{"node": "OpenRouter raw",
                                           "type": "main", "index": 0}]]},
            "OpenRouter raw": {"main": [[{"node": "Result",
                                           "type": "main", "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
    }


def api(method, path, body=None):
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"X-N8N-API-KEY": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


def push():
    wf = build_workflow()
    (HERE / "kesh-stend.json").write_text(
        json.dumps(wf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    existing = {w["name"]: w["id"] for w in api("GET", "/workflows?limit=250")["data"]}
    if wf["name"] in existing:
        wid = existing[wf["name"]]
        api("PUT", f"/workflows/{wid}", wf)
        print(f"обновлён: {wid}")
    else:
        wid = api("POST", "/workflows", wf)["id"]
        print(f"создан: {wid}")
    api("POST", f"/workflows/{wid}/publish", {})
    print("опубликован")
    return wid


def post_form(payload_text):
    url = f"{HOST}/form/{WEBHOOK}"
    boundary = "----keshboundary"
    body = (f"--{boundary}\r\n"
            'Content-Disposition: form-data; name="field-0"\r\n\r\n'
            f"{payload_text}\r\n--{boundary}--\r\n").encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_execution(exec_id):
    req = urllib.request.Request(
        f"{API}/executions/{exec_id}?includeData=true",
        headers={"X-N8N-API-KEY": KEY})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def call(body_dict, timeout=150, sleep=1.0):
    """Один сырой вызов. Возвращает полный ответ провайдера + id execution."""
    t_sent = time.time()
    resp = post_form(json.dumps(body_dict, ensure_ascii=False))
    waiting = resp.get("formWaitingUrl", "")
    exec_id = urllib.parse.urlparse(waiting).path.rstrip("/").split("/")[-1]
    deadline = time.time() + timeout
    out = None
    node_ms = None
    while time.time() < deadline:
        time.sleep(sleep)
        try:
            ex = get_execution(exec_id)
        except Exception:
            continue
        run = ex.get("data", {}).get("resultData", {}).get("runData", {})
        if "OpenRouter raw" in run:
            entry = run["OpenRouter raw"][0]
            node_ms = entry.get("executionTime")
            try:
                out = entry["data"]["main"][0][0]["json"]
            except Exception:
                out = {"_no_json": True, "_entry_error": entry.get("error")}
            break
    return {"exec_id": exec_id, "node_ms": node_ms,
            "wall_s": round(time.time() - t_sent, 2), "response": out}


USAGE_KEYS_SEEN = set()


def usage_of(resp):
    """Вытащить usage как есть, без переименований — какие поля пришли, те и пишем."""
    if not isinstance(resp, dict):
        return {}
    u = resp.get("usage") or {}
    USAGE_KEYS_SEEN.update(u.keys())
    return u


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.push:
        push()
    if a.selftest:
        r = call({"model": "anthropic/claude-haiku-5.5",
                  "messages": [{"role": "user", "content": "Ответь одним словом: 2+2?"}],
                  "max_tokens": 16, "usage": {"include": True}})
        print(json.dumps(r, ensure_ascii=False, indent=2)[:3000])
