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
    python3 sobrat_razdel.py 0-1-2-3-4-5-6-7 --size 15 --odnim-pptx   # вся лекция
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
         "4": "sec4-vedenie-dokumentatsii",
         "5": "sec5-kvalifikaciya-i-iznos",
         # Вся лекция: ключ — тег, который `render_sec.py` склеивает из своих
         # аргументов ("-".join(sorted(secs))). Разделов у лекции ВОСЕМЬ, не
         # пять: кроме пяти стадий есть «0. Вход», «6. Итоги» и «7. Закрытие»,
         # и без них собралось бы 64 кадра из 89.
         "0-1-2-3-4-5-6-7": "lec-07-vsya-lekciya"}


def razdely(tag):
    """Разделы, которые называет тег. `render_sec.py` склеивает тег из своих
    аргументов (`"-".join(sorted(secs))`), поэтому тег «1-2-3-4-5» означает
    пять разделов, а «4» — один. Обратный разбор держится здесь, чтобы вся
    лекция собиралась тем же прогоном, что и один раздел."""
    return tag.split("-")


def ids_razdela(tag):
    """Номера кадров раздела — тем же способом, которым их отбирает
    `render_sec.ids_of`, чтобы счёт кусков и счёт кадров не разошлись."""
    import render_sec
    return [i for i, _ in render_sec.ids_of(set(razdely(tag)))]


def shag(nazvanie, cmd, cwd=None):
    print(f"\n=== {nazvanie} ===\n$ {' '.join(map(str, cmd))}", flush=True)
    r = subprocess.run([str(c) for c in cmd], cwd=str(cwd or HERE))
    if r.returncode:
        raise SystemExit(f"{nazvanie}: код {r.returncode}")


