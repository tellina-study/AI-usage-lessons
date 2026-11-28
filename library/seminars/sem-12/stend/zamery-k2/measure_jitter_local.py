#!/usr/bin/env python3
"""Замер №3 (дрожание входа) — ФИНАЛЬНАЯ версия, после решения оркестратора 2026-11-21:
API-модели (`nvidia/nemotron-3.5-embed-1b:free`, `nvidia/llama-nemotron-embed-vl-1b-v2:free`)
заменены на ЛОКАЛЬНЫЕ CLIP ViT-B/32 и SigLIP (`google/siglip-base-patch16-224`) — тот же
рецепт и те же модели, что ставились на С10
(`sem-10/stend/measure/case4_local_clip_retrieval_30.py`,
`case4_local_siglip_retrieval_30.py`), плюс ОДНА платная модель как кросс-проверка —
`mongodb/voyage-multimodal-3.5` (уже 30/30 оригиналов в кэше, raw/originals_mongodb_voyage-
multimodal-3.5.json, переиспользуем, не пересчитываем).

Причина перехода на локальные модели — НЕ запасной вариант, а то, что лучше подходит самой
задаче: дрожание входа требует множества ДЕТЕРМИНИРОВАННЫХ повторных прогонов одного и того
же изображения, и локальная модель даёт бит-в-бит повторяемый результат без сетевой/очередной
нестабильности free-tier (которая и стала честной находкой №2/№3 этого замера — см. README).

Пять вариантов искажения (common_k2.VARIANTS, см. там же для точных параметров):
downscale_60pct, recompress_q30, rotate_1deg, crop_5pct (каждый меняет один параметр) и
composite_rotate_crop (заявленный трудный случай — поворот и обрезка одновременно).

Прогон на ВСЕХ 30 сканах CORD (не выборке).
"""
import base64
import io
import json
import time

from PIL import Image

from common_k2 import VARIANTS, cosine, embed_mm, load_corpus, load_or_fetch_originals

VOYAGE_MODEL = "mongodb/voyage-multimodal-3.5"


def data_url_to_pil(data_url):
    raw = base64.b64decode(data_url.split(",", 1)[1])
    return Image.open(io.BytesIO(raw)).convert("RGB")


def load_clip():
    import torch
    from transformers import CLIPModel, CLIPProcessor

    t0 = time.time()
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    model.eval()
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    load_s = time.time() - t0
    print(f"=== CLIP (openai/clip-vit-base-patch32) loaded in {load_s:.1f}s ===")
    return model, processor, load_s, torch


def load_siglip():
    import torch
    from transformers import SiglipModel, SiglipImageProcessor

    t0 = time.time()
    model = SiglipModel.from_pretrained("google/siglip-base-patch16-224")
    model.eval()
    processor = SiglipImageProcessor.from_pretrained("google/siglip-base-patch16-224")
    load_s = time.time() - t0
    print(f"=== SigLIP (google/siglip-base-patch16-224) loaded in {load_s:.1f}s ===")
    return model, processor, load_s, torch


def embed_local(model, processor, torch, pil_im):
    t0 = time.time()
    inputs = processor(images=pil_im, return_tensors="pt")
    with torch.no_grad():
        out = model.get_image_features(**inputs)
    vec = out.pooler_output[0].tolist()
    return vec, time.time() - t0


def nearest(query_vec, pool):
    best, best_score = None, -2.0
    for sid, v in pool.items():
        if v is None:
            continue
        s = cosine(query_vec, v)
        if s > best_score:
            best_score, best = s, sid
    return best, best_score


def run_local_model(model_name, load_fn, ids, paths, variant_fns_orig_data_url):
    model, processor, load_s, torch = load_fn()
    infer_times = []

    print(f"--- {model_name}: 30 оригиналов ---")
    originals = {}
    for sid in ids:
        data_url = variant_fns_orig_data_url(paths[sid])
        pil = data_url_to_pil(data_url)
        vec, dt = embed_local(model, processor, torch, pil)
        originals[sid] = vec
        infer_times.append(dt)

    variants_out = {}
    for vname, vfunc in VARIANTS.items():
        print(f"--- {model_name} / {vname} ---")
        rows = []
        for sid in ids:
            pil = data_url_to_pil(vfunc(paths[sid]))
            vec, dt = embed_local(model, processor, torch, pil)
            infer_times.append(dt)
            cos_to_own = cosine(vec, originals[sid])
            nn_id, nn_score = nearest(vec, originals)
            rows.append({
                "id": sid,
                "cosine_to_own_original": round(cos_to_own, 4),
                "nearest_original": nn_id,
                "nearest_cosine": round(nn_score, 4),
                "self_match": (nn_id == sid),
            })
        n = len(rows)
        n_self = sum(1 for r in rows if r["self_match"])
        cos_values = [r["cosine_to_own_original"] for r in rows]
        summary = {
            "n_ok": n, "n_fail": 0,
            "recall_at_1_self_match": round(n_self / n, 4),
            "n_nn_switched": n - n_self,
            "mean_cosine_to_own_original": round(sum(cos_values) / len(cos_values), 4),
            "min_cosine_to_own_original": round(min(cos_values), 4),
            "max_cosine_to_own_original": round(max(cos_values), 4),
            "cost_usd": 0.0,
        }
        print(f"  ИТОГ {model_name}/{vname}: {json.dumps(summary, ensure_ascii=False)}")
        variants_out[vname] = {"summary": summary, "details": rows, "fail_log": []}

    avg_infer_s = sum(infer_times) / len(infer_times)
    return {
        "n_originals_ok": len(originals),
        "originals_fail": [],
        "originals_cost_usd": 0.0,
        "avg_local_forward_pass_s": round(avg_infer_s, 4),
        "checkpoint_load_s": round(load_s, 2),
        "variants": variants_out,
    }


