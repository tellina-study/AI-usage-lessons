#!/usr/bin/env python3
"""Общие утилиты для замеров №3 (дрожание входа) и №4 (согласие моделей) Кейса 2,
Семинар 12 (issue #351). Повторяет приёмы `sem-10/stend/measure/case4_full_retrieval_30.py`
(to_data_url, soft_dup/hard_dup-стиль искажений, embed_mm с ретраями, cosine) — не
изобретает новый способ вызова, адаптирует набор искажений под задание замера №3.

Вызовы идут через `harness_call.call_raw` на готовый вебхук `s10-raw-openrouter`
(id S4AMVj1hVmcs4fe8) — ключ OpenRouter остаётся на стороне n8n, новый сценарий не создаётся.
"""
import base64
import io
import json
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from PIL import Image

from harness_call import call_raw

CORPUS_META = "../../../sem-10/stend/corpus/cord_sample_meta.json"
CORPUS_DIR_PREFIX = "../../../sem-10/stend/"  # + s["file"] (file уже содержит "corpus/cord_sample/...")

RAW_DIR = "raw"


def load_corpus():
    samples = json.load(open(CORPUS_META, encoding="utf-8"))
    ids = [s["id"] for s in samples]
    paths = {s["id"]: CORPUS_DIR_PREFIX + s["file"] for s in samples}
    return samples, ids, paths


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


def _to_data_url_from_im(im, w=300, h=450, q=80):
    im2 = im.resize((w, h))
    buf = io.BytesIO()
    im2.save(buf, format="JPEG", quality=q)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


def _load_rgb(path):
    return Image.open(path).convert("RGB")


# ---------- варианты входа (замер №3) ----------
# Рабочее разрешение везде 300x450 — та же точка сравнения, что C10 использовал как
# "реальный скан" (case4_working_mm_results.json step1). Каждый вариант меняет РОВНО
# один параметр файла относительно оригинала, кроме composite (заявленный трудный случай).

def variant_original(path, w=300, h=450, q=80):
    return _to_data_url_from_im(_load_rgb(path), w, h, q)


def variant_downscale(path, w=300, h=450, q=80, factor=0.6):
    """Уменьшение: ресайз до 60% линейного размера рабочего разрешения, затем назад."""
    im = _load_rgb(path).resize((w, h))
    small = im.resize((max(1, int(w * factor)), max(1, int(h * factor))), Image.LANCZOS)
    back = small.resize((w, h), Image.LANCZOS)
    return _to_data_url_from_im(back, w, h, q)


def variant_recompress(path, w=300, h=450, q=30):
    """Пересжатие: та же геометрия, качество JPEG заметно ниже (80 -> 30)."""
    return _to_data_url_from_im(_load_rgb(path), w, h, q)


def variant_rotate1(path, w=300, h=450, q=80, angle=1):
    """Поворот на 1 градус (не 12°, как в C10 hard_dup) — тонкое искажение по заданию."""
    im = _load_rgb(path)
    rotated = im.rotate(angle, resample=Image.BICUBIC, fillcolor=(255, 255, 255), expand=False)
    return _to_data_url_from_im(rotated, w, h, q)


def variant_crop5(path, w=300, h=450, q=80, frac=0.05):
    """Обрезка 5% с каждого края."""
    im = _load_rgb(path)
    ww, hh = im.size
    cropped = im.crop((int(ww * frac), int(hh * frac), int(ww * (1 - frac)), int(hh * (1 - frac))))
    return _to_data_url_from_im(cropped, w, h, q)


def variant_composite(path, w=300, h=450, q=80, angle=1, frac=0.05):
    """Трудный случай: поворот + обрезка одновременно (та же комбинация, что C10 hard_dup
    использовал на 12°/4%, здесь на тонких параметрах замена №3 — 1°/5%)."""
    im = _load_rgb(path)
    rotated = im.rotate(angle, resample=Image.BICUBIC, fillcolor=(255, 255, 255), expand=False)
    ww, hh = rotated.size
    cropped = rotated.crop((int(ww * frac), int(hh * frac), int(ww * (1 - frac)), int(hh * (1 - frac))))
    return _to_data_url_from_im(cropped, w, h, q)


VARIANTS = {
    "downscale_60pct": variant_downscale,
    "recompress_q30": variant_recompress,
    "rotate_1deg": variant_rotate1,
    "crop_5pct": variant_crop5,
    "composite_rotate_crop": variant_composite,
}


def embed_mm(model, data_url, retries=8, timeout=90):
    """Один вызов эмбеддинга с ретраями. Возвращает
    (vector_or_None, cost_usd_or_None, error_or_None).

    Бесплатные модели (`:free`) на этом стенде регулярно отвечают HTTP 503 'Service is
    overloaded' под параллельной нагрузкой (замерено на этом же прогоне: 8 из 17 вызовов
    отказали при 4 одновременных воркерах) — backoff здесь длиннее обычного (старт 4с,
    множитель 1.8, потолок 25с) и ретраев больше (8), чтобы отличать настоящий отказ модели
    от перегрузки бесплатного тира в моменте."""
    body = {"model": model, "input": data_url}
    last_err = None
    for attempt in range(retries):
        try:
            r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=timeout)
        except Exception as e:
            last_err = f"transport: {e}"
            time.sleep(min(25.0, 4.0 * (1.8 ** attempt)))
            continue
        resp = r.get("response") or {}
        if "data" in resp and resp["data"]:
            vec = resp["data"][0]["embedding"]
            cost = (resp.get("usage", {}) or {}).get("cost")
            return vec, cost, None
        last_err = json.dumps(resp, ensure_ascii=False)[:300]
        # код 404 "No endpoints found" — модель снята/переименована у провайдера, это
        # НЕ перегрузка и ретраями не лечится (измерено: 3/3 одинаковый 404 без улучшения
        # на nvidia/llama-nemotron-embed-vl-1b-v2:free, 2026-11-21). Не жжём бюджет ретраев
        # на заведомо постоянную ошибку.
        err_code = (resp.get("error") or {}).get("code")
        if err_code == 404:
            return None, None, last_err
        time.sleep(min(25.0, 4.0 * (1.8 ** attempt)))
    return None, None, last_err


