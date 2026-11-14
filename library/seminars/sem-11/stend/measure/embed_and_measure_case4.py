#!/usr/bin/env python3
"""Семинар 11, Кейс 4 — эмбеддинг корпуса и замер семантического размытия
поиска с ростом РАЗНООБРАЗИЯ (не просто размера, см. build_corpus_case4.py).

Методология (WYDOT, arXiv:2606.11350): фиксированные запросы (8 якорей),
точный (brute-force) косинусный поиск, меняется только состав корпуса.
ТРИ параллельных трека роста РАВНОГО размера на каждом шаге — размер отделён
от разнообразия, разнообразие отделено от случайности выбора дистрактора:

  Track H            — рост случайными документами ТОЙ ЖЕ широкой темы
                        (биология) — size control, своя тема.
  Track D_random      — рост СЛУЧАЙНЫМИ документами заметно других тем
                        (история, физика, спорт, экономика…) — diversity,
                        но без намеренного выбора "похожих" дистракторов.
  Track D_adversarial — рост документами заметно других тем, отобранными
                        ПО СМЫСЛОВОЙ БЛИЗОСТИ к вопросам якорей (ближайшие
                        по косинусу среди кандидатного пула чужих тем) —
                        тот же механизм, что hard-negative mining в
                        Meghwani et al. (arXiv:2505.18366, источник #2
                        брифа 04): реальные документы, которые "звучат
                        похоже", но относятся к другой теме.

D_random и D_adversarial — одного размера на каждом шаге и берутся из ОДНОГО
кандидатного пула (track_d_candidates, 1600 реальных документов чужих тем);
разница только в ПОРЯДКЕ/ОТБОРЕ, не в теме и не в источнике — это и
изолирует вклад "похожести" от вклада "просто чужой темы".

Все эмбеддинг-вызовы — через вебхук стенда `s10-raw-openrouter` (переиспользован
по канону), модель `openai/text-embedding-3-small`, та же, что sem-10 Кейс 1.
Запускать из measure/, предварительно `python3 build_corpus_case4.py` и
`source /home/harness/.n8n-lab-credentials` (N8N_API_URL/N8N_API_KEY)."""
import json
import random
import time

from harness2 import embed_batch, cosine

random.seed(42)

GROWTH_STEPS = [0, 20, 100, 300]
BATCH = 80
N_NEAREST_PER_ANCHOR = 60  # top-K кандидатов D на анкор для adversarial-отбора


def embed_all(texts, label):
    vecs = []
    exec_ids = []
    total_cost = 0.0
    t0 = time.time()
    for i in range(0, len(texts), BATCH):
        chunk = texts[i:i + BATCH]
        v, meta = embed_batch(chunk)
        vecs.extend(v)
        exec_ids.append(meta["exec_id"])
        total_cost += meta.get("cost") or 0.0
        print(f"  [{label}] batch {i}-{i+len(chunk)} exec_id={meta['exec_id']} "
              f"wall={meta['wall_s']}s cost={meta.get('cost')}")
    return vecs, exec_ids, total_cost, round(time.time() - t0, 1)


def rank_of(gold_doc_id, scored):
    for i, (doc_id, _) in enumerate(scored, start=1):
        if doc_id == gold_doc_id:
            return i
    return None


