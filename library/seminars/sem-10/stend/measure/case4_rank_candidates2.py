#!/usr/bin/env python3
"""Расширение case4_rank_candidates.py: margin (same-doc near-dup cosine - diff-doc
cosine) на 3 чеках вместо 1, чтобы не полагаться на один шумный замер перед выбором
модели для полного замера по 30 сканам."""
import json

import base64
import io

from PIL import Image

from harness_call import call_raw


def to_data_url(path, w=300, h=450, q=80):
    im = Image.open(path).convert("RGB").resize((w, h))
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=q)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


def soft_dup_data_url(path, w=300, h=450, q=80):
    im = Image.open(path).convert("RGB")
    soft = im.resize((int(im.width * 0.97), int(im.height * 0.97))).resize((w, h))
    buf = io.BytesIO()
    soft.save(buf, format="JPEG", quality=60)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0

CANDIDATES = [
    "nvidia/nemotron-3.5-embed-1b:free",
    "nvidia/llama-nemotron-embed-vl-1b-v2:free",
    "mongodb/voyage-multimodal-3.5",
    "google/gemini-embedding-2",
    "cohere/embed-5-fast",
]
RECEIPTS = ["receipt_00.jpg", "receipt_15.jpg", "receipt_07.jpg"]

results = {}
for model in CANDIDATES:
    margins = []
    for rid in RECEIPTS:
        path = f"../corpus/cord_sample/{rid}"
        orig = to_data_url(path)
        soft = soft_dup_data_url(path)
        other_rid = next(r for r in RECEIPTS if r != rid)
        other_path = f"../corpus/cord_sample/{other_rid}"
        other_orig = to_data_url(other_path)
        ra = call_raw("https://openrouter.ai/api/v1/embeddings", {"model": model, "input": orig}, timeout=60)
        rb = call_raw("https://openrouter.ai/api/v1/embeddings", {"model": model, "input": soft}, timeout=60)
        rc = call_raw("https://openrouter.ai/api/v1/embeddings", {"model": model, "input": other_orig}, timeout=60)
        resp_a, resp_b, resp_c = ra["response"] or {}, rb["response"] or {}, rc["response"] or {}
        if "data" not in resp_a or "data" not in resp_b or "data" not in resp_c:
            print(model, rid, "ERROR")
            continue
        va, vb, vc = resp_a["data"][0]["embedding"], resp_b["data"][0]["embedding"], resp_c["data"][0]["embedding"]
        same_doc = cosine(va, vb)
        diff_doc = cosine(va, vc)
        margins.append(same_doc - diff_doc)
        print(model, rid, "same_doc=", round(same_doc, 4), "diff_doc=", round(diff_doc, 4), "margin=", round(same_doc - diff_doc, 4))
    avg_margin = sum(margins) / len(margins) if margins else None
    results[model] = {"margins": margins, "avg_margin": avg_margin}
    print(f"  >>> {model} avg_margin={avg_margin}")

json.dump(results, open("case4-rank-candidates2-results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
