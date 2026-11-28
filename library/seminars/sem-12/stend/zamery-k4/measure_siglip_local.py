#!/usr/bin/env python3
"""Кейс 4 (issue #351) — тот же замер полосы неопределённости, что на модели
`nvidia/nemotron-3.5-embed-1b:free` (`rebuild_true_labels.py`), но ВТОРОЙ, НЕЗАВИСИМОЙ
моделью: SigLIP (`google/siglip-base-patch16-224`), целиком ЛОКАЛЬНО, без единого сетевого
вызова — вес модели уже лежит в кеше этого окружения (`~/.cache/huggingface/hub`), поэтому
даже загрузка модели не трогает сеть.

**Почему локальная модель, а не вторая сетевая.** Прямое указание брифа (§«живой стенд»):
бесплатный тариф `nvidia/nemotron-3.5-embed-1b:free` сам по себе уже на пределе (находка
соседней сессии 2026-11-21 — около 12 успешных ответов из 30 после восьми попыток на вызов),
а родственная модель `nvidia/llama-nemotron-embed-vl-1b-v2:free` исчезла из каталога
поставщика между 4 и 21 ноября. Повторять замер ещё одной сетевой моделью — рисковать тем же
дефицитом. SigLIP снимает этот риск: один раз загруженная модель, инференс на CPU, результат
воспроизводится бит в бит при повторном запуске.

**Почему эта версия НЕ наследует порок top-1 вообще, а не просто его не повторяет.** В замере
на nemotron единственный источник правды — сырой JSON предыдущего занятия, где near-dup
retrieval сохранял только argmax (лучшего кандидата), а не cosine против заведомо верного
оригинала — отсюда и выпавшая пара `receipt_02`. Здесь эмбеддинги всех 90 изображений (30
оригиналов + 30 soft-dup + 30 hard-dup) держатся в памяти целиком, поэтому cosine(дубль_i,
его_собственный_оригинал_i) вычисляется НАПРЯМУЮ для всех 30 без исключения — top-1 поиск
используется только для отдельной информационной метрики (recall@1), не для того, какие пары
попадают в разметку SAME.

Переиспользует БЕЗ ИЗМЕНЕНИЙ (только чтение, файл не трогается) из
`sem-10/stend/measure/case4_full_retrieval_30.py`: `cosine`, `to_data_url`, `soft_dup`,
`hard_dup` — те же детерминированные функции аугментации, что видела nemotron (resize*0,97+
recompress q60 для soft; поворот 12°+обрезка 4% для hard), так что оба замера сравнивают
модели на БУКВАЛЬНО одних и тех же файлах.

Запуск (из своей папки):

    cd library/seminars/sem-12/stend/zamery-k4
    python3 measure_siglip_local.py
    # -> raw/siglip_band_analysis.json; без обращений к сети (модель из кеша HF)
"""
import io
import json
import os
import sys
import time

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SEM10_MEASURE = os.path.join(HERE, "..", "..", "..", "sem-10", "stend", "measure")
sys.path.insert(0, SEM10_MEASURE)
_cwd_before_import = os.getcwd()
os.chdir(SEM10_MEASURE)  # case4_full_retrieval_30.py читает corpus-метаданные относительным путём при импорте
from case4_full_retrieval_30 import cosine, to_data_url, soft_dup, hard_dup  # noqa: E402
os.chdir(_cwd_before_import)

CORPUS_META = os.path.join(SEM10_MEASURE, "..", "corpus", "cord_sample_meta.json")
OUT = os.path.join(HERE, "raw", "siglip_band_analysis.json")
SIGLIP_MODEL_NAME = "google/siglip-base-patch16-224"


def data_url_to_pil(data_url):
    import base64
    raw = base64.b64decode(data_url.split(",", 1)[1])
    return Image.open(io.BytesIO(raw)).convert("RGB")


def load_siglip():
    import torch
    from transformers import SiglipImageProcessor, SiglipModel

    t0 = time.time()
    model = SiglipModel.from_pretrained(SIGLIP_MODEL_NAME)
    model.eval()
    processor = SiglipImageProcessor.from_pretrained(SIGLIP_MODEL_NAME)
    load_s = time.time() - t0
    return model, processor, load_s, torch


