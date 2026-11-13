#!/usr/bin/env python3
"""Сводит два прогона `case4_quality_limits.py` (--engine api и --engine clip) в один
канонический файл ../raw/case4_quality_limits.json. Ничего не измеряет сам — только
сводит, считает базы и выписывает границу по каждой оси.

Граница оси определяется механически и одинаково для всех осей: первая точка, на
которой recall@1 падает НИЖЕ опорного, и первая, на которой он падает ниже половины
опорного. Так «где граница» — вычисленное из данных число, а не выбранное глазами.
"""
import json
import sys

AXIS_RU = {"compression": "сжатие (качество JPEG)",
           "resolution": "разрешение запроса",
           "quality": "качество (размытие по Гауссу)"}
DUP_RU = {"soft_dup": "мягкий дубль (пересканировали)",
          "hard_dup": "жёсткий дубль (сняли под углом, поворот 12° + обрезка 4%)"}


def boundary(points, labels):
    """Первое падение ниже опоры и первое падение ниже половины опоры."""
    anchor = points[labels[0]]["summary"]["recall_at_1"]
    first_drop, first_half, first_neg_margin = None, None, None
    for L in labels:
        s = points[L]["summary"]
        r, m = s["recall_at_1"], s.get("margin")
        if r is None:
            continue
        if first_drop is None and anchor is not None and r < anchor:
            first_drop = L
        if first_half is None and anchor and r < anchor / 2:
            first_half = L
        if first_neg_margin is None and m is not None and m <= 0:
            first_neg_margin = L
    return {"anchor_recall_at_1": anchor,
            "first_point_below_anchor": first_drop,
            "first_point_below_half_anchor": first_half,
            "first_point_with_nonpositive_margin": first_neg_margin}


