#!/usr/bin/env python3
"""Замер 1 (Кейс 1, трудные вопросы) — issue #299.

Прогоняет 15 трудных вопросов (`voprosy_zamer1.HARD_QUESTIONS`) через ДВА уже стоящих на
стенде сценария — `С9 · Кейс 1, версия 1` (вебхук `s9-answer-free`) и `С9 · Кейс 1, версия 2`
(вебхук `s9-answer-gated`). Ничего не создаёт и не публикует — только настоящие HTTP-отправки
в форму и прямое чтение `GET /executions/<id>?includeData=true` (не самоотчёт «API принял
JSON»). 15×2 = 30 отправок = 30 вызовов модели (по одному на отправку в каждой версии —
проверено устройством обоих сценариев в `stend/sborka.py`).

Usage:
    source /home/harness/.n8n-lab-credentials
    python3 run_zamer1.py --output raw/zamer1-results.json
"""
import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request

from voprosy_zamer1 import HARD_QUESTIONS

HOST = "https://n8n.lessons.tellian.io"


def post_form(webhook_path, question_text):
    url = f"{HOST}/form/{webhook_path}"
    boundary = "----zamer1boundary"
    body = (
        f"--{boundary}\r\n"
        'Content-Disposition: form-data; name="field-0"\r\n\r\n'
        f"{question_text}\r\n"
        f"--{boundary}--\r\n"
    ).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_execution(api_url, api_key, exec_id):
    req = urllib.request.Request(
        f"{api_url}/executions/{exec_id}?includeData=true",
        headers={"X-N8N-API-KEY": api_key},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def node_items(run_data, node_name):
    try:
        return run_data[node_name][0]["data"]["main"][0]
    except Exception:
        return None


def run_one(api_url, api_key, webhook_path, question_text, wait_node, sleep=0.6, timeout=25):
    resp = post_form(webhook_path, question_text)
    waiting_url = resp.get("formWaitingUrl", "")
    exec_id = None
    try:
        path = urllib.parse.urlparse(waiting_url).path
        exec_id = path.rstrip("/").split("/")[-1]
    except Exception:
        pass
    if not exec_id:
        return {"error": "no execution id", "raw_resp": resp}

    run_data = {}
    deadline = time.time() + timeout
    while time.time() < deadline:
        time.sleep(sleep)
        try:
            ex = get_execution(api_url, api_key, exec_id)
        except Exception:
            continue
        run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
        if wait_node in run_data:
            break
    return {"execution_id": exec_id, "run_data": run_data}


def extract_v1(run_data):
    items = node_items(run_data, "Answer (free self-report)")
    answer = None
    if items:
        answer = items[0]["json"].get("text")
    return {"answer": answer}


def extract_v2(run_data):
    items = node_items(run_data, "Answer with grounding (structured)")
    answer, grounded = None, None
    if items:
        out = items[0]["json"].get("output", {})
        answer = out.get("answer")
        grounded = out.get("grounded_in_item")
    decision = "answered" if "Write row (answered)" in run_data else (
        "escalated" if "Write row (escalated)" in run_data else "НЕРАСПОЗНАНО")
    return {"answer": answer, "grounded_in_item": grounded, "decision": decision}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    api_url = os.environ.get("N8N_API_URL")
    api_key = os.environ.get("N8N_API_KEY")
    if not api_url or not api_key:
        print("N8N_API_URL / N8N_API_KEY не заданы", file=sys.stderr)
        sys.exit(1)

    results = []
    calls = 0
    for i, q in enumerate(HARD_QUESTIONS, start=1):
        print(f"[{i}/15] v1 (free): {q['question'][:50]}...", file=sys.stderr)
        r1 = run_one(api_url, api_key, "s9-answer-free", q["question"],
                     "Answer (free self-report)")
        calls += 1
        v1 = extract_v1(r1.get("run_data", {})) if "run_data" in r1 else {"error": r1}

        print(f"[{i}/15] v2 (gated): {q['question'][:50]}...", file=sys.stderr)
        r2 = run_one(api_url, api_key, "s9-answer-gated", q["question"],
                     "Answer with grounding (structured)")
        calls += 1
        v2 = extract_v2(r2.get("run_data", {})) if "run_data" in r2 else {"error": r2}

        results.append({
            "n": i, "kb_id": q["kb_id"], "question": q["question"],
            "correct_by_base": q["correct_by_base"], "trap": q["trap"],
            "v1_execution_id": r1.get("execution_id"), "v1": v1,
            "v2_execution_id": r2.get("execution_id"), "v2": v2,
        })
        print(f"      calls so far: {calls}", file=sys.stderr)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump({"calls_total": calls, "results": results}, f, ensure_ascii=False, indent=2)
    print(f"Готово. Вызовов: {calls}. Записано в {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
