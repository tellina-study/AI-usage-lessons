# -*- coding: utf-8 -*-
"""`deckkit` — общее ядро сборщиков дек курса. Issue #229.

Объединение двух зрелых сборщиков поколения 2: `build_lec07.py` (Лекция 7) и
`build_v4.py` с его импортами (Лекция 6). Что откуда взято, где они
расходились и что из этого следует — `README.md` рядом.

Ядро НЕ знает раскладки кадра: раскладка — дело деки, образец — `refdeck.py`.

Порядок слоёв, снизу вверх (выше по списку — ни от чего из нижележащего не
зависит):

    theme · report → metrics → prims → markup · slidefile
                             → tables · plates · scheme · columns · flow
                             → media → refdeck
                             → probes → selftest · regress → regress_decks

Два прогона, которыми ядро сдаётся:

    python3 -m deckkit.selftest           — 35 проб на сломанном входе
    python3 -m deckkit.regress_decks --all — регрессия на двух доставленных деках
"""
__all__ = ["theme", "report", "metrics", "prims", "markup", "slidefile",
           "tables", "plates", "scheme", "columns", "flow", "media",
           "refdeck", "probes", "selftest", "regress", "regress_decks"]
