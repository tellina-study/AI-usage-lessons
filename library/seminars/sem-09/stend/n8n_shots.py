#!/usr/bin/env python3
"""Снять настоящие скрины живого стенда n8n.lessons.tellian.io для Семинара 9 (issue #299).

Логин по `N8N_UI_EMAIL`/`N8N_UI_PASSWORD` из `/home/harness/.n8n-lab-credentials` — тот же
путь, что сработал для Семинара 8 (`notes/mcp-limitations.md` [#233-8], апдейт 2026-10-20):
headless-браузер поднимается через обход `~/.cache/page-shot-libs/x`
(`tools/presentation-build/setup_page_shots.sh`), без root.

Запуск — ОБЯЗАТЕЛЬНО после `source` того скрипта в той же оболочке:

    source tools/presentation-build/setup_page_shots.sh
    python3 library/seminars/sem-09/stend/n8n_shots.py

Секреты читаются из окружения, в этот файл не вписаны и в вывод не печатаются.
"""
import os
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

HOST = "https://n8n.lessons.tellian.io"
EMAIL = os.environ["N8N_UI_EMAIL"]
PASSWORD = os.environ["N8N_UI_PASSWORD"]
OUT = Path(__file__).parent / "n8n-screenshots-raw"
OUT.mkdir(exist_ok=True)

WF_V1 = "nT26QhET2tQ8fEle"  # С9 · Кейс 1, версия 1 — отвечает свободно (самоотчёт)
WF_V2 = "3bcRZrtG8i5f3O9Z"  # С9 · Кейс 1, версия 2 — проверка по пункту базы

# formWaitingUrl двух УЖЕ сделанных прогонов (не новые заявки — простой GET уже готовой
# страницы результата, см. notes/mcp-limitations.md [#233-5]): execution 606 (версия 1,
# вопрос «Как перенести занятие, если я заболел?») и execution 612 (та же вопрос, версия 2).
RESULT_URLS = {
    "case1-v1-result-screen": (
        "https://n8n.lessons.tellian.io/form-waiting/606"
        "?signature=0e34cecdffbe5adfa62aeb1f1c2b76ca08e1ae7051d80bc1f948139abaece4ee"),
    "case1-v2-result-screen": (
        "https://n8n.lessons.tellian.io/form-waiting/612"
        "?signature=194482868500b239cd30e4a685a897063736983f296f3240298433526803783b"),
}


def login(page):
    page.goto(f"{HOST}/signin", wait_until="networkidle")
    time.sleep(1.5)
    page.fill('input[name="emailOrLdapLoginId"]', EMAIL)
    page.fill('input[name="password"]', PASSWORD)
    page.click('[data-test-id="form-submit-button"]')
    page.wait_for_load_state("networkidle")
    time.sleep(1.5)


def open_workflow(page, wf_id):
    page.goto(f"{HOST}/workflow/{wf_id}", wait_until="networkidle")
    time.sleep(2.5)  # холст рисуется асинхронно (vue-flow), сеть уже "idle", кадр ещё нет


def shoot_canvas(page, name):
    path = OUT / f"{name}.png"
    page.screenshot(path=str(path))
    print(f"  {name}.png — канвас")


def open_node_panel(page, node_name):
    """Двойной клик по ноде открывает NDV (Node Detail View) — панель параметров."""
    node = page.locator(f'[data-test-id="canvas-node"]:has-text("{node_name}")').first
    node.dblclick()
    time.sleep(1.2)


def close_node_panel(page):
    page.keyboard.press("Escape")
    time.sleep(0.6)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1600, "height": 1000})
        login(page)

        # --- версия 1: холст + панель промта -----------------------------------------
        open_workflow(page, WF_V1)
        shoot_canvas(page, "case1-v1-canvas")
        open_node_panel(page, "Answer (free self-report)")
        page.screenshot(path=str(OUT / "case1-v1-prompt-panel.png"))
        print("  case1-v1-prompt-panel.png — промт версии 1 (свободный ответ)")
        close_node_panel(page)

        # --- версия 2: холст + панель промта + панель детерминированной проверки -----
        open_workflow(page, WF_V2)
        shoot_canvas(page, "case1-v2-canvas")
        open_node_panel(page, "Answer with grounding (structured)")
        page.screenshot(path=str(OUT / "case1-v2-prompt-panel.png"))
        print("  case1-v2-prompt-panel.png — промт + схема версии 2")
        close_node_panel(page)
        open_node_panel(page, "Grounded in known KB item?")
        page.screenshot(path=str(OUT / "case1-v2-check-panel.png"))
        print("  case1-v2-check-panel.png — условие детерминированной проверки")
        close_node_panel(page)

        browser.close()

        # --- экраны результата, которые видит обратившийся (публичные, без логина) ---
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 900, "height": 700})
        for name, url in RESULT_URLS.items():
            page.goto(url, wait_until="networkidle")
            time.sleep(1)
            page.screenshot(path=str(OUT / f"{name}.png"))
            print(f"  {name}.png — экран результата (клиент)")
        browser.close()


