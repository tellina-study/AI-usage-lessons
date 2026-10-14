# -*- coding: utf-8 -*-
"""РАЗНОСТНЫЕ ПРОБЫ: пол видимого слоя, лестница заголовка, число-заголовок,
тело в две колонки.

Правило то же, что у всего пакета: ПРОВЕРКА, НЕ ПРОВЕРЕННАЯ НА СЛОМАННОМ
ВХОДЕ, — НЕ ПРОВЕРКА. И то же уточнение, что в `selftest_layout.py`: на
четырёх из семи проб ниже мало знать, что предупреждение вышло, — надо
знать, ОТ ЧЕГО оно вышло, а значит собрать один и тот же вход дважды.

  [пол]                 подпись внутри ужатого тела уходит под 12 пт — и
                        названа; тому же кадру с запасом места — молчание
  [пол-класс]           пол видит НЕ ТОЛЬКО тело: оговорка плашки, набранная
                        10,5 пт, названа, а набранная 12 пт — нет
  [пол-таблица]         и клетку таблицы тоже: класс, который проходил мимо
                        пола ЦЕЛИКОМ, пока `tables.py` не звал `floor.pt`
  [пол-ручка]           порог, поднятый декой, ДЕЙСТВУЕТ: прежняя подпись
                        `floor=VIS_PT` застывала при импорте и ручку глушила
  [знаки-hex]           знак считается по кодировке файла: прежнее «всегда
                        четыре цифры» теряло односимвольный прогон НАЦЕЛО
  [пол-мимо-проекции]   вход, который старая проверка пропускала ПО
                        ПОСТРОЕНИЮ: номинал тела ровно на пороге, подпись
                        под ним
  [лестница-заголовка]  ступень выбрана по «ставится в одну строку», а не по
                        «влезает в рамку», — и на том же заголовке старое
                        правило давало две строки
  [заголовок-длинный]   заголовок, не влезающий в строку ни на одной
                        ступени, НАЗВАН, а не отдан деке молча
  [число-заголовок]     число встаёт крупнее фразы, фраза — под ним; число
                        без фразы отвергнуто
  [две-колонки]         две колонки взяты, когда кегль от них не падает, и
                        отвергнуты, когда упал бы; отказ возвращает кегли
"""
from . import (floor, metrics, pdfmeasure, plates, prims, probes_floor,
               report, tables, titles, twocol)
from .probes_layout import BRICK


def _runs(blocks, per=3, cap=False):
    """Прогон тела той же склейки, какой его строят деки."""
    out, first = [], True
    for i in range(blocks):
        sz = 12.0 if (cap and i == blocks - 1) else 15.0
        if not first:
            out.append({"text": "", "size": sz, "newpara": True,
                        "space_before": 7})
        first = False
        out.append({"text": BRICK * per, "size": sz, "italic": sz == 12.0})
    return out


def probe_floor_body(ok, bad, say):
    """Подпись внутри ужатого тела названа, а в непритёртом — нет."""
    out = {}
    for name, blocks, h in (("тесно", 7, 2.10), ("просторно", 2, 6.00)):
        runs = _runs(blocks, 3, cap=True)
        report.reset()
        metrics.fit_runs(runs, 12.15, h, tag="проба")
        lo = floor.check_runs(runs, "проба")
        out[name] = (lo, [w for w in report.WARNINGS if w.startswith("[пол]")])
    report.reset()
    if not out["тесно"][1] or out["просторно"][1]:
        bad.append(f"[пол] тесно {out['тесно']}, просторно {out['просторно']}"
                   " — проба ловит не пол")
    else:
        ok.append("[пол]")
        say(f"{'[пол]':<24} на ужатом теле: ЛОВИТ  →  подпись села "
            f"{out['тесно'][0]:.1f} пт и названа; тому же телу с запасом — "
            f"{out['просторно'][0]:.1f} пт и молчание")


