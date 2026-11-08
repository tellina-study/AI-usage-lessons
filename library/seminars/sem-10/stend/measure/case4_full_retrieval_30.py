#!/usr/bin/env python3
"""Кейс 4 (issue #311) — полный замер retrieval по ВСЕМ 30 сканам CORD, двумя частями:

(A) Near-duplicate retrieval (имитация повторного скана/фото того же чека, мягкая и
    жёсткая аугментация — ТА ЖЕ методика, что уже пилотировалась на случайных 6 из 30
    в case4_measure.py::near_duplicate_injection_test, здесь — расширена на ВСЕ 30, не
    выборку): для каждого из 30 чеков строим soft-dup и hard-dup, ищем ближайший ОРИГИНАЛ
    среди всех 30 по эмбеддингу/отпечатку, recall@1 = доля верных попаданий. Это даёт
    recall@1-метрику в том же духе, что case1_measure.py (query -> nearest -> correct?),
    для:
      - рабочей мультимодальной модели, найденной case4_find_working_mm.py +
        case4_rank_candidates2.py (nvidia/nemotron-3.5-embed-1b:free — наибольший margin
        same-doc-near-dup vs diff-doc среди 8 кандидатов, различающих изображения, и это
        free-tier модель);
      - perceptual hash (классика, уже "рабочая" часть решения владельца, n66);
      - текстового эмбеддинга OCR — ТРИВИАЛЬНО для этого теста (эталонный OCR CORD не
        меняется аугментацией картинки, см. методологическая оговорка case4_measure.py) —
        посчитан и показан как контроль/нижняя граница метода, не как честный тест текста.

(B) Семантическое разделение текста по содержанию (качественный вывод part (а) из
    case4_measure.py "эмбеддинги содержательно различаются" — здесь получает число):
    пара "вопрос по содержанию чека" (построен из gt_parse.menu.nm — название позиции,
    есть не у всех чеков) -> к какому чеку он относится реально -> recall@1 текстового
    поиска среди ВСЕХ 30 OCR-текстов. Честный тест (вопрос не повторяет OCR слово в
    слово — только название позиции, остальное из OCR не раскрывается).
"""
import base64
import io
import json
import random
import time

from PIL import Image

from harness_call import call_raw

MM_MODEL = "nvidia/nemotron-3.5-embed-1b:free"
TEXT_MODEL = "openai/text-embedding-3-small"

samples = json.load(open("../corpus/cord_sample_meta.json"))
ids = [s["id"] for s in samples]
paths = {s["id"]: f"../{s['file']}" for s in samples}


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


def to_data_url(path, w=300, h=450, q=80):
    im = Image.open(path).convert("RGB").resize((w, h))
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=q)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


def soft_dup(path, w=300, h=450):
    im = Image.open(path).convert("RGB")
    soft = im.resize((max(1, int(im.width * 0.97)), max(1, int(im.height * 0.97)))).resize((w, h))
    buf = io.BytesIO()
    soft.save(buf, format="JPEG", quality=60)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


def hard_dup(path, w=300, h=450):
    im = Image.open(path).convert("RGB")
    hard = im.rotate(12, expand=True, fillcolor=(255, 255, 255))
    ww, hh = hard.size
    hard = hard.crop((int(ww * 0.04), int(hh * 0.04), int(ww * 0.96), int(hh * 0.96)))
    hard = hard.resize((w, h))
    buf = io.BytesIO()
    hard.save(buf, format="JPEG", quality=80)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


def average_hash(pil_im, hash_size=8):
    im = pil_im.convert("L").resize((hash_size, hash_size), Image.LANCZOS)
    pixels = list(im.getdata())
    avg = sum(pixels) / len(pixels)
    return "".join("1" if p > avg else "0" for p in pixels)


def hamming(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def embed_mm(data_url, retries=4):
    body = {"model": MM_MODEL, "input": data_url}
    last = None
    for attempt in range(retries):
        r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=90)
        resp = r["response"] or {}
        if "data" in resp:
            return resp["data"][0]["embedding"], r.get("exec_id")
        last = resp
        time.sleep(2.0 * (attempt + 1))
    print("  embed_mm FAILED after retries:", json.dumps(last, ensure_ascii=False)[:200])
    return None, None


