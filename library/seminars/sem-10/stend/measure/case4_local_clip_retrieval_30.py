#!/usr/bin/env python3
"""Кейс 4 (issue #311) — тот же замер, что case4_full_retrieval_30.py, но мультимодальный
эмбеддинг считается ЛОКАЛЬНО (без HTTP-вызова к OpenRouter/n8n) через CLIP
(`openai/clip-vit-base-patch32`, HF `transformers`, CPU-инференс) — ответ на вопрос
владельца курса: «а почему не попробовали локальную модель (CLIP/SigLIP/DINOv2 —
индустриальный стандарт для этой задачи)?».

Переиспользует БЕЗ ИЗМЕНЕНИЙ из case4_full_retrieval_30.py:
  - to_data_url / soft_dup / hard_dup — те же функции аугментации (детерминированные,
    без random — resize*0.97 и поворот 12° на фиксированных числах, так что результат
    бит-в-бит идентичен тому, что было отправлено в nemotron-3.5-embed-1b:free);
  - cosine — та же функция косинусного сходства на python-списках.

Часть A (near-dup recall@1): для всех 30 сканов — soft-dup и hard-dup, эмбеддинг CLIP,
поиск ближайшего ОРИГИНАЛА среди 30 по cosine, recall@1 отдельно для soft/hard.

Часть C (семантическое совпадение vs текст): ground truth "семантически ближайший ДРУГОЙ
чек" берётся НЕ пересчётом text-embedding-3-small (это уже сделано и сохранено), а ПРЯМО
из ../raw/case4_mm_full_retrieval.json::part_C_semantic_similarity_agreement.details[].
text_gold_nearest — тот же золотой сосед, что уже использован для nemotron и phash,
никакого нового вызова OpenRouter не требуется. recall@1(CLIP) = доля чеков, где CLIP
(на ОРИГИНАЛЬНЫХ, неаугментированных сканах) выбирает среди остальных 29 того же соседа.

Честно: если CLIP окажется хуже nemotron/phash — это нормальный результат, цифры не
подгоняются.
"""
import base64
import io
import json
import time

from PIL import Image

from case4_full_retrieval_30 import cosine, to_data_url, soft_dup, hard_dup

CLIP_MODEL_NAME = "openai/clip-vit-base-patch32"
REFERENCE_JSON = "../raw/case4_mm_full_retrieval.json"

samples = json.load(open("../corpus/cord_sample_meta.json"))
ids = [s["id"] for s in samples]
paths = {s["id"]: f"../{s['file']}" for s in samples}


def data_url_to_pil(data_url):
    raw = base64.b64decode(data_url.split(",", 1)[1])
    return Image.open(io.BytesIO(raw)).convert("RGB")


def load_clip():
    import torch
    from transformers import CLIPModel, CLIPProcessor

    t0 = time.time()
    model = CLIPModel.from_pretrained(CLIP_MODEL_NAME)
    model.eval()
    processor = CLIPProcessor.from_pretrained(CLIP_MODEL_NAME)
    load_s = time.time() - t0
    print(f"=== CLIP ({CLIP_MODEL_NAME}) loaded in {load_s:.1f}s ===")
    return model, processor, load_s, torch