def zametki(tag, imya, odnim_pptx=False):
    """Собрать `<имя>-notes.pdf` из того же pptx, которым собраны слайды.

    ДВА ПУТИ, И У КАЖДОГО СВОЯ ЦЕНА — выбирать осознанно.

    Путь кусками (по умолчанию). `render_sec.py` режет вход по `--size` и
    кладёт `parts-sec/sec<тег>-01.pptx`, `-02.pptx` и далее; заметки раньше
    собирались ТОЛЬКО из первого куска. Пока раздел был короче шестнадцати
    кадров, это совпадало. На шестнадцатом `notes_pages_pdf.py` сказал
    «count mismatch: pdf_pages=16 pptx_notes=15; using 15» ОДНОЙ строкой
    посреди вывода — и выпустил заметки без последнего кадра. Теперь заметки
    собираются по КАЖДОМУ куску и склеиваются по порядку кусков.

    ЦЕНА ЭТОГО ПУТИ, ЗАМЕРЕНА: `notes_pages_pdf.py` нумерует «слайд N» и
    подвал «страница / всего» ВНУТРИ своего прогона, а офсета у него нет.
    Шесть кусков дали в склейке шесть «слайд 1» и шесть счётчиков страниц с
    начала — 215 страниц читаются как шесть документов подряд. Для ОДНОГО
    раздела это незаметно (кусок один), для всей лекции — дефект, который
    видит читатель.

    Путь одним pptx (`odnim_pptx=True`) — для всей лекции. Сборка ПОЛНОЙ
    деки в один pptx не рендерится через `soffice` (память, `notes/
    mcp-limitations.md` [#229-2]), но заметкам рендер и не нужен: они берут
    КАРТИНКИ из уже склеенного PDF, а ТЕКСТ — из pptx. Поэтому полный pptx
    собирается без рендера, и в пару ему идёт склейка кусков. Пара «кадр ↔
    заметка» позиционная (страница i ↔ слайд i), а порядок у обоих один и
    тот же — `slidefile.slide_files`. Нумерация выходит сквозной.
    """
    pdf = HERE / f"{imya}.pdf"
    if not pdf.exists():
        raise SystemExit(f"нет входа для заметок: {pdf}")

    if odnim_pptx:
        import build_lec07 as B
        from deckkit import report
        only = ",".join(ids_razdela(tag))
        pptx = HERE / f"{imya}.pptx"
        print(f"\n=== полный pptx под заметки ({len(only.split(','))} кадров, "
              f"без рендера) ===", flush=True)
        keep = report.snapshot()
        B.build(only=only, out=pptx)
        report.restore(keep)
        kuski = [pptx]
        pdfs = [pdf]
    else:
        kuski = sorted((HERE / "parts-sec").glob(f"sec{tag}-*.pptx"))
        if not kuski:
            raise SystemExit(f"кусков сборки для тега {tag} нет")
        pdfs = [k.with_suffix(".pdf") for k in kuski]

    chasti = []
    with tempfile.TemporaryDirectory() as d:
        for n, (pptx, pdf_i) in enumerate(zip(kuski, pdfs), 1):
            for f in (pptx, pdf_i):
                if not f.exists():
                    raise SystemExit(f"нет входа для заметок: {f}")
            lecdir = Path(d) / (imya if len(kuski) == 1 else f"{imya}-{n:02d}")
            (lecdir / "rendered").mkdir(parents=True)
            shutil.copy2(HERE / "deck.yaml", lecdir / "deck.yaml")
            shutil.copy2(pptx, lecdir / "rendered" / f"{lecdir.name}.pptx")
            shutil.copy2(pdf_i, lecdir / "rendered" / f"{lecdir.name}.pdf")
            shag(f"заметки, кусок {n} из {len(kuski)}",
                 [sys.executable, TOOLS / "notes_pages_pdf.py",
                  lecdir, "--dpi", "150"])
            chasti.append(lecdir / "rendered" / f"{lecdir.name}-notes.pdf")
        gotovo = HERE / f"{imya}-notes.pdf"
        if len(chasti) == 1:
            shutil.copy2(chasti[0], gotovo)
        else:
            shag("склейка заметок",
                 ["bash", "-lc",
                  ". /home/harness/.local/lo-portable-env.sh && pdfunite "
                  + " ".join(f"'{c}'" for c in chasti)
                  + f" '{gotovo}'"])
    print(f"[ok] {imya}-notes.pdf")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("razdel")
    ap.add_argument("--tolko-zametki", action="store_true")
    ap.add_argument("--size", type=int, default=0,
                    help="кадров в куске; 0 — весь раздел одним куском")
    ap.add_argument("--imya", default=None,
                    help="имя пары файлов, если его нет в IMENA")
    ap.add_argument("--odnim-pptx", action="store_true",
                    help="заметки одним прогоном по полному pptx — сквозная "
                         "нумерация «слайд N»; нужно для всей лекции")
    a = ap.parse_args()
    tag = a.razdel
    imya = a.imya or IMENA.get(tag)
    if not imya:
        raise SystemExit(f"для раздела {tag} имя пары файлов не задано "
                         f"(см. IMENA в этом файле)")

    if not a.tolko_zametki:
        # Куски чистятся до сборки: иначе заметки склеятся с хвостом прошлого
        # прогона, а слайды — нет, и разойдутся они молча.
        kadrov = len(ids_razdela(tag))
        for stale in (HERE / "parts-sec").glob(f"sec{tag}-*"):
            stale.unlink() if stale.is_file() else None
        shag("слайды", [sys.executable, HERE / "render_sec.py",
                        *razdely(tag), "--size", str(a.size or max(kadrov, 1))])
        src = HERE / f"sec-{tag}.pdf"
        if not src.exists():
            raise SystemExit(f"render_sec.py не оставил {src}")
        shutil.copy2(src, HERE / f"{imya}.pdf")
        print(f"[ok] {imya}.pdf")

    zametki(tag, imya, odnim_pptx=a.odnim_pptx)

    print("\nОба файла пересобраны. Закоммитить ОБА — артефакт в ветке и есть "
          "то,\nчто откроет читатель; свежесть своей локальной пересборки "
          "ему не видна.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
