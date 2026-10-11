#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Запреты видимого слоя — по файлам кадров деки, а не по планам.

Зачем отдельный запуск. `tools/lecture-production/scan_visible_layer.py` ищет видимый
слой по разметке ПЛАНА — строкам вида «- **на экране:** …». В файле кадра такой разметки
нет: видимый слой там — поле `title`, полоса плашек, схема, столбцы и раздел «## Видимый
текст слайда». Поэтому прогон того скрипта по `slides/*.md` даёт «видимых полей: 0 — чисто»
на любом входе, и ноль этот не значит ничего. Ровно о таком нуле предупреждает docstring
самого скрипта.

Этот файл НЕ заводит своих запретов: словарь `BANS`, снятие идиомы тождества и ведро
«похоже на запрет» берутся импортом из того же скрипта — один источник правил. Своё здесь
одно: извлечение настоящего видимого слоя кадра плюс четыре запрета, которых у плана не
бывает, потому что они про файл кадра: служебная метка сверки на экране, ярлык «Вопрос
залу», заглушка-записка другой сессии и ссылка курса на себя.

    python3 scan_deck_visible.py --selftest     # доказать, что проверка умеет находить
    python3 scan_deck_visible.py                # прогон по slides/*.md
"""
import re
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
TOOLS = next(d / "tools" / "lecture-production" for d in HERE.parents
         if (d / "tools" / "lecture-production" / "scan_visible_layer.py").exists())
sys.path.insert(0, str(TOOLS))
from scan_visible_layer import BANS, IDIOM, NEGATED          # noqa: E402

EXTRA = {
    "служебная метка сверки на экране":
        re.compile(r"\[VFY[^\]]*\]|\[VERIFY-DAY-OF\]|\[FACT-CHECK\]", re.I),
    "служебный ярлык вместо самого вопроса":
        re.compile(r"вопрос\s+залу\s*:", re.I),
    "заглушка-записка на видимом слое":
        re.compile(r"\{\{(заметки|источник)\s*:"),
    "ссылка курса на себя":
        re.compile(r"→\s*s\d|\bсм\.\s*слайд|\bLO[1-9]\b|§\s*\d"),
}
ALL = dict(BANS)
ALL.update(EXTRA)

# Именованные исключения. Каждое — не «похоже на ложное», а названная причина,
# по которой строка под регулярку плана попадает, а запрета не несёт. Молча снимать
# нельзя: исключение печатается в прогоне рядом с причиной, и самотест отдельно
# доказывает, что исключение НЕ проглатывает настоящее нарушение того же класса.
EXEMPT = [
    ("превосходная форма", re.compile(r"главн(ого|ым|ому|ый) врач", re.I),
     "«заместитель главного врача» — должность, не превосходная форма"),
    ("превосходная форма", re.compile(r"в сам(ое|ом) начал", re.I),
     "«в самое начало» — указание места в работе, не превосходная форма"),
    ("превосходная форма", re.compile(r"сам(ому|ой|им|ого|а|и)\b", re.I),
     "«искать самому», «сама модель» — возвратное местоимение, не превосходная форма"),
    ("тайминг на видимом слое", re.compile(r"\d+\s*мин(ут)?\s*\d+\s*с|разбор расхожд", re.I),
     "измеренная длительность работы, а не тайминг раздела лекции"),
]


def exempt(name, text, span):
    """Исключение снимает ОДНО попадание, а не всю строку.

    Разница несущая, и она доказана приманкой в самотесте: строка «заместитель
    главного врача назвал это лучшим решением» содержит и исключение, и настоящее
    нарушение того же класса. Снятие по строке проглотило бы второе."""
    for n, rx, why in EXEMPT:
        if n != name:
            continue
        for m in rx.finditer(text):
            if m.start() <= span[1] and span[0] <= m.end():
                return why
    return None


def visible_lines(path):
    """Настоящий видимый слой кадра: заголовок, плашки, схема, столбцы, тело."""
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.S)
    if not m:
        return []
    meta = yaml.safe_load(m.group(1)) or {}
    out = []
    if meta.get("title"):
        out.append(("title", str(meta["title"])))
    for it in meta.get("blocks") or []:
        if isinstance(it, dict):
            for k in ("label", "value", "note"):
                if it.get(k):
                    out.append((f"плашка/{k}", str(it[k])))
    sch = meta.get("scheme")
    if isinstance(sch, dict):
        if sch.get("caption"):
            out.append(("схема/подпись", str(sch["caption"])))
        for r in sch.get("rows") or []:
            if isinstance(r, dict):
                if r.get("label"):
                    out.append(("схема/ряд", str(r["label"])))
                for st in r.get("steps") or []:
                    out.append(("схема/шаг", str(st)))
    cols = meta.get("columns")
    if isinstance(cols, dict):
        for side in ("left", "right"):
            c = cols.get(side)
            if isinstance(c, dict):
                if c.get("head"):
                    out.append(("столбец/шапка", str(c["head"])))
                for i in c.get("items") or []:
                    out.append(("столбец/строка", str(i)))
    body = re.search(r"##\s*Видимый текст слайда\s*\n(.*?)(?=\n##\s|\Z)", m.group(2), re.S)
    for ln in (body.group(1) if body else "").split("\n"):
        if ln.strip():
            out.append(("тело", ln.strip()))
    return out


def scan_one(path):
    hits, hedged, taken = [], [], []
    for where, text in visible_lines(path):
        probe = IDIOM.sub(" ", text)
        for name, rx in ALL.items():
            live, why = [], None
            for m in rx.finditer(probe):
                w = exempt(name, probe, m.span())
                if w:
                    why = w
                else:
                    live.append(m.group(0))
            if live:
                rec = (name, where, text[:110], None)
                (hedged if NEGATED.search(probe) else hits).append(rec)
            elif why:
                taken.append((name, where, text[:110], why))
    return hits, hedged, taken


_BROKEN = {
    "тайминг на видимом слое": "Раздел идёт 14 минут, дальше перерыв.",
    "методический мета-комментарий": "Лектору: методически важно сказать это медленно.",
    "превосходная форма": "Главный вывод вечера одной строкой.",
    "научная запись числа": "Расчёт занял 1,687·10⁵ часов.",
    "p-значение или интервал на экране": "Разница незначима, p = 0,60.",
    "служебная метка сверки на экране": "Одно чтение — 48 секунд [VFY: секунды сверить].",
    "служебный ярлык вместо самого вопроса": "Вопрос залу: где у вас стоит такой фильтр?",
    "заглушка-записка на видимом слое": "Формулировка — {{заметки: уточнить у сессии раздела}}.",
    "ссылка курса на себя": "Подробнее — § 3.9 и далее → s48.",
}
_CLEAN = "Одно чтение маммограммы — сорок восемь секунд, разбор расхождения кратно дольше."
# Приманки: строка, где исключение СРАБОТАЛО БЫ, и рядом настоящее нарушение
# того же класса — проверка обязана его поймать, невзирая на исключение.
_DECOY_SUP = "Заместитель главного врача назвал это важнейшим выводом вечера."
_DECOY_TIME = "Один разбор расхождения — 2 минуты 12 секунд, а раздел идёт 14 минут."

_HEAD = ('---\nid: s01\ntype: case\ntitle: "Проба"\nsource: "—"\n---\n\n'
         '## Видимый текст слайда\n\n')


def selftest():
    tmp = Path(tempfile.mkdtemp(prefix="lec07-vis-"))
    ok, bad = [], []
    p = tmp / "clean.md"
    p.write_text(_HEAD + _CLEAN + "\n\n## Заметки лектора\n\nпроба\n", encoding="utf-8")
    h, _, _ = scan_one(p)
    print("── САМОПРОВЕРКА ЗАПРЕТОВ ВИДИМОГО СЛОЯ ──────────────────────")
    print(f"чистый кадр: срабатываний {len(h)}"
          + (" — " + "; ".join(x[0] for x in h) if h else " (молчит, как и должен)"))
    if h:
        bad.append("чистый кадр дал срабатывание — проверка шумит")
    for name, text in _BROKEN.items():
        q = tmp / "broken.md"
        q.write_text(_HEAD + text + "\n\n## Заметки лектора\n\nпроба\n", encoding="utf-8")
        hh, _, _ = scan_one(q)
        got = [x for x in hh if x[0] == name]
        print(f"{name:<42} {'ЛОВИТ' if got else 'НЕ ЛОВИТ'}")
        (ok if got else bad).append(name)
    # Исключение не должно проглатывать настоящее нарушение того же класса.
    for text, why in ((_DECOY_SUP, "превосходная форма"), (_DECOY_TIME, "тайминг на видимом слое")):
        q = tmp / "decoy.md"
        q.write_text(_HEAD + text + "\n\n## Заметки лектора\n\nпроба\n", encoding="utf-8")
        hh, _, tk = scan_one(q)
        got = [x for x in hh if x[0] == why]
        print(f"исключение не глушит запрет ({why:<30}) "
              f"{'ДОКАЗАНО' if got else 'ПРОВАЛ'}")
        (ok if got else bad).append("исключение/" + why)
    print("─────────────────────────────────────────────────────────────")
    print(f"запретов ловит: {len(ok)} из {len(_BROKEN) + 2}")
    if bad:
        print("НЕ ДОКАЗАНО: " + ", ".join(bad))
        return 1
    print("все запреты доказаны на сломанном входе")
    return 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
    files = sorted((HERE / "slides").glob("s*.md"),
                   key=lambda f: (int(re.match(r"s(\d+)", f.name).group(1)), f.name))
    tot, hedge_all, taken_all = 0, [], []
    for f in files:
        hits, hedged, taken = scan_one(f)
        if hits:
            print(f"\n{f.name}")
            for name, where, text, _ in hits:
                print(f"  [{name}] {where}: {text}")
            tot += len(hits)
        hedge_all += [(f.name, *r) for r in hedged]
        taken_all += [(f.name, *r) for r in taken]
    if taken_all:
        print("\nснято по именованным исключениям:")
        for nm, name, where, text, why in taken_all:
            print(f"  {nm} [{name}] {where}: {text}\n      причина: {why}")
    if hedge_all:
        print("\nведро «похоже на запрет, глазами» (запрет внутри запрета):")
        for nm, name, where, text, _ in hedge_all:
            print(f"  {nm} [{name}] {where}: {text}")
    print(f"\nкадров просмотрено: {len(files)} · срабатываний: {tot} · "
          f"снято исключениями: {len(taken_all)} · глазами: {len(hedge_all)}")
    return 1 if tot else 0


if __name__ == "__main__":
    sys.exit(main())
