#!/usr/bin/env python3
"""Семинар 12, Кейс 1, Замер №1 — ДОПОЛНЕНИЕ 2026-11-21 (по требованию владельца через
оркестратора): расширение набора ЛЁГКИХ запросов recall@1 с 2 до 16 (+1 трудный) БЕЗ
повторных vision-вызовов. Подписи/поля/гибрид-фразы уже сгенерированы в Замере №1
(`raw/descriptions_results.json`, 90 реальных вызовов gpt-4o-mini) — они не зависят от
того, какие запросы к ним потом задают, поэтому перегенерировать их незачем (дешевле и
честнее переиспользовать). Единственные НОВЫЕ реальные вызовы здесь — эмбеддинги текста
запросов + повторное вычисление эмбеддингов caption/semantic_phrase (те же тексты, что
были, эмбеддинги просто не сохранялись как векторы в прошлый раз — только usage).

Запуск:
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    cd library/seminars/sem-12/stend/zamery-k1
    python3 rescan_case1_queries.py
"""
import json
import re
from pathlib import Path

from harness2_lite import cosine, embed_batch, parse_amount

HERE = Path(__file__).resolve().parent
IN_PATH = HERE / "raw" / "descriptions_results.json"
OUT_PATH = HERE / "raw" / "case1_light_expanded_recall.json"

# --- Расширенный набор запросов. Методологическая оговорка (факт, не извинение, С9):
# все 16 ЛЁГКИХ запросов построены на поле key_amount (итоговая сумма) — это не сужение
# замера, а свойство корпуса: в схеме «поля» только 2 числовых поля (key_amount,
# item_count); item_count в этом корпусе 30 чеков имеет РОВНО ОДНО уникальное значение
# (5 позиций, receipt_20 — уже используется как трудный запрос, искать второй уникальный
# item_count-запрос в этом корпусе физически не из чего, гистограмма {1:10,2:9,3:7,5:1,
# 6:3}); дат в gt_parse нет вовсе; scene_type/валюта не различаются (все 30 — чеки в
# рупиях). Поэтому диверсификация набора идёт НЕ по типу поля (другого богатого числового
# поля в корпусе и схеме нет), а по ФОРМЕ вопроса к тому же полю: абсолютный ранг
# (1-е/2-е/3-е место сверху и снизу), диапазон (узкий интервал с одним попаданием),
# «ближе всего к X» (минимальное расстояние с чётким отрывом от второго места) — так
# набор проверяет recall на РАЗНЫХ типах рассуждения над одним полем, не 16 копий одного
# вопроса с разными числами.
QUERIES = {
    # --- исходные 2 (без изменений) ---
    "light_1_max_total": {"text": "Какой чек (документ) имеет наибольшую итоговую сумму (TOTAL)?", "gold": "receipt_28"},
    "light_2_min_total": {"text": "Какой чек (документ) имеет наименьшую итоговую сумму (TOTAL)?", "gold": "receipt_03"},
    # --- новые: ранги 2-е/3-е место ---
    "light_3_2nd_max_total": {"text": "Какой чек имеет ВТОРУЮ по величине итоговую сумму (не самую большую, а следующую за ней)?", "gold": "receipt_20"},
    "light_4_2nd_min_total": {"text": "Какой чек имеет ВТОРУЮ по малости итоговую сумму (не самую маленькую, а следующую за ней)?", "gold": "receipt_10"},
    "light_5_3rd_max_total": {"text": "Какой чек имеет ТРЕТЬЮ по величине итоговую сумму?", "gold": "receipt_14"},
    "light_6_3rd_min_total": {"text": "Какой чек имеет ТРЕТЬЮ по малости итоговую сумму?", "gold": "receipt_02"},
    # --- новые: узкий диапазон ---
    "light_7_range_175500_180000": {"text": "В каком чеке итоговая сумма — от 175 500 до 180 000?", "gold": "receipt_19"},
    "light_8_range_150000_160000": {"text": "В каком чеке итоговая сумма — от 150 000 до 160 000?", "gold": "receipt_18"},
    "light_9_range_135000_140000": {"text": "В каком чеке итоговая сумма — от 135 000 до 140 000?", "gold": "receipt_26"},
    "light_10_range_119500_121000": {"text": "В каком чеке итоговая сумма — от 119 500 до 121 000?", "gold": "receipt_12"},
    # --- новые: «ближе всего к X» ---
    "light_11_closest_58000": {"text": "У какого чека итоговая сумма БЛИЖЕ ВСЕГО к 58 000 (не обязательно равна)?", "gold": "receipt_00"},
    "light_12_closest_45000": {"text": "У какого чека итоговая сумма БЛИЖЕ ВСЕГО к 45 000?", "gold": "receipt_06"},
    "light_13_closest_35000": {"text": "У какого чека итоговая сумма БЛИЖЕ ВСЕГО к 35 000?", "gold": "receipt_09"},
    "light_14_closest_62000": {"text": "У какого чека итоговая сумма БЛИЖЕ ВСЕГО к 62 000?", "gold": "receipt_27"},
    "light_15_closest_147000": {"text": "У какого чека итоговая сумма БЛИЖЕ ВСЕГО к 147 000?", "gold": "receipt_29"},
    "light_16_closest_71000": {"text": "У какого чека итоговая сумма БЛИЖЕ ВСЕГО к 71 000?", "gold": "receipt_16"},
}
LIGHT_KEYS = list(QUERIES.keys())

