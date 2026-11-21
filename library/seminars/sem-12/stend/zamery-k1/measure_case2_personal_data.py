#!/usr/bin/env python3
"""Семинар 12, Кейс 1, Замер №2 — доля пропусков поля «персональные данные в кадре»
при трёх разрешениях x двух раскладках (лёгкая/трудная). Бинарный классификатор
gpt-4o-mini через вебхук стенда s10-raw-openrouter.

Позитивный набор (персональные/платёжные данные РЕАЛЬНО есть, проверено чтением
ocr_text всех 30 записей глазами, не только грепом владельца — см. README):
receipt_00, receipt_08, receipt_12, receipt_17, receipt_24, receipt_29 (6, не 5 —
receipt_17 ("Debit 91,000") грубый греп владельца пропустил).

Два режима запуска:
    python3 measure_case2_personal_data.py --pilot
        — пилот: 5 позитивных + 5 негативных x 2 раскладки x 6 разрешений шкалы
          (full/half/quarter/eighth/sixteenth/thirtysecond) — поиск градиента.
    python3 measure_case2_personal_data.py --final full half ... (3 имени шага)
        — финальный прогон: 6 позитивных + 9 негативных x 2 раскладки x 3 выбранных
          разрешения.
"""
import argparse
import json
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from harness2_lite import (
    SCALE_STEPS, extract_json, hard_layout_data_url, to_data_url, vision_call,
)
from PIL import Image

HERE = Path(__file__).resolve().parent
STEND_DIR = HERE.parent.parent.parent / "sem-10" / "stend"
CORPUS_DIR = STEND_DIR / "corpus"
META_PATH = CORPUS_DIR / "cord_sample_meta.json"

POSITIVES = ["receipt_00", "receipt_08", "receipt_12", "receipt_17", "receipt_24", "receipt_29"]
PILOT_POSITIVES = ["receipt_00", "receipt_08", "receipt_12", "receipt_17", "receipt_24"]
ALL_IDS = [f"receipt_{i:02d}" for i in range(30)]
NEG_POOL = [x for x in ALL_IDS if x not in POSITIVES]

_rnd = random.Random(12)
PILOT_NEG = sorted(_rnd.sample(NEG_POOL, 5))
_remaining = [x for x in NEG_POOL if x not in PILOT_NEG]
FINAL_NEG = sorted(PILOT_NEG + sorted(_rnd.sample(_remaining, 4)))

SYS_PROMPT = (
    'Ответь СТРОГО JSON {"personal_data_present": true/false, "reason": "одно короткое '
    'предложение почему"} — есть ли на этом изображении видимые персональные или '
    "платёжные данные: номер карты, ФИО, подпись, телефон? Если не уверен — дай лучшую "
    "оценку, не отказывайся отвечать. Кроме JSON ничего не пиши."
)
USER_TEXT = "Есть ли на этом изображении персональные/платёжные данные?"


def path_for(rid, meta_by_id):
    return STEND_DIR / meta_by_id[rid]["file"]


def make_image(rid, path, layout, scale_name):
    scale = SCALE_STEPS[scale_name]
    with Image.open(path) as im:
        ow, oh = im.size
    tw, th = max(1, round(ow * scale)), max(1, round(oh * scale))
    if layout == "easy":
        return to_data_url(str(path), w=tw, h=th), (tw, th)
    else:
        return hard_layout_data_url(str(path), tw, th), (tw, th)


def call_one(rid, path, layout, scale_name):
    img, dims = make_image(rid, path, layout, scale_name)
    r = vision_call(SYS_PROMPT, USER_TEXT, img, timeout=90)
    parsed = extract_json(r.get("content"))
    pred = parsed.get("personal_data_present") if isinstance(parsed, dict) else None
    reason = parsed.get("reason") if isinstance(parsed, dict) else None
    return {
        "id": rid, "layout": layout, "scale": scale_name, "dims": dims,
        "gold_positive": rid in POSITIVES,
        "pred": pred, "reason": reason, "raw_content": r.get("content"),
        "exec_id": r.get("exec_id"), "wall_s": r.get("wall_s"),
        "cost": r.get("cost"), "prompt_tokens": r.get("prompt_tokens"),
    }


