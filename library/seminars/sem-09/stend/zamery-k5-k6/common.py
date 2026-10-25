#!/usr/bin/env python3
"""Общие функции прогона для Замеров 3-4 (Кейсы 5/6) Семинара 9 — issue #299.

Тот же приём, что `sem-08/stend/run_refund_test.py`: настоящая отправка HTTP-запроса на
живой вебхук плюс прямое чтение `GET /executions/<id>?includeData=true` — самоотчёт «API
принял JSON» здесь не используется нигде.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HOST = "https://n8n.lessons.tellian.io"


def env_or_die():
    api_url = os.environ.get("N8N_API_URL")
    api_key = os.environ.get("N8N_API_KEY")
    if not api_url or not api_key:
        print("N8N_API_URL / N8N_API_KEY не заданы — source /home/harness/.n8n-lab-credentials",
              file=sys.stderr)
        sys.exit(1)
    return api_url, api_key


def post_form(webhook_path, field_value, field_name="field-0"):
    """Form Trigger — один текстовый вопрос. Возвращает распарсенный ответ (formWaitingUrl)."""
    url = f"{HOST}/form/{webhook_path}"
    boundary = "----k5k6boundary"
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="{field_name}"\r\n\r\n'
        f"{field_value}\r\n"
        f"--{boundary}--\r\n"
    ).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def exec_id_from_waiting_url(resp):
    waiting_url = resp.get("formWaitingUrl", "")
    path = urllib.parse.urlparse(waiting_url).path
    return path.rstrip("/").split("/")[-1]


def get_execution(api_url, api_key, exec_id):
    req = urllib.request.Request(
        f"{api_url}/executions/{exec_id}?includeData=true",
        headers={"X-N8N-API-KEY": api_key})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def node_output(run_data, node_name):
    try:
        return run_data[node_name][0]["data"]["main"][0][0]["json"]
    except Exception:
        return None


def wait_for_node(api_url, api_key, exec_id, node_name, timeout=25, sleep=0.5):
    """Опрос до готовности — решение принимается асинхронно (вызов модели), фиксированного
    сна недостаточно (тот же приём, что `run_refund_test.py`)."""
    deadline = time.time() + timeout
    run_data = {}
    while time.time() < deadline:
        time.sleep(sleep)
        try:
            ex = get_execution(api_url, api_key, exec_id)
        except Exception:
            continue
        run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
        if node_name in run_data:
            return run_data
    return run_data


def post_json_webhook(webhook_path, body):
    """Обычный Webhook (не Form Trigger), responseMode=lastNode — ответ синхронный, тело
    ответа = вывод последнего узла графа."""
    url = f"{HOST}/webhook/{webhook_path}"
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST",
                                  headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            return True, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return False, {"http_status": e.code, "body": e.read().decode("utf-8", "replace")}


def latest_execution_id(api_url, api_key, workflow_id, after_ts_ms):
    """У Webhook-узла (не Form Trigger) ответ синхронный и не содержит execution id — тот
    читается отдельно: берём самое свежее исполнение этого workflow, запущенное ПОСЛЕ
    отправки нашего запроса (`after_ts_ms`, время до POST, мс с эпохи)."""
    req = urllib.request.Request(
        f"{api_url}/executions?workflowId={workflow_id}&limit=5",
        headers={"X-N8N-API-KEY": api_key})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    for ex in data.get("data", []):
        # startedAt — ISO8601 UTC с 'Z'
        import datetime
        started = datetime.datetime.fromisoformat(ex["startedAt"].replace("Z", "+00:00"))
        started_ms = started.timestamp() * 1000
        if started_ms >= after_ts_ms - 2000:  # запас 2с на рассинхрон часов
            return ex["id"]
    return data["data"][0]["id"] if data.get("data") else None
