#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Объявленная минута кадра против ВЕСА кадра на свежем PDF. Issue #293, Этап E.

Зачем отдельный прогон, когда рядом лежит `pereschet_minut.py`. Тот считает
по сохранённому замеру круга 7–10 (`zamer-diyeta-r7-r10/`), снятому с деки на
102 кадра: половины нынешних кадров в нём нет вовсе, а у тех, что есть, вес
относится к содержанию до Этапов A–D. Пересчитать по нему нынешнюю деку
значило бы раздать кадрам веса их прежних версий.

Почему не `pol_slov_po_pdf.py`, который меряет вес по PDF и делает это
строже. Два его предусловия на Этапе E не выполняются ни при какой правке
кадров:

* свежесть входа он проверяет КОММИТОМ, которым записан PDF (`git log -1 --
  <pdf>`), а этап не коммитит ничего по наряду — пересобранный и
  пере-рендеренный в том же проходе PDF читается им как «старше 53 правленых
  кадров». Оракул слеп к пересборке без коммита, и отказ здесь ложный;
* сверку «страница стоит на своём кадре» он ведёт через `ocenka.files_for`, а
  тот берёт заголовок кадра из ПЕРВОГО заголовка markdown — и на кадре с
  пустым разделом «Видимый текст слайда» (диаграмма во весь кадр, удар,
  кадр-пауза) получает «Заметки лектора». Восемь кадров деки объявляются
  несовпавшими, хотя страницы на своих местах.

Поэтому здесь: порядок страниц берётся у САМОГО сборщика
(`slidefile.slide_files`, тот же порядок, в котором `build_lec07.build`
пишет страницы), а сверка идёт по заголовку из ФРОНТМАТТЕРА и только там,
где он не пуст. Темп — 122 слова на минуту, медиана деки; то же число и та
же округлённость до 0,05, что у `pereschet_minut.py`, чтобы два прогона
нельзя было сравнить и получить разные ответы из-за разных знаменателей.

    python3 zamer_minut_po_pdf.py                      # вся дека
    python3 zamer_minut_po_pdf.py --sid s27a,s33,s31    # только эти кадры
    python3 zamer_minut_po_pdf.py --pdf look/final-293/lec-07-karkas.pdf
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))

import build_lec07 as B                                      # noqa: E402
from deckkit import report, slidefile                        # noqa: E402

TEMP = 122.0        # слов на минуту — медиана деки, та же, что в `pereschet_minut`
SHAG = 0.05         # шаг объявления минуты


def stranitsy(pdf):
    """Текст каждой страницы PDF, по порядку."""
    import fitz
    with fitz.open(str(pdf)) as d:
        return [p.get_text() for p in d]


def slov(text):
    return len([w for w in re.split(r"\s+", text) if w.strip()])


def kadry():
    """(sid, заголовок из фронтматтера, объявленная минута, файл) по порядку
    СБОРКИ. Предупреждения `slide_files` о двух файлах на номер в отчёт этого
    прогона не уносим — он замер, а не сборка."""
    keep = report.snapshot()
    files = slidefile.slide_files(B.SLIDES_DIR)
    report.restore(keep)
    out = []
    for f in files:
        m = re.match(r"^---\n(.*?)\n---", f.read_text(encoding="utf-8"), re.S)
        meta = yaml.safe_load(m.group(1)) if m else {}
        meta = meta or {}
        out.append((f.name.split("-")[0], str(meta.get("title") or "").strip(),
                    float(meta.get("timing_min") or 0),
                    str(meta.get("section") or ""), f))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default="lec-07-karkas.pdf")
    ap.add_argument("--sid", default="")
    a = ap.parse_args()
    pdf = HERE / a.pdf if not Path(a.pdf).is_absolute() else Path(a.pdf)
    if not pdf.exists():
        print(f"ОТКАЗ: PDF {a.pdf} не найден — вес кадра берётся только с "
              "собранного, оценкой по файлу он не берётся")
        return 2
    pages, frames = stranitsy(pdf), kadry()
    if len(pages) != len(frames):
        print(f"ОТКАЗ: страниц {len(pages)}, кадров {len(frames)} — "
              "сопоставить страницу с кадром нечем")
        return 2
    # Сверка порядка. Заголовок из фронтматтера ищется в тексте страницы по
    # ДОЛЕ слов: перенос, мягкий дефис и разрядка ломают точное совпадение.
    plokho = []
    for i, (sid, title, _t, _sec, _f) in enumerate(frames):
        if not title:
            continue
        ws = [w.lower().strip(".,:;«»—·()")
              for w in re.split(r"\s+", title) if len(w) > 3]
        if not ws:
            continue
        txt = pages[i].lower()
        dolya = sum(1 for w in ws if w in txt) / len(ws)
        if dolya < 0.6:
            plokho.append(f"стр.{i + 1} {sid} — {dolya:.0%} слов заголовка")
    if plokho:
        print("ОТКАЗ: страница стоит не на своём кадре — " + " · ".join(plokho))
        return 2
    print(f"сверено по заголовкам фронтматтера: страниц {len(pages)}, "
          f"сдвигов нет ({pdf.name})")
    want = {x.strip() for x in a.sid.split(",") if x.strip()}
    rows, so, sn = [], 0.0, 0.0
    for i, (sid, _title, t, sec, f) in enumerate(frames):
        w = slov(pages[i])
        new = round(round(w / TEMP / SHAG) * SHAG, 2)
        so, sn = so + t, sn + new
        if not want or sid in want:
            rows.append((sid, sec.split(".")[0], w, t, new, f.name))
    print(f"{'кадр':<8}{'р':>3}{'слов':>6}{'объявл':>8}{'замер':>7}{'Δ':>7}")
    for sid, sec, w, t, new, _n in rows:
        print(f"{sid:<8}{sec:>3}{w:>6}{t:>8.2f}{new:>7.2f}{new - t:>+7.2f}")
    print(f"вся дека: объявлено {so:.2f} · замер {sn:.2f} ({sn - so:+.2f})")
    if want:
        gs = sum(r[3] for r in rows)
        gn = sum(r[4] for r in rows)
        print(f"выбранные {len(rows)} кадров: объявлено {gs:.2f} · "
              f"замер {gn:.2f} ({gn - gs:+.2f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
