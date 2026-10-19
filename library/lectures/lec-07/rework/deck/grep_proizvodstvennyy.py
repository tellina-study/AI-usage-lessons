#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Производственный язык и методические оговорки на кадре — греп по §11.6,
§6.3 и §7.1 `tools/presentation-build/trebovaniya-k-soderzhaniyu-forma.md`.

ПОЧЕМУ PYTHON, А НЕ `grep -P`. Замерено производством Семинара 6
(`tools/seminar-production/README.md` §8.6): `grep -P` по кириллице даёт
НОЛЬ там, где совпадения есть, потому что `\\b`/`\\w` в PCRE здесь считают по
байтам. Ложный ноль выглядит как подтверждение чистоты — и один раз уже был
за него принят. Модуль `re` Питона считает по символам, поэтому греп живёт
здесь.

ЧТО СКАНИРУЕТСЯ — ОБА СЛОЯ. Видимый текст кадра И заметки лектора:
прошлый круг показал, что снятое с кадра утекает в заметки, а заметки
владелец читает (§6.3, §11.6). Фронтматтер не сканируется: там живут
`pol_slov`, `razbor_part` и прочая бухгалтерия сборки, которую зал не видит.

    python3 grep_proizvodstvennyy.py                 # весь раздел 1
    python3 grep_proizvodstvennyy.py s16 s18         # отдельные кадры
    python3 grep_proizvodstvennyy.py --selftest      # проверить сам греп
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLIDES = HERE / "slides"

# Раздел по умолчанию. Кадры называются по своему `id`, порядок — показа.
RAZDEL_1 = ["s11", "s11a", "s12", "s13", "s13a", "s13b", "s15", "s15a",
            "s16", "s16a", "s18", "s18a", "s18b", "s20"]

# ── §11.6 — расширенный список производственного языка ──────────────────
# Каждый шаблон якорится С ОБЕИХ СТОРОН там, где это возможно: односторонний
# якорь `[Рр]ол[ьияею]\b` находил «роля» внутри «контроля» (§8.6, пять ложных
# срабатываний за одно производство).
SHABLONY = [
    # §11.6, дословно из канона
    (r"[Ии]мени\s+\S+\s+не\s+(получил|назвал|называет|печатает)", "§11.6 «Имени … не получила»"),
    (r"[Пп]рибор\s+\S+\s+не\s+назван", "§11.6 «Прибор … не назван»"),
    (r"кадром\s+(следом|раньше|перед\s+этим)", "§11.6 «кадром следом»"),
    (r"\bкадр[еа]\s+(перед\s+этим|следом)", "§11.6 «на кадре перед этим»"),
    (r"[Рр]аздел\s+(берёт|закрыл|закрывает)", "§11.6 «Раздел берёт/закрыл»"),
    (r"подмножеств\w*", "§11.6 «подмножество»"),
    (r"\bразряд\w*", "§11.6/§6.3 «разряд»"),
    (r"\bсвод\b", "§11.6 «свод»"),
    (r"по\s+этой\s+паре", "§11.6 «по этой паре»"),
    (r"\(опционально\)", "§11.6 «(опционально)»"),
    (r"та\s+же\s+работ\w+", "§11.6 «та же работой»"),
    (r"\bдостроить\b", "§11.6 «достроить»"),
    # §6.3 — протечки процесса
    (r"\bрычаг\w*", "§6.3 «рычаг»"),
    (r"несущ\w+\s+ос[ьи]", "§6.3 «несущая ось»"),
    (r"вклад\s*№", "§6.3 «вклад №»"),
    (r"по\s+постановке", "§6.3 «по постановке»"),
    (r"см\.\s*разбор", "§6.3 «см. разбор»"),
    (r"(?<![A-Za-zА-Яа-я0-9])s\d{1,3}[a-z]?(?![A-Za-zА-Яа-я0-9])", "§6.3 имя нашего кадра"),
    (r"chapter-part\w*|research/\d|research\s*#\d|rework/", "§11.5 самоссылка на репозиторий"),
    # §7.1 — методические оговорки о том, как устроен наш замер
    (r"[Дд]ругое\s+измерение", "§7.1 оговорка о замере"),
    (r"в\s+одну\s+бухгалтерию", "§7.1 оговорка о замере"),
    (r"не\s+одна\s+шкала|одна\s+шкала", "§7.1 оговорка о замере"),
    (r"взят[ыа]?\s+с\s+разных\s+программ", "§7.1 оговорка о замере"),
    (r"разные\s+величины\s+в\s+двух\s+валютах", "§7.1 оговорка о замере"),
    (r"не\s+складыва\w+", "§7.1 оговорка о замере"),
    (r"значимости\s+не\s+достигла|оценка\s+регистратора", "§7.1 оговорка о замере"),
    (r"[Сс]мешанн\w+|частично-?bucket", "§7.1 оговорка о нашей разметке"),
    # § No Timing / No Methodology — те же два разряда, что уже ENFORCED
    (r"(методическ|педагогическ)\w*", "§ No Methodology"),
    (r"\b\d+\s*мин(ут\w*)?\b", "§ No Timing"),
    (r"Лектору|Преподавателю|Вы\s+здесь", "§ No Methodology"),
]
SKOMPILIROVANO = [(re.compile(p), p, imya) for p, imya in SHABLONY]