def run_batch(jobs, max_workers=6):
    results = []
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futs = {ex.submit(call_one, *j): j for j in jobs}
        done = 0
        for fut in as_completed(futs):
            j = futs[fut]
            try:
                r = fut.result()
            except Exception as e:
                rid, path, layout, scale_name = j
                r = {"id": rid, "layout": layout, "scale": scale_name, "pred": None,
                     "gold_positive": rid in POSITIVES, "error": str(e)}
            results.append(r)
            done += 1
            if done % 10 == 0:
                print(f"    ... {done}/{len(jobs)} ({time.time()-t0:.0f}с)")
    print(f"  батч из {len(jobs)} занял {time.time()-t0:.1f}с")
    return results


def summarize(results):
    by_key = {}
    for r in results:
        key = (r["scale"], r["layout"])
        by_key.setdefault(key, []).append(r)
    summary = {}
    for (scale, layout), rows in by_key.items():
        pos = [r for r in rows if r["gold_positive"]]
        neg = [r for r in rows if not r["gold_positive"]]
        pos_miss = [r for r in pos if r["pred"] is False or r["pred"] is None]
        neg_fp = [r for r in neg if r["pred"] is True]
        summary[f"{scale}|{layout}"] = {
            "n_pos": len(pos), "n_neg": len(neg),
            "miss_rate_pos": len(pos_miss) / len(pos) if pos else None,
            "miss_count": len(pos_miss), "miss_ids": [r["id"] for r in pos_miss],
            "false_positive_rate_neg": len(neg_fp) / len(neg) if neg else None,
            "fp_count": len(neg_fp), "fp_ids": [r["id"] for r in neg_fp],
        }
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", action="store_true")
    ap.add_argument("--final", nargs=3, metavar=("SCALE1", "SCALE2", "SCALE3"))
    args = ap.parse_args()

    meta = json.load(open(META_PATH, encoding="utf-8"))
    meta_by_id = {s["id"]: s for s in meta}

    if args.pilot:
        ids = PILOT_POSITIVES + PILOT_NEG
        scales = list(SCALE_STEPS.keys())
        out_path = HERE / "raw" / "case2_pilot_results.json"
        print(f"ПИЛОТ: {len(ids)} изображений ({len(PILOT_POSITIVES)} позитив + {len(PILOT_NEG)} негатив) "
              f"x 2 раскладки x {len(scales)} разрешений = {len(ids)*2*len(scales)} вызовов")
    elif args.final:
        scales = list(args.final)
        for s in scales:
            assert s in SCALE_STEPS, f"неизвестный шаг шкалы: {s}"
        ids = POSITIVES + FINAL_NEG
        out_path = HERE / "raw" / "case2_personal_data_results.json"
        print(f"ФИНАЛ: {len(ids)} изображений ({len(POSITIVES)} позитив + {len(FINAL_NEG)} негатив) "
              f"x 2 раскладки x {len(scales)} разрешений ({scales}) = {len(ids)*2*len(scales)} вызовов")
    else:
        ap.error("нужен --pilot или --final SCALE1 SCALE2 SCALE3")
        return

    jobs = []
    for rid in ids:
        path = path_for(rid, meta_by_id)
        for layout in ("easy", "hard"):
            for scale_name in scales:
                jobs.append((rid, path, layout, scale_name))

    results = run_batch(jobs)
    summary = summarize(results)

    out = {
        "model": "openai/gpt-4o-mini", "mode": "pilot" if args.pilot else "final",
        "scales_tested": scales, "positives": POSITIVES if not args.pilot else PILOT_POSITIVES,
        "negatives": FINAL_NEG if not args.pilot else PILOT_NEG,
        "summary": summary, "results": results,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Записано: {out_path}")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
