#!/usr/bin/env python3
"""Семинар 11, Кейс 4 — сборка корпуса для замера семантического размытия
поиска с ростом РАЗНООБРАЗИЯ базы (не просто размера — это другой эффект,
уже измеренный sem-10 Кейсом 1 на росте размера однородного-ish пула).

Методология (WYDOT, arXiv:2606.11350): ФИКСИРОВАННЫЙ набор запросов, ТОЧНЫЙ
(не ANN) поиск, меняется ТОЛЬКО состав/разнообразие корпуса. Чтобы отделить
эффект разнообразия от эффекта размера, который sem-10 Кейс 1 уже измерил
(см. sem-10/rework/section-1-khranenie-bazy.md), этот замер строит ДВА
параллельных трека роста РАВНОГО размера на каждом шаге:

  Track H (homogeneous)  — рост добавлением документов ТОЙ ЖЕ широкой темы
                            (биология/жизнь) — аналог «курс добавил ещё
                            материалов своего же курса».
  Track D (diverse)      — рост добавлением документов ЗАМЕТНО ДРУГИХ тем
                            (история, физика, спорт, география, экономика и
                            т.п., отфильтровано от биологии) — аналог
                            «учебный центр свёл в одну базу несколько курсов»
                            (сцена Ольги, см. SETKA-KEYSOV.md Кейс 4).

Все тексты — настоящие параграфы SberQuAD (train+val, уже закэшированы
локально на этом стенде с Семинара 10 — /tmp/sem10-data/sberquad_{train,val}.
parquet, тот же источник, никаких новых источников не выдумано). Якоря
(«маленькая однородная база») — 3 уже измеренных needle-вопроса Кейса 1
Семинара 10 (q1/q6/q7, все биология — circulation/mitochondria/diptera) +
5 дополнительных настоящих биологических Q&A-пар, намайненных той же
эвристикой качества, что уже применяет build_corpus_v2.py Семинара 10
(answer_start сверен с реальным текстом, длина контекста 350-1100 символов)
— расширение до N=8 запросов сделано ИСКЛЮЧИТЕЛЬНО для устойчивости оценки
(N=3 слишком шумно для процентов), не меняет качественную природу вопроса.

Запускать из measure/. Читает /tmp/sem10-data/sberquad_{train,val}.parquet
(не копирует их в репозиторий — см. sem-10/.gitignore конвенцию, тот же
принцип применён здесь: исходные parquet остаются вне git)."""
import json
import random
import re

import pandas as pd

random.seed(42)

SBERQUAD_TRAIN = "/tmp/sem10-data/sberquad_train.parquet"
SBERQUAD_VAL = "/tmp/sem10-data/sberquad_val.parquet"
CASE1_CORPUS = ("/home/harness/harness-projects/256/.worktrees/folder-288/"
                "session-b2efe723-e1e67a60/library/seminars/sem-10/stend/corpus/corpus_case1.json")

# 2026-11-18 (issue #345, владелец: «масштаб надо расширить... от десятков до полного
# набора») — оба потолка поднимаются до РЕАЛЬНОГО размера доступного пула, не до
# произвольного числа. Пулы роста ниже больше не берутся из good_qa_rows() (который
# требует валидной Q&A-пары — answer_start, длина 350-1100): это требование нужно
# ТОЛЬКО якорям (их буквально спрашивают и проверяют ответ), документы роста — просто
# тексты-дистракторы, их Q&A-валидность не используется. Снятие этого фильтра для пулов
# роста — единственный способ приблизиться к «полному набору» на этом источнике: честный
# максимум без него — 686 биологических (Track H) и 7838 нехимических-прочих (Track D)
# документов из 9078 уникальных параграфов train+val (см. ниже, после построения пулов,
# числа печатаются и фиксируются в meta). Это НЕ «десятки тысяч» — это и есть реальный
# потолок данного локального кэша SberQuAD, см. честную оговорку в README/главе.
N_GROWTH_PER_TRACK = 10_000  # верхняя граница-заглушка, фактический размер пула Track H
                              # меньше (ограничен реальным числом биологических документов
                              # корпуса) — см. meta.n_track_h в итоговом corpus_case4.json
N_D_CANDIDATES = 10_000       # то же для Track D — фактический размер ограничен реальным
                              # числом «не биологии» в корпусе, см. meta.n_track_d_candidates

