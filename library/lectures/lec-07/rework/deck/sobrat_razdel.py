#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""СБОРКА РАЗДЕЛА ЦЕЛИКОМ: оба файла, под теми именами, под которыми лежат в ветке.

ЗАЧЕМ ЭТОТ ФАЙЛ ЕСТЬ. `render_sec.py` кладёт результат в `sec-<тег>.pdf` —
своё рабочее имя, — а в ветке раздел лежит парой `sec1-skrining-otbor.pdf`
(слайды) и `sec1-skrining-otbor-notes.pdf` (заметки). Переименование и
сборка заметок делались руками и нигде записаны не были. Цена измерена:
круг правок 2026-10-19 пересобрал раздел, получил чистый PDF — и закоммитил
при этом СТАРЫЙ артефакт от 4cf377d1, где наложение текста на `s16` ещё
было. Фикс в `deckkit/plates.py` реален и работает, но тот, кто открыл бы
PDF по ссылке из ветки, увидел бы ровно тот баг, о котором отчитались как
о закрытом. Поймала это соседняя сессия, прогнав сторож по ЗАКОММИЧЕННОМУ
файлу, а не по своей пересборке — замер входа против замера выхода ещё раз.

ЧТО ДЕЛАЕТ. Три шага одним прогоном:
  1. `render_sec.py <раздел>` — сборка pptx кусками, рендер, склейка;
  2. `sec-<тег>.pdf` → `<имя>.pdf` — слайды под веточным именем;
  3. `notes_pages_pdf.py` по собранным pptx+pdf → `<имя>-notes.pdf` —
     страница на кадр: картинка кадра сверху, полные заметки лектора снизу.

Шагу 3 нужен каталог вида `<имя>/rendered/<имя>.pptx|.pdf` плюс `deck.yaml`
рядом — инструмент выводит все имена из имени каталога (`notes/
mcp-limitations.md` [#171-1]). Поэтому здесь строится временная раскладка
с нужными именами, а не правится сам инструмент: он общий для всех лекций
курса, и раздел одной лекции — не повод его трогать.

    python3 sobrat_razdel.py 1                 # собрать оба файла раздела 1
    python3 sobrat_razdel.py 1 --tolko-zametki # не пересобирать, только заметки
"""
import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parents[4] / "tools" / "presentation-build"

# Имя пары файлов в ветке для каждого раздела. Держится здесь, а не
# выводится из заголовка: имя закоммиченного файла — договорённость с теми,
# кто на него ссылается, и переехать оно может только осознанно.
IMENA = {"1": "sec1-skrining-otbor",
         "4": "sec4-vedenie-dokumentatsii"}


def ids_razdela(tag):
    """Номера кадров раздела — тем же способом, которым их отбирает
    `render_sec.ids_of`, чтобы счёт кусков и счёт кадров не разошлись."""
    import render_sec
    return [i for i, _ in render_sec.ids_of({tag})]


def shag(nazvanie, cmd, cwd=None):
    print(f"\n=== {nazvanie} ===\n$ {' '.join(map(str, cmd))}", flush=True)
    r = subprocess.run([str(c) for c in cmd], cwd=str(cwd or HERE))
    if r.returncode:
        raise SystemExit(f"{nazvanie}: код {r.returncode}")


def zametki(tag, imya):
    """Собрать `<имя>-notes.pdf` из того же pptx, которым собраны слайды.

    ПАДАЕТ, А НЕ ТЕРЯЕТ (круг 2, #285). `render_sec.py` режет раздел на
    куски по `--size` (по умолчанию 15) и складывает `parts-sec/secN-01.pptx`,
    `-02.pptx` и так далее; слайды склеиваются из всех кусков, а заметки
    собирались ТОЛЬКО из первого. Пока раздел был короче шестнадцати кадров,
    это совпадало. На шестнадцатом кадре `notes_pages_pdf.py` сказал
    «count mismatch: pdf_pages=16 pptx_notes=15; using 15» ОДНОЙ строкой
    посреди вывода — и выпустил заметки без последнего кадра. Проверка ниже
    делает из этой строки отказ: лучше не собрать, чем собрать неполным.
    """
    kuski = sorted((HERE / "parts-sec").glob(f"sec{tag}-*.pptx"))
    if len(kuski) != 1:
        raise SystemExit(
            f"кусков сборки {len(kuski)} ({', '.join(k.name for k in kuski)}), "
            f"а заметки собираются из одного. Пересобрать слайды одним куском:\n"
            f"    python3 render_sec.py {tag} --size {len(kuski) * 15 + 15}")
    pptx = kuski[0]
    pdf = HERE / f"{imya}.pdf"
    for p in (pptx, pdf):
        if not p.exists():
            raise SystemExit(f"нет входа для заметок: {p}")
    with tempfile.TemporaryDirectory() as d:
        lecdir = Path(d) / imya
        (lecdir / "rendered").mkdir(parents=True)
        shutil.copy2(HERE / "deck.yaml", lecdir / "deck.yaml")
        shutil.copy2(pptx, lecdir / "rendered" / f"{imya}.pptx")
        shutil.copy2(pdf, lecdir / "rendered" / f"{imya}.pdf")
        shag("заметки", [sys.executable, TOOLS / "notes_pages_pdf.py",
                         lecdir, "--dpi", "150"])
        gotovo = lecdir / "rendered" / f"{imya}-notes.pdf"
        shutil.copy2(gotovo, HERE / f"{imya}-notes.pdf")
    print(f"[ok] {imya}-notes.pdf")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("razdel")
    ap.add_argument("--tolko-zametki", action="store_true")
    a = ap.parse_args()
    tag = a.razdel
    imya = IMENA.get(tag)
    if not imya:
        raise SystemExit(f"для раздела {tag} имя пары файлов не задано "
                         f"(см. IMENA в этом файле)")

    if not a.tolko_zametki:
        # Раздел собирается ОДНИМ куском: иначе заметки соберутся не по всему
        # разделу (см. `zametki` выше). Размер берётся по числу кадров раздела.
        kadrov = len(ids_razdela(tag))
        for stale in (HERE / "parts-sec").glob(f"sec{tag}-*"):
            stale.unlink() if stale.is_file() else None
        shag("слайды", [sys.executable, HERE / "render_sec.py", tag,
                        "--size", str(max(kadrov, 1))])
        src = HERE / f"sec-{tag}.pdf"
        if not src.exists():
            raise SystemExit(f"render_sec.py не оставил {src}")
        shutil.copy2(src, HERE / f"{imya}.pdf")
        print(f"[ok] {imya}.pdf")

    zametki(tag, imya)

    print("\nОба файла пересобраны. Закоммитить ОБА — артефакт в ветке и есть "
          "то,\nчто откроет читатель; свежесть своей локальной пересборки "
          "ему не видна.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
