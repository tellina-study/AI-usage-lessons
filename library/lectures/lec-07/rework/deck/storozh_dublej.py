#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сторож дословных повторов в заметках лектора: абзац, уже сказанный выше.

ЧТО ОН ЛОВИТ И ПОЧЕМУ ИМЕННО ЭТО. За два круга правок из заметок деки
снято пять абзацев, каждый из которых дословно или почти дословно
повторял абзац, стоявший в том же файле выше: s11a (829 → 751),
s12 (825 → 739), s13 (814 → 768), s15 (576 → 512) и пара s16/s17 при
свёртке. Ни критика, ни просмотр глазами их не нашли — нашлись они
только при сверке заметок на длину.

Общее у всех пяти — не «ленивое повторение», а **отсутствие прохода по
заметке целиком после правки**: абзац дописывался в конец, когда та же
мысль уже стояла в середине. Поэтому сторож сравнивает абзацы ВНУТРИ
одного файла и не ищет повторов между файлами: между кадрами повтор
бывает намеренным (одна мысль, предъявленная дважды на разных стадиях),
а внутри одной заметки — почти никогда.

ПОЧЕМУ ПОРОГ 0,85 И ПОЧЕМУ МЕРА ТАКАЯ. Мера — доля общих слов от
МЕНЬШЕГО из двух словарей: короткий абзац, целиком вложенный в длинный,
обязан ловиться, а при делении на объединение он тонет. На пяти снятых
повторах эта мера даёт от 0,86 до 1,00; ближайший НЕ повтор — 0,59
(s11a, два абзаца про решение стадии и про профессию как признак
группы). Порог 0,85 разделяет эти две кучи с запасом и на материале
этой деки ложных срабатываний не даёт. Проверяется это не на словах:

    python3 storozh_dublej.py --samoproverka

прогоняет сторож по состоянию деки ДО снятия повторов и печатает,
нашёл ли он там те кадры, ради которых заведён.

ПЕЧАТЬ ТОГО, ЧТО ПРОЧИТАНО, — ОБЯЗАТЕЛЬНАЯ ЧАСТЬ ОТВЕТА. В этом
производстве дважды случилось одно и то же: инструмент молча терял вход
и выдавал правдоподобный ответ — `git ls-tree` с путём от корня репозитория
вернул ноль файлов, и счёт «разборных кадров» вышел нулевым вместо
тридцати; разбор числа по частям кадра считал подвал по сырому полю и
завышал его втрое. Поэтому сторож всегда печатает, сколько файлов он
прочёл, сколько абзацев разобрал и сколько пар сравнил, а на пустом
входе падает с ненулевым кодом вместо бодрого «повторов нет».

    python3 storozh_dublej.py                 # вся папка slides/
    python3 storozh_dublej.py slides/s12-*.md # только названные файлы
    python3 storozh_dublej.py --porog 0.9
    python3 storozh_dublej.py --samoproverka

Код возврата: 0 — повторов нет; 1 — повторы найдены; 2 — читать было
нечего (пустой вход), и это отказ, а не «чисто».
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLIDES = HERE / "slides"

# Абзац короче этого в счёт не идёт: подзаголовок, строка источников и
# однострочная связка повторяются по делу и повтором не являются.
MIN_SLOV = 12
PO_UMOLCHANIYU = 0.85

# Коммит, на котором повторы ещё стояли в файлах, — материал самопроверки.
# Взят ПОСЛЕ круга диеты и ДО снятия повторов: сами повторы круг диеты и
# завёл, дописывая снятое с кадров в конец заметок, поэтому на более раннем
# коммите сторож честно находит ноль — и это не его отказ, а свойство
# материала. На этом состоянии он обязан находить те четыре кадра, которые
# потом правились руками; остальные его находки там — настоящие, просто о
# них тогда никто не знал.
DO_SNYATIYA = "4f334391"
ZHDEM = {"s11a", "s12", "s13", "s15"}


def slova(s):
    """Множество значимых слов абзаца: кириллица и цифры, разметка снята."""
    s = re.sub(r"\[[^\]]*\]\([^)]*\)", " ", s)          # ссылки целиком
    s = re.sub(r"[^а-яёА-ЯЁ0-9]+", " ", s)
    return {w for w in s.lower().split() if len(w) > 2}


def abzatsy(text):
    """Абзацы раздела «Заметки лектора» — то, что лектор произносит."""
    if "## Заметки лектора" not in text:
        return []
    notes = text.split("## Заметки лектора", 1)[1]
    out = []
    for raw in notes.split("\n\n"):
        a = raw.strip()
        if a.startswith("**Источники.**") or a.startswith("#"):
            continue
        if len(a.split()) < MIN_SLOV:
            continue
        out.append(a)
    return out


def pary(ab):
    """Все пары абзацев файла с мерой общности по МЕНЬШЕМУ словарю."""
    slov = [slova(a) for a in ab]
    for i in range(len(ab)):
        for j in range(i + 1, len(ab)):
            a, b = slov[i], slov[j]
            if not a or not b:
                continue
            yield i, j, len(a & b) / min(len(a), len(b))


def proverit(files, porog):
    """(находки, сколько файлов, сколько абзацев, сколько пар сравнено)."""
    nakhodki, n_ab, n_par = [], 0, 0
    for f, text in files:
        ab = abzatsy(text)
        n_ab += len(ab)
        for i, j, m in pary(ab):
            n_par += 1
            if m >= porog:
                nakhodki.append((f, i + 1, j + 1, m, ab[i], ab[j]))
    return nakhodki, len(files), n_ab, n_par


def chitat_s_diska(paths):
    return [(p.name, p.read_text(encoding="utf-8")) for p in paths]


