#!/usr/bin/env python3
"""Снять настоящие скрины живого стенда n8n.lessons.tellian.io для Семинара 10 (issue #311).

Та же техника, что Семинар 8/9 (`notes/mcp-limitations.md` [#233-8], апдейт 2026-10-20):
headless-браузер поднимается через обход `~/.cache/page-shot-libs/x`
(`tools/presentation-build/setup_page_shots.sh`), логин по `N8N_UI_EMAIL`/`N8N_UI_PASSWORD`.

Запуск — ОБЯЗАТЕЛЬНО после `source` того скрипта в ТОЙ ЖЕ оболочке (иначе
LD_LIBRARY_PATH не доживёт, и chromium упадёт с exitCode=127):

    source tools/presentation-build/setup_page_shots.sh
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    python3 library/seminars/sem-10/stend/n8n_shots.py                  # все 4 кейса
    python3 library/seminars/sem-10/stend/n8n_shots.py --only case4     # ровно один

Секреты читаются из окружения, в этот файл не вписаны и в вывод не печатаются.

Снимает для всех 4 кейсов Семинара 10:
  - холст воркфлоу (широкий кроп главного пути, без боковых панелей/поповеров)
  - панель параметров (NDV) для 1-2 узлов, несущих механику кейса, в РАЗВЁРНУТОМ виде

`--only` сужает прогон до перечисленных кейсов — кадры остальных остаются как были.
Кейс 4 переписан 2026-11-12 на рабочую модель, и его новые кадры носят новые имена
(`case4-canvas-working`, `case4-embed-working-panel`, `case4-cosine-panel`): прежние
titan-кадры (`case4-canvas.png`, `case4-embed-image-panel.png`) кейсу ещё нужны как
запись не удавшейся попытки и не перезаписываются.
"""
import os
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

HOST = "https://n8n.lessons.tellian.io"
EMAIL = os.environ["N8N_UI_EMAIL"]
PASSWORD = os.environ["N8N_UI_PASSWORD"]
OUT = Path(__file__).parent / "n8n-screenshots-raw"
OUT.mkdir(exist_ok=True)

# id из README.md — Кейс 1 и Кейс 4 существовали до этой сессии, Кейс 2/3 созданы ею
# (sborka.py::case2_chunking_workflow / case3_search_workflow).
WF_CASE1 = "JNXhpgEoOC937W5g"  # С10 · Кейс 1 — векторное хранилище (демо-экран)
WF_CASE2 = "oLiJHPEy6uII7W5J"  # С10 · Кейс 2 — нарезка документа (демо-экран)
WF_CASE3 = "xAFFyyTJLYzZSvk8"  # С10 · Кейс 3 — виды поиска + реранкер (демо-экран)
WF_CASE4 = "s08s4eHIo6zbP8JQ"  # С10 · Кейс 4 — мультимодальный эмбеддинг (демо-экран)

VIEW_CANVAS = {"width": 2200, "height": 1250}
VIEW_PANEL = {"width": 1600, "height": 1000}

# Поля, вне которых кадр не режется: слева боковая панель n8n, сверху крошки с именем
# сценария, снизу полоса журналов (см. n8n_shots.py Семинара 9, та же мера).
SAFE = {"x0": 58, "y0": 70, "x1": 2188, "y1": 1202}

JS_KILL_CHECKLIST = """
() => {
  const panels = Array.from(document.querySelectorAll('div,section,aside')).filter(e => {
    const r = e.getBoundingClientRect();
    return r.width > 200 && r.width < 700 && (e.innerText || '').trim().startsWith('Production Checklist');
  });
  if (!panels.length) return 'нет';
  const panel = panels[panels.length - 1];
  const btn = panel.querySelector('button, [role="button"], svg, i');
  if (btn) { btn.dispatchEvent(new MouseEvent('click', {bubbles: true})); }
  const still = document.body.innerText.includes('Production Checklist');
  if (still) { panel.style.display = 'none'; return 'снята из разметки'; }
  return 'закрыта кнопкой';
}
"""

JS_RECTS = """
(sels) => {
  const out = [];
  for (const s of sels) {
    for (const e of document.querySelectorAll(s)) {
      const r = e.getBoundingClientRect();
      if (r.width > 0 && r.height > 0) out.push([r.x, r.y, r.right, r.bottom]);
    }
  }
  return out;
}
"""