BIO_KW = re.compile(
    r"клетк|орган[иы]зм|кровен|кровоснаб|\bкровь|\bкрови\b|живот[нм]|растени|биолог|фермент|белк|белок|"
    r"ткан[ьи]|млекопитающ|бактери|вирус|генетик|эволюци|мутаци|хромосом|"
    r"анатоми|физиологи|экосистем|популяци[яию]|насеком|позвоночн|беспозвоночн|фотосинтез|"
    r"пищевар|организма|клеточ",
    re.IGNORECASE,
)
# Убран широкий \bген[а-яё]*\b (ловил «генерал», «генеральный» как ложные
# срабатывания «ген»/«генетика») — проверено вручную на первой сборке пула
# (anchor-new2 «Грибоедов… генерала», anchor-new5 «Генетически… финикийцы» —
# оба ложные для цели «якорь явно про биологию», не для роста D-трека, где
# шум в 1 документе из 300 не меняет вывод, но для 5 именных якорей это
# недопустимо — якоря проверяются дополнительно: см. MIN_BIO_HITS ниже).
MIN_BIO_HITS = 2  # для якорей (не для пула роста) — не одно случайное слово


def load_sberquad_rows():
    df = pd.concat([pd.read_parquet(SBERQUAD_TRAIN), pd.read_parquet(SBERQUAD_VAL)], ignore_index=True)
    seen_ctx = set()
    rows = []
    for _, r in df.iterrows():
        ctx = r["context"]
        if ctx in seen_ctx:
            continue
        seen_ctx.add(ctx)
        rows.append(r)
    return rows


def good_qa_rows(rows):
    """Та же проверка качества, что build_corpus_v2.py Семинара 10: длина
    контекста 350-1100 символов, answer_start реально указывает на текст
    ответа (S10 нашёл 22,0% строк HF-конвертации SberQuAD с несовпадением —
    тот же фильтр применён здесь, не повторяем тот же дефект)."""
    out = []
    for r in rows:
        ans = r["answers"]
        if len(ans["text"]) == 0:
            continue
        text = ans["text"][0]
        start = int(ans["answer_start"][0])
        ctx = r["context"]
        if not (350 <= len(ctx) <= 1100):
            continue
        if ctx[start:start + len(text)] != text:
            continue
        out.append({"context": ctx, "question": r["question"], "answer": text, "answer_start": start})
    return out


