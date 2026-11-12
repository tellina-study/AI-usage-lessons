#!/usr/bin/env python3
"""Кейс 4 (issue #311) — ГРАНИЦЫ ПРИМЕНИМОСТИ рабочей мультимодальной модели по
сжатию, разрешению и качеству запроса.

Прямой вопрос владельца курса: «показать границы применимости по сжатию/размерам,
качеству». До этого прохода таких данных у кейса не было: раздел
`raw/case4_resolution_probe.json` мерил разрешение у БИТОЙ модели
(`amazon/titan-embed-image-v1`, cosine=1,0 на любых двух картинках), а полный замер
`raw/case4_mm_full_retrieval.json` снят в одной единственной точке качества.

УСТРОЙСТВО ЗАМЕРА — ИНДЕКС НЕ ДЕГРАДИРУЕТ, ДЕГРАДИРУЕТ ТОЛЬКО ЗАПРОС.
Все 30 оригиналов CORD лежат в индексе в ОПОРНОМ виде 300×450 JPEG q80 — ровно том,
с которым работает весь Кейс 4. Деградирует только картинка-запрос. Это реалистичный
случай: в заявке приходит пережатое/мелкое/смазанное фото, а в хранилище лежит
нормальный скан. Обратный случай (деградировал индекс) этим замером НЕ покрыт.

Запрос — дубль того же чека, построенный ДЕТЕРМИНИРОВАННО (без `random`) теми же
преобразованиями, что в `case4_full_retrieval_30.py`:
  - мягкий дубль  (`soft_dup`) — пересканировали: resize×0,97 → целевой размер;
  - жёсткий дубль (`hard_dup`) — сняли под углом: поворот 12° + обрезка 4% краёв.
Здесь они параметризованы по (размер, качество JPEG, радиус размытия) — геометрия
преобразования не менялась, добавлены только параметры рендера.

ТРИ ОСИ, ПО ЧЕТЫРЕ ТОЧКИ, ПЕРВАЯ — ОПОРНАЯ (одна и та же для всех трёх осей):
  сжатие:     300×450 q80 (опора) · q50 · q25 · q10
  разрешение: q80 300×450 (опора) · 150×225 · 100×150 · 64×96
  качество:   300×450 q80 размытие 0 (опора) · 1,0 · 2,0 · 3,0 пикселя (GaussianBlur)

МЕТРИКИ НА ТОЧКУ: recall@1 (ближайший из 30 оригиналов — тот же чек?), среднее
косинусное сходство с ВЕРНЫМ оригиналом, среднее с ближайшим НЕВЕРНЫМ, запас между
ними (margin), средний размер строки base64 и его доля от опорной точки.

ДВЕ ЗАДАЧИ: мягкий дубль и жёсткий дубль — по всем 10 точкам каждая.
ТРИ СЧИТАЮЩИХ: `nvidia/nemotron-3.5-embed-1b:free` (API, `--engine api`), локальный
CLIP ViT-B/32 (`--engine clip`, бесплатно, вторая точка сравнения) и perceptual hash
(average-hash 8×8, считается в обоих прогонах локально — классическая контрастная
линия, бесплатная).

Исход заранее не известен. Если модель держится до q10 — так и записывается; точки под
красивый вывод не подбираются.

Запуск:
  set -a; . /home/harness/.n8n-lab-credentials; set +a
  python3 case4_quality_limits.py --engine clip   # быстрый бесплатный прогон (и проверка логики)
  python3 case4_quality_limits.py --engine api    # рабочая модель через вебхук s10-raw-openrouter
"""
import argparse
import base64
import io
import json
import os
import time

from PIL import Image, ImageFilter

MM_MODEL = "nvidia/nemotron-3.5-embed-1b:free"
CLIP_MODEL_NAME = "openai/clip-vit-base-patch32"

# (ось, метка точки, w, h, качество JPEG, радиус размытия)
ANCHOR = ("anchor", "300x450_q80_blur0", 300, 450, 80, 0.0)
POINTS = [
    ANCHOR,
    ("compression", "300x450_q50", 300, 450, 50, 0.0),
    ("compression", "300x450_q25", 300, 450, 25, 0.0),
    ("compression", "300x450_q10", 300, 450, 10, 0.0),
    ("resolution", "150x225_q80", 150, 225, 80, 0.0),
    ("resolution", "100x150_q80", 100, 150, 80, 0.0),
    ("resolution", "64x96_q80", 64, 96, 80, 0.0),
    ("quality", "blur1.0", 300, 450, 80, 1.0),
    ("quality", "blur2.0", 300, 450, 80, 2.0),
    ("quality", "blur3.0", 300, 450, 80, 3.0),
]
# опорная точка — первая точка КАЖДОЙ оси (один и тот же рендер, не три разных)
AXES = {
    "compression": ["300x450_q80_blur0", "300x450_q50", "300x450_q25", "300x450_q10"],
    "resolution": ["300x450_q80_blur0", "150x225_q80", "100x150_q80", "64x96_q80"],
    "quality": ["300x450_q80_blur0", "blur1.0", "blur2.0", "blur3.0"],
}

