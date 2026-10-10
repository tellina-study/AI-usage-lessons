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
* `title` — из обложки (`hero_cover`, n01), заголовок.
* `cover_hook` — короткая загадка в золотой коробке обложки, если она там есть.
* `central_question` — вопрос занятия: из ПЕРВОГО слайда с приёмом
  `reflection_question` (на Семинаре 6 это n04, где вопрос задаётся после двух
  промахов; повторно он же стоит на n63). До пересмотра по сторителлингу вопрос
  занятия стоял на самой обложке, и поле читалось оттуда; теперь на обложке
  стоит загадка, и чтение из обложки приносило бы в манифест не тот вопрос.
* `axis` — из ПЕРВОГО слайда с приёмом `recap_table` (на Семинаре 6 это n03,
  ось занятия с пустыми строками). Отличие от Семинара 5: там ось-первый-раз
  называлась отдельным приёмом `keystone_scope_map`, и `axis` брался из него;
  здесь первый и повторный показ оси делят один приём `recap_table` — других
  признаков, кроме порядка появления в файлах, различить их не может.
* `seminar_number`, `audience`, `format`, `language`, `slot_min` — прозаические
  поля, переносятся из прежнего `deck.yaml` как есть: вывести их неоткуда.

    python3 make_deck_yaml.py                      # переписать ../deck.yaml под slides/n*
    python3 make_deck_yaml.py --check              # только сверить, ничего не писать
    python3 make_deck_yaml.py --lang en            # переписать ../deck.en.yaml под slides-en/n*
    python3 make_deck_yaml.py --lang en --check    # то же, без записи

## Английский манифест (issue 225, EN-трек Семинара 6)

`deck.en.yaml` СОБИРАЕТСЯ ТЕМ ЖЕ генератором из `slides-en/`, а не копируется с русского и
переводится руками. Причина та же, по которой генератор вообще заведён (докстринг sem-05):
манифест скучно править руками, и правят его невнимательно — а переведённая копия добавляет к
этому вторую беду, расхождение с собственными слайдами, которое ничем не ловится. Все поля,
которые генератор СЧИТАЕТ, он считает по английским слайдам: `assertion`, `learning_goal`,
`visual` едут из их фронтматтера дословно, `title` / `cover_hook` / `central_question` / `axis`
— с английской обложки, английского слайда-вопроса и английской оси.

Единственное, чего в английских слайдах нет нигде, — прозаические поля шапки (`audience`,
`format`). Их нельзя ни вывести, ни перенести с русского (перенос занёс бы кириллицу в
английский артефакт — зеркальная проверка §5.7 замка), поэтому они лежат пятью строками в
`rendered/deck-head.en.yaml`, и генератор читает их ОТТУДА. Если файла нет — генератор
отказывается работать и называет его, вместо того чтобы молча выдать манифест с пустой или
русской шапкой.