# =====================================================================================
# Шесть фигур Семинара 9 — Кейсы 2–6 (issue #299, бриф §5)
# =====================================================================================
#
# Запуск:  source tools/presentation-build/setup_page_shots.sh
#          set -a && source /home/harness/.n8n-lab-credentials && set +a
#          python3 library/seminars/sem-09/stend/n8n_shots.py --figures
#
# Ничего на стенде не меняется: только открыть сценарий в редакторе, раскрыть панель узла,
# снять кадр. Ни «Сохранить», ни «Опубликовать», ни запуск узла не нажимаются; сценарии
# с `active=false` (замеры K4 и K5п) НЕ активируются — редактор их и не требует.

FIGS = Path(__file__).parents[1] / "rendered" / "figures"

# id нужны для открытия сценария в редакторе; на видимый слой кадра они не попадают —
# шапка с именем сценария и крошками обрезается (см. `clip_canvas`).
WF_K3_CODE = "4WwTEwcwbzPdC5k0"   # С9 · замер K3 · цикл с кодовой проверкой
WF_K3_JUDGE = "x7XYG1HLGM9ls4sR"  # С9 · замер K3 · цикл с судьёй-моделью
WF_K4_NUM = "St32ioA4GV7LPDMY"    # С9 · замер K4 · возврат, числовое поле формы (active=false)
WF_K5_T0 = "z3ZEfAaJZzo6qUDi"     # С9 · замер K5 — повторы одного вопроса при T=0
WF_K6 = "Sg3VSg0bIxqJOGCP"        # С9 · замер K6 — чтение фотографии квитанции

# Поля, вне которых кадр не режется: слева боковая панель n8n, сверху крошки с именем
# сценария и проектом пользователя, снизу полоса журналов.
SAFE = {"x0": 58, "y0": 70, "x1": 1588, "y1": 952}

# Холст снимается в широком окне: «вместить всё» упирается в ширину окна, и в узком окне
# большой сценарий ужимается до зума 0,73 — подписи узлов выходят мельче, чем могли бы.
# В широком окне зум доходит до единицы, и тот же холст даёт кадр с крупным текстом.
VIEW_CANVAS = {"width": 2200, "height": 1250}
VIEW_PANEL = {"width": 1600, "height": 1000}


def safe_box(page):
    vp = page.viewport_size
    return {"x0": 58, "y0": 70, "x1": vp["width"] - 12, "y1": vp["height"] - 48}

# Всплывающая карточка n8n «Production Checklist» ложится поверх холста. Это баннер
# продукта, не содержание стенда; закрывается своей же кнопкой, а если кнопка не нашлась —
# снимается из разметки (о подмене содержания речи не идёт, кадр от этого ничего не теряет).
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


def _union(rects, pad, safe=None, pad_bottom=None):
    safe = safe or SAFE
    x0 = min(r[0] for r in rects) - pad
    y0 = min(r[1] for r in rects) - pad
    x1 = max(r[2] for r in rects) + pad
    y1 = max(r[3] for r in rects) + (pad if pad_bottom is None else pad_bottom)
    x0 = max(x0, safe["x0"]); y0 = max(y0, safe["y0"])
    x1 = min(x1, safe["x1"]); y1 = min(y1, safe["y1"])
    return {"x": x0, "y": y0, "width": x1 - x0, "height": y1 - y0}


def clip_canvas(page, pad=78):
    """Прямоугольник по узлам холста: шапка с именем сценария и пустое поле по краям вне кадра."""
    rects = page.evaluate(JS_RECTS, ['[data-test-id="canvas-node"]', '[data-test-id="edge-label"]'])
    # снизу запас больше: подпись узла и его подзаголовок стоят НИЖЕ рамки узла
    return _union(rects, pad, safe=safe_box(page), pad_bottom=98)


def clip_panel(page, pad=14):
    """Прямоугольник ровно по колонке параметров узла.

    Границы по горизонтали берутся у самой колонки, а не у её содержимого: иначе в кадр
    попадает обрезок соседней панели входа («INPUT», «No input data»), который к настройке
    узла отношения не имеет и читается как брак кадра.
    """
    col = page.evaluate(JS_RECTS, ['[data-test-id="node-parameters"]'])[0]
    rects = page.evaluate(JS_RECTS, [
        '[data-test-id="tab-params"]',
        '[data-test-id="node-parameters"] [data-test-id="parameter-item"]',
        '[data-test-id="collection-parameter-add"]',
        '.el-popper:not([style*="display: none"])',
    ])
    box = _union(rects, pad, safe={"x0": 24, "y0": 26, "x1": 1576, "y1": 990})
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
    except Exception as exc:  # не критично: кадр просто будет уже
        print(f"    (разделитель не сдвинулся: {exc})")


