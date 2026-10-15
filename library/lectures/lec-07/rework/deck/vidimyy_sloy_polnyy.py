#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ПОЛНЫЙ видимый слой кадра — все поля, которые доезжают до экрана.

Зачем отдельно от `scan_deck_visible.visible_lines`. Тот извлекает `title`,
плашки, схему (подпись · ряд · шаг), столбцы и тело — и этого НЕ ХВАТАЕТ.
Куплено ошибкой в этом производстве (#229): проход по словарю на кадре `s64`
дал ноль, а крупное число кадра стояло в поле `headline_number` голым, без
единицы, — поле видимое, читателем не прочитанное. Тем же классом ошибки
мимо прохода уехала подпись единицы `scheme.unit` на `s05` и `s45`
(«верных ответов из ста» вместо балла по рубрике).

Перечень полей собран не на глаз, а пересчётом ВСЕХ ключей фронтматтера
всех 101 кадра деки: `headline_number` стоит на одном кадре, `figure` на
одном, `media_caption` на трёх, `scheme.unit`/`scheme.base`/`scheme.marks`
на пяти. Редкое поле и есть то, которое проход пропускает.

Не видимы (проверено по сборщику): `assertion`, `media_note`,
`media_needed`, `method_steps`, `form`, `vizforma`, `pol_slov`, `vfy`,
`status`, `timing_min`, `in_bucket`, `razbor_part`. Поле `source` печатается
в подвале ссылкой — считается видимым и помечается отдельно, чтобы имена
изданий не шли в счёт латиницы.

    python3 vidimyy_sloy_polnyy.py s05 s45     # показать слой кадров
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent


# Поля фронтматтера, которые этот извлекатель НЕ смотрит, и почему. Список
# печатается рядом с нулём намеренно: ноль без него — это и есть та ошибка,
# которую файл лечит (`notes/mcp-limitations.md` [#229-15]). Проверка, которая
# молчит, не отличима от проверки, которой нечего сказать.
NE_SMOTRIM = {
    "assertion": "служебное, на экран не выводится (deckkit/slidefile.py)",
    "media_note": "рабочая записка о добыче снимка",
    "media_needed": "наряд на добычу снимка",
    "media": "путь к файлу, а не текст",
    "method_steps": "разметка формы разбора для планов",
    "form": "разметка формы для планов",
    "vizforma": "имя первоосновы кадра для разнарядки",
    "pol_slov": "объявленный пол и его причина",
    "vfy": "флаг сверки",
    "status": "состояние производства",
    "timing_min": "хронометраж, metadata для оркестрации",
    "in_bucket": "доля провалов и ограничений",
    "razbor_part": "номер части разбора",
    "id": "идентификатор", "local_id": "идентификатор",
    "section": "имя раздела для отбора", "type": "тип кадра",
}
# `source` смотрится только по просьбе (`s_podvalom=True`): он печатается в
# подвале ссылкой, то есть видим, но имена изданий и авторов латиницей в нём
# законны — в счёт латиницы и словаря он не идёт.


def chego_ne_videli(path):
    """Какие НЕсмотренные поля на этом кадре реально заполнены.

    Зовётся вместе с печатью нуля: «срабатываний 0» честно лишь тогда,
    когда рядом сказано, где прогон не искал."""
    raw = Path(path).read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", raw, re.S)
    if not m:
        return []
    d = yaml.safe_load(m.group(1)) or {}
    return [(k, NE_SMOTRIM[k]) for k in d
            if k in NE_SMOTRIM and d[k] not in (None, "", [], {}, False)]


def polnyy(path, s_podvalom=False):
    """Список (где, текст). `где` годится как адрес в отчёте."""
    raw = Path(path).read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.S)
    if not m:
        return []
    d = yaml.safe_load(m.group(1)) or {}
    out = []

    def add(gde, v):
        if v not in (None, "", [], {}):
            out.append((gde, str(v)))

    add("title", d.get("title"))
    add("крупное число", d.get("headline_number"))
    add("подпись снимка", d.get("media_caption"))
    for i, it in enumerate(d.get("blocks") or []):
        if isinstance(it, dict):
            for k in ("label", "value", "note"):
                add(f"плашка[{i}]/{k}", it.get(k))
    fig = d.get("figure")
    if isinstance(fig, dict):
        for k in ("value", "unit", "base"):
            add(f"число кадра/{k}", fig.get(k))
    sch = d.get("scheme")
    if isinstance(sch, dict):
        for k in ("caption", "unit", "base", "axis"):
            add(f"схема/{k}", sch.get(k))
        for mk in sch.get("marks") or []:
            add("схема/метка", mk if not isinstance(mk, dict)
                else " · ".join(str(x) for x in mk.values()))
        for r in sch.get("rows") or []:
            if isinstance(r, dict):
                add("схема/ряд", r.get("label"))
                for st in r.get("steps") or []:
                    add("схема/шаг", st)
    cols = d.get("columns")
    if isinstance(cols, dict):
        for side in ("left", "right"):
            c = cols.get(side)
            if isinstance(c, dict):
                add(f"столбец/{side}/шапка", c.get("head"))
                for it in c.get("items") or []:
                    add(f"столбец/{side}/строка", it)
    body = re.search(r"##\s*Видимый текст слайда\s*\n(.*?)(?=\n##\s|\Z)",
                     m.group(2), re.S)
    for ln in (body.group(1) if body else "").split("\n"):
        if ln.strip():
            add("тело", ln.strip())
    if s_podvalom:
        add("подвал/источник", d.get("source"))
    return out


def kadry_polosy(sections):
    """Кадры деки, чей `section` начинается с одного из префиксов."""
    out = []
    for f in sorted((HERE / "slides").glob("s*.md")):
        m = re.match(r"^---\n(.*?)\n---", f.read_text(encoding="utf-8"), re.S)
        if not m:
            continue
        sec = str((yaml.safe_load(m.group(1)) or {}).get("section") or "")
        if sec.startswith(tuple(sections)):
            out.append(f)
    return out


if __name__ == "__main__":
    ids = sys.argv[1:]
    for f in sorted((HERE / "slides").glob("s*.md")):
        sid = f.stem.split("-")[0]
        if ids and sid not in ids:
            continue
        print(f"===== {sid} =====")
        vid = polnyy(f)
        for gde, txt in vid:
            print(f"  [{gde}] {txt[:160]}")
        if not vid:
            print("  видимых полей не нашлось — и вот где не искали:")
        for k, why in chego_ne_videli(f):
            print(f"  (не смотрим) {k}: {why}")
