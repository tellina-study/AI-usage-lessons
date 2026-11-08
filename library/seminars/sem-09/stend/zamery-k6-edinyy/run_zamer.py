#!/usr/bin/env python3
"""Замер А (Задание З3, issue #299) — единый мультимодальный вызов: в ОДНОМ запросе к
модели уходят фотография квитанции И текст заявки клиента с суммой, модель читает
фотографию и сама сравнивает прочитанное с заявкой.

30 живых вызовов — та же `receipt-01` на тех же шести разрешениях
(`../zamery-k5-k6/receipts/resolution/`), что и двухшаговый бейзлайн
(`../zamery-k5-k6/results-k6-resolution.json`), 5 повторов на разрешение, та же модель
(`qwen/qwen3-vl-8b-instruct`), та же температура (0.2 — см. `sborka.py`, расхождение с
заданием зафиксировано там и в README). План вызовов и текст промта — ОДИН модуль
`promt.py`, читаемый и этим файлом, и `proverka_protechki.py` (чтобы проверка на
протечку проверяла именно то, что уйдёт на стенд).

Usage:
    N8N_API_URL=... N8N_API_KEY=... python3 proverka_protechki.py   # ДО вызова, обязательно
    N8N_API_URL=... N8N_API_KEY=... python3 run_zamer.py
"""
import base64
import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
K5K6 = HERE.parent / "zamery-k5-k6"
sys.path.insert(0, str(K5K6))
sys.path.insert(0, str(HERE))
import common  # noqa: E402  (../zamery-k5-k6/common.py — только читаем, не меняем)
import promt  # noqa: E402

WORKFLOW_ID = None  # заполняется после первого `sborka.py --push`, см. README/stend-id.json
RAW_DIR = HERE / "raw"
RAW_DIR.mkdir(exist_ok=True)

manifest = json.loads((K5K6 / "receipts-manifest.json").read_text(encoding="utf-8"))
RES_INFO = {r["name"]: r for r in manifest["resolution_variants"]}


def telo_zaprosa(entry):
    """Собирает тело HTTP-запроса на вебхук `s9-m6-edinyy` — ровно те поля, что уходят
    на стенд, ни одного лишнего. Читает те же файлы картинок, что бейзлайн (пути из
    `../zamery-k5-k6/receipts-manifest.json`, относительно `../zamery-k5-k6/`)."""
    path = RES_INFO[entry["resolution"]]["file"]
    img_bytes = (K5K6 / path).read_bytes()
    b64 = base64.b64encode(img_bytes).decode()
    return {
        "image_base64": b64, "mime_type": "image/png",
        "receipt_id": entry["receipt_id"],
        "prompt_text": promt.build_prompt(entry),
    }


def to_number(x):
    """Модель форматирует числа по-разному («18990», «18990,00», «18 990») несмотря на
    просьбу «без пробелов и валюты» — пилотный вызов (execution 1829, resolution=full)
    вернул `sum_rub: "18990,00"` строкой с запятой вместо точки. Сравнение чисел ОБЯЗАНО
    пройти через этот парсер, иначе честный правильный ответ в непривычном формате
    засчитался бы как ошибка — это была бы ошибка измерения, не модели."""
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    s = re.sub(r"[^\d,.\-]", "", str(x).strip())
    if not s:
        return None
    if "," in s and "." not in s:
        last = s.split(",")[-1]
        s = s.replace(",", ".") if len(last) == 2 else s.replace(",", "")
    elif "," in s and "." in s:
        s = s.replace(",", "")
    try:
        return float(s)
    except Exception:
        return None


def parse_model_json(content):
    cleaned = re.sub(r"^```(json)?|```$", "", content.strip(), flags=re.MULTILINE).strip()
    try:
        return json.loads(cleaned), None
    except Exception as e:
        return None, str(e)


