#!/usr/bin/env python3
"""Кейс 4 (issue #351) — полоса неопределённости на уже измеренном сырье С10.

Ничего не вызывает стенд повторно (канон: «распределение 435 пар уже измерено... пересчитывать
не надо»). Берёт сырые числа из sem-10/stend/raw/case4_mm_full_retrieval.json — часть A
(near-dup retrieval: soft-dup = пересжатие+resize*0.97, hard-dup = поворот 12°+обрезка 4%) и
часть C (семантическое сходство: для каждого из 30 чеков — ближайший ДРУГОЙ чек по тому же
mm-эмбеддингу) — и размечает пары «тот же документ / другой документ» явно, вместо того чтобы
читать их из агрегированной статистики.

Модель: nvidia/nemotron-3.5-embed-1b:free (мультимодальный эмбеддинг, картинка на входе,
300x450 JPEG q80, выбрана на С10 по margin-тесту — README-part2.md). Дата исходного замера:
2026-11-04 (issue #311, sem-10). Рецепт пересборки исходных чисел —
sem-10/stend/measure/case4_full_retrieval_30.py.

Разметка пар:
  SAME  — (оригинал_i, soft-dup_i) и (оригинал_i, hard-dup_i), где dup — деформированная копия
          ТОГО ЖЕ документа (деформация детерминирована, задаётся кодом С10).
  DIFF  — (оригинал_i, оригинал_j) для i != j — все 30 сканов CORD в корпусе суть РАЗНЫЕ
          настоящие документы (не дубли друг друга), это гарантия корпуса, не предположение.

Канон §8.12 (отказы грейдера читаются глазами): near-dup retrieval в части A ищет ближайший
ОРИГИНАЛ по cosine, а не просто публикует cosine(dup, свой оригинал) — в одном случае из 30
(hard-dup) ближайшим оказался ЧУЖОЙ оригинал. Для этого случая записанный cosine — это
НЕ SAME-пара, а ещё одна, причём особо опасная, DIFF-пара (дубль документа обманул поиск и
подошёл к другому документу ближе, чем к своему). Скрипт разбирает этот случай явно, не
усредняет его молча в выборку SAME.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_MM = os.path.join(HERE, "..", "..", "..", "sem-10", "stend", "raw", "case4_mm_full_retrieval.json")
OUT = os.path.join(HERE, "raw", "band_analysis.json")

MM_MODEL = "nvidia/nemotron-3.5-embed-1b:free"


def load():
    with open(SRC_MM, encoding="utf-8") as f:
        return json.load(f)


def build_labeled_pairs(d):
    part_a = d["part_A_near_dup_retrieval"]["details"]
    part_c = d["part_C_semantic_similarity_agreement"]["details"]

    same_soft = []   # (id, cosine) — оригинал против своего soft-dup, все 30 корректны
    same_hard = []   # (id, cosine) — оригинал против своего hard-dup, где recall@1 верный
    diff_misfire = []  # hard-dup, где ближайшим оказался ЧУЖОЙ оригинал — это DIFF, не SAME
    diff_nearest_other = []  # (id, nearest_other_id, cosine) — из part C, все пары гарантированно разные документы

    for row in part_a:
        rid = row["id"]
        if row.get("mm_soft_cosine") is not None:
            same_soft.append({"id": rid, "cosine": row["mm_soft_cosine"], "correct": row["mm_soft_correct"]})
        if row.get("mm_hard_cosine") is not None:
            if row["mm_hard_correct"]:
                same_hard.append({"id": rid, "cosine": row["mm_hard_cosine"]})
            else:
                diff_misfire.append({
                    "dup_of": rid,
                    "matched_instead": row["mm_hard_nearest"],
                    "cosine": row["mm_hard_cosine"],
                    "note": f"hard-dup документа {rid} (поворот 12°+обрезка 4%) подошёл по "
                             f"cosine ближе к ЧУЖОМУ документу {row['mm_hard_nearest']}, чем к "
                             f"своему оригиналу — настоящая DIFF-пара, не SAME.",
                })

    for row in part_c:
        if row.get("mm_cosine") is not None:
            diff_nearest_other.append({"id": row["id"], "nearest_other": row["mm_nearest"], "cosine": row["mm_cosine"]})

    # все soft-dup попали в правильный self-match (recall@1 = 1.0/30) — без misfire
    assert all(r["correct"] for r in same_soft), "неожиданный misfire в soft-dup — перепроверить руками"

    return same_soft, same_hard, diff_misfire, diff_nearest_other


def band_stats(same_vals, diff_vals, label):
    """same_vals, diff_vals — списки cosine. Возвращает порог-инвариантную статистику полосы."""
    t_low = min(same_vals)            # ниже — только DIFF в выборке (уверенно "другой")
    t_high = max(diff_vals)           # выше — только SAME в выборке (уверенно "тот же")
    if t_low > t_high:
        # чистое разделение, полосы нет
        return {
            "case": label,
            "band_exists": False,
            "t_low": round(t_low, 4),
            "t_high": round(t_high, 4),
            "n_same_in_band": 0,
            "n_diff_in_band": 0,
            "n_total_pairs": len(same_vals) + len(diff_vals),
            "note": "min(SAME) > max(DIFF) — зазор чистый, порог в этом промежутке разделяет "
                    "выборку без единой ошибки.",
        }
    same_in_band = [v for v in same_vals if t_low <= v <= t_high]
    diff_in_band = [v for v in diff_vals if t_low <= v <= t_high]
    return {
        "case": label,
        "band_exists": True,
        "t_low": round(t_low, 4),
        "t_high": round(t_high, 4),
        "n_same_in_band": len(same_in_band),
        "n_diff_in_band": len(diff_in_band),
        "n_total_pairs": len(same_vals) + len(diff_vals),
        "share_in_band": round((len(same_in_band) + len(diff_in_band)) / (len(same_vals) + len(diff_vals)), 4),
        "same_values_in_band": sorted(same_in_band),
        "diff_values_in_band": sorted(diff_in_band),
    }


def threshold_tradeoff(same_vals, diff_vals, thresholds):
    """При каждом пороге T (match, если cosine >= T): сколько FN (пропущен тот же документ)
    и FP (принят чужой за тот же) в нашей размеченной выборке."""
    rows = []
    for t in thresholds:
        fn = sum(1 for v in same_vals if v < t)
        fp = sum(1 for v in diff_vals if v >= t)
        rows.append({"threshold": round(t, 4), "false_non_match_FN": fn, "false_match_FP": fp, "fn_plus_fp": fn + fp})
    return rows


def run():
    d = load()
    same_soft, same_hard, diff_misfire, diff_nearest_other = build_labeled_pairs(d)

    soft_vals = [r["cosine"] for r in same_soft]
    hard_vals = [r["cosine"] for r in same_hard]
    diff_vals_base = [r["cosine"] for r in diff_nearest_other]
    diff_vals_with_misfire = diff_vals_base + [r["cosine"] for r in diff_misfire]

    easy = band_stats(soft_vals, diff_vals_base, "лёгкий случай (soft-dup: пересжатие+resize)")
    hard = band_stats(hard_vals, diff_vals_with_misfire, "трудный случай (hard-dup: поворот 12°+обрезка 4%)")

    hard_thresholds = sorted(set([hard["t_low"], hard["t_high"]] + [round(hard["t_low"] + 0.01 * i, 4)
                                                                     for i in range(1, int((hard["t_high"] - hard["t_low"]) * 100) + 1)]))
    tradeoff = threshold_tradeoff(hard_vals, diff_vals_with_misfire, hard_thresholds)

    out = {
        "model": MM_MODEL,
        "model_settings": "мультимодальный эмбеддинг, вход — JPEG 300x450 q80 (soft-dup: resize*0.97"
                           "+recompress q60 перед финальным ресайзом; hard-dup: поворот 12°, обрезка "
                           "4% краёв, затем ресайз)",
        "source_measurement_date": "2026-11-04",
        "source_issue": "sem-10 issue #311, доп. проход «поиск рабочей мультимодальной модели»",
        "source_raw_file": "sem-10/stend/raw/case4_mm_full_retrieval.json",
        "source_recipe": "sem-10/stend/measure/case4_full_retrieval_30.py",
        "new_stand_calls": 0,
        "n_corpus_scans": 30,
        "corpus": "30 реальных сканов CORD (naver-clova-ix/cord-v2, test split), sem-10/stend/corpus/",
        "labeling_method": {
            "SAME": "оригинал_i против его собственного soft-dup или hard-dup (детерминированная "
                    "деформация, не отдельный документ)",
            "DIFF": "оригинал_i против оригинала_j (i != j, все 30 — гарантированно разные настоящие "
                    "документы) + одна найденная by-eye misfire-пара (см. diff_misfire_case ниже)",
        },
        "easy_case": easy,
        "hard_case": hard,
        "diff_misfire_case_read_by_eye": diff_misfire,
        "threshold_tradeoff_hard_case": tradeoff,
        "raw_pairs": {
            "same_soft": same_soft,
            "same_hard": same_hard,
            "diff_nearest_other": diff_nearest_other,
            "diff_misfire": diff_misfire,
        },
        "background_different_modality_not_fused": {
            "note": "Текстовый (OCR) эмбеддинг, другая модель — фон, не входит в полосу выше: "
                    "435 пар, openai/text-embedding-3-small, среднее 0.5206, диапазон 0.2766-0.8487 "
                    "(sem-10/stend/raw/case4_mm_full_retrieval.json → pairwise_text_cosine_stats_all_435_pairs). "
                    "Не смешивается с mm-числами выше: другая модальность, другая модель.",
            "model": "openai/text-embedding-3-small",
            "n_pairs": d["pairwise_text_cosine_stats_all_435_pairs"]["n_pairs"],
            "mean": d["pairwise_text_cosine_stats_all_435_pairs"]["mean"],
            "min": d["pairwise_text_cosine_stats_all_435_pairs"]["min"],
            "max": d["pairwise_text_cosine_stats_all_435_pairs"]["max"],
        },
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(json.dumps({"easy_case": easy, "hard_case": hard, "misfire": diff_misfire}, ensure_ascii=False, indent=2))
    print(f"\nзаписано: {OUT}")


if __name__ == "__main__":
    run()