def probe_floor_not_proj(ok, bad, say):
    """Вход, который старая проверка пропускала ПО ПОСТРОЕНИЮ.

    `metrics.check_proj` меряет номинал деки (15 пт), умноженный на масштаб.
    При масштабе 0,80 это ровно 12,0 — порог не нарушен, проверка молчит. А
    подпись, у которой основа 12 пт, на том же масштабе садится на 9,5.
    Проба доказывает ОБЕ половины сразу: `[проекция]` молчит, `[пол]`
    говорит. Без первой половины она не отличала бы новую проверку от
    старой."""
    runs = _runs(4, 3, cap=True)
    report.reset()
    metrics.apply_scale(runs, [r["size"] for r in runs], 0.80,
                        metrics.GRID_PT)
    metrics.check_proj(0.80, "проба", 15.0)
    proj = [w for w in report.WARNINGS if w.startswith("[проекция]")]
    lo = floor.check_runs(runs, "проба")
    pol = [w for w in report.WARNINGS if w.startswith("[пол]")]
    report.reset()
    if proj or not pol or lo > 12.0:
        bad.append(f"[пол-мимо-проекции] проекция {len(proj)}, пол "
                   f"{len(pol)}, самый мелкий кегль {lo} — проба не о том")
    else:
        ok.append("[пол-мимо-проекции]")
        say(f"{'[пол-мимо-проекции]':<24} разностно: ЛОВИТ  →  при масштабе "
            f"0,80 номинал тела ровно 12,0 и `[проекция]` молчит, а подпись "
            f"села {lo:.1f} пт и названа `[пол]`")


def probe_floor_class(ok, bad, say):
    """Пол видит НЕ ТОЛЬКО тело: та же оговорка плашки, набранная 10,5 пт,
    названа, а набранная 12 — нет. Половина, без которой «пол на все классы»
    осталось бы заявлением."""
    out = {}
    for name, pt in (("10,5 пт", 10.5), ("12 пт", 12.0)):
        report.reset()
        floor.pt(pt, "проба/плашка1", "оговорка плашки")
        out[name] = [w for w in report.WARNINGS if w.startswith("[пол]")]
    report.reset()
    if not out["10,5 пт"] or out["12 пт"]:
        bad.append(f"[пол-класс] 10,5 пт → {len(out['10,5 пт'])}, 12 пт → "
                   f"{len(out['12 пт'])} — пол не разбирает класс")
    else:
        ok.append("[пол-класс]")
        say(f"{'[пол-класс]':<24} на классе плашки: ЛОВИТ  →  оговорка в "
            "10,5 пт названа, та же в 12 пт — молчание. Набор `DEFAULT` "
            f"держит оговорку {plates.DEFAULT.note_pt:.0f} пт, набор "
            f"Лекции 6 — {plates.LEC06.note_pt:.1f} пт, и это РАЗНЫЕ наборы")