def slug(model):
    return model.replace("/", "_").replace(":", "_")


def originals_cache_path(model):
    return os.path.join(RAW_DIR, f"originals_{slug(model)}.json")


def load_or_fetch_originals(model, ids, paths, sleep_between=0.4):
    """Возвращает (vectors: {id: vec_or_None}, fail_log: [...], total_cost: float).
    Пишет/дочитывает кэш raw/originals_<model>.json — повторный запуск не бьёт по API
    заново, и партиальный прогон можно продолжить (кэш пишется после каждой картинки)."""
    os.makedirs(RAW_DIR, exist_ok=True)
    path = originals_cache_path(model)
    if os.path.exists(path):
        cached = json.load(open(path, encoding="utf-8"))
        vectors = cached["vectors"]
        fail_log = cached.get("fail_log", [])
        total_cost = cached.get("total_cost", 0.0)
        # ВАЖНО: ранее помеченный FAIL (ключ есть, vec=None) без этого условия никогда не
        # ретраился повторным запуском — "sid not in vectors" его не видит. Честные нули
        # из §8.11 обязаны быть настоящими "модель не ответила после ретраев", а не
        # "мы просто больше не спрашивали".
        missing = [sid for sid in ids if vectors.get(sid) is None]
        if not missing:
            print(f"  [cache] {model}: {len(vectors)} оригиналов загружены из {path}")
            return vectors, fail_log, total_cost
        print(f"  [cache] {model}: {len(ids) - len(missing)} есть, {len(missing)} считаем/доретраиваем")
    else:
        vectors, fail_log, total_cost = {}, [], 0.0
        missing = ids

    for sid in missing:
        vec, cost, err = embed_mm(model, variant_original(paths[sid]))
        vectors[sid] = vec
        if cost:
            total_cost += cost
        if vec is None:
            fail_log.append({"id": sid, "stage": "original", "error": err})
            print(f"    {model} orig {sid}: FAIL ({err[:80] if err else '?'})")
        else:
            print(f"    {model} orig {sid}: ok")
        json.dump({"vectors": vectors, "fail_log": fail_log, "total_cost": total_cost},
                   open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        time.sleep(sleep_between)
    return vectors, fail_log, total_cost


_cache_lock = threading.Lock()


def load_or_fetch_originals_concurrent(model, ids, paths, max_workers=4):
    """Та же задача, что load_or_fetch_originals, но недостающие картинки считаются
    параллельно (вызовы I/O-bound — сетевой вебхук + поллинг execution, GIL отпускается
    на time.sleep/urllib) пулом потоков. Нужно только для скорости на бесплатном стенде:
    сериализованный прогон 180 вызовов занял >10 минут на первые 13 картинок из-за
    HTTP 503 overload + ретраев. Кэш пишется под локом после каждого завершённого вызова —
    партиальный прогон переживает kill/restart так же, как последовательная версия."""
    os.makedirs(RAW_DIR, exist_ok=True)
    path = originals_cache_path(model)
    if os.path.exists(path):
        cached = json.load(open(path, encoding="utf-8"))
        vectors = cached["vectors"]
        fail_log = cached.get("fail_log", [])
        total_cost = cached.get("total_cost", 0.0)
    else:
        vectors, fail_log, total_cost = {}, [], 0.0

    missing = [sid for sid in ids if vectors.get(sid) is None]
    if not missing:
        print(f"  [cache] {model}: {len(vectors)} оригиналов загружены из {path}")
        return vectors, fail_log, total_cost
    # старые записи FAIL для sid из missing будут задвоены в fail_log новой записью при
    # повторном отказе — это ожидаемо и честно (видно, сколько раз модель отказала всего).
    print(f"  [cache] {model}: {len(ids) - len(missing)} есть, {len(missing)} считаем/доретраиваем (workers={max_workers})")

    state = {"vectors": vectors, "fail_log": fail_log, "total_cost": total_cost}

    def work(sid):
        vec, cost, err = embed_mm(model, variant_original(paths[sid]))
        return sid, vec, cost, err

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(work, sid): sid for sid in missing}
        for fut in as_completed(futures):
            sid, vec, cost, err = fut.result()
            with _cache_lock:
                state["vectors"][sid] = vec
                if cost:
                    state["total_cost"] += cost
                if vec is None:
                    state["fail_log"].append({"id": sid, "stage": "original", "error": err})
                    print(f"    {model} orig {sid}: FAIL ({err[:80] if err else '?'})")
                else:
                    print(f"    {model} orig {sid}: ok")
                json.dump(state, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    return state["vectors"], state["fail_log"], state["total_cost"]
