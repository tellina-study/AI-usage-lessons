#!/usr/bin/env python3
"""Кейс 4 (issue #311) — ДОПОЛНИТЕЛЬНАЯ (необязательная) вторая точка сравнения к
case4_local_clip_retrieval_30.py: та же методика, та же модель окружения (локально,
CPU, без OpenRouter), но `google/siglip-base-patch16-224` вместо CLIP ViT-B/32 — SigLIP
считается более современным на задачах similarity (sigmoid loss вместо softmax).

Структура, функции аугментации (to_data_url/soft_dup/hard_dup, детерминированные) и
ground truth для части C — переиспользованы БЕЗ ИЗМЕНЕНИЙ из case4_full_retrieval_30.py /
../raw/case4_mm_full_retrieval.json, ровно как в case4_local_clip_retrieval_30.py — см.
комментарии там для методологии. Этот файл — не повтор содержания, а запуск той же
логики другой моделью; приоритетный, обязательный прогон — CLIP (см. тот скрипт).
"""
import base64
import io
import json
import time

from PIL import Image

from case4_full_retrieval_30 import cosine, to_data_url, soft_dup, hard_dup

SIGLIP_MODEL_NAME = "google/siglip-base-patch16-224"
REFERENCE_JSON = "../raw/case4_mm_full_retrieval.json"

samples = json.load(open("../corpus/cord_sample_meta.json"))
ids = [s["id"] for s in samples]
paths = {s["id"]: f"../{s['file']}" for s in samples}


def data_url_to_pil(data_url):
    raw = base64.b64decode(data_url.split(",", 1)[1])
    return Image.open(io.BytesIO(raw)).convert("RGB")


def load_siglip():
    import torch
    from transformers import SiglipModel, SiglipImageProcessor

    t0 = time.time()
    model = SiglipModel.from_pretrained(SIGLIP_MODEL_NAME)
    model.eval()
    processor = SiglipImageProcessor.from_pretrained(SIGLIP_MODEL_NAME)
    load_s = time.time() - t0
    print(f"=== SigLIP ({SIGLIP_MODEL_NAME}) loaded in {load_s:.1f}s ===")
    return model, processor, load_s, torch


def embed_siglip(model, processor, torch, pil_im):
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


def nearest_among(query_sid, pool, others):
    best, best_score = None, -2.0
    qv = pool[query_sid]
    for o in others:
        ov = pool.get(o)
        if ov is None:
            continue
        s = cosine(qv, ov)
        if s > best_score:
            best_score, best = s, o
    return best, best_score


def run():
    t_wall0 = time.time()
    model, processor, load_s, torch = load_siglip()

    mm_orig, mm_soft, mm_hard = {}, {}, {}
    infer_times = []

    for stage, pool, build in (
        ("originals", mm_orig, lambda p: to_data_url(p)),
        ("soft-dup", mm_soft, lambda p: soft_dup(p)),
        ("hard-dup", mm_hard, lambda p: hard_dup(p)),
    ):
        print(f"=== embedding 30 {stage} (SigLIP, local) ===")
        for sid in ids:
            p = paths[sid]
            pil = data_url_to_pil(build(p))
            vec, dt = embed_siglip(model, processor, torch, pil)
            pool[sid] = vec
            infer_times.append(dt)

    avg_infer_s = sum(infer_times) / len(infer_times)
    print(f"=== avg SigLIP forward-pass time per image: {avg_infer_s:.4f}s (n={len(infer_times)}) ===")

    retrieval_rows = []
    for sid in ids:
        row = {"id": sid}
        nn, score = nearest(mm_soft[sid], mm_orig)
        row["siglip_soft_nearest"] = nn
        row["siglip_soft_correct"] = (nn == sid)
        row["siglip_soft_cosine"] = round(score, 4)
        nn, score = nearest(mm_hard[sid], mm_orig)
        row["siglip_hard_nearest"] = nn
        row["siglip_hard_correct"] = (nn == sid)
        row["siglip_hard_cosine"] = round(score, 4)
        retrieval_rows.append(row)

    n = len(retrieval_rows)
    recall_summary = {
        "n_scans": n,
        "siglip_model": SIGLIP_MODEL_NAME,
        "siglip_soft_dup_recall_at_1": sum(r["siglip_soft_correct"] for r in retrieval_rows) / n,
        "siglip_hard_dup_recall_at_1": sum(r["siglip_hard_correct"] for r in retrieval_rows) / n,
    }
    print("\n=== PART A SUMMARY (SigLIP) ===")
    print(json.dumps(recall_summary, ensure_ascii=False, indent=2))

    ref = json.load(open(REFERENCE_JSON))
    gold_rows = ref["part_C_semantic_similarity_agreement"]["details"]
    gold_by_id = {r["id"]: r["text_gold_nearest"] for r in gold_rows}

    sem_rows = []
    for sid in ids:
        gold_nn = gold_by_id.get(sid)
        others = [x for x in ids if x != sid]
        nn, score = nearest_among(sid, mm_orig, others)
        sem_rows.append({
            "id": sid,
            "text_gold_nearest": gold_nn,
            "siglip_nearest": nn,
            "siglip_cosine": round(score, 4),
            "siglip_agrees_with_text": (nn == gold_nn) if gold_nn else None,
        })

    agree_rows = [r for r in sem_rows if r["siglip_agrees_with_text"] is not None]
    semantic_summary = {
        "method": "Ground truth = text_gold_nearest взятый ПРЯМО из " + REFERENCE_JSON
                  + " (как в case4_local_clip_retrieval_30.py), не пересчитан.",
        "n_scans": len(agree_rows),
        "chance_level_recall_at_1": round(1 / (len(ids) - 1), 4),
        "siglip_model": SIGLIP_MODEL_NAME,
        "siglip_semantic_agreement_recall_at_1": (
            sum(r["siglip_agrees_with_text"] for r in agree_rows) / len(agree_rows) if agree_rows else None
        ),
    }
    print("\n=== PART C SUMMARY (SigLIP) ===")
    print(json.dumps(semantic_summary, ensure_ascii=False, indent=2))

    wall_s = time.time() - t_wall0
    out = {
        "purpose": "Дополнительная (не обязательная) вторая локальная точка сравнения к CLIP "
                   "ViT-B/32 — SigLIP считается более современным на задачах similarity.",
        "model": SIGLIP_MODEL_NAME,
        "environment": {"device": "CPU", "clip_checkpoint_load_s": round(load_s, 2)},
        "timing": {"avg_forward_pass_s_per_image": round(avg_infer_s, 4),
                   "n_images_embedded": len(infer_times),
                   "total_wall_s_this_script": round(wall_s, 1)},
        "part_A_near_dup_retrieval": {"summary": recall_summary, "details": retrieval_rows},
        "part_C_semantic_similarity_agreement": {"summary": semantic_summary, "details": sem_rows},
    }
    json.dump(out, open("case4_local_siglip_results_raw.json", "w", encoding="utf-8"),
               ensure_ascii=False, indent=2)
    print("\n=== FINAL (SigLIP) ===")
    print(json.dumps({"recall_summary": recall_summary, "semantic_summary": semantic_summary,
                       "timing": out["timing"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
