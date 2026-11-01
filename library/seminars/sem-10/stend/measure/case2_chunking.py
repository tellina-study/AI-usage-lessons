#!/usr/bin/env python3
"""Кейс 2 — v1 (нарезка фиксированным размером) против v2 (по структуре предложений)
на реальных контекстах SberQuAD с известным answer_start/answer_end.

Метрика: доля вопросов, для которых полный текст эталонного ответа оказывается
целиком в ОДНОМ куске (не разорван границей) — считается структурно (без LLM/API).
"""
import json
import re

import pandas as pd

CHUNK_SIZE = 180  # символов — заголовочное значение свода (полный sweep — ниже в summary)
OVERLAP = 0

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


def answer_intact(chunks, a_start, a_end):
    """Есть ли ровно один кусок, целиком содержащий [a_start, a_end)?"""
    for (s, e, _t) in chunks:
        if s <= a_start and a_end <= e:
            return True
    return False


sweep = []
for sz in [120, 180, 220, 300, 450]:
    n_t = n_v1 = n_v2 = 0
    for ctx, qs in sample:
        fc = chunk_fixed(ctx, size=sz)
        sc = chunk_structural(ctx, target=sz)
        for q in qs:
            a_s = q["answer_start"]; a_e = a_s + len(q["answer"])
            if a_e > len(ctx):
                continue
            n_t += 1
            if not answer_intact(fc, a_s, a_e):
                n_v1 += 1
            if not answer_intact(sc, a_s, a_e):
                n_v2 += 1
    sweep.append({"chunk_size_chars": sz, "n_questions": n_t,
                   "v1_broken": n_v1, "v1_broken_rate": round(n_v1 / n_t, 3),
                   "v2_broken": n_v2, "v2_broken_rate": round(n_v2 / n_t, 3)})

results = []
n_total = 0
n_v1_broken = 0
n_v2_broken = 0
for ctx, qs in sample:
    fixed_chunks = chunk_fixed(ctx)
    struct_chunks = chunk_structural(ctx)
    for q in qs:
        a_start = q["answer_start"]
        a_end = a_start + len(q["answer"])
        if a_end > len(ctx):
            continue
        v1_ok = answer_intact(fixed_chunks, a_start, a_end)
        v2_ok = answer_intact(struct_chunks, a_start, a_end)
        n_total += 1
        if not v1_ok:
            n_v1_broken += 1
        if not v2_ok:
            n_v2_broken += 1
        results.append({
            "question": q["question"],
            "answer": q["answer"],
            "context_len": len(ctx),
            "n_chunks_v1": len(fixed_chunks),
            "n_chunks_v2": len(struct_chunks),
            "v1_answer_intact": v1_ok,
            "v2_answer_intact": v2_ok,
        })

summary = {
    "source": "SberQuAD (kuznetsoffandrey/sberquad), validation split, уникальные контексты >=500 символов",
    "offset_mismatch_in_raw_dataset": f"{n_offset_mismatch}/{n_offset_total} ({n_offset_mismatch/n_offset_total:.1%})",
    "n_documents": len(sample),
    "headline_chunk_size_chars": CHUNK_SIZE,
    "overlap_chars": OVERLAP,
    "n_questions": n_total,
    "v1_fixed_size": {
        "answer_intact_count": n_total - n_v1_broken,
        "answer_broken_count": n_v1_broken,
        "answer_broken_rate": round(n_v1_broken / n_total, 3) if n_total else None,
    },
    "v2_structural": {
        "answer_intact_count": n_total - n_v2_broken,
        "answer_broken_count": n_v2_broken,
        "answer_broken_rate": round(n_v2_broken / n_total, 3) if n_total else None,
    },
    "sensitivity_sweep_by_chunk_size": sweep,
}
print(json.dumps(summary, ensure_ascii=False, indent=2))
json.dump({"summary": summary, "details": results}, open("case2-results.json", "w", encoding="utf-8"),
           ensure_ascii=False, indent=2)
