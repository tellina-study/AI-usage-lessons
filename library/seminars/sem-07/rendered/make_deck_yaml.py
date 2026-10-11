#!/usr/bin/env python3
"""Собрать `deck.yaml` ИЗ САМИХ ФАЙЛОВ СЛАЙДОВ. Семинар 7, по образцу
`sem-06/rendered/make_deck_yaml.py` (та же причина для генератора, тот же
риск ручной правки «скучного» файла).

Что берётся откуда:

* `id`, `type`, `duration_min`, `assertion`, `learning_goal`, `visual` — из
  фронтматтера слайда, дословно.
* `file` — из имени файла.
* `slide_count`, `duration_min` шапки, разбивка по блокам — СЧИТАЮТСЯ.
* `title` — из обложки (`hero_cover`, n01).
* `cover_hook` — короткая загадка в золотой коробке обложки, если она там
  есть (на n01 её нет по прямому требованию задания слайда — обложка
  «чистая»; поле останется пустым, и это ожидаемо, не дефект).
* `central_question` — вопрос занятия: из ПЕРВОГО слайда с приёмом
  `question_with_option_cards` ИЛИ `guess_the_number` (на Семинаре 7 это
  n21 — «Нужен ли здесь полноценный вызов модели — или достаточно метки?»).
  Отличие от Семинара 6: там этот вопрос стоял за приёмом `reflection_
  question` буквально; здесь то же имя — ТИП слайда (`type:`), а
  `visual.pattern` у вопросных слайдов этой деки — `question_with_option_
  cards`/`guess_the_number` (см. `build_sem07.PATTERN_ROLE`/`GENRE_FN`), и
  читать нужно именно их, иначе central_question осталось бы пустым.
* `axis` — из ПЕРВОГО слайда с приёмом `recap_table` (n02, лестница из
  девяти строк, пустая).
* `seminar_number`, `audience`, `format`, `language`, `slot_min` — из
  `HEAD_DEFAULTS` при первой сборке (deck.yaml ещё не существует вовсе —
  в отличие от Семинара 6, у Семинара 7 нет предыдущей версии манифеста,
  откуда их перенести); при повторных сборках — из уже существующего
  deck.yaml, как в Семинаре 6.

    python3 make_deck_yaml.py            # переписать ../deck.yaml под slides/n*
    python3 make_deck_yaml.py --check    # только сверить, ничего не писать
"""
import re
import sys
from pathlib import Path

import yaml

import build_sem07 as B
import deck_kit as K
import slide_parts as SP

ROOT = Path(__file__).resolve().parent.parent
HERE = Path(__file__).resolve().parent
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)

CARRIED = ("seminar_number", "audience", "format", "language", "slot_min")

# Бутстрап шапки — используется ТОЛЬКО когда ../deck.yaml ещё не существует
# (самая первая сборка этого занятия). `ARCHITECTURE.md` frontmatter:
# duration_min: 90 (слот), material_min: 87 (целевой бюджет материала).
HEAD_DEFAULTS = {
    "seminar_number": 7,
    "audience": "3 курс, 09.03.01 — практикующие инженеры, все пользуются ИИ-ассистентами",
    "format": ("слайды фасилитатора + открытые вопросы с карточками (вопрос ДО разбора) + "
               "один вопрос без карточек (устная оценка числа) + механика на примерах; "
               "живого терминала нет"),
    "language": "ru",
    "slot_min": 90,
}

LANGS = {"ru": {"slides": "slides", "deck": "deck.yaml", "head": None}}


def frontmatter(path):
    m = FM.match(path.read_text(encoding="utf-8"))
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def slides_of(prefix, lang="ru"):
    sub = LANGS[lang]["slides"]
    out = []
    for f in sorted((ROOT / sub).glob(f"{prefix}*.md")):
        fm = frontmatter(f)
        sid = fm.get("id") or f.name.split("-")[0]
        if sid != f.name.split("-")[0]:
            print(f"  ⚠ {f.name}: id «{sid}» не совпадает с именем файла")
        row = {"id": sid, "file": f"{sub}/{f.name}"}
        for k in ("type", "duration_min", "assertion", "learning_goal", "visual"):
            if k in fm:
                row[k] = fm[k]
        out.append((B.num(sid), row, f))
    out.sort(key=lambda r: r[0])
    return [r[1] for r in out], [r[2] for r in out]


QUOTE_WRAP = '«»"“”'

