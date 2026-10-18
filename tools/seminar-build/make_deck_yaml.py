#!/usr/bin/env python3
"""Собрать `deck.yaml` ИЗ САМИХ ФАЙЛОВ СЛАЙДОВ — один генератор на все занятия.

    python3 tools/seminar-build/make_deck_yaml.py --seminar 07
    python3 tools/seminar-build/make_deck_yaml.py --seminar 07 --check

Зачем генератор. Манифест скучно править руками, и правят его невнимательно:
карта и манифест разошлись с фронтматтером, и на их числах потом считали
минуты — сессия получила 12,0 там, где в слайдах стояло 10,75 (канон §8.5,
правило куплено этим случаем). Поэтому:

* `type`, `duration_min`, `assertion`, `learning_goal`, `visual` — из
  фронтматтера слайда, дословно. Это поля, которые автор уже написал;
  второй раз их никто не вводит.
* `slide_count`, `duration_min` шапки, разбивка по блокам — СЧИТАЮТСЯ.
* `title` — заголовок обложки; `cover_hook` — короткая загадка в золотой
  коробке обложки, если она там есть.
* `central_question` — вопрос занятия, с приёма, названного в конфиге
  (`deck_yaml.central_question_patterns`): у разных занятий он стоит за
  разными именами приёмов, и угадывать его по типу слайда нельзя.
* `axis` — `assertion` первого слайда с приёмом оси
  (`deck_yaml.axis_pattern`).
* `seminar_number`, `audience`, `format`, `language`, `slot_min` —
  прозаические поля: вывести их неоткуда, поэтому они переносятся из уже
  существующего манифеста, а на самой первой сборке берутся из
  `deck_yaml.head_defaults` конфига занятия.

## Английский манифест

`deck.en.yaml` СОБИРАЕТСЯ ТЕМ ЖЕ генератором из `slides-en/`, а не копируется
с русского и переводится руками: переведённая копия добавляет к обычной беде
ручной правки вторую — расхождение с собственными слайдами, которое ничем не
ловится. Единственное, чего в английских слайдах нет нигде, — прозаическая
шапка: её нельзя ни вывести, ни перенести с русского (перенос занёс бы
кириллицу в английский артефакт), поэтому язык может объявить свой файл
шапки (`langs.en.head`), и его отсутствие — отказ, а не пустая шапка.
Границы блоков в шапке-комментарии берутся из общей разметки, то есть по
номерам: нумерация у двух дек одна.
"""

import re
import sys
from pathlib import Path

import yaml

import deck_config as D
import deck_kit as K
import slide_parts as SP

FM = re.compile(r"^---\n(.*?)\n---\n", re.S)

# Поля шапки, которые не выводятся ни из чего и переносятся как есть.
CARRIED = ("seminar_number", "audience", "format", "language", "slot_min")

# Кавычки, в которые может быть обёрнута реплика: русские «ёлочки» и
# английские пары. Снимаются со ЗНАЧЕНИЯ поля манифеста: русские
# `cover_hook`/`central_question` лежат без «ёлочек», и английские обязаны
# лежать так же — иначе одно поле двух манифестов различается обёрткой, и
# сверка RU↔EN спотыкается на ней каждый раз.
QUOTE_WRAP = '«»"“”'


def _cfg():
    return D.table("deck_yaml")