HARD_QUERIES = {
    "hard_1_item_count_5": {"text": "В каком чеке ровно 5 позиций товара (строк меню)?", "gold": "receipt_20", "field": "item_count", "mode": "equals", "value": 5},
    "hard_2_tax_range": {"text": "В каком чеке сумма налога (отдельная строка TAX/PB1, НЕ итоговая сумма чека) — от 12 500 до 14 000?", "gold": "receipt_29", "field": None},
    "hard_3_negative_discount": {"text": "В каком чеке была применена скидка (отрицательное значение в строке скидки/discount)?", "gold": "receipt_00", "field": None},
}


def rank_value_for_query(qname, vals_by_id, ids):
    """Определяет top-1 по варианту «поля» для каждого ЛЁГКОГО запроса (все — key_amount)."""
    valid = {k: v for k, v in vals_by_id.items() if v is not None}
    if not valid:
        return None
    if qname == "light_1_max_total":
        return max(valid, key=lambda k: (valid[k], -ids.index(k)))
    if qname == "light_2_min_total":
        return min(valid, key=lambda k: (valid[k], ids.index(k)))
    if qname == "light_3_2nd_max_total":
        order = sorted(valid, key=lambda k: valid[k], reverse=True)
        return order[1] if len(order) > 1 else None
    if qname == "light_4_2nd_min_total":
        order = sorted(valid, key=lambda k: valid[k])
        return order[1] if len(order) > 1 else None
    if qname == "light_5_3rd_max_total":
        order = sorted(valid, key=lambda k: valid[k], reverse=True)
        return order[2] if len(order) > 2 else None
    if qname == "light_6_3rd_min_total":
        order = sorted(valid, key=lambda k: valid[k])
        return order[2] if len(order) > 2 else None
    if qname.startswith("light_7") or qname.startswith("light_8") or qname.startswith("light_9") or qname.startswith("light_10"):
        bounds = {
            "light_7_range_175500_180000": (175500, 180000),
            "light_8_range_150000_160000": (150000, 160000),
            "light_9_range_135000_140000": (135000, 140000),
            "light_10_range_119500_121000": (119500, 121000),
        }[qname]
        lo, hi = bounds
        matches = sorted([k for k, v in valid.items() if lo <= v <= hi])
        return matches[0] if matches else None
    if qname.startswith("light_11") or qname.startswith("light_12") or qname.startswith("light_13") or qname.startswith("light_14") or qname.startswith("light_15") or qname.startswith("light_16"):
        target = {
            "light_11_closest_58000": 58000, "light_12_closest_45000": 45000,
            "light_13_closest_35000": 35000, "light_14_closest_62000": 62000,
            "light_15_closest_147000": 147000, "light_16_closest_71000": 71000,
        }[qname]
        return min(valid, key=lambda k: (abs(valid[k] - target), ids.index(k)))
    return None