def run_voyage(ids, paths):
    print(f"--- {VOYAGE_MODEL}: оригиналы из кэша (не пересчитываем) ---")
    originals, orig_fail, orig_cost = load_or_fetch_originals(VOYAGE_MODEL, ids, paths)
    n_orig_ok = sum(1 for v in originals.values() if v is not None)
    print(f"  оригиналов: {n_orig_ok}/{len(ids)} ok (из кэша, cost ${orig_cost:.6f} — уже оплачено замером №4)")

    variants_out = {}
    total_new_cost = 0.0
    for vname, vfunc in VARIANTS.items():
        print(f"--- {VOYAGE_MODEL} / {vname} ---")
        rows = []
        fail_log = []
        for sid in ids:
            data_url = vfunc(paths[sid])
            vec, cost, err = embed_mm(VOYAGE_MODEL, data_url)
            if cost:
                total_new_cost += cost
            if vec is None:
                fail_log.append({"id": sid, "error": err})
                print(f"    {sid}: FAIL ({err[:80] if err else '?'})")
                time.sleep(0.4)
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
            time.sleep(0.4)
        n = len(rows)
        n_self = sum(1 for r in rows if r["self_match"])
        cos_values = [r["cosine_to_own_original"] for r in rows if r["cosine_to_own_original"] is not None]
        summary = {
            "n_ok": n, "n_fail": len(fail_log),
            "recall_at_1_self_match": round(n_self / n, 4) if n else None,
            "n_nn_switched": n - n_self,
            "mean_cosine_to_own_original": round(sum(cos_values) / len(cos_values), 4) if cos_values else None,
            "min_cosine_to_own_original": round(min(cos_values), 4) if cos_values else None,
            "max_cosine_to_own_original": round(max(cos_values), 4) if cos_values else None,
            "cost_usd": round(total_new_cost, 6),
        }
        print(f"  ИТОГ {VOYAGE_MODEL}/{vname}: {json.dumps(summary, ensure_ascii=False)}")
        variants_out[vname] = {"summary": summary, "details": rows, "fail_log": fail_log}
        # checkpoint
        json.dump({"n_originals_ok": n_orig_ok, "originals_fail": orig_fail,
                   "originals_cost_usd": round(orig_cost, 6), "new_distortion_cost_usd": round(total_new_cost, 6),
                   "variants": variants_out},
                  open("raw/jitter_results_local.json.voyage_checkpoint", "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)

    return {
        "n_originals_ok": n_orig_ok,
        "originals_fail": orig_fail,
        "originals_cost_usd": round(orig_cost, 6),
        "new_distortion_cost_usd": round(total_new_cost, 6),
        "variants": variants_out,
    }


def main():
    from common_k2 import variant_original

    samples, ids, paths = load_corpus()
    t0 = time.time()

    out = {"models": ["openai/clip-vit-base-patch32 (локально)",
                       "google/siglip-base-patch16-224 (локально)",
                       VOYAGE_MODEL + " (платно, кросс-проверка)"],
           "variants": list(VARIANTS.keys()), "per_model": {}}

    print("\n=== CLIP ===")
    out["per_model"]["openai/clip-vit-base-patch32"] = run_local_model(
        "CLIP", load_clip, ids, paths, variant_original)
    json.dump(out, open("raw/jitter_results_local.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print("\n=== SigLIP ===")
    out["per_model"]["google/siglip-base-patch16-224"] = run_local_model(
        "SigLIP", load_siglip, ids, paths, variant_original)
    json.dump(out, open("raw/jitter_results_local.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(f"\n=== {VOYAGE_MODEL} (платная кросс-проверка) ===")
    out["per_model"][VOYAGE_MODEL] = run_voyage(ids, paths)
    out["elapsed_s"] = round(time.time() - t0, 1)
    json.dump(out, open("raw/jitter_results_local.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"\n=== ЗАМЕР №3 (ЛОКАЛЬНЫЕ МОДЕЛИ + 1 ПЛАТНАЯ) ЗАВЕРШЁН за {out['elapsed_s']}s ===")


if __name__ == "__main__":
    main()
