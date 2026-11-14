#!/usr/bin/env python3
"""Снять настоящие скрины живого стенда n8n.lessons.tellian.io для Семинара 11, Кейс 2
(issue #345) — тем же приёмом, что `sem-10/stend/n8n_shots.py` (headless-браузер через
обход `~/.cache/page-shot-libs/x`).

Запуск — ОБЯЗАТЕЛЬНО в той же оболочке, что и `setup_page_shots.sh`:

    source tools/presentation-build/setup_page_shots.sh
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    python3 library/seminars/sem-11/stend/n8n_shots_case2.py

Снимает: холст целиком (вся цепочка — иерархическая резка + семантическая резка, один
прогон) и развёрнутые панели узлов, несущих механику кейса: «Нарезка иерархическая: дети +
родитель», «Подстановка родителя», «Разрыв смысла и порог (gap_threshold)».
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

WF_CASE2 = "ihiDLBOAAgL0SL1M"  # С11 · Кейс 2 — иерархическая и семантическая нарезка (демо-экран)

VIEW_CANVAS = {"width": 2400, "height": 1100}
VIEW_PANEL = {"width": 1600, "height": 1000}

SAFE_MARGIN = {"x0": 58, "y0": 70, "bottom": 48}

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
    return {"x0": SAFE_MARGIN["x0"], "y0": SAFE_MARGIN["y0"],
            "x1": vp["width"] - 12, "y1": vp["height"] - SAFE_MARGIN["bottom"]}


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
    time.sleep(2.5)
    print("    карточка Production Checklist:", page.evaluate(JS_KILL_CHECKLIST))
    page.click('[data-test-id="zoom-to-fit"]')
    time.sleep(1.2)


def open_node_panel(page, node_name):
    node = page.locator(f'[data-test-id="canvas-node"]:has-text("{node_name}")').first
    node.dblclick()
    time.sleep(1.2)


def close_node_panel(page):
    page.keyboard.press("Escape")
    time.sleep(0.6)


def expand_code_editor(page):
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


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport=VIEW_CANVAS, device_scale_factor=2)
        login(page)

        save_canvas(page, WF_CASE2, "case2-s11-canvas-full",
                    "Документ+вопрос -> иерархическая резка (дети+родитель) -> эмбеддинг -> "
                    "поиск top-1 ребёнка -> подстановка родителя -> ответ gpt-4o-mini -> "
                    "разбор -> семантическая резка (предложения) -> эмбеддинг -> разрыв+порог -> результат")
        save_panel(page, "Нарезка иерархическая: дети + родитель", "case2-s11-hier-split-panel",
                   "код: дети chunk_structural(target=90), родитель = документ целиком", expand_editor=True)
        save_panel(page, "Подстановка родителя", "case2-s11-substitute-parent-panel",
                   "код: единица поиска (top1_child) заменяется на единицу ответа (parent_text)",
                   expand_editor=True)
        save_panel(page, "Разрыв смысла и порог (gap_threshold)", "case2-s11-gap-threshold-panel",
                   "код: cosine-разрыв между соседними предложениями, разрез при gap > gap_threshold",
                   expand_editor=True)
        save_panel(page, "Эмбеддинг вопроса и детей (text-embedding-3-small)",
                   "case2-s11-embed-children-panel",
                   "HTTP-запрос: модель text-embedding-3-small, вход — вопрос + тексты детей")

        browser.close()


if __name__ == "__main__":
    main()
