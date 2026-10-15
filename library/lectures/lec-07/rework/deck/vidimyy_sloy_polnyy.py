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


# ПРИ КАКОМ УСЛОВИИ поле доезжает до экрана. Заведено потому, что «поле есть»
# НЕ равно «зал это видит», и на этом ошиблись сразу две сессии в один день
# (`notes/mcp-limitations.md` [#229-16]): обе проверяли СМЫСЛ строки
# `media_caption` и ни одна — рисуется ли она вообще. Рисуется она только при
# `media_hero`, и уходит не под картинку, а последним сегментом строки
# источника в подвал.
USLOVIE = {
    "title": ("всегда, кроме дивайдера и обложки — там видно `# Имя` из тела",
              "deckkit/slidefile.py"),
    "headline_number": ("всегда, если поле задано", "deckkit/titles.py"),
    "blocks": ("всегда, если список непуст", "deckkit/plates.py"),
    "scheme": ("всегда, если задана", "deckkit/scheme.py"),
    "columns": ("всегда, если заданы", "deckkit/columns.py"),
    "figure": ("всегда, если задана", "deckkit/figure.py"),
    "source": ("в подвале, ссылкой; «—» не печатается",
               "build_lec07.py:272"),
    "media_caption": ("ТОЛЬКО при `media_hero: true`, и не под картинкой, а "
                      "последним сегментом строки источника в подвале",
                      "build_lec07.py:275 и :327, deckkit/media.py:309"),
}


def usloviya(path):
    """Поля этого кадра и условие рисования каждого — заполнено ли, нарисуется.

    Отвечает на вопрос, которого не задала ни одна проверка до [#229-16]:
    строка в файле есть — увидит ли её зал."""
    raw = Path(path).read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", raw, re.S)
    d = (yaml.safe_load(m.group(1)) or {}) if m else {}
    out = []
    for k, (cond, adres) in USLOVIE.items():
        if d.get(k) in (None, "", [], {}):
            continue
        risuet = "да"
        if k == "media_caption" and not d.get("media_hero"):
            risuet = "НЕТ — `media_hero` не задан, строка в файл есть, зал её не видит"
        out.append((k, risuet, cond, adres))
    return out


def polya_sborshchika():
    """Поля фронтматтера, которые РЕАЛЬНО читает код сборки — выведено из кода.

    Решение О17: перечень видимого слоя обязан собираться из того, что рисует
    сборщик, а не поддерживаться руками. Иначе каждая новая первооснова в ядре
    открывает новую слепую зону — так и вышло четыре раза за два дня
    (`headline_number`, `scheme.unit`, `figure`, `media_caption`).

    Этот прогон — СТОРОЖ списка выше, не замена ему: он ищет обращения вида
    `meta.get("имя")` / `["имя"]` по сборщику деки и по всему ядру отрисовки и
    говорит, не появилось ли поля, которого `polnyy` не смотрит. Чего он НЕ
    умеет: поле, которое ядро читает вычисленным именем, он не увидит — и
    поэтому печатает это ограничение вместе с ответом."""
    pat = re.compile(r'(?:meta|sl|d|s|spec|it|row|c)\.get\(\s*["\']([a-z_]+)["\']'
                     r'|\[["\']([a-z_]+)["\']\]')
    kern = next((d / "tools" / "presentation-build" / "deckkit")
                for d in HERE.parents
                if (d / "tools" / "presentation-build" / "deckkit").exists())
    src = [HERE / "build_lec07.py", *sorted(kern.glob("*.py"))]
    vidit = set()
    for f in src:
        try:
            txt = f.read_text(encoding="utf-8")
        except OSError:
            continue
        for m in pat.finditer(txt):
            vidit.add(m.group(1) or m.group(2))
    # Что `polnyy` реально извлекает, и что намеренно пропущено с причиной.
    smotrim = {"title", "headline_number", "media_caption", "blocks",
               "scheme", "columns", "figure", "source"}
    # Поля, которые сборщик читает, но текста залу они не дают.
    ne_tekst = {"id": "идентификатор, не текст",
                "type": "тип кадра, выбирает раскладку",
                "media": "путь к файлу снимка, не текст",
                "media_hero": "флаг «снимок во весь кадр»"}
    chitaet = vidit & (smotrim | set(NE_SMOTRIM) | set(ne_tekst))
    # Слепая зона: сборщик читает, а мы не смотрим и причины не записано.
    slepo = sorted(chitaet - smotrim - set(NE_SMOTRIM) - set(ne_tekst))
    return sorted(chitaet), slepo, sorted(
        (chitaet & set(ne_tekst)) | (chitaet & set(NE_SMOTRIM)))


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
    chital, slepo, s_prichinoy = polya_sborshchika()
    print("поля фронтматтера, которые читает код сборки: " + ", ".join(chital))
    print("из них пропущены НАМЕРЕННО, с причиной: " + ", ".join(s_prichinoy))
    print("СЛЕПАЯ ЗОНА (сборщик читает, мы не смотрим, причины нет): "
          + (", ".join(slepo) if slepo else "нет — список сошёлся"))
    bez_uslovia = sorted(set(chital) - set(USLOVIE) - set(NE_SMOTRIM)
                         - {"id", "media", "media_hero", "type"})
    print("полей без записанного условия рисования: "
          + (", ".join(bez_uslovia) if bez_uslovia else "нет — условие есть у каждого"))
    print("чего этот сторож не умеет: поля, читаемого ядром под вычисленным "
          "именем, он не увидит; и условие рисования он СВЕРЯЕТ по записи "
          "выше, а не выводит из кода.\n")
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
        for k, risuet, cond, adres in usloviya(f):
            if risuet != "да":
                print(f"  !! {k}: {risuet}  [{adres}]")