def main():
    data = json.load(open(IN_PATH, encoding="utf-8"))
    per_call = data["per_call"]
    ids = sorted({k.split("|")[0] for k in per_call.keys()})

    caption_texts = [per_call[f"{rid}|caption"]["text_for_embedding"] or "(нет описания)" for rid in ids]
    hybrid_texts = [per_call[f"{rid}|hybrid"]["text_for_embedding"] or "(нет фразы)" for rid in ids]

    all_query_texts = [q["text"] for q in QUERIES.values()] + [q["text"] for q in HARD_QUERIES.values()]
    all_query_names = list(QUERIES.keys()) + list(HARD_QUERIES.keys())

    print(f"Переэмбеддинг: caption x{len(ids)}, hybrid x{len(ids)}, запросы x{len(all_query_texts)} "
          f"(0 новых vision-вызовов, 3 новых embed-вызова)")
    caption_vecs, cap_usage = embed_batch(caption_texts)
    hybrid_vecs, hyb_usage = embed_batch(hybrid_texts)
    query_vecs, q_usage = embed_batch(all_query_texts)
    qvec = dict(zip(all_query_names, query_vecs))

    # --- значения key_amount/item_count по варианту "fields", взятые из УЖЕ СУЩЕСТВУЮЩИХ ответов ---
    key_amount_vals = {rid: parse_amount((per_call[f"{rid}|fields"]["parsed"] or {}).get("key_amount")) for rid in ids}
    item_count_vals = {}
    for rid in ids:
        raw = (per_call[f"{rid}|fields"]["parsed"] or {}).get("item_count")
        try:
            item_count_vals[rid] = int(raw) if raw is not None else None
        except Exception:
            item_count_vals[rid] = parse_amount(raw)

    recall = {"fields": {}, "caption": {}, "hybrid": {}}
    detail = {"fields": {}, "caption": {}, "hybrid": {}}

    for qname, q in QUERIES.items():
        gold = q["gold"]
        top1_fields = rank_value_for_query(qname, key_amount_vals, ids)
        recall["fields"][qname] = 1 if top1_fields == gold else 0
        detail["fields"][qname] = {"top1": top1_fields, "gold": gold}

        qv = qvec[qname]
        sims_cap = {rid: cosine(qv, caption_vecs[i]) for i, rid in enumerate(ids)}
        top1_cap = max(sims_cap, key=sims_cap.get)
        recall["caption"][qname] = 1 if top1_cap == gold else 0
        detail["caption"][qname] = {"top1": top1_cap, "gold": gold, "cos_top1": sims_cap[top1_cap], "cos_gold": sims_cap.get(gold)}

        sims_hyb = {rid: cosine(qv, hybrid_vecs[i]) for i, rid in enumerate(ids)}
        top1_hyb = max(sims_hyb, key=sims_hyb.get)
        recall["hybrid"][qname] = 1 if top1_hyb == gold else 0
        detail["hybrid"][qname] = {"top1": top1_hyb, "gold": gold, "cos_top1": sims_hyb[top1_hyb], "cos_gold": sims_hyb.get(gold)}

    for qname, q in HARD_QUERIES.items():
        gold = q["gold"]
        if qname == "hard_1_item_count_5":
            matches = sorted([k for k, v in item_count_vals.items() if v == q["value"]])
            top1_fields = matches[0] if matches else None
            note = None
        else:
            top1_fields = None
            note = "в схеме «поля» нет поля под этот факт — структурно не отвечаем (0), не ошибка модели"
        recall["fields"][qname] = 1 if top1_fields == gold else 0
        detail["fields"][qname] = {"top1": top1_fields, "gold": gold, "note": note}

        qv = qvec[qname]
        sims_cap = {rid: cosine(qv, caption_vecs[i]) for i, rid in enumerate(ids)}
        top1_cap = max(sims_cap, key=sims_cap.get)
        recall["caption"][qname] = 1 if top1_cap == gold else 0
        detail["caption"][qname] = {"top1": top1_cap, "gold": gold, "cos_top1": sims_cap[top1_cap], "cos_gold": sims_cap.get(gold)}

        sims_hyb = {rid: cosine(qv, hybrid_vecs[i]) for i, rid in enumerate(ids)}
        top1_hyb = max(sims_hyb, key=sims_hyb.get)
        recall["hybrid"][qname] = 1 if top1_hyb == gold else 0
        detail["hybrid"][qname] = {"top1": top1_hyb, "gold": gold, "cos_top1": sims_hyb[top1_hyb], "cos_gold": sims_hyb.get(gold)}

    summary = {}
    for variant in ("fields", "caption", "hybrid"):
        light_vals = [recall[variant][k] for k in LIGHT_KEYS]
        hard_vals = [recall[variant][k] for k in HARD_QUERIES.keys()]
        summary[variant] = {
            "n_light": len(light_vals), "light_correct": sum(light_vals),
            "recall_light_avg": sum(light_vals) / len(light_vals),
            "n_hard": len(hard_vals), "hard_correct": sum(hard_vals),
            "recall_hard_avg": sum(hard_vals) / len(hard_vals),
            "light_per_query": {k: recall[variant][k] for k in LIGHT_KEYS},
            "hard_per_query": {k: recall[variant][k] for k in HARD_QUERIES.keys()},
        }

    out = {
        "note": "Дополнение 2026-11-21 к Замеру №1 — расширенный набор лёгких запросов "
                "(2 -> 16), переиспользует 90 vision-вызовов из descriptions_results.json, "
                "0 новых vision-вызовов, только переэмбеддинг (3 батч-вызова).",
        "queries_light": QUERIES, "queries_hard": HARD_QUERIES,
        "summary": summary, "detail": detail,
        "embed_usage": {"caption": cap_usage, "hybrid": hyb_usage, "queries": q_usage},
        "key_amount_predicted": key_amount_vals, "item_count_predicted": item_count_vals,
    }
    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Записано: {OUT_PATH}")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
