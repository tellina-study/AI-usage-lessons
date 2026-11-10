#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Спайк Фазы 1 (issue #338, `architecture.md` §3): можно ли подключить
СУЩЕСТВУЮЩИЕ `slides/s06..s13-*.md` Лекции 11 к общему ядру `deckkit`
(issue #229) почти без правки содержания — или контент надо переписывать
под другой набор типов/форм?

Диапазон: Раздел 1 целиком — `s06` (дивайдер) … `s13` (следующий дивайдер),
то есть `deck.yaml` id `s06,s07,s08,s09,s10,s11,s12,s13`.

НИ ОДИН файл кадра `slides/*.md` этим скриптом НЕ правится. Ни один из
существующих `rendered/build_lec11.py` / `rendered/build_lec11_part2.py` /
`rendered/lec-11.pptx` не трогается — это отдельный, параллельный build,
выход которого лежит в этой же папке (`section1-spike.pptx/.pdf`).

ЧТО СДЕЛАНО ПО ОБРАЗЦУ (см. финальный отчёт сессии оркестратору за разбор
находок по каждому пункту):

1. **`refdeck.divider`/`refdeck.content` использованы БЕЗ ПРАВКИ** — это и
   есть главная находка спайка. `s06`/`s13` (`type: section_divider`) идут
   через `refdeck.divider`, `s07..s12` (`type: assertion_visual`) — через
   `refdeck.content`. Ядро не модифицировано ни строкой.
2. **Поля фронтматтера, которых у этого диапазона НЕТ вовсе**:
   `title` (заголовок сейчас живёт ПЕРВОЙ строкой `# …` видимого тела, не
   фронтматтером), `source`/`media`/`media_hero`/`media_caption`, `blocks:`,
   `scheme:`, `columns:`. Для `title` — адаптер `extract_title_if_missing`
   ниже достаёт первую H1-строку тела В ПАМЯТИ (файл кадра не трогается) и
   кладёт её в `sl.title`, которую уже умеет рисовать `refdeck.heading`.
   Для `media` — демонстрационно подключены ТРИ уже существующих ассета
   старого сборщика (`MEDIA_OVERRIDE` ниже): реальные PNG/JPG лежат на
   диске (`rendered/assets/charts/…`, `rendered/assets/screenshots/…`), их
   просто не из чего было прочитать — `media:` в `.md` не было. `source`/
   `blocks`/`scheme`/`columns` НЕ подключены — у этого диапазона `references:`
   это список ключей библиографии («mckinsey-2025-state-of-ai»), а не
   готовая строка с URL, которую понимает `footer()` ядра; разрешение
   ключ→URL — отдельная работа, за пределами спайка (см. отчёт, находка №5).
3. **Тело кадра НЕ структурировано под плашки/столбцы/схему.** Числа
   («78%», «5,5%», «Разрыв ~14×» у `s07`; OT/IT-колонки у `s09`; три
   карточки-причины у `s10`; трио историй у `s12`) сейчас набраны ПРОЗОЙ с
   `**жирным**` внутри обычных абзацев — не декларативными `blocks:`/
   `columns:`/`scheme:`. `refdeck.content()` рисует такую прозу ОДНИМ
   потоком текста (`body_blocks` → `fit_runs`), то есть собирается чисто,
   но без формы «плашка/колонки», которую требует текущая методика подачи
   (`CLAUDE.md` § «Форма подачи слайда»). Это и есть содержательная находка
   спайка, вынесенная в отчёт (не исправляется здесь).

Запуск:
  python3 build_section1_spike.py              — только PPTX
  python3 build_section1_spike.py --render     — ещё PDF+PNG (soffice, таймаут)
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent             # .../lec-11/rework/spike-deckkit
LEC_ROOT = HERE.parents[1]                          # .../lec-11
REPO_ROOT = HERE.parents[4]                         # корень репозитория
sys.path.insert(0, str(REPO_ROOT / "tools" / "presentation-build"))

from deckkit import (contrast, floor, markup, media, metrics, prims,  # noqa: E402
                     refdeck, render as rnd, report, slidefile)

SLIDES_DIR = LEC_ROOT / "slides"
OUT = HERE / "section1-spike.pptx"
SNAPS = HERE / "snapshots"

RANGE = "s06,s07,s08,s09,s10,s11,s12,s13"

# ─── адаптер №0: формат файла кадра у этой лекции — ДРУГОЙ ──────────────
# НАХОДКА, не предусмотренная докстрокой `slidefile.py`: ядро ждёт тело
# между явным заголовком `## Видимый текст слайда` и `## Заметки лектора`
# (см. формат файла в шапке `slidefile.py`). У `slides/s06..s13-*.md`
# Лекции 11 этого заголовка-обёртки НЕТ ВООБЩЕ — видимый текст идёт сразу
# после фронтматтера (первой строкой `# Заголовок`), а раздел заметок
# называется по-английски `## Speaker notes`, не `## Заметки лектора`.
# Без правки `read_slide()` находит ПУСТОЕ тело на всех восьми файлах
# (`[файл] sNN: нет раздела «Видимый текст слайда»`) — кадр собирается
# БЕЗ ЕДИНОЙ СТРОКИ видимого текста, молча. Это тот же класс правки, что
# `build_lec08_v5.py` уже делал для `## Заметки` vs `## Заметки лектора`
# (см. его собственный docstring) — правится ЧИТАТЕЛЬ модулёвым атрибутом,
# а не файлы кадров: какой заголовок считать границей раздела — свойство
# НАБОРА ФАЙЛОВ, а не содержания. Видимый текст здесь — это ВСЁ тело ДО
# заголовка `## Speaker notes` (а не отдельный поднабор под своим
# заголовком), поэтому паттерн не просто переименован, а перестроен:
# первая группа — с начала тела и ЛЕНИВО до этой границы либо до конца.
slidefile._SEC_VIS = r"\A(.*?)(?=\n##[ \t]*Speaker notes[ \t]*\r?\n|\Z)"
slidefile._SEC_NOTES = r"##[ \t]*Speaker notes[ \t]*\r?\n(.*?)(?=\n##\s|\Z)"

# ─── пол кегля видимого слоя: 15 пт, решение владельца 29.10.2026 ───
# Поднят ЗДЕСЬ (пакет читает VIS_PT в момент вызова, см. `floor.py`
# docstring) — тот же приём, что `build_lec08_v5.py`/`build_lec09.py`.
# `refdeck.heading()` уже и так рисует заголовок с `floor=15.0` (значение
# внутри самого образца); тело у `refdeck.content()` проверяется не через
# `floor.py`, а через СТАРЫЙ механизм `metrics.check_proj` (порог 12,0,
# см. `metrics.PROJ_PT`, вызывается АВТОМАТИЧЕСКИ внутри `fit_runs`, когда
# деке назван `proj_base`, что `refdeck.Geometry.body_pt=15.0` и делает) —
# именно он и даёт «нарушения пола кегля 12pt», ожидаемые в задании. Подъём
# `floor.VIS_PT` здесь всё равно сделан — для `contrast`/любых будущих
# вызовов `floor.check_runs`, даже если текущий `refdeck.content()` его не
# зовёт ни разу (сам образец, см. его docstring, рассчитан на минимальный
# набор вызовов ядра, а не на полный набор сторожей настоящей деки).
floor.VIS_PT = 15.0

# ─── адаптер №1: заголовок — первая H1-строка тела, а не поле фронтматтера
# ──────────────────────────────────────────────────────────────────────
_TITLE_RE = re.compile(r"^#[ \t]+(.+?)[ \t]*\r?\n\s*\n", re.M)


def extract_title_if_missing(sl):
    """`sl.title` пуст (поля `title` у фронтматтера s07..s12 нет вовсе) —
    достать первую строку `# …` видимого тела В ПАМЯТИ и убрать её оттуда,
    чтобы `refdeck.heading()` нарисовала её КАК ЗАГОЛОВОК, а не как первый
    абзац тела (иначе assertion-headline напечатался бы дважды — один раз
    крупным заголовком через `sl.title`, если бы он там был, и один раз
    первым блоком тела через `body_blocks`).

    Файл кадра НЕ правится — это изменение только объекта `Slide` в памяти
    этого прогона."""
    if sl.title:
        return
    m = _TITLE_RE.match(sl.body)
    if not m:
        report.warn(
            f"[спайк-заголовок] {sl.sid}: нет поля `title` и тело не "
            "начинается строкой «# …» — заголовок рисоваться не будет")
        return
    sl.title = m.group(1).strip()
    sl.body = sl.body[m.end():]
    sl._cache.clear()


# ─── адаптер №2: подключение УЖЕ СУЩЕСТВУЮЩИХ ассетов старого сборщика ──
# `media:` в `slides/s07..s12-*.md` нет ни на одном файле — старый
# `build_lec11.py` вшивал путь к PNG/JPG литералом в Python-коде функции
# кадра (`s07_adoption`, `s08_market_estimates`, `s10_foundation_models`),
# а не читал его из `.md`. Файлы при этом РЕАЛЬНЫЕ и лежат на диске — это
# не замена контента, а демонстрация, что их можно подключить фронтматтер-
# эквивалентным способом (поле `media`, относительно `LEC_ROOT`), без
# правки `.md`. Выбран ПО ОДНОМУ ассету на кадр (контент-кадр `content()`
# рисует один боковой снимок, не два) — там, где у старого сборщика было
# два чарта (`s07`), взят более информативный (bar, не donut).
MEDIA_OVERRIDE = {
    "s07": "rendered/assets/charts/s07-pilot-failure.png",
    "s08": "rendered/assets/charts/s08-market-divergence.png",
    "s10": "rendered/assets/screenshots/s10-siemens-hq.jpg",
}


def apply_media_override(sl):
    rel = MEDIA_OVERRIDE.get(sl.sid)
    if rel and (LEC_ROOT / rel).exists():
        sl.meta["media"] = rel
    elif rel:
        report.warn(f"[спайк-ассет] {sl.sid}: ожидался файл {rel}, "
                    "которого нет на диске")


# refdeck.content() рисует плашки/схему/число/столбцы ТОЛЬКО если
# `sl.meta.get("type")` лежит в `CONTENT_TYPES` образца — а там нет
# `assertion_visual` (образец знает только свой игрушечный словарь типов).
# Расширяется здесь, РАНТАЙМОМ, а не правкой `refdeck.py`: ни один из этих
# восьми кадров сегодня не несёт `blocks:`/`scheme:`/`columns:`, так что на
# ЭТОМ входе расширение ничего не меняет — оно просто не оставляет ложного
# «молчания», если кадр такое поле когда-нибудь получит.
refdeck.CONTENT_TYPES.add("assertion_visual")


BUILDERS = {"section_divider": refdeck.divider}


def content_adapter(p, sl, root, g):
    extract_title_if_missing(sl)
    return refdeck.content(p, sl, root, g)


def build(slides_dir, out, *, root, only):
    root = root or slides_dir
    p = prims.new_deck()
    n = 0
    for f in slidefile.slide_files(slides_dir, only):
        sl = slidefile.read_slide(f)
        if sl is None:
            continue
        apply_media_override(sl)
        kind = str(sl.meta.get("type") or "assertion_visual").strip()
        builder = BUILDERS.get(kind, content_adapter)
        s = (builder(p, sl, root, refdeck.G) if builder is content_adapter
             else builder(p, sl, root, refdeck.G))
        markup.notes_with_links(s, sl.notes)
        if sl.sid not in report.GOLD_SEEN:
            report.warn(f"[золото] {sl.sid}: золотого акцента на кадре нет")
        n += 1
    metrics.font_gaps()
    p.save(str(out))
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--render", action="store_true",
                    help="ещё PDF и PNG (soffice+pdftoppm, с таймаутом)")
    args = ap.parse_args()

    report.reset()
    n = build(SLIDES_DIR, OUT, root=LEC_ROOT, only=RANGE)
    blocking = report.report(n, out_name=OUT.name)

    from pptx import Presentation
    prs = Presentation(str(OUT))
    rows = contrast.check(prs, tag=OUT.name)
    bad = [r for r in rows if r["ok"] is False]
    print(f"\nконтраст видимого слоя: прогонов {len(rows)}, ниже порога "
          f"{len(bad)} на {len({r['page'] for r in bad})} кадрах")
    for r in bad:
        print(f"  стр {r['page']} {r['shape']}: «{r['text']}» — "
              f"{r['ratio']:.2f}:1 (порог {r['thr']:.1f}:1)")

    if args.render:
        rc = rnd.render(OUT, SNAPS)
        if rc:
            return rc

    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
