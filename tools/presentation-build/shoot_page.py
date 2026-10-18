#!/usr/bin/env python3
"""Снять веб-страницу в PNG для слайда.

Перед запуском: source tools/presentation-build/setup_page_shots.sh
(именно `source` и именно без конвейера — иначе chromium упадёт с 127, см. шапку скрипта).

Снимок страницы — настоящее изображение источника, а не его пересказ. Правилам курса
стилизованная карточка «похожая на страницу» запрещена: в Лекции 8 шестнадцать таких
карточек прошли проверку покрытия и были отвергнуты владельцем на приёмке.

Использование:
    python3 shoot_page.py <url> <выход.png> [--full] [--selector CSS] [--width 1440]
                          [--user-agent UA] [--via-curl [ХОСТ]]

Когда хост отбивает сам браузер. Бывает, что страница открывается `curl`-ом и не открывается
браузером с того же адреса в ту же секунду: краевой фильтр узнаёт клиента по отпечатку и
перебрасывает его на страницу-заглушку (`accessdata.fda.gov` отвечает так, хотя `www.fda.gov`
работает; заглушка там отдаёт 404, и `goto` крутится в петле перенаправлений до таймаута).
Тогда:

    --user-agent "<настоящий UA Chrome>"   # сперва дешёвое: иногда фильтр смотрит только UA
    --via-curl                             # если не помогло: запросы к хосту страницы
                                            # забираются `curl`-ом и отдаются в браузер
    --via-curl accessdata.fda.gov           # то же, но перехват только для этого хоста

`--via-curl` не подменяет и не дорисовывает ничего: байты приходят от самого сервера, их
отрисовывает настоящий браузер, подресурсы (стили, изображения шапки) грузятся тем же путём.
Запросы к посторонним хостам при этом отбиваются, а не пропускаются (иначе недоступный
наружу счётчик держит страницу до таймаута — измерено на той же странице FDA); что именно
отбито, печатается после снимка, чтобы «страница как её видит посетитель» было проверяемым
утверждением, а не предположением. Нужны и чужие хосты — `--via-curl '*'`.
На права это никак не влияет — см. напоминание, которое печатается после снимка.
"""
import argparse
import mimetypes
import subprocess
import sys
from urllib.parse import urlsplit

# Настоящий UA Chrome: нужен и сам по себе (--user-agent), и как UA для curl при --via-curl,
# чтобы браузер и curl выглядели для сервера одинаково.
CHROME_UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
             "Chrome/131.0.0.0 Safari/537.36")


