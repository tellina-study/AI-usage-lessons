#!/usr/bin/env python3
"""Общие примитивы восьми программных схем Семинара 9 (issue #299).

Восемь схем «слоя 1» живут в семи рисовалках рядом с этим файлом
(`make_figures_lestnitsa.py`, `..._k1.py` … `..._k6.py`). Общего в них три
вещи, и каждая куплена порогом сторожа, а не вкусом.

── 1. КЕГЛЬ МЕРЯЕТСЯ, А НЕ ОЦЕНИВАЕТСЯ ─────────────────────────────────────

Порог деки — **не ниже 7,5 pt** (`tools/seminar-production/README.md` §7).
Кегль схемы живёт в ПИКСЕЛЯХ холста, и переводной коэффициент — не свойство
рисовалки: он зависит от того, какой ШИРИНЫ картинка в итоге встанет на
слайд. `deck_kit.figure` вписывает схему в отведённый прямоугольник
(`deck_config.WIDTH` = 12,23″) и, когда не хватает высоты, ужимает её ЦЕЛИКОМ
вместе с шириной (потолок приёма — `deck_kit.FIG_NATURAL_H` = 4,3″).

Отсюда формула `pt_floor` ниже и единственное правило композиции, которое
здесь нельзя нарушать: **холст 2400 px шириной и не выше 843 px**. При таком
отношении сторон (843/2400 = 0,351) схема встаёт в полную ширину 12,23″, то
есть 196,2 px на дюйм, и один пиксель кегля стоит 0,367 pt. Пол в 24 px даёт
8,81 pt — запас к порогу, а не касание его.

Схема выше 843 px при той же ширине ужимается по высоте, плотность растёт, и
тот же кегль в пикселях даёт МЕНЬШЕ пунктов. Поэтому `pt_report` печатает
пункты для обоих случаев (потолок приёма 4,3″ и полная ширина) и ругается
сам, а не ждёт, пока кто-нибудь посмотрит на схему глазами. На глаз кегль
схем в этом курсе мерили дважды и дважды ошиблись (`sem-06/qa/kegl-shem-ru.md`).

── 2. ПАЛИТРА ЗАКРЫТА СЕМЬЮ ЦВЕТАМИ ────────────────────────────────────────

Разрешены ровно: `#21295C` · `#065A82` · `#1C7293` · тил `#028090` · золото
`#F0AB00` · поверхность `#F4F7FA` · белый. Всё остальное из тулкита
(`RED`, `MUTE`, `WARM`, `PALE`, `GREY_*`, `INK`, `GOLDINK`…) в этих восьми
схемах НЕ применяется, и `audit_sources` ругается на само упоминание такого
имени в исходнике. Тёмный текст — `DEEP`, вторичный — `LIGHT`: ровно те роли,
что назначены палитре в `CLAUDE.md`.

Из этого следует одно неудобство, которое стоит знать заранее: у `clabel` и
`box` тулкита умолчание цвета — `INK`/`W`, то есть цвет МИМО палитры.
Поэтому здесь свои обёртки (`txt`, `ctxt`, `wrapped`, `card`, `plashka`), и у
них цвет — обязательный параметр без умолчания.

── 3. ПОДПИСИ ВНУТРИ СХЕМ — ПИКСЕЛИ, И ГРЕП ПО ДЕКЕ ДАЁТ ПО НИМ НОЛЬ ────────

Канон §7: снятые термины, обещания залу, тайминг, методические комментарии,
англицизмы и формат сопоставления «не X, а Y» (`tools/editorial/README.md`
§1) внутри фигур ищутся в ИСХОДНИКЕ рисовалки, а не в её выводе.
`audit_sources` делает это сам: собирает каждую строку, которая реально дошла
до холста (через тот же патч `ImageDraw.text`, которым тулкит переводит
подписи), и проверяет её по трём спискам — запрещённые обороты (включая
сопоставление, из общего `sopostavlenie_figury.FIGURY` — issue #299, дыра 1),
латиница, научная запись. Самоотчёт «я проверил» проверкой не считается,
поэтому аудит печатает НАЙДЕННОЕ, а не слово «чисто».

Запуск: `python3 make_figures_all.py` рисует все восемь и печатает замеры.
"""
import re
import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))