# Приёмы, на которых стоит «вопрос занятия» (см. докстринг — отличие от
# Семинара 6, где центральный вопрос всегда лежал буквально за `visual.
# pattern: reflection_question`).
CENTRAL_QUESTION_PATTERNS = ("question_with_option_cards", "guess_the_number")


def _gold_question(visual):
    """Вопрос из золотой коробки слайда — первая цитата, кончающаяся «?»."""
    for kind, b in SP.blocks(visual):
        if kind == "quote":
            body = " ".join(K.plain(l) for l in b).strip()
            if body.rstrip("»\"' ").endswith("?"):
                return body.strip(QUOTE_WRAP)
    return None


def cover_texts(files):
    title = hook = question = axis = None
    for f in files:
        fm = frontmatter(f)
        pat = (fm.get("visual") or {}).get("pattern")
        t, _a, v, _n = SP.sections(f.read_text(encoding="utf-8"))
        if pat == "hero_cover" and title is None:
            title = t
            hook = _gold_question(v)
        if pat in CENTRAL_QUESTION_PATTERNS and question is None:
            question = _gold_question(v)
        if pat == "recap_table" and axis is None:
            axis = fm.get("assertion")
    return title, hook, question, axis


def gaps(slides):
    ids = [s["id"] for s in slides]
    nums = {B.num(i) for i in ids}
    holes = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    return holes, dupes


def build(prefix="n", lang="ru"):
    cfg = LANGS[lang]
    slides, files = slides_of(prefix, lang)
    if not slides:
        raise SystemExit(f"слайдов по образцу «{cfg['slides']}/{prefix}*.md» не найдено")
    holes, dupes = gaps(slides)
    if holes:
        print(f"  ⚠ пропуски в нумерации: {holes}")
    if dupes:
        print(f"  ⚠ повторяющиеся идентификаторы: {dupes}")

    head = dict(HEAD_DEFAULTS)
    f = ROOT / cfg["deck"]
    if f.exists():
        prev = dict((yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("deck") or {})
        head.update({k: prev[k] for k in CARRIED if k in prev})
    title, hook, question, axis = cover_texts(files)

    total = round(sum(s.get("duration_min") or 0 for s in slides), 2)
    deck = {k: head[k] for k in CARRIED if k in head}
    deck.update({
        "title": title or head.get("title"),
        "cover_hook": hook or head.get("cover_hook"),
        "central_question": question or head.get("central_question"),
        "axis": axis or head.get("axis"),
        "duration_min": total,
        "slide_count": len(slides),
    })
    deck["language"] = lang
    order = ["seminar_number", "title", "audience", "duration_min", "format",
             "cover_hook", "central_question", "language", "slide_count", "axis",
             "slot_min"]
    deck = {k: deck[k] for k in order if k in deck} | {
        k: v for k, v in deck.items() if k not in order and v is not None}
    return {"deck": deck, "slides": slides}, slides


def header_comment(slides, deck, lang="ru"):
    lines = [f"# {deck['title']}",
             "# Файл СОБРАН генератором: python3 rendered/make_deck_yaml.py",
             "# Поля слайдов — из фронтматтера самих слайдов; правьте слайд, а не этот файл.",
             "#",
             "# Хронометраж по блокам (считан, не переписан):"]
    B.set_lang(lang)
    for lo, hi, name, _ in B.sections_for(slides[0]["id"])[0]:
        s = sum(x.get("duration_min") or 0 for x in slides if lo <= B.num(x["id"]) <= hi)
        if s:
            lines.append(f"#   {name:<10} n{lo:02d}–n{hi:02d}  {s:>6.2f} мин")
    lines.append(f"#   {'ИТОГО':<10}            {deck['duration_min']:>6.2f} мин "
                 f"при слоте {deck.get('slot_min', '?')}")
    return "\n".join(lines) + "\n\n"


def main():
    argv = sys.argv[1:]
    check = "--check" in argv
    lang = "ru"
    doc, slides = build("n", lang)
    text = header_comment(slides, doc["deck"], lang) + yaml.safe_dump(
        doc, allow_unicode=True, sort_keys=False, width=100, default_flow_style=False)
    out = ROOT / LANGS[lang]["deck"]
    if check:
        cur = out.read_text(encoding="utf-8") if out.exists() else ""
        print(f"{out.name}: " + ("совпадает с файлом" if cur == text else "РАСХОДИТСЯ с файлом"))
        return
    out.write_text(text, encoding="utf-8")
    print(f"{out.name}: {doc['deck']['slide_count']} слайдов, "
          f"{doc['deck']['duration_min']} мин при слоте {doc['deck'].get('slot_min')}")


if __name__ == "__main__":
    main()