samples = json.load(open("../corpus/cord_sample_meta.json"))
ids = [s["id"] for s in samples]
paths = {s["id"]: f"../{s['file']}" for s in samples}


# ---------------------------------------------------------------- общие примитивы
def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


def _encode(im, q):
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=q)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


def to_data_url(path, w=300, h=450, q=80):
    """ИНДЕКС. Ровно as-is из case4_full_retrieval_30.py — не деградирует никогда."""
    im = Image.open(path).convert("RGB").resize((w, h))
    return _encode(im, q)


def soft_dup(path, w=300, h=450, q=80, blur=0.0):
    """Мягкий дубль (пересканировали). Геометрия как в case4_full_retrieval_30.py:
    resize×0,97 → целевой размер. Параметры рендера добавлены."""
    im = Image.open(path).convert("RGB")
    out = im.resize((max(1, int(im.width * 0.97)), max(1, int(im.height * 0.97)))).resize((w, h))
    if blur:
        out = out.filter(ImageFilter.GaussianBlur(radius=blur))
    return _encode(out, q)


def hard_dup(path, w=300, h=450, q=80, blur=0.0):
    """Жёсткий дубль (сняли под углом). Геометрия как в case4_full_retrieval_30.py:
    поворот 12° + обрезка 4% краёв → целевой размер."""
    im = Image.open(path).convert("RGB")
    out = im.rotate(12, expand=True, fillcolor=(255, 255, 255))
    ww, hh = out.size
    out = out.crop((int(ww * 0.04), int(hh * 0.04), int(ww * 0.96), int(hh * 0.96)))
    out = out.resize((w, h))
    if blur:
        out = out.filter(ImageFilter.GaussianBlur(radius=blur))
    return _encode(out, q)


def average_hash(pil_im, hash_size=8):
    im = pil_im.convert("L").resize((hash_size, hash_size), Image.LANCZOS)
    pixels = list(im.getdata())
    avg = sum(pixels) / len(pixels)
    return "".join("1" if p > avg else "0" for p in pixels)


