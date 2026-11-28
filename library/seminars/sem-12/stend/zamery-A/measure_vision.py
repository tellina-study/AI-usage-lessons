#!/usr/bin/env python3
"""Кейс A, вариант 1 — мультимодальная модель (openai/gpt-4o-mini, image_url data-URL) извлекает
целевые поля напрямую с картинки. 30 реальных вызовов, по одному на форму (все 4-6
целевых полей формы — одним JSON-вызовом, не по полю отдельно).

Запуск:
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    cd library/seminars/sem-12/stend/zamery-A
    .venv/bin/python3 measure_vision.py
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from harness_a import SYS_EXTRACT, build_user_prompt, extract_json, to_data_url, vision_call

HERE = Path(__file__).resolve().parent
BASE_DIR = Path("/tmp/s12-corpora/funsd/dataset")
OUT_PATH = HERE / "raw" / "vision_results.json"


def run_one(form):
    fid = form["form_id"]
    img_path = BASE_DIR / form["split"] / "images" / form["img"]
    data_url = to_data_url(img_path)
    user = build_user_prompt(form["targets"])
    t0 = time.time()
    r = vision_call(SYS_EXTRACT, user, data_url)
    r["wall_s_outer"] = round(time.time() - t0, 2)
    r["parsed"] = extract_json(r["content"])
    return fid, r


def main():
    corpus = json.load(open(HERE / "korpus" / "vyborka.json"))
    out = {}
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(run_one, form): form["form_id"] for form in corpus}
        for fut in as_completed(futs):
            fid, r = fut.result()
            out[fid] = r
            ok = r["parsed"] is not None
            print(fid, f"{r['wall_s_outer']}s", "cost=", r.get("cost"), "parsed_ok=", ok)
    total = time.time() - t0
    total_cost = sum((out[f].get("cost") or 0) for f in out)
    print(f"ИТОГО {total:.1f}s, {len(out)} форм, цена ${total_cost:.4f}")
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump({"meta": {"model": "openai/gpt-4o-mini", "n_forms": len(out),
                             "total_cost": round(total_cost, 6), "total_wall_s": round(total, 2)},
                   "per_form": out}, fh, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
