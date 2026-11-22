#!/usr/bin/env python3
"""Кейс 4 (issue #351) — пересборка разметки SAME/DIFF по ИСТИННЫМ меткам корпуса, не по
выдаче top-1 метода (находка этой сессии, см. `README.md` раздел «Порок первой версии
разметки»).

**Что было не так в `analyze_band.py`.** Прежняя разметка брала SAME-пару в выборку, только
если near-dup retrieval (поиск ближайшего оригинала по cosine среди всех 30) САМ нашёл
правильный оригинал (`mm_hard_correct == True`). Это разметка по выдаче метода, который
оценивается, а не по истинному соответствию корпуса (какой скан — дубль какого документа —
известно по построению корпуса, независимо от того, что ответил метод). У одного из 30 сканов
(`receipt_02`, hard-dup) near-dup retrieval ошибся и посчитал ближайшим ЧУЖОЙ документ
(`receipt_04`) — и из-за этого истинная SAME-пара (receipt_02 hard-dup × его собственный
оригинал receipt_02) целиком выпала из выборки: её cosine никогда не сохранялся, потому что
`case4_full_retrieval_30.py::nearest_mm` возвращает только argmax (лучший кандидат), а не
cosine против ПРАВИЛЬНОГО кандидата, если он не победил.

**Что здесь исправлено.** Разметка SAME строится по истинному соответствию корпуса: у каждого
из 30 сканов РОВНО один dup на один оригинал, и это пара SAME независимо от того, что сказал
top-1 поиск. Для 29 из 30 сканов исходный cosine(dup, свой оригинал) совпадает с тем, что было
сохранено (там retrieval ответил верно, значит сохранённое число и искомое — одно и то же). Для
`receipt_02` точного числа нет физически в сыром JSON С10 (см. выше) — и этот замер его не
изобретает. Новый вызов к модели, который восстановил бы ровно это число, в этой сессии
недоступен: сетевой доступ к стенду n8n здесь блокируется на уровне чтения credentials
(классификатор auto-mode отказал в `source /home/harness/.n8n-lab-credentials`), а независимо
от этого запасной сетевой путь всё равно рискованный — тот же бесплатный тариф
`nemotron-3.5-embed-1b:free`, по свежей находке соседней сессии (2026-11-21), отдаёт около
12 векторов из 30 после восьми попыток на вызов. Поэтому значение честно помечено «не
замерено», с верхней границей (<0,7547 — ровно поэтому top-1 предпочёл receipt_04).

Численные выводы о полосе (t_low/t_high/доля пар в полосе/торговля порогом) **не меняются**
относительно `analyze_band.py`: они и раньше считались по известным числам, и ровно эти же 29
известных SAME-значений остаются известными здесь. Что меняется — методология разметки (от
«что сказал метод» к «что известно о корпусе») и явное присутствие гэпа в данных вместо его
молчаливого исчезновения. Единственный содержательный новый вывод: раз истинных SAME-пар 30, а
не 29, доля полосы должна считаться от 30+31=61 истинной пары, а не от 60 — и тот способ
подсчёта, который был в `analyze_band.py` (60), слегка ЗАНИЖАЛ знаменатель и тем самым
НЕМНОГО ЗАНИЖАЛ видимую полосу (см. README).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_MM = os.path.join(HERE, "..", "..", "..", "sem-10", "stend", "raw", "case4_mm_full_retrieval.json")
OUT = os.path.join(HERE, "raw", "band_analysis_true_labels.json")

MM_MODEL = "nvidia/nemotron-3.5-embed-1b:free"


def load():
    with open(SRC_MM, encoding="utf-8") as f:
        return json.load(f)


def build_true_labeled_pairs(d):
    part_a = d["part_A_near_dup_retrieval"]["details"]
    part_c = d["part_C_semantic_similarity_agreement"]["details"]

    same_soft = []          # 30 — все корректны у исходного замера, истинная метка = top-1 здесь совпадают
    same_hard_known = []    # 29 — истинная SAME-пара, cosine известен (retrieval не ошибся)
    same_hard_unmeasured = []  # 0 или 1 — истинная SAME-пара есть по корпусу, но cosine не сохранён
    diff_misfire = []       # DIFF-пара, найденная ПОБОЧНО тем же поиском (не входит в "30 nearest-other")
    diff_nearest_other = []  # 30 — оригинал_i против ближайшего ДРУГОГО оригинала (part C, всегда истинный DIFF)

    for row in part_a:
        rid = row["id"]
        if row.get("mm_soft_cosine") is not None:
            same_soft.append({"id": rid, "cosine": row["mm_soft_cosine"]})
        if row.get("mm_hard_cosine") is not None:
            if row["mm_hard_correct"]:
                # top-1 указал на истинный оригинал — сохранённое число и есть cosine(dup, свой оригинал)
                same_hard_known.append({"id": rid, "cosine": row["mm_hard_cosine"]})
            else:
                # истинная SAME-пара (receipt_i, hard-dup_i) РЕАЛЬНО существует по корпусу — но
                # сохранённое число относится к ДРУГОЙ паре (dup против чужого оригинала-победителя)
                same_hard_unmeasured.append({
                    "id": rid,
                    "cosine": None,
                    "bounded_above": row["mm_hard_cosine"],
                    "note": f"истинная SAME-пара (receipt_i={rid}, его hard-dup) существует по "
                             f"построению корпуса, но её cosine не сохранён исходным замером "
                             f"(near-dup retrieval сохраняет только argmax); известно лишь, что "
                             f"она МЕНЬШЕ {row['mm_hard_cosine']} — иначе поиск выбрал бы её, а "
                             f"не чужой документ {row['mm_hard_nearest']}. Новый вызов стенда "
                             f"для восстановления точного числа недоступен в этой сессии (нет "
                             f"доступа к credentials n8n) — значение не домысливается.",
                })
                # сам побочный результат — ОТДЕЛЬНАЯ, корректно размеченная DIFF-пара (dup документа
                # rid действительно сравнивался с действительно другим документом nearest) — её
                # истинность не зависит от того, выиграл ли её argmax; она просто есть
                diff_misfire.append({
                    "dup_of": rid,
                    "matched_instead": row["mm_hard_nearest"],
                    "cosine": row["mm_hard_cosine"],
                    "note": f"hard-dup документа {rid} (поворот 12°+обрезка 4%) оказался по cosine "
                             f"ближе к ЧУЖОМУ документу {row['mm_hard_nearest']}, чем к своему "
                             f"оригиналу — настоящая DIFF-пара независимо от разметки SAME.",
                })

    for row in part_c:
        if row.get("mm_cosine") is not None:
            diff_nearest_other.append({"id": row["id"], "nearest_other": row["mm_nearest"], "cosine": row["mm_cosine"]})

    assert len(same_soft) == 30
    assert len(same_hard_known) + len(same_hard_unmeasured) == 30, "истинных SAME-hard пар должно быть 30 — по одной на скан"
    assert len(diff_nearest_other) == 30

    return same_soft, same_hard_known, same_hard_unmeasured, diff_misfire, diff_nearest_other


def band_stats(same_vals, diff_vals, label, n_same_true_total, n_same_unmeasured):
    t_low = min(same_vals)
    t_high = max(diff_vals)
    n_total_known = len(same_vals) + len(diff_vals)
    n_total_true = n_same_true_total + len(diff_vals)
    if t_low > t_high:
        band = {
            "band_exists": False,
            "t_low": round(t_low, 4),
            "t_high": round(t_high, 4),
            "n_same_in_band": 0,
            "n_diff_in_band": 0,
        }
    else:
        same_in_band = [v for v in same_vals if t_low <= v <= t_high]
        diff_in_band = [v for v in diff_vals if t_low <= v <= t_high]
        band = {
            "band_exists": True,
            "t_low": round(t_low, 4),
            "t_high": round(t_high, 4),
            "n_same_in_band": len(same_in_band),
            "n_diff_in_band": len(diff_in_band),
            "same_values_in_band": sorted(same_in_band),
            "diff_values_in_band": sorted(diff_in_band),
        }
    return {
        "case": label,
        "n_total_pairs_with_known_cosine": n_total_known,
        "n_total_true_pairs_including_unmeasured": n_total_true,
        "n_same_unmeasured_excluded_from_numbers_above": n_same_unmeasured,
        "share_in_band_of_known": (round((band.get("n_same_in_band", 0) + band.get("n_diff_in_band", 0)) / n_total_known, 4)
                                    if band["band_exists"] else 0.0),
        **band,
    }


def threshold_tradeoff(same_vals, diff_vals, thresholds):
    rows = []
    for t in thresholds:
        fn = sum(1 for v in same_vals if v < t)
        fp = sum(1 for v in diff_vals if v >= t)
        rows.append({"threshold": round(t, 4), "false_non_match_FN": fn, "false_match_FP": fp, "fn_plus_fp": fn + fp})
    return rows


def run():
    d = load()
    same_soft, same_hard_known, same_hard_unmeasured, diff_misfire, diff_nearest_other = build_true_labeled_pairs(d)

    soft_vals = [r["cosine"] for r in same_soft]
    hard_known_vals = [r["cosine"] for r in same_hard_known]
    diff_vals_base = [r["cosine"] for r in diff_nearest_other]
    diff_vals_with_misfire = diff_vals_base + [r["cosine"] for r in diff_misfire]

    easy = band_stats(soft_vals, diff_vals_base, "лёгкий случай (soft-dup: пересжатие+resize)",
                       n_same_true_total=30, n_same_unmeasured=0)
    hard = band_stats(hard_known_vals, diff_vals_with_misfire, "трудный случай (hard-dup: поворот 12°+обрезка 4%)",
                       n_same_true_total=30, n_same_unmeasured=len(same_hard_unmeasured))

    hard_thresholds = sorted(set([hard["t_low"], hard["t_high"]] + [round(hard["t_low"] + 0.01 * i, 4)
                                                                     for i in range(1, int((hard["t_high"] - hard["t_low"]) * 100) + 1)]))
    tradeoff = threshold_tradeoff(hard_known_vals, diff_vals_with_misfire, hard_thresholds)

    out = {
        "purpose": "Пересборка band_analysis.json по ИСТИННЫМ меткам корпуса (issue #351, находка "
                   "этой сессии при подхвате после предшественника) — не по выдаче top-1, которая "
                   "была источником разметки в analyze_band.py. См. docstring этого файла и "
                   "README.md «Порок первой версии разметки».",
        "model": MM_MODEL,
        "source_measurement_date": "2026-11-04",
        "source_raw_file": "sem-10/stend/raw/case4_mm_full_retrieval.json",
        "new_stand_calls": 0,
        "new_stand_calls_note": "Попытка нового вызова для восстановления значения receipt_02 "
                                 "не предпринималась — доступ к credentials n8n в этой сессии "
                                 "заблокирован классификатором auto-mode; см. same_hard_unmeasured.",
        "n_corpus_scans": 30,
        "easy_case": easy,
        "hard_case": hard,
        "same_hard_unmeasured": same_hard_unmeasured,
        "diff_misfire_case_read_by_eye": diff_misfire,
        "threshold_tradeoff_hard_case": tradeoff,
        "raw_pairs": {
            "same_soft": same_soft,
            "same_hard_known": same_hard_known,
            "same_hard_unmeasured": same_hard_unmeasured,
            "diff_nearest_other": diff_nearest_other,
            "diff_misfire": diff_misfire,
        },
        "comparison_with_top1_biased_version": {
            "old_file": "raw/band_analysis.json (analyze_band.py)",
            "what_changed": "SAME-hard теперь ЯВНО 30 истинных пар (29 известных числом + 1 "
                            "помеченная «не замерено, <0,7547»), а не 29 без следа пропавшей. "
                            "Числа t_low/t_high/торговли порогом совпадают с прежними — пропавшее "
                            "значение и раньше не входило в расчёт, менялась только видимость "
                            "пропуска, не сами числа.",
            "why_old_version_understated_the_band": "Знаменатель доли «пар в полосе» у старой "
                            "версии — 60 известных (29+31), у истинной разметки — 61 истинная "
                            "пара (30+31), и ЕСЛИ пропавшее значение окажется внутри полосы "
                            "[0,7049; 0,7547] или ниже t_low, доля пар в полосе вырастет, а не "
                            "останется 11,7%. Старая версия не содержала ложного числа, но "
                            "создавала ложное ощущение полноты — ровно та находка, которую просил "
                            "задокументировать не выбрасывая.",
        },
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(json.dumps({"easy_case": easy, "hard_case": hard,
                       "same_hard_unmeasured": same_hard_unmeasured}, ensure_ascii=False, indent=2))
    print(f"\nзаписано: {OUT}")


if __name__ == "__main__":
    run()
