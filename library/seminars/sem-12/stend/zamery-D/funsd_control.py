#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Семинар 12, Кейс D — D12: контроль на документах A (FUNSD). Тот же опыт,
другой материал: 50 отсканированных форм, корпус текста — полный OCR
(`words`/`text` разметки FUNSD, уже «распознанный»), 14 запросов (7
буквальных + 7 смысловых), те же 4 ветки. Нужен webhook (branch 2) — перед
запуском: `source ~/.n8n-lab.env`.
"""
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
SEM10_MEASURE = HERE.parent.parent.parent / "sem-10" / "stend" / "measure"
sys.path.insert(0, str(SEM10_MEASURE))

import torch
from PIL import Image
from transformers import AutoModel, AutoProcessor

from funsd_corpus import load_fulltext, doc_ids, image_path
from branch1_lexical import lemmatize, build_index, rank
from branch4_hybrid import rrf_merge

TEXT_MODEL = "openai/text-embedding-3-small"
SIGLIP_MODEL = "google/siglip-base-patch16-224"


def branch1(texts, ids, queries):
    doc_lemma_sets, df = build_index(texts)
    out = {}
    for q in queries:
        scored, _ = rank(q["text"], doc_lemma_sets, df, len(ids))
        out[q["num"]] = [s[0] for s in scored[:3]]
    return out


def branch2(texts, ids, queries):
    from harness2 import embed_batch, cosine
    corpus_vecs_list, cmeta = embed_batch([texts[i] for i in ids], model=TEXT_MODEL)
    corpus_vecs = dict(zip(ids, corpus_vecs_list))
    query_vecs_list, qmeta = embed_batch([q["text"] for q in queries], model=TEXT_MODEL)
    out = {}
    for q, qv in zip(queries, query_vecs_list):
        scored = sorted(((cid, cosine(qv, cv)) for cid, cv in corpus_vecs.items()), key=lambda x: -x[1])
        out[q["num"]] = [c for c, _ in scored[:3]]
    return out, cmeta, qmeta


def branch3(ids, queries):
    model = AutoModel.from_pretrained(SIGLIP_MODEL)
    processor = AutoProcessor.from_pretrained(SIGLIP_MODEL)
    model.eval()
    pils = [Image.open(image_path(i)).convert("RGB") for i in ids]
    with torch.no_grad():
        img_vecs = model.get_image_features(**processor(images=pils, return_tensors="pt"))
        img_vecs = img_vecs if isinstance(img_vecs, torch.Tensor) else img_vecs.pooler_output
        img_vecs = img_vecs / img_vecs.norm(dim=-1, keepdim=True)
        txt_vecs = model.get_text_features(**processor(text=[q["text"] for q in queries], padding="max_length", return_tensors="pt"))
        txt_vecs = txt_vecs if isinstance(txt_vecs, torch.Tensor) else txt_vecs.pooler_output
        txt_vecs = txt_vecs / txt_vecs.norm(dim=-1, keepdim=True)
    sims = txt_vecs @ img_vecs.T
    out = {}
    for q, row in zip(queries, sims):
        pairs = sorted(zip(ids, row.tolist()), key=lambda x: -x[1])
        out[q["num"]] = [p[0] for p in pairs[:3]]
    return out


def score(ranks, queries):
    rows = []
    for q in queries:
        top = ranks.get(q["num"], [])
        rows.append({
            "num": q["num"], "type": q["type"], "answer": q["answer"], "top3": top,
            "correct_at_1": bool(top) and top[0] == q["answer"],
            "correct_at_3": q["answer"] in top,
        })
    by_type = {}
    for t in ("буквальная", "смысловая"):
        trows = [r for r in rows if r["type"] == t]
        by_type[t] = {
            "n": len(trows),
            "recall@1": sum(r["correct_at_1"] for r in trows) / len(trows),
            "recall@3": sum(r["correct_at_3"] for r in trows) / len(trows),
        }
    return rows, by_type


def run():
    assert os.environ.get("N8N_API_KEY"), "N8N_API_KEY не задан — source ~/.n8n-lab.env"

    ids = doc_ids()
    texts = load_fulltext()
    queries = json.loads((HERE / "funsd_zaprosy.json").read_text(encoding="utf-8"))["queries"]
    print(f"=== FUNSD: {len(ids)} форм, {len(queries)} запросов (7 буквальных + 7 смысловых) ===")

    r1 = branch1(texts, ids, queries)
    print("ветка 1 (слова) готова")
    r2, cmeta, qmeta = branch2(texts, ids, queries)
    print(f"ветка 2 (смысл) готова, cost={round((cmeta['cost'] or 0) + (qmeta['cost'] or 0), 6)}")
    r3 = branch3(ids, queries)
    print("ветка 3 (SigLIP, EN) готова")
    r4_13 = rrf_merge([r1, r3])
    r4_123 = rrf_merge([r1, r2, r3])
    print("ветка 4 (гибрид) готова")

    rows1, by1 = score(r1, queries)
    rows2, by2 = score(r2, queries)
    rows3, by3 = score(r3, queries)
    rows4_13, by4_13 = score({k: [p[0] for p in v] for k, v in r4_13.items()}, queries)
    rows4_123, by4_123 = score({k: [p[0] for p in v] for k, v in r4_123.items()}, queries)

    out = {
        "описание": "D12 — контроль на FUNSD (50 форм, 14 запросов: 7 буквальных + 7 смысловых)",
        "ветка_1_слова": {"by_type": by1, "details": rows1},
        "ветка_2_смысл": {"by_type": by2, "details": rows2, "cost_usd": round((cmeta['cost'] or 0) + (qmeta['cost'] or 0), 6)},
        "ветка_3_siglip_EN": {"by_type": by3, "details": rows3},
        "ветка_4_гибрид_1_3": {"by_type": by4_13, "details": rows4_13},
        "ветка_4_гибрид_1_2_3": {"by_type": by4_123, "details": rows4_123},
    }
    (HERE / "raw" / "funsd_control_results.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "ветка_1": by1, "ветка_2": by2, "ветка_3": by3,
        "гибрид_1_3": by4_13, "гибрид_1_2_3": by4_123,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
