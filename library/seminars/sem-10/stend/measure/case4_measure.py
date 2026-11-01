#!/usr/bin/env python3
"""Кейс 4 — подпись/OCR→текстовый эмбеддинг vs мультимодальный эмбеддинг картинки
(amazon/titan-embed-image-v1 через OpenRouter — voyage-multimodal-3 не существует на
этом стенде, см. README §"Открытый технический риск", живой прогон test_embed*.py)
vs perceptual hash (дубли/почти-дубли) — на подвыборке CORD (30 сканов чеков).
"""
import base64
import io
import json
import time

from PIL import Image

from harness2 import embed_batch, cosine, call_raw

samples = json.load(open("cord_sample_meta.json"))


# ---------- 1. подготовка картинок (сжатие под лимит /embeddings, см. README) ----------
def to_data_url(path, w=64, h=96, q=80):
    im = Image.open(path).convert("RGB").resize((w, h))
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=q)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"data:image/jpeg;base64,{b64}", len(b64)


# ---------- 2. perceptual hash (классика, без ИИ, без внешних библиотек) ----------
def average_hash(path, hash_size=8):
    im = Image.open(path).convert("L").resize((hash_size, hash_size), Image.LANCZOS)
    pixels = list(im.getdata())
    avg = sum(pixels) / len(pixels)
    bits = "".join("1" if p > avg else "0" for p in pixels)
    return bits