def open_canvas(page, wf_id):
    page.set_viewport_size(VIEW_CANVAS)
    open_workflow(page, wf_id)
    print("    карточка Production Checklist:", page.evaluate(JS_KILL_CHECKLIST))
    page.click('[data-test-id="zoom-to-fit"]')
    time.sleep(1.2)


def save(page, clip, raw_name, fig_name, what):
    page.screenshot(path=str(OUT / f"{raw_name}.png"))
    FIGS.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(FIGS / fig_name), clip=clip)
    print(f"  {fig_name}  ({int(clip['width'])}×{int(clip['height'])} в точках страницы, ×2) — {what}")


def figures():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1600, "height": 1000}, device_scale_factor=2)
        login(page)

        # --- k2: база знаний целиком в промте (узел версии 1 Кейса 1) ------------------
        open_canvas(page, WF_V1)
        page.set_viewport_size(VIEW_PANEL); time.sleep(0.6)
        open_node_panel(page, "Answer (free self-report)")
        page.locator('[class*="modal"]').first.click()   # раскрыть поле промта целиком
        time.sleep(2)
        box = page.locator(".cm-editor").nth(1).bounding_box()
        head = page.evaluate(JS_RECTS, ['.el-dialog h3, .el-dialog [class*="header"]'])
        top = min([r[1] for r in head] + [box["y"]]) - 8 if head else box["y"] - 10
        save(page,
             {"x": box["x"] - 10, "y": top, "width": box["width"] + 20,
              "height": box["y"] + box["height"] + 10 - top},
             "case1-v1-prompt-expanded", "k2-promt-baza.png",
             "промт узла «Answer (free self-report)» целиком: kb1…kb10 внутри текста промта")
        page.keyboard.press("Escape"); time.sleep(0.6)
        close_node_panel(page)

        # --- k3: холст цикла генератор → проверяющий → переделка -----------------------
        open_canvas(page, WF_K3_CODE)
        save(page, clip_canvas(page), "case3-cycle-code-canvas", "k3-holst-tsikl.png",
             "холст цикла: Generate answer → Code check → Retry or finish? → Prepare retry")

        # --- k3: панель проверяющего (кодовая проверка того же сценария) ---------------
        page.set_viewport_size(VIEW_PANEL); time.sleep(0.6)
        open_node_panel(page, "Code check")
        widen_params(page)
        save(page, clip_panel(page), "case3-code-check-panel", "k3-panel-proveryayushchego.png",
             "панель узла «Code check» — сам текст проверки")
        close_node_panel(page)

        # --- запасной кадр: панель судьи-модели (в фигуры не идёт, лежит в сырых) ------
        open_canvas(page, WF_K3_JUDGE)
        page.set_viewport_size(VIEW_PANEL); time.sleep(0.6)
        open_node_panel(page, "Judge verdict")
        widen_params(page)
        page.screenshot(path=str(OUT / "case3-judge-panel.png"), clip=clip_panel(page))
        print("  (запас) case3-judge-panel.png — панель узла «Judge verdict»")
        close_node_panel(page)

        # --- k4: холст с точкой ветвления по сумме возврата ----------------------------
        # Сценарий снят с публикации (active=false) — редактор публикации не требует,
        # и кнопка публикации здесь не нажимается.
        open_canvas(page, WF_K4_NUM)
        save(page, clip_canvas(page), "case4-numfield-canvas", "k4-holst-vetvlenie.png",
             "холст возврата: ветвление «Amount over threshold?» на две ветки решения")

        # --- k5: панель параметров узла модели ----------------------------------------
        open_canvas(page, WF_K5_T0)
        page.set_viewport_size(VIEW_PANEL); time.sleep(0.6)
        open_node_panel(page, "Model (T=0)")
        widen_params(page)
        page.locator('[data-test-id="collection-parameter-add"]').first.click()
        time.sleep(1.2)
        save(page, clip_panel(page), "case5-model-params", "k5-panel-parametrov.png",
             "панель узла модели: Sampling Temperature 0.0 + раскрытый список доступных полей")
        page.keyboard.press("Escape"); time.sleep(0.4)
        close_node_panel(page)

        # --- k6: холст чтения фотографии квитанции ------------------------------------
        open_canvas(page, WF_K6)
        save(page, clip_canvas(page), "case6-receipt-canvas", "k6-holst-chtenie.png",
             "холст чтения квитанции: приём фотографии → сборка запроса → чтение моделью")

        browser.close()


if __name__ == "__main__":
    if "--figures" in sys.argv:
        figures()
    else:
        main()