def login(page):
    page.goto(f"{HOST}/signin", wait_until="networkidle")
    time.sleep(1.5)
    page.fill('input[name="emailOrLdapLoginId"]', EMAIL)
    page.fill('input[name="password"]', PASSWORD)
    page.click('[data-test-id="form-submit-button"]')
    page.wait_for_load_state("networkidle")
    time.sleep(1.5)


def safe_box(page):
    vp = page.viewport_size
    return {"x0": 58, "y0": 70, "x1": vp["width"] - 12, "y1": vp["height"] - 48}


def _union(rects, pad, safe, pad_bottom=None):
    x0 = min(r[0] for r in rects) - pad
    y0 = min(r[1] for r in rects) - pad
    x1 = max(r[2] for r in rects) + pad
    y1 = max(r[3] for r in rects) + (pad if pad_bottom is None else pad_bottom)
    x0 = max(x0, safe["x0"]); y0 = max(y0, safe["y0"])
    x1 = min(x1, safe["x1"]); y1 = min(y1, safe["y1"])
    return {"x": x0, "y": y0, "width": x1 - x0, "height": y1 - y0}


def clip_canvas(page, pad=78):
    rects = page.evaluate(JS_RECTS, ['[data-test-id="canvas-node"]', '[data-test-id="edge-label"]'])
    return _union(rects, pad, safe=safe_box(page), pad_bottom=98)


def clip_panel(page, pad=14):
    col = page.evaluate(JS_RECTS, ['[data-test-id="node-parameters"]'])[0]
    rects = page.evaluate(JS_RECTS, [
        '[data-test-id="tab-params"]',
        '[data-test-id="node-parameters"] [data-test-id="parameter-item"]',
        '[data-test-id="collection-parameter-add"]',
        '.el-popper:not([style*="display: none"])',
    ])
    box = _union(rects, pad, safe={"x0": 24, "y0": 26, "x1": col[2] + 500, "y1": 990})
    x0, x1 = col[0] - 2, col[2] + 2
    return {"x": x0, "y": box["y"], "width": x1 - x0, "height": box["height"]}


def widen_params(page):
    """Сдвинуть разделитель панелей влево: поле параметров занимает кадр, пустой вход — нет."""
    try:
        handle = page.locator('[data-test-id="panel-drag-button"]').first
        box = handle.bounding_box()
        page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
        page.mouse.down()
        page.mouse.move(60, box["y"] + box["height"] / 2, steps=18)
        page.mouse.up()
        time.sleep(0.8)
    except Exception as exc:
        print(f"    (разделитель не сдвинулся: {exc})")


def open_canvas(page, wf_id):
    page.set_viewport_size(VIEW_CANVAS)
    page.goto(f"{HOST}/workflow/{wf_id}", wait_until="networkidle")
    time.sleep(2.5)  # холст рисуется асинхронно (vue-flow)
    print("    карточка Production Checklist:", page.evaluate(JS_KILL_CHECKLIST))
    page.click('[data-test-id="zoom-to-fit"]')
    time.sleep(1.2)


def open_node_panel(page, node_name):
    """Двойной клик по ноде открывает NDV (Node Detail View) — панель параметров."""
    node = page.locator(f'[data-test-id="canvas-node"]:has-text("{node_name}")').first
    node.dblclick()
    time.sleep(1.2)


def close_node_panel(page):
    page.keyboard.press("Escape")
    time.sleep(0.6)


def expand_code_editor(page):
    """Code-узлы n8n показывают редактор в сжатом виде по умолчанию — разворачиваем
    (клик по иконке expand), иначе длинный JS срезается (С9-урок: сжатый вид обрезает
    текст, см. `n8n_shots.py` Семинара 9, k2-promt-baza)."""
    try:
        btn = page.locator('[class*="expand"], button[title*="Expand" i]').first
        if btn.count() and btn.is_visible():
            btn.click()
            time.sleep(1)
    except Exception as exc:
        print(f"    (кнопка expand не найдена: {exc})")


def save_canvas(page, wf_id, name, what):
    open_canvas(page, wf_id)
    path = OUT / f"{name}.png"
    page.screenshot(path=str(path), clip=clip_canvas(page))
    print(f"  {name}.png — холст: {what}")


