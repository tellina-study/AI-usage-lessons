#!/usr/bin/env python3
"""Фаза 0 замеров №3 и №4 (Кейс 2, Семинар 12, issue #351): считает и кэширует вектор
эмбеддинга ОРИГИНАЛА (без искажений, 300x450 JPEG q80) для всех 30 сканов CORD по каждой
из шести моделей, нужных обоим замерам. Кэш переиспользуется:
- Замером №3 (дрожание входа) — модели nvidia/nemotron-3.5-embed-1b:free и
  nvidia/llama-nemotron-embed-vl-1b-v2:free как база для cosine-дрифта и NN-поиска.
- Замером №4 (согласие моделей) — те же два плюс nvidia/nemotron-3.5-embed-8b:free
  (лёгкий случай — та же архитектурная линия, разный размер) и google/gemini-embedding-2,
  cohere/embed-5-fast, mongodb/voyage-multimodal-3.5 (трудный случай — разные поставщики,
  margin≈0 по C10).

Запуск идемпотентен: кэш пишется в raw/originals_<model>.json после КАЖДОЙ картинки,
повторный запуск на той же машине продолжает, а не начинает заново.
"""
import json
import time

from common_k2 import load_or_fetch_originals_concurrent, load_corpus

MODELS = [
    # Здоровые модели — первыми, чтобы продвигать замер №4 независимо от статуса
    # проблемных моделей ниже (2026-11-21: nemotron-3.5-embed-1b в затяжном отказе
    # 503/504, llama-nemotron-embed-vl-1b-v2 404 "No endpoints found" — снята/переименована
    # у провайдера, подтверждено прямым curl живого каталога, см. доклад оркестратору).
    "nvidia/nemotron-3.5-embed-8b:free",
    "google/gemini-embedding-2",
    "cohere/embed-5-fast",
    "mongodb/voyage-multimodal-3.5",
    "nvidia/nemotron-3.5-embed-1b:free",
    "nvidia/llama-nemotron-embed-vl-1b-v2:free",
]


def main():
    samples, ids, paths = load_corpus()
    print(f"Корпус: {len(ids)} сканов")
    summary = {}
    t0 = time.time()
    for model in MODELS:
        print(f"\n=== {model} ===")
        vectors, fail_log, cost = load_or_fetch_originals_concurrent(model, ids, paths, max_workers=2)
        n_ok = sum(1 for v in vectors.values() if v is not None)
        summary[model] = {"n_ok": n_ok, "n_fail": len(fail_log), "cost_usd": round(cost, 6)}
        print(f"  итог {model}: {n_ok}/{len(ids)} ok, cost ${cost:.6f}")
    elapsed = time.time() - t0
    print("\n=== ИТОГ fetch_originals ===")
    print(json.dumps({"summary": summary, "elapsed_s": round(elapsed, 1)}, ensure_ascii=False, indent=2))
    json.dump({"summary": summary, "elapsed_s": round(elapsed, 1)},
               open("raw/fetch_originals_summary.json", "w", encoding="utf-8"),
               ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
