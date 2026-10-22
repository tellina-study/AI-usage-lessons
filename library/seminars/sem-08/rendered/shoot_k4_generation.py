#!/usr/bin/env python3
"""Снимки холста и панели узла ЖИВОЙ генерации карточки Кейса 4.

Волна 1г «конфетки» Семинара 8 (issue #292), задача C. Шаг генерации собран на
стенде этой же волной (`stend/sborka.py: stage_4_generate`, workflow
`Yg4CcRdssgX3lfvw`) — до неё слайд n51 говорил о генерации как об архитектурной
оценке по чужому прайсу, и показывать было нечего.

ТОЛЬКО ЧТЕНИЕ. Скрипт входит в интерфейс, открывает холст, умещает его в экран,
снимает кадр, затем открывает двойным щелчком узел генерации и снимает панель
настройки. Он не запускает воркфлоу (прогоны делает `stend/run_k4_generation.py`),
не правит узлы и не трогает управляющее API.

Доступы — из файлов ВНЕ репозитория (`~/.n8n-lab.env`, затем
`/home/harness/.n8n-lab-credentials`), в код не попадают.

Перед запуском (именно `source`, именно без конвейера — иначе chromium падает с
кодом 127, см. шапку `tools/presentation-build/setup_page_shots.sh`):

    source tools/presentation-build/setup_page_shots.sh
    python3 library/seminars/sem-08/rendered/shoot_k4_generation.py

Кадры сохраняются сырыми в `stend/n8n-screenshots-raw/`: кроп под слайд делает
`make_figures_k4gen.py`, и граница кропа проверяема по необрезанному файлу.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEM = HERE.parent
RAW = SEM / "stend" / "n8n-screenshots-raw"

WORKFLOW_ID = "Yg4CcRdssgX3lfvw"       # С8 · Кейс 4 — генерация карточки (живой узел)
CANVAS_NAME = "case4-generatsiya-holst-2026-10-22.png"
PANEL_NAME = "case4-generatsiya-uzel-2026-10-22.png"
NODE_TITLE = "Generate card (OpenRouter image)"


def _creds():
    vals = {}
    for p in (Path.home() / ".n8n-lab.env", Path("/home/harness/.n8n-lab-credentials")):
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*(?:export\s+)?([A-Z0-9_]+)\s*=\s*(.*)\s*$", line)
            if m:
                vals.setdefault(m.group(1), m.group(2).strip().strip('"').strip("'"))
    user = vals.get("N8N_UI_USER") or vals.get("N8N_UI_EMAIL")
    pwd = vals.get("N8N_UI_PASS") or vals.get("N8N_UI_PASSWORD")
    base = re.sub(r"/api/v\d+/?$", "", vals.get("N8N_API_URL", "")).rstrip("/")
    if not (user and pwd and base):
        sys.exit("нет доступов интерфейса стенда: проверь ~/.n8n-lab.env "
                 "и /home/harness/.n8n-lab-credentials")
    return base, user, pwd


def main():
    from playwright.sync_api import sync_playwright

    base, user, pwd = _creds()
    RAW.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox"])
        ctx = br.new_context(viewport={"width": 1900, "height": 1100},
                             device_scale_factor=1, color_scheme="light")
        pg = ctx.new_page()

        pg.goto(f"{base}/signin", wait_until="domcontentloaded", timeout=60000)
        pg.wait_for_timeout(1500)
        if "signin" in pg.url:
            pg.fill("input[type=email], input[name=email]", user)
            pg.fill("input[type=password], input[name=password]", pwd)
            pg.click("button[type=submit], button:has-text('Sign in')")
            pg.wait_for_timeout(4000)
        print("после входа:", pg.url)

        pg.goto(f"{base}/workflow/{WORKFLOW_ID}", wait_until="domcontentloaded",
                timeout=60000)
        pg.wait_for_timeout(7000)
        print("холст:", pg.url, "| заголовок:", pg.title())

        # «Уместить в экран»: цепочка генерации стоит правее исходных узлов С7, и
        # в последнем сохранённом положении холста легко оказывается за краем.
        for sel in ("button[data-test-id=zoom-to-fit]", "[data-test-id=zoom-to-fit]",
                    "button[aria-label*='fit' i]"):
            try:
                pg.click(sel, timeout=3000)
                print("уместил в экран через", sel)
                break
            except Exception:
                continue
        else:
            try:
                pg.keyboard.press("1")
                print("уместил в экран горячей клавишей 1")
            except Exception:
                print("не удалось уместить в экран — кадр снят как есть")
        pg.wait_for_timeout(2500)

        pg.screenshot(path=str(RAW / CANVAS_NAME))
        print("сырой кадр холста:", RAW / CANVAS_NAME)

        body = pg.inner_text("body")
        for needle in ("Generate card", "Card bytes and cost", "Base64 to file",
                       "Send generated card", "Compose notification"):
            print(f"   на экране «{needle}»: {body.count(needle)}")

        # Панель узла — двойной щелчок по самому узлу на холсте.
        opened = False
        for sel in (f"[data-test-id=canvas-node]:has-text('{NODE_TITLE}')",
                    f"div:has-text('{NODE_TITLE}')"):
            try:
                pg.dblclick(sel, timeout=5000)
                opened = True
                print("панель открыта через", sel)
                break
            except Exception:
                continue
        if not opened:
            print("не удалось открыть узел — панель не снята")
        else:
            pg.wait_for_timeout(3000)
            pg.screenshot(path=str(RAW / PANEL_NAME))
            print("сырой кадр панели:", RAW / PANEL_NAME)
            body = pg.inner_text("body")
            for needle in ("JSON", "openrouter.ai", "gemini-2.5-flash-image",
                           "Credential to connect with"):
                print(f"   в панели «{needle}»: {body.count(needle)}")

        br.close()


if __name__ == "__main__":
    main()
