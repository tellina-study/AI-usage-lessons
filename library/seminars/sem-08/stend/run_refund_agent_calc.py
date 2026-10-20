#!/usr/bin/env python3
"""Прогон варианта «дать модели инструмент-калькулятор» (карточка вопроса №2, Кейс 3) на живом
стенде. Архитектура отличается от run_refund_test.py: один узел `@n8n/n8n-nodes-langchain.agent`
делает всё сразу (читает текст, решает, вызывать ли калькулятор, вызывает его или не вызывает,
отвечает одним словом) — нет отдельного узла извлечения суммы, это и есть предмет проверки
карточки: вероятностность не исчезает, она «переезжает на шаг раньше».

Решение читается из поля `output` агента нечётким совпадением по корню «добр»/«эскал», потому
что реальный прогон уже показал артефакт модели — смешанный алфавит в ответе («Odобрить»,
латинская O + кириллица) — это не баг скрипта, это честная находка о том, как ведёт себя агент
с инструментом, когда сам инструмент не справился с запросом (см. iteration-log).
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse

HOST = "https://n8n.lessons.tellian.io"


def post_form(webhook_path, text):
    url = f"{HOST}/form/{webhook_path}"
    boundary = "----refundagentboundary"
    body = (
        f"--{boundary}\r\n"
        'Content-Disposition: form-data; name="field-0"\r\n\r\n'
        f"{text}\r\n"
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


def classify(raw):
    low = raw.lower()
    has_approve = bool(re.search(r"добр", low))  # "добр" (одобрить)
    has_escalate = bool(re.search(r"эскал", low))  # "эскал"
    if has_approve and not has_escalate:
        return "одобрить"
    if has_escalate and not has_approve:
        return "эскалировать"
    return f"НЕРАСПОЗНАНО:{raw!r}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--webhook-path", required=True)
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--agent-node", default="Decide refund (agent+calculator)")
    ap.add_argument("--calc-node", default="Calculator")
    ap.add_argument("--sleep", type=float, default=1.5)
    args = ap.parse_args()

    api_url = os.environ.get("N8N_API_URL")
    api_key = os.environ.get("N8N_API_KEY")
    if not api_url or not api_key:
        print("N8N_API_URL / N8N_API_KEY не заданы", file=sys.stderr)
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
        try:
            path = urllib.parse.urlparse(waiting_url).path
            exec_id = path.rstrip("/").split("/")[-1]
        except Exception:
            exec_id = None
        if not exec_id:
            results.append({**row, "error": "no execution id", "raw_resp": resp})
            continue

        run_data = {}
        deadline = time.time() + 25
        while time.time() < deadline:
            time.sleep(args.sleep)
            try:
                ex = get_execution(api_url, api_key, exec_id)
            except Exception:
                continue
            run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
            if args.agent_node in run_data:
                break

        agent_out = None
        try:
            agent_out = run_data[args.agent_node][0]["data"]["main"][0][0]["json"].get("output")
        except Exception:
            pass
        calc_calls = len(run_data.get(args.calc_node, []))
        calc_failed = False
        try:
            for call in run_data.get(args.calc_node, []):
                resp_text = call["data"]["ai_tool"][0][0]["json"].get("response", "")
                if "don't know" in resp_text or "не умею" in resp_text.lower():
                    calc_failed = True
        except Exception:
            pass

        decision = classify(agent_out or "")
        entry = {
            **row,
            "execution_id": exec_id,
            "agent_raw_output": agent_out,
            "decision": decision,
            "calculator_calls": calc_calls,
            "calculator_failed_at_least_once": calc_failed,
            "correct": decision == row["expected_by_rule_B"],
        }
        results.append(entry)
        print(f"id={row['id']:>10} target={row.get('target_amount_rub')} "
              f"raw={agent_out!r} decision={decision} calc_calls={calc_calls} "
              f"calc_failed={calc_failed} correct={entry['correct']}")

    n_correct = sum(1 for r in results if r.get("correct"))
    out = {
        "webhook_path": args.webhook_path,
        "input_file": args.input,
        "count": len(results),
        "correct": n_correct,
        "score": f"{n_correct}/{len(results)}",
        "calculator_failed_count": sum(1 for r in results if r.get("calculator_failed_at_least_once")),
        "results": results,
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nИТОГО: {n_correct}/{len(results)} -> {args.output}")
    print(f"Калькулятор не справился хотя бы раз: {out['calculator_failed_count']}/{len(results)}")


if __name__ == "__main__":
    main()