def call_once(entry, api_url, api_key, workflow_id):
    body = telo_zaprosa(entry)
    t0_ms = time.time() * 1000
    ok, resp = common.post_json_webhook("s9-m6-edinyy", body)
    if not ok:
        return {"ok": False, "error": resp, "entry": entry}
    content = resp.get("choices", [{}])[0].get("message", {}).get("content", "")
    parsed, parse_err = parse_model_json(content)
    exec_id = common.latest_execution_id(api_url, api_key, workflow_id, t0_ms)
    return {
        "ok": True, "execution_id": exec_id, "raw_content": content,
        "parsed": parsed, "parse_error": parse_err,
        "usage": resp.get("usage", {}),
        "entry": entry,
        "prompt_sha256": __import__("hashlib").sha256(
            body["prompt_text"].encode("utf-8")).hexdigest(),
    }


def evaluate(record):
    entry = record["entry"]
    parsed = record.get("parsed") or {}
    sum_val = to_number(parsed.get("sum_rub"))
    date_val = parsed.get("date")
    zayavka_echo = to_number(parsed.get("zayavka_sum_rub"))
    verdict_raw = str(parsed.get("verdict", "")).strip().lower()

    sum_correct = (sum_val is not None and abs(sum_val - promt.TRUE_SUM) < 0.01)
    date_correct = (date_val == promt.TRUE_DATE)

    true_verdict = "sovpalo" if entry["zayavka_verna"] else "ne_sovpalo"
    # Модель иногда отвечает синонимами несмотря на просьбу — нормализуем мягко, но
    # фиксируем сырое значение отдельно, чтобы не замести под ковёр странный ответ.
    verdict_norm = None
    if verdict_raw in ("sovpalo", "совпало", "match", "true", "да"):
        verdict_norm = "sovpalo"
    elif verdict_raw in ("ne_sovpalo", "не совпало", "не_совпало", "mismatch",
                         "false", "нет"):
        verdict_norm = "ne_sovpalo"
    verdict_correct = (verdict_norm == true_verdict)

    # Самосогласованность (диагностика, не из задания, но нужна чтобы отличить «модель
    # промахнулась мимо правды» от «модель запуталась в собственном сравнении»):
    # совпадает ли вердикт модели с НАИВНЫМ численным сравнением ЕЁ ЖЕ двух названных
    # чисел (sum_rub против zayavka_sum_rub), независимо от того, правильны ли они
    # относительно истины. Пилотный вызов (execution 1829) дал sum_rub=18990,00,
    # zayavka_sum_rub=18990 — численно РАВНЫ — но verdict=ne_sovpalo: модель сама себе
    # противоречит, видимо из-за разницы в форматировании строки («,00» против без
    # него), а не из-за фактического расхождения сумм.
    self_consistent = None
    if sum_val is not None and zayavka_echo is not None and verdict_norm is not None:
        naive_match = abs(sum_val - zayavka_echo) < 0.01
        self_consistent = (verdict_norm == "sovpalo") == naive_match

    # Якорение (главный побочный вопрос задания): в случаях zayavka_verna=False —
    # назвала ли модель прочитанной СУММОЙ ФОТОГРАФИИ именно сумму заявки (неверную),
    # а не настоящую сумму квитанции? Это отдельно от sum_correct (которое просто
    # "неверно"): здесь проверяем КОНКРЕТНО подтягивание к заявке.
    anchored_to_claim = None
    if not entry["zayavka_verna"] and sum_val is not None:
        anchored_to_claim = abs(sum_val - entry["zayavka_sum"]) < 0.01 and not sum_correct

    record["sum_correct"] = sum_correct
    record["date_correct"] = date_correct
    record["true_verdict"] = true_verdict
    record["verdict_raw"] = verdict_raw
    record["verdict_norm"] = verdict_norm
    record["verdict_correct"] = verdict_correct
    record["self_consistent"] = self_consistent
    record["anchored_to_claim"] = anchored_to_claim
    record["zayavka_echo"] = zayavka_echo
    return record


