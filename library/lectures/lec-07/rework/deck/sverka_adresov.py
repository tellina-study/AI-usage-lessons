#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сверка адресов главы на кадрах деки: существует ли цель, на которую указывает `chapter_ref`.

Отвечает на ОДИН вопрос — разрешается ли адрес. На вопрос «тот ли это параграф по
содержанию» не отвечает и отвечать не может: для этого нужен список переехавших и
переписанных параграфов со стороны главы.

Две ловушки, на которых прогон уже один раз соврал и которые здесь закрыты явно:

1. **Словарь берётся по границам `CHAP`, а не грепом по `'sNN':`.** В `make_deck_yaml.py`
   пять словарей с похожими ключами (`ACQUIRED` держит пути к снимкам), и широкий греп
   подмешивал в адреса `rework/deck/assets/...jpg` — девять ложных «НЕ НАЙДЕН».
2. **Файл в адресе действует до следующего упоминания файла.** Адрес вида
   «`chapter-part1b.md` §1.2, §2.1, `chapter-part2.md` §3.1» относит §3.1 ко ВТОРОМУ
   файлу. Прежняя редакция брала последний файл строки для всех номеров — четыре
   ложных «НЕ НАЙДЕН» на одном `s01b`.

    python3 sverka_adresov.py            # отчёт
    python3 sverka_adresov.py --selftest # доказать, что прогон умеет находить расхождение
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def chap():
    """Адреса ровно из словаря `CHAP`, по его границам."""
    src = (HERE / "make_deck_yaml.py").read_text(encoding="utf-8")
    m = re.search(r"^CHAP\s*=\s*\{(.*?)^\}", src, re.S | re.M)
    if not m:
        raise SystemExit("CHAP не найден — изменилось устройство генератора")
    return dict(re.findall(r"'(s[0-9a-z]+)'\s*:\s*'([^']*)'", m.group(1)))


def chapter_index():
    """По каждой части главы: заголовки и объявленные номера параграфов."""
    heads, nums = {}, {}
    for p in sorted(ROOT.glob("chapter*.md")):
        t = p.read_text(encoding="utf-8")
        heads[p.name] = [h.strip() for h in re.findall(r"^#{1,6}\s+(.+?)\s*$", t, re.M)]
        # ТОЛЬКО заголовки. Номер, УПОМЯНУТЫЙ в прозе («см. § 9.9»), параграф не определяет:
        # §9.9 определён в chapter-part4f.md, а в chapter-part4e.md лишь назван ссылкой — и
        # адрес `part4e §9.9` разрешался МОЛЧА, пока номера собирались по всему тексту.
        nums[p.name] = set(re.findall(r"^#{1,6}\s*§?\s*([0-9]+(?:\.[0-9]+)?[а-я]?)\b", t, re.M))
    return heads, nums


TOKEN = re.compile(r"([a-z0-9_\-/]*\.md)|§\s*([0-9]+(?:\.[0-9]+)?[а-я]?)|§\s+([^§+,]{4,70})")


def targets(ref):
    """Цели адреса как `(файл, вид, значение)`; файл действует до следующего упоминания."""
    out, cur = [], None
    for m in TOKEN.finditer(ref):
        fn, num, name = m.group(1), m.group(2), m.group(3)
        if fn:
            # контекст задаёт любой .md: после «research/07-….md» идут параграфы
            # ИССЛЕДОВАНИЯ, и приписывать их главе нельзя
            cur = fn if re.match(r"chapter[0-9a-z\-]*\.md$", fn.split("/")[-1]) else None
        elif num:
            out.append((cur, "номер", num))
        elif name:
            # «§ Вопросы и ответы для самопроверки (+ chapter-part5b.md §12.4)»: «+» стоит
            # ВНУТРИ скобки, и открывающая скобка попадала в имя заголовка — ложный «нет».
            out.append((cur, "заголовок",
                        name.strip().rstrip("(").rstrip(".,;—- ").strip()))
    return out


def resolve(tgt, heads, nums):
    fn, kind, val = tgt
    if fn is None:
        return "не адрес главы"  # цель относится к исследованию или файл не назван
    if fn not in heads:
        return "ФАЙЛА НЕТ"
    if kind == "номер":
        return "ок" if val in nums[fn] else "НОМЕРА НЕТ"
    # Скобка в адресе — НОТАЦИЯ словаря, а не часть заголовка: «§ Раздел 1 (вводка)»
    # значит «вводная часть Раздела 1», а заголовок в главе — «## Раздел 1. <название>».
    # Слова «вводка» в главе нет ни разу; матчить надо по стволу до скобки.
    stem = re.sub(r"\s*\([^)]*\)\s*$", "", val).strip().rstrip(":.,;—-").strip()
    for cand in (val, stem):
        low = cand.lower()
        if any(low in h.lower() for h in heads[fn]):
            return "ок"
        # «Раздел 1» против «## Раздел 1. Первичный скрининг…» — префиксное совпадение
        if any(h.lower().startswith(low) for h in heads[fn]):
            return "ок"
    return "ЗАГОЛОВКА НЕТ"


