#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА деки Лекции 7 — на РАСКЛАДКЕ ЭТОЙ деки. Issue #229.

Зовётся из `build_lec07.py --selftest`; отдельным файлом потому, что оба
не влезают в предел 600 строк (`CLAUDE.md`), а не потому, что это
необязательная часть сдачи.

Ядро сдаётся своей самопроверкой отдельно (`python3 -m deckkit.selftest`,
35 проб). Здесь доказывается другое: что те же сломанные входы ловятся,
когда их собирает обложка, дивайдер и содержательный кадр ЭТОЙ лекции, а
не образцовая раскладка пакета, — плюс три проверки, которых у ядра нет и
быть не может, потому что они про эту деку: подбор ширины боковой
иллюстрации, два обязательных hero против порога §5.9 и живая гиперссылка.
"""
import tempfile
from pathlib import Path

from PIL import Image

from build_lec07 import (LEC_ROOT, SLIDES_DIR, build, content,
                         fit_media, verify_links)
from deckkit import media, prims, probes, report, slidefile

# ════════════════════════════════════════════════════════════════════
# сломанные входы
# ════════════════════════════════════════════════════════════════════
# Сломанные входы берутся из `deckkit.probes` — те же файлы кадров, что
# проверяют ядро, но прогнанные через раскладку ЭТОЙ деки: обложку, дивайдер
# и содержательный кадр отсюда, а не образцовую раскладку пакета. Дублировать
# фикстуры было бы хуже вдвойне — и лишние триста строк, и два перечня,
# которые расходятся.
#
# Табличный путь пропущен: таблиц в этой деке ноль (`deckkit.tables`
# доступен, но ни один кадр его пока не зовёт), и прогонять через неё пробы
# на столбец и матрицу значило бы отчитываться о проверке, которой здесь
# нечего проверять.
SKIP = {"[столбец]", "[матрица] нет", "[матрица] очищено",
        # Три предупреждения Лекции 6 у этой деки выключены осознанно
        # (`build_lec07.PLATES`, там же замер: 35 срабатываний, из них 30 по
        # чужому порогу). Проба на выключенное предупреждение — не провал
        # проверки, а проба не о том; ядро доказывает все три у себя.
        "[плашки] подпись", "[плашки] значению", "[плашки] оговорка"}


def _assets(d):
    """Снимки под пробы §5.9: портрет (даёт четверть площади) и широкий.
    Имена — те, на которые ссылаются фикстуры ядра."""
    Image.new("RGB", (670, 1000), (200, 210, 220)).save(d / "probe-portrait.png")
    Image.new("RGB", (1500, 1000), (210, 215, 225)).save(d / "probe-wide.png")


def selftest():
    """Прогон каждой проверки на нарочно сломанном входе.

    Проверка, показавшая ноль, ничего не значит, пока не доказано, что она
    умеет находить. Поэтому два прогона на каждое предупреждение: чистый
    кадр (обязан молчать) и сломанный (обязан сработать)."""
    tmp = Path(tempfile.mkdtemp(prefix="lec07-selftest-"))
    ok, bad, seq = [], [], [0]

    def run(files, name="probe"):
        report.reset()
        seq[0] += 1
        d = tmp / f"d{seq[0]}"
        d.mkdir()
        _assets(d)
        for nm, txt in files:
            (d / nm).write_text(txt, encoding="utf-8")
        build(out=tmp / f"{name}.pptx", slides_dir=d, root=d)
        return list(report.WARNINGS)

    base = run([("s01-clean.md", probes.CLEAN)], name="clean")
    print("── САМОПРОВЕРКА ДЕКИ (раскладка Лекции 7) ───────────────────")
    print(f"чистый кадр: предупреждений {len(base)}"
          + (" — " + "; ".join(base) if base else " (молчит, как и должен)"))
    (bad if base else ok).append("[чистый кадр]")

    for key, (sid, txt) in probes.BROKEN.items():
        if key in SKIP:
            continue
        tag, _, need = key.partition(" ")
        w = run([(f"{sid}-broken.md", txt)])
        hit = [x for x in w if x.startswith(tag) and (not need or need in x)]
        print(f"{key:<24} на сломанном входе: "
              + ("ЛОВИТ" if hit else "НЕ ЛОВИТ")
              + (f"  →  {hit[0][:84]}" if hit else ""))
        if key in probes.LABELS:
            print(f"{'':24} доказывает: {probes.LABELS[key]}")
        (ok if hit else bad).append(key)

    w = run([("s01-a.md", probes.CLEAN), ("s01-b.md", probes.CLEAN)])
    hit = [x for x in w if x.startswith("[файлы]")]
    print(f"{'[файлы]':<24} на сломанном входе: "
          + ("ЛОВИТ" if hit else "НЕ ЛОВИТ"))
    (ok if hit else bad).append("[файлы]")

    print("── пробы, которые ставятся только ЭТОЙ декой ────────────────")
    ok.extend(probe_fit_media(bad))
    ok.extend(probe_heroes(bad))
    ok.extend(probe_live_links(tmp, bad))
    print("─────────────────────────────────────────────────────────────")
    print(f"проверок доказано: {len(ok)} из {len(ok) + len(bad)}")
    print("ядро сдаётся своей самопроверкой отдельно: "
          "python3 -m deckkit.selftest")
    if bad:
        print("НЕ ДОКАЗАНО: " + ", ".join(bad))
        return 1
    print("все проверки доказаны на сломанном входе")
    return 0


def probe_fit_media(bad):
    """`fit_media` РАЗНОСТНО: мало знать, что ширина подобралась, — надо
    знать, что при назначенной 4,30" кадр ломается, а при подобранной нет.
    Берётся настоящий `s18`, на котором подбор и понадобился: выдуманная
    проба здесь доказывала бы выдуманный кадр."""
    f = [x for x in SLIDES_DIR.glob("s18-*.md")]
    if not f:
        bad.append("[подбор кадра] файла s18 нет — проба не поставлена")
        return []
    # Поиск начинается с НАРОЧНО слишком широкого слота, а не с рабочих
    # 4,30": доказывается механизм, а не нынешний исход. Проба, написанная
    # на исход, завтра соврёт в обе стороны — и когда подбор сломается, и
    # когда кадр просто перестанет в нём нуждаться.
    W0 = 6.00
    keep = report.snapshot()
    report.reset()
    sl = slidefile.read_slide(f[0])
    fit_media(sl, LEC_ROOT, w0=W0)
    chosen = sl.media_w
    report.WARNINGS[:] = []
    sl.media_w = W0
    content(prims.new_deck(), sl, LEC_ROOT)
    at_full = list(report.blocking())
    report.WARNINGS[:] = []
    sl.media_w = chosen
    content(prims.new_deck(), sl, LEC_ROOT)
    at_fit = list(report.blocking())
    report.restore(keep)
    if chosen >= W0 or not at_full or at_fit:
        bad.append(f"[подбор кадра] s18: подобрано {chosen:.2f}\", "
                   f"блокирующих при {W0:.2f}\" {len(at_full)}, при "
                   f"подобранной {len(at_fit)} — проба больше не доказывает "
                   "подбор")
        return []
    print(f"{'[подбор кадра]':<24} разностно: ЛОВИТ  →  s18 при {W0:.2f}\" "
          f"даёт {len(at_full)} блокирующих, при подобранной {chosen:.2f}\" "
          "— ноль")
    return ["[подбор кадра]"]


def probe_heroes(bad):
    """Два обязательных hero этой деки — против порога §5.9. Проба на
    настоящих кадрах, а не на выдуманных: порог здесь взят впритык (окно
    ширины — три сотых дюйма), и любая правка текста s105 его сдвинет."""
    keep = report.snapshot()
    report.reset()
    build(only="s01,s105", out=Path(tempfile.mkdtemp()) / "hero.pptx")
    areas = dict(report.HERO_AREA)
    report.restore(keep)
    low = {k: v for k, v in areas.items() if v < media.HERO_MIN_AREA}
    if len(areas) != 2 or low:
        bad.append(f"[hero §5.9] обязательных hero {len(areas)}, под порогом "
                   f"{low or 'ни одного'} — ожидались s01 и s105 выше 40%")
        return []
    print(f"{'[hero §5.9]':<24} на настоящих кадрах: ЛОВИТ  →  "
          + " · ".join(f"{k} {100 * v:.1f}%" for k, v in sorted(areas.items())))
    return ["[hero §5.9]"]


def probe_live_links(tmp, bad):
    """Гиперссылка лежит в пакете как `r:id`, а не как синий текст. У самой
    деки ссылок ноль, и это единственное доказательство, что путь подвала и
    заметок вообще работает."""
    n, targets = verify_links(tmp / "clean.pptx")
    if n < 2 or targets < 2:
        bad.append("[ссылка-живая] в XML чистого кадра не нашлось двух "
                   f"отношений гиперссылки (подвал+заметки): {n}/{targets}")
        return []
    print(f"{'[ссылка-живая]':<24} на чистом кадре: ЛОВИТ  →  подвал и "
          "заметки дали настоящие `r:id` в пакете")
    return ["[ссылка-живая]"]
