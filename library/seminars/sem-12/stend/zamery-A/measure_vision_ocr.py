#!/usr/bin/env python3
"""Кейс A, вариант 4 — «картинка и распознанный текст вместе»: в ту же
мультимодальную модель (openai/gpt-4o-mini) уходят ОБА входа одним вызовом —
data-URL картинки (как в варианте 1) и результат OCR текстом (как в варианте 3,
гибриде). Модель читает изображение, имея распознанное как подсказку.

Сопоставимость с прежними тремя — построена, а не заявлена:
  * корпус тот же — `korpus/vyborka.json`, 100 форм, не перенабирается;
  * модель и вызов те же — `harness_a.vision_call` БЕЗ изменений (тот же вебхук
    `s10-raw-openrouter`, тот же `usage.include=true`, та же картинка JPEG q=90
    полного разрешения через `to_data_url`);
  * системный промт тот же — `harness_a.SYS_EXTRACT`, дословно, не правлен;
  * пользовательское сообщение = `build_user_prompt(targets)` варианта 1 ПЛЮС
    блок с OCR-текстом, взятый ДОСЛОВНО из `measure_hybrid.py` (те же слова
    «Текст документа (результат OCR, построчно, без сохранения исходной
    раскладки)») — чтобы подсказка была той же самой подсказкой, что видел
    гибрид, а не новой её формулировкой. Это единственное отличие от варианта 1;
  * OCR НЕ перезапускается — берётся готовый `raw/ocr_results.json`, тот же
    текст, что получил гибрид (иначе числа разъехались бы с вариантом 3).

Промт сознательно НЕ улучшается под этот вариант: задача — измерить метод, а не
подобрать формулировку (задание владельца, 2026-11-25).

Запуск:
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    cd library/seminars/sem-12/stend/zamery-A
    .venv/bin/python3 measure_vision_ocr.py
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from harness_a import SYS_EXTRACT, build_user_prompt, extract_json, to_data_url, vision_call

HERE = Path(__file__).resolve().parent
BASE_DIR = Path("/tmp/s12-corpora/funsd/dataset")
OUT_PATH = HERE / "raw" / "vision_ocr_results.json"

# Дословно тот же блок подсказки, что `measure_hybrid.py` подаёт гибриду — скопирован,
# а не переписан (см. докстринг: подсказка обязана быть той же подсказкой).
OCR_BLOCK = ("\n\nТекст документа (результат OCR, построчно, без сохранения исходной "
             "раскладки):\n---\n{}\n---")


def run_one(form, ocr_text):
    fid = form["form_id"]
    img_path = BASE_DIR / form["split"] / "images" / form["img"]
    data_url = to_data_url(img_path)
    user = build_user_prompt(form["targets"]) + OCR_BLOCK.format(ocr_text)
    t0 = time.time()
    r = vision_call(SYS_EXTRACT, user, data_url)
    r["wall_s_outer"] = round(time.time() - t0, 2)
    r["parsed"] = extract_json(r["content"])
    return fid, r


def main():
    corpus = json.load(open(HERE / "korpus" / "vyborka.json"))
    ocr = json.load(open(HERE / "raw" / "ocr_results.json"))["per_form"]
    out = {}
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(run_one, form, ocr[form["form_id"]]["text_joined"]): form["form_id"]
                for form in corpus}
        for fut in as_completed(futs):
            fid, r = fut.result()
            out[fid] = r
            ok = r["parsed"] is not None
            print(fid, f"{r['wall_s_outer']}s", "cost=", r.get("cost"), "parsed_ok=", ok,
                  flush=True)
    total = time.time() - t0
    total_cost = sum((out[f].get("cost") or 0) for f in out)
    print(f"ИТОГО {total:.1f}s, {len(out)} форм, цена ${total_cost:.4f}")
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump({"meta": {"model": "openai/gpt-4o-mini (картинка + OCR-текст одним вызовом)",
                             "n_forms": len(out), "total_cost": round(total_cost, 6),
                             "total_wall_s": round(total, 2)},
                   "per_form": out}, fh, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
