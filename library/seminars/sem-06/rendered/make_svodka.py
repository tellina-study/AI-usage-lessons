#!/usr/bin/env python3
"""Собрать `SVODKA-SLAIDOV.md` ИЗ ФАЙЛОВ СЛАЙДОВ.

Карта слайдов — производное, и правило о производном (канон
`tools/seminar-production/README.md` §8.5) куплено этим самым файлом: карту
правили руками, она разошлась с фронтматтером, и на её числах потом считали
минуты — сессия получила 12,0 там, где в слайдах стояло 10,75. Генератора до
сведения после проведения у неё не было вовсе; это он.

Что откуда:

* номер, тип, минуты — из фронтматтера слайда; заголовок экрана — первая
  строка `# …` файла;
* границы блоков — из `build_sem06.sections_for`, то есть ровно те, по которым
  рисует дорожку сам сборщик деки: два источника границ разошлись бы молча;
* границы кейсов — по развилкам (`section_divider_macro`); «начало ступени» —
  развилка и то, что стоит за ней до первой сцены (`problem_scenario`);
* имена кейсов и вступление — `svodka-tekst.yaml`: из слайдов они не выводятся
  (дивайдер называет проблему словами сцены, а не именем кейса);
* все суммы и счётчики СЧИТАЮТСЯ.

    python3 make_svodka.py            # переписать ../SVODKA-SLAIDOV.md
    python3 make_svodka.py --check    # только сверить, ничего не писать
"""
import re
import sys
from datetime import date
from pathlib import Path

import yaml

import build_sem06 as B

ROOT = Path(__file__).resolve().parent.parent
HERE = Path(__file__).resolve().parent


def mins(x):
    """1.0 → «1», 1.25 → «1,25» — так, как это читают в карте."""
    return (f"{x:g}").replace(".", ",")


def sl(n):
    """«64 слайда», «11 слайдов», «1 слайд» — счётная форма по-русски."""
    last, two = n % 10, n % 100
    if 11 <= two <= 14 or last == 0 or last >= 5:
        return f"{n} слайдов"
    return f"{n} слайд" + ("" if last == 1 else "а")


def headline(rel):
    for line in (ROOT / rel).read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "—"


def groups(slides, lo, hi, stage, names):
    """Разбить блок на «начало ступени» и кейсы. Возвращает список
    (подзаголовок или None, слайды)."""
    body = [s for s in slides if lo <= B.num(s["id"]) <= hi]
    if stage is None:
        return [(None, body)], 0
    pat = lambda s: (s.get("visual") or {}).get("pattern")
    cuts = [i for i, s in enumerate(body) if pat(s) == "section_divider_macro"]
    if not cuts:
        return [(None, body)], 0
    out, case = [], 0
    for k, start in enumerate(cuts):
        end = cuts[k + 1] if k + 1 < len(cuts) else len(body)
        chunk = body[start:end]
        if k == 0:
            scene = next((i for i, s in enumerate(chunk) if pat(s) == "problem_scenario"), None)
            if scene is None:
                print(f"  ⚠ в первом кейсе блока нет сцены (`problem_scenario`) — "
                      f"«начало ступени» не выделено")
            elif scene > 1:
                out.append(("nachalo", chunk[:scene]))
                chunk = chunk[scene:]
        case += 1
        out.append((case, chunk))
    return out, case