def fetch_via_curl(url: str, ua: str, timeout: int = 45):
    """Забрать URL через curl. Возвращает (код, тип содержимого, байты)."""
    marker = b"\n__HTTPCODE__"
    p = subprocess.run(
        ["curl", "-sS", "--max-time", str(timeout), "-L", "-A", ua,
         "-w", "\n__HTTPCODE__%{http_code}__%{content_type}", url],
        capture_output=True)
    raw = p.stdout
    i = raw.rfind(marker)
    if i < 0:
        return 599, "text/plain", "curl не ответил: ".encode() + p.stderr[:300]
    tail = raw[i + len(marker):].decode("utf-8", "replace")
    code, _, ctype = tail.partition("__")
    ctype = ctype.strip() or mimetypes.guess_type(url)[0] or "application/octet-stream"
    return int(code or 599), ctype, raw[:i]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("out")
    ap.add_argument("--full", action="store_true", help="страница целиком, не первый экран")
    ap.add_argument("--selector", help="снять только этот элемент (CSS-путь)")
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--wait", type=int, default=2500, help="мс после загрузки")
    ap.add_argument("--user-agent", dest="user_agent", nargs="?", const=CHROME_UA,
                    help="свой User-Agent; без значения — настоящий UA Chrome")
    ap.add_argument("--via-curl", dest="via_curl", nargs="?", const="",
                    metavar="ХОСТ",
                    help="забирать запросы через curl и отдавать их в браузер; "
                         "без значения — только хост снимаемой страницы, "
                         "со значением — подстрока хоста (или '*' для всех запросов)")
    a = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright не поднят — сперва: source tools/presentation-build/setup_page_shots.sh",
              file=sys.stderr)
        return 2

    # Какому хосту подставлять curl. Пустое значение флага = хост самой страницы.
    curl_pattern = None
    if a.via_curl is not None:
        curl_pattern = a.via_curl or (urlsplit(a.url).hostname or "")
        if not curl_pattern:
            print("--via-curl: не понял, для какого хоста перехватывать — "
                  "укажите его явно", file=sys.stderr)
            return 2
        if "/" in curl_pattern or curl_pattern.lower().endswith(".png"):
            # `--via-curl` без значения съедает следующее слово, если оно идёт сразу за ним:
            # `shoot_page.py --via-curl url out.png` отдаст образцом «url». Ловим здесь,
            # иначе перехват молча не сработает и страница упрётся в таймаут.
            print(f"--via-curl: «{curl_pattern}» не похоже на хост — похоже, флаг забрал "
                  "соседний аргумент. Ставьте его ПОСЛЕ адреса и выходного файла.",
                  file=sys.stderr)
            return 2
    ua = a.user_agent or (CHROME_UA if curl_pattern else None)

    served, failed, dropped, doc_fail = [], [], {}, []

    def route(r):
        url = r.request.url
        host = urlsplit(url).hostname or ""
        if curl_pattern == "*" or curl_pattern in host:
            code, ctype, body = fetch_via_curl(url, ua)
            kind = r.request.resource_type
            (served if code < 400 else failed).append((code, kind, url))
            if kind == "document" and code >= 400:
                doc_fail.append(code)
            try:
                r.fulfill(status=code, content_type=ctype, body=body,
                          headers={"content-type": ctype, "cache-control": "no-store"})
            except Exception as exc:          # запрос уже отменён страницей — не беда
                print(f"  не отдалось в браузер: {type(exc).__name__}: {url[:90]}",
                      file=sys.stderr)
        else:
            # Запросы к посторонним хостам отбиваются сразу, а не пропускаются. Причина
            # измерена: страница FDA тянет счётчик с `dap.digitalgov.gov`, наружу он здесь
            # не ходит, и браузер ждёт его до таймаута `goto` — снимок не получается вовсе
            # (проверено: с `continue_` те же 90 с и ни одного кадра). Что отбито — печатается
            # после снимка: страница вышла без этих кусков, и знать об этом надо.
            dropped[host] = dropped.get(host, 0) + 1
            r.abort()

    with sync_playwright() as p:
        browser = p.chromium.launch(
            args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"])
        ctx_kw = {"viewport": {"width": a.width, "height": a.height},
                  "device_scale_factor": 2}
        if ua:
            ctx_kw["user_agent"] = ua
        ctx = browser.new_context(**ctx_kw)
        if curl_pattern:
            ctx.route("**/*", route)
        page = ctx.new_page()
        try:
            page.goto(a.url, wait_until="domcontentloaded", timeout=90000)
        except Exception as exc:
            print(f"страница не открылась: {type(exc).__name__}: {exc}", file=sys.stderr)
            browser.close()
            return 1
        page.wait_for_timeout(a.wait)
        title = page.title()
        if a.selector:
            el = page.query_selector(a.selector)
            if el is None:
                print(f"элемента «{a.selector}» на странице нет — снимок не сделан",
                      file=sys.stderr)
                browser.close()
                return 1
            el.screenshot(path=a.out)
        else:
            page.screenshot(path=a.out, full_page=a.full)
        browser.close()

    print(f"снято: {a.out}")
    print(f"заголовок страницы: {title}")
    if curl_pattern:
        print(f"через curl (хост «{curl_pattern}»): отдано {len(served)} запросов, "
              f"с ошибкой {len(failed)}")
        for code, kind, url in failed[:10]:
            print(f"  {code} {kind} {url[:110]}")
        if dropped:
            top = ", ".join(f"{h} ×{n}" for h, n in
                            sorted(dropped.items(), key=lambda kv: -kv[1])[:8])
            print(f"отбито как посторонние хосты: {top}"
                  + (" …" if len(dropped) > 8 else ""))
            print("  Если среди них стили или изображения — страница вышла без них: "
                  "расширьте образец хоста или возьмите --via-curl '*'.")
        if doc_fail:
            print(f"!!! ГЛАВНЫЙ ДОКУМЕНТ не получен: сервер ответил {doc_fail[0]}. "
                  "На снимке не страница, а ошибка — не используйте его. "
                  "Чаще всего это временно: повторите через минуту.", file=sys.stderr)
        print("Байты получены curl-ом от самого сервера и отрисованы настоящим браузером — "
              "но на права это не влияет никак: обход фильтра не делает содержимое страницы "
              "ни свободнее, ни доступнее для публикации.")
    print("Запишите в реестр: адрес, дату съёмки и права на содержимое страницы. "
          "Снимок страницы не делает её содержимое свободным.")
    return 1 if doc_fail else 0


if __name__ == "__main__":
    sys.exit(main())