def run():
    t0 = time.time()

    # ---------- (A) near-dup retrieval: originals + soft + hard, mm + phash ----------
    mm_orig, mm_soft, mm_hard = {}, {}, {}
    phash_orig, phash_soft, phash_hard = {}, {}, {}
    fail_log = []

    print("=== embedding 30 originals (mm) ===")
    for sid in ids:
        p = paths[sid]
        vec, exec_id = embed_mm(to_data_url(p))
        if vec is None:
            fail_log.append({"id": sid, "stage": "orig"})
        mm_orig[sid] = vec
        pil = Image.open(p).convert("RGB")
        phash_orig[sid] = average_hash(pil)
        print(f"  orig {sid}: mm_ok={vec is not None}")
        time.sleep(0.3)

    print("=== embedding 30 soft-dup (mm) ===")
    for sid in ids:
        p = paths[sid]
        du = soft_dup(p)
        vec, exec_id = embed_mm(du)
        if vec is None:
            fail_log.append({"id": sid, "stage": "soft"})
        mm_soft[sid] = vec
        # phash on the decoded soft-dup bytes (consistent with image actually sent)
        raw = base64.b64decode(du.split(",", 1)[1])
        pil = Image.open(io.BytesIO(raw)).convert("RGB")
        phash_soft[sid] = average_hash(pil)
        print(f"  soft {sid}: mm_ok={vec is not None}")
        time.sleep(0.3)

    print("=== embedding 30 hard-dup (mm) ===")
    for sid in ids:
        p = paths[sid]
        du = hard_dup(p)
        vec, exec_id = embed_mm(du)
        if vec is None:
            fail_log.append({"id": sid, "stage": "hard"})
        mm_hard[sid] = vec
        raw = base64.b64decode(du.split(",", 1)[1])
        pil = Image.open(io.BytesIO(raw)).convert("RGB")
        phash_hard[sid] = average_hash(pil)
        print(f"  hard {sid}: mm_ok={vec is not None}")
        time.sleep(0.3)

    def nearest_mm(query_vec, pool):
        best, best_score = None, -2.0
        for sid, v in pool.items():
            if v is None:
                continue
            s = cosine(query_vec, v)
            if s > best_score:
                best_score, best = s, sid
        return best, best_score

    def nearest_phash(query_hash, pool):
        best, best_d = None, 999
        for sid, h in pool.items():
            d = hamming(query_hash, h)
            if d < best_d:
                best_d, best = d, sid
        return best, best_d

    retrieval_rows = []
    for sid in ids:
        row = {"id": sid}
        if mm_soft[sid] is not None:
            nn, score = nearest_mm(mm_soft[sid], mm_orig)
            row["mm_soft_nearest"] = nn
            row["mm_soft_correct"] = (nn == sid)
            row["mm_soft_cosine"] = round(score, 4)
        if mm_hard[sid] is not None:
            nn, score = nearest_mm(mm_hard[sid], mm_orig)
            row["mm_hard_nearest"] = nn
            row["mm_hard_correct"] = (nn == sid)
            row["mm_hard_cosine"] = round(score, 4)
        nn, d = nearest_phash(phash_soft[sid], phash_orig)
        row["phash_soft_nearest"] = nn
        row["phash_soft_correct"] = (nn == sid)
        row["phash_soft_hamming"] = d
        nn, d = nearest_phash(phash_hard[sid], phash_orig)
        row["phash_hard_nearest"] = nn
        row["phash_hard_correct"] = (nn == sid)
        row["phash_hard_hamming"] = d
        retrieval_rows.append(row)

    n = len(retrieval_rows)
    mm_soft_rows = [r for r in retrieval_rows if "mm_soft_correct" in r]
    mm_hard_rows = [r for r in retrieval_rows if "mm_hard_correct" in r]
    recall_summary = {
        "n_scans": n,
        "mm_model": MM_MODEL,
        "mm_n_embedded_ok": len(mm_soft_rows),
        "mm_soft_dup_recall_at_1": (sum(r["mm_soft_correct"] for r in mm_soft_rows) / len(mm_soft_rows)
                                     if mm_soft_rows else None),
        "mm_hard_dup_recall_at_1": (sum(r["mm_hard_correct"] for r in mm_hard_rows) / len(mm_hard_rows)
                                     if mm_hard_rows else None),
        "phash_soft_dup_recall_at_1": sum(r["phash_soft_correct"] for r in retrieval_rows) / n,
        "phash_hard_dup_recall_at_1": sum(r["phash_hard_correct"] for r in retrieval_rows) / n,
    }
    print(json.dumps(recall_summary, ensure_ascii=False, indent=2))

    # checkpoint — не терять часть A, если часть B упадёт на кривых метаданных
    json.dump({"part_A_near_dup_retrieval": {"summary": recall_summary, "details": retrieval_rows,
                                               "fail_log": fail_log}},
               open("case4-full-retrieval-30-partA-checkpoint-results.json", "w", encoding="utf-8"),
               ensure_ascii=False, indent=2)

    # ---------- (B) text semantic separation: content-query recall@1 across 30 ----------
    content_queries = []
    for s in samples:
        menu = s.get("gt_parse", {}).get("menu")
        nm = None
        if isinstance(menu, dict):
            nm = menu.get("nm")
        elif isinstance(menu, list):
            first = next((m for m in menu if isinstance(m, dict) and m.get("nm")), None)
            nm = first.get("nm") if first else None
        if nm and len(nm.strip()) >= 3:
            content_queries.append({"id": s["id"], "query": nm.strip()})
    print(f"=== {len(content_queries)} content-queries (из gt_parse.menu.nm) ===")

    ocr_texts = [s["ocr_text"] for s in samples]
    body = {"model": TEXT_MODEL, "input": ocr_texts}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=120)
    resp = r["response"] or {}
    text_vecs = {}
    text_embed_cost = None
    if "data" in resp:
        for s, d in zip(samples, resp["data"]):
            text_vecs[s["id"]] = d["embedding"]
        text_embed_cost = (resp.get("usage", {}) or {}).get("cost")

    q_body = {"model": TEXT_MODEL, "input": [c["query"] for c in content_queries]}
    rq = call_raw("https://openrouter.ai/api/v1/embeddings", q_body, timeout=120)
    respq = rq["response"] or {}
    query_rows = []
    if "data" in respq:
        for c, d in zip(content_queries, respq["data"]):
            qvec = d["embedding"]
            best, best_score = None, -2.0
            for sid, v in text_vecs.items():
                sc = cosine(qvec, v)
                if sc > best_score:
                    best_score, best = sc, sid
            query_rows.append({"id": c["id"], "query": c["query"], "retrieved": best,
                                "correct": (best == c["id"]), "cosine": round(best_score, 4)})
    text_recall_at_1 = (sum(r["correct"] for r in query_rows) / len(query_rows)) if query_rows else None

    # pairwise text separation (descriptive stat, quantifies case4_measure.py part (a))
    pair_text_cosines = []
    pair_mm_cosines = []
    pair_phash_hamming = []
    pair_rows_full = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            tc = cosine(text_vecs[a], text_vecs[b]) if (a in text_vecs and b in text_vecs) else None
            mc = cosine(mm_orig[a], mm_orig[b]) if (mm_orig.get(a) is not None and mm_orig.get(b) is not None) else None
            hd = hamming(phash_orig[a], phash_orig[b])
            if tc is not None:
                pair_text_cosines.append(tc)
            if tc is not None and mc is not None:
                pair_mm_cosines.append(mc)
                pair_phash_hamming.append(hd)
                pair_rows_full.append({"a": a, "b": b, "text_cosine": round(tc, 4),
                                        "mm_cosine": round(mc, 4), "phash_hamming": hd})

    def pearson(xs, ys):
        n_ = len(xs)
        mx, my = sum(xs) / n_, sum(ys) / n_
        cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        vx = sum((x - mx) ** 2 for x in xs)
        vy = sum((y - my) ** 2 for y in ys)
        return cov / ((vx * vy) ** 0.5) if vx and vy else 0.0

    # ---------- (C) СЕМАНТИЧЕСКОЕ сходство (роль варианта 2 из n59 — "похож ли скан по
    # смыслу на один из прошлых", НЕ "это тот же самый пересканированный документ" —
    # это роль phash/части (A) выше). Ground truth для "семантически ближайший ДРУГОЙ
    # чек в этой выборке" берём из уже проверенного рабочего метода — текстового
    # эмбеддинга OCR (part (а) case4_measure.py, корректно различает чеки по содержанию).
    # Для каждого из 30 чеков (ОРИГИНАЛ, без аугментации — это тест на РАЗНЫХ документах,
    # не на дублях) находим ближайший ИЗ ОСТАЛЬНЫХ 29 по cosine текста, mm-эмбеддинга,
    # phash — и считаем, насколько mm/phash согласны с текстовым "золотым" соседом.
    # Это recall@1-метрика в духе case1_measure.py (query -> nearest -> correct?), где
    # query = сам чек, corpus = остальные 29, "gold" = ближайший по тексту.
    sem_rows = []
    for sid in ids:
        others = [x for x in ids if x != sid]

        def nearest_among(pool_fn, maximize=True):
            best, best_score = None, (-1e9 if maximize else 1e9)
            for o in others:
                s = pool_fn(o)
                if s is None:
                    continue
                if (maximize and s > best_score) or (not maximize and s < best_score):
                    best_score, best = s, o
            return best, best_score

        gold_nn, gold_score = nearest_among(lambda o: cosine(text_vecs[sid], text_vecs[o]) if sid in text_vecs and o in text_vecs else None)
        mm_nn, mm_score = nearest_among(lambda o: cosine(mm_orig[sid], mm_orig[o]) if mm_orig.get(sid) is not None and mm_orig.get(o) is not None else None)
        ph_nn, ph_score = nearest_among((lambda o: -hamming(phash_orig[sid], phash_orig[o])), maximize=True)
        sem_rows.append({
            "id": sid,
            "text_gold_nearest": gold_nn, "text_gold_cosine": round(gold_score, 4) if gold_score is not None else None,
            "mm_nearest": mm_nn, "mm_cosine": round(mm_score, 4) if mm_score not in (None, -1e9) else None,
            "mm_agrees_with_text": (mm_nn == gold_nn) if (mm_nn and gold_nn) else None,
            "phash_nearest": ph_nn, "phash_hamming": (-ph_score) if ph_score != -1e9 else None,
            "phash_agrees_with_text": (ph_nn == gold_nn) if (ph_nn and gold_nn) else None,
        })

    n_sem = len(sem_rows)
    mm_agree_rows = [r for r in sem_rows if r["mm_agrees_with_text"] is not None]
    ph_agree_rows = [r for r in sem_rows if r["phash_agrees_with_text"] is not None]
    semantic_summary = {
        "method": "Ground truth 'семантически ближайший ДРУГОЙ чек' = top-1 среди остальных "
                  "29 по text-embedding(OCR) cosine (проверенный рабочий метод, part (a)). "
                  "recall@1(mm) = доля чеков, где mm-эмбеддинг (на ОРИГИНАЛЬНЫХ, "
                  "неаугментированных сканах) выбирает ТОГО ЖЕ ближайшего соседа, что текст. "
                  "Аналогично для phash. Chance-level при 29 кандидатах ≈ 1/29 = 0.034.",
        "n_scans": n_sem,
        "chance_level_recall_at_1": round(1 / (len(ids) - 1), 4),
        "mm_model": MM_MODEL,
        "mm_semantic_agreement_recall_at_1": (sum(r["mm_agrees_with_text"] for r in mm_agree_rows) / len(mm_agree_rows)
                                                if mm_agree_rows else None),
        "phash_semantic_agreement_recall_at_1": (sum(r["phash_agrees_with_text"] for r in ph_agree_rows) / len(ph_agree_rows)
                                                   if ph_agree_rows else None),
        "pearson_correlation_text_vs_mm_cosine_all_pairs": round(pearson(pair_text_cosines, pair_mm_cosines), 4) if pair_mm_cosines else None,
        "pearson_correlation_text_cosine_vs_phash_similarity_all_pairs": (
            round(pearson(pair_text_cosines, [64 - h for h in pair_phash_hamming]), 4) if pair_phash_hamming else None),
        "n_pairs_for_correlation": len(pair_mm_cosines),
    }
    print("\n=== (C) SEMANTIC AGREEMENT ===")
    print(json.dumps(semantic_summary, ensure_ascii=False, indent=2))

    elapsed = time.time() - t0
    out = {
        "part_A_near_dup_retrieval": {
            "method": "soft-dup (resize*0.97+recompress q60, имитация повторного скана) и "
                      "hard-dup (поворот 12°+обрезка 4% краёв, имитация съёмки под углом) "
                      "для ВСЕХ 30 сканов (не выборки 6, как в case4_measure.py) — для каждой "
                      "пары (оригинал, дубль) эмбеддим/хэшируем дубль и ищем ближайший ОРИГИНАЛ "
                      "среди всех 30 по cosine (mm) / Hamming (phash); recall@1 = доля, где "
                      "ближайший — тот самый оригинал.",
            "summary": recall_summary,
            "details": retrieval_rows,
            "fail_log": fail_log,
        },
        "part_B_text_content_recall": {
            "method": "Запрос = название позиции чека (gt_parse.menu.nm, короткий содержательный "
                      "фрагмент, не вся OCR-строка) -> text-embedding-3-small -> cosine top-1 среди "
                      "ВСЕХ 30 OCR-эмбеддингов чеков -> совпадает ли top-1 с чеком-источником запроса.",
            "n_queries": len(query_rows),
            "recall_at_1": text_recall_at_1,
            "details": query_rows,
            "text_embed_cost_usd": text_embed_cost,
        },
        "pairwise_text_cosine_stats_all_435_pairs": {
            "n_pairs": len(pair_text_cosines),
            "mean": round(sum(pair_text_cosines) / len(pair_text_cosines), 4) if pair_text_cosines else None,
            "min": round(min(pair_text_cosines), 4) if pair_text_cosines else None,
            "max": round(max(pair_text_cosines), 4) if pair_text_cosines else None,
        },
        "part_C_semantic_similarity_agreement": {
            "summary": semantic_summary,
            "details": sem_rows,
        },
        "total_wall_s": round(elapsed, 1),
    }
    json.dump(out, open("case4-full-retrieval-30-results.json", "w", encoding="utf-8"),
               ensure_ascii=False, indent=2)
    print("\n=== FINAL SUMMARY ===")
    print(json.dumps({"recall_summary": recall_summary,
                       "text_content_recall_at_1": text_recall_at_1,
                       "pairwise_text_cosine_stats": out["pairwise_text_cosine_stats_all_435_pairs"]},
                      ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
