#!/usr/bin/env python3
"""Снимок холста обновлённой цепочки Кейса 3, процесс (B) — после того, как на
ветку «одобрено» добавлен узел отправки сообщения клиенту.

Волна 1в «конфетки» Семинара 8 (issue #292), задача A. Узел добавлен на живом
стенде решением владельца 2026-10-22 («добавляй»): до этого ветка «одобрено»
кончалась экраном результата формы, и клиент о решении не узнавал ничего —
на слайде это выглядело как процесс, который принял решение и никому его не
сказал.

ТОЛЬКО ЧТЕНИЕ. Скрипт логинится в интерфейс, открывает холст воркфлоу и
снимает кадр. Он не запускает воркфлоу, не правит узлы и не трогает API
стенда — единственные действия в браузере это ввод логина, переход по адресу
и нажатие «уместить в экран».

Доступы берутся из файлов ВНЕ репозитория (`~/.n8n-lab.env`, затем
`/home/harness/.n8n-lab-credentials`) и в код не попадают.

Перед запуском (именно `source`, именно без конвейера — иначе chromium падает
с кодом 127, см. шапку `tools/presentation-build/setup_page_shots.sh`):

    source tools/presentation-build/setup_page_shots.sh
    python3 library/seminars/sem-08/rendered/shoot_case3b_chain.py

Кадр сохраняется сырым в `stend/n8n-screenshots-raw/` — кроп под слайд делает
волна подключения, граница кропа проверяема по необрезанному файлу.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEM = HERE.parent
RAW = SEM / "stend" / "n8n-screenshots-raw"

WORKFLOW_ID = "1ZspTIY2zukoEYAF"   # С8 · Кейс 3, процесс (B) — решение принимает код
RAW_NAME = "case3-process-b-s-uzlom-klientu-2026-10-22.png"


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
        ctx = br.new_context(viewport={"width": 1600, "height": 900},
                             device_scale_factor=2, color_scheme="light")
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

        # «Уместить в экран»: без него холст открывается в последнем сохранённом
        # положении, и добавленный узел может оказаться за краем кадра.
        for sel in ("button[data-test-id=zoom-to-fit]",
                    "[data-test-id=zoom-to-fit]",
                    "button[aria-label*='fit' i]"):
            try:
                pg.click(sel, timeout=3000)
                print("уместил в экран через", sel)
                break
            except Exception:
                continue
        else:
            try:
                pg.keyboard.press("1")   # горячая клавиша n8n «zoom to fit»
                print("уместил в экран горячей клавишей 1")
            except Exception:
                print("не удалось уместить в экран — кадр снят как есть")
        pg.wait_for_timeout(2500)

        out = RAW / RAW_NAME
        pg.screenshot(path=str(out))
        print("сырой кадр:", out)

        body = pg.inner_text("body")
        for needle in ("Notify client", "Amount over threshold",
                       "Result screen", "Extract amount"):
            print(f"   на экране «{needle}»: {body.count(needle)}")

        br.close()


if __name__ == "__main__":
    main()