def hamming(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


# ---------- запуск ----------
def run():
    t0 = time.time()

    # мультимодальный эмбеддинг — по одной картинке за вызов (модель не принимает
    # массив input, см. test_mm_format.py: array -> "invalid_union expected string")
    mm_vecs = {}
    mm_cost = 0.0
    for s in samples:
        data_url, b64len = to_data_url(s["file"])
        body = {"model": "amazon/titan-embed-image-v1", "input": data_url}
        r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=60)
        resp = r["response"] or {}
        if "data" not in resp:
            print("ОШИБКА embed", s["id"], json.dumps(resp, ensure_ascii=False)[:200])
            continue
        mm_vecs[s["id"]] = resp["data"][0]["embedding"]
        mm_cost += (resp.get("usage", {}) or {}).get("cost", 0) or 0
        print(f"  mm-embed {s['id']}: b64={b64len} wall={r['wall_s']}s")

    # текстовый эмбеддинг подписи/OCR — батчем
    ocr_texts = [s["ocr_text"] for s in samples]
    text_vecs_list, text_meta = embed_batch(ocr_texts)
    text_vecs = {s["id"]: v for s, v in zip(samples, text_vecs_list)}
    print(f"text-embed batch: wall={text_meta['wall_s']}s cost={text_meta['cost']}")

    # perceptual hash
    phashes = {s["id"]: average_hash(s["file"]) for s in samples}

    # --- A. корреляция "текст похож" vs "картинка похожа" по всем парам ---
    ids = [s["id"] for s in samples]
    text_sims, img_sims, phash_dists = [], [], []
    pair_rows = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            ts = cosine(text_vecs[a], text_vecs[b])
            vs = cosine(mm_vecs[a], mm_vecs[b]) if a in mm_vecs and b in mm_vecs else None
            hd = hamming(phashes[a], phashes[b])
            text_sims.append(ts)
            if vs is not None:
                img_sims.append(vs)
            phash_dists.append(hd)
            pair_rows.append({"a": a, "b": b, "text_cosine": round(ts, 3),
                               "image_cosine": round(vs, 3) if vs is not None else None,
                               "phash_hamming": hd})

    def pearson(xs, ys):
        n = len(xs)
        mx, my = sum(xs) / n, sum(ys) / n
        cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        vx = sum((x - mx) ** 2 for x in xs)
        vy = sum((y - my) ** 2 for y in ys)
        return cov / ((vx * vy) ** 0.5) if vx and vy else 0.0

    paired_text = [r["text_cosine"] for r in pair_rows if r["image_cosine"] is not None]
    paired_img = [r["image_cosine"] for r in pair_rows if r["image_cosine"] is not None]
    corr_text_image = pearson(paired_text, paired_img)

    # --- B. контролируемый почти-дубль: лёгкая (пересжатие) и жёсткая (поворот+обрезка) аугментация ---
    import random
    random.seed(3)
    aug_ids = random.sample(ids, 6)
    aug_results = []
    for aid in aug_ids:
        src = next(s for s in samples if s["id"] == aid)["file"]
        im = Image.open(src).convert("RGB")
        # мягкая аугментация: пересжатие + небольшое изменение размера (имитация повторного скана)
        soft = im.resize((int(im.width * 0.97), int(im.height * 0.97)))
        buf = io.BytesIO(); soft.save(buf, format="JPEG", quality=60)
        soft_bytes = buf.getvalue()
        # жёсткая аугментация: поворот 12° + обрезка края (другой угол съёмки телефоном)
        hard = im.rotate(12, expand=True, fillcolor=(255, 255, 255))
        w, h = hard.size
        hard = hard.crop((int(w * 0.04), int(h * 0.04), int(w * 0.96), int(h * 0.96)))

        soft_path = f"cord_sample/{aid}_soft.jpg"
        hard_path = f"cord_sample/{aid}_hard.jpg"
        Image.open(io.BytesIO(soft_bytes)).save(soft_path)
        hard.save(hard_path)

        orig_phash = phashes[aid]
        soft_phash = average_hash(soft_path)
        hard_phash = average_hash(hard_path)

        def mm_embed_file(path):
            data_url, _ = to_data_url(path)
            body = {"model": "amazon/titan-embed-image-v1", "input": data_url}
            r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=60)
            resp = r["response"] or {}
            return resp["data"][0]["embedding"] if "data" in resp else None

        soft_vec = mm_embed_file(soft_path)
        hard_vec = mm_embed_file(hard_path)

        other_ids = [x for x in ids if x != aid]
        random_other = random.choice(other_ids)
        baseline_phash_dist = hamming(orig_phash, phashes[random_other])
        baseline_cos = cosine(mm_vecs[aid], mm_vecs[random_other]) if aid in mm_vecs else None

        aug_results.append({
            "id": aid,
            "phash_hamming_vs_soft_dup": hamming(orig_phash, soft_phash),
            "phash_hamming_vs_hard_dup": hamming(orig_phash, hard_phash),
            "phash_hamming_vs_unrelated_baseline": baseline_phash_dist,
            "image_cosine_vs_soft_dup": round(cosine(mm_vecs[aid], soft_vec), 3) if soft_vec and aid in mm_vecs else None,
            "image_cosine_vs_hard_dup": round(cosine(mm_vecs[aid], hard_vec), 3) if hard_vec and aid in mm_vecs else None,
            "image_cosine_vs_unrelated_baseline": round(baseline_cos, 3) if baseline_cos is not None else None,
        })
        print(f"  aug {aid}: soft_phash_dist={aug_results[-1]['phash_hamming_vs_soft_dup']} "
              f"hard_phash_dist={aug_results[-1]['phash_hamming_vs_hard_dup']} "
              f"baseline_phash_dist={baseline_phash_dist}")

    elapsed = time.time() - t0
    out = {
        "n_images": len(samples),
        "source": "naver-clova-ix/cord-v2, test split, первые 30 сканов",
        "mm_model": "amazon/titan-embed-image-v1 (voyage-multimodal-3 не существует на OpenRouter "
                    "этого стенда — живой прогон test_embed2.py/test_embed3.py, см. README)",
        "mm_model_critical_finding": (
            "живым прогоном (debug_mm.py/debug_mm3..6.py) обнаружено: на реальном разрешении скана "
            "(300x450 JPEG q80, base64 ~18-26 тыс. символов) модель возвращает БИТОВО ИДЕНТИЧНЫЙ "
            "вектор для ЛЮБЫХ двух разных картинок (cosine=1.0, совпадение до 9 знаков) — запрос "
            "не ошибается, выглядит как успех, но картинка не учитывается вообще. Порог проверен "
            "вилкой: 64x96 (~6-8 тыс. символов base64) — вектор меняется от картинки к картинке "
            "(см. ниже); 128x192 (~4.3-4.6 тыс.) — меняется слабо (cosine~0.997); 300x450 — не "
            "меняется совсем. Этот замер использует 64x96 — единственный проверенный рабочий размер, "
            "т.е. МУЛЬТИМОДАЛЬНЫЙ ЭМБЕДДИНГ ЧЕРЕЗ OPENROUTER НА ЭТОМ СТЕНДЕ РАБОТАЕТ ТОЛЬКО ДЛЯ "
            "ТЕЛЕФОННОЙ ИКОНКИ-ПРЕВЬЮ, НЕ ДЛЯ СКАНА ЧИТАЕМОГО РАЗМЕРА — архитектурно иной результат, "
            "чем план ожидал (ARCHITECTURE.md §5/§7 п.1); подробности и сырые вызовы — debug_mm*.py."
        ),
        "text_model": "openai/text-embedding-3-small",
        "mm_embed_cost_usd": round(mm_cost, 6),
        "text_embed_cost_usd": text_meta["cost"],
        "n_images_mm_embedded": len(mm_vecs),
        "correlation_text_vs_image_cosine_over_all_pairs": round(corr_text_image, 3),
        "n_pairs": len(pair_rows),
        "near_duplicate_injection_test": aug_results,
        "note_on_near_dup_test": ("OCR-текст (ground truth CORD) не меняется аугментацией изображения — "
                                   "честно тестировать 'подпись теряет визуальное' на этой паре нельзя "
                                   "(реальный OCR на повороте бы деградировал, эталонная разметка нет); "
                                   "поэтому near-dup тест ограничен phash vs мультимодальный эмбеддинг."),
        "total_wall_s": round(elapsed, 1),
    }
    json.dump({"summary": out, "pairs_sample": pair_rows[:40]},
              open("case4-results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