def probe_floor_table(ok, bad, say):
    """Клетка таблицы — класс, который проходил мимо пола ЦЕЛИКОМ.

    Прожарка 2026-10-14 §3.9: `tables.py` не звал `floor.pt` ни разу, у
    таблицы свой предел подбора `TBL_FLOOR` = 8 пт, и сборка сообщила ОДИН
    кадр ниже пола там, где по собранному PDF их ШЕСТЬ. Пять потерянных —
    клетки матриц на 11,5 пт и таблица `s102`, где 70% знаков кадра.

    Разностно, и вторая половина — не «та же таблица крупнее», а ТЕЛО:
    пол на классе «тело» при 15 пт молчит на том же прогоне. Именно этим
    прежняя самопроверка и обманывалась — она доказывала `[пол]` на классе,
    у которого дыры нет, и проходила. Без половины про тело эта проба
    повторила бы ту же ошибку с другой стороны."""
    table = [["Режим", "Что делает"],
             ["отбор", "классификация изображений"]]
    out = {}
    for name, sz in (("11,5 пт", 11.5), ("12,5 пт", 12.5)):
        report.reset()
        tables.reset_caches()
        s = prims.blank(prims.new_deck())
        tables.draw_table(s, 0.5, 0.5, table, sz, 6.0, "проба/таблица")
        out[name] = [w for w in report.WARNINGS
                     if w.startswith("[пол]") and "клетка таблицы" in w]
    report.reset()
    body = floor.check_runs([{"text": "тело кадра", "size": 15.0}], "проба")
    body_said = [w for w in report.WARNINGS if w.startswith("[пол]")]
    report.reset()
    if not out["11,5 пт"] or out["12,5 пт"] or body_said:
        bad.append(f"[пол-таблица] 11,5 пт → {len(out['11,5 пт'])}, 12,5 пт "
                   f"→ {len(out['12,5 пт'])}, тело 15 пт → "
                   f"{len(body_said)} — пол не видит клетку либо шумит")
    else:
        ok.append("[пол-таблица]")
        say(f"{'[пол-таблица]':<24} разностно: ЛОВИТ  →  клетка на 11,5 пт "
            f"названа, та же на 12,5 пт — молчание; а ТЕЛО на {body:.1f} пт "
            "молчит на том же прогоне, то есть прежняя самопроверка "
            "проходила, доказывая пол на классе без дыры. Предел подбора "
            f"таблицы {tables.TBL_FLOOR:.0f} пт ниже пола видимого слоя "
            f"{floor.VIS_PT:.0f} пт — и поднимать его нельзя, иначе рвётся "
            "слово в столбце")


def probe_title_ladder(ok, bad, say):
    """Ступень выбрана по «ставится в одну строку», а не по «влезает»."""
    t = probes_floor.TITLE_WRAPS_AT_TOP
    w, h = 12.23, 0.92
    report.reset()
    old = metrics.fit_size(t, w, h, hi=27.0, lo=19.0, floor=15.0, bold=True,
                           ls=1.08, tag="проба")
    new, lines = titles.fit_title(t, w, h, tag="проба")
    said = [x for x in report.WARNINGS if x.startswith("[заголовок]")]
    report.reset()
    n_old = metrics.n_lines(t, old, w, True)
    if n_old < 2 or lines != 1 or said or new not in titles.LADDER:
        bad.append(f"[лестница-заголовка] старым правилом {old} пт / {n_old} "
                   f"строк, лестницей {new} пт / {lines} — проба не о том")
    else:
        ok.append("[лестница-заголовка]")
        say(f"{'[лестница-заголовка]':<24} разностно: ЛОВИТ  →  тот же "
            f"заголовок старым правилом {old:.1f} пт в {n_old} строки, "
            f"лестницей {new:.1f} пт в одну")


def probe_title_too_long(ok, bad, say):
    """Заголовок, не влезающий в строку ни на одной ступени, НАЗВАН."""
    w, h = 12.23, 0.92
    report.reset()
    titles.fit_title(probes_floor.TITLE_TOO_LONG, w, h, tag="проба-длинный")
    long_said = [x for x in report.WARNINGS if x.startswith("[заголовок]")]
    report.reset()
    titles.fit_title(probes_floor.TITLE_WRAPS_AT_TOP, w, h, tag="проба")
    short_said = [x for x in report.WARNINGS if x.startswith("[заголовок]")]
    report.reset()
    if not long_said or short_said:
        bad.append(f"[заголовок-длинный] длинный {len(long_said)}, обычный "
                   f"{len(short_said)} — проба ловит не длину")
    else:
        ok.append("[заголовок-длинный]")
        say(f"{'[заголовок-длинный]':<24} на сломанном входе: ЛОВИТ  →  "
            f"{long_said[0][:72]}")


