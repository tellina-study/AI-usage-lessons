#!/usr/bin/env python3
"""Проверка единственности верного ответа у каждого из 100 запросов.

Как. Запрос лемматизируется (pymorphy3), служебные слова отбрасываются. Для
каждой содержательной леммы считается, в скольких РАЗМЕТКАХ корпуса-101 она
встречается. Запрос считается РАЗЛИЧАЮЩИМ, если у него есть хотя бы одна лемма,
встречающаяся ровно в одной разметке — и это разметка его ответа.

Это сторож, а не доказательство: он показывает, у каких запросов нет ни одного
уникального слова, и эти запросы читаются ГЛАЗАМИ (канон §8.12). Его вывод —
список на проверку, а не вердикт.

Запуск:  python3 proverka_edinstvennosti.py
"""
import json, re, sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from corpus_b101 import load_razmetka  # noqa: E402
import pymorphy3  # noqa: E402

MORPH = pymorphy3.MorphAnalyzer()
STOP = set("""и в во не что он на я с со как а то все она так его но да ты к у же вы за бы по
только ее мне было вот от меня еще нет о из ему теперь когда даже ну вдруг ли если уже или ни
быть был него до вас нибудь опять уж вам ведь там потом себя ничего ей может они тут где есть
надо ней для мы тебя их чем была сам чтоб без будто чего раз тоже себе под будет ж тогда кто
этот того потому этого какой совсем ним здесь этом один почти мой тем чтобы нее сейчас были
куда зачем всех никогда можно при наконец два об другой хоть после над больше тот через эти
нас про всего них какая много разве три эту моя впрочем хорошо свою этой перед иногда лучше
чуть том нельзя такой им более всегда конечно всю между видно стоять находиться лежать стоит
который которая которые это весь свой её рядом виден видна видны кадр снимок фотография""".split())
# Английские служебные слова: без них сторож считал «on»/«with»/«and» содержательными
# и выдавал 35 ложных тревог из 100 — собственный грейдер, разошедшийся с чтением
# глазами, не публикуется как факт (канон §8.12). Пойман на первом же прогоне.
STOP_EN = set("""a an the of in on at to for with and or is are was were be been by from as
into over under near this that these those there here it its his her their our your my no not
they he she we you i do does did has have had will would can could single lone own same other
another which who whom whose while during about above below between behind beside front back
up down out off than then when where why how all any both each few more most some such only
same so very s t don now also just like one two three four five six seven eight nine ten
people person man woman men women thing things""".split())
LAT = re.compile(r"[A-Za-z][A-Za-z'’-]*")
CYR = re.compile(r"[А-Яа-яЁё][А-Яа-яЁё-]*")


def lemmas(text):
    out = set()
    for w in CYR.findall(text.lower()):
        if len(w) < 3:
            continue
        l = MORPH.parse(w)[0].normal_form
        if l not in STOP and len(l) > 2:
            out.add(l)
    for w in LAT.findall(text):
        wl = w.lower()
        if len(wl) >= 2 and wl not in STOP_EN:
            out.add(wl)
    return out


def main():
    """Единственность — свойство СОЧЕТАНИЯ слов запроса, не одного слова.
    Поэтому каждая разметка корпуса оценивается числом лемм запроса, которые в
    ней есть; ответ обязан быть ЕДИНСТВЕННЫМ максимумом. Ничья с другим снимком
    = запрос не различает их, и он читается глазами.

    Первая версия этого сторожа считала уникальность ОДНОГО слова и дала 35
    ложных тревог из 100 (плюс английские служебные слова шли как содержательные).
    Обе ошибки пойманы на прогоне и записаны в журнал — сторож, разошедшийся с
    чтением глазами, не публикуется как факт (канон §8.12).
    """
    rz = load_razmetka()
    doc_lem = {i: lemmas(" ".join(e["what_is_visible"])) for i, e in rz.items()}
    qs = json.loads((HERE / "zaprosy_101.json").read_text(encoding="utf-8"))["queries"]

    clean, ties = 0, []
    for q in qs:
        ql = lemmas(q["ru"]) | lemmas(q["en"])
        scores = {i: len(ql & ls) for i, ls in doc_lem.items()}
        best = max(scores.values())
        winners = [i for i, s in scores.items() if s == best]
        q["_best"] = best
        q["_margin"] = best - max([s for i, s in scores.items() if i != q["answer"]] or [0])
        if winners == [q["answer"]]:
            clean += 1
        else:
            ties.append((q, winners, scores))

    print(f"запросов: {len(qs)}")
    print(f"ответ — ЕДИНСТВЕННЫЙ максимум по числу совпавших лемм: {clean}")
    print(f"ничья или чужой максимум (читать глазами): {len(ties)}")
    print()
    for q, winners, scores in ties:
        other = [i for i in winners if i != q["answer"]]
        mark = "ОТВЕТ НЕ В ЛИДЕРАХ" if q["answer"] not in winners else "ничья"
        print(f"  [{q['num']} {q['class_name']}] {mark}, совпало {q['_best']} лемм")
        print(f"      {q['ru'][:78]}")
        print(f"      ответ {q['answer'][:8]} (его счёт {scores[q['answer']]}), "
              f"спорят: {', '.join(i[:8] for i in other[:6])}")
    margins = sorted(q["_margin"] for q in qs)
    print()
    print(f"отрыв ответа от лучшего чужого снимка, по всем {len(qs)} запросам: "
          f"мин {margins[0]}, медиана {margins[len(margins)//2]}, макс {margins[-1]}")
    print(f"запросов с отрывом 0 или меньше: {sum(1 for m in margins if m <= 0)}")


if __name__ == "__main__":
    main()