def sloi(put):
    """Видимый текст и заметки кадра — фронтматтер отрезан."""
    t = put.read_text(encoding="utf-8")
    t = re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S)
    telo, _, zametki = t.partition("## Заметки лектора")
    telo = telo.replace("## Видимый текст слайда", "")
    return telo, zametki


def skan(put, tiho=False):
    telo, zametki = sloi(put)
    naydeno = []
    for sloy, tekst in (("тело", telo), ("заметки", zametki)):
        for rx, shablon, imya in SKOMPILIROVANO:
            for m in rx.finditer(tekst):
                levo = max(0, m.start() - 34)
                kontekst = " ".join(tekst[levo:m.end() + 34].split())
                naydeno.append((sloy, imya, m.group(0), kontekst))
    if naydeno and not tiho:
        print(f"\n{put.name} — {len(naydeno)}")
        for sloy, imya, chto, kontekst in naydeno:
            print(f"  [{sloy:8}] {imya:34} «{chto}»")
            print(f"             …{kontekst}…")
    return naydeno


def selftest():
    """Греп обязан найти то, что мы сами подложили, и не найти соседнее.

    Отдельно проверяется ложное срабатывание односторонних якорей: «контроля»
    и «показал» не должны ловиться шаблонами «роль» и «разряд» (§8.6).
    """
    proba = (
        "## Видимый текст слайда\n\n"
        "Имени система не получила; прибор испытания не назван. "
        "Арбитраж — кадром следом, разряд выше слов участника, "
        "по этой паре видно. 14 минут на раздел, методически важно.\n\n"
        "## Заметки лектора\n\n"
        "Здесь чисто: контроля достаточно, показал зал, парадигма не в счёт.\n"
    )
    put = Path("/tmp/_proba_grep.md")
    put.write_text(proba, encoding="utf-8")
    naydeno = skan(put, tiho=True)
    telo = [n for n in naydeno if n[0] == "тело"]
    zam = [n for n in naydeno if n[0] == "заметки"]
    ok = len(telo) >= 7 and len(zam) == 0
    print(f"selftest: в подложенном теле найдено {len(telo)} (ждём ≥7), "
          f"в чистых заметках {len(zam)} (ждём 0)")
    for _, imya, chto, _ in telo:
        print(f"  тело: {imya} — «{chto}»")
    for _, imya, chto, k in zam:
        print(f"  ЛОЖНОЕ СРАБАТЫВАНИЕ в заметках: {imya} — «{chto}» …{k}…")
    print("selftest ПРОШЁЛ — нулю этого грепа можно верить" if ok
          else "selftest ПРОВАЛЕН — нулю этого грепа верить НЕЛЬЗЯ")
    put.unlink()
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kadry", nargs="*", help="id кадров; пусто — весь раздел 1")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    nuzhny = a.kadry or RAZDEL_1
    vsego = 0
    for sid in nuzhny:
        fayly = sorted(SLIDES.glob(f"{sid}-*.md"))
        if not fayly:
            print(f"{sid}: файла нет")
            continue
        for f in fayly:
            vsego += len(skan(f))
    print(f"\nкадров {len(nuzhny)} · совпадений {vsego} · "
          f"шаблонов {len(SHABLONY)} (Python re, не grep -P)")
    if vsego == 0:
        print("ЧИСТО на обоих слоях — теле и заметках.")
    return 1 if vsego else 0


if __name__ == "__main__":
    sys.exit(main())