def probe_headline(ok, bad, say, run, tmp, seq):
    """Число встаёт крупнее фразы — и число без фразы отвергнуто."""
    w = run([("s82-head.md", probes_floor.head_frame(
        "s82", "Пример 2, цена: чувствительность просела",
        num="82,9 % → 81,5 %")),
        ("s83-bad.md", probes_floor.HEADLINE_NO_TITLE)], tmp, seq)
    said = [x for x in w if x.startswith("[заголовок]") and "s83" in x]
    sizes = _probe_sizes(tmp)
    report.reset()
    if not said or not sizes or sizes[0] <= sizes[1]:
        bad.append(f"[число-заголовок] кегли {sizes}, отказ без фразы "
                   f"{len(said)} — проба не доказывает перестановку")
    else:
        ok.append("[число-заголовок]")
        say(f"{'[число-заголовок]':<24} на собранном кадре: ЛОВИТ  →  число "
            f"{sizes[0]:.0f} пт стоит над фразой {sizes[1]:.0f} пт "
            "(прежде фраза была самым крупным текстом кадра); число без "
            "фразы отвергнуто")


def _probe_sizes(tmp):
    """Два самых крупных кегля первого кадра собранной пробы."""
    from pptx import Presentation
    p = Presentation(str(tmp / "probe.pptx"))
    out = []
    for sh in p.slides[0].shapes:
        if not sh.has_text_frame:
            continue
        for para in sh.text_frame.paragraphs:
            for r in para.runs:
                if r.text.strip() and r.font.size:
                    out.append(r.font.size.pt)
    return sorted(set(out), reverse=True)[:2]


def probe_two_columns(ok, bad, say):
    """Две колонки взяты там, где кегль не падает, и отвергнуты там, где
    упал бы; отказ возвращает кегли нетронутыми."""
    res = {}
    for name, (blocks, per, w, h) in (
            ("берутся", (4, 2, 12.15, 5.20)),
            ("отвергнуты", (6, 3, 12.15, 1.30))):
        runs = _runs(blocks, per)
        report.reset()
        cw = (w - 0.40) / 2
        two = twocol.fit_two(runs, cw, h, w, h, tag="проба")
        plain = metrics.scan_scale(runs, w, h)
        res[name] = (two[0] if two else None, plain,
                     [r["size"] for r in runs])
    report.reset()
    took, plain_took, _ = res["берутся"]
    ref, plain_ref, sizes_ref = res["отвергнуты"]
    if took is None or ref is not None or sizes_ref != [15.0] * len(sizes_ref):
        bad.append(f"[две-колонки] {res} — проба не доказывает ни выбора, "
                   "ни возврата кеглей")
    else:
        ok.append("[две-колонки]")
        say(f"{'[две-колонки]':<24} разностно: ЛОВИТ  →  в высокой рамке "
            f"взяты масштабом {took:.2f} (одной колонкой было бы "
            f"{plain_took:.2f}); в низкой отвергнуты — одной колонкой там "
            f"{plain_ref}, и кегли вернулись 15,0 пт, а не дном лестницы")