def embed(model, processor, torch, pil_im):
    t0 = time.time()
    inputs = processor(images=pil_im, return_tensors="pt")
    with torch.no_grad():
        out = model.get_image_features(**inputs)
    vec = out.pooler_output[0].tolist()
    return vec, time.time() - t0


def band_stats(same_vals, diff_vals, label):
    t_low = min(same_vals)
    t_high = max(diff_vals)
    n_total = len(same_vals) + len(diff_vals)
    if t_low > t_high:
        return {
            "case": label, "band_exists": False,
            "t_low": round(t_low, 4), "t_high": round(t_high, 4),
            "n_same_in_band": 0, "n_diff_in_band": 0, "n_total_pairs": n_total,
            "note": "зазор чистый — любой порог между t_high и t_low разделяет выборку без ошибок",
        }
    same_in_band = [v for v in same_vals if t_low <= v <= t_high]
    diff_in_band = [v for v in diff_vals if t_low <= v <= t_high]
    return {
        "case": label, "band_exists": True,
        "t_low": round(t_low, 4), "t_high": round(t_high, 4),
        "n_same_in_band": len(same_in_band), "n_diff_in_band": len(diff_in_band),
        "n_total_pairs": n_total,
        "share_in_band": round((len(same_in_band) + len(diff_in_band)) / n_total, 4),
        "same_values_in_band": sorted(same_in_band),
        "diff_values_in_band": sorted(diff_in_band),
    }


def threshold_tradeoff(same_vals, diff_vals, thresholds):
    rows = []
    for t in thresholds:
        fn = sum(1 for v in same_vals if v < t)
        fp = sum(1 for v in diff_vals if v >= t)
        rows.append({"threshold": round(t, 4), "false_non_match_FN": fn, "false_match_FP": fp, "fn_plus_fp": fn + fp})
    return rows