def selftest():
    heads = {"chapter.md": ["§1.1 Настоящий заголовок"]}
    nums = {"chapter.md": {"1.1"}}
    cases = [
        ("chapter.md §1.1", "ок", "существующий номер"),
        ("chapter.md §9.9", "НОМЕРА НЕТ", "номер, которого нет"),
        ("chapter-nope.md §1.1", "ФАЙЛА НЕТ", "файл, которого нет"),
        ("chapter.md § Настоящий заголовок", "ок", "существующий заголовок"),
        ("chapter.md § Выдуманный заголовок", "ЗАГОЛОВКА НЕТ", "заголовок, которого нет"),
    ]
    bad = 0
    for ref, want, why in cases:
        got = [resolve(t, heads, nums) for t in targets(ref)]
        ok = want in got
        print(f"  {'ок ' if ok else 'СБОЙ'} {why:34s} {ref:40s} → {got}")
        bad += not ok
    # вторая ловушка: файл действует до следующего упоминания
    # нотация со скобкой разрешается по стволу
    h2 = {"chapter.md": ["Раздел 1. Первичный скрининг и отбор"]}
    n2 = {"chapter.md": set()}
    for ref, want, why in (("chapter.md § Раздел 1 (вводка)", "ок", "нотация «(вводка)» по стволу"),
                           ("chapter.md § Раздел 9 (вводка)", "ЗАГОЛОВКА НЕТ", "ствол, которого нет")):
        got = [resolve(x, h2, n2) for x in targets(ref)]
        ok = want in got
        print(f"  {'ок ' if ok else 'СБОЙ'} {why:34s} {ref:40s} → {got}")
        bad += not ok
    t4 = targets("chapter-part5.md §10.10 — источник кадра rework/research/07-x.md §1.1")
    ok4 = [x for x in t4 if x[2] == "1.1"] and [x for x in t4 if x[2] == "1.1"][0][0] is None
    print(f"  {'ок ' if ok4 else 'СБОЙ'} {'§ после файла исследования — не главе':34s} → {t4}")
    bad += not ok4
    t2 = targets("chapter-a.md §1.2, chapter-b.md §3.1")
    ok2 = t2 == [("chapter-a.md", "номер", "1.2"), ("chapter-b.md", "номер", "3.1")]
    print(f"  {'ок ' if ok2 else 'СБОЙ'} номер относится к своему файлу      → {t2}")
    bad += not ok2
    print(f"\nсамотест: сбоев {bad}")
    return 1 if bad else 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
    sys.path.insert(0, str(next(d / "tools" / "presentation-build" for d in HERE.parents
                           if (d / "tools" / "presentation-build").exists())))
    from deckkit import slidefile
    import yaml
    live = []
    for f in slidefile.slide_files(HERE / "slides"):
        m = re.match(r"^---\n(.*?)\n---", f.read_text(encoding="utf-8"), re.S)
        live.append((yaml.safe_load(m.group(1)) or {}).get("id"))
    C, (heads, nums) = chap(), chapter_index()
    checked = miss = 0
    rows = []
    for sid in live:
        ref = C.get(sid)
        if ref is None:
            rows.append((sid, "—", [("—", "адреса нет в CHAP", "НЕТ АДРЕСА")]))
            miss += 1
            continue
        checked += 1
        bad = [(t[0], f"{t[1]} {t[2]}", r)
               for t in targets(ref)
               if (r := resolve(t, heads, nums)) not in ("ок", "не адрес главы")]
        if bad:
            rows.append((sid, ref, bad))
            miss += 1
    print(f"частей главы {len(heads)} · адресов в CHAP {len(C)} · живых кадров {len(live)}")
    print(f"проверено адресов {checked} · кадров с нерешаемой целью {miss}\n")
    for sid, ref, bad in rows:
        print(f"  {sid:7s} {ref[:96]}")
        for fn, what, st in bad:
            print(f"          → {str(fn):22s} {what[:56]:58s} {st}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