def probe_floor_knob(ok, bad, say):
    """Порог пола, поднятый декой, ДЕЙСТВУЕТ — и проба ловит, когда он
    застыл при импорте.

    Сломанный вход здесь — САМА прежняя подпись: `def f(..., floor=VIS_PT)`
    брала порог один раз, при импорте, и `floor.VIS_PT = 9` потом не делал
    РОВНО НИЧЕГО — ни эффекта, ни отказа, хотя шапка `floor.py` обещает деке
    именно эту ручку. Ниже прежняя подпись воспроизведена замыканием и
    прогнана тем же входом, что нынешняя. Без этой половины проба
    доказывала бы только, что 10,5 меньше 12."""
    def frozen(size, *, thr=floor.VIS_PT):      # прежнее поведение, дословно
        return size < thr - 1e-9

    was = floor.VIS_PT
    out = {}
    try:
        for name, thr in (("порог 9", 9.0), ("порог 12", 12.0)):
            floor.VIS_PT = thr
            report.reset()
            floor.pt(10.5, "проба/плашка1", "оговорка плашки")
            out[name] = ([w for w in report.WARNINGS
                          if w.startswith("[пол]")], frozen(10.5))
    finally:
        floor.VIS_PT = was
        report.reset()
    if out["порог 9"][0] or not out["порог 12"][0] \
            or not out["порог 9"][1]:
        bad.append(f"[пол-ручка] при пороге 9 пт {len(out['порог 9'][0])} "
                   f"предупреждений, при 12 пт {len(out['порог 12'][0])}, "
                   f"застывшая подпись при 9 пт {out['порог 9'][1]} — ручка "
                   "порога не действует либо проба не о ней")
    else:
        ok.append("[пол-ручка]")
        say(f"{'[пол-ручка]':<24} разностно: ЛОВИТ  →  та же оговорка 10,5 "
            "пт при пороге 12 названа, при 9 — молчание; прежняя подпись "
            "`floor=VIS_PT` на том же входе при 9 всё равно считала её "
            "подпольной — порог застывал при импорте")


# (операнд, байт на знак, сколько знаков в нём на самом деле)
GLYPH_CASES = (
    ("<41>", 1, 1),                 # прежнее правило давало 2 // 4 = 0
    ("<414243>", 1, 3),             # прежнее давало 1
    ("(abc)", 1, 3),                # обычная строка — считалась верно
    ("[<41> -20 <4243>]", 1, 3),    # массив TJ с кернингом между знаками
    ("<00410042>", 2, 2),           # те же байты составным шрифтом
)


def probe_glyph_count(ok, bad, say):
    """Знаки считаются по КОДИРОВКЕ файла, а не допущением.

    Разностно: тот же операнд прежним правилом («всегда четыре цифры на
    знак») и нынешним. Без этой половины проба доказывала бы только, что
    `len // 2` считает по два.

    Эта мера — вход ВСЕХ чисел круга про мелкий текст, и до сих пор у неё
    не было ни одной пробы. Прежнее правило теряло односимвольный прогон
    НАЦЕЛО, а таких прогонов у Лекции 7 около половины, у Лекции 6 — три
    четверти: доли двух дек были несравнимы между собой."""
    now = [pdfmeasure._glyphs(a, b) for a, b, _w in GLYPH_CASES]
    want = [w for _a, _b, w in GLYPH_CASES]
    was = [pdfmeasure._glyphs(a, 2) for a, _b, _w in GLYPH_CASES]
    wide = pdfmeasure.glyph_bytes(b"/Font /Subtype /Type0 /Encoding "
                                  b"/Identity-H")
    plain = pdfmeasure.glyph_bytes(b"/Font /Subtype /TrueType")
    if now != want or was[0] != 0 or was == want or (wide, plain) != (2, 1):
        bad.append(f"[знаки-hex] нынешним правилом {now}, нужно {want}, "
                   f"прежним {was}, байт на знак составного/простого "
                   f"{(wide, plain)} — проба не о том")
    else:
        ok.append("[знаки-hex]")
        say(f"{'[знаки-hex]':<24} разностно: ЛОВИТ  →  `<41>` — это 1 знак, "
            f"прежнее правило давало {was[0]}; по пяти операндам нынешнее "
            f"{now} против прежнего {was}; составной шрифт узнаётся "
            f"({wide} байта на знак) против простого ({plain})")


def run_all(ok, bad, say, run, tmp, seq):
    probe_floor_body(ok, bad, say)
    probe_floor_not_proj(ok, bad, say)
    probe_floor_class(ok, bad, say)
    probe_floor_table(ok, bad, say)
    probe_floor_knob(ok, bad, say)
    probe_glyph_count(ok, bad, say)
    probe_title_ladder(ok, bad, say)
    probe_title_too_long(ok, bad, say)
    probe_headline(ok, bad, say, run, tmp, seq)
    probe_two_columns(ok, bad, say)
    report.reset()
