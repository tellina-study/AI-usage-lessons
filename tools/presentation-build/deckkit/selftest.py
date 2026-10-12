# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА ЯДРА: каждая проверка — на нарочно сломанном входе.

Стандарт здесь один и он не обсуждается: ПРОВЕРКА, НЕ ПРОВЕРЕННАЯ НА
СЛОМАННОМ ВХОДЕ, — НЕ ПРОВЕРКА. Поэтому на каждое предупреждение два
прогона: чистый кадр (обязан молчать) и сломанный (обязан сработать).

Сверх файловых проб идут РАЗНОСТНЫЕ — те, где мало знать, что
предупреждение сработало, надо знать, ОТ ЧЕГО оно сработало:

  [отбивка]       от отбивки абзаца, и ровно на её величину (7 пт на разрыв)
  [курсив]        от курсива, и так, что коэффициентом это не лечится
  [мера-06]       мера ядра совпадает с мерой Лекции 6 на однородном тексте
  [предел-столбца] столбец не уже своего слова — И без предела был бы уже
  [зебра]         полосы таблицы идут в том порядке, в каком шли
  [схема-ии]      «модель» — шаг модели, «моделирование» — НЕ шаг модели
  [тень]          `<p:style>` снимается, и флаг делает ровно то, что обещает
  [шрифт]         отсутствующее начертание выходит пробелом, а не оценкой
  [ссылка-живая]  гиперссылка лежит в пакете как `r:id`, а не как синий текст
  [отпечаток]     регрессия ловит сдвиг фигуры на ОДИН EMU