def main():
    check = "--check" in sys.argv
    txt = yaml.safe_load((HERE / "svodka-tekst.yaml").read_text(encoding="utf-8"))
    deck = yaml.safe_load((ROOT / "deck.yaml").read_text(encoding="utf-8"))
    slides = deck["slides"]
    sections = B.sections_for(slides[0]["id"])[0]

    total_min = round(sum(s.get("duration_min") or 0 for s in slides), 2)
    slot = deck["deck"].get("slot_min")

    L = []
    L.append("---")
    L.append("seminar: 6")
    L.append("issue: 225")
    L.append(f'title: "{txt["title"]}"')
    L.append(f"обновлена: {date.today().isoformat()}")
    L.append(f'статус: "СОБРАНА генератором rendered/make_svodka.py из фронтматтера слайдов: '
             f'{sl(len(slides))}, {mins(total_min)} минуты при слоте {slot}, '
             f'сквозная нумерация n01…{slides[-1]["id"]}"')
    L.append('источник: "library/seminars/sem-06/slides/n*.md — поля id / type / duration_min '
             'и первая строка заголовка"')
    L.append("---")
    L.append("")
    L.append("# Карта слайдов — Семинар 6")
    L.append("")
    L.append(txt["vstupleniye"].rstrip())
    L.append("")

    case_counter = 0
    for bi, (lo, hi, name, stage) in enumerate(sections):
        body = [s for s in slides if lo <= B.num(s["id"]) <= hi]
        if not body:
            continue
        bmin = round(sum(s.get("duration_min") or 0 for s in body), 2)
        full = (txt.get("bloki") or {}).get(name, name)
        L.append(f"## Блок {bi} — {full} ({mins(bmin)} мин, {sl(len(body))})")
        L.append("")
        parts, _ = groups(slides, lo, hi, stage, txt)
        for tag, chunk in parts:
            cmin = round(sum(s.get("duration_min") or 0 for s in chunk), 2)
            if tag == "nachalo":
                sub = txt["nachalo"].get(name, "развилка, база, одностраничник")
                L.append(f"### Начало ступени — {sub} ({mins(cmin)} мин, {sl(len(chunk))})")
                L.append("")
            elif isinstance(tag, int):
                case_counter += 1
                title = txt["keysy"].get(case_counter, "—")
                L.append(f"### Кейс {case_counter} — {title} ({mins(cmin)} мин, "
                         f"{sl(len(chunk))})")
                L.append("")
            L.append("| № | Тип | Что на слайде | Мин |")
            L.append("|---|---|---|---|")
            for s in chunk:
                L.append(f"| `{s['id']}` | `{s.get('type', '—')}` | {headline(s['file'])} "
                         f"| {mins(s.get('duration_min') or 0)} |")
            L.append("")

    if case_counter != len(txt["keysy"]):
        print(f"  ⚠ кейсов в деке {case_counter}, имён в svodka-tekst.yaml "
              f"{len(txt['keysy'])} — поправить сидкар")

    # Время, которое по устройству слайда принадлежит залу. Считается по приёму,
    # а не по длине текста под слайдом, и разложено по видам, чтобы число можно
    # было проверить, а не принять на слово: прежняя, правленная руками карта
    # называла здесь 11,00 и тут же перечисляла слагаемые на 9,50.
    ZAL = {"question_with_option_cards": "голосования",
           "cobuilding_config_reveal": "со-сборка и практика",
           "reflection_question": "вопрос занятия и обсуждение"}
    vidy = []
    zal_min = 0.0
    for pat, label in ZAL.items():
        gr = [s for s in slides if (s.get("visual") or {}).get("pattern") == pat]
        if not gr:
            continue
        m = round(sum(s.get("duration_min") or 0 for s in gr), 2)
        zal_min += m
        vidy.append(f"{label} — {', '.join('`%s`' % s['id'] for s in gr)}, {mins(m)}")
    zal_min = round(zal_min, 2)
    zal = [s for s in slides if (s.get("visual") or {}).get("pattern") in ZAL]

    L.append(f"**Итог: {sl(len(slides))}, {mins(total_min)} минуты при слоте {slot}.** "
             f"Запас — {mins(round(slot - total_min, 2))} минуты. Счёт ведёт `duration_min` "
             f"слайда, и только он: длина заметок мерой времени занятия не является "
             f"(`CUT-ORDER.md`, раздел «Чем здесь больше не считают»).")
    L.append("")
    L.append(f"**Залу принадлежит {mins(zal_min)} минуты из {mins(total_min)}** — "
             f"{sl(len(zal))}, где по устройству слайда говорит зал. По видам: "
             + "; ".join(vidy) + ". Что из этого снимать нельзя и почему — `CUT-ORDER.md`.")
    L.append("")

    text = "\n".join(L)
    out = ROOT / "SVODKA-SLAIDOV.md"
    if check:
        print("совпадает с файлом" if out.read_text(encoding="utf-8") == text
              else "РАСХОДИТСЯ с файлом")
        return
    out.write_text(text, encoding="utf-8")
    print(f"{out.name}: {len(slides)} слайдов, {mins(total_min)} мин, "
          f"{case_counter} кейсов, залу {mins(zal_min)} мин")


if __name__ == "__main__":
    main()