def proverit_papku(slides_dir=None, porog=PO_UMOLCHANIYU):
    """Вызываемый вход для свода приёмки: результат ВОЗВРАЩАЕТСЯ, не печатается.

    Заведён затем, чтобы оболочка приёмки могла сказать в общей сводке,
    СКОЛЬКО пар и в каких кадрах, а не только «код возврата 1». Обёртка
    процессом этого сказать не может, и сводка выходит беднее.

    Возвращает словарь:
        prochitano: {"файлов": int, "абзацев": int, "пар": int}
        nahodki:    [{"kadr", "abzats_1", "abzats_2", "obshchnost",
                      "slov_vo_vtorom", "vyderzhka_1", "vyderzhka_2"}, …]
        porog:      применённый порог
        pusto:      True, если читать было нечего, — вызывающий ОБЯЗАН
                    отличить это от «повторов нет» (ровно та ошибка, ради
                    которой печать прочитанного стала требованием).
    """
    d = Path(slides_dir) if slides_dir else SLIDES
    files = chitat_s_diska(sorted(p for p in d.glob("s*.md") if p.is_file()))
    nakhodki, n_f, n_ab, n_par = proverit(files, porog)
    return {
        "prochitano": {"файлов": n_f, "абзацев": n_ab, "пар": n_par},
        "porog": porog,
        "pusto": n_f == 0 or n_ab == 0,
        "nahodki": [
            {"kadr": f.split("-")[0], "abzats_1": i, "abzats_2": j,
             "obshchnost": round(m, 3), "slov_vo_vtorom": len(b.split()),
             "vyderzhka_1": re.sub(r"\s+", " ", a)[:160],
             "vyderzhka_2": re.sub(r"\s+", " ", b)[:160]}
            for f, i, j, m, a, b in nakhodki],
    }


def chitat_iz_git(commit):
    """Файлы кадров из коммита — для самопроверки на материале «до»."""
    names = subprocess.run(
        ["git", "ls-tree", "--name-only", commit],
        cwd=SLIDES, capture_output=True, text=True).stdout.split("\n")
    out = []
    for n in names:
        if not n.endswith(".md") or n == "README.md":
            continue
        t = subprocess.run(["git", "show", f"{commit}:./{n}"],
                           cwd=SLIDES, capture_output=True, text=True).stdout
        if t:
            out.append((n, t))
    return out


def pechat_vkhoda(n_f, n_ab, n_par, otkuda):
    """Что прочитано — печатается ВСЕГДА, до всякого вывода о находках."""
    print(f"прочитано: {n_f} файлов, {n_ab} абзацев заметок, "
          f"сравнено {n_par} пар ({otkuda})")
    if n_f == 0 or n_ab == 0:
        print("ОТКАЗ: читать было нечего. Это не «повторов нет» — это "
              "пустой вход; проверьте путь и из какой папки запущено.")
        return False
    return True


def pechat_nakhodok(nakhodki, porog):
    if not nakhodki:
        print(f"повторов с общностью ≥ {porog:.2f} не найдено")
        return 0
    print(f"\nповторов найдено: {len(nakhodki)} (порог {porog:.2f})")
    for f, i, j, m, a, b in nakhodki:
        sid = f.split("-")[0]
        print(f"\n  {sid}: абзац {i} ~ абзац {j}, общность {m:.2f} — "
              f"во втором {len(b.split())} слов")
        print(f"      [{i}] {re.sub(r'\s+', ' ', a)[:120]}…")
        print(f"      [{j}] {re.sub(r'\s+', ' ', b)[:120]}…")
    print("\nСнимать можно ТОЛЬКО дословные и полностью вложенные абзацы. "
          "Пересказ той же мысли другими словами — не дубль: он бывает "
          "намеренным, и решает это человек, а не сторож.")
    return 1


def samoproverka(porog):
    """Сторож обязан находить те пять повторов, ради которых заведён."""
    files = chitat_iz_git(DO_SNYATIYA)
    nakhodki, n_f, n_ab, n_par = proverit(files, porog)
    print(f"самопроверка на состоянии деки до снятия повторов ({DO_SNYATIYA})")
    if not pechat_vkhoda(n_f, n_ab, n_par, f"из git, коммит {DO_SNYATIYA}"):
        return 2
    nashel = {f.split("-")[0] for f, *_ in nakhodki}
    print(f"кадры с повторами: {sorted(nashel) or '—'}")
    print(f"ожидались:         {sorted(ZHDEM)}")
    ne_nashel = ZHDEM - nashel
    lishnie = nashel - ZHDEM
    if ne_nashel:
        print(f"ПРОВАЛ: не найдены {sorted(ne_nashel)}")
    if lishnie:
        print(f"сверх ожидаемого: {sorted(lishnie)} — на этом коммите это "
              "НЕ ложные срабатывания: повторы там настоящие, их просто "
              "никто тогда не искал")
    print("самопроверка пройдена" if not ne_nashel else "самопроверка провалена")
    return 0 if not ne_nashel else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--porog", type=float, default=PO_UMOLCHANIYU)
    ap.add_argument("--samoproverka", action="store_true")
    a = ap.parse_args()

    if a.samoproverka:
        return samoproverka(a.porog)

    paths = ([Path(x) for x in a.files] if a.files
             else sorted(p for p in SLIDES.glob("s*.md")))
    paths = [p for p in paths if p.is_file()]
    files = chitat_s_diska(paths)
    nakhodki, n_f, n_ab, n_par = proverit(files, a.porog)
    otkuda = "названные файлы" if a.files else f"папка {SLIDES.name}/"
    if not pechat_vkhoda(n_f, n_ab, n_par, otkuda):
        return 2
    return pechat_nakhodok(nakhodki, a.porog)


if __name__ == "__main__":
    sys.exit(main())
