#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Качает иконки Lucide и перекрашивает их в палитру курса — НЕ часть
сборки деки (issue #355 §9.6).

Зачем этот скрипт ОТДЕЛЬНЫЙ от `deckkit.ikonki`. Сборка деки
(`build_lecNN.py`, `deckkit.render`) не имеет сетевых побочных эффектов —
тот же договор, что держит `media.resolve_media` на конвертации ЛОКАЛЬНОГО
файла, а не на скачивании недостающего. `deckkit.ikonki.draw_icon` читает
готовый PNG из каталога иконок деки и честно предупреждает, если файла
нет — так деку можно пересобрать без сети сколько угодно раз. Этот скрипт
заполняет каталог ОДИН раз, руками, до сборки.

Что делает:
  1. Качает `https://unpkg.com/lucide-static/icons/<name>.svg` по имени.
  2. Красит: Lucide держит цвет контура атрибутом `stroke="currentColor"` —
     строковая замена на `stroke="<hex>"` ДО растеризации, не перекраска
     готового PNG постфактум (битовая перекраска даёт сглаживание по
     старому цвету на границе — замена в самом SVG его не даёт).
  3. Растеризует через `rsvg-convert` (путь и `LD_LIBRARY_PATH` — те же,
     что `build_lec09.py:344`, тот же сборочный хост) в PNG 48px и 96px с
     прозрачным фоном.
  4. Кладёт `<outdir>/<name>-48.png` и `<name>-96.png` — ровно те имена,
     которые `deckkit.ikonki.draw_icon` и ручной pipeline Лекции 10
     (`assets/icons/*-48.png`) уже ищут.

Падение сети или `rsvg-convert` на ОДНОЙ иконке не останавливает список
остальных — именованное предупреждение на каждую, итоговый код выхода
ненулевой, если хоть одна не вышла (та же дисциплина, что `report.warn` в
самой сборке: сказано по имени, не молчанием и не общим крахом).

Запуск:
    python3 fetch_icons.py --outdir <lec-root>/rendered/assets/icons \\
        --color 1C7293 sprout wheat leaf tractor
    python3 fetch_icons.py --outdir ... --names-file icons.txt
"""
import argparse
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

LUCIDE_URL = "https://unpkg.com/lucide-static/icons/{name}.svg"
RSVG_BIN = "/home/harness/.local/render-extras/sysroot/usr/bin/rsvg-convert"
RSVG_LIB = "/home/harness/.local/render-extras/sysroot/usr/lib/x86_64-linux-gnu"
SIZES = (48, 96)


def recolor_svg(svg_text, hexcolor):
    """`stroke="currentColor"` → `stroke="#<hex>"`, строкой, до растра.
    Lucide отдаёт оба написания цвета по-разному в разных версиях набора
    — оба заменяются, а не угадывается одно."""
    color = f"#{hexcolor.lstrip('#')}"
    return (svg_text
            .replace('stroke="currentColor"', f'stroke="{color}"')
            .replace("stroke='currentColor'", f"stroke='{color}'"))


def fetch_svg(name, *, timeout=15):
    url = LUCIDE_URL.format(name=name)
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.read().decode("utf-8")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        print(f"[иконка] {name}: сеть — {e}", file=sys.stderr)
        return None


def rasterize(svg_path, out_png, width):
    env = dict(os.environ)
    env["LD_LIBRARY_PATH"] = RSVG_LIB + (
        ":" + env["LD_LIBRARY_PATH"] if env.get("LD_LIBRARY_PATH") else "")
    r = subprocess.run(
        [RSVG_BIN, "-w", str(width), "-h", str(width),
         "--keep-aspect-ratio", str(svg_path), "-o", str(out_png)],
        env=env, capture_output=True, text=True)
    if r.returncode:
        print(f"[иконка] {svg_path.stem}: rsvg-convert упал — "
              f"{r.stderr[-300:]}", file=sys.stderr)
        return False
    return True


def fetch_one(name, outdir, color, *, svg_cache):
    svg_cache.mkdir(parents=True, exist_ok=True)
    outdir.mkdir(parents=True, exist_ok=True)
    svg_text = fetch_svg(name)
    if svg_text is None:
        return False
    svg_text = recolor_svg(svg_text, color)
    svg_path = svg_cache / f"{name}-{color}.svg"
    svg_path.write_text(svg_text, encoding="utf-8")
    ok = True
    for size in SIZES:
        out_png = outdir / f"{name}-{size}.png"
        ok = rasterize(svg_path, out_png, size) and ok
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("names", nargs="*", help="имена иконок Lucide (без .svg)")
    ap.add_argument("--names-file", help="файл с именами, по одному в строке")
    ap.add_argument("--outdir", required=True,
                    help="каталог иконок деки, напр. .../assets/icons")
    ap.add_argument("--color", default="1C7293",
                    help="цвет контура, hex без # (умолчание — LIGHT палитры)")
    ap.add_argument("--svg-cache", default=None,
                    help="куда класть промежуточный .svg (умолчание — "
                    "<outdir>/.svg-cache)")
    args = ap.parse_args(argv)

    names = list(args.names)
    if args.names_file:
        names += [ln.strip() for ln in Path(args.names_file).read_text(
            encoding="utf-8").splitlines() if ln.strip()
            and not ln.strip().startswith("#")]
    if not names:
        ap.error("ни одного имени иконки — список пуст")

    outdir = Path(args.outdir)
    svg_cache = Path(args.svg_cache) if args.svg_cache else outdir / ".svg-cache"

    failed = []
    for name in names:
        ok = fetch_one(name, outdir, args.color, svg_cache=svg_cache)
        print(f"{'OK ' if ok else 'ХУДО'} {name}")
        if not ok:
            failed.append(name)

    print(f"итог: {len(names) - len(failed)} из {len(names)} — "
          f"{outdir}" + (f", не вышло: {', '.join(failed)}" if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
