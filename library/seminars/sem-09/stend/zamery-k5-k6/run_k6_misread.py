#!/usr/bin/env python3
"""Замер 4.2 — Кейс 6: класс отказа, которого нет у текста — валидный по формату разбор с
неверным числом. Прогоняет receipt-02..receipt-06 (полное разрешение, состаренные) по 2
раза каждую через `s9-m6-read`. Для каждого ответа сверяет sum_rub/date с ИЗВЕСТНОЙ верной
парой (синтетическая квитанция — истина известна точно, не предполагается).

Usage: N8N_API_URL=... N8N_API_KEY=... python3 run_k6_misread.py
"""
import base64
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import common
from run_k6_resolution import parse_model_json, WORKFLOW_ID

HERE = Path(__file__).parent

# Истина по каждой квитанции — взята дословно из generate_receipts.py RECEIPTS (не из
# чтения модели).
TRUTH = {
    "receipt-02": {"amount": "23 450,00", "sum": 23450.00, "date": "03.10.2026"},
    "receipt-03": {"amount": "31 200,00", "sum": 31200.00, "date": "21.10.2026"},
    "receipt-04": {"amount": "9 800,00", "sum": 9800.00, "date": "14.07.2026"},
    "receipt-05": {"amount": "12 450,00", "sum": 12450.00, "date": "29.08.2026"},
    "receipt-06": {"amount": "27 300,00", "sum": 27300.00, "date": "05.10.2026"},
}
N_PER_RECEIPT = 2


def call_once(receipt_id, api_url, api_key):
    import time
    path = HERE / "receipts" / "aged" / f"{receipt_id}-aged.png"
    img_bytes = path.read_bytes()
    b64 = base64.b64encode(img_bytes).decode()
    body = {"image_base64": b64, "mime_type": "image/png", "receipt_id": receipt_id}
    t0_ms = time.time() * 1000
    ok, resp = common.post_json_webhook("s9-m6-read", body)
    if not ok:
        return {"ok": False, "error": resp}
    content = resp.get("choices", [{}])[0].get("message", {}).get("content", "")
    parsed, parse_err = parse_model_json(content)
    exec_id = common.latest_execution_id(api_url, api_key, WORKFLOW_ID, t0_ms)
    return {"ok": True, "execution_id": exec_id, "raw_content": content,
            "parsed": parsed, "parse_error": parse_err}


def main():
    api_url, api_key = common.env_or_die()
    all_results = {}
    n_valid_json = 0
    n_sum_wrong_but_valid_json = 0
    n_date_wrong_but_valid_json = 0
    n_calls = 0

    for receipt_id, truth in TRUTH.items():
        print(f"\n=== {receipt_id} (верно: {truth['sum']} / {truth['date']}) ===")
        entries = []
        for i in range(1, N_PER_RECEIPT + 1):
            entry = call_once(receipt_id, api_url, api_key)
            n_calls += 1
            if not entry["ok"]:
                print(f"  #{i} ОШИБКА: {entry['error']}")
                entries.append(entry)
                continue
            parsed = entry.get("parsed")
            valid_json = parsed is not None and "sum_rub" in parsed and "date" in parsed
            if valid_json:
                n_valid_json += 1
                sum_val = parsed.get("sum_rub")
                date_val = parsed.get("date")
                sum_correct = (isinstance(sum_val, (int, float)) and
                               abs(sum_val - truth["sum"]) < 0.01)
                date_correct = (date_val == truth["date"])
                entry["sum_correct"] = sum_correct
                entry["date_correct"] = date_correct
                if not sum_correct:
                    n_sum_wrong_but_valid_json += 1
                if not date_correct:
                    n_date_wrong_but_valid_json += 1
                print(f"  #{i} exec={entry['execution_id']} sum={sum_val} "
                      f"(correct={sum_correct}) date={date_val} (correct={date_correct}) "
                      f"raw_seen={parsed.get('raw_text_seen')}")
            else:
                entry["sum_correct"] = None
                entry["date_correct"] = None
                print(f"  #{i} exec={entry['execution_id']} НЕВАЛИДНЫЙ JSON: "
                      f"{entry['raw_content'][:200]}")
            entries.append(entry)
        all_results[receipt_id] = {"truth": truth, "entries": entries}

    out = {
        "n_calls": n_calls, "n_valid_json": n_valid_json,
        "n_sum_wrong_despite_valid_json": n_sum_wrong_but_valid_json,
        "n_date_wrong_despite_valid_json": n_date_wrong_but_valid_json,
        "by_receipt": all_results,
    }
    out_path = HERE / "results-k6-misread.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nИТОГО: {n_calls} вызовов, валидный JSON {n_valid_json}/{n_calls}, "
          f"сумма неверна при валидном JSON {n_sum_wrong_but_valid_json}, "
          f"дата неверна при валидном JSON {n_date_wrong_but_valid_json} -> {out_path}")


if __name__ == "__main__":
    main()
