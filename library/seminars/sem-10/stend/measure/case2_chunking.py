#!/usr/bin/env python3
"""Кейс 2 — четыре версии нарезки документа на реальных контекстах SberQuAD с известным
answer_start/answer_end: v1 (фиксированный размер), v2 (по структуре предложений),
v3 (по границам слов — не рвёт слово, но не знает о предложении), v4 (фиксированный
размер с перекрытием — закрывает честный открытый пункт прежнего замера: перекрытие
не было проверено ни на одном прогоне).

Метрика: доля вопросов, для которых полный текст эталонного ответа оказывается
целиком в ОДНОМ куске (не разорван границей) — считается структурно (без LLM/API).
"""
import json
import re

import pandas as pd

CHUNK_SIZE = 180  # символов — заголовочное значение свода (полный sweep — ниже в summary)
OVERLAP = 0
OVERLAP_FRAC_V4 = 0.15  # доля size, используемая версией 4 (перекрытие)

df = pd.read_parquet("sberquad_val.parquet")
by_ctx = {}
n_offset_mismatch = 0
n_offset_total = 0
for _, r in df.iterrows():
    ans = r["answers"]
    if len(ans["text"]) == 0:
        continue
    n_offset_total += 1
    a_start = int(ans["answer_start"][0])
    a_text = ans["text"][0]
    ctx = r["context"]
    # НАХОДКА (раздел §8.7 канона — проверять напрямую): у ~22% строк этого HF-конвёртера
    # SberQuAD поле answer_start не совпадает с реальным положением текста ответа в context
    # (сдвиг кодировки/нормализации кавычек в исходной конвертации). Такие строки не годятся
    # для измерения "разорвана ли граница куска" — отбрасываем их здесь, а не подгоняем офсет.
    if ctx[a_start:a_start + len(a_text)] != a_text:
        n_offset_mismatch += 1
        continue
    by_ctx.setdefault(ctx, []).append({
        "question": r["question"],
        "answer": a_text,
        "answer_start": a_start,
    })
print(f"[данные] offset mismatch в исходном датасете: {n_offset_mismatch}/{n_offset_total} "
      f"= {n_offset_mismatch/n_offset_total:.1%} — такие строки отброшены из замера Кейса 2")

# документы подлиннее, чтобы дробление на >=2 куска было содержательным
candidates = [(c, qs) for c, qs in by_ctx.items() if len(c) >= 500]
import random
random.seed(7)
random.shuffle(candidates)
sample = candidates[:60]


def chunk_fixed(text, size=CHUNK_SIZE, overlap=OVERLAP):
    chunks = []
    i = 0
    while i < len(text):
        end = min(i + size, len(text))
        chunks.append((i, end, text[i:end]))
        if end == len(text):
            break
        i += size - overlap
    return chunks


SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def chunk_structural(text, target=CHUNK_SIZE):
    """Режет по границам предложений, набирая предложения до ~target символов."""
    sentences = SENT_SPLIT.split(text)
    chunks = []
    pos = 0
    cur_start = 0
    cur_text = ""
    for sent in sentences:
        # найти реальное положение предложения в исходном тексте (устойчиво к пробелам)
        idx = text.find(sent, pos)
        if idx == -1:
            idx = pos
        s_start, s_end = idx, idx + len(sent)
        if cur_text and len(cur_text) + len(sent) + 1 > target:
            chunks.append((cur_start, pos, cur_text))
            cur_text = sent
            cur_start = s_start
        else:
            if not cur_text:
                cur_start = s_start
            cur_text = (cur_text + " " + sent).strip() if cur_text else sent
        pos = s_end
    if cur_text:
        chunks.append((cur_start, len(text), cur_text))
    return chunks


WORD_SPLIT = re.compile(r"\S+")


def chunk_word_boundary(text, size=CHUNK_SIZE):
    """Режет по границам слов: слово целиком никогда не рвётся, но граница предложения
    не учитывается вовсе — дешёвый шаг вверх от голого счёта символов."""
    words = list(WORD_SPLIT.finditer(text))
    if not words:
        return [(0, len(text), text)]
    chunks = []
    cur_start = words[0].start()
    cur_end = cur_start
    cur_len = 0
    for m in words:
        w = m.group()
        added = len(w) if cur_len == 0 else len(w) + 1
        if cur_len and cur_len + added > size:
            chunks.append([cur_start, cur_end])
            cur_start = m.start()
            cur_len = len(w)
        else:
            cur_len += added
        cur_end = m.end()
    chunks.append([cur_start, cur_end])
    # куски делаются смежными (конец = начало следующего), как в chunk_fixed/chunk_structural —
    # иначе пробел между словами выпадает из всех кусков и искажает замер на границе
    for i in range(len(chunks) - 1):
        chunks[i][1] = chunks[i + 1][0]
    chunks[-1][1] = len(text)
    return [(s, e, text[s:e]) for s, e in chunks]