from fig_toolkit import *          # noqa: F401,F403  — примитивы и палитра
from fig_toolkit import DREW, WARN
# Запрет «не X, а Y» (issue #299, дыра 1) — ОДИН источник на два сторожа:
# `audit_sopostavleniya.py` читает его по собранному `.pptx`, этот модуль —
# по строкам, реально дошедшим до холста схемы. Подписи схем — пиксели, и
# грепу по деке неоткуда взять этот запрет для них иначе. См. докстринг
# `sopostavlenie_figury.py`.
from sopostavlenie_figury import FIGURY as _SOPOSTAVLENIE_FIGURY

# ── Палитра, закрытая на семь цветов ───────────────────────────────────────
PALETTE = {
    "#21295C": DEEP, "#065A82": MID, "#1C7293": LIGHT,
    "#028090": TEAL, "#F0AB00": GOLD, "#F4F7FA": SURF, "#FFFFFF": W,
}
FORBIDDEN_NAMES = ("RED", "MUTE", "WARM", "PALE", "GHOST", "DIMTX", "GOLDTX",
                   "DARKCARD", "GOLDINK", "GREY_FILL", "GREY_TX", "SOFT_GREY", "INK")

# Геометрия, общая для всех восьми (см. докстринг §1).
CW = 2400
H_MAX = 843
SLOT_W = 12.23      # deck_config.WIDTH — ширина отведённого схеме места, дюймы
FIG_CEIL = 4.3      # deck_kit.FIG_NATURAL_H — потолок высоты приёма, дюймы
PT_FLOOR = 7.5      # порог деки, tools/seminar-production/README.md §7
PT_TARGET = 8.3     # свой запас: касаться порога нечем

DRAWN = []          # каждая строка, дошедшая до холста (для аудита исходника)

_PATCHED_TEXT = ImageDraw.ImageDraw.text


def _text_collect(self, xy, text, *a, **k):
    if isinstance(text, str) and text.strip():
        DRAWN.append(text)
    return _PATCHED_TEXT(self, xy, text, *a, **k)


ImageDraw.ImageDraw.text = _text_collect


# ── Замер кегля в пунктах ──────────────────────────────────────────────────
def pt_floor(w_px, h_px, kegl_px, *, max_h=FIG_CEIL, slot_w=SLOT_W):
    """Сколько ПУНКТОВ даст кегль `kegl_px` на холсте `w_px`×`h_px`.

    Повторяет арифметику `deck_kit.figure`: ширина на слайде — отведённая,
    пока хватает высоты; когда не хватает, схема ужимается целиком, и
    ширина становится производной от высоты."""
    fw = min(slot_w, max_h * w_px / h_px)
    return kegl_px * 72 * fw / w_px


def pt_report(title="схемы Семинара 9"):
    """Печатает замер по каждой нарисованной схеме и падает, если пол кегля
    ниже порога деки. Пол в пикселях приходит из `fig_toolkit.DREW` — его
    собирает патч `ImageDraw.text`, то есть замер идёт по тому, что реально
    нарисовано, а не по тому, что задумано."""
    print(f"\n{title} — замер кегля:")
    print(f"   {'схема':34} {'холст':>11} {'кегль':>7} {'в ширину':>9} {'ужатая':>8}")
    bad = []
    for name, size, kegl in DREW:
        if kegl is None:
            continue
        w_px, h_px = size
        full = kegl * 72 * SLOT_W / w_px
        shrunk = pt_floor(w_px, h_px, kegl)
        mark = "" if shrunk >= PT_FLOOR else "  ✘ НИЖЕ ПОРОГА"
        if shrunk < PT_FLOOR:
            bad.append((name, shrunk))
        print(f"   {name:34} {w_px:>5}×{h_px:<5} {kegl:>4} px "
              f"{full:>7.2f} pt {shrunk:>6.2f} pt{mark}")
        if h_px > H_MAX:
            print(f"      ⚠ холст выше {H_MAX} px — схема ужмётся по высоте, "
                  f"и пол кегля упадёт до {shrunk:.2f} pt")
    print(f"\n   порог деки {PT_FLOOR} pt · свой запас {PT_TARGET} pt · "
          f"ниже порога: {len(bad)}")
    if WARN:
        print("\nПРЕДУПРЕЖДЕНИЯ (текст шире отведённого места):")
        for w_ in dict.fromkeys(WARN):
            print("  ", w_)
    else:
        print("   предупреждений о ширине нет: весь текст укладывается в блоки")
    return bad