def main():
    data = json.load(open("corpus_case4.json", encoding="utf-8"))
    anchors = data["anchors"]
    track_h = data["track_h_growth"]
    d_candidates = data["track_d_candidates"]

    exec_log = {}
    cost_total = 0.0

    print(f"embedding {len(anchors)} anchor contexts...")
    v, eids, cost, _ = embed_all([a["context"] for a in anchors], "anchor-ctx")
    exec_log["anchor_contexts"] = eids
    cost_total += cost
    for a, vec in zip(anchors, v):
        a["embedding"] = vec

    print(f"embedding {len(anchors)} anchor questions...")
    v, eids, cost, _ = embed_all([a["question"] for a in anchors], "anchor-q")
    exec_log["anchor_questions"] = eids
    cost_total += cost
    for a, vec in zip(anchors, v):
        a["q_embedding"] = vec

    print(f"embedding {len(track_h)} Track H (same-domain random growth) docs...")
    v, eids, cost, _ = embed_all([d["text"] for d in track_h], "track-h")
    exec_log["track_h"] = eids
    cost_total += cost
    for d, vec in zip(track_h, v):
        d["embedding"] = vec

    print(f"embedding {len(d_candidates)} Track D candidate pool (other domains) docs...")
    v, eids, cost, _ = embed_all([d["text"] for d in d_candidates], "track-d-candidates")
    exec_log["track_d_candidates"] = eids
    cost_total += cost
    for d, vec in zip(d_candidates, v):
        d["embedding"] = vec

    print(f"embedding cost so far: ${cost_total:.6f}")

    # --- D_random: случайный срез кандидатного пула (фикс. seed, тот же для всех шагов) ---
    d_random = list(d_candidates)
    random.shuffle(d_random)
    d_random = d_random[:max(GROWTH_STEPS)]

    # --- D_adversarial: для каждого анкора — top-N_NEAREST_PER_ANCHOR кандидатов
    # по косинусу (вопрос анкора vs кандидат), объединение, сортировка по
    # МАКСИМАЛЬНОМУ косинусу среди всех анкоров (самые опасные — первые). ---
    best_score = {}
    for a in anchors:
        scored = sorted(
            ((d["doc_id"], cosine(a["q_embedding"], d["embedding"])) for d in d_candidates),
            key=lambda t: t[1], reverse=True,
        )
        for doc_id, score in scored[:N_NEAREST_PER_ANCHOR]:
            if doc_id not in best_score or score > best_score[doc_id]:
                best_score[doc_id] = score
    by_id = {d["doc_id"]: d for d in d_candidates}
    d_adv_ids_sorted = sorted(best_score.keys(), key=lambda doc_id: best_score[doc_id], reverse=True)
    print(f"D_adversarial pool (union of top-{N_NEAREST_PER_ANCHOR} per anchor, deduped): {len(d_adv_ids_sorted)} unique docs")
    d_adversarial = [by_id[doc_id] for doc_id in d_adv_ids_sorted][:max(GROWTH_STEPS)]

    tracks = {
        "H_same_domain_random": track_h,
        "D_random": d_random,
        "D_adversarial": d_adversarial,
    }
    for name, pool in tracks.items():
        print(f"{name}: available for growth = {len(pool)} (steps capped at this if smaller)")

    results = []
    for track_name, pool in tracks.items():
        for step in GROWTH_STEPS:
            if step > len(pool):
                continue
            subset_pool = pool[:step]
            candidates = [(a["anchor_id"], a["embedding"]) for a in anchors] + \
                         [(d["doc_id"], d["embedding"]) for d in subset_pool]
            corpus_size = len(candidates)
            for a in anchors:
                scored = sorted(
                    ((doc_id, cosine(a["q_embedding"], vec)) for doc_id, vec in candidates),
                    key=lambda t: t[1], reverse=True,
                )
                rank = rank_of(a["anchor_id"], scored)
                top1_id, top1_score = scored[0]
                gold_score = next(s for doc_id, s in scored if doc_id == a["anchor_id"])
                non_gold_scored = [(doc_id, s) for doc_id, s in scored if doc_id != a["anchor_id"]]
                best_rival_id, best_rival_score = non_gold_scored[0]

                def snippet(doc_id, n=220):
                    doc = by_id.get(doc_id)
                    if doc is None:
                        doc = next((hh for hh in track_h if hh["doc_id"] == doc_id), None)
                    return (doc["text"][:n] if doc else None)

                results.append({
                    "track": track_name,
                    "growth_step": step,
                    "corpus_size": corpus_size,
                    "anchor_id": a["anchor_id"],
                    "question": a["question"],
                    "rank_of_gold": rank,
                    "recall_at_1": rank == 1,
                    "recall_at_3": rank is not None and rank <= 3,
                    "recall_at_5": rank is not None and rank <= 5,
                    "gold_cosine": round(gold_score, 4),
                    "top1_doc_id": top1_id,
                    "top1_cosine": round(top1_score, 4),
                    "top1_is_gold": top1_id == a["anchor_id"],
                    "top1_text_snippet": None if top1_id == a["anchor_id"] else snippet(top1_id),
                    # лучший СОПЕРНИК (не считая самого золотого документа) — и его зазор
                    # до золотого: показывает, сокращается ли запас, даже если top1 не сменился
                    "best_rival_doc_id": best_rival_id,
                    "best_rival_cosine": round(best_rival_score, 4),
                    "margin_gold_minus_best_rival": round(gold_score - best_rival_score, 4),
                    "best_rival_snippet": snippet(best_rival_id),
                })
            n1 = sum(r["recall_at_1"] for r in results if r["track"] == track_name and r["growth_step"] == step)
            print(f"[{track_name}] step={step} corpus_size={corpus_size} — recall@1={n1}/{len(anchors)}")

    summary = {}
    for track_name in tracks:
        summary[track_name] = {}
        for step in GROWTH_STEPS:
            rows = [r for r in results if r["track"] == track_name and r["growth_step"] == step]
            if not rows:
                continue
            n = len(rows)
            summary[track_name][str(step)] = {
                "corpus_size": rows[0]["corpus_size"],
                "n_anchors": n,
                "recall_at_1": sum(r["recall_at_1"] for r in rows) / n,
                "recall_at_3": sum(r["recall_at_3"] for r in rows) / n,
                "mean_margin_gold_minus_best_rival": round(sum(r["margin_gold_minus_best_rival"] for r in rows) / n, 4),
                "recall_at_5": sum(r["recall_at_5"] for r in rows) / n,
                "mean_rank": sum(r["rank_of_gold"] for r in rows) / n,
                "mean_gold_cosine": round(sum(r["gold_cosine"] for r in rows) / n, 4),
            }

    out = {
        "meta": data["meta"],
        "growth_steps": GROWTH_STEPS,
        "n_nearest_per_anchor_for_adversarial": N_NEAREST_PER_ANCHOR,
        "embed_model": "openai/text-embedding-3-small",
        "exec_log": exec_log,
        "cost_usd_total": round(cost_total, 6),
        "summary": summary,
        "details": results,
        "anchors_no_embedding": [{k: v for k, v in a.items() if k not in ("embedding", "q_embedding")}
                                  for a in anchors],
    }
    json.dump(out, open("case4-results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("saved case4-results.json")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
