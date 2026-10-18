#!/usr/bin/env python3
"""Собрать `SVODKA-SLAIDOV.md` ИЗ ФАЙЛОВ СЛАЙДОВ — один генератор на все занятия.

    python3 tools/seminar-build/make_svodka.py --seminar 07
    python3 tools/seminar-build/make_svodka.py --seminar 07 --check

Карта слайдов — производное, и правило о производном (канон
`tools/seminar-production/README.md` §8.5) куплено именно ею: карту правили
руками, она разошлась с фронтматтером, и на её числах потом считали минуты —
сессия получила 12,0 там, где в файлах стояло 10,75.

Что откуда:

* номера, типы, минуты — из фронтматтера слайдов; заголовок строки — первая
  строка `# ` файла слайда;
* границы блоков — из общей разметки (`deck-config.yaml`, `razmetka`), то есть
  ровно те, по которым рисует дорожку сам сборщик деки: два источника границ
  разошлись бы молча;
* границы кейсов — по дивайдерам кейса (`svodka.case_divider_patterns`);
  «начало ступени» — дивайдер и то, что стоит за ним до первой сцены;
* имена кейсов и вступление — `svodka-tekst.yaml` рядом со слайдами: из
  слайдов они не выводятся (дивайдер называет проблему словами сцены, а не
  именем кейса);
* время зала — по приёму слайда (`svodka.zal`), а не по длине текста под ним.
"""
import re
import sys
from datetime import date
from pathlib import Path

import yaml

import deck_config as D


def _cfg():
    return D.table("svodka")


def case_divider_patterns():
    return tuple(_cfg().get("case_divider_patterns")
                 or ("section_divider_macro", "case_divider_quote"))


def mins(x):
    """1.0 → «1», 1.25 → «1,25» — так, как это читают в карте."""
    return (f"{x:g}").replace(".", ",")


def sl(n):
    """«34 слайда», «11 слайдов», «1 слайд» — счётная форма по-русски."""
    last, two = n % 10, n % 100
    if 11 <= two <= 14 or last == 0 or last >= 5:
        return f"{n} слайдов"
    return f"{n} слайд" + ("" if last == 1 else "а")


def headline(rel):
    for line in (D.ROOT / rel).read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "—"


def groups(slides, lo, hi, stage, names):
    """Разбить блок на «начало ступени» и кейсы. Возвращает список
    (подзаголовок или None, слайды)."""
    body = [s for s in slides if lo <= D.num(s["id"]) <= hi]
    if stage is None:
        return [(None, body)], 0
    pat = lambda s: (s.get("visual") or {}).get("pattern")
    cuts = [i for i, s in enumerate(body) if pat(s) in case_divider_patterns()]
    if not cuts:
        return [(None, body)], 0
    out, case = [], 0
    for k, start in enumerate(cuts):
        end = cuts[k + 1] if k + 1 < len(cuts) else len(body)
        chunk = body[start:end]
        if k == 0:
            scene = next((i for i, s in enumerate(chunk)
                          if pat(s) == _cfg().get("scene_pattern", "problem_scenario")), None)
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
    argv = sys.argv[1:]
    check = "--check" in argv
    seminar = None
    if "--seminar" in argv:
        i = argv.index("--seminar")
        seminar = argv[i + 1] if i + 1 < len(argv) else ""
    import build as B
    seminar = seminar or B.seminar_from_cwd()
    if not seminar:
        raise SystemExit("не сказано, какое это занятие: передайте `--seminar NN` "
                         "или запускайте из папки семинара")
    D.configure(seminar)
    txt = yaml.safe_load((D.HERE / "svodka-tekst.yaml").read_text(encoding="utf-8"))
    deck = yaml.safe_load((D.ROOT / D.deck_file()).read_text(encoding="utf-8"))
    slides = deck["slides"]
    sections = D.sections_for(slides[0]["id"])[0]

    total_min = round(sum(s.get("duration_min") or 0 for s in slides), 2)
    slot = deck["deck"].get("slot_min")

    L = []
    L.append("---")
    L.append(f"seminar: {int(D.SEM)}")
    L.append(f"issue: {D.CFG.get('issue', '?')}")
    L.append(f'title: "{txt["title"]}"')
    L.append(f"обновлена: {date.today().isoformat()}")
    L.append(f'статус: "СОБРАНА генератором tools/seminar-build/make_svodka.py из фронтматтера слайдов: '
             f'{sl(len(slides))}, {mins(total_min)} минуты при слоте {slot}, '
             f'сквозная нумерация n01…{slides[-1]["id"]}"')
    L.append(f'источник: "library/seminars/sem-{D.SEM}/{D.slides_dir()}/n*.md — поля '
             f'id / type / duration_min и первая строка заголовка"')
    L.append("---")
    L.append("")
    L.append(f"# Карта слайдов — Семинар {int(D.SEM)}")
    L.append("")
    L.append(txt["vstupleniye"].rstrip())
    L.append("")

    case_counter = 0
    for bi, (lo, hi, name, stage) in enumerate(sections):
        body = [s for s in slides if lo <= D.num(s["id"]) <= hi]
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
                sub = (txt.get("nachalo") or {}).get(
                    name, _cfg().get("nachalo_default", "развилка, одностраничник"))
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

    # Время, которое по устройству слайда принадлежит залу: приём → как это
    # называется в карте (`svodka.zal` конфига занятия). Считается по приёму, а
    # не по длине текста под слайдом, и разложено по видам, чтобы число можно
    # было проверить, а не принять на слово.
    ZAL = _cfg().get("zal") or {}
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
    out = D.ROOT / "SVODKA-SLAIDOV.md"
    if check:
        print("совпадает с файлом" if out.read_text(encoding="utf-8") == text
              else "РАСХОДИТСЯ с файлом")
        return
    out.write_text(text, encoding="utf-8")
    print(f"{out.name}: {len(slides)} слайдов, {mins(total_min)} мин, "
          f"{case_counter} кейсов, залу {mins(zal_min)} мин")


if __name__ == "__main__":
    main()
