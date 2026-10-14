#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Два счёта повествования Лекции 7, которыми меряют, стало ли лучше.

    python3 zamer-povestvovaniya.py [ревизия ...]

Без аргументов меряет рабочее дерево. С несколькими — печатает их подряд, чтобы
«было → стало» читалось одной выдачей:

    python3 zamer-povestvovaniya.py 4787f2cb 0218ae48 HEAD

ЧТО СЧИТАЕТСЯ, и чем один счёт отличается от другого по природе.

1. ЖИВЫЕ СЦЕНЫ — счёт по РЕЕСТРУ, а не по образцу. Сцену распознать грепом нельзя:
   «человек, у которого есть ситуация и исход» (stroenie-i-povestvovanie.md §3) — это
   суждение. Поэтому ниже лежит поимённый реестр девяти сцен замера 2026-10-14 с якорной
   фразой каждой, и скрипт отвечает на один вопрос: ГДЕ эта сцена лежит сейчас и жива ли она.
   Так ловится то, что счётом по кадру не ловится: сцена раздела 7 переехала с `s73c` на
   `s73ca` между 4787f2cb и 0218ae48, и счёт «есть ли сцена на s73c» дал бы ложную тревогу.
   НОВУЮ сцену скрипт не увидит — её вносит человек, строкой в SCENES.

2. АДРЕСА ОСИ ПО РАЗДЕЛАМ — счёт механический и полный. Четыре адреса заявлены на keystone
   `s05`; порог канона §1.1 — «ни один раздел не остаётся без адресов».

Считается ВИДИМЫЙ слой (тело кадра + плашки). Заметки не считаются нарочно: находка P0-1
отчёта `storitelling-2026-10-14.md` в том и состоит, что ось живёт в заметках, а зал видит
кадр. Снятые кадры (`slides/_snyato/`) не считаются.

Третьим счётом идёт вопрос залу: он дешёвый, и именно он поймал, что диета убрала «из вас»
из вопроса на `s61` — вопрос к залу стал риторическим, не потеряв ни одного кадра. Он же
печатает отдельно четыре кадра, у которых вопрос ОБЯЗАН звучать без обращения (RHETORIC_BY_DESIGN):
счёт их видит, но в «починить» не кладёт — иначе правка сломает исполнение канона §1.2.