Границы блоков в шапке-комментарии берутся из `build_sem06.sections_for`, то есть выводятся по
РУССКОМУ манифесту. Это не недосмотр: границы — свойство нумерации, а нумерация у двух дек одна
(имена файлов совпадают знак в знак, на этом стоит сверка §5.8 замка). Английские имена блоков
взяты из замка (Часть D: Мостик → Bridge, Субагент → Subagent, Сборка → Wrap-up).
"""
import re
import sys
from pathlib import Path

import yaml

import build_sem06 as B
import deck_kit as K
import slide_parts as SP

ROOT = Path(__file__).resolve().parent.parent
HERE = Path(__file__).resolve().parent
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)

# Поля шапки, которые не выводятся ни из чего и переносятся как есть.
CARRIED = ("seminar_number", "audience", "format", "language", "slot_min")

# Язык → (каталог слайдов, имя манифеста, откуда брать прозаическую шапку).
# Русская строка читает шапку из своего же манифеста (как было); английская — из отдельного
# файла, потому что переносить её с русского нельзя, а выводить неоткуда (см. докстринг).
LANGS = {
    "ru": {"slides": "slides", "deck": "deck.yaml", "head": None},
    "en": {"slides": "slides-en", "deck": "deck.en.yaml", "head": "deck-head.en.yaml"},
}

# Имена блоков занятия по-английски — из замка (Часть D). Нужны только шапке-комментарию:
# сами границы считаются по номерам, а номера у двух дек одни.
BLOCKS_EN = {"Мостик": "Bridge", "MCP": "MCP", "Субагент": "Subagent", "Сборка": "Wrap-up"}


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


# Кавычки, в которые может быть обёрнута реплика: русские «ёлочки» и английские пары.
# Снимаются с ЗНАЧЕНИЯ поля манифеста (не со слайда): в русском манифесте `cover_hook` и
# `central_question` лежат без «ёлочек», и английский обязан лежать так же — иначе одно и то же
# поле двух манифестов различается обёрткой, и сверка RU↔EN спотыкается на ней каждый раз.
QUOTE_WRAP = '«»"\u201c\u201d'


def _gold_question(visual):
    """Вопрос из золотой коробки слайда — первая цитата, кончающаяся «?»."""
    for kind, b in SP.blocks(visual):
        if kind == "quote":
            body = " ".join(K.plain(l) for l in b).strip()
            if body.rstrip("»\"' ").endswith("?"):
                return body.strip(QUOTE_WRAP)
    return None


def cover_texts(files):
    """Заголовок, загадка обложки, вопрос занятия и строка оси — из слайдов.

    `axis` берётся из ПЕРВОГО по порядку файлов слайда с приёмом
    `recap_table` (см. докстринг модуля) — не из второго, не из последнего:
    `files` уже отсортирован по номеру (`slides_of`), и первое совпадение в
    цикле — самое раннее появление оси в деке.

    `central_question` — из ПЕРВОГО слайда с приёмом `reflection_question`
    (n04). Обложка вопроса занятия больше не несёт: после пересмотра по
    сторителлингу там стоит загадка, и она уезжает в отдельное поле
    `cover_hook`, чтобы манифест не выдавал её за вопрос занятия."""
    title = hook = question = axis = None
    for f in files:
        fm = frontmatter(f)
        pat = (fm.get("visual") or {}).get("pattern")
        t, _a, v, _n = SP.sections(f.read_text(encoding="utf-8"))
        if pat == "hero_cover" and title is None:
            title = t
            hook = _gold_question(v)
        if pat == "reflection_question" and question is None:
            question = _gold_question(v)
        if pat == "recap_table" and axis is None:
            axis = fm.get("assertion")
    return title, hook, question, axis


def gaps(slides):
    """Дыры и повторы в нумерации.

    Повтор считается по ИДЕНТИФИКАТОРУ, а не по номеру: `n20` и `n18a` — это
    два разных слайда с одним номером, и так их и заводят, когда слайд делят
    надвое и не хотят двигать всю деку. Проверка по номеру объявляла такую
    пару дефектом — ложно, и ровно в тот момент, когда деление слайдов идёт
    потоком."""
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

    # Прозаические поля шапки переносятся из того же `deck.yaml`, если он уже
    # существует (первая сборка — его ещё нет, и голова будет пустой; Семинар 6
    # не держит рядом легаси-деку, в отличие от Семинара 5 c `deck-s50.yaml`).
    head = {}
    if cfg["head"]:
        # Английская строка: прозаическая шапка — отдельный файл, и его отсутствие это отказ,
        # а не пустая шапка. Манифест с пустым `audience`/`format` выглядит собранным и
        # проходит дальше, а дыру в нём замечает только читатель сайта.
        hf = HERE / cfg["head"]
        if not hf.exists():
            raise SystemExit(
                f"нет файла шапки «{hf.relative_to(ROOT.parent)}» — вывести `audience`/"
                f"`format` для языка «{lang}» неоткуда, а переносить их с русского нельзя "
                f"(кириллица в английском артефакте). Завести файл и повторить")
        head = dict(yaml.safe_load(hf.read_text(encoding="utf-8")) or {})
    else:
        f = ROOT / cfg["deck"]
        if f.exists():
            head = dict((yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("deck") or {})
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
    # порядок полей шапки — читаемый, а не алфавитный
    order = ["seminar_number", "title", "audience", "duration_min", "format",
             "cover_hook", "central_question", "language", "slide_count", "axis",
             "slot_min"]
    deck = {k: deck[k] for k in order if k in deck} | {
        k: v for k, v in deck.items() if k not in order}
    return {"deck": deck, "slides": slides}, slides


def header_comment(slides, deck, lang="ru"):
    en = lang == "en"
    if en:
        lines = [f"# {deck['title']}",
                 "# This file is GENERATED: python3 rendered/make_deck_yaml.py --lang en",
                 "# Slide fields come from the frontmatter of slides-en/*.md — edit the slide, "
                 "not this file.",
                 "# The prose header fields (audience, format) come from "
                 "rendered/deck-head.en.yaml.",
                 "#",
                 "# Timing per section (computed, not retyped):"]
    else:
        lines = [f"# {deck['title']}",
                 "# Файл СОБРАН генератором: python3 rendered/make_deck_yaml.py",
                 "# Поля слайдов — из фронтматтера самих слайдов; правьте слайд, а не этот файл.",
                 "#",
                 "# Хронометраж по блокам (считан, не переписан):"]
    for lo, hi, name, _ in B.sections_for(slides[0]["id"])[0]:
        s = sum(x.get("duration_min") or 0 for x in slides if lo <= B.num(x["id"]) <= hi)
        if s:
            label = BLOCKS_EN.get(name, name) if en else name
            unit = "min" if en else "мин"
            lines.append(f"#   {label:<10} n{lo:02d}–n{hi:02d}  {s:>6.2f} {unit}")
    if en:
        lines.append(f"#   {'TOTAL':<10}            {deck['duration_min']:>6.2f} min "
                     f"in a {deck.get('slot_min', '?')}-min slot")
    else:
        lines.append(f"#   {'ИТОГО':<10}            {deck['duration_min']:>6.2f} мин "
                     f"при слоте {deck.get('slot_min', '?')}")
    return "\n".join(lines) + "\n\n"


def main():
    argv = sys.argv[1:]
    check = "--check" in argv
    lang = "ru"
    if "--lang" in argv:
        i = argv.index("--lang")
        lang = argv[i + 1] if i + 1 < len(argv) else ""
    if lang not in LANGS:
        raise SystemExit(f"--lang принимает {'/'.join(LANGS)}, передано «{lang}»")
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
