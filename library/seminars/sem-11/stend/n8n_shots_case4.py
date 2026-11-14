#!/usr/bin/env python3
"""Снять настоящие скрины живого стенда n8n.lessons.tellian.io для Кейса 4 Семинара 11
(issue #345) — та же техника, что Семинар 10/9/8 (`notes/mcp-limitations.md` [#233-8]).

Запуск — ОБЯЗАТЕЛЬНО после `source` обхода в ТОЙ ЖЕ оболочке:

    source tools/presentation-build/setup_page_shots.sh
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    python3 library/seminars/sem-11/stend/n8n_shots_case4.py

Снимает:
  - холст воркфлоу (широкий кроп главного пути)
  - панель параметров узла «Поиск со скоупингом…» (развёрнутый код — один фильтр-строка,
    отличающая его от узла «без скоупинга»)
  - РЕАЛЬНЫЙ прогон через опубликованную форму: заполняет поле `payload` настоящим JSON
    (вопрос + anchor-new3-context + Dc-1063, та же пара, что в живой находке замера) и снимает
    экран результата после отправки — то есть сам ответ формы, не только устройство узлов.
"""
import json
import os
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

HOST = "https://n8n.lessons.tellian.io"
EMAIL = os.environ["N8N_UI_EMAIL"]
PASSWORD = os.environ["N8N_UI_PASSWORD"]
OUT = Path(__file__).parent / "n8n-screenshots-raw"
OUT.mkdir(exist_ok=True)

WF_CASE4 = "IJPkfAfk68iUes2G"  # С11 · Кейс 4 — скоупинг по домену (демо-экран)
WEBHOOK_PATH = "s11-case4-scoping"

VIEW_CANVAS = {"width": 2200, "height": 1250}
VIEW_PANEL = {"width": 1600, "height": 1000}
VIEW_FORM = {"width": 1100, "height": 1000}

HERE = Path(__file__).parent
CORPUS = json.loads((HERE / "corpus" / "corpus_case4.json").read_text())
anchor = next(a for a in CORPUS["anchors"] if a["anchor_id"] == "anchor-new3")
dc1063 = next(c for c in CORPUS["track_d_candidates"] if c["doc_id"] == "Dc-1063")
PAYLOAD = json.dumps({
    "question": anchor["question"],
    "course_id": "bio",
    "docs": [
        {"id": "anchor-new3-context", "text": anchor["context"], "course_id": "bio"},
        {"id": "Dc-1063", "text": dc1063["text"], "course_id": "other"},
    ],
}, ensure_ascii=False)

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


def submit_form_and_shoot(page):
    """Реальный прогон через опубликованную форму — заполняет payload, жмёт submit,
    снимает экран ПОСЛЕ ответа (completion screen с обеими цифрами)."""
    page.set_viewport_size(VIEW_FORM)
    page.goto(f"{HOST}/form/{WEBHOOK_PATH}", wait_until="networkidle")
    time.sleep(1.5)
    page.fill("textarea", PAYLOAD)
    page.click('button[type="submit"], button:has-text("Submit"), button:has-text("Отправ")')
    page.wait_for_load_state("networkidle")
    time.sleep(3.0)
    path = OUT / "case4-scoping-result.png"
    page.screenshot(path=str(path), full_page=True)
    print(f"  case4-scoping-result.png — экран результата после реальной отправки формы")


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport=VIEW_CANVAS, device_scale_factor=2)
        login(page)

        save_canvas(page, WF_CASE4, "case4-scoping-canvas",
                    "Вопрос+индекс → Embed query+документы → без скоупинга → со скоупингом → Result")
        save_panel(page, "Поиск со скоупингом (фильтр course_id перед ранжированием)",
                   "case4-scoped-panel",
                   "код: фильтр course_id перед cosine top-1 — единственное отличие от узла без скоупинга",
                   expand_editor=True)
        save_panel(page, "Поиск без скоупинга (весь объединённый индекс)",
                   "case4-unscoped-panel",
                   "код: cosine top-1 без фильтра, по всем документам индекса",
                   expand_editor=True)

        submit_form_and_shoot(page)

        browser.close()


if __name__ == "__main__":
    main()
