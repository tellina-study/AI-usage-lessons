#!/usr/bin/env python3
"""Живой прогон демо-сценария «С10 · Кейс 4 — мультимодальный эмбеддинг (демо-экран)»
(`sborka.py::case4_multimodal_workflow`, вебхук `s10-case4-mm`) на НАСТОЯЩИХ сканах
CORD из `corpus/cord_sample/` — не на синтетической картинке.

Переписан 2026-11-12 вместе со сценарием. Прежняя версия слала одну крошечную
картинку (`tinyA.png.b64`) в сценарий из одного узла на `amazon/titan-embed-image-v1` —
той модели, которая отдавала битово одинаковый вектор на разные картинки. Сейчас
прогоняется вся механика кейса: запрос → эмбеддинг → косинус до индекса → ближайший.

Что в прогоне:
  - **запрос** — `receipt_07`, пересобранный ЖЁСТКОЙ аугментацией (поворот 12° + обрезка
    4% с каждого края + пересжатие), то есть имитация пересъёмки того же чека телефоном
    под углом. Взята именно жёсткая, а не мягкая: на ней стоит заглавное число кейса
    (recall@1 = 0,967 у рабочей модели против 0,233 у perceptual hash,
    `raw/case4_mm_full_retrieval.json` часть A) — демо-экран обязан показывать тот
    случай, о котором кейс говорит, а не самый лёгкий;
  - **индекс** — 5 ОРИГИНАЛОВ: `receipt_07` (верный ответ) + 4 чужих чека. Аугментации
    (`hard_dup`) — прямой порт из `case4_full_retrieval_30.py`, не самостоятельная
    реализация, чтобы демо-экран и замер не расходились в том, что считают «поворотом».

Подписи сканов (`label`) — наши, для проверки глазами; в модель уходят ТОЛЬКО пиксели
(`image`), подпись в тело запроса не попадает (см. узел «Тело запроса …»: в `input`
уходит `s.image`).

**Это демо-экран механики, а не замер.** Число этого прогона — одно попадание на
индексе из 5, а не recall по выборке. Числа кейса живут в
`raw/case4_mm_full_retrieval.json` / `raw/case4_working_mm_results.json` (30 сканов,
части A/B/C) и этим прогоном не пересчитываются.

Запуск:
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    cd library/seminars/sem-10/stend/measure && python3 trigger_case4_mm.py
Протокол выполнения ложится в `../raw/case4_mm_working_execution.json`.
"""
import base64
import io
import json
import time
import urllib.parse

from PIL import Image

from harness_call import get_execution, post_form

QUERY_ID = "receipt_07"
INDEX_IDS = ["receipt_07", "receipt_00", "receipt_11", "receipt_15", "receipt_18"]
COS_NODE = "Косинусное расстояние до индекса"
OUT = "../raw/case4_mm_working_execution.json"

samples = {s["id"]: f"../{s['file']}" for s in json.load(open("../corpus/cord_sample_meta.json"))}


def to_data_url(path, w=300, h=450, q=80):
    """Порт case4_full_retrieval_30.py::to_data_url — оригинал в рабочем разрешении."""
    im = Image.open(path).convert("RGB").resize((w, h))
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=q)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


def hard_dup(path, w=300, h=450):
    """Порт case4_full_retrieval_30.py::hard_dup — поворот 12° + обрезка 4% краёв."""
    im = Image.open(path).convert("RGB")
    hard = im.rotate(12, expand=True, fillcolor=(255, 255, 255))
    ww, hh = hard.size
    hard = hard.crop((int(ww * 0.04), int(hh * 0.04), int(ww * 0.96), int(hh * 0.96)))
    hard = hard.resize((w, h))
    buf = io.BytesIO()
    hard.save(buf, format="JPEG", quality=80)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


def label_of(scan_id):
    return "чек " + scan_id.split("_")[1]


payload = {
    "query": {"label": f"{label_of(QUERY_ID)}, снятый заново под углом 12°",
              "image": hard_dup(samples[QUERY_ID])},
    "index": [{"label": label_of(i), "image": to_data_url(samples[i])} for i in INDEX_IDS],
}
print(f"запрос: {payload['query']['label']}")
print(f"индекс: {', '.join(s['label'] for s in payload['index'])}")
print(f"объём тела формы: {len(json.dumps(payload)) // 1024} КБ")

resp = post_form("s10-case4-mm", [json.dumps(payload, ensure_ascii=False)])
exec_id = urllib.parse.urlparse(resp.get("formWaitingUrl", "")).path.rstrip("/").split("/")[-1]
print("exec_id", exec_id)

ex, deadline = None, time.time() + 120
while time.time() < deadline:
    time.sleep(2)
    ex = get_execution(exec_id)
    run = ex.get("data", {}).get("resultData", {}).get("runData", {})
    if COS_NODE in run or ex.get("status") in ("error", "crashed"):
        break

run = ex.get("data", {}).get("resultData", {}).get("runData", {})
print("status:", ex.get("status"), "| узлы с данными:", list(run))
if COS_NODE in run:
    entry = run[COS_NODE][0]
    if entry.get("error"):
        print("ОШИБКА узла:", json.dumps(entry["error"], ensure_ascii=False)[:800])
    else:
        print("---- экран результата ----")
        print(entry["data"]["main"][0][0]["json"]["summary"])
else:
    for name, entries in run.items():
        if entries[0].get("error"):
            print(f"ОШИБКА в узле {name}:", json.dumps(entries[0]["error"], ensure_ascii=False)[:800])

json.dump(ex, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("протокол:", OUT)
