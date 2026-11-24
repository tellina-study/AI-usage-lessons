#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Семинар 12, Кейс D — ветка 3: поиск по вектору картинки, локально.

Модель `google/siglip-base-patch16-224`, `transformers` 5.22.2 — `.pooler_output`,
не тензор (`[#351-3]`). Вектор кадра целиком, один раз на снимок. Запросы —
EN (основной прогон, текстовая башня обучена на английских подписях) и
RU (подзамер — цена перевода, числа идут на кадр D04/D06).
"""
import json
from pathlib import Path

import torch
from PIL import Image
from transformers import AutoProcessor, AutoModel

from corpus_b101 import corpus_ids, find_image_path

HERE = Path(__file__).resolve().parent
MODEL_ID = "google/siglip-base-patch16-224"


def load_model():
    model = AutoModel.from_pretrained(MODEL_ID)
    processor = AutoProcessor.from_pretrained(MODEL_ID)
    model.eval()
    return model, processor


def embed_images(model, processor, ids):
    paths = [find_image_path(i) for i in ids]
    pils = [Image.open(p).convert("RGB") for p in paths]
    with torch.no_grad():
        batch = processor(images=pils, return_tensors="pt")
        out = model.get_image_features(**batch)
        vecs = out if isinstance(out, torch.Tensor) else out.pooler_output
        vecs = vecs / vecs.norm(dim=-1, keepdim=True)
    return vecs


def embed_texts(model, processor, texts):
    with torch.no_grad():
        batch = processor(text=texts, padding="max_length", truncation=True, return_tensors="pt")
        out = model.get_text_features(**batch)
        vecs = out if isinstance(out, torch.Tensor) else out.pooler_output
        vecs = vecs / vecs.norm(dim=-1, keepdim=True)
    return vecs


def rank_from_sims(sims_row, ids):
    pairs = sorted(zip(ids, sims_row.tolist()), key=lambda x: -x[1])
    return pairs


def run():
    ids = corpus_ids()
    queries = json.loads((HERE / "zaprosy_101.json").read_text(encoding="utf-8"))["queries"]

    print(f"=== {MODEL_ID}, {len(ids)} картинок, {len(queries)} запросов (EN + RU) ===")
    model, processor = load_model()
    img_vecs = embed_images(model, processor, ids)
    print("картинки векторизованы:", img_vecs.shape)

    en_vecs = embed_texts(model, processor, [q["en"] for q in queries])
    ru_vecs = embed_texts(model, processor, [q["ru"] for q in queries])
    print("тексты векторизованы (EN, RU):", en_vecs.shape, ru_vecs.shape)

    sims_en = en_vecs @ img_vecs.T
    sims_ru = ru_vecs @ img_vecs.T

    def score(sims):
        rows = []
        for q, sim_row in zip(queries, sims):
            pairs = rank_from_sims(sim_row, ids)
            top_ids = [p[0] for p in pairs[:3]]
            rows.append({
                "num": q["num"], "class": q["class"], "answer": q["answer"],
                "top3": [(pid, round(sc, 4)) for pid, sc in pairs[:3]],
                "correct_at_1": top_ids[0] == q["answer"],
                "correct_at_3": q["answer"] in top_ids,
            })
        return rows

    rows_en = score(sims_en)
    rows_ru = score(sims_ru)

    def by_class(rows):
        out = {}
        for cls in (1, 2, 3):
            cls_rows = [r for r in rows if r["class"] == cls]
            out[cls] = {
                "n": len(cls_rows),
                "recall@1": sum(r["correct_at_1"] for r in cls_rows) / len(cls_rows),
                "recall@3": sum(r["correct_at_3"] for r in cls_rows) / len(cls_rows),
            }
        return out

    out = {
        "branch": "3_siglip_local",
        "model": MODEL_ID,
        "device": "cpu",
        "vector_source": ".pooler_output ([#351-3])",
        "n_images": len(ids),
        "n_queries": len(queries),
        "EN": {
            "by_class": by_class(rows_en),
            "overall_recall@1": sum(r["correct_at_1"] for r in rows_en) / len(rows_en),
            "overall_recall@3": sum(r["correct_at_3"] for r in rows_en) / len(rows_en),
            "details": rows_en,
        },
        "RU": {
            "by_class": by_class(rows_ru),
            "overall_recall@1": sum(r["correct_at_1"] for r in rows_ru) / len(rows_ru),
            "overall_recall@3": sum(r["correct_at_3"] for r in rows_ru) / len(rows_ru),
            "details": rows_ru,
        },
    }
    (HERE / "raw" / "branch3_results_101.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "EN_by_class": out["EN"]["by_class"], "EN_overall": out["EN"]["overall_recall@1"],
        "RU_by_class": out["RU"]["by_class"], "RU_overall": out["RU"]["overall_recall@1"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