# ── Подписи: цвет обязателен, ширина проверяется ───────────────────────────
def txt(d, x, y, s, sz, col, *, b=False, m=False, limit=None, where="?"):
    fo = f(sz, b, m)
    if limit:
        fit(d, s, fo, limit, where)
    d.text((x, y), s, font=fo, fill=col)
    return sz


def ctxt(d, cx, y, s, sz, col, *, b=False, m=False, limit=None, where="?"):
    fo = f(sz, b, m)
    if limit:
        fit(d, s, fo, limit, where)
    d.text((cx - d.textlength(s, font=fo) / 2, y), s, font=fo, fill=col)
    return sz


def wrapped(d, x, y, s, sz, col, limit, *, b=False, lh=None, center=None, where="?"):
    """Длинная подпись становится несколькими строками, а не выезжает за
    край. Возвращает занятую высоту — композиция считается по ней."""
    fo = f(sz, b)
    lh = lh or sz + 7
    lines = wrap(d, s, fo, limit)
    lines_at(d, x, y, lines, fo, col, lh, center=center)
    return len(lines) * lh - (lh - sz)


def runs(d, x, y, parts, sz, *, limit=None, where="?"):
    """Строка из кусков разного начертания и цвета: `[(текст, цвет, жирный)]`.
    Нужна там, где название и пояснение стоят В ОДНУ строку — иначе пришлось
    бы или разрывать строку, или терять разницу между ними."""
    cx = x
    for s, col, bold in parts:
        fo = f(sz, bold)
        d.text((cx, y), s, font=fo, fill=col)
        cx += d.textlength(s, font=fo)
    if limit and cx - x > limit:
        WARN.append(f"{where}: строка из кусков шире отведённого на "
                    f"{cx - x - limit:.0f} px")
    return cx - x


# ── Поверхности ────────────────────────────────────────────────────────────
def card(d, x, y, w, h, *, fill=SURF, stroke=LIGHT, sw=3, r=16):
    """Окружение содержательного блока — та самая «океанская скруглённая
    коробка», один повторяющийся элемент на всех схемах деки."""
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill,
                        outline=stroke, width=sw)


def node(d, x, y, w, h, title, sub, *, fill=SURF, stroke=LIGHT, sw=3,
         tcol=DEEP, scol=LIGHT, tsz=34, ssz=26, where="?"):
    """Узел схемы: название крупно, пояснение мельче, обе строки центрованы
    и обе переносятся по словам."""
    card(d, x, y, w, h, fill=fill, stroke=stroke, sw=sw)
    lim = w - 44
    fo_t, fo_s = f(tsz, True), f(ssz)
    t_lines = wrap(d, title, fo_t, lim)
    s_lines = wrap(d, sub, fo_s, lim) if sub else []
    th = len(t_lines) * (tsz + 8)
    sh = len(s_lines) * (ssz + 7)
    y0 = y + (h - th - (14 if s_lines else 0) - sh) / 2
    lines_at(d, 0, y0, t_lines, fo_t, tcol, tsz + 8, center=x + w / 2)
    if s_lines:
        lines_at(d, 0, y0 + th + 14, s_lines, fo_s, scol, ssz + 7,
                 center=x + w / 2)
    for ln in t_lines + s_lines:
        fit(d, ln, fo_t if ln in t_lines else fo_s, lim, where)


def plashka(d, x, y, w, h, number, label, *, tone="base", nsz=54, lsz=25,
            where="?"):
    """Число — плашкой, а не внутри абзаца (форма §5.14). `tone='glavnoe'` —
    золотая: ею помечается то одно число, из-за которого схема нарисована.

    Содержимое центруется по высоте ВМЕСТЕ: подпись в одну строку и подпись в
    две строки прежде давали плашки с разным пустым дном, и ряд из двух
    плашек читался съехавшим."""
    # Три вида плашки, и третий заведён не для красоты: внутри панели,
    # у которой СВОЯ цветная рамка, золотая рамка плашки спорит с ней за
    # смысл цвета. `chislo` оставляет золото числу и отдаёт рамку панели.
    gold = tone == "glavnoe"
    chislo = tone == "chislo"
    card(d, x, y, w, h, fill=W if gold else SURF,
         stroke=GOLD if gold else LIGHT, sw=5 if gold else 3)
    fo_l = f(lsz)
    lines = wrap(d, label, fo_l, w - 40)
    lh = lsz + 7
    block = nsz + 12 + len(lines) * lh - (lh - lsz)
    y0 = y + (h - block) / 2
    ctxt(d, x + w / 2, y0, number, nsz, GOLD if gold or chislo else MID, b=True,
         limit=w - 34, where=f"{where} · число")
    lines_at(d, 0, y0 + nsz + 12, lines, fo_l, DEEP if gold or chislo else LIGHT,
             lh, center=x + w / 2)