def main():
    runs = {}
    for eng in ("api", "clip"):
        try:
            runs[eng] = json.load(open(f"case4_quality_limits_{eng}_raw.json"))
        except FileNotFoundError:
            print(f"!! нет прогона {eng} — сводка будет без него", file=sys.stderr)

    if "api" not in runs:
        print("!! нет прогона api — это основной счётчик, сводка не имеет смысла", file=sys.stderr)
        sys.exit(1)

    api = runs["api"]
    axes_out = {}
    for axis, labels in api["axes"].items():
        per_dup = {}
        for dup in ("hard_dup", "soft_dup"):
            if dup not in api["results"]:
                continue
            engines = {}
            for eng, run in runs.items():
                if dup not in run["results"]:
                    continue
                pts = run["results"][dup]
                if not all(L in pts for L in labels):
                    continue
                engines[eng] = {
                    "model": run["model"],
                    "boundary": boundary(pts, labels),
                    "points": {L: pts[L]["summary"] for L in labels},
                    "per_scan_details": {L: pts[L]["details"] for L in labels},
                }
            # отпечаток берём из api-прогона (считается локально, в обоих одинаков)
            if dup in api["results"]:
                pts = api["results"][dup]
                engines["phash"] = {
                    "model": "average-hash 8×8 (perceptual hash, без модели)",
                    "boundary": {"anchor_recall_at_1": pts[labels[0]]["summary"]["phash_recall_at_1"],
                                 "note": "граница по этим трём осям не достигается — см. headline"},
                    "points": {L: {"phash_recall_at_1": pts[L]["summary"]["phash_recall_at_1"],
                                   "phash_mean_hamming_to_own": pts[L]["summary"]["phash_mean_hamming_to_own"],
                                   "mean_b64_chars": pts[L]["summary"]["mean_b64_chars"],
                                   "b64_chars_share_of_anchor": pts[L]["summary"].get("b64_chars_share_of_anchor")}
                               for L in labels},
                }
            per_dup[dup] = {"task": DUP_RU[dup], "engines": engines}
        axes_out[axis] = {"axis": AXIS_RU[axis], "point_labels": labels,
                          "point_render_params": {L: api["points"][L] for L in labels},
                          "tasks": per_dup}

    out = {
        "purpose": "Кейс 4 (issue #311), прямой вопрос владельца курса — «показать границы "
                   "применимости по сжатию/размерам, качеству». До этого прохода таких данных "
                   "у кейса не было: раздел про разрешение мерил БИТУЮ модель "
                   "(amazon/titan-embed-image-v1, cosine=1,0 на любых двух картинках, "
                   "raw/case4_resolution_probe.json), а полный замер рабочей модели "
                   "(raw/case4_mm_full_retrieval.json) снят в ОДНОЙ точке качества.",
        "verified_at": api.get("verified_at"),
        "method": {
            "index_does_NOT_degrade": "Все 30 оригиналов CORD лежат в индексе в ОПОРНОМ виде "
                "300×450 JPEG q80 — ровно том, с которым работает весь Кейс 4. Деградирует "
                "ТОЛЬКО картинка-запрос. Это реалистичный случай: в заявке приходит "
                "пережатое/мелкое/смазанное фото, а в хранилище лежит нормальный скан. "
                "Обратный случай (деградировал индекс) этим замером НЕ покрыт.",
            "query": "Дубль того же чека, построенный ДЕТЕРМИНИРОВАННО (без random) теми же "
                "преобразованиями, что в measure/case4_full_retrieval_30.py: мягкий дубль — "
                "resize×0,97 → целевой размер; жёсткий — поворот 12° + обрезка 4% краёв → "
                "целевой размер. Геометрия не менялась; добавлены параметры рендера "
                "(размер, качество JPEG, радиус размытия).",
            "axes": "Три оси, по четыре точки, ПЕРВАЯ ТОЧКА ОПОРНАЯ И ОДНА И ТА ЖЕ для всех "
                "трёх осей (300×450 q80 без размытия) — не три разных рендера.",
            "metrics": "recall@1 (ближайший из 30 оригиналов — тот же чек?), среднее косинусное "
                "сходство с ВЕРНЫМ оригиналом, среднее с ближайшим НЕВЕРНЫМ, запас между ними "
                "(margin), средний размер строки base64 и его доля от опорной точки.",
            "boundary_rule": "Граница оси вычислена механически: первая точка ниже опорного "
                "recall@1, первая ниже половины опорного, первая с margin ≤ 0.",
            "phash_index_note": "Отпечаток индекса считается на ПОЛНОМ файле оригинала "
                "(как в case4_full_retrieval_30.py), а average-hash сам сводит картинку к 8×8 — "
                "поэтому отпечаток СТРУКТУРНО почти безразличен к сжатию/разрешению/размытию. "
                "Это свойство метода, а не неожиданная эмпирическая победа.",
            "shared_stand_caveat": "Во время прогона тот же вебхук s10-raw-openrouter "
                "использовала параллельная сессия (замерено: до ~4,6 запуска в секунду на том же "
                "сценарии). На recall/cosine это не влияет (они детерминированы при заданной "
                "модели и входе), но mean_embed_s — задержка ПОД КОНКУРЕНЦИЕЙ, не чистый бенчмарк.",
        },
        "engines": {eng: {"model": r["model"], "embedding_dim": r["embedding_dim"],
                          "kind": ("API через вебхук s10-raw-openrouter (ключ OpenRouter "
                                   "остаётся на стороне n8n)" if eng == "api"
                                   else "локально, CPU, бесплатно")}
                    for eng, r in runs.items()},
        "index": api["index"],
        "axes": axes_out,
        "fail_log": {eng: r["fail_log"] for eng, r in runs.items()},
        "timing": {eng: r["timing"] for eng, r in runs.items()},
    }
    json.dump(out, open("../raw/case4_quality_limits.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("записано ../raw/case4_quality_limits.json")
    # печать сводки для глаз
    for axis, blob in axes_out.items():
        print(f"\n===== {blob['axis']} =====")
        for dup, d in blob["tasks"].items():
            print(f"  -- {d['task']}")
            for eng, e in d["engines"].items():
                if eng == "phash":
                    rs = [e["points"][L]["phash_recall_at_1"] for L in blob["point_labels"]]
                else:
                    rs = [e["points"][L]["recall_at_1"] for L in blob["point_labels"]]
                print(f"     {eng:6s} recall@1 по точкам: {rs}  граница: "
                      f"{e['boundary'].get('first_point_below_anchor')}")


if __name__ == "__main__":
    main()
