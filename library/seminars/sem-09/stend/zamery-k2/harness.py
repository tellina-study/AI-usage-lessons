#!/usr/bin/env python3
"""Кейс 2 — общий стенд-харнесс для серий замеров по структурированию промта, issue #299.

Правка владельца 2026-10-27: пять направлений (неизменный префикс для кэша, структурирование/
форматирование, расположение данных, формулировка правил, +1 своё), по каждому — не менее 10
замеров на живом стенде, показать, как работает, оценить качество, собрать итоговый промт.

Один generic сценарий `С9 · замер K2 · произвольный промт` (webhook `s9-k2-experiment`,
одно текстовое поле «Промт» — ВЕСЬ промт целиком, без сборки внутри n8n), чтобы варьировать
текст с python-стороны без republish на каждый вариант. Модель — тот же `qwen/qwen-2.5-7b-
instruct`, тот же credential, что везде на этом стенде.

Usage:
    source /home/harness/.n8n-lab-credentials && set -a && \
        source /home/harness/.n8n-lab-credentials && set +a
    python3 harness.py --push      # один раз
    python3 harness.py --selftest  # один настоящий вызов, проверить устройство
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")
HOST = "https://n8n.lessons.tellian.io"
WEBHOOK = "s9-k2-experiment"

OPENROUTER_CRED = {"openRouterApi": {"id": "VbxiQn8TbqA4R2mw", "name": "OpenRouter account"}}


def build_workflow():
    return {
        "name": "С9 · замер K2 · произвольный промт",
        "nodes": [
            {
                "id": "k2_trigger", "name": "Prompt in",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-180, 0], "webhookId": WEBHOOK,
                "parameters": {
                    "path": WEBHOOK, "formTitle": "Замер Кейса 2 — произвольный промт",
                    "formDescription": "Служебный стенд, не форма студента",
                    "formFields": {"values": [{
                        "fieldLabel": "Промт", "fieldType": "textarea",
                        "requiredField": True}]},
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "k2_model", "name": "Model",
                "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter", "typeVersion": 1,
                "position": [60, 200],
                "parameters": {"model": "qwen/qwen-2.5-7b-instruct", "options": {}},
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "k2_chain", "name": "Answer",
                "type": "@n8n/n8n-nodes-langchain.chainLlm", "typeVersion": 1.4,
                "position": [60, 0],
                "parameters": {
                    "promptType": "define",
                    "text": "={{ $json['Промт'] }}",
                    "options": {}},
            },
            {
                "id": "k2_result", "name": "Result",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [300, 0],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Готово",
                    "completionMessage": "={{ $json.text }}",
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Prompt in": {"main": [[{"node": "Answer", "type": "main", "index": 0}]]},
            "Answer": {"main": [[{"node": "Result", "type": "main", "index": 0}]]},
            "Model": {"ai_languageModel": [[{"node": "Answer", "type": "ai_languageModel",
                                              "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
    }


def api(method, path, body=None):
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"X-N8N-API-KEY": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


def push():
    wf = build_workflow()
    (HERE / "k2-experiment.json").write_text(
        json.dumps(wf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    existing = {w["name"]: w["id"] for w in api("GET", "/workflows?limit=100")["data"]}
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


def post_form(prompt_text):
    url = f"{HOST}/form/{WEBHOOK}"
    boundary = "----k2boundary"
    body = (f"--{boundary}\r\n"
            'Content-Disposition: form-data; name="field-0"\r\n\r\n'
            f"{prompt_text}\r\n--{boundary}--\r\n").encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data, time.time() - t0


def get_execution(exec_id):
    req = urllib.request.Request(
        f"{API}/executions/{exec_id}?includeData=true",
        headers={"X-N8N-API-KEY": KEY})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def node_items(run_data, node_name):
    try:
        return run_data[node_name][0]["data"]["main"][0]
    except Exception:
        return None


def call(prompt_text, sleep=0.5, timeout=30):
    """Один вызов: отправка промта, ожидание, чтение текста ответа + латентность."""
    resp, post_latency = post_form(prompt_text)
    waiting_url = resp.get("formWaitingUrl", "")
    exec_id = urllib.parse.urlparse(waiting_url).path.rstrip("/").split("/")[-1]
    run_data = {}
    t0 = time.time()
    deadline = t0 + timeout
    while time.time() < deadline:
        time.sleep(sleep)
        try:
            ex = get_execution(exec_id)
        except Exception:
            continue
        run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
        if "Answer" in run_data:
            break
    wait_latency = time.time() - t0
    items = node_items(run_data, "Answer")
    text = None
    if items:
        try:
            text = items[0]["json"]["text"]
        except Exception:
            text = None
    # latency по таймстампам самого узла (точнее, чем ожидание опросом)
    node_latency = None
    try:
        entry = run_data["Answer"][0]
        node_latency = entry.get("executionTime")  # мс, если n8n его пишет
    except Exception:
        pass
    return {"exec_id": exec_id, "text": text,
            "wait_latency_s": round(wait_latency, 2),
            "node_latency_ms": node_latency}


def grade(answer_text, must_include_patterns, must_not_include_patterns=()):
    """Толерантный к падежу/форме грейдинг — тот же приём, что в Кейсе 3 (regex, не substring)."""
    if not answer_text:
        return False, "нет ответа"
    reasons = []
    for pat in must_include_patterns:
        if not re.search(pat, answer_text, re.I):
            reasons.append(f"нет «{pat}»")
    for pat in must_not_include_patterns:
        if re.search(pat, answer_text, re.I):
            reasons.append(f"есть запрещённое «{pat}»")
    return (len(reasons) == 0), "; ".join(reasons) if reasons else "ок"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.push:
        push()
    if args.selftest:
        r = call("Ответь одним словом: сколько будет 2+2?")
        print(json.dumps(r, ensure_ascii=False, indent=2))