def hamming(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def pil_of(data_url):
    raw = base64.b64decode(data_url.split(",", 1)[1])
    return Image.open(io.BytesIO(raw)).convert("RGB")


def b64_len(data_url):
    return len(data_url.split(",", 1)[1])


# ---------------------------------------------------------------- считающие
class ApiEngine:
    """Рабочая мультимодальная модель через вебхук s10-raw-openrouter. Ключ OpenRouter
    остаётся на стороне n8n — здесь его нет и он не нужен."""

    name = "api"
    label = MM_MODEL

    def __init__(self):
        from harness_call import call_raw
        self._call = call_raw
        self.fail_log = []
        self.n_calls = 0
        self.call_s = 0.0

    def embed(self, data_url, tag, retries=4):
        body = {"model": MM_MODEL, "input": data_url}
        last = None
        for attempt in range(retries):
            t0 = time.time()
            r = self._call("https://openrouter.ai/api/v1/embeddings", body, timeout=90, sleep=0.5)
            self.n_calls += 1
            self.call_s += time.time() - t0
            resp = r["response"] or {}
            if "data" in resp:
                if attempt:
                    self.fail_log.append({"tag": tag, "attempt": attempt, "outcome": "recovered_after_retry"})
                return resp["data"][0]["embedding"]
            last = resp
            self.fail_log.append({"tag": tag, "attempt": attempt, "exec_id": r.get("exec_id"),
                                  "error": json.dumps(last, ensure_ascii=False)[:300]})
            time.sleep(2.0 * (attempt + 1))
        self.fail_log.append({"tag": tag, "outcome": "FAILED_after_all_retries"})
        print(f"  !! embed FAILED {tag}: {json.dumps(last, ensure_ascii=False)[:160]}")
        return None


class ClipEngine:
    """Локальный CLIP ViT-B/32 — бесплатно, та же методика, вторая точка сравнения."""

    name = "clip"
    label = CLIP_MODEL_NAME

    def __init__(self):
        import torch
        from transformers import CLIPModel, CLIPProcessor
        os.environ.setdefault("HF_HOME", os.path.join(os.getcwd(), ".hf-cache"))
        t0 = time.time()
        self.torch = torch
        self.model = CLIPModel.from_pretrained(CLIP_MODEL_NAME)
        self.model.eval()
        self.processor = CLIPProcessor.from_pretrained(CLIP_MODEL_NAME)
        self.load_s = round(time.time() - t0, 1)
        print(f"=== CLIP ({CLIP_MODEL_NAME}) загружен за {self.load_s} с ===")
        self.fail_log = []
        self.n_calls = 0
        self.call_s = 0.0

    def embed(self, data_url, tag, retries=1):
        t0 = time.time()
        inputs = self.processor(images=pil_of(data_url), return_tensors="pt")
        with self.torch.no_grad():
            out = self.model.get_image_features(**inputs)
        self.n_calls += 1
        self.call_s += time.time() - t0
        # transformers 5.x: get_image_features возвращает BaseModelOutputWithPooling,
        # а не тензор (в 4.x возвращался тензор, и `out[0]` работал). Спроецированный
        # эмбеддинг картинки (512) лежит в `pooler_output`; `out[0]` здесь — это
        # last_hidden_state [1, 50, 768], НЕ эмбеддинг. Проверено: два разных чека
        # дают cosine 0,8157, один файл дважды — ровно 1,0.
        vec = out.pooler_output[0] if hasattr(out, "pooler_output") else out[0]
        return vec.tolist()


# ---------------------------------------------------------------- замер
def measure_point(engine, dup_fn, point, index_vecs, index_phash, ckpt_path, state):
    axis, label, w, h, q, blur = point
    tag_base = f"{dup_fn.__name__}:{label}"
    print(f"--- {tag_base} ---")
    rows = []
    for sid in ids:
        du = dup_fn(paths[sid], w=w, h=h, q=q, blur=blur)
        row = {"id": sid, "b64_chars": b64_len(du)}

        # perceptual hash — локально, бесплатно, в обоих прогонах одинаково
        qh = average_hash(pil_of(du))
        ph_best, ph_d = None, 999
        ph_own = hamming(qh, index_phash[sid])
        for other, h2 in index_phash.items():
            d = hamming(qh, h2)
            if d < ph_d:
                ph_d, ph_best = d, other
        row.update({"phash_nearest": ph_best, "phash_correct": ph_best == sid,
                    "phash_hamming_to_own": ph_own, "phash_hamming_to_nearest": ph_d})

        vec = engine.embed(du, f"{tag_base}:{sid}")
        if vec is None:
            row["embed_ok"] = False
            rows.append(row)
            continue
        row["embed_ok"] = True
        cos_own, best_wrong, best_wrong_id = None, -2.0, None
        for other in ids:
            if index_vecs.get(other) is None:
                continue
            c = cosine(vec, index_vecs[other])
            if other == sid:
                cos_own = c
            elif c > best_wrong:
                best_wrong, best_wrong_id = c, other
        nearest = sid if (cos_own is not None and cos_own >= best_wrong) else best_wrong_id
        row.update({"nearest": nearest, "correct": nearest == sid,
                    "cos_correct": round(cos_own, 4) if cos_own is not None else None,
                    "cos_best_wrong": round(best_wrong, 4), "best_wrong_id": best_wrong_id})
        rows.append(row)
        if engine.name == "api":
            time.sleep(0.3)

    ok = [r for r in rows if r.get("embed_ok")]
    summary = {
        "axis_point": label, "w": w, "h": h, "jpeg_quality": q, "blur_radius": blur,
        "n_scans": len(rows), "n_embed_ok": len(ok),
        "recall_at_1": round(sum(r["correct"] for r in ok) / len(ok), 4) if ok else None,
        "n_correct": sum(r["correct"] for r in ok),
        "mean_cos_correct": round(sum(r["cos_correct"] for r in ok) / len(ok), 4) if ok else None,
        "mean_cos_best_wrong": round(sum(r["cos_best_wrong"] for r in ok) / len(ok), 4) if ok else None,
        "mean_b64_chars": round(sum(r["b64_chars"] for r in rows) / len(rows), 1),
        "phash_recall_at_1": round(sum(r["phash_correct"] for r in rows) / len(rows), 4),
        "phash_mean_hamming_to_own": round(sum(r["phash_hamming_to_own"] for r in rows) / len(rows), 2),
    }
    if summary["mean_cos_correct"] is not None:
        summary["margin"] = round(summary["mean_cos_correct"] - summary["mean_cos_best_wrong"], 4)
    print("   " + json.dumps({k: summary[k] for k in
                              ("recall_at_1", "mean_cos_correct", "mean_cos_best_wrong",
                               "margin", "mean_b64_chars", "phash_recall_at_1")
                              if k in summary}, ensure_ascii=False))
    state.setdefault(dup_fn.__name__, {})[label] = {"summary": summary, "details": rows}
    json.dump(state, open(ckpt_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return summary


def add_baselines(points_map):
    """Каждое число несёт базу: доля от опорной точки и абсолют опорной рядом."""
    anchor = points_map.get(ANCHOR[1], {}).get("summary")
    if not anchor:
        return
    for label, blob in points_map.items():
        s = blob["summary"]
        s["baseline_anchor_point"] = ANCHOR[1]
        s["anchor_recall_at_1"] = anchor["recall_at_1"]
        s["anchor_mean_b64_chars"] = anchor["mean_b64_chars"]
        s["anchor_margin"] = anchor.get("margin")
        s["b64_chars_share_of_anchor"] = (round(s["mean_b64_chars"] / anchor["mean_b64_chars"], 4)
                                          if anchor["mean_b64_chars"] else None)
        if s["recall_at_1"] is not None and anchor["recall_at_1"]:
            s["recall_delta_vs_anchor"] = round(s["recall_at_1"] - anchor["recall_at_1"], 4)
        if s.get("margin") is not None and anchor.get("margin"):
            s["margin_share_of_anchor"] = round(s["margin"] / anchor["margin"], 4)


def run(engine_name):
    t0 = time.time()
    engine = ApiEngine() if engine_name == "api" else ClipEngine()
    ckpt = f"case4_quality_limits_{engine_name}_ckpt.json"
    state = {}

    print(f"=== ИНДЕКС: 30 оригиналов CORD в опорном виде 300×450 q80 ({engine.label}) ===")
    index_vecs, index_phash, index_b64 = {}, {}, []
    for sid in ids:
        du = to_data_url(paths[sid])
        index_b64.append(b64_len(du))
        # phash индекса — на ПОЛНОМ оригинале, как в case4_full_retrieval_30.py
        index_phash[sid] = average_hash(Image.open(paths[sid]).convert("RGB"))
        index_vecs[sid] = engine.embed(du, f"index:{sid}")
        if engine.name == "api":
            time.sleep(0.3)
    n_idx_ok = sum(1 for v in index_vecs.values() if v is not None)
    print(f"=== индекс готов: {n_idx_ok}/30 векторов ===")

    # порядок: жёсткий дубль первым (различающая задача) — если свободный тариф
    # оборвётся, самое ценное уже снято
    for dup_fn in (hard_dup, soft_dup):
        for p in POINTS:
            measure_point(engine, dup_fn, p, index_vecs, index_phash, ckpt, state)

    for dup in state:
        add_baselines(state[dup])

    out = {
        "engine": engine_name,
        "model": engine.label,
        "embedding_dim": next((len(v) for v in index_vecs.values() if v), None),
        "index": {
            "n_scans": 30, "n_embed_ok": n_idx_ok,
            "form": "300×450 JPEG q80 (опорный вид всего Кейса 4)",
            "degrades": False,
            "mean_b64_chars": round(sum(index_b64) / len(index_b64), 1),
            "phash_source": "average_hash на ПОЛНОМ оригинале файла (как в case4_full_retrieval_30.py)",
        },
        "points": {label: {"axis": axis, "w": w, "h": h, "jpeg_quality": q, "blur_radius": blur}
                   for axis, label, w, h, q, blur in POINTS},
        "axes": AXES,
        "results": state,
        "fail_log": engine.fail_log,
        "timing": {"total_wall_s": round(time.time() - t0, 1), "n_embed_calls": engine.n_calls,
                   "mean_embed_s": round(engine.call_s / engine.n_calls, 3) if engine.n_calls else None},
    }
    path = f"case4_quality_limits_{engine_name}_raw.json"
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\n=== записано {path}; {engine.n_calls} вызовов, "
          f"{out['timing']['total_wall_s']} с, сбоев в журнале: {len(engine.fail_log)} ===")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", choices=["api", "clip"], required=True)
    run(ap.parse_args().engine)
