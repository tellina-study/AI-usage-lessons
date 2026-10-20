"""English captions for Seminar 8 diagrams (issue #172/#274, EN track).

Key — the Russian string exactly as it stands in the drawing script; value —
the English string as it goes onto the canvas. Mechanics and the reason the
dictionary is its own file, not a second drawing script, are in
`fig_toolkit.py`'s own docstring. Order follows draw order, figure by figure;
`BY_FIG` below says which string belongs to which figure (used by
`fig_toolkit.report()` to tell "key never reached the canvas" apart from
"key belongs to another drawing script"). Edited by hand.

This file is SHARED by all of sem-08's drawing scripts, the same way
`fig_strings_en.py` is shared across sem-06's — several parallel translators
(cases n05-n54, intro/closing n01-n04+n55-n57) touch it concurrently, each
adding their own figures' section. Covered so far: `make_figures_zillow.py`
(Zillow, n40/n43) and `make_figures_lestnitsa.py` (the arc ladder, n03).
Other drawing scripts (`make_figures_k1.py` .. `make_figures_k4.py`,
`make_figures_c3.py`, `make_figures_n02.py`) add their own entries here when
their own EN slides are produced — append a new `# ── figure.png ──` section,
do not replace an existing one (two agents clobbered each other's sections
once already on 2026-10-20 — merge, don't overwrite).

The real-screenshot figure `n02` (`shov-s7-obzor-klassifikatsii.png`) is
NOT here and never will be: it is an annotated screenshot, not a
`fig_toolkit` programmatic figure, so it does not go through `T()`/
`set_lang()` — its English captions are hardcoded directly in
`make_figures_n02_en.py` (see that file's own docstring).

A miss (Cyrillic with no entry here) is never silent: `fig_toolkit.report()`
prints the list. An unused key is reported too — a typo in the key.
"""

STRINGS = {

    # ── zillow-shema-bez-geyta.png ──────────────────────────────────────────
    "Zillow Offers — как принималось решение без гейта":
        "Zillow Offers — how the decision was made with no gate",
    "Zestimate":
        "Zestimate",
    "алгоритмическая оценка дома":
        "algorithmic home valuation",
    "Решение о покупке":
        "Purchase decision",
    "без обязательного гейта":
        "no mandatory gate",
    "Покупка исполняется":
        "Purchase executes",
    "окна мониторинга нет":
        "no monitoring window",
    "Квартальный отчёт":
        "Quarterly report",
    "здесь и видна ошибка":
        "the error shows up here",
    "Ошибка накапливается незаметно между кварталами, не внутри них.":
        "The error accumulates unnoticed between quarters, not within them.",
    "Списание запасов $304,4 млн за 3 кв. 2021, $407,9 млн по итогам года; сокращение ~25% штата.":
        "Inventory write-down $304.4M for Q3 2021, $407.9M for the full year; workforce cut ~25%.",

    # ── zillow-shema-s-geytom.png ───────────────────────────────────────────
    "Альтернатива с гейтом: человек выше порога риска + circuit breaker":
        "The alternative with a gate: a human above the risk threshold + a circuit breaker",
    "алгоритмическая оценка (вход)":
        "algorithmic valuation (input)",
    "Человек-андеррайтер":
        "Human underwriter",
    "выше порога суммы/риска":
        "above the amount/risk threshold",
    "Покупка":
        "Purchase",
    "исполняется решением человека":
        "executes on a human decision",
    "Circuit breaker":
        "Circuit breaker",
    "проверка отклонения еженедельно":
        "deviation checked weekly",
    "Решение выше порога риска — у человека, не у модели.":
        "The decision above the risk threshold belongs to a human, not to the model.",
    "Окно контроля — неделя, не квартал.":
        "The control window is a week, not a quarter.",

    # ── lestnitsa-dugi.png ───────────────────────────────────────────────────
    'Хватит одного вызова: ответ модели, поиск по своим документам':
        'One call is enough: a model answer, a search over your own documents',
    'Цепочка: шаги в известном порядке, данные между ними':
        'Chain: steps in a known order, data passed between them',
    'Маршрут: путь задаёт категория входа':
        "Route: the input's category picks the path",
    'Параллель: независимые проверки одного входа':
        'Parallel: independent checks on one input',
    'Цикл: повтор по элементам, проверка выхода':
        'Loop: repeat over items, check the exit condition',
    'Подпроцесс: дирижёр и несколько исполнителей':
        'Subprocess: a conductor and several performers',
    'Агент: порядок шагов выбирает сам':
        'Agent: it picks the order of steps itself',
    'Несколько агентов вместе':
        'Several agents together',
    'Выключить: вернуться к ручному процессу':
        'Turn it off: go back to a manual process',
    'до С7':
        'before S7',
    'С7 → С8 · сегодня':
        'S7 → S8 · today',
    'С9':
        'S9',
    'С10':
        'S10',
    'С11':
        'S11',
    'С12':
        'S12',
    'выше — сложнее процесс; каждое занятие закрывает свою ступень':
        'higher — more complex the process; each class closes its own rung',
}

BY_FIG = {
    "zillow-shema-bez-geyta.png": [
        "Zillow Offers — как принималось решение без гейта",
        "Zestimate",
        "алгоритмическая оценка дома",
        "Решение о покупке",
        "без обязательного гейта",
        "Покупка исполняется",
        "окна мониторинга нет",
        "Квартальный отчёт",
        "здесь и видна ошибка",
        "Ошибка накапливается незаметно между кварталами, не внутри них.",
        "Списание запасов $304,4 млн за 3 кв. 2021, $407,9 млн по итогам года; сокращение ~25% штата.",
    ],
    "zillow-shema-s-geytom.png": [
        "Альтернатива с гейтом: человек выше порога риска + circuit breaker",
        "Zestimate",
        "алгоритмическая оценка (вход)",
        "Человек-андеррайтер",
        "выше порога суммы/риска",
        "Покупка",
        "исполняется решением человека",
        "Circuit breaker",
        "проверка отклонения еженедельно",
        "Решение выше порога риска — у человека, не у модели.",
        "Окно контроля — неделя, не квартал.",
    ],
    'lestnitsa-dugi.png': [
        'Хватит одного вызова: ответ модели, поиск по своим документам',
        'Цепочка: шаги в известном порядке, данные между ними',
        'Маршрут: путь задаёт категория входа',
        'Параллель: независимые проверки одного входа',
        'Цикл: повтор по элементам, проверка выхода',
        'Подпроцесс: дирижёр и несколько исполнителей',
        'Агент: порядок шагов выбирает сам',
        'Несколько агентов вместе',
        'Выключить: вернуться к ручному процессу',
        'до С7',
        'С7 → С8 · сегодня',
        'С9',
        'С10',
        'С11',
        'С12',
        'выше — сложнее процесс; каждое занятие закрывает свою ступень',
    ],
}
