#!/usr/bin/env python3
"""Собрать `deck.en.yaml` ИЗ АНГЛИЙСКИХ СЛАЙДОВ — драйвер поверх `make_deck_yaml.py`.

Тот же замысел, что у `build_sem05_en.py`: русский генератор не форкается и не
правится, он импортируется и перенастраивается. Правило русского файла
остаётся в силе и для английской дорожки — **правьте слайд, а не манифест**:
переводчик трогает только `slides-en/*.md`, `deck.en.yaml` пересобирается
одной командой.

Почему порядок слайдов берётся из `deck.yaml`, а не из `ls slides-en/`
---------------------------------------------------------------------
Русский генератор перечисляет слайды глобом по каталогу. Пока дорожка
переводится, в `slides-en/` лежит ЧАСТЬ слайдов — и глоб дал бы манифест на
девять слайдов, в котором `n65` оказался бы шестым. От позиции в манифесте
зависит номер слайда в углу (`build_sem05.slide_number`) и номер кейса на
значке развилки (`divider_index`), так что частичный манифест молча
перенумеровал бы деку.

Поэтому порядок, `id`, `type`, `duration_min` и `visual.pattern` берутся из
русского `deck.yaml` — он авторитетен по составу, — а переводимые поля
(`assertion`, `learning_goal`, `visual.primary`, `visual.tag`) подставляются из
фронтматтера английского слайда там, где он есть. Где его ещё нет, поле
остаётся русским и слайд помечается в отчёте как непереведённый: манифест
всегда полон на 68 строк, и всегда видно, сколько из них настоящие.

Когда переведены все 68, подстановка срабатывает на каждом слайде, русских
полей в выходном файле не остаётся, и этот же файл становится финальным
манифестом — отдельного «финального» режима нет.

`visual.backup` переносится ПО-РУССКИ сознательно (решение D7, см.
EN-TRACK-BRIEF.md): это производственная справка о происхождении, она цитирует
собственные слова владельца курса и называет русские исходники. На слайд она
не попадает, сборщик её не читает, а перевод цитаты сделал бы цитату неверной.

    python3 make_deck_yaml_en.py           # переписать ../deck.en.yaml
    python3 make_deck_yaml_en.py --check   # только сверить, ничего не писать
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import make_deck_yaml as MK                   # noqa: E402
import build_sem05 as B                       # noqa: E402
import deck_kit as K                          # noqa: E402
import slide_parts as SP                      # noqa: E402
import build_sem05_en as EN                   # noqa: E402  (chrome table)

ROOT = MK.ROOT
SLIDES_EN = ROOT / "slides-en"
DECK_RU = ROOT / "deck.yaml"
DECK_EN = ROOT / "deck.en.yaml"

CYR = re.compile("[А-Яа-яЁё]")

# Прозаические поля шапки: вывести их неоткуда (то же рассуждение, что в
# русском генераторе), поэтому они записаны здесь — по-английски, один раз.
HEAD_EN = {
    "seminar_number": 5,
    "audience": "3rd year, 09.03.01 — practicing engineers, all of them use AI assistants",
    "format": "facilitator slides + open questions with cards (the question BEFORE the "
              "evidence) + co-building the artifact + mechanics on worked examples; "
              "there is no live terminal",
    "language": "en",
    "slot_min": 90,
}

# Переводимые поля фронтматтера. `pattern`/`figure` машинно читаемые и
# переносятся дословно; `backup` — решение D7 (см. докстринг).
TRANSLATED = ("assertion", "learning_goal")
TRANSLATED_VISUAL = ("primary", "tag")


def en_frontmatter(name):
    f = SLIDES_EN / name
    return MK.frontmatter(f) if f.exists() else None


def cover_texts_en():
    """Заголовок, центральный вопрос и ось — из английских слайдов.

    `make_deck_yaml.cover_texts` снимает кавычки через `strip("«»")`, то есть
    только русские; в английских артефактах кавычки прямые (решение D5), и без
    этой правки центральный вопрос попал бы в манифест вместе с ними.
    """
    title = question = axis = None
    for f in sorted(SLIDES_EN.glob("n*.md")):
        fm = MK.frontmatter(f)
        pat = (fm.get("visual") or {}).get("pattern")
        t, _a, v, _n = SP.sections(f.read_text(encoding="utf-8"))
        if pat == "hero_cover" and title is None:
            title = t
            for kind, b in SP.blocks(v):
                if kind == "quote":
                    body = " ".join(K.plain(l) for l in b).strip()
                    if body.rstrip('»"\' ').endswith("?"):
                        question = body.strip('«»"')
        if pat == "keystone_scope_map" and axis is None:
            axis = fm.get("assertion")
    return title, question, axis


def build():
    ru = yaml.safe_load(DECK_RU.read_text(encoding="utf-8"))
    slides, untranslated = [], []

    for s in ru["slides"]:
        name = Path(s["file"]).name
        fm = en_frontmatter(name)
        row = {"id": s["id"], "file": f"slides-en/{name}"}
        for k in ("type", "duration_min"):
            if k in s:
                row[k] = s[k]
        for k in TRANSLATED:
            if k in s:
                row[k] = (fm or {}).get(k, s[k])
        if "visual" in s:
            v = dict(s["visual"])
            env = (fm or {}).get("visual") or {}
            for k in TRANSLATED_VISUAL:
                if k in v and k in env:
                    v[k] = env[k]
            row["visual"] = v
        slides.append(row)
        if fm is None:
            untranslated.append(s["id"])

    title, question, axis = cover_texts_en()
    total = round(sum(s.get("duration_min") or 0 for s in slides), 2)
    deck = dict(HEAD_EN)
    deck.update({
        "title": title or ru["deck"].get("title"),
        "central_question": question or ru["deck"].get("central_question"),
        "axis": axis or ru["deck"].get("axis"),
        "duration_min": total,
        "slide_count": len(slides),
    })
    order = ["seminar_number", "title", "audience", "duration_min", "format",
             "central_question", "language", "slide_count", "axis", "slot_min"]
    deck = {k: deck[k] for k in order if k in deck} | {
        k: v for k, v in deck.items() if k not in order}
    return {"deck": deck, "slides": slides}, slides, untranslated


def header_comment(slides, deck):
    lines = [f"# {deck['title']}",
             "# Generated: python3 rendered/make_deck_yaml_en.py",
             "# Slide fields come from the frontmatter of slides-en/*.md — "
             "edit the slide, not this file.",
             "# Order, type and duration_min come from the RU deck.yaml, which is "
             "authoritative for",
             "# the deck's composition (see the generator's docstring: a partial glob "
             "would renumber the deck).",
             "#",
             "# Timing per section (counted, not copied):"]
    for lo, hi, name, _ in B.sections_for(slides[0]["id"])[0]:
        s = sum(x.get("duration_min") or 0 for x in slides
                if lo <= B.num(x["id"]) <= hi)
        if s:
            lines.append(f"#   {EN.CHROME_DEFAULT.get(name, name):<16} "
                         f"n{lo:02d}–n{hi:02d}  {s:>6.2f} min")
    lines.append(f"#   {'TOTAL':<16}             {deck['duration_min']:>6.2f} min "
                 f"in a {deck.get('slot_min', '?')}-minute slot")
    return "\n".join(lines) + "\n\n"


def main():
    check = "--check" in sys.argv
    doc, slides, untranslated = build()
    text = header_comment(slides, doc["deck"]) + yaml.safe_dump(
        doc, allow_unicode=True, sort_keys=False, width=100,
        default_flow_style=False)

    if DECK_EN.resolve() == DECK_RU.resolve():      # paranoia, not politeness
        raise SystemExit("ОТКАЗ: генератор не пишет deck.yaml (русский манифест)")

    if check:
        cur = DECK_EN.read_text(encoding="utf-8") if DECK_EN.exists() else ""
        print("совпадает с файлом" if cur == text else "РАСХОДИТСЯ с файлом")
    else:
        DECK_EN.write_text(text, encoding="utf-8")
        print(f"{DECK_EN.name}: {doc['deck']['slide_count']} слайдов, "
              f"{doc['deck']['duration_min']} мин при слоте "
              f"{doc['deck'].get('slot_min')}")

    done = len(slides) - len(untranslated)
    print(f"переведено слайдов: {done}/{len(slides)}")
    if untranslated:
        print(f"ещё не переведены ({len(untranslated)}): "
              f"{', '.join(untranslated[:20])}"
              f"{'…' if len(untranslated) > 20 else ''}")
        print("  (их поля в манифесте пока русские — это ожидаемо, "
              "сборка их пропускает в режиме --partial)")
    else:
        # Полный перевод: русских полей остаться не должно нигде, кроме
        # `visual.backup` (решение D7).
        stray = []
        for s in doc["slides"]:
            for k in TRANSLATED:
                if k in s and CYR.search(str(s[k])):
                    stray.append(f"{s['id']}.{k}")
            for k in TRANSLATED_VISUAL:
                v = (s.get("visual") or {}).get(k)
                if v and CYR.search(str(v)):
                    stray.append(f"{s['id']}.visual.{k}")
        if stray:
            print(f"ВНИМАНИЕ: русский текст в переводимых полях: "
                  f"{', '.join(stray)}")
        else:
            print("зеркальная проверка: русского текста в переводимых полях нет "
                  "(visual.backup исключён — решение D7)")


if __name__ == "__main__":
    main()