def chunk_fixed_overlap(text, size=CHUNK_SIZE, frac=OVERLAP_FRAC_V4):
    """Та же резка по счёту символов, что v1, но с перекрытием между соседними кусками."""
    overlap = round(size * frac)
    return chunk_fixed(text, size=size, overlap=overlap)


def answer_intact(chunks, a_start, a_end):
    """Есть ли ровно один кусок, целиком содержащий [a_start, a_end)?"""
    for (s, e, _t) in chunks:
        if s <= a_start and a_end <= e:
            return True
    return False


VERSIONS = {
    "v1": lambda ctx, sz: chunk_fixed(ctx, size=sz),
    "v2": lambda ctx, sz: chunk_structural(ctx, target=sz),
    "v3": lambda ctx, sz: chunk_word_boundary(ctx, size=sz),
    "v4": lambda ctx, sz: chunk_fixed_overlap(ctx, size=sz),
}

sweep = []
for sz in [120, 180, 220, 300, 450]:
    n_t = 0
    n_broken = {k: 0 for k in VERSIONS}
    for ctx, qs in sample:
        chunks_by_v = {k: f(ctx, sz) for k, f in VERSIONS.items()}
        for q in qs:
            a_s = q["answer_start"]; a_e = a_s + len(q["answer"])
            if a_e > len(ctx):
                continue
            n_t += 1
            for k, chunks in chunks_by_v.items():
                if not answer_intact(chunks, a_s, a_e):
                    n_broken[k] += 1
    row = {"chunk_size_chars": sz, "n_questions": n_t}
    for k in VERSIONS:
        row[f"{k}_broken"] = n_broken[k]
        row[f"{k}_broken_rate"] = round(n_broken[k] / n_t, 3)
    sweep.append(row)

results = []
n_total = 0
n_broken_headline = {k: 0 for k in VERSIONS}
for ctx, qs in sample:
    chunks_by_v = {k: f(ctx, CHUNK_SIZE) for k, f in VERSIONS.items()}
    for q in qs:
        a_start = q["answer_start"]
        a_end = a_start + len(q["answer"])
        if a_end > len(ctx):
            continue
        n_total += 1
        ok_by_v = {}
        for k, chunks in chunks_by_v.items():
            ok = answer_intact(chunks, a_start, a_end)
            ok_by_v[k] = ok
            if not ok:
                n_broken_headline[k] += 1
        results.append({
            "question": q["question"],
            "answer": q["answer"],
            "context_len": len(ctx),
            **{f"n_chunks_{k}": len(chunks_by_v[k]) for k in VERSIONS},
            **{f"{k}_answer_intact": ok_by_v[k] for k in VERSIONS},
        })

VERSION_LABELS = {
    "v1": "резать по счёту символов",
    "v2": "резать по границам предложений",
    "v3": "резать по границам слов",
    "v4": "резать по счёту символов с перекрытием",
}

summary = {
    "source": "SberQuAD (kuznetsoffandrey/sberquad), validation split, уникальные контексты >=500 символов",
    "offset_mismatch_in_raw_dataset": f"{n_offset_mismatch}/{n_offset_total} ({n_offset_mismatch/n_offset_total:.1%})",
    "n_documents": len(sample),
    "headline_chunk_size_chars": CHUNK_SIZE,
    "overlap_chars_v1_v2_v3": 0,
    "overlap_chars_v4": round(CHUNK_SIZE * OVERLAP_FRAC_V4),
    "overlap_frac_v4": OVERLAP_FRAC_V4,
    "n_questions": n_total,
    "versions": {
        k: {
            "label": VERSION_LABELS[k],
            "answer_intact_count": n_total - n_broken_headline[k],
            "answer_broken_count": n_broken_headline[k],
            "answer_broken_rate": round(n_broken_headline[k] / n_total, 3) if n_total else None,
        }
        for k in VERSIONS
    },
    "sensitivity_sweep_by_chunk_size": sweep,
}
print(json.dumps(summary, ensure_ascii=False, indent=2))
json.dump({"summary": summary, "details": results}, open("case2-results.json", "w", encoding="utf-8"),
           ensure_ascii=False, indent=2)
