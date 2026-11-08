#!/usr/bin/env python3
"""Ранжирование 8 рабочих mm-кандидатов (case4_find_working_mm.py) по качеству
разделения: cosine(оригинал, мягкий почти-дубль ТОГО ЖЕ чека) ОБЯЗАН быть заметно
выше cosine(оригинал, другой случайный чек) — иначе "различает разные картинки"
не значит "пригодно для retrieval похожих/дублей". ПЕРВЫЙ, быстрый проход — один
чек (receipt_00), мягкая аугментация (та же, что case4_measure.py: resize*0.97 +
JPEG q60). Самодостаточен (не зависит от ephemeral *_raw.json других прогонов —
diff_doc_cos считается здесь же, не читается из файла). Устойчивая версия на 3
чеках — case4_rank_candidates2.py, её числа и есть те, что попали в README.
"""
import io
import json

from PIL import Image

from harness_call import call_raw


def to_data_url(path, w=300, h=450, q=80):
    im = Image.open(path).convert("RGB").resize((w, h))
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=q)
    import base64
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


def soft_dup_data_url(path, w=300, h=450, q=80):
    im = Image.open(path).convert("RGB")
    soft = im.resize((int(im.width * 0.97), int(im.height * 0.97))).resize((w, h))
    buf = io.BytesIO()
    soft.save(buf, format="JPEG", quality=60)
    import base64
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


CANDIDATES = [
    "cohere/embed-5-fast",
    "cohere/embed-5-pro",
    "nvidia/nemotron-3.5-embed-1b:free",
    "nvidia/nemotron-3.5-embed-8b:free",
    "mongodb/voyage-multimodal-3.5",
    "google/gemini-embedding-2",
    "google/gemini-embedding-2-preview",
    "nvidia/llama-nemotron-embed-vl-1b-v2:free",
]

def run():
    orig_url = to_data_url("../corpus/cord_sample/receipt_00.jpg")
    soft_url = soft_dup_data_url("../corpus/cord_sample/receipt_00.jpg")
    other_url = to_data_url("../corpus/cord_sample/receipt_15.jpg")

    ranking = []
    for model in CANDIDATES:
        ra = call_raw("https://openrouter.ai/api/v1/embeddings", {"model": model, "input": orig_url}, timeout=60)
        rb = call_raw("https://openrouter.ai/api/v1/embeddings", {"model": model, "input": soft_url}, timeout=60)
        rc = call_raw("https://openrouter.ai/api/v1/embeddings", {"model": model, "input": other_url}, timeout=60)
        resp_a, resp_b, resp_c = ra["response"] or {}, rb["response"] or {}, rc["response"] or {}
        if "data" not in resp_a or "data" not in resp_b or "data" not in resp_c:
            print(model, "ERROR", json.dumps(resp_a, ensure_ascii=False)[:150], json.dumps(resp_b, ensure_ascii=False)[:150])
            continue
        vec_a, vec_b, vec_c = resp_a["data"][0]["embedding"], resp_b["data"][0]["embedding"], resp_c["data"][0]["embedding"]
        same_doc_cos = cosine(vec_a, vec_b)
        diff_doc_cos = cosine(vec_a, vec_c)
        margin = same_doc_cos - diff_doc_cos
        row = {"model": model, "cosine_same_doc_soft_dup": round(same_doc_cos, 6),
               "cosine_diff_doc": round(diff_doc_cos, 6), "margin": round(margin, 6)}
        ranking.append(row)
        print(model, "same_doc=", row["cosine_same_doc_soft_dup"], "diff_doc=", row["cosine_diff_doc"], "margin=", row["margin"])

    ranking.sort(key=lambda r: -r["margin"])
    print("\n=== RANKING (margin desc, n=1 чек — быстрая прикидка, см. case4_rank_candidates2.py для устойчивой версии) ===")
    for r in ranking:
        print(r)
    return ranking


if __name__ == "__main__":
    run()
