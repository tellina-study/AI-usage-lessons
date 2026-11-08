#!/usr/bin/env python3
"""Замер 4.1 — Кейс 6: сжатие/разрешение против точности чтения. Одна и та же состаренная
квитанция (`receipt-01`) в шести разрешениях (`receipts/resolution/receipt-01-{full,half,
quarter,eighth,sixteenth,thirtysecond}.png`) — по 5 живых вызовов на разрешение через
`С9 · замер K6 — чтение фотографии квитанции` (`s9-m6-read`). Мерит: на каком разрешении
падает точность суммы, ломаются ли цифры раньше букв (сумма против даты), высота символа
суммы на каждом разрешении (геометрия ресайза, см. `generate_receipts.py` /
`receipts-manifest.json`).

**Честное переизмерение 2026-10-27 (issue #299) — протечка промта.** Промт `k6_read()`
в `sborka.py` до этой правки содержал РЕАЛЬНУЮ сумму `receipt-01` (`например 18990.00`)
как «пример формата» — модели не нужно было читать фотографию, достаточно было
скопировать число из собственной инструкции. Это полностью объясняло 100% точность
суммы даже на разрешениях, где глазом не видно ни одной цифры. Промт исправлен (число-
пример убрано), и ВСЕ 30 вызовов этого файла — свежие, ни один ответ не переиспользован
из предыдущей (протекавшей) эпохи измерения. Старый результат архивирован как
`results-k6-resolution-PROTECHKA-2026-10-27.json` — исторический артефакт протечки, не
источник действующих чисел (см. README «Протечка промта обнаружена и исправлена»).

Usage: N8N_API_URL=... N8N_API_KEY=... python3 run_k6_resolution.py
"""
import base64
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import common

HERE = Path(__file__).parent
TRUE_SUM = 18990.00
TRUE_DATE = "12.09.2026"
WORKFLOW_ID = "Sg3VSg0bIxqJOGCP"

manifest = json.loads((HERE / "receipts-manifest.json").read_text(encoding="utf-8"))
RES_INFO = {r["name"]: r for r in manifest["resolution_variants"]}

RESOLUTIONS = ["full", "half", "quarter", "eighth", "sixteenth", "thirtysecond"]
N_PER_RES = {"full": 5, "half": 5, "quarter": 5, "eighth": 5,
             "sixteenth": 5, "thirtysecond": 5}
# Единые 5 повторов на все шесть разрешений (честное переизмерение 2026-10-27, issue
# #299) — прежняя асимметрия 5/5/5/5/3/3 была следствием бюджета ПРЕДЫДУЩЕЙ (протекавшей)
# сессии измерения и закрывалась отдельным добором (`run_k6_resolution_topup.py`); раз всё
# равно переизмеряем с нуля из-за протечки промта, нет смысла повторять это в два захода.


def parse_model_json(content):
    # Модель иногда оборачивает JSON в ```json ... ``` несмотря на просьбу не делать этого —
    # снимаем обёртку перед парсингом, не считаем это отдельным классом отказа.
    cleaned = re.sub(r"^```(json)?|```$", "", content.strip(), flags=re.MULTILINE).strip()
    try:
        return json.loads(cleaned), None
    except Exception as e:
        return None, str(e)


def call_once(res_name, api_url, api_key):
    path = RES_INFO[res_name]["file"]
    img_bytes = (HERE / path).read_bytes()
    b64 = base64.b64encode(img_bytes).decode()
    body = {"image_base64": b64, "mime_type": "image/png", "receipt_id": f"receipt-01-{res_name}"}
    t0_ms = time.time() * 1000
    ok, resp = common.post_json_webhook("s9-m6-read", body)
    if not ok:
        return {"ok": False, "error": resp}
    content = resp.get("choices", [{}])[0].get("message", {}).get("content", "")
    parsed, parse_err = parse_model_json(content)
    exec_id = common.latest_execution_id(api_url, api_key, WORKFLOW_ID, t0_ms)
    return {
        "ok": True, "execution_id": exec_id, "raw_content": content,
        "parsed": parsed, "parse_error": parse_err,
        "usage": resp.get("usage", {}),
    }


def evaluate(entry):
    parsed = entry.get("parsed") or {}
    sum_val = parsed.get("sum_rub")
    date_val = parsed.get("date")
    sum_correct = (isinstance(sum_val, (int, float)) and abs(sum_val - TRUE_SUM) < 0.01)
    date_correct = (date_val == TRUE_DATE)
    entry["sum_correct"] = sum_correct
    entry["date_correct"] = date_correct
    return entry


def main():
    api_url, api_key = common.env_or_die()
    out_path = HERE / "results-k6-resolution.json"
    # Честное переизмерение 2026-10-27 (issue #299, протечка промта исправлена) — ВСЕ
    # шесть разрешений прогоняются заново живыми вызовами; старый (протекавший) файл
    # результатов архивирован отдельно (`results-k6-resolution-PROTECHKA-2026-10-27.json`,
    # см. README) и НЕ читается как кэш — сюда намеренно не возвращена логика
    # «уже прогнано ранее, пропускаю»: любой кэш из протекавшей эпохи был бы недействителен.
    all_results = {}

    for res_name in RESOLUTIONS:
        info = RES_INFO[res_name]
        n_for_this = N_PER_RES[res_name]
        print(f"\n=== {res_name} ({info['size'][0]}x{info['size'][1]}, "
              f"высота цифры суммы ~{info['amount_glyph_height_px']}px) ===")
        entries = []
        for i in range(1, n_for_this + 1):
            entry = call_once(res_name, api_url, api_key)
            if entry["ok"]:
                entry = evaluate(entry)
                print(f"  #{i} exec={entry.get('execution_id')} sum={entry['parsed'].get('sum_rub') if entry['parsed'] else None} "
                      f"(correct={entry['sum_correct']}) date={entry['parsed'].get('date') if entry['parsed'] else None} "
                      f"(correct={entry['date_correct']}) raw_seen={entry['parsed'].get('raw_text_seen') if entry['parsed'] else entry.get('raw_content')}")
            else:
                print(f"  #{i} ОШИБКА: {entry['error']}")
            entries.append(entry)
        all_results[res_name] = {
            "glyph_height_px": info["amount_glyph_height_px"],
            "image_size": info["size"], "entries": entries,
            "n_sum_correct": sum(1 for e in entries if e.get("sum_correct")),
            "n_date_correct": sum(1 for e in entries if e.get("date_correct")),
            "n": len(entries),
        }

    out_path.write_text(json.dumps({
        "true_sum": TRUE_SUM, "true_date": TRUE_DATE, "by_resolution": all_results,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\nСВОДКА:")
    for res_name in RESOLUTIONS:
        r = all_results[res_name]
        print(f"  {res_name:8s} glyph={r['glyph_height_px']:>5}px  "
              f"сумма верна {r['n_sum_correct']}/{r['n']}  дата верна {r['n_date_correct']}/{r['n']}")
    print(f"\n-> {out_path}")


if __name__ == "__main__":
    main()