def run():
    t_wall0 = time.time()
    samples = json.load(open(CORPUS_META))
    ids = [s["id"] for s in samples]
    paths = {s["id"]: os.path.join(SEM10_MEASURE, "..", s["file"]) for s in samples}

    model, processor, load_s, torch = load_siglip()
    print(f"=== SigLIP ({SIGLIP_MODEL_NAME}) загружен из локального кеша за {load_s:.1f}с ===")

    orig_vec, soft_vec, hard_vec = {}, {}, {}
    infer_times = []
    for stage, pool, build in (
        ("оригиналы", orig_vec, lambda p: to_data_url(p)),
        ("soft-dup (пересжатие)", soft_vec, lambda p: soft_dup(p)),
        ("hard-dup (поворот+обрезка)", hard_vec, lambda p: hard_dup(p)),
    ):
        print(f"=== эмбеддинг 30 {stage} ===")
        for sid in ids:
            pil = data_url_to_pil(build(paths[sid]))
            vec, dt = embed(model, processor, torch, pil)
            pool[sid] = vec
            infer_times.append(dt)

    avg_infer_s = sum(infer_times) / len(infer_times)

    # ---- истинные SAME-пары: cosine(оригинал_i, дубль_i) НАПРЯМУЮ, без top-1 ----
    same_soft_true = [{"id": sid, "cosine": round(cosine(orig_vec[sid], soft_vec[sid]), 4)} for sid in ids]
    same_hard_true = [{"id": sid, "cosine": round(cosine(orig_vec[sid], hard_vec[sid]), 4)} for sid in ids]

    # ---- истинные DIFF-пары: для каждого оригинала — самый похожий ДРУГОЙ оригинал (full scan) ----
    diff_nearest_other = []
    for sid in ids:
        best, best_score = None, -2.0
        for other in ids:
            if other == sid:
                continue
            s = cosine(orig_vec[sid], orig_vec[other])
            if s > best_score:
                best_score, best = s, other
        diff_nearest_other.append({"id": sid, "nearest_other": best, "cosine": round(best_score, 4)})

    # ---- informational only: top-1 retrieval recall@1 (не влияет на разметку выше) ----
    def nearest_in_pool(query_vec, pool):
        best, best_score = None, -2.0
        for pid, v in pool.items():
            s = cosine(query_vec, v)
            if s > best_score:
                best_score, best = s, pid
        return best, best_score

    retrieval_rows = []
    for sid in ids:
        nn_soft, sc_soft = nearest_in_pool(soft_vec[sid], orig_vec)
        nn_hard, sc_hard = nearest_in_pool(hard_vec[sid], orig_vec)
        retrieval_rows.append({
            "id": sid,
            "soft_nearest": nn_soft, "soft_correct": nn_soft == sid, "soft_cosine": round(sc_soft, 4),
            "hard_nearest": nn_hard, "hard_correct": nn_hard == sid, "hard_cosine": round(sc_hard, 4),
        })
    recall_summary = {
        "n_scans": len(ids),
        "soft_dup_recall_at_1": sum(r["soft_correct"] for r in retrieval_rows) / len(retrieval_rows),
        "hard_dup_recall_at_1": sum(r["hard_correct"] for r in retrieval_rows) / len(retrieval_rows),
        "note": "recall@1 здесь — ТОЛЬКО информационная метрика поиска, она не определяет, какие "
                "пары попали в разметку SAME/DIFF ниже (та строится напрямую по истинному "
                "соответствию корпуса, без top-1 — см. docstring).",
    }

    soft_vals = [r["cosine"] for r in same_soft_true]
    hard_vals = [r["cosine"] for r in same_hard_true]
    diff_vals = [r["cosine"] for r in diff_nearest_other]

    easy = band_stats(soft_vals, diff_vals, "лёгкий случай (soft-dup: пересжатие+resize)")
    hard = band_stats(hard_vals, diff_vals, "трудный случай (hard-dup: поворот 12°+обрезка 4%)")

    hard_thresholds = sorted(set([hard["t_low"], hard["t_high"]] + [round(hard["t_low"] + 0.01 * i, 4)
                                                                     for i in range(1, int((hard["t_high"] - hard["t_low"]) * 100) + 1)]))
    tradeoff = threshold_tradeoff(hard_vals, diff_vals, hard_thresholds) if hard["band_exists"] else []

    wall_s = time.time() - t_wall0
    out = {
        "model": SIGLIP_MODEL_NAME,
        "model_settings": "мультимодальный энкодер картинки SigLIP base patch16-224, локальный "
                           "инференс на CPU, вход — тот же JPEG 300x450, что видела nemotron "
                           "(to_data_url/soft_dup/hard_dup из case4_full_retrieval_30.py, без "
                           "изменений)",
        "environment": {"device": "CPU", "checkpoint_source": "локальный кеш "
                         "~/.cache/huggingface/hub (без сетевого вызова)",
                         "checkpoint_load_s": round(load_s, 2),
                         "avg_forward_pass_s_per_image": round(avg_infer_s, 4),
                         "n_images_embedded": len(infer_times),
                         "total_wall_s_this_script": round(wall_s, 1)},
        "n_corpus_scans": 30,
        "corpus": "те же 30 реальных сканов CORD, sem-10/stend/corpus/",
        "labeling_method": "ИСТИННОЕ соответствие корпуса — cosine(оригинал_i, его собственный "
                            "soft/hard-dup) вычислен напрямую для всех 30 без исключения; top-1 "
                            "поиск посчитан отдельно и не влияет на разметку (см. "
                            "retrieval_recall_informational_only).",
        "retrieval_recall_informational_only": {"summary": recall_summary, "details": retrieval_rows},
        "easy_case": easy,
        "hard_case": hard,
        "threshold_tradeoff_hard_case": tradeoff,
        "raw_pairs": {
            "same_soft_true": same_soft_true,
            "same_hard_true": same_hard_true,
            "diff_nearest_other": diff_nearest_other,
        },
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("\n=== ИТОГ (SigLIP, истинная разметка, без top-1-смещения) ===")
    print(json.dumps({"easy_case": easy, "hard_case": hard, "recall_informational": recall_summary,
                       "environment": out["environment"]}, ensure_ascii=False, indent=2))
    print(f"\nзаписано: {OUT}")


if __name__ == "__main__":
    run()
