#!/usr/bin/env python3
"""Кейс B, круг 3: два vision-метода (рассказ / поля) на ВСЁМ корпусе-101.

Промты, модель и вебхук — те же, что в `run_vision_descriptions.py` первого круга,
дословно (иначе 40 старых и 61 новый снимок стали бы несравнимы). Уже посчитанные
вызовы первого круга (`raw/vision_results.json`, 80 штук на 40 снимков) НЕ
перезапускаются — переносятся как есть, с пометкой `batch: "krug1"`; новые получают
`batch: "krug3"`. Это важно для честности строки «цена и задержка»: два прогона шли
в разное время и из разных сессий, и смешивать их задержки молча нельзя.

Запуск:  set -a; . ~/.n8n-lab.env; set +a; python3 run_vision_101.py
Выход:   raw/vision_results_101.json
"""
import json, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from harness2_lite import CHAT_MODEL, extract_json, to_data_url, vision_call, word_count
from run_vision_descriptions import SYS_CAPTION, USER_CAPTION, SYS_FIELDS, USER_FIELDS, VARIANTS

HERE = Path(__file__).resolve().parent
CORPUS = HERE / "corpus-cache"
OLD = HERE / "raw" / "vision_results.json"
OUT = HERE / "raw" / "vision_results_101.json"


def call_one(rid, variant):
    sys_p, user_p = {"caption": (SYS_CAPTION, USER_CAPTION),
                     "fields": (SYS_FIELDS, USER_FIELDS)}[variant]
    r = vision_call(sys_p, user_p, to_data_url(str(CORPUS / f"{rid}.jpg")))
    r.update(id=rid, variant=variant, batch="krug3")
    if variant == "fields":
        r["parsed"] = extract_json(r["content"])
    r["words"] = word_count(r["content"])
    return r


def main():
    doc = json.loads((HERE / "razmetka-101.json").read_text(encoding="utf-8"))
    ids = [e["id"] for e in doc["entries"] if e["in_corpus"]]
    old = json.loads(OLD.read_text(encoding="utf-8"))
    kept = []
    for r in old["results"]:
        r = dict(r); r["batch"] = "krug1"; kept.append(r)
    have = {(r["id"], r["variant"]) for r in kept if r.get("content")}
    jobs = [(rid, v) for rid in ids for v in VARIANTS if (rid, v) not in have]
    print(f"корпус {len(ids)}; перенесено из круга 1: {len(kept)}; новых вызовов: {len(jobs)}")

    results, t0 = [], time.time()
    with ThreadPoolExecutor(6) as ex:
        futs = {ex.submit(call_one, rid, v): (rid, v) for rid, v in jobs}
        for n, fut in enumerate(as_completed(futs), 1):
            rid, v = futs[fut]
            try:
                r = fut.result()
            except Exception as e:
                r = {"id": rid, "variant": v, "batch": "krug3", "error": str(e)}
            results.append(r)
            if n % 20 == 0 or not r.get("content"):
                print(f"  {n}/{len(jobs)} {rid} {v}: {'OK' if r.get('content') else 'FAIL ' + str(r.get('raw_error') or r.get('error'))}")

    allr = kept + results
    OUT.write_text(json.dumps({
        "model": CHAT_MODEL, "sys_caption": SYS_CAPTION, "user_caption": USER_CAPTION,
        "sys_fields": SYS_FIELDS, "user_fields": USER_FIELDS,
        "n_images": len(ids), "n_calls": len(allr),
        "krug3_wall_s": round(time.time() - t0, 1),
        "note": "batch=krug1 — 80 вызовов сессии s12-plan-abc-tri-keysa на 40 снимках; "
                "batch=krug3 — вызовы этой сессии на 61 добранном снимке; промты и модель те же",
        "results": allr,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    ok = sum(1 for r in allr if r.get("content"))
    empty = sum(1 for r in allr if not r.get("content"))
    print(f"\nзаписей в файле: {len(allr)}; НЕПУСТЫХ: {ok}; пустых/ошибок: {empty}")


if __name__ == "__main__":
    main()
