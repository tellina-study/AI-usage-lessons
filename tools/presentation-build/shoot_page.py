#!/usr/bin/env python3
"""Снять веб-страницу в PNG для слайда.

Перед запуском: source tools/presentation-build/setup_page_shots.sh

Снимок страницы — настоящее изображение источника, а не его пересказ. Правилам курса
стилизованная карточка «похожая на страницу» запрещена: в Лекции 8 шестнадцать таких
карточек прошли проверку покрытия и были отвергнуты владельцем на приёмке.

Использование:
    python3 shoot_page.py <url> <выход.png> [--full] [--selector CSS] [--width 1440]
"""
import argparse
import sys


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("out")
    ap.add_argument("--full", action="store_true", help="страница целиком, не первый экран")
    ap.add_argument("--selector", help="снять только этот элемент (CSS-путь)")
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--wait", type=int, default=2500, help="мс после загрузки")
    a = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright не поднят — сперва: source tools/presentation-build/setup_page_shots.sh",
              file=sys.stderr)
        return 2

    with sync_playwright() as p:
        browser = p.chromium.launch(
            args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"])
        page = browser.new_page(viewport={"width": a.width, "height": a.height},
                                device_scale_factor=2)
        try:
            page.goto(a.url, wait_until="domcontentloaded", timeout=60000)
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
    print("Запишите в реестр: адрес, дату съёмки и права на содержимое страницы. "
          "Снимок страницы не делает её содержимое свободным.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
