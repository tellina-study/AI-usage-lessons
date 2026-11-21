#!/usr/bin/env python3
"""ДОПОЛНЕНИЕ к замеру №3 (не замена) — третий, самый грубый уровень искажения, по
прямому требованию оркестратора 2026-11-21: ноль переключений первого соседа у
CLIP/SigLIP на пяти своих вариантах (`measure_jitter_local.py`, 1°/5%/q30/60%) недостаточен
как результат по канону §8.11, пока не проверен силой, которую СОСЕДНИЙ Кейс 4 того же
занятия (ветка `hc/s12-k4-porog-2-bc37ac51`, `stend/zamery-k4/measure_siglip_local.py`,
прочитан через `git show`, НЕ переключаясь на чужую ветку) уже прогнал на той же модели —
и получил НЕ ноль (полоса неопределённости на 75% выборки, 45 пар из 60).

Искажения — `soft_dup`/`hard_dup`, импортированы НАПРЯМУЮ (не переписаны) из
`sem-10/stend/measure/case4_full_retrieval_30.py` — тот же приём cwd-переключения на
время импорта, что и в `zamery-k4/measure_siglip_local.py` (он читает corpus-метаданные
относительным путём при импорте модуля):
  - soft_dup: resize×0,97 + пересжатие q60 (мягче, чем у Кейса 4 названо "лёгким", но это
    ИХ лёгкий случай, не наш — raw-функция идентична байт-в-байт);
  - hard_dup: поворот 12° + обрезка 4% краёв + resize назад до 300×450 (это их ТРУДНЫЙ
    случай и САМАЯ ГРУБАЯ деформация, что встречалась в этом занятии вообще).

Метрика — СВОЯ (switch_rate = 1 − recall@1 self-match, mean_cos), НЕ band-метрика Кейса 4
(полоса между same/diff) — они измеряют разные вещи на одних и тех же файлах; расхождение
между "ноль по switch_rate" и "не-ноль по band-метрике" тоже возможная находка, см. README.

Модели: CLIP ViT-B/32, SigLIP (оба — локально, originals пересчитаны заново: в
`measure_jitter_local.py` они не персистились как отдельный файл) + voyage-multimodal-3.5
(платно, originals — из уже посчитанного кэша `raw/originals_mongodb_voyage-multimodal-3.5.json`,
только 60 новых вызовов на soft/hard).
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SEM10_MEASURE = os.path.join(HERE, "..", "..", "..", "sem-10", "stend", "measure")
sys.path.insert(0, SEM10_MEASURE)
_cwd_before_import = os.getcwd()
os.chdir(SEM10_MEASURE)  # case4_full_retrieval_30.py читает corpus-метаданные относительным путём при импорте
from case4_full_retrieval_30 import soft_dup, hard_dup, to_data_url  # noqa: E402
os.chdir(_cwd_before_import)

from common_k2 import cosine, embed_mm, load_corpus, load_or_fetch_originals  # noqa: E402
from measure_jitter_local import data_url_to_pil, embed_local, load_clip, load_siglip, nearest  # noqa: E402

VOYAGE_MODEL = "mongodb/voyage-multimodal-3.5"
DEFORMATIONS = {"case4_soft_dup": soft_dup, "case4_hard_dup": hard_dup}


def eval_one(originals, model_vec_fn, ids):
    """originals: {id: vec}; model_vec_fn(sid, def_name) -> vec. Возвращает per-deformation
    summary+details, той же формой, что measure_jitter_local.py."""
    out = {}
    for dname, dfunc in DEFORMATIONS.items():
        rows, fail_log = [], []
        for sid in ids:
            vec, err = model_vec_fn(sid, dfunc)
            if vec is None:
                fail_log.append({"id": sid, "error": err})
                continue
            own_orig = originals.get(sid)
            cos_to_own = cosine(vec, own_orig) if own_orig is not None else None
            nn_id, nn_score = nearest(vec, originals)
            rows.append({
                "id": sid,
                "cosine_to_own_original": round(cos_to_own, 4) if cos_to_own is not None else None,
                "nearest_original": nn_id,
                "nearest_cosine": round(nn_score, 4),
                "self_match": (nn_id == sid),
            })
        n = len(rows)
        n_self = sum(1 for r in rows if r["self_match"])
        cos_values = [r["cosine_to_own_original"] for r in rows if r["cosine_to_own_original"] is not None]
        summary = {
            "n_ok": n, "n_fail": len(fail_log),
            "recall_at_1_self_match": round(n_self / n, 4) if n else None,
            "n_nn_switched": n - n_self,
            "mean_cosine_to_own_original": round(sum(cos_values) / len(cos_values), 4) if cos_values else None,
        }
        print(f"  ИТОГ {dname}: {json.dumps(summary, ensure_ascii=False)}")
        out[dname] = {"summary": summary, "details": rows, "fail_log": fail_log}
    return out


def run_local(model_name, load_fn, ids, paths):
    model, processor, load_s, torch = load_fn()
    print(f"--- {model_name}: 30 оригиналов (пересчёт — не персистились из measure_jitter_local.py) ---")
    originals = {}
    for sid in ids:
        pil = data_url_to_pil(to_data_url(paths[sid]))
        vec, _ = embed_local(model, processor, torch, pil)
        originals[sid] = vec

    def model_vec_fn(sid, dfunc):
        pil = data_url_to_pil(dfunc(paths[sid]))
        vec, _ = embed_local(model, processor, torch, pil)
        return vec, None

    print(f"--- {model_name}: деформация силой Кейса 4 ---")
    return eval_one(originals, model_vec_fn, ids), 0.0


def run_voyage(ids, paths):
    print(f"--- {VOYAGE_MODEL}: оригиналы из кэша (не пересчитываем) ---")
    originals, _, orig_cost = load_or_fetch_originals(VOYAGE_MODEL, ids, paths)
    print(f"  оригиналов: {sum(1 for v in originals.values() if v)}/{len(ids)} ok (из кэша)")

    total_new_cost = [0.0]

    def model_vec_fn(sid, dfunc):
        vec, cost, err = embed_mm(VOYAGE_MODEL, dfunc(paths[sid]))
        if cost:
            total_new_cost[0] += cost
        import time as _t
        _t.sleep(0.4)
        return vec, err

    print(f"--- {VOYAGE_MODEL}: деформация силой Кейса 4 ---")
    result = eval_one(originals, model_vec_fn, ids)
    return result, total_new_cost[0]


def main():
    samples, ids, paths = load_corpus()
    t0 = time.time()
    out = {
        "purpose": "Дополнение к замеру №3 — деформация силой соседнего Кейса 4 "
                   "(soft_dup/hard_dup из case4_full_retrieval_30.py, импортированы напрямую, "
                   "не переписаны), по требованию оркестратора: ноль переключений на своих "
                   "пяти мягче вариантах не считается результатом, пока не проверен силой, на "
                   "которой Кейс 4 получил НЕ ноль (band 75% выборки).",
        "deformations": {
            "case4_soft_dup": "resize×0,97 + пересжатие q60 (их лёгкий случай)",
            "case4_hard_dup": "поворот 12° + обрезка 4% краёв (их трудный случай — самая "
                              "грубая деформация во всём занятии)",
        },
        "models": {},
    }

    print("\n=== CLIP, деформация силой Кейса 4 ===")
    res, cost = run_local("CLIP", load_clip, ids, paths)
    out["models"]["openai/clip-vit-base-patch32"] = {"deformations": res, "cost_usd": cost}
    json.dump(out, open("raw/jitter_case4_strength_results.json", "w", encoding="utf-8"),
               ensure_ascii=False, indent=2)

    print("\n=== SigLIP, деформация силой Кейса 4 ===")
    res, cost = run_local("SigLIP", load_siglip, ids, paths)
    out["models"]["google/siglip-base-patch16-224"] = {"deformations": res, "cost_usd": cost}
    json.dump(out, open("raw/jitter_case4_strength_results.json", "w", encoding="utf-8"),
               ensure_ascii=False, indent=2)

    print(f"\n=== {VOYAGE_MODEL}, деформация силой Кейса 4 ===")
    res, cost = run_voyage(ids, paths)
    out["models"][VOYAGE_MODEL] = {"deformations": res, "cost_usd": round(cost, 6)}
    out["elapsed_s"] = round(time.time() - t0, 1)
    json.dump(out, open("raw/jitter_case4_strength_results.json", "w", encoding="utf-8"),
               ensure_ascii=False, indent=2)
    print(f"\n=== ДОПОЛНЕНИЕ ЗАВЕРШЕНО за {out['elapsed_s']}s -> raw/jitter_case4_strength_results.json ===")


if __name__ == "__main__":
    main()
