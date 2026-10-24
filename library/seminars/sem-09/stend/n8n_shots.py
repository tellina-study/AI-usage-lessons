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


if __name__ == "__main__":
    main()