def plashka_para(d, x, y, w, h, left, right, caption, *, nsz=48, lsz=25,
                 csz=25, gold_idx=1, ramka=GOLD, where="?"):
    """Пара «было → стало» — ОДНА плашка, не два числа на разных местах
    (форма §5.14). Числа разводятся своими подписями, чтобы два похожих
    числа не стояли в одной фразе."""
    card(d, x, y, w, h, fill=W if ramka is GOLD else SURF, stroke=ramka,
         sw=5 if ramka is GOLD else 3)
    half = w / 2
    cap_h = 44 if caption else 0
    for i, (num, lab) in enumerate((left, right)):
        cx = x + half * (0.5 + i)
        ctxt(d, cx, y + 22, num, nsz, GOLD if i == gold_idx else MID, b=True,
             limit=half - 40, where=f"{where} · число {i + 1}")
        wrapped(d, cx - half / 2 + 20, y + 26 + nsz + 8, lab, lsz, DEEP,
                half - 40, center=cx, where=f"{where} · подпись {i + 1}")
    d.line([x + half, y + 22, x + half, y + h - cap_h - 14], fill=LIGHT, width=2)
    if caption:
        wrapped(d, x + 24, y + h - cap_h + 2, caption, csz, LIGHT, w - 48,
                center=x + w / 2, where=f"{where} · оговорка")


def tick(d, cx, cy, s, col, wd=5):
    """Залитая галочка — «прочитано верно»."""
    d.line([cx - s, cy, cx - s * 0.25, cy + s * 0.72], fill=col, width=wd)
    d.line([cx - s * 0.25, cy + s * 0.72, cx + s, cy - s * 0.62], fill=col, width=wd)


def cross(d, cx, cy, s, col, wd=5):
    d.line([cx - s, cy - s, cx + s, cy + s], fill=col, width=wd)
    d.line([cx - s, cy + s, cx + s, cy - s], fill=col, width=wd)


def person(d, cx, cy, s, col):
    """Человек в схеме: кто получает ответ или кому уходит заявка. Без него
    схема — четыре коробки без адресата."""
    d.ellipse([cx - s * 0.42, cy - s, cx + s * 0.42, cy - s * 0.16], fill=col)
    d.pieslice([cx - s * 0.82, cy - s * 0.1, cx + s * 0.82, cy + s * 1.5],
               180, 360, fill=col)


