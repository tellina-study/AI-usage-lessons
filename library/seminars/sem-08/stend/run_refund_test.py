#!/usr/bin/env python3
"""Прогон набора тестовых запросов Кейса 3 через ОДИН живой webhook n8n и честная запись
результата. Не генератор данных (см. `_gen_refund_requests.py` / `_gen_refund_requests_extra.py`)
— это прогон уже подготовленных текстов через настоящий стенд, настоящим HTTP-триггером.

Usage:
    N8N_API_URL=... N8N_API_KEY=... python3 run_refund_test.py \
        --webhook-path s8-refund-model \
        --input refund-requests-extra.json \
        --output /tmp/out.json \
        --node-for-amount "Extract amount" \
        --node-for-decision "Decide refund (model)" \
        --decision-field text

Читает ключи и адрес ТОЛЬКО из переменных окружения (`N8N_API_URL`, `N8N_API_KEY`) — см.
`~/.n8n-lab.env`. Ключ никогда не печатается и не логируется.

Для процесса (B) (IF-узел, две ветки) решение читается не из текста узла, а из того, какая из
двух Result screen-веток исполнилась — см. `--mode if-branch`.
"""
import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.parse

HOST = "https://n8n.lessons.tellian.io"


def post_form(webhook_path, text):
    url = f"{HOST}/form/{webhook_path}"
    boundary = "----refundtestboundary"
    body_parts = []
    body_parts.append(f"--{boundary}\r\n")
    body_parts.append('Content-Disposition: form-data; name="field-0"\r\n\r\n')
    body_parts.append(text + "\r\n")
    body_parts.append(f"--{boundary}--\r\n")
    body = "".join(body_parts).encode("utf-8")
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


def node_output(run_data, node_name):
    try:
        return run_data[node_name][0]["data"]["main"][0][0]["json"]
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--webhook-path", required=True)
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--amount-node", default="Extract amount")
    ap.add_argument("--mode", choices=["model-text", "if-branch"], default="model-text")
    ap.add_argument("--decision-node", default="Decide refund (model)")
    ap.add_argument("--if-ok-node", default="Result screen (approve)")
    ap.add_argument("--if-esc-node", default="Result screen (escalate)")
    ap.add_argument("--sleep", type=float, default=0.4)
    args = ap.parse_args()

    api_url = os.environ.get("N8N_API_URL")
    api_key = os.environ.get("N8N_API_KEY")
    if not api_url or not api_key:
        print("N8N_API_URL / N8N_API_KEY не заданы — source ~/.n8n-lab.env", file=sys.stderr)
        sys.exit(1)

    data = json.load(open(args.input, encoding="utf-8"))
    requests_ = data["requests"]

    results = []
    for row in requests_:
        text = row["text"]
        try:
            resp = post_form(args.webhook_path, text)
        except Exception as e:
            results.append({**row, "error": f"POST failed: {e}"})
            continue
        waiting_url = resp.get("formWaitingUrl", "")
        # formWaitingUrl вида https://host/form-waiting/<execId>?signature=...
        exec_id = None
        try:
            path = urllib.parse.urlparse(waiting_url).path
            exec_id = path.rstrip("/").split("/")[-1]
        except Exception:
            pass
        if not exec_id:
            results.append({**row, "error": "no execution id in response", "raw_resp": resp})
            continue

        # Опрос до готовности: решение принимается асинхронно (вызов модели), фиксированного
        # сна недостаточно — ждём появления нужного узла в runData, не дольше 20с.
        run_data = {}
        deadline = time.time() + 20
        while time.time() < deadline:
            time.sleep(args.sleep)
            try:
                ex = get_execution(api_url, api_key, exec_id)
            except Exception as e:
                continue
            run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
            if args.mode == "model-text" and args.decision_node in run_data:
                break
            if args.mode == "if-branch" and (
                args.if_ok_node in run_data or args.if_esc_node in run_data
            ):
                break
        amount_out = node_output(run_data, args.amount_node)
        extracted_amount = None
        if amount_out and isinstance(amount_out.get("output"), dict):
            extracted_amount = amount_out["output"].get("amount_rub")

        entry = {**row, "execution_id": exec_id, "extracted_amount": extracted_amount}

        if args.mode == "model-text":
            dec_out = node_output(run_data, args.decision_node)
            raw = (dec_out or {}).get("text", "")
            raw_norm = raw.strip().lower()
            if "одобр" in raw_norm:
                decision = "одобрить"
            elif "эскал" in raw_norm:
                decision = "эскалировать"
            else:
                decision = f"НЕРАСПОЗНАНО:{raw!r}"
            entry["decision_raw"] = raw
            entry["decision"] = decision
        else:  # if-branch
            ok_out = node_output(run_data, args.if_ok_node)
            esc_out = node_output(run_data, args.if_esc_node)
            if ok_out is not None:
                entry["decision"] = "одобрить"
            elif esc_out is not None:
                entry["decision"] = "эскалировать"
            else:
                entry["decision"] = "НЕРАСПОЗНАНО: ни одна ветка не исполнилась"

        entry["correct"] = entry.get("decision") == row["expected_by_rule_B"]
        results.append(entry)
        print(f"id={row['id']:>3} amount={row.get('target_amount_rub', row.get('amount_rub'))} "
              f"extracted={extracted_amount} decision={entry.get('decision')} "
              f"expected={row['expected_by_rule_B']} correct={entry['correct']}")

    n_correct = sum(1 for r in results if r.get("correct"))
    out = {
        "webhook_path": args.webhook_path,
        "mode": args.mode,
        "input_file": args.input,
        "count": len(results),
        "correct": n_correct,
        "score": f"{n_correct}/{len(results)}",
        "results": results,
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nИТОГО: {n_correct}/{len(results)} -> {args.output}")


if __name__ == "__main__":
    main()