Четвёртым идёт разряд свидетельства на кадрах-разборах — счёт механический, по строгим словам
лестницы `s05b`. Поимённый разбор «что поднять, что устанавливать заново» —
`storitelling-2026-10-14-chast2.md` §9.2.
"""
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

SLIDES = "library/lectures/lec-07/rework/deck/slides/"

# Реестр сцен: имя · якорная фраза · где лежала при замере 2026-10-14 (101 кадр, 4787f2cb).
SCENES = [
    ("женщина 54 лет, письмо по возрасту", "пятьдесят четыре", "s01d"),
    ("техник у прибора",                   "техник ставит",    "s22a"),
    ("техник добывает годный снимок",      "у техника появилась", "s28"),
    ("приём: кашель три недели",           "кашель три недели", "s36"),
    ("половина третьего ночи, 30 коек",    "половина третьего", "s53"),
    ("приём на двенадцать минут",          "двенадцать минут", "s60c"),
    ("комиссия в четверг",                 "четверг",          "s66"),
    ("врач вернулся после года",           "рука дольше ищет", "s73c"),
    ("химик, виварий, доброволец",         "химик ставит",     "s77"),
]

ADDRESSES = {"внимание": r"вниман", "навык": r"навык",
             "подпись": r"подпис", "арбитраж": r"арбитраж"}

# Обращение к залу. Без него вопрос риторический: канон §3 — «вопросы про личный опыт
# собирают ответы; абстрактные собирают тишину, после которой лектор отвечает сам».
TO_ROOM = r"\bиз вас\b|\bу вас\b|\bу кого\b|\bвам\b|\bваш|\bвы бы\b|\bвы \b"

# Четыре кадра, у которых вопрос ОБЯЗАН звучать без обращения к залу, и правка их сломала бы.
# `s03`/`s106` — три проверки, инструмент, который лекция выдаёт залу. `s05`/`s103` — вопрос
# лекции, который канон §1.2 требует произнести РОВНО ДВАЖДЫ: во входе и в сборке. Счёт их
# печатает отдельно, чтобы они не попали в список «починить» (разбор — отчёт §9.1).
RHETORIC_BY_DESIGN = {"s03", "s106", "s05", "s103"}

# Разряд свидетельства (лестница `s05b`). Слова строгие: «пересказать» и «проверить» сюда не
# попадают нарочно — на них счёт давал ложные срабатывания.
RANK = (r"рандомизированн\w+|проспективн\w+|ретроспективн\w+|наблюдательн\w+|самоотчёт\w*|"
        r"поперечн\w+|мета-?анализ\w*|предрегистрирован\w+|виньетк\w+|лабораторн\w+ опыт\w*|"
        r"перекрёстн\w+|когорт\w+|срез\b|двойн\w+ слеп\w+|жреби\w+|препринт\w*")

# Кадр считается разбором, если его заголовок так и называется.
RAZBOR_TITLE = r"Пример \d|Зеркало|Доверие и стаж|Правило, собранное"


def read_slides(rev=None):
    """{sid: {'sec':…, 'vis':…}} из рабочего дерева (rev=None) или из ревизии."""
    out = {}
    if rev:
        names = subprocess.run(["git", "ls-tree", "-r", "--name-only", rev, SLIDES],
                               capture_output=True, text=True).stdout.split()
    else:
        names = [str(p) for p in sorted(Path(SLIDES).glob("*.md"))]
    for name in names:
        if "/_snyato/" in name or name.endswith("README.md"):
            continue
        if rev:
            text = subprocess.run(["git", "show", f"{rev}:{name}"],
                                  capture_output=True, text=True).stdout
        else:
            text = Path(name).read_text(encoding="utf-8")
        sid = re.search(r"^id:\s*(\S+)", text, re.M)
        if not sid:
            continue
        sec = re.search(r"^section:\s*\"?([^\"\n]+)", text, re.M)
        vis = re.search(r"## Видимый текст слайда\n(.*?)(?=\n## |\Z)", text, re.S)
        blocks = re.search(r"^blocks:\n(.*?)^\w", text, re.S | re.M)
        title = re.search(r"^title:\s*\"?([^\"\n]+)", text, re.M)
        out[sid.group(1)] = {
            "sec": sec.group(1).strip() if sec else "",
            "title": title.group(1).strip() if title else "",
            "vis": (vis.group(1) if vis else "") + " " + (blocks.group(1) if blocks else ""),
        }
    return out


def scenes(deck):
    print("\n[1] ЖИВЫЕ СЦЕНЫ — девять из реестра замера 2026-10-14")
    alive = 0
    for name, anchor, was in SCENES:
        here = sorted(s for s, d in deck.items() if anchor in d["vis"].lower())
        if here:
            alive += 1
            moved = "" if was in here else f"  ← переехала с {was}"
            print(f"  ✓ {name:<34} {', '.join(here)}{moved}")
        else:
            print(f"  ✗ {name:<34} СЦЕНЫ НЕТ НА ВИДИМОМ СЛОЕ (была на {was})")
    print(f"  живо {alive} из {len(SCENES)}")
    return alive


def axis(deck):
    print("\n[2] АДРЕСА ОСИ ПО РАЗДЕЛАМ — порог §1.1: ни одного раздела без адресов")
    per, sizes = defaultdict(Counter), Counter()
    for _, d in deck.items():
        sizes[d["sec"]] += 1
        for name, pat in ADDRESSES.items():
            if re.search(pat, d["vis"], re.I):
                per[d["sec"]][name] += 1
    mute = []
    for sec in sorted(sizes, key=lambda s: (len(s.split(".")[0]), s)):
        c = per[sec]
        flag = ""
        if not sum(c.values()):
            mute.append(sec)
            flag = "  ← НИ ОДНОГО"
        print(f"  {sec[:46]:<46} кадров {sizes[sec]:>2} | вним {c['внимание']} "
              f"навык {c['навык']} подп {c['подпись']} арб {c['арбитраж']}{flag}")
    whole = Counter()
    for c in per.values():
        whole.update(c)
    print(f"  по деке: " + " · ".join(f"{k} {whole[k]}" for k in ADDRESSES))
    print(f"  разделов без единого адреса: {len(mute)}")
    return mute


def questions(deck):
    print("\n[3] ВОПРОС ЗАЛУ на кадре — считается только вопрос С ОБРАЩЕНИЕМ к залу")
    per = defaultdict(list)
    rhetoric = []
    for sid, d in deck.items():
        for sentence in re.split(r"\n|(?<=\?)\s", d["vis"]):
            if "?" not in sentence:
                continue
            if re.search(TO_ROOM, sentence, re.I):
                per[d["sec"]].append(sid)
            else:
                rhetoric.append(sid)
    missing = []
    for sec in sorted(set(d["sec"] for d in deck.values()),
                      key=lambda s: (len(s.split(".")[0]), s)):
        got = sorted(set(per[sec]))
        if not got:
            missing.append(sec)
        print(f"  {sec[:46]:<46} {', '.join(got) if got else 'НЕТ'}")
    print(f"  разделов без вопроса к залу на кадре: {len(missing)}")
    by_design = sorted(set(rhetoric) & RHETORIC_BY_DESIGN)
    to_fix = sorted(set(rhetoric) - RHETORIC_BY_DESIGN)
    print(f"  вопрос без обращения ПО ЗАМЫСЛУ (не трогать): {', '.join(by_design) or '—'}")
    print(f"  вопрос без обращения, ЧИНИТЬ: {', '.join(to_fix) or '—'}")
    return missing


def ranks(deck):
    """Разряд свидетельства на видимом слое кадров-разборов (канон §7, лестница `s05b`)."""
    print("\n[4] РАЗРЯД СВИДЕТЕЛЬСТВА на кадрах-разборах")
    razb = {sid: d for sid, d in deck.items() if re.search(RAZBOR_TITLE, d["title"])}
    named = sorted(s for s, d in razb.items() if re.search(RANK, d["vis"], re.I))
    lack = sorted(set(razb) - set(named))
    print(f"  кадров-разборов {len(razb)} · слово разряда встретилось у {len(named)} · нет у {len(lack)}")
    print(f"  со словом:  {', '.join(named) or '—'}")
    print(f"  без слова:  {', '.join(lack) or '—'}")
    print("  ВНИМАНИЕ: этот счёт — сигнал, не вердикт. Он врёт в обе стороны, замерено:")
    print("    ложно ДА  — «срез» на s44 это ГИСТОЛОГИЧЕСКИЙ срез; «метаанализ» на s30/s30a")
    print("                относится к классическому режиму, а не к разбору;")
    print("    ложно НЕТ — s49c разряд называет словами («по группам жребием, 30 дней"
          " наблюдения»),")
    print("                термина лестницы при этом не употребляя.")
    print("    Выверенный вручную список — storitelling-2026-10-14-chast2.md §9.2"
          " (назван у четырёх).")
    return len(named), len(razb)


def main():
    revs = sys.argv[1:] or [None]
    for rev in revs:
        deck = read_slides(rev)
        print("=" * 96)
        print(f"РЕВИЗИЯ {rev or 'рабочее дерево'} — кадров {len(deck)}")
        scenes(deck)
        axis(deck)
        questions(deck)
        ranks(deck)
    return 0


if __name__ == "__main__":
    sys.exit(main())