def padlock(d, cx, cy, s, col, *, open_=False):
    """Замок — «это значение код читает сам». Открытый замок — «значение
    пришло из текста, который читала модель»."""
    d.rounded_rectangle([cx - s, cy, cx + s, cy + s * 1.3], radius=s // 3, fill=col)
    # Дуга обязана КОНЧАТЬСЯ на верхней грани корпуса: вертикальный центр её
    # рамки — ровно `cy`. Иначе концы дуги висят выше корпуса, и закрытый
    # замок рисуется открытым (так и было на первом прогоне схемы гейта).
    bx = cx + (s * 0.55 if open_ else 0)
    d.arc([bx - s * 0.62, cy - s * 0.85, bx + s * 0.62, cy + s * 0.85], 180, 360,
          fill=col, width=max(4, s // 4))


# ── Аудит исходника: запреты живут в рисовалке, не в её выводе ─────────────
_LATIN_OK = {"n8n"}      # имя узла/инструмента — единственная разрешённая латиница
_BAN_PHRASES = (
    (r"\d+\s*мин(ут|\.)?\b", "тайминг в кадре"),
    (r"врем[яени]\s+раздел", "тайминг в кадре"),
    (r"тайминг|длительност", "тайминг в кадре"),
    (r"[⏱⏰]", "тайминг в кадре"),
    (r"методическ|педагогическ", "методический комментарий"),
    (r"на этом этапе студент|здесь студент|студент усваива", "методический комментарий"),
    # Обращение, а не слово: «связь с преподавателем» — пункт базы знаний
    # учебного центра, и ловить его этим сторожем значит ловить содержание.
    # Поэтому формы ДАТЕЛЬНОГО падежа, с якорями по обе стороны.
    (r"(?:^|[\s«(])(?:лектору|преподавателю|ведущему)(?:[\s:,.»)]|$)",
     "подсказка ведущему"),
    (r"вы здесь|мы здесь|разбор дальше|вернёмся|вернемся", "подсказка ведущему"),
    (r"ке[йи]с\s*\d|провал\b|надзаголов", "надзаголовок жанра"),
    (r"webhook|workflow\s*id|прогон\s*№", "служебный идентификатор"),
    (r"\d\s*[·,.]\d+\s*[·×]\s*10[⁰-₟\^]", "научная запись"),
    (r"\d\s*[·×]\s*10\s*[⁰-₟]", "научная запись"),
) + tuple(
    # Формат сопоставления «не X, а Y» (issue #299, дыра 1): те же шаблоны,
    # что `audit_sopostavleniya.py` применяет к собранному `.pptx` — здесь
    # к строкам, дошедшим до холста схемы. `re.search` принимает и готовый
    # compiled-паттерн, и строку, поэтому объекты из FIGURY подставляются
    # сюда без перекомпиляции и без второй копии регулярок.
    (rx, f"сопоставление {name}") for name, rx in _SOPOSTAVLENIE_FIGURY
)


def audit_sources():
    """Три проверки по ИСХОДНИКУ и по строкам, реально дошедшим до холста."""
    here = _Path(__file__).resolve().parent
    srcs = sorted(here.glob("make_figures_*.py"))
    print("\nаудит исходника рисовалок:")

    off = []
    for p in srcs:
        body = p.read_text(encoding="utf-8")
        body = re.sub(r'""".*?"""', "", body, flags=re.S)      # докстринги не рисуются
        # Сам список запрещённых имён — не их употребление: аудит обязан
        # пропускать собственное объявление, иначе ругается на себя.
        body = re.sub(r"FORBIDDEN_NAMES\s*=\s*\([^)]*\)", "", body, flags=re.S)
        body = re.sub(r"^PALETTE\s*=\s*\{[^}]*\}", "", body, flags=re.S | re.M)
        for name in FORBIDDEN_NAMES:
            for m in re.finditer(rf"(?<![A-Za-z_]){name}(?![A-Za-z_])", body):
                off.append(f"{p.name}: имя цвета мимо палитры — {name}")
        for m in re.finditer(r"#[0-9A-Fa-f]{6}", body):
            if m.group(0).upper() not in PALETTE:
                off.append(f"{p.name}: цвет мимо палитры — {m.group(0)}")
    print(f"   цвета: {'чисто' if not off else str(len(off)) + ' нарушений'}")
    for o in dict.fromkeys(off):
        print("     ✘", o)

    lat = {}
    for s in DRAWN:
        for w_ in re.findall(r"[A-Za-z][A-Za-z0-9+_-]{1,}", s):
            if w_.lower() not in {a.lower() for a in _LATIN_OK}:
                lat.setdefault(w_, s)
    print(f"   латиница в подписях: {len(lat)} уникальных"
          f"{' (разрешено: ' + ', '.join(sorted(_LATIN_OK)) + ')' if not lat else ''}")
    for w_, src in lat.items():
        print(f"     ✘ {w_!r} — в подписи {src[:70]!r}")

    hits = []
    for s in DRAWN:
        low = s.lower()
        for pat, why in _BAN_PHRASES:
            if re.search(pat, low):
                hits.append(f"{why}: {s[:70]!r}")
    print(f"   запрещённые обороты: {len(hits)}")
    for h in dict.fromkeys(hits):
        print("     ✘", h)

    print(f"   подписей на холсте всего: {len(DRAWN)} "
          f"({len(set(DRAWN))} уникальных)")
    return off, lat, hits
