#!/usr/bin/env python3
"""Кейс 4 (issue #311) — поиск РАБОЧЕЙ мультимодальной embedding-модели на этом стенде,
по прямому указанию владельца («давай попробуем тут всё-таки рабочий кейс сделать»).

Метод:
1. Полный каталог `GET /v1/embeddings/models` (НЕ основной /v1/models — тот отдаёт только
   chat-модели, эмбеддинговые модели живут в отдельном, недокументированном явно списке,
   см. README §"Открытый технический риск"). Найдено живым вызовом 2026-11-04:
   `https://openrouter.ai/api/v1/embeddings/models` — публичный, без credential-ключа.
2. Из 40 эмбеддинг-моделей каталога отобраны по `architecture.input_modalities` содержащим
   "image" — 9 штук (включая уже известный битый `amazon/titan-embed-image-v1`).
3. Контролируемый тест (ТОТ ЖЕ критерий, что в case4_measure.py / README): два ЗАВЕДОМО
   РАЗНЫХ скана CORD (receipt_00.jpg, receipt_15.jpg — та же пара, что в
   raw/case4_resolution_probe.json, для сравнимости), разрешение 300×450 (та же договорённость
   "реальный скан" из resolution_probe), JPEG q80. cosine между эмбеддингами ОБЯЗАН заметно
   отличаться от 1.0, если модель реально видит картинку (простой факт "ответ без ошибки"
   ничего не доказывает — см. README).
"""
import base64
import io
import json
import time

from PIL import Image

from harness_call import call_raw


def to_data_url(path, w=300, h=450, q=80):
    im = Image.open(path).convert("RGB").resize((w, h))
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=q)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"data:image/jpeg;base64,{b64}", len(b64)


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


CANDIDATES = [
    "amazon/titan-embed-image-v1",          # известный битый (контроль, перепроверка)
    "cohere/embed-5-fast",
    "cohere/embed-5-pro",
    "nvidia/nemotron-3.5-embed-1b:free",
    "nvidia/nemotron-3.5-embed-8b:free",
    "mongodb/voyage-multimodal-3.5",
    "google/gemini-embedding-2",
    "google/gemini-embedding-2-preview",
    "nvidia/llama-nemotron-embed-vl-1b-v2:free",
]

IMG_A = "../corpus/cord_sample/receipt_00.jpg"
IMG_B = "../corpus/cord_sample/receipt_15.jpg"


def embed_image(model, data_url, timeout=90):
    body = {"model": model, "input": data_url}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=timeout)
    resp = r["response"] or {}
    return resp, r


def run():
    data_url_a, len_a = to_data_url(IMG_A)
    data_url_b, len_b = to_data_url(IMG_B)
    print(f"IMG_A b64_chars={len_a} IMG_B b64_chars={len_b}")

    results = []
    for model in CANDIDATES:
        row = {"model": model}
        # text sanity probe first (cheap-ish, confirms model id resolves + text path works)
        rt = call_raw("https://openrouter.ai/api/v1/embeddings",
                       {"model": model, "input": "test"}, timeout=30)
        resp_t = rt["response"] or {}
        if "error" in resp_t or "data" not in resp_t:
            row["status"] = "MODEL_NOT_AVAILABLE_OR_TEXT_ERROR"
            row["text_probe_error"] = json.dumps(resp_t, ensure_ascii=False)[:300]
            print(model, "-> MODEL NOT AVAILABLE:", row["text_probe_error"])
            results.append(row)
            continue
        row["text_probe_dim"] = len(resp_t["data"][0]["embedding"])

        resp_a, ra = embed_image(model, data_url_a)
        resp_b, rb = embed_image(model, data_url_b)
        row["exec_ids"] = [ra.get("exec_id"), rb.get("exec_id")]
        if "data" not in resp_a or "data" not in resp_b:
            row["status"] = "IMAGE_INPUT_ERROR"
            row["image_error_a"] = json.dumps(resp_a, ensure_ascii=False)[:300]
            row["image_error_b"] = json.dumps(resp_b, ensure_ascii=False)[:300]
            print(model, "-> IMAGE INPUT ERROR:", row.get("image_error_a") or row.get("image_error_b"))
            results.append(row)
            continue

        vec_a = resp_a["data"][0]["embedding"]
        vec_b = resp_b["data"][0]["embedding"]
        row["dim"] = len(vec_a)
        cos = cosine(vec_a, vec_b)
        row["cosine_different_receipts"] = round(cos, 9)
        row["bit_identical"] = (vec_a == vec_b)
        row["usage_a"] = resp_a.get("usage")
        row["usage_b"] = resp_b.get("usage")
        if row["bit_identical"] or cos > 0.9999:
            row["status"] = "BROKEN_IGNORES_IMAGE"
        else:
            row["status"] = "DISTINGUISHES_IMAGES"
        print(model, "-> cosine(different receipts) =", row["cosine_different_receipts"],
              "bit_identical=", row["bit_identical"], "=>", row["status"])
        results.append(row)
        time.sleep(0.5)

    out = {
        "purpose": "issue #311 — поиск рабочей мультимодальной embedding-модели на стенде "
                   "OpenRouter, по прямому указанию владельца («давай попробуем тут всё-таки "
                   "рабочий кейс сделать»), помимо уже документированного провала "
                   "amazon/titan-embed-image-v1.",
        "catalog_source": "GET https://openrouter.ai/api/v1/embeddings/models (40 моделей всего, "
                           "9 из них с 'image' в architecture.input_modalities) — "
                           "НЕ основной /v1/models (452-453 chat-модели, embedding-моделей там нет "
                           "вообще, подтверждено живым запросом 2026-11-04).",
        "test_pair": [IMG_A, IMG_B],
        "test_resolution": "300x450 JPEG q80 (та же договорённость 'реальный скан', что "
                            "raw/case4_resolution_probe.json)",
        "criterion": "cosine между эмбеддингами ДВУХ РАЗНЫХ чеков обязан заметно отличаться от "
                     "1.0, если модель реально использует картинку; факт ответа без HTTP-ошибки "
                     "ничего не доказывает (см. README).",
        "candidates": results,
    }
    json.dump(out, open("case4-find-working-mm-results.json", "w", encoding="utf-8"),
               ensure_ascii=False, indent=2)
    print("\n=== ИТОГ ===")
    for r in results:
        print(r["model"], "->", r.get("status"))


if __name__ == "__main__":
    run()
