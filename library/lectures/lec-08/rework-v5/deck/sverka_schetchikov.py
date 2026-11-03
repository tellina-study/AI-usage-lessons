# -*- coding: utf-8 -*-
"""СЧЁТЧИКИ В ПРОЗЕ: числа, которые никакой генератор не пересобирает.

ЗАЧЕМ. Структурный разрез — снятый кадр, сведённые два в один, убранный
разбор — молча оставляет за собой числа, записанные СЛОВАМИ внутри текста:
«третье произнесение из четырёх», «шесть разобранных случаев», «остальные
пять». `deck.yaml` пересобирается программой и всегда прав; проза — нет.

ЗАМЕР, ради которого это написано: свёртка ОДНОГО кейса оставила 15
расхождений в 11 кадрах. Их не нашли ни критика, ни проведение, ни просмотр
глазами — только отдельный проход по всей деке на один вопрос.

ЧТО ЭТО НЕ ДЕЛАЕТ. Не чинит и не судит: решить, верно ли «из четырёх»,
может только тот, кто знает состав. Задача — предъявить ВСЕ такие места
разом, чтобы ни одно не осталось непроверенным.

ДВА СЛОЯ, И ИХ НЕЛЬЗЯ МЕШАТЬ. Служебные строки — комментарии `#`, поля
`chapter_ref`, `media_needed`, `vfy`, `*_zakaz` — это журнал работы, и
ссылка на снятый кадр в нём ЗАКОННА: «кадр поглотил s69a» обязано помнить
имя поглощённого. Первый прогон не различал слои и выдал 39 «поломок», из
которых почти все были такими записями, — счёт, в котором тонет настоящая
находка, хуже отсутствия счёта.

Запуск:  python3 sverka_schetchikov.py
"""
import re
import pathlib
import collections

SLIDES = pathlib.Path(__file__).resolve().parent.parent / "slides"

CHISLITELNYE = ("один|одного|одном|одна|две|двух|двум|три|трёх|трех|четыре|"
                "четырёх|четырех|пять|пяти|шесть|шести|семь|семи|восемь|"
                "восьми|девять|девяти|десять|десяти|одиннадцать|двенадцать")

PORYADKOVYE = ("перв|втор|трет|четвёрт|четверт|пят|шест|седьм|восьм|девят|"
               "десят")

OBRAZTSY = [
    # «из четырёх», «из 4», «одно из трёх» — самый частый вид
    ("из N", re.compile(r"\bиз\s+(?:%s|\d{1,2})\b" % CHISLITELNYE, re.I)),
    # «третье произнесение», «второй разбор», «пятый кейс»
    ("порядковое + предмет",
     re.compile(r"\b(?:%s)(?:ий|ье|ья|ое|ый|ая|ой|их|ем|ом)\s+"
                r"(?:произнесени|разбор|кейс|случа|кадр|раздел|пример|"
                r"упоминани|ступен)\w*" % PORYADKOVYE, re.I)),
    # «шесть случаев», «пять разборов», «три кадра»
    ("числительное + предмет",
     re.compile(r"\b(?:%s)\s+(?:случа|разбор|кейс|кадр|раздел|пример|"
                r"упоминани|ступен|адрес)\w*" % CHISLITELNYE, re.I)),
    # «остальные пять», «прочие три»
    ("остальные N",
     re.compile(r"\b(?:остальны|прочи|оставшиес)\w*\s+"
                r"(?:%s|\d{1,2})\b" % CHISLITELNYE, re.I)),
    # прямая ссылка на кадр: снятый кадр оставляет висячую ссылку
    ("ссылка на кадр", re.compile(r"\bs\d{1,3}[a-z]?\b")),
]


def main():
    zhivye = set()
    for f in sorted(SLIDES.glob("s*.md")):
        m = re.search(r"^id:\s*(\S+)", f.read_text(encoding="utf-8"), re.M)
        if m:
            zhivye.add(m.group(1).strip().strip('"'))

    naydeno = collections.defaultdict(list)
    visyachie = []
    zhurnal = 0

    sluzhebnye = re.compile(r"^\s*#|^\s*(chapter_ref|media_needed|vfy|"
                            r"\w*_zakaz|media_note|layout_note|local_id|"
                            r"source|answered_at)\s*:")
    for f in sorted(SLIDES.glob("s*.md")):
        text = f.read_text(encoding="utf-8")
        sid = (re.search(r"^id:\s*(\S+)", text, re.M) or [None, f.stem])[1]
        for nomer, stroka in enumerate(text.splitlines(), 1):
            sluzhebnaya = bool(sluzhebnye.match(stroka))
            for imya, obrazets in OBRAZTSY:
                for hit in obrazets.finditer(stroka):
                    if imya == "ссылка на кадр":
                        tsel = hit.group(0)
                        if tsel in zhivye or tsel == sid:
                            continue
                        if sluzhebnaya:
                            zhurnal += 1
                            continue
                        visyachie.append((sid, nomer, tsel,
                                          stroka.strip()[:90]))
                        continue
                    if sluzhebnaya:
                        continue
                    naydeno[imya].append((sid, nomer,
                                          hit.group(0),
                                          stroka.strip()[:90]))

    print(f"кадров прочитано: {len(zhivye)}")
    print(f"ссылок на снятые кадры в служебном журнале: {zhurnal} "
          f"(законны — журнал обязан помнить снятое)\n")
    if visyachie:
        print(f"ВИСЯЧИЕ ССЫЛКИ НА СНЯТЫЕ КАДРЫ — {len(visyachie)}; "
              f"это не предупреждение, это поломка:")
        for sid, n, tsel, s in visyachie:
            print(f"  {sid:>6}:{n:<4} → {tsel:<6} | {s}")
        print()
    for imya, _ in OBRAZTSY:
        if imya == "ссылка на кадр":
            continue
        spisok = naydeno[imya]
        print(f"— {imya}: {len(spisok)}")
        for sid, n, g, s in spisok:
            print(f"  {sid:>6}:{n:<4} «{g}» | {s}")
        print()
    print("Счётчик — не ошибка. Ошибка — счётчик, который никто не пересчитал "
          "после разреза. Проверь КАЖДЫЙ против нынешнего состава.")


if __name__ == "__main__":
    main()
