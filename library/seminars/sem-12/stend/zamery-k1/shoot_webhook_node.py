#!/usr/bin/env python3
"""Снять настоящий скрин живого стенда n8n для Семинара 12, Кейс 1 (слайд n18/n19).

Воркфлоу `s10-raw-openrouter` (id `S4AMVj1hVmcs4fe8`) — тот самый вебхук, которым
сделаны ВСЕ 300+ вызовов обоих замеров этого кейса (см. stend/zamery-k1/README.md,
harness_call.py). Снимаем холст целиком и, если получится, развёрнутую панель
параметров узла Webhook/HTTP Response.

Техника — дословно `sem-10/stend/n8n_shots.py` (обход `~/.cache/page-shot-libs/x`,
[#233-8], снято 2026-10-20). Запуск ОБЯЗАТЕЛЬНО после:
    source tools/presentation-build/setup_page_shots.sh
    set -a; source /home/harness/.n8n-lab-credentials; set +a
в ТОЙ ЖЕ оболочке.
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

WF_RAW_OPENROUTER = "S4AMVj1hVmcs4fe8"  # s10-raw-openrouter — вебхук всех 300+ вызовов

VIEW_CANVAS = {"width": 2200, "height": 1250}
VIEW_PANEL = {"width": 1600, "height": 1000}


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


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport=VIEW_CANVAS, device_scale_factor=2)
        login(page)

        open_canvas(page, WF_RAW_OPENROUTER)
        path = OUT / "raw-openrouter-canvas.png"
        page.screenshot(path=str(path), clip=clip_canvas(page))
        print(f"  {path.name} — холст s10-raw-openrouter")

        # список имён узлов на холсте — чтобы знать, какой открыть панелью
        names = page.evaluate(
            "() => Array.from(document.querySelectorAll('[data-test-id=\"canvas-node\"]'))"
            ".map(e => (e.innerText || '').split('\\n')[0])"
        )
        print("    узлы на холсте:", names)

        # пробуем открыть панель первого узла (обычно Webhook/триггер)
        try:
            page.set_viewport_size(VIEW_PANEL)
            time.sleep(0.6)
            node = page.locator('[data-test-id="canvas-node"]').first
            node.dblclick()
            time.sleep(1.2)
            widen_params(page)
            path2 = OUT / "raw-openrouter-webhook-panel.png"
            page.screenshot(path=str(path2), clip=clip_panel(page))
            print(f"  {path2.name} — панель первого узла")
        except Exception as exc:
            print(f"    (панель не снята: {exc})")

        browser.close()


if __name__ == "__main__":
    main()
