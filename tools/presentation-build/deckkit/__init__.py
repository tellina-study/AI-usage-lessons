# -*- coding: utf-8 -*-
"""`deckkit` — общее ядро сборщиков дек курса. Issue #229.

Объединение двух зрелых сборщиков поколения 2: `build_lec07.py` (Лекция 7) и
`build_v4.py` с его импортами (Лекция 6). Что откуда взято, где они
расходились и что из этого следует — `README.md` рядом.

Ядро НЕ знает раскладки кадра: раскладка — дело деки, образец — `refdeck.py`.

Порядок слоёв, снизу вверх (выше по списку — ни от чего из нижележащего не
зависит):

    theme · report → metrics → prims → markup · slidefile
                             → tables · plates · scheme · columns
                             → figure · flow
                             → wrap → media · contrast → refdeck · render
                             → probes → selftest · regress → regress_decks

Два прогона, которыми ядро сдаётся:

    python3 -m deckkit.selftest           — пробы на сломанном входе
    python3 -m deckkit.contrast --selftest — пробы пола контраста и hero
    python3 -m deckkit.contrast <файл>    — таблица контраста по собранной деке
    python3 -m deckkit.regress_decks --all — регрессия на двух доставленных деках
"""
__all__ = ["theme", "report", "metrics", "prims", "markup", "slidefile",
           "tables", "plates", "scheme", "columns", "figure", "flow",
           "wrap", "media",
           "refdeck", "render", "probes", "probes_layout", "probes_contrast",
           "contrast", "selftest", "selftest_layout", "selftest_contrast",
           "regress", "regress_decks"]