def embed_clip(model, processor, torch, pil_im):
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
    model, processor, load_s, torch = load_clip()

    mm_orig, mm_soft, mm_hard = {}, {}, {}
    infer_times = []

    print("=== embedding 30 originals (CLIP, local) ===")
    for sid in ids:
        p = paths[sid]
        pil = data_url_to_pil(to_data_url(p))
        vec, dt = embed_clip(model, processor, torch, pil)
        mm_orig[sid] = vec
        infer_times.append(dt)
        print(f"  orig {sid}: ok ({dt:.3f}s)")

    print("=== embedding 30 soft-dup (CLIP, local) ===")
    for sid in ids:
        p = paths[sid]
        pil = data_url_to_pil(soft_dup(p))
        vec, dt = embed_clip(model, processor, torch, pil)
        mm_soft[sid] = vec
        infer_times.append(dt)
        print(f"  soft {sid}: ok ({dt:.3f}s)")

    print("=== embedding 30 hard-dup (CLIP, local) ===")
    for sid in ids:
        p = paths[sid]
        pil = data_url_to_pil(hard_dup(p))
        vec, dt = embed_clip(model, processor, torch, pil)
        mm_hard[sid] = vec
        infer_times.append(dt)
        print(f"  hard {sid}: ok ({dt:.3f}s)")

    avg_infer_s = sum(infer_times) / len(infer_times)
    print(f"=== avg CLIP forward-pass time per image: {avg_infer_s:.4f}s (n={len(infer_times)}) ===")

    # ---------- Part A: near-dup retrieval ----------
    retrieval_rows = []
    for sid in ids:
        row = {"id": sid}
        nn, score = nearest(mm_soft[sid], mm_orig)
        row["clip_soft_nearest"] = nn
        row["clip_soft_correct"] = (nn == sid)
        row["clip_soft_cosine"] = round(score, 4)
        nn, score = nearest(mm_hard[sid], mm_orig)
        row["clip_hard_nearest"] = nn
        row["clip_hard_correct"] = (nn == sid)
        row["clip_hard_cosine"] = round(score, 4)
        retrieval_rows.append(row)

    n = len(retrieval_rows)
    recall_summary = {
        "n_scans": n,
        "clip_model": CLIP_MODEL_NAME,
        "clip_soft_dup_recall_at_1": sum(r["clip_soft_correct"] for r in retrieval_rows) / n,
        "clip_hard_dup_recall_at_1": sum(r["clip_hard_correct"] for r in retrieval_rows) / n,
    }
    print("\n=== PART A SUMMARY ===")
    print(json.dumps(recall_summary, ensure_ascii=False, indent=2))

    # ---------- Part C: semantic agreement vs text gold neighbor (reused, not recomputed) ----------
    ref = json.load(open(REFERENCE_JSON))
    gold_rows = ref["part_C_semantic_similarity_agreement"]["details"]
    gold_by_id = {r["id"]: r["text_gold_nearest"] for r in gold_rows}
    missing_gold = [sid for sid in ids if sid not in gold_by_id or gold_by_id[sid] is None]
    if missing_gold:
        print(f"  WARNING: no text gold neighbor for {missing_gold} (skipped in agreement calc)")

    sem_rows = []
    for sid in ids:
        gold_nn = gold_by_id.get(sid)
        others = [x for x in ids if x != sid]
        clip_nn, clip_score = nearest_among(sid, mm_orig, others)
        sem_rows.append({
            "id": sid,
            "text_gold_nearest": gold_nn,
            "clip_nearest": clip_nn,
            "clip_cosine": round(clip_score, 4),
            "clip_agrees_with_text": (clip_nn == gold_nn) if gold_nn else None,
        })

    agree_rows = [r for r in sem_rows if r["clip_agrees_with_text"] is not None]
    semantic_summary = {
        "method": "Ground truth 'семантически ближайший ДРУГОЙ чек' = text_gold_nearest, "
                  "взятый ПРЯМО из уже готового " + REFERENCE_JSON + " (top-1 среди остальных "
                  "29 по text-embedding(OCR) cosine, тот же золотой сосед, что уже использован "
                  "для nemotron-3.5-embed-1b:free и phash) — НЕ пересчитан заново. "
                  "recall@1(CLIP) = доля чеков, где CLIP-эмбеддинг (на ОРИГИНАЛЬНЫХ, "
                  "неаугментированных сканах) выбирает ТОГО ЖЕ ближайшего соседа, что текст.",
        "n_scans": len(agree_rows),
        "chance_level_recall_at_1": round(1 / (len(ids) - 1), 4),
        "clip_model": CLIP_MODEL_NAME,
        "clip_semantic_agreement_recall_at_1": (
            sum(r["clip_agrees_with_text"] for r in agree_rows) / len(agree_rows) if agree_rows else None
        ),
    }
    print("\n=== PART C SUMMARY ===")
    print(json.dumps(semantic_summary, ensure_ascii=False, indent=2))

    wall_s = time.time() - t_wall0

    # ---------- for-context comparison with the already-known OpenRouter timing ----------
    openrouter_total_wall_s = ref.get("total_wall_s")
    openrouter_n_mm_calls = 90  # 30 orig + 30 soft + 30 hard, same structure as this script
    openrouter_avg_s_per_call = (
        round(openrouter_total_wall_s / openrouter_n_mm_calls, 2) if openrouter_total_wall_s else None
    )

    out = {
        "purpose": "issue #311 — owner question: почему не попробовали ЛОКАЛЬНУЮ модель "
                   "эмбеддинга картинок (CLIP/SigLIP/DINOv2 — индустриальный стандарт для "
                   "этой задачи, без API/rate-limit/цены за вызов)? Тот же замер, что уже "
                   "прогнан для nvidia/nemotron-3.5-embed-1b:free (case4_full_retrieval_30.py), "
                   "теперь локальной моделью CLIP ViT-B/32, для честного сравнения числом.",
        "model": CLIP_MODEL_NAME,
        "environment": {
            "install_method": "python3 -m virtualenv .venv-clip (система externally-managed, "
                              "без root/venv-apt — virtualenv поставлен через "
                              "pip install --user --break-system-packages virtualenv)",
            "packages": "torch (CPU-only wheel, download.pytorch.org/whl/cpu) + transformers + pillow + numpy",
            "device": "CPU (нет GPU в этом окружении — не требуется для ViT-B/32)",
            "clip_checkpoint_load_s": round(load_s, 2),
        },
        "timing": {
            "avg_clip_forward_pass_s_per_image": round(avg_infer_s, 4),
            "n_images_embedded": len(infer_times),
            "total_wall_s_this_script": round(wall_s, 1),
            "for_context_openrouter_nemotron_total_wall_s": openrouter_total_wall_s,
            "for_context_openrouter_avg_s_per_mm_call": openrouter_avg_s_per_call,
            "note": "OpenRouter-время включает сетевой round-trip через n8n-вебхук + поллинг "
                    "execution (harness_call.py опрашивает каждую секунду) + явный sleep(0.3) "
                    "между вызовами — не чистое время инференса модели на стороне провайдера; "
                    "сравнение honest-but-approximate, не apples-to-apples замер серверного GPU-времени.",
        },
        "part_A_near_dup_retrieval": {
            "method": "Те же soft_dup/hard_dup из case4_full_retrieval_30.py (детерминированные, "
                      "без random) — для каждой пары (оригинал, дубль) CLIP-эмбеддинг дубля, "
                      "поиск ближайшего ОРИГИНАЛА среди всех 30 по cosine; recall@1 = доля, где "
                      "ближайший — тот самый оригинал.",
            "summary": recall_summary,
            "details": retrieval_rows,
        },
        "part_C_semantic_similarity_agreement": {
            "summary": semantic_summary,
            "details": sem_rows,
        },
        "comparison_table": {
            "columns": ["nvidia/nemotron-3.5-embed-1b:free (API)", "CLIP ViT-B/32 (локально)",
                        "perceptual hash", "текст (эталон)"],
            "recall_at_1_soft_dup": [1.0, round(recall_summary["clip_soft_dup_recall_at_1"], 4),
                                      0.9667, None],
            "recall_at_1_hard_dup_rotation": [0.9667, round(recall_summary["clip_hard_dup_recall_at_1"], 4),
                                                0.2333, None],
            "recall_at_1_semantic_agreement": [0.2667,
                                                 round(semantic_summary["clip_semantic_agreement_recall_at_1"], 4)
                                                 if semantic_summary["clip_semantic_agreement_recall_at_1"] is not None else None,
                                                 0.0333, 0.9667],
            "chance_level_semantic": 0.0345,
        },
    }
    json.dump(out, open("case4_local_clip_results_raw.json", "w", encoding="utf-8"),
               ensure_ascii=False, indent=2)
    print("\n=== FINAL ===")
    print(json.dumps({"recall_summary": recall_summary, "semantic_summary": semantic_summary,
                       "timing": out["timing"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
