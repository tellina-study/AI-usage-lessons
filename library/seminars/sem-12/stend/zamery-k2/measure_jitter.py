#!/usr/bin/env python3
"""Замер №3 (ARCHITECTURE.md §8, SETKA-KEYSOV.md Кейс 2) — дрожание входа.

Вопрос: для одной и той же картинки, подвергнутой лёгкому и жёсткому файловому
искажению, насколько уезжает вектор (cosine с оригиналом) и меняется ли первый сосед
при поиске среди всех 30 оригиналов — по каждой из двух рабочих моделей С10
(margin 0,593 и 0,392): nvidia/nemotron-3.5-embed-1b:free и
nvidia/llama-nemotron-embed-vl-1b-v2:free.

Пять вариантов искажения (НЕ C10's soft/hard — тоньше, по заданию):
downscale_60pct, recompress_q30, rotate_1deg, crop_5pct — каждый меняет один параметр;
composite_rotate_crop — заявленный трудный случай (поворот+обрезка вместе).

Требует кэш оригиналов (raw/originals_<model>.json), который пишет fetch_originals.py —
запускать после него. Прогон на ВСЕХ 30 сканах (не выборке) — установленная норма стенда
после замечания владельца на С10 (sem-10/stend/README.md §Корпус).
"""
import json
import time

from common_k2 import VARIANTS, cosine, embed_mm, load_corpus, load_or_fetch_originals

MODELS = [
    "nvidia/nemotron-3.5-embed-1b:free",
    "nvidia/llama-nemotron-embed-vl-1b-v2:free",
]


def nearest(query_vec, pool):
    best, best_score = None, -2.0
    for sid, v in pool.items():
        if v is None:
            continue
        s = cosine(query_vec, v)
        if s > best_score:
            best_score, best = s, sid
    return best, best_score


def main():
    samples, ids, paths = load_corpus()
    t0 = time.time()
    out = {"models": MODELS, "variants": list(VARIANTS.keys()), "per_model": {}}

    for model in MODELS:
        print(f"\n=== {model}: оригиналы (кэш) ===")
        originals, orig_fail, orig_cost = load_or_fetch_originals(model, ids, paths)
        n_orig_ok = sum(1 for v in originals.values() if v is not None)
        print(f"  оригиналов: {n_orig_ok}/{len(ids)} ok")

        model_out = {"n_originals_ok": n_orig_ok, "originals_fail": orig_fail,
                     "originals_cost_usd": round(orig_cost, 6), "variants": {}}

        for vname, vfunc in VARIANTS.items():
            print(f"  --- {model} / {vname} ---")
            rows = []
            fail_log = []
            total_cost = orig_cost if False else 0.0  # отдельный счёт за эту серию
            for sid in ids:
                data_url = vfunc(paths[sid])
                vec, cost, err = embed_mm(model, data_url)
                if cost:
                    total_cost += cost
                if vec is None:
                    fail_log.append({"id": sid, "error": err})
                    print(f"    {sid}: FAIL ({err[:80] if err else '?'})")
                    time.sleep(0.4)
                    continue
                own_orig = originals.get(sid)
                cos_to_own = cosine(vec, own_orig) if own_orig is not None else None
                nn_id, nn_score = nearest(vec, originals)
                row = {
                    "id": sid,
                    "cosine_to_own_original": round(cos_to_own, 4) if cos_to_own is not None else None,
                    "nearest_original": nn_id,
                    "nearest_cosine": round(nn_score, 4),
                    "self_match": (nn_id == sid),
                }
                rows.append(row)
                print(f"    {sid}: cos_own={row['cosine_to_own_original']} "
                      f"nn={nn_id} self_match={row['self_match']}")
                time.sleep(0.4)

            n = len(rows)
            n_self = sum(1 for r in rows if r["self_match"])
            cos_values = [r["cosine_to_own_original"] for r in rows if r["cosine_to_own_original"] is not None]
            summary = {
                "n_ok": n,
                "n_fail": len(fail_log),
                "recall_at_1_self_match": round(n_self / n, 4) if n else None,
                "n_nn_switched": n - n_self,
                "mean_cosine_to_own_original": round(sum(cos_values) / len(cos_values), 4) if cos_values else None,
                "min_cosine_to_own_original": round(min(cos_values), 4) if cos_values else None,
                "max_cosine_to_own_original": round(max(cos_values), 4) if cos_values else None,
                "cost_usd": round(total_cost, 6),
            }
            print(f"  ИТОГ {model}/{vname}: {json.dumps(summary, ensure_ascii=False)}")
            model_out["variants"][vname] = {"summary": summary, "details": rows, "fail_log": fail_log}

            # checkpoint после каждого варианта — не терять прогресс при сбое следующего
            out["per_model"][model] = model_out
            json.dump(out, open("raw/jitter_results.json", "w", encoding="utf-8"),
                       ensure_ascii=False, indent=2)

    elapsed = time.time() - t0
    out["elapsed_s"] = round(elapsed, 1)
    json.dump(out, open("raw/jitter_results.json", "w", encoding="utf-8"),
               ensure_ascii=False, indent=2)
    print(f"\n=== ЗАМЕР №3 ЗАВЕРШЁН за {elapsed:.1f}s ===")


if __name__ == "__main__":
    main()
