#!/usr/bin/env python3
"""Снимок таблицы данных живого стенда n8n — строки буквального повтора
(Кейс 2, слайд n23a по плану §4.12).

Волна 1а «конфетки» Семинара 8 (issue #292), задача 3. На слайде должна
стоять НАСТОЯЩАЯ таблица заявок стенда, а не нарисованная: правило «никаких
моков» (`notes/mcp-limitations.md`, канон §2) не делает исключения для
таблиц.

ТОЛЬКО ЧТЕНИЕ. Скрипт логинится в интерфейс, открывает таблицу и снимает
кадр. Он не запускает ни одного воркфлоу, не правит ни одной строки и не
трогает API стенда — единственные действия в браузере это ввод логина,
переход по адресу и прокрутка.

Доступы берутся из файлов ВНЕ репозитория (`~/.n8n-lab.env`, затем
`/home/harness/.n8n-lab-credentials`) и в код не попадают — ни логин, ни
пароль, ни адрес с ключом здесь не записаны.

Перед запуском (именно `source`, именно без конвейера — иначе chromium
падает с кодом 127, см. шапку `tools/presentation-build/setup_page_shots.sh`):

    source tools/presentation-build/setup_page_shots.sh
    python3 library/seminars/sem-08/rendered/shoot_datatable.py

Кадр сохраняется сырым в `stend/n8n-screenshots-raw/` (как все прочие
скрины стенда — чтобы граница любого будущего кропа была проверяема по
необрезанному файлу), а кроп области таблицы — в
`rendered/figures/k2-datatable-povtor-real.png`.
"""
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEM = HERE.parent
RAW = SEM / "stend" / "n8n-screenshots-raw"
OUT = HERE / "figures"

# Проект и таблица стенда (идентификаторы самого стенда, не секреты —
# без входа в интерфейс по ним ничего не открывается).
PROJECT_ID = "ndldnbw7m6ghSlg8"
TABLE_ID = "xlDAQCm75jLAKNom"          # таблица `requests`, 31 строка

RAW_NAME = "datatable-requests-2026-10-22.png"
FIG_NAME = "k2-datatable-povtor-real.png"


def _creds():
    """Логин/пароль интерфейса из файлов вне репозитория. Порядок: сначала
    `~/.n8n-lab.env` (`N8N_UI_USER`/`N8N_UI_PASS`), затем
    `/home/harness/.n8n-lab-credentials` (`N8N_UI_EMAIL`/`N8N_UI_PASSWORD`)."""
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
    api = vals.get("N8N_API_URL", "")
    base = re.sub(r"/api/v\d+/?$", "", api).rstrip("/")
    if not (user and pwd and base):
        sys.exit("нет доступов интерфейса стенда: проверь ~/.n8n-lab.env "
                 "и /home/harness/.n8n-lab-credentials")
    return base, user, pwd


def main():
    from playwright.sync_api import sync_playwright

    base, user, pwd = _creds()
    RAW.mkdir(parents=True, exist_ok=True)
    url = f"{base}/projects/{PROJECT_ID}/datatables/{TABLE_ID}"

    with sync_playwright() as p:
        # deviceScaleFactor=2 — кадр снимается вдвое плотнее окна: мелкий
        # текст таблицы на проекторе не должен ловить ступеньки. Светлая
        # тема — `colorScheme="light"`, на слайде курса тёмная тема
        # интерфейса читается хуже и ломает Ocean-палитру.
        br = p.chromium.launch(args=["--no-sandbox"])
        ctx = br.new_context(viewport={"width": 1500, "height": 950},
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

        pg.goto(url, wait_until="domcontentloaded", timeout=60000)
        pg.wait_for_timeout(6000)
        print("таблица:", pg.url, "| заголовок:", pg.title())

        raw_path = RAW / RAW_NAME
        pg.screenshot(path=str(raw_path))
        print("сырой кадр:", raw_path, "размер", pg.viewport_size)

        # Отдельно — список строк таблицы в тексте страницы: по нему видно,
        # попали ли в кадр строки буквального повтора, без разглядывания PNG.
        body = pg.inner_text("body")
        for needle in ("перенести занятие", "внести оплату", "оплатить"):
            hits = body.count(needle)
            print(f"   на экране «{needle}»: {hits}")
        (RAW / (RAW_NAME.replace(".png", "-text.txt"))).write_text(
            body, encoding="utf-8")

        # ── второй кадр: тот же экран, но окно низкое и список прокручен в
        # конец. Зачем: на первой странице таблицы между шапкой и нижним
        # кустом повторов лежат две строки мусорного тестового ввода
        # («ывавыаыв» — кто-то стучал по клавиатуре, проверяя форму). В один
        # прямоугольник с шапкой они попадают неизбежно, а на слайде читаются
        # как неряшливость стенда и уводят вопрос зала в сторону. Низкое окно
        # оставляет в кадре шапку (она прилипшая) и последние строки —
        # кусты буквального повтора Петра и Анны подряд. Это тот же живой
        # экран в том же состоянии, просто окно меньше: ни одна строка не
        # скрыта фильтром и ни одна не изменена.
        pg.set_viewport_size({"width": 1500, "height": 560})
        pg.wait_for_timeout(1200)
        pg.mouse.move(750, 400)
        for _ in range(6):
            pg.mouse.wheel(0, 600)
            pg.wait_for_timeout(250)
        pg.wait_for_timeout(1500)
        tail_path = RAW / RAW_NAME.replace(".png", "-tail.png")
        pg.screenshot(path=str(tail_path))
        print("кадр с прокруткой в конец:", tail_path)

        # Вторая страница таблицы — только в текст, для записи в отчёт
        # (нажатие стрелки «вперёд» — обычная навигация, данные не меняются).
        #
        # Переход ПРОВЕРЯЕТСЯ по содержимому, а не по тому, что клик не
        # бросил исключение: первый заход нажимал `text=/^2$/`, исключения не
        # было, файл записался — и в нём лежала та же первая страница.
        # Отчёт об успехе, не подтверждённый данными, — ровно тот вид вранья,
        # который канон запрещает сильнее всего.
        try:
            pg.set_viewport_size({"width": 1500, "height": 950})
            pg.wait_for_timeout(1000)
            pg.evaluate("window.scrollTo(0, 0)")
            pg.wait_for_timeout(500)
            pg.get_by_text("2", exact=True).last.click(timeout=8000)
            pg.wait_for_timeout(3000)
            txt = pg.inner_text("body")
            ok = "\n21\n" in txt
            (RAW / RAW_NAME.replace(".png", "-page2-text.txt")).write_text(
                txt, encoding="utf-8")
            print("вторая страница:", "открыта (видна строка 21)" if ok
                  else "НЕ ОТКРЫЛАСЬ — в файле снова первая страница")
        except Exception as e:                      # noqa: BLE001
            print("вторую страницу открыть не удалось:", type(e).__name__, e)

        br.close()


if __name__ == "__main__":
    main()
