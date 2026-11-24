#!/usr/bin/env python3
"""Кейс A, вариант 3 — гибрид: OCR-текст (rapidocr-onnxruntime, уже прогнан, см.
raw/ocr_results.json) подаётся текстом в openai/gpt-4o-mini с тем же JSON-промтом, что
у варианта «модель-зрение» (harness_a.SYS_EXTRACT/build_user_prompt) — меняется только
вход (текст вместо картинки), промт и схема не меняются (С6: единица сравнения общая).

Запуск:
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    cd library/seminars/sem-12/stend/zamery-A
    .venv/bin/python3 measure_hybrid.py
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from harness_a import SYS_EXTRACT, build_user_prompt, extract_json, text_call

HERE = Path(__file__).resolve().parent
OUT_PATH = HERE / "raw" / "hybrid_results.json"


def run_one(form, ocr_text):
    fid = form["form_id"]
    user = (
        build_user_prompt(form["targets"])
        + "\n\nТекст документа (результат OCR, построчно, без сохранения исходной "
          "раскладки):\n---\n" + ocr_text + "\n---"
    )
    t0 = time.time()
    r = text_call(SYS_EXTRACT, user)
    r["wall_s_outer"] = round(time.time() - t0, 2)
    r["parsed"] = extract_json(r["content"])
    return fid, r


def main():
    corpus = json.load(open(HERE / "korpus" / "vyborka.json"))
    ocr = json.load(open(HERE / "raw" / "ocr_results.json"))["per_form"]
    out = {}
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(run_one, form, ocr[form["form_id"]]["text_joined"]): form["form_id"]
                for form in corpus}
        for fut in as_completed(futs):
            fid, r = fut.result()
            out[fid] = r
            ok = r["parsed"] is not None
            print(fid, f"{r['wall_s_outer']}s", "cost=", r.get("cost"), "parsed_ok=", ok)
    total = time.time() - t0
    total_cost = sum((out[f].get("cost") or 0) for f in out)
    print(f"ИТОГО {total:.1f}s, {len(out)} форм, цена ${total_cost:.4f}")
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump({"meta": {"model": "openai/gpt-4o-mini (текст, вход — OCR rapidocr-onnxruntime)",
                             "n_forms": len(out), "total_cost": round(total_cost, 6),
                             "total_wall_s": round(total, 2)},
                   "per_form": out}, fh, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
