#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Семинар 12, Кейс 3 — клетка «найди, где есть вот это» (поиск мелкой детали внутри
картинки): вектор на весь кадр против векторов на плитках.

Данные: 30 реальных сканов CORD (`sem-10/stend/corpus/cord_sample/receipt_NN.jpg`) +
ground truth bbox всех строк чека (`raw/cord_ground_truth_bboxes.json`, подготовлен
оркестратором). Модель: `openai/clip-vit-base-patch32`, локально, CPU, тот же паттерн
вызова, что в `sem-10/stend/measure/case4_local_clip_retrieval_30.py`
(`CLIPModel.get_image_features` → в этой версии transformers возвращает
`BaseModelOutputWithPooling`, берём `.pooler_output[0]` — проверено живым вызовом
перед написанием этого скрипта, не предположение).

Алгоритм — см. README.md в этой же папке и промпт оркестратора (issue sem-12-k3).
Один проход, методика зафиксирована ДО просмотра чисел (сетка плиток 4x2, паддинг
20%, порог длины строки 2 символа) — результат не подгоняется под гипотезу.
"""
import json
import time
from pathlib import Path

from PIL import Image

HERE = Path(__file__).parent.resolve()
CORPUS_DIR = HERE.parent.parent.parent / "sem-10" / "stend" / "corpus" / "cord_sample"
GT_PATH = HERE / "raw" / "cord_ground_truth_bboxes.json"
OUT_PATH = HERE / "raw" / "case3_tiles_vs_whole_results.json"

CLIP_MODEL_NAME = "openai/clip-vit-base-patch32"
TILE_ROWS = 4
TILE_COLS = 2
PAD_FRAC = 0.20
MIN_LINE_TEXT_LEN = 2


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


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


def embed_clip(model, processor, torch_mod, pil_im):
    t0 = time.time()
    inputs = processor(images=pil_im, return_tensors="pt")
    with torch_mod.no_grad():
        out = model.get_image_features(**inputs)
    vec = out.pooler_output[0].tolist()
    return vec, time.time() - t0


# ---------- Step 1: build easy/hard "small-detail" queries per receipt ----------

def line_bbox(line):
    xs, ys = [], []
    for w in line["words"]:
        q = w["quad"]
        xs.extend([q["x1"], q["x2"], q["x3"], q["x4"]])
        ys.extend([q["y1"], q["y2"], q["y3"], q["y4"]])
    return min(xs), min(ys), max(xs), max(ys)


def line_text(line):
    return " ".join(w["text"] for w in line["words"])


def build_queries(gt_item):
    img_w = gt_item["image_size"]["width"]
    img_h = gt_item["image_size"]["height"]
    candidates = []
    for line in gt_item["valid_line"]:
        txt = line_text(line)
        if len(txt) < MIN_LINE_TEXT_LEN:
            continue
        xmin, ymin, xmax, ymax = line_bbox(line)
        area_norm = ((xmax - xmin) * (ymax - ymin)) / (img_w * img_h)
        candidates.append({
            "line_text": txt,
            "bbox": [xmin, ymin, xmax, ymax],
            "area_norm": area_norm,
        })
    if not candidates:
        return None, None, 0
    candidates.sort(key=lambda c: c["area_norm"])
    hard = candidates[0]
    easy = candidates[-1]
    return easy, hard, len(candidates)


def pad_and_clamp(bbox, img_w, img_h, pad_frac):
    xmin, ymin, xmax, ymax = bbox
    bw, bh = xmax - xmin, ymax - ymin
    px, py = bw * pad_frac, bh * pad_frac
    xmin = max(0, xmin - px)
    ymin = max(0, ymin - py)
    xmax = min(img_w, xmax + px)
    ymax = min(img_h, ymax + py)
    return int(round(xmin)), int(round(ymin)), int(round(xmax)), int(round(ymax))


# ---------- Step 3: tile grid ----------

def make_tiles(img_w, img_h, rows=TILE_ROWS, cols=TILE_COLS):
    xs = [round(c * img_w / cols) for c in range(cols + 1)]
    ys = [round(r * img_h / rows) for r in range(rows + 1)]
    tiles = []
    for r in range(rows):
        for c in range(cols):
            box = (xs[c], ys[r], xs[c + 1], ys[r + 1])
            tiles.append((r, c, box))
    return tiles


def nearest(query_vec, pool_dict):
    best_id, best_score = None, -2.0
    for pid, v in pool_dict.items():
        s = cosine(query_vec, v)
        if s > best_score:
            best_score, best_id = s, pid
    return best_id, best_score


def run():
    t_wall0 = time.time()
    gt = json.load(open(GT_PATH, encoding="utf-8"))
    gt_by_id = {item["id"]: item for item in gt}
    ids = [item["id"] for item in gt]
    print(f"=== {len(ids)} receipts loaded from ground truth ===")

    model, processor, load_s, torch_mod = load_clip()

    # ---- Step 1: build queries ----
    easy_queries, hard_queries, anomalies = [], [], []
    area_stats_easy, area_stats_hard = [], []
    for sid in ids:
        item = gt_by_id[sid]
        img_w, img_h = item["image_size"]["width"], item["image_size"]["height"]
        easy, hard, n_candidates = build_queries(item)
        if easy is None:
            anomalies.append({"id": sid, "issue": "no valid_line passed length filter — excluded entirely"})
            continue
        if n_candidates == 1:
            anomalies.append({"id": sid, "issue": "only 1 line passed length filter — easy == hard query"})
        easy_bbox_pad = pad_and_clamp(easy["bbox"], img_w, img_h, PAD_FRAC)
        hard_bbox_pad = pad_and_clamp(hard["bbox"], img_w, img_h, PAD_FRAC)
        easy_queries.append({
            "source_id": sid, "line_text": easy["line_text"], "bbox": easy["bbox"],
            "bbox_padded": list(easy_bbox_pad), "area_norm": easy["area_norm"],
            "n_candidate_lines": n_candidates,
        })
        hard_queries.append({
            "source_id": sid, "line_text": hard["line_text"], "bbox": hard["bbox"],
            "bbox_padded": list(hard_bbox_pad), "area_norm": hard["area_norm"],
            "n_candidate_lines": n_candidates,
        })
        area_stats_easy.append(easy["area_norm"])
        area_stats_hard.append(hard["area_norm"])

    print(f"=== built {len(easy_queries)} easy + {len(hard_queries)} hard queries "
          f"({len(anomalies)} anomalies logged) ===")

    # ---- Step 2: embed full frames ----
    print("=== embedding 30 full frames (CLIP, local, CLIPProcessor default resize) ===")
    full_vecs = {}
    full_infer_times = []
    full_images = {}
    for sid in ids:
        p = CORPUS_DIR / f"{sid}.jpg"
        pil = Image.open(p).convert("RGB")
        full_images[sid] = pil
        vec, dt = embed_clip(model, processor, torch_mod, pil)
        full_vecs[sid] = vec
        full_infer_times.append(dt)
    print(f"  done ({len(full_infer_times)} images, avg {sum(full_infer_times)/len(full_infer_times):.3f}s)")

    # ---- Step 3: embed tiles ----
    print(f"=== embedding tiles ({TILE_ROWS}x{TILE_COLS} grid, {len(ids)*TILE_ROWS*TILE_COLS} total) ===")
    tile_vecs = {}
    tile_parent = {}
    tile_infer_times = []
    for sid in ids:
        pil = full_images[sid]
        img_w, img_h = pil.size
        tiles = make_tiles(img_w, img_h)
        for r, c, box in tiles:
            tile_id = f"{sid}__tile_r{r}_c{c}"
            crop = pil.crop(box)
            vec, dt = embed_clip(model, processor, torch_mod, crop)
            tile_vecs[tile_id] = vec
            tile_parent[tile_id] = sid
            tile_infer_times.append(dt)
    print(f"  done ({len(tile_infer_times)} tiles, avg {sum(tile_infer_times)/len(tile_infer_times):.3f}s)")

    # ---- Step 2+3: embed query crops and run both methods ----
    def embed_queries(queries, label):
        crop_infer_times = []
        rows = []
        for q in queries:
            sid = q["source_id"]
            pil = full_images[sid]
            crop = pil.crop(tuple(q["bbox_padded"]))
            vec, dt = embed_clip(model, processor, torch_mod, crop)
            crop_infer_times.append(dt)

            whole_pred, whole_score = nearest(vec, full_vecs)
            tile_pred_id, tile_score = nearest(vec, tile_vecs)
            tile_pred_source = tile_parent[tile_pred_id]

            rows.append({
                "source_id": sid,
                "line_text": q["line_text"],
                "area_norm": round(q["area_norm"], 6),
                "n_candidate_lines": q["n_candidate_lines"],
                "whole_frame_predicted_source": whole_pred,
                "whole_frame_cosine": round(whole_score, 4),
                "whole_frame_correct": whole_pred == sid,
                "tiles_predicted_tile": tile_pred_id,
                "tiles_predicted_source": tile_pred_source,
                "tiles_cosine": round(tile_score, 4),
                "tiles_correct": tile_pred_source == sid,
            })
        print(f"  [{label}] {len(rows)} queries embedded, "
              f"avg {sum(crop_infer_times)/len(crop_infer_times):.3f}s/crop")
        return rows

    print("=== Part: easy queries (largest line per receipt) ===")
    easy_rows = embed_queries(easy_queries, "easy")
    print("=== Part: hard queries (smallest line per receipt) ===")
    hard_rows = embed_queries(hard_queries, "hard")

    n_easy = len(easy_rows)
    n_hard = len(hard_rows)
    summary = {
        "whole_frame_recall_at_1_easy": sum(r["whole_frame_correct"] for r in easy_rows) / n_easy,
        "whole_frame_recall_at_1_hard": sum(r["whole_frame_correct"] for r in hard_rows) / n_hard,
        "tiles_recall_at_1_easy": sum(r["tiles_correct"] for r in easy_rows) / n_easy,
        "tiles_recall_at_1_hard": sum(r["tiles_correct"] for r in hard_rows) / n_hard,
    }
    print("\n=== SUMMARY (recall@1) ===")
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    wall_s = time.time() - t_wall0

    out = {
        "purpose": "Семинар 12, Кейс 3 — клетка «найди, где есть вот это»: вектор на весь "
                   "кадр против векторов на плитках, для поиска мелкой детали внутри скана чека.",
        "date": "2026-11-21",
        "model": CLIP_MODEL_NAME,
        "environment": {
            "device": "CPU",
            "clip_checkpoint_load_s": round(load_s, 2),
            "image_resolution": "CLIPProcessor default resize (224x224), без ручного ресайза",
        },
        "config": {
            "tile_grid_rows": TILE_ROWS,
            "tile_grid_cols": TILE_COLS,
            "tile_grid_note": "4x2 выбрано по форме картинок корпуса (большинство сканов "
                               "портретные, h/w в районе 1.3-1.8), зафиксировано ДО просмотра "
                               "результатов, не подбиралось по recall.",
            "query_crop_padding_frac": PAD_FRAC,
            "min_line_text_len_filter": MIN_LINE_TEXT_LEN,
        },
        "query_construction": {
            "method": "Для каждого чека — объединяющий bbox по словам каждой строки valid_line, "
                      "area_norm = bbox_area / (image_w * image_h). Лёгкий запрос = строка с "
                      "максимальным area_norm (деталь набрана крупнее остальных). Трудный "
                      "запрос = строка с минимальным area_norm среди прошедших фильтр длины "
                      "(мелкая деталь рядом с другими такими же, не единственная мелкая на пустом фоне).",
            "n_receipts_total": len(ids),
            "n_receipts_with_queries": len(easy_queries),
            "n_anomalies": len(anomalies),
            "anomalies": anomalies,
            "mean_area_norm_easy": round(sum(area_stats_easy) / len(area_stats_easy), 4) if area_stats_easy else None,
            "mean_area_norm_hard": round(sum(area_stats_hard) / len(area_stats_hard), 4) if area_stats_hard else None,
        },
        "timing": {
            "n_full_frame_embeddings": len(full_infer_times),
            "n_tile_embeddings": len(tile_infer_times),
            "n_query_crop_embeddings": n_easy + n_hard,
            "total_embedding_passes": len(full_infer_times) + len(tile_infer_times) + n_easy + n_hard,
            "avg_s_per_full_frame": round(sum(full_infer_times) / len(full_infer_times), 4),
            "avg_s_per_tile": round(sum(tile_infer_times) / len(tile_infer_times), 4),
            "total_wall_s": round(wall_s, 1),
            "note": "Все эмбеддинги считаются локально на CPU, без сетевых вызовов к внешним API.",
        },
        "summary_recall_at_1": summary,
        "details_easy": easy_rows,
        "details_hard": hard_rows,
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    json.dump(out, open(OUT_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"\n=== saved to {OUT_PATH} ===")
    print(json.dumps({"summary_recall_at_1": summary, "timing": out["timing"],
                       "n_anomalies": len(anomalies)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
