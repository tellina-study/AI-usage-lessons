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
from . import (floor, metrics, plates, probes_floor, report, titles, twocol)
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


def run_all(ok, bad, say, run, tmp, seq):
    probe_floor_body(ok, bad, say)
    probe_floor_not_proj(ok, bad, say)
    probe_floor_class(ok, bad, say)
    probe_title_ladder(ok, bad, say)
    probe_title_too_long(ok, bad, say)
    probe_headline(ok, bad, say, run, tmp, seq)
    probe_two_columns(ok, bad, say)
    report.reset()