def main():
    print("loading SberQuAD train+val (local cache, no network)...")
    rows = load_sberquad_rows()
    print(f"unique contexts: {len(rows)}")
    good = good_qa_rows(rows)
    print(f"good (length+answer_start valid): {len(good)}")

    def n_distinct_hits_top(ctx):
        return len(set(m.lower() for m in BIO_KW.findall(ctx)))

    bio_good_all = [g for g in good if BIO_KW.search(g["context"])]
    # >=2 несовпадающих biology-хита — не только для якорей (см. ниже), но и
    # для самого пула роста Track H: один-единственный хит слишком часто
    # ложный (напр. «100-клеточная доска» шашек ловится на «клеточ» — та же
    # русская лексическая многозначность «клетка = биологическая клетка ИЛИ
    # клетка сетки/доски», которая и есть иллюстрация механики размытия, но
    # мы не хотим её именно В ОДНОРОДНОМ треке — там она не на своём месте).
    bio_good = [g for g in bio_good_all if n_distinct_hits_top(g["context"]) >= MIN_BIO_HITS]
    nonbio_good = [g for g in good if not BIO_KW.search(g["context"])]
    print(f"bio_good_all: {len(bio_good_all)}  bio_good (>={MIN_BIO_HITS} hits): {len(bio_good)}  "
          f"nonbio_good: {len(nonbio_good)}")

    # --- Якоря: 3 переносятся из Кейса 1 С10 (needle-1/6/7, все биология) ---
    case1 = json.load(open(CASE1_CORPUS, encoding="utf-8"))
    corpus1 = {d["id"]: d for d in case1["corpus_500"]}
    q1map = {q["qid"]: q for q in case1["questions"]}
    reused_qids = ["q1", "q6", "q7"]
    anchors = []
    reused_contexts = set()
    for qid in reused_qids:
        q = q1map[qid]
        ctx = corpus1[q["gold_doc_id"]]["text"]
        reused_contexts.add(ctx)
        anchors.append({
            "anchor_id": f"anchor-{qid}",
            "question": q["question"],
            "answer": q["answer"],
            "context": ctx,
            "lexical_class": q["lexical_class"],
            "provenance": f"sem-10 Кейс 1, qid={qid}, gold_doc_id={q['gold_doc_id']} (переносится дословно)",
        })

    # --- +5 новых биологических Q&A-якорей (та же эвристика качества) ---
    # Для якорей — усиленный фильтр (>=2 несовпадающих biology-хита в тексте),
    # чтобы не взять случайное одно-словное совпадение («генерала» ловился
    # прежней версией как «ген» — см. комментарий у MIN_BIO_HITS выше).
    def n_distinct_hits(ctx):
        return len(set(m.lower() for m in BIO_KW.findall(ctx)))

    bio_for_anchors = [g for g in bio_good
                        if g["context"] not in reused_contexts and n_distinct_hits(g["context"]) >= MIN_BIO_HITS]
    random.shuffle(bio_for_anchors)
    seen_ctx_new = set()
    added = 0
    for g in bio_for_anchors:
        if g["context"] in seen_ctx_new:
            continue
        seen_ctx_new.add(g["context"])
        anchors.append({
            "anchor_id": f"anchor-new{added + 1}",
            "question": g["question"],
            "answer": g["answer"],
            "context": g["context"],
            "lexical_class": "unclassified-new-anchor",
            "provenance": "намайнен для Кейса 4 С11 той же эвристикой качества, что build_corpus_v2.py С10 "
                          "(answer_start сверен, длина 350-1100)",
        })
        added += 1
        if added >= 5:
            break
    print(f"anchors total: {len(anchors)} (3 перенесённых + {added} новых)")

    anchor_contexts = {a["context"] for a in anchors}

    # --- Пулы роста: 2026-11-18, расширено на ВЕСЬ корпус (rows), не на good_qa_rows().
    # Документы роста — чистые тексты-дистракторы, их Q&A (answer_start/длина 350-1100)
    # никогда не читается ни одним шагом замера (только якоря реально спрашиваются) —
    # поэтому ограничивать пул роста той же меркой, что нужна для надёжного Q&A, означало
    # отбрасывать 9078-6551=2527 настоящих документов корпуса без причины, которая к этому
    # пулу применима. Классификация bio/not-bio — тот же BIO_KW/MIN_BIO_HITS, что и раньше,
    # просто применённый к полному rows, а не к его урезанной "good" подвыборке.
    bio_rows_all = [r for r in rows if BIO_KW.search(r["context"])]
    bio_rows = [r for r in bio_rows_all if n_distinct_hits_top(r["context"]) >= MIN_BIO_HITS]
    nonbio_rows = [r for r in rows if not BIO_KW.search(r["context"])]
    print(f"[full corpus, не только good_qa_rows] bio_rows_all: {len(bio_rows_all)}  "
          f"bio_rows (>={MIN_BIO_HITS} hits): {len(bio_rows)}  nonbio_rows: {len(nonbio_rows)}")

    bio_pool_src = [{"context": r["context"]} for r in bio_rows if r["context"] not in anchor_contexts]
    nonbio_pool_src = [{"context": r["context"]} for r in nonbio_rows if r["context"] not in anchor_contexts]
    random.shuffle(bio_pool_src)
    random.shuffle(nonbio_pool_src)

    # dedupe by context within each pool
    def dedupe(pool):
        seen = set()
        out = []
        for g in pool:
            if g["context"] in seen:
                continue
            seen.add(g["context"])
            out.append(g)
        return out

    bio_pool_src = dedupe(bio_pool_src)[:N_GROWTH_PER_TRACK]
    nonbio_pool_src = dedupe(nonbio_pool_src)[:N_D_CANDIDATES]
    print(f"bio_pool (Track H growth): {len(bio_pool_src)}  "
          f"nonbio_pool (Track D candidates): {len(nonbio_pool_src)}")

    track_h = [{"doc_id": f"H-{i+1}", "text": g["context"]} for i, g in enumerate(bio_pool_src)]
    track_d_candidates = [{"doc_id": f"Dc-{i+1}", "text": g["context"]} for i, g in enumerate(nonbio_pool_src)]

    out = {
        "meta": {
            "source": "SberQuAD (train+val, localcache /tmp/sem10-data, из Семинара 10)",
            "bio_keyword_pattern": BIO_KW.pattern,
            "n_anchors": len(anchors),
            "n_track_h": len(track_h),
            "n_track_d_candidates": len(track_d_candidates),
            "seed": 42,
        },
        "anchors": anchors,
        "track_h_growth": track_h,                      # своя тема (биология), случайный порядок — size control
        "track_d_candidates": track_d_candidates,        # чужие темы, кандидатный пул — из него в
                                                          # embed_and_measure_case4.py отбираются
                                                          # D_random (случайный срез) и D_adversarial
                                                          # (ближайшие по смыслу "ложные похожие")
    }
    json.dump(out, open("corpus_case4.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("saved corpus_case4.json")
    for a in anchors:
        print(f"  {a['anchor_id']}: Q={a['question'][:60]!r} A={a['answer']!r}")


if __name__ == "__main__":
    main()
