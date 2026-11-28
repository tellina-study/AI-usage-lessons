#!/usr/bin/env python3
"""Семинар 12, Кейс 1, Замер №1 — три варианта описания изображения (caption / поля /
гибрид) на 30 сканах CORD. 90 реальных vision-вызовов gpt-4o-mini через вебхук стенда
s10-raw-openrouter + эмбеддинги text-embedding-3-small для recall@1 вариантов
caption/гибрид. Корпус — library/seminars/sem-10/stend/corpus/ (готовый, read-only).

Запуск:
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    cd library/seminars/sem-12/stend/zamery-k1
    python3 measure_case1_descriptions.py
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from harness2_lite import (
    CHAT_MODEL, EMBED_MODEL, cosine, embed_batch, extract_json, parse_amount,
    to_data_url, vision_call, word_count,
)

HERE = Path(__file__).resolve().parent
STEND_DIR = HERE.parent.parent.parent / "sem-10" / "stend"
CORPUS_DIR = STEND_DIR / "corpus"
META_PATH = CORPUS_DIR / "cord_sample_meta.json"
OUT_PATH = HERE / "raw" / "descriptions_results.json"

SYS_CAPTION = (
    "Ты — система автоматической подписи изображений для фотобанка/поискового архива. "
    "Опиши это изображение связно, одним абзацем (3-6 предложений), как для карточки "
    "фотобанка: что это за документ/сцена, какие важные детали видны, какой текст и "
    "суммы заметны. Пиши связный текст, БЕЗ JSON, БЕЗ списков, БЕЗ заголовков — только "
    "один абзац."
)
USER_CAPTION = "Опиши это изображение одним связным абзацем."

SYS_FIELDS = (
    "Ты — система автоматического тегирования документов для поискового архива. "
    "Проанализируй изображение и верни СТРОГО валидный JSON-объект (без markdown-"
    "ограждения ```, без пояснений до или после — только сам JSON) с полями:\n"
    '- "scene_type" (строка): тип сцены/документа, например "чек", "квитанция", '
    '"фото людей" и т.п.\n'
    '- "has_text" (bool): есть ли на изображении видимый текст\n'
    '- "personal_data_present" (bool): есть ли видимые персональные или платёжные '
    "данные (номер карты, ФИО, подпись, телефон)\n"
    '- "image_quality" (строка): одно из "чёткое", "смазанное", "тёмное"\n'
    '- "key_amount" (строка): ГЛАВНАЯ (итоговая) денежная сумма документа, как она '
    "написана на документе, например итоговая сумма чека (поле TOTAL/GRAND TOTAL)\n"
    '- "item_count" (целое число): число позиций/строк товара в чеке (посчитай строки '
    "меню; если не применимо — 0)\n"
    "Верни ТОЛЬКО JSON-объект с этими 6 полями и больше ничего."
)
USER_FIELDS = "Заполни поля по схеме для этого изображения."

SYS_HYBRID = SYS_FIELDS.replace(
    "Верни ТОЛЬКО JSON-объект с этими 6 полями и больше ничего.",
    '- "semantic_phrase" (строка): ОДНА свободная фраза (не абзац!) для смыслового '
    'поиска по архиву, например "чек из кафе с оплатой картой и большой скидкой".\n'
    "Верни ТОЛЬКО JSON-объект с этими 7 полями и больше ничего.",
)
USER_HYBRID = USER_FIELDS

VARIANTS = ["caption", "fields", "hybrid"]

# --- Запросы recall@1 (построены и проверены на уникальность по meta.json, см. README) ---
QUERIES = {
    "light_1_max_total": {
        "group": "light",
        "text": "Какой чек (документ) имеет наибольшую итоговую сумму (TOTAL)?",
        "gold": "receipt_28",
        "field": "key_amount",
        "rank": "max",
    },
    "light_2_min_total": {
        "group": "light",
        "text": "Какой чек (документ) имеет наименьшую итоговую сумму (TOTAL)?",
        "gold": "receipt_03",
        "field": "key_amount",
        "rank": "min",
    },
    "hard_1_item_count_5": {
        "group": "hard",
        "text": "В каком чеке ровно 5 позиций товара (строк меню)?",
        "gold": "receipt_20",
        "field": "item_count",
        "rank": "equals",
        "value": 5,
    },
    "hard_2_tax_range": {
        "group": "hard",
        "text": (
            "В каком чеке сумма налога (отдельная строка налога/TAX/PB1, НЕ итоговая "
            "сумма чека) — от 12 500 до 14 000?"
        ),
        "gold": "receipt_29",
        "field": None,  # сознательно: в схеме поля «поля» НЕТ поля под налог
        "rank": "schema_blind_spot",
    },
}


def call_one(rid, path, variant):
    img = to_data_url(str(path))
    sys_p, user_p = {
        "caption": (SYS_CAPTION, USER_CAPTION),
        "fields": (SYS_FIELDS, USER_FIELDS),
        "hybrid": (SYS_HYBRID, USER_HYBRID),
    }[variant]
    r = vision_call(sys_p, user_p, img)
    r["id"] = rid
    r["variant"] = variant
    return r


def main():
    meta = json.load(open(META_PATH, encoding="utf-8"))
    print(f"Корпус: {len(meta)} сканов из {META_PATH}")

    jobs = []
    for s in meta:
        rid = s["id"]
        path = STEND_DIR / s["file"]  # s["file"] вида "corpus/cord_sample/receipt_00.jpg"
        for variant in VARIANTS:
            jobs.append((rid, path, variant))

    print(f"Всего vision-вызовов: {len(jobs)}")
    results = []
    t_start = time.time()
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(call_one, rid, path, variant): (rid, variant) for rid, path, variant in jobs}
        done = 0
        for fut in as_completed(futs):
            rid, variant = futs[fut]
            try:
                r = fut.result()
            except Exception as e:
                r = {"id": rid, "variant": variant, "content": None, "error": str(e)}
            results.append(r)
            done += 1
            if done % 10 == 0:
                print(f"  ... {done}/{len(jobs)} готово ({time.time()-t_start:.0f}с)")

    print(f"Все vision-вызовы заняты {time.time()-t_start:.1f}с")

    # --- парсинг + длины ---
    by_id_variant = {}
    for r in results:
        rid, variant = r["id"], r["variant"]
        content = r.get("content")
        parsed = None
        if variant in ("fields", "hybrid"):
            parsed = extract_json(content)
        entry = {
            "exec_id": r.get("exec_id"), "wall_s": r.get("wall_s"), "node_ms": r.get("node_ms"),
            "prompt_tokens": r.get("prompt_tokens"), "completion_tokens": r.get("completion_tokens"),
            "cost": r.get("cost"), "raw_content": content, "parsed": parsed,
        }
        if variant == "caption":
            entry["text_for_embedding"] = content or ""
            entry["len_chars"] = len(content) if content else 0
            entry["len_words"] = word_count(content)
        else:
            compact = json.dumps(parsed, ensure_ascii=False, separators=(",", ":")) if parsed else (content or "")
            entry["len_chars"] = len(compact)
            entry["len_words"] = word_count(compact)
            if variant == "hybrid":
                entry["text_for_embedding"] = (parsed or {}).get("semantic_phrase", "") if parsed else ""
        by_id_variant[(rid, variant)] = entry

    ids = [s["id"] for s in meta]

    # --- эмбеддинги для caption и hybrid(semantic_phrase) ---
    caption_texts = [by_id_variant[(rid, "caption")]["text_for_embedding"] or "(нет описания)" for rid in ids]
    hybrid_texts = [by_id_variant[(rid, "hybrid")]["text_for_embedding"] or "(нет фразы)" for rid in ids]
    query_texts = [q["text"] for q in QUERIES.values()]

    print("Эмбеддинги: caption x30, hybrid-phrase x30, запросы x4 ...")
    caption_vecs, cap_usage = embed_batch(caption_texts)
    hybrid_vecs, hyb_usage = embed_batch(hybrid_texts)
    query_vecs, q_usage = embed_batch(query_texts)
    print("готово:", cap_usage, hyb_usage, q_usage)

    query_vec_by_name = dict(zip(QUERIES.keys(), query_vecs))

    # --- recall@1 ---
    recall = {v: {} for v in VARIANTS}
    recall_detail = {v: {} for v in VARIANTS}

    for qname, q in QUERIES.items():
        gold = q["gold"]

        # variant: fields
        if q["field"] is None:
            recall["fields"][qname] = 0
            recall_detail["fields"][qname] = {"note": "в схеме «поля» нет поля под этот факт — структурно не отвечаем (0), не ошибка модели"}
        else:
            vals = {}
            for rid in ids:
                parsed = by_id_variant[(rid, "fields")]["parsed"] or {}
                raw_v = parsed.get(q["field"])
                if q["field"] == "key_amount":
                    vals[rid] = parse_amount(raw_v)
                else:
                    try:
                        vals[rid] = int(raw_v) if raw_v is not None else None
                    except Exception:
                        vals[rid] = parse_amount(raw_v)
            valid = {k: v for k, v in vals.items() if v is not None}
            if q["rank"] == "max":
                top1 = max(valid, key=lambda k: (valid[k], -ids.index(k))) if valid else None
            elif q["rank"] == "min":
                top1 = min(valid, key=lambda k: (valid[k], ids.index(k))) if valid else None
            elif q["rank"] == "equals":
                matches = sorted([k for k, v in valid.items() if v == q["value"]])
                top1 = matches[0] if matches else None  # детерминированный tie-break: наименьший id
            else:
                top1 = None
            recall["fields"][qname] = 1 if top1 == gold else 0
            recall_detail["fields"][qname] = {"predicted_values": vals, "top1": top1, "gold": gold}

        # variant: caption (эмбеддинг)
        qv = query_vec_by_name[qname]
        sims_cap = {rid: cosine(qv, caption_vecs[i]) for i, rid in enumerate(ids)}
        top1_cap = max(sims_cap, key=sims_cap.get)
        recall["caption"][qname] = 1 if top1_cap == gold else 0
        recall_detail["caption"][qname] = {"top1": top1_cap, "gold": gold, "cos_top1": sims_cap[top1_cap], "cos_gold": sims_cap.get(gold)}

        # variant: hybrid (эмбеддинг semantic_phrase)
        sims_hyb = {rid: cosine(qv, hybrid_vecs[i]) for i, rid in enumerate(ids)}
        top1_hyb = max(sims_hyb, key=sims_hyb.get)
        recall["hybrid"][qname] = 1 if top1_hyb == gold else 0
        recall_detail["hybrid"][qname] = {"top1": top1_hyb, "gold": gold, "cos_top1": sims_hyb[top1_hyb], "cos_gold": sims_hyb.get(gold)}

    # --- агрегаты длины/цены по вариантам ---
    summary = {}
    for variant in VARIANTS:
        entries = [by_id_variant[(rid, variant)] for rid in ids]
        costs = [e["cost"] for e in entries if e["cost"] is not None]
        words = [e["len_words"] for e in entries]
        chars = [e["len_chars"] for e in entries]
        pt = [e["prompt_tokens"] for e in entries if e["prompt_tokens"] is not None]
        ct = [e["completion_tokens"] for e in entries if e["completion_tokens"] is not None]
        summary[variant] = {
            "n": len(entries),
            "avg_cost_per_call": sum(costs) / len(costs) if costs else None,
            "cost_per_1000_images": (sum(costs) / len(costs) * 1000) if costs else None,
            "avg_words": sum(words) / len(words) if words else None,
            "avg_chars": sum(chars) / len(chars) if chars else None,
            "avg_prompt_tokens": sum(pt) / len(pt) if pt else None,
            "avg_completion_tokens": sum(ct) / len(ct) if ct else None,
            "recall_light": {k: v for k, v in recall[variant].items() if QUERIES[k]["group"] == "light"},
            "recall_hard": {k: v for k, v in recall[variant].items() if QUERIES[k]["group"] == "hard"},
            "recall_light_avg": sum(v for k, v in recall[variant].items() if QUERIES[k]["group"] == "light") / sum(1 for k in QUERIES if QUERIES[k]["group"] == "light"),
            "recall_hard_avg": sum(v for k, v in recall[variant].items() if QUERIES[k]["group"] == "hard") / sum(1 for k in QUERIES if QUERIES[k]["group"] == "hard"),
        }

    out = {
        "model": CHAT_MODEL,
        "embed_model": EMBED_MODEL,
        "n_images": len(ids),
        "variants": VARIANTS,
        "queries": QUERIES,
        "summary": summary,
        "recall_detail": recall_detail,
        "per_call": {f"{rid}|{variant}": by_id_variant[(rid, variant)] for rid in ids for variant in VARIANTS},
        "embed_usage": {"caption": cap_usage, "hybrid": hyb_usage, "queries": q_usage},
        "total_wall_s": round(time.time() - t_start, 1),
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Записано: {OUT_PATH}")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