def save_panel(page, node_name, name, what, expand_editor=False):
    page.set_viewport_size(VIEW_PANEL)
    time.sleep(0.6)
    open_node_panel(page, node_name)
    widen_params(page)
    if expand_editor:
        expand_code_editor(page)
    path = OUT / f"{name}.png"
    page.screenshot(path=str(path), clip=clip_panel(page))
    print(f"  {name}.png — панель узла «{node_name}»: {what}")
    close_node_panel(page)


ALL_CASES = ("case1", "case2", "case3", "case4")


def main(cases=ALL_CASES):
    """Снять кадры для перечисленных кейсов. `cases` сужается флагом `--only`.

    Выключатель заведён 2026-11-12: прогон ради ОДНОГО переписанного кейса не должен
    перезаснимать (то есть перезаписывать) кадры трёх остальных — они уже отобраны,
    обрезаны и стоят на слайдах; новый снимок того же холста отличается хотя бы зумом,
    и фигуры пришлось бы пересобирать без причины.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport=VIEW_CANVAS, device_scale_factor=2)
        login(page)

        # --- Кейс 1 — векторное хранилище -------------------------------------------
        if "case1" in cases:
            save_canvas(page, WF_CASE1, "case1-canvas",
                        "Embed query → Simple Vector Store (cosine top-1) → Answer (RAG)")
            save_panel(page, "Simple Vector Store (cosine top-1)", "case1-vector-store-panel",
                       "код cosine top-1 по присланным эмбеддингам документов", expand_editor=True)
            save_panel(page, "Answer (RAG)", "case1-answer-panel",
                       "промт ответа только по найденному куску")

        # --- Кейс 2 — нарезка документа -----------------------------------------------
        if "case2" in cases:
            save_canvas(page, WF_CASE2, "case2-canvas",
                        "Документ → нарезка фикс. размером → нарезка по предложениям → сравнение")
            save_panel(page, "Нарезка фиксированным размером", "case2-fixed-chunk-panel",
                       "код нарезки фиксированным размером (порт chunk_fixed)", expand_editor=True)
            save_panel(page, "Нарезка по границам предложений", "case2-structural-chunk-panel",
                       "код нарезки по границам предложений (порт chunk_structural)", expand_editor=True)

        # --- Кейс 3 — виды поиска + реранкер -------------------------------------------
        if "case3" in cases:
            save_canvas(page, WF_CASE3, "case3-canvas",
                        "keyword → embed query → cosine → RRF fusion → LLM-реранкер → разбор")
            save_panel(page, "RRF fusion (hybrid)", "case3-rrf-panel",
                       "код RRF-слияния (k=60) keyword+vector рангов", expand_editor=True)
            save_panel(page, "LLM-реранкер (gpt-4o-mini)", "case3-reranker-panel",
                       "тело запроса LLM-реранкера: промт с top-N кандидатами")

        # --- Кейс 4 — мультимодальный эмбеддинг -----------------------------------------
        # Сценарий переписан 2026-11-12 на РАБОЧУЮ модель + узел сравнения
        # (sborka.py::case4_multimodal_workflow). Кадры прежнего, titan-холста
        # (case4-canvas.png / case4-embed-image-panel.png) НЕ перезаписываются: они
        # остаются записью не удавшейся попытки, которую кейс рассказывает. Новым
        # кадрам — новые имена.
        if "case4" in cases:
            save_canvas(page, WF_CASE4, "case4-canvas-working",
                        "Запрос-скан + индекс → Тело запроса: nemotron-3.5-embed-1b → "
                        "Эмбеддинги сканов → Косинусное расстояние до индекса")
            save_panel(page, "Тело запроса: nemotron-3.5-embed-1b",
                       "case4-embed-working-panel",
                       "имя рабочей модели литералом + сборка тела: запрос и индекс одним вызовом",
                       expand_editor=True)
            save_panel(page, "Косинусное расстояние до индекса", "case4-cosine-panel",
                       "код косинуса: вектор запроса против векторов индекса, ближайший + отрыв",
                       expand_editor=True)

        browser.close()


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="+", choices=ALL_CASES, default=list(ALL_CASES),
                    metavar="CASE", help=f"снять кадры только этих кейсов, из: {', '.join(ALL_CASES)}")
    main(tuple(ap.parse_args().only))
