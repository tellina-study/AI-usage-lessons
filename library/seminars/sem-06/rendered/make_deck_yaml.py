#!/usr/bin/env python3
"""Собрать `deck.yaml` ИЗ САМИХ ФАЙЛОВ СЛАЙДОВ. Семинар 6, по образцу
`sem-05/rendered/make_deck_yaml.py` (та же причина для генератора, тот же
риск ручной правки «скучного» файла — см. sem-05 докстринг этого модуля).

Что берётся откуда:

* `id`, `type`, `duration_min`, `assertion`, `learning_goal`, `visual` — из
  фронтматтера слайда, дословно. Это и есть поля, которые автор уже написал;
  второй раз их никто не вводит.
* `file` — из имени файла.
* `slide_count`, `duration_min` шапки, разбивка по блокам — СЧИТАЮТСЯ, не
  переносятся руками.
* `title`, `central_question` — из обложки (`hero_cover`, n01): заголовок и
  вопрос в золотой коробке.
* `axis` — из ПЕРВОГО слайда с приёмом `recap_table` (на Семинаре 6 это n03,
  ось занятия с пустыми строками). Отличие от Семинара 5: там ось-первый-раз
  называлась отдельным приёмом `keystone_scope_map`, и `axis` брался из него;
  здесь первый и повторный показ оси делят один приём `recap_table` — других
  признаков, кроме порядка появления в файлах, различить их не может.
* `seminar_number`, `audience`, `format`, `language`, `slot_min` — прозаические
  поля, переносятся из прежнего `deck.yaml` как есть: вывести их неоткуда.

    python3 make_deck_yaml.py            # переписать ../deck.yaml под слайды n*
    python3 make_deck_yaml.py --check    # только сверить, ничего не писать
"""
import re
import sys
from pathlib import Path

import yaml

import build_sem06 as B
import deck_kit as K
import slide_parts as SP

ROOT = Path(__file__).resolve().parent.parent
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)

# Поля шапки, которые не выводятся ни из чего и переносятся как есть.
CARRIED = ("seminar_number", "audience", "format", "language", "slot_min")


def frontmatter(path):
    m = FM.match(path.read_text(encoding="utf-8"))
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def slides_of(prefix):
    out = []
    for f in sorted((ROOT / "slides").glob(f"{prefix}*.md")):
        fm = frontmatter(f)
        sid = fm.get("id") or f.name.split("-")[0]
        if sid != f.name.split("-")[0]:
            print(f"  ⚠ {f.name}: id «{sid}» не совпадает с именем файла")
        row = {"id": sid, "file": f"slides/{f.name}"}
        for k in ("type", "duration_min", "assertion", "learning_goal", "visual"):
            if k in fm:
                row[k] = fm[k]
        out.append((B.num(sid), row, f))
    out.sort(key=lambda r: r[0])
    return [r[1] for r in out], [r[2] for r in out]


def cover_texts(files):
    """Заголовок, центральный вопрос и строка оси — из самих слайдов.

    `axis` берётся из ПЕРВОГО по порядку файлов слайда с приёмом
    `recap_table` (см. докстринг модуля) — не из второго, не из последнего:
    `files` уже отсортирован по номеру (`slides_of`), и первое совпадение в
    цикле — самое раннее появление оси в деке."""
    title = question = axis = None
    for f in files:
        fm = frontmatter(f)
        pat = (fm.get("visual") or {}).get("pattern")
        t, _a, v, _n = SP.sections(f.read_text(encoding="utf-8"))
        if pat == "hero_cover" and title is None:
            title = t
            for kind, b in SP.blocks(v):
                if kind == "quote":
                    body = " ".join(K.plain(l) for l in b).strip()
                    if body.rstrip("»\"' ").endswith("?"):
                        question = body.strip("«»")
        if pat == "recap_table" and axis is None:
            axis = fm.get("assertion")
    return title, question, axis


def gaps(slides):
    """Дыры и повторы в нумерации.

    Повтор считается по ИДЕНТИФИКАТОРУ, а не по номеру: `n18` и `n18a` — это
    два разных слайда с одним номером, и так их и заводят, когда слайд делят
    надвое и не хотят двигать всю деку. Проверка по номеру объявляла такую
    пару дефектом — ложно, и ровно в тот момент, когда деление слайдов идёт
    потоком."""
    ids = [s["id"] for s in slides]
    nums = {B.num(i) for i in ids}
    holes = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    return holes, dupes


def build(prefix="n"):
    slides, files = slides_of(prefix)
    if not slides:
        raise SystemExit(f"слайдов по образцу «{prefix}*.md» не найдено")
    holes, dupes = gaps(slides)
    if holes:
        print(f"  ⚠ пропуски в нумерации: {holes}")
    if dupes:
        print(f"  ⚠ повторяющиеся идентификаторы: {dupes}")

    # Прозаические поля шапки переносятся из того же `deck.yaml`, если он уже
    # существует (первая сборка — его ещё нет, и голова будет пустой; Семинар 6
    # не держит рядом легаси-деку, в отличие от Семинара 5 c `deck-s50.yaml`).
    head = {}
    f = ROOT / "deck.yaml"
    if f.exists():
        head = dict((yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("deck") or {})
    title, question, axis = cover_texts(files)

    total = round(sum(s.get("duration_min") or 0 for s in slides), 2)
    deck = {k: head[k] for k in CARRIED if k in head}
    deck.update({
        "title": title or head.get("title"),
        "central_question": question or head.get("central_question"),
        "axis": axis or head.get("axis"),
        "duration_min": total,
        "slide_count": len(slides),
    })
    # порядок полей шапки — читаемый, а не алфавитный
    order = ["seminar_number", "title", "audience", "duration_min", "format",
             "central_question", "language", "slide_count", "axis", "slot_min"]
    deck = {k: deck[k] for k in order if k in deck} | {
        k: v for k, v in deck.items() if k not in order}
    return {"deck": deck, "slides": slides}, slides


def header_comment(slides, deck):
    lines = [f"# {deck['title']}",
             "# Файл СОБРАН генератором: python3 rendered/make_deck_yaml.py",
             "# Поля слайдов — из фронтматтера самих слайдов; правьте слайд, а не этот файл.",
             "#",
             "# Хронометраж по блокам (считан, не переписан):"]
    for lo, hi, name, _ in B.sections_for(slides[0]["id"])[0]:
        s = sum(x.get("duration_min") or 0 for x in slides if lo <= B.num(x["id"]) <= hi)
        if s:
            lines.append(f"#   {name:<10} n{lo:02d}–n{hi:02d}  {s:>6.2f} мин")
    lines.append(f"#   {'ИТОГО':<10}            {deck['duration_min']:>6.2f} мин "
                 f"при слоте {deck.get('slot_min', '?')}")
    return "\n".join(lines) + "\n\n"


def main():
    check = "--check" in sys.argv
    doc, slides = build("n")
    text = header_comment(slides, doc["deck"]) + yaml.safe_dump(
        doc, allow_unicode=True, sort_keys=False, width=100, default_flow_style=False)
    out = ROOT / "deck.yaml"
    if check:
        cur = out.read_text(encoding="utf-8") if out.exists() else ""
        print("совпадает с файлом" if cur == text else "РАСХОДИТСЯ с файлом")
        return
    out.write_text(text, encoding="utf-8")
    print(f"{out.name}: {doc['deck']['slide_count']} слайдов, "
          f"{doc['deck']['duration_min']} мин при слоте {doc['deck'].get('slot_min')}")


if __name__ == "__main__":
    main()