Запуск:  python3 -m deckkit.selftest
"""
import sys
import tempfile
from pathlib import Path

from PIL import Image

from . import (markup, metrics, plates, prims, probes, refdeck, regress,
               report, scheme, tables)
from .theme import SURFACE, WHITE

OK, BAD, SAID = [], [], []


def say(line):
    SAID.append(line)
    print(line)


def _assets(d):
    """Снимки под пробы §5.9: портрет (0,67 — даёт четверть площади) и
    широкий. Рисуются здесь, а не берутся из деки: проба ядра не вправе
    зависеть от ассетов лекции."""
    Image.new("RGB", (670, 1000), (200, 210, 220)).save(d / "probe-portrait.png")
    Image.new("RGB", (1500, 1000), (210, 215, 225)).save(d / "probe-wide.png")


def _run(files, tmp, seq, name="probe"):
    report.reset()
    tables.reset_caches()
    seq[0] += 1
    d = tmp / f"d{seq[0]}"
    d.mkdir()
    _assets(d)
    for nm, txt in files:
        (d / nm).write_text(txt, encoding="utf-8")
    refdeck.build(d, tmp / f"{name}.pptx", root=d)
    return list(report.WARNINGS)


# ════════════════════════════════════════════════════════════════════
# файловые пробы
# ════════════════════════════════════════════════════════════════════


def file_probes(tmp, seq):
    base = _run([("s01-clean.md", probes.CLEAN),
                 ("s02-clean-table.md", probes.CLEAN_TABLE)],
                tmp, seq, name="clean")
    say("── САМОПРОВЕРКА ЯДРА ────────────────────────────────────────")
    say(f"чистые кадры (прогон и таблица): предупреждений {len(base)}"
        + (" — " + "; ".join(base) if base else " (молчат, как и должны)"))
    (BAD if base else OK).append("[чистый кадр]")
    if base:
        BAD.append("чистый кадр выдал предупреждение — проверка шумит")

    for key, (sid, txt) in probes.BROKEN.items():
        tag, _, need = key.partition(" ")
        w = _run([(f"{sid}-broken.md", txt)], tmp, seq)
        hit = [x for x in w if x.startswith(tag) and (not need or need in x)]
        say(f"{key:<24} на сломанном входе: "
            + ("ЛОВИТ" if hit else "НЕ ЛОВИТ")
            + (f"  →  {hit[0][:88]}" if hit else ""))
        if key in probes.LABELS:
            say(f"{'':24} доказывает: {probes.LABELS[key]}")
        (OK if hit else BAD).append(key)

    # Два файла на один номер кадра: читатель молча берёт первый, и об этом
    # обязан сказать.
    w = _run([("s01-a.md", probes.CLEAN), ("s01-b.md", probes.CLEAN)],
             tmp, seq)
    hit = [x for x in w if x.startswith("[файлы]")]
    say(f"{'[файлы]':<24} на сломанном входе: "
        + ("ЛОВИТ" if hit else "НЕ ЛОВИТ")
        + (f"  →  {hit[0][:88]}" if hit else ""))
    (OK if hit else BAD).append("[файлы]")
    return base


# ════════════════════════════════════════════════════════════════════
# разностные пробы
# ════════════════════════════════════════════════════════════════════


def probe_space_before():
    """Отбивка абзацев входит в меру — и ровно на свою величину.

    Без этой половины достаточно было бы уменьшить отбивку вдвое:
    предупреждение осталось бы на месте, а мера снова начала бы врать,
    только тише."""
    probe = [{"text": f"Абзац {i}.", "size": 15.0,
              **({"newpara": True, "space_before": 7} if i > 1 else {})}
             for i in range(1, 9)]
    flat = [{k: v for k, v in r.items() if k != "space_before"} for r in probe]
    w = 12.23
    delta = metrics.runs_h(probe, w, 1.26) - metrics.runs_h(flat, w, 1.26)
    want = 7 * 7.0 / 72.0            # семь разрывов на восемь абзацев
    if abs(delta - want) > 0.005:
        BAD.append(f"[отбивка] мера разрыва {delta:.3f}\" против положенных "
                   f"{want:.3f}\" — отбивка считается не вся")
    else:
        OK.append("[отбивка]")
        say(f"{'[отбивка]':<24} в мере высоты: ЛОВИТ  →  восемь абзацев дают "
            f"{delta:.3f}\" разрывов, ровно 7 пт на каждый")


def probe_italic():
    """Курсив меряется СВОИМИ метриками, и коэффициентом это не лечится.

    Берётся та самая строка, на которой дефект был виден: оговорка плашки
    `s63` Лекции 7 во всю ширину плашечной колонки. По ней держатся три
    утверждения сразу.
      1. Правда — ТРИ строки, а мера по прямому начертанию обещает две.
      2. Коэффициент не спасает ни щедрый (1,031 — тот, что стоял), ни
         точный для этой строки: оба дают те же две строки.
      3. Единого верного коэффициента не существует, и видно это внутри
         ОДНОЙ строки: «дублированная» в курсиве УЖЕ прямого,
         «рецензентов» — ШИРЕ. Одно число не может быть одновременно меньше
         единицы и больше неё."""
    note = ("слепая дублированная оценка 22 рецензентов "
            "на 100 госпитализациях")
    st = plates.LEC07
    iw = (12.23 - st.gap * 3) / 4 - 2 * st.pad
    true_n = metrics.n_lines(note, st.note_pt, iw, False, True)
    own = metrics._unit_w(note, False, True) / metrics._unit_w(note, False,
                                                               False)
    proxy = {c: metrics.n_lines(note, st.note_pt, iw / c, False, False)
             for c in (1.0, 1.0235, 1.031)}
    narrow = (metrics._unit_w("дублированная", False, True)
              / metrics._unit_w("дублированная", False, False))
    wide = (metrics._unit_w("рецензентов", False, True)
            / metrics._unit_w("рецензентов", False, False))
    if true_n != 3 or any(v != 2 for v in proxy.values()):
        BAD.append(f"[курсив] правда {true_n} строк, прокси по "
                   f"коэффициентам {proxy} — проба больше не доказывает, "
                   "что коэффициент не спасает")
    elif not narrow < 1.0 < wide:
        BAD.append(f"[курсив] внутри одной строки курсив больше не отходит "
                   f"от прямого в ДВЕ стороны ({narrow:.3f} и {wide:.3f}) — "
                   "похоже, мера снова идёт по одному начертанию")
    else:
        OK.append("[курсив]")
        say(f"{'[курсив]':<24} в мере числа строк: ЛОВИТ  →  правда "
            f"{true_n} строки, прокси по прямому даёт 2 при любом "
            f"коэффициенте (1,0 · {own:.4f} своё · 1,031 прежний); в одной "
            f"строке курсив и уже прямого ({narrow:.3f}), и шире "
            f"({wide:.3f})")


def probe_lec06_parity():
    """Мера ядра = мера Лекции 6 на ОДНОРОДНОМ тексте.

    Это то утверждение, на котором держится вся регрессия: если бы мера
    расходилась, общее ядро сдвигало бы геометрию доставленной деки,
    прочитанной залу. Здесь оно проверяется прямо — своей, независимой
    реализацией прежней меры, а не ссылкой на то, что регрессия прошла."""
    def old_n_lines(text, size, w_in, bold=False):
        maxw = w_in * 72.0
        words = text.split()
        if not words:
            return 1
        lines, cur = 1, words[0]
        for wd in words[1:]:
            t = cur + " " + wd
            if metrics.text_w(t, size, bold) <= maxw:
                cur = t
            else:
                lines, cur = lines + 1, wd
        return lines

    def old_est(text, size, w_in, ls, bold=False):
        rows = sum(old_n_lines(p, size, w_in, bold) for p in text.split("\n"))
        return rows * size * ls * metrics.LH / 72.0 * metrics.SAFE

    cases = [
        ("Короткая строка", 15.0, 3.0, 1.24, False),
        ("Классификация на тексте: на входе элемент спецификации, на выходе "
         "метка «требование / не требование»", 13.5, 4.45, 1.18, False),
        ("ЗАГОЛОВОК ПОЛУЖИРНЫМ НА УЗКОЙ КОЛОНКЕ", 11.0, 1.7, 1.08, True),
        ("Абзац\nс разрывом\nи ещё одним", 16.0, 6.0, 1.26, False),
        ("", 16.0, 6.0, 1.18, False),
        ("Неразрывноеоченьдлинноеслово", 17.0, 1.2, 1.22, True),
    ]
    diff = []
    for text, size, w, ls, bold in cases:
        a, b = metrics.n_lines(text, size, w, bold), old_n_lines(text, size,
                                                                 w, bold)
        c, d = metrics.est_h(text, size, w, ls, bold), old_est(text, size, w,
                                                               ls, bold)
        if a != b or abs(c - d) > 1e-12:
            diff.append((text[:28], a, b, c, d))
    if diff:
        BAD.append(f"[мера-06] мера ядра разошлась с прежней на "
                   f"{len(diff)} входах: {diff[:2]}")
    else:
        OK.append("[мера-06]")
        say(f"{'[мера-06]':<24} совместимость меры: ЛОВИТ  →  на {len(cases)} "
            "однородных входах число строк и высота совпадают с прежней "
            "мерой Лекции 6 до последнего знака")


def probe_col_min():
    """Предел ширины столбца работает — И без него столбец был бы уже слова.

    Проба разностная нарочно: «все столбцы шире своих слов» — утверждение,
    которое верно и у таблицы, где делить нечего. Ценность в том, что
    ПРОПОРЦИОНАЛЬНОЕ деление (как было до правки) эту же таблицу ломает."""
    table = [["Прослеживаемость",
              "Что именно делает режим и как это проверяют на практике "
              "инженером и врачом вместе", "Да"],
             ["Электроэнцефалографический",
              "отбирает спорные места в спецификации и передаёт их человеку "
              "на проверку целиком", "Нет"],
             ["Структурированность",
              "проверяет разметку человека и сверяет её с разметкой модели "
              "по всем срезам", "Да"]]
    rows = tables.rows_of(table)
    size, w = 11.0, 8.0
    widths = tables.table_widths(rows, size, w)
    mins = tables.col_min(rows, size, tables.TBL_TIGHT)
    want = tables.col_want(rows, size)
    tot = sum(want)
    naive = [w * x / tot for x in want]
    starved = [j for j in range(len(mins)) if naive[j] < mins[j] - 1e-9]
    broken = [j for j in range(len(mins)) if widths[j] < mins[j] - 1e-9]
    if not starved:
        BAD.append("[предел-столбца] пропорциональное деление этой таблицы "
                   "уже никого не обделяет — проба перестала доказывать "
                   "правку, её вход надо подобрать заново")
    elif broken:
        BAD.append(f"[предел-столбца] столбцы {broken} вышли уже своего "
                   "самого длинного слова — предел не держит")
    else:
        OK.append("[предел-столбца]")
        say(f"{'[предел-столбца]':<24} ширины столбцов: ЛОВИТ  →  "
            f"пропорциональное деление обделяло столбцы {starved} "
            f"({naive[starved[0]]:.2f}\" против нужных "
            f"{mins[starved[0]]:.2f}\"), с пределом ни один не уже своего "
            "слова")


def probe_zebra(tmp):
    """Порядок полос таблицы. Переставленная пара даёт ровную шахматку
    наоборот — на снимке почти не видно, в XML видно сразу. Регрессия на
    деке Лекции 6 этот порядок уже один раз поймала; здесь он закреплён
    пробой, чтобы впредь ловилось без деки."""
    report.reset()
    tables.reset_caches()
    p = prims.new_deck()
    s = prims.blank(p)
    table = [["Шапка", "Вторая"], ["первая", "строка"], ["вторая", "строка"]]
    tables.draw_table(s, 0.5, 0.5, table, 11.0, 6.0, "проба")
    fills = []
    for shp in s.shapes:
        try:
            fills.append(str(shp.fill.fore_color.rgb))
        except Exception:
            fills.append(None)
    # На каждую ячейку по ДВЕ фигуры: плашка и надпись. Шапка — ячейки 0-1,
    # то есть фигуры 0-3; первая строка — фигуры 4-7, вторая — 8-11.
    row1, row2 = fills[4:8:2], fills[8:12:2]
    # Первая строка после шапки — БЕЛАЯ, вторая на поверхности: `i % 2`,
    # где `i` — номер строки вместе с шапкой. Порядок выглядит обратным
    # интуиции и ровно поэтому закреплён пробой: регрессия на деке Лекции 6
    # поймала его переставленным, и на снимке это почти не видно.
    want1, want2 = str(WHITE), str(SURFACE)
    if row1 != [want1, want1] or row2 != [want2, want2]:
        BAD.append(f"[зебра] полосы таблицы пошли {row1} / {row2}, а должны "
                   f"{want1} / {want2}")
    else:
        OK.append("[зебра]")
        say(f"{'[зебра]':<24} порядок полос таблицы: ЛОВИТ  →  первая строка "
            f"после шапки белая ({want1}), вторая на поверхности ({want2})")


def probe_scheme_ai():
    """«модель» — шаг модели, «моделирование» — НЕ шаг модели.

    Поймано на настоящем `s02` Лекции 6: карта цикла изделия получила
    золотую обводку на стадии «3. Моделирование», которая к модели не
    относится. Утверждение разностное: один вход обязан сработать, другой
    обязан НЕ сработать."""
    yes = bool(scheme.AI_WORD.search("модель отбирает спорное"))
    no = bool(scheme.AI_WORD.search("3. Моделирование"))
    also = bool(scheme.AI_WORD.search("нейросеть размечает"))
    if not (yes and also) or no:
        BAD.append(f"[схема-ии] «модель» {yes}, «нейросеть» {also}, "
                   f"«Моделирование» {no} — различение сломано")
    else:
        OK.append("[схема-ии]")
        say(f"{'[схема-ии]':<24} шаг модели: ЛОВИТ  →  «модель» и "
            "«нейросеть» да, «Моделирование» нет")


def probe_shadow():
    """Тень снимается удалением `<p:style>`, и флаг делает ровно то, что
    обещает. По умолчанию — снимается: это разногласие двух сборщиков,
    разобранное в пользу Лекции 6 (`notes/mcp-limitations.md` [#223-8])."""
    P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
    res = {}
    for flag in (True, False):
        prims.STRIP_THEME_STYLE = flag
        p = prims.new_deck()
        s = prims.blank(p)
        shp = prims.ocean_box(s, 1, 1, 2, 1)
        res[flag] = len(shp._element.findall(P + "style"))
    prims.STRIP_THEME_STYLE = True
    if res[True] != 0 or res[False] == 0:
        BAD.append(f"[тень] со снятием осталось стилей {res[True]}, без "
                   f"снятия {res[False]} — флаг не делает того, что обещает")
    else:
        OK.append("[тень]")
        say(f"{'[тень]':<24} снятие темы: ЛОВИТ  →  по умолчанию `<p:style>` "
            f"снят (0), а в режиме воспроизведения Лекции 7 остаётся "
            f"({res[False]}) — именно он и даёт тень в LibreOffice")


def probe_font_gap():
    """Отсутствующее начертание выходит ПРОБЕЛОМ `[шрифт]`, а не молчаливой
    оценкой по соседнему файлу."""
    report.reset()
    saved = dict(metrics._TTF)
    cache = dict(metrics._FCACHE)
    gaps = dict(metrics._FONT_GAP)
    try:
        metrics._TTF[(False, True)] = Path("/nonexistent/NoSuchFace.ttf")
        metrics._FCACHE.pop((False, True), None)
        metrics._FONT_GAP.clear()
        metrics.text_w("проба", 12.0, False, True)
        metrics.font_gaps()
        hit = [w for w in report.WARNINGS if w.startswith("[шрифт]")]
    finally:
        metrics._TTF.clear(); metrics._TTF.update(saved)
        metrics._FCACHE.clear(); metrics._FCACHE.update(cache)
        metrics._FONT_GAP.clear(); metrics._FONT_GAP.update(gaps)
    if not hit:
        BAD.append("[шрифт] отсутствующее начертание прошло молча")
    else:
        OK.append("[шрифт]")
        say(f"{'[шрифт]':<24} на сломанном входе: ЛОВИТ  →  {hit[0][:88]}")


def probe_live_links(tmp):
    """Гиперссылка лежит в пакете как `r:id` на внешнее отношение, а не как
    подчёркнутый синий текст. Самоотчёт не принимается — считается XML."""
    import zipfile
    from lxml import etree
    A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
    path = tmp / "clean.pptx"
    body = notes = targets = 0
    with zipfile.ZipFile(path) as z:
        for nm in z.namelist():
            if not nm.endswith(".xml"):
                continue
            if nm.startswith("ppt/slides/slide"):
                root = etree.fromstring(z.read(nm))
                body += sum(1 for e in root.iter(f"{A}hlinkClick")
                            if e.get(f"{R}id"))
            elif nm.startswith("ppt/notesSlides/notesSlide"):
                root = etree.fromstring(z.read(nm))
                notes += sum(1 for e in root.iter(f"{A}hlinkClick")
                             if e.get(f"{R}id"))
        for nm in z.namelist():
            if ".rels" in nm and ("slides/_rels" in nm
                                  or "notesSlides/_rels" in nm):
                root = etree.fromstring(z.read(nm))
                targets += sum(1 for e in root.iter()
                               if (e.get("Type") or "").endswith("/hyperlink"))
    if body < 1 or notes < 1 or targets < 2:
        BAD.append(f"[ссылка-живая] в XML чистого кадра подвал {body}, "
                   f"заметки {notes}, отношений {targets} — ждали хотя бы "
                   "по одной и двух отношений")
    else:
        OK.append("[ссылка-живая]")
        say(f"{'[ссылка-живая]':<24} в пакете: ЛОВИТ  →  подвал {body} · "
            f"заметки {notes} · отношений {targets}")


def probe_fingerprint(tmp):
    """Проверка на саму проверку: отпечаток регрессии обязан поймать сдвиг
    фигуры на ОДИН EMU. Отпечаток, который «всегда совпадает», доказывал бы
    не совпадение дек, а собственную слепоту."""
    from pptx.util import Emu
    src = tmp / "clean.pptx"
    p = prims.new_deck()
    s = prims.blank(p)
    prims.ocean_box(s, 1, 1, 2, 1)
    a = tmp / "fp-a.pptx"
    b = tmp / "fp-b.pptx"
    p.save(str(a))
    s.shapes[0].width = Emu(s.shapes[0].width + 1)
    p.save(str(b))
    same = regress.compare(regress.fingerprint(a), regress.fingerprint(a))
    diff = regress.compare(regress.fingerprint(a), regress.fingerprint(b))
    if same or not diff:
        BAD.append(f"[отпечаток] сам с собой {len(same)} расхождений, со "
                   f"сдвигом на 1 EMU — {len(diff)}; отпечаток слеп")
    else:
        OK.append("[отпечаток]")
        say(f"{'[отпечаток]':<24} чувствительность: ЛОВИТ  →  сдвиг на 1 EMU "
            f"даёт {len(diff)} расхождение, файл сам с собой — 0")
    # Побайтово те же два файла неотличимы от любых других: метки времени
    # делают байтовое сравнение неработающим, а не строгим.
    say(f"{'':24} (байтовое сравнение здесь не годится: `python-pptx` "
        "пишет в пакет метки времени)")


# ════════════════════════════════════════════════════════════════════


def selftest():
    tmp = Path(tempfile.mkdtemp(prefix="deckkit-selftest-"))
    seq = [0]
    file_probes(tmp, seq)
    say("── разностные пробы ─────────────────────────────────────────")
    probe_space_before()
    probe_italic()
    probe_lec06_parity()
    probe_col_min()
    probe_zebra(tmp)
    probe_scheme_ai()
    probe_shadow()
    probe_font_gap()
    probe_live_links(tmp)
    probe_fingerprint(tmp)
    say("─────────────────────────────────────────────────────────────")
    total = len(OK) + len(BAD)
    say(f"проверок доказано: {len(OK)} из {total}")
    if BAD:
        say("НЕ ДОКАЗАНО:")
        for x in BAD:
            say("  " + x)
        return 1
    say("все проверки доказаны на сломанном входе")
    return 0


if __name__ == "__main__":
    sys.exit(selftest())