def main():
    api_url, api_key = common.env_or_die()
    stend_ids_path = HERE / "stend-ids.json"
    if not stend_ids_path.exists():
        print("stend-ids.json не найден — сначала `python3 sborka.py --push`, "
              "затем записать выданный id сценария в stend-ids.json: "
              '{"k6-edinyy": "<id>"}', file=sys.stderr)
        sys.exit(1)
    workflow_id = json.loads(stend_ids_path.read_text(encoding="utf-8"))["k6-edinyy"]

    plan = promt.plan()
    all_records = []
    rejected = []  # отклонены ДО модели (не в счёт бюджета) — фиксируем отдельно

    for entry in plan:
        raw_path = RAW_DIR / f"{entry['resolution']}-{entry['repeat_idx']}.json"
        if raw_path.exists():
            # Пилотный вызов (execution 1829, resolution=full #1) уже сделан вручную
            # ДО этого запуска, во время проверки проводки — повторный вызов на тот же
            # (resolution, repeat_idx) потратил бы живой вызов бюджета впустую на то,
            # что уже измерено. Пересчитываем метрики заново (evaluate() менялся после
            # пилота — добавлен to_number/self_consistent), но САМ вызов не повторяем.
            cached = json.loads(raw_path.read_text(encoding="utf-8"))
            rec = evaluate(cached)
            print(f"  {entry['resolution']:12s} #{entry['repeat_idx']} "
                  f"(из кэша, пилотный вызов exec={rec.get('execution_id')})")
            all_records.append(rec)
            raw_path.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
            continue
        rec = call_once(entry, api_url, api_key, workflow_id)
        if rec["ok"]:
            rec = evaluate(rec)
            print(f"  {entry['resolution']:12s} #{entry['repeat_idx']} "
                  f"exec={rec.get('execution_id')} verna={entry['zayavka_verna']!s:5s} "
                  f"sum={rec['parsed'].get('sum_rub') if rec['parsed'] else None} "
                  f"(ok={rec['sum_correct']}) date={rec['parsed'].get('date') if rec['parsed'] else None} "
                  f"(ok={rec['date_correct']}) verdict={rec['verdict_raw']!r} "
                  f"(ok={rec['verdict_correct']}) anchored={rec['anchored_to_claim']}")
        else:
            http_status = rec["error"].get("http_status") if isinstance(rec["error"], dict) else None
            print(f"  {entry['resolution']:12s} #{entry['repeat_idx']} ОШИБКА: {rec['error']}")
            if http_status in (400, 404, 422):
                rejected.append(rec)
                continue  # не входит в счёт вызовов, доехавших до модели
        all_records.append(rec)
        # не раскрываем ключи — это уже делает common.py; просто пауза, чтобы не
        # долбить вебхук быстрее, чем предыдущий execution успевает записаться.
        time.sleep(0.3)
        raw_path.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")

    by_resolution = {}
    for res in promt.RESOLUTIONS:
        entries = [r for r in all_records if r["entry"]["resolution"] == res and r["ok"]]
        by_resolution[res] = {
            "glyph_height_px": None,  # см. receipts-manifest.json при желании сопоставить
            "n": len(entries),
            "n_sum_correct": sum(1 for e in entries if e.get("sum_correct")),
            "n_date_correct": sum(1 for e in entries if e.get("date_correct")),
            "n_verdict_correct": sum(1 for e in entries if e.get("verdict_correct")),
            "n_anchored_to_claim": sum(1 for e in entries if e.get("anchored_to_claim")),
            "n_self_inconsistent": sum(1 for e in entries if e.get("self_consistent") is False),
            "entries": entries,
        }

    out = {
        "true_sum": promt.TRUE_SUM, "true_date": promt.TRUE_DATE,
        "model": "qwen/qwen3-vl-8b-instruct", "temperature": 0.2,
        "n_total_ok": len(all_records),
        "n_rejected_before_model": len(rejected),
        "rejected": rejected,
        "by_resolution": by_resolution,
    }
    (HERE / "results-k6-edinyy.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\nСВОДКА (единый вызов):")
    for res in promt.RESOLUTIONS:
        r = by_resolution[res]
        print(f"  {res:12s} сумма {r['n_sum_correct']}/{r['n']}  дата {r['n_date_correct']}/{r['n']}  "
              f"вердикт {r['n_verdict_correct']}/{r['n']}  якорение={r['n_anchored_to_claim']}  "
              f"самопротиворечие={r['n_self_inconsistent']}")
    print(f"\nВызовов, доехавших до модели: {len(all_records)}  "
          f"отклонено до модели: {len(rejected)}")
    print(f"-> results-k6-edinyy.json")


if __name__ == "__main__":
    main()