def frontmatter(path):
    m = FM.match(path.read_text(encoding="utf-8"))
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def slides_of(prefix, lang="ru"):
    sub = D.slides_dir()
    out = []
    for f in sorted((D.ROOT / sub).glob(f"{prefix}*.md")):
        fm = frontmatter(f)
        sid = fm.get("id") or f.name.split("-")[0]
        if sid != f.name.split("-")[0]:
            print(f"  ⚠ {f.name}: id «{sid}» не совпадает с именем файла")
        row = {"id": sid, "file": f"{sub}/{f.name}"}
        for k in ("type", "duration_min", "assertion", "learning_goal", "visual"):
            if k in fm:
                row[k] = fm[k]
        out.append((D.num(sid), row, f))
    out.sort(key=lambda r: r[0])
    return [r[1] for r in out], [r[2] for r in out]


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

    Берётся ПЕРВОЕ совпадение: `files` уже отсортирован по номеру, и первое
    совпадение в цикле — самое раннее появление в деке, а не второе и не
    последнее."""
    cover_pat = _cfg().get("cover_pattern", "hero_cover")
    q_pats = tuple(_cfg().get("central_question_patterns") or ())
    axis_pat = _cfg().get("axis_pattern")
    title = hook = question = axis = None
    for f in files:
        fm = frontmatter(f)
        pat = (fm.get("visual") or {}).get("pattern")
        t, _a, v, _n = SP.sections(f.read_text(encoding="utf-8"))
        if pat == cover_pat and title is None:
            title = t
            hook = _gold_question(v)
        if pat in q_pats and question is None:
            question = _gold_question(v)
        if axis_pat and pat == axis_pat and axis is None:
            axis = fm.get("assertion")
    return title, hook, question, axis


def gaps(slides):
    """Дыры и повторы в нумерации.

    Повтор считается по ИДЕНТИФИКАТОРУ, а не по номеру: `n20` и `n18a` — два
    разных слайда с одним номером, и так их и заводят, когда слайд делят
    надвое и не хотят двигать всю деку. Проверка по номеру объявляла такую
    пару дефектом — ложно, и ровно в тот момент, когда деление слайдов идёт
    потоком."""
    ids = [s["id"] for s in slides]
    nums = {D.num(i) for i in ids}
    holes = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    return holes, dupes


def build(prefix="n", lang="ru"):
    D.set_lang(lang)
    slides, files = slides_of(prefix, lang)
    if not slides:
        raise SystemExit(f"слайдов по образцу «{D.slides_dir()}/{prefix}*.md» не найдено")
    holes, dupes = gaps(slides)
    if holes:
        print(f"  ⚠ пропуски в нумерации: {holes}")
    if dupes:
        print(f"  ⚠ повторяющиеся идентификаторы: {dupes}")

    head = dict(_cfg().get("head_defaults") or {})
    head_file = (D.CFG.get("langs") or {}).get(lang, {}).get("head")
    if head_file:
        # Отдельный файл шапки (английский трек): его отсутствие — отказ, а не
        # пустая шапка. Манифест с пустым `audience`/`format` выглядит
        # собранным и проходит дальше, а дыру замечает только читатель сайта.
        hf = D.HERE / head_file
        if not hf.exists():
            raise SystemExit(
                f"нет файла шапки «{hf}» — вывести `audience`/`format` для языка "
                f"«{lang}» неоткуда, а переносить их с русского нельзя (кириллица "
                f"в английском артефакте). Завести файл и повторить")
        head = dict(yaml.safe_load(hf.read_text(encoding="utf-8")) or {})
    else:
        f = D.ROOT / D.deck_file()
        if f.exists():
            head.update(dict(
                (yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("deck") or {}))
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
             f"# Файл СОБРАН генератором: python3 tools/seminar-build/"
             f"make_deck_yaml.py --seminar {D.SEM}",
             "# Поля слайдов — из фронтматтера самих слайдов; правьте слайд, а не этот файл.",
             "#",
             "# Хронометраж по блокам (считан, не переписан):"]
    D.set_lang(lang)
    for lo, hi, name, _ in D.sections_for(slides[0]["id"])[0]:
        s = sum(x.get("duration_min") or 0 for x in slides if lo <= D.num(x["id"]) <= hi)
        if s:
            lines.append(f"#   {name:<10} n{lo:02d}–n{hi:02d}  {s:>6.2f} мин")
    lines.append(f"#   {'ИТОГО':<10}            {deck['duration_min']:>6.2f} мин "
                 f"при слоте {deck.get('slot_min', '?')}")
    return "\n".join(lines) + "\n\n"


def main():
    argv = sys.argv[1:]
    check = "--check" in argv
    seminar, lang = None, "ru"
    if "--seminar" in argv:
        i = argv.index("--seminar")
        seminar = argv[i + 1] if i + 1 < len(argv) else ""
    if "--lang" in argv:
        i = argv.index("--lang")
        lang = argv[i + 1] if i + 1 < len(argv) else "ru"
    if not D.CFG:
        import build as B
        seminar = seminar or B.seminar_from_cwd()
        if not seminar:
            raise SystemExit("не сказано, какое это занятие: передайте `--seminar NN` "
                             "или запускайте из папки семинара")
        D.configure(seminar, lang)
    doc, slides = build("n", lang)
    text = header_comment(slides, doc["deck"], lang) + yaml.safe_dump(
        doc, allow_unicode=True, sort_keys=False, width=100, default_flow_style=False)
    out = D.ROOT / D.deck_file()
    if check:
        cur = out.read_text(encoding="utf-8") if out.exists() else ""
        print(f"{out.name}: " + ("совпадает с файлом" if cur == text
                                 else "РАСХОДИТСЯ с файлом"))
        return
    out.write_text(text, encoding="utf-8")
    print(f"{out.name}: {doc['deck']['slide_count']} слайдов, "
          f"{doc['deck']['duration_min']} мин при слоте {doc['deck'].get('slot_min')}")


if __name__ == "__main__":
    main()
