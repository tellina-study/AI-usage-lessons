# -*- coding: utf-8 -*-
"""Fixed labels the case-deck renderers write onto slides themselves.

These are NOT spec content: they are the renderer's own chrome (section labels,
the closing slide's heading, the map subtitle), so translating a spec alone left
them Russian on an English deck. Both build_cases_deck.py and render_png.py read
them from here so the two renderers cannot drift apart.

`set_lang()` is called once per seminar by the renderer, from the spec's `lang`.
"""

_LANG = "ru"

CHROME = {
    "map_title":        {"ru": "Карта занятия",   "en": "Session map"},
    "map_sub":          {"ru": "Каждый кейс: контекст → решение и схема → усложнение из практики → разбор с примером",
                         "en": "Every case: context → solution and schema → a complication from practice → breakdown with an example"},
    "concept_how":      {"ru": "Как работает",    "en": "How it works"},
    "resolution_bar":   {"ru": "Разбор · как реализовать",
                         "en": "Breakdown · how to build it"},
    "resolution_how":   {"ru": "Как реализовать", "en": "How to build it"},
    "structured_schema":{"ru": "Задаём схему ответа", "en": "We set the response schema"},
    "structured_get":   {"ru": "Что получаем",    "en": "What we get"},
    "structured_limit": {"ru": "Где упираемся",   "en": "Where it stops short"},
    "breakdown_bar":    {"ru": "Разбор · компоненты и комментарии",
                         "en": "Breakdown · components and commentary"},
    "breakdown_comp":   {"ru": "Ключевые компоненты", "en": "Key components"},
    "breakdown_comm":   {"ru": "Ключевые комментарии по теме",
                         "en": "Key commentary on the topic"},
    "closing_title":    {"ru": "Что унести",      "en": "What to take away"},
}


def set_lang(lang):
    global _LANG
    if lang not in ("ru", "en"):
        raise ValueError(f"no chrome for language {lang!r}")
    _LANG = lang


def T(key):
    return CHROME[key][_LANG]
