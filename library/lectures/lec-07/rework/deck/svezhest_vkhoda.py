#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Свежесть входа и счёт кадров против манифестов — две дешёвые проверки,
каждая ловит целый класс дефектов, и ни одной из них в приёмке не было.

ПЕРВАЯ: СТОРОЖ, ПОСМОТРЕВШИЙ ПРОШЛУЮ ВЕРСИЮ. Канон (`storozha-i-priyomka.md`
§11): «перед тем как верить сторожу — сверить время файлов: `pptx` новее
`pdf` или снимков означает, что сторож смотрел прошлую версию (за
производство Семинара 6 это случилось трижды)». Замер по устаревшему PDF
выглядит как замер: числа есть, они правдоподобны, относятся они к деке,
которой больше нет. Поэтому прогон сравнивает время самого свежего файла
кадра со временем PDF и снимков и падает, а не предупреждает.

ВТОРАЯ: ГЕНЕРАТОР МОЛЧА ВЫБРОСИЛ КАДР. Тот же §11 называет замер
2026-10-14: пять новых кадров описания стадии несли ПРЕЖНЕЕ имя раздела,
генератор манифеста не нашёл для них раздела и не выпустил их записей
вовсе — а манифест выглядел исправным, потому что «НЕ СОПОСТАВЛЕН: 0»
считается по выпущенным записям и выброшенных не видит. Собранная дека при
этом была полной: сборщик читает каталог кадров напрямую. Расходились дека
и её ОПИСАНИЕ, и описание читают все остальные проверки. Канон называет это
долгом и называет лекарство: «счёт файлов кадров на диске против счёта
записей в манифестах — одна строка, ловит весь этот класс».

ПОЧЕМУ СЧЁТ ИДЁТ ПО ОБЪЕДИНЕНИЮ, А НЕ ПО ФАЙЛАМ. Манифестов три, и это
НЕ копии: они делят деку на части (30 + 47 + 22 = 99). Первая версия этой
проверки сравнивала каждый манифест с полным числом кадров и выдала три
ложные тревоги подряд — ровно то, за что сторожей и снимают с довольствия.
Сравнивается объединение идентификаторов, и отдельно печатается,
пересекаются ли части: пересечение означает, что кадр попал в деку дважды.

    python3 svezhest_vkhoda.py
    python3 svezhest_vkhoda.py --pdf lec-07-karkas.pdf
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))

import build_lec07 as B                                      # noqa: E402
from deckkit import slidefile                                # noqa: E402

# Идентификаторы берутся РАЗБОРОМ YAML по ключу `slides`, а не грепом по
# `- id:`. Греп здесь ошибся дважды подряд на одном файле: сначала посчитал
# каждый манифест против полного числа кадров (три ложные тревоги), потом
# подобрал пять записей `D2…D6` из раздела `divergences` — это записанные
# расхождения, а не кадры. Сторож, который кричит на исправной деке, стоит
# ровно столько же, сколько сторож, который молчит на сломанной.


def kadry_na_diske():
    return {f.name.split("-")[0]: f for f in slidefile.slide_files(B.SLIDES_DIR)}


def manifesty():
    """{имя манифеста: [id кадров]} — только список `slides`."""
    import yaml
    out = {}
    for m in sorted(HERE.glob("deck*.yaml")):
        d = yaml.safe_load(m.read_text(encoding="utf-8")) or {}
        spisok = d.get("slides")
        if spisok is None:
            print(f"ОТКАЗ-ПРЕДУПРЕЖДЕНИЕ: в {m.name} нет списка `slides` — "
                  "манифест не того устройства, сверять нечем")
            continue
        out[m.name] = [str(z.get("id")) for z in spisok if isinstance(z, dict)]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default="lec-07-karkas.pdf")
    a = ap.parse_args()

    disk = kadry_na_diske()
    mans = manifesty()
    vsego_zapisey = sum(len(v) for v in mans.values())
    print(f"прочитано: кадров на диске {len(disk)} · манифестов {len(mans)} · "
          f"записей в них {vsego_zapisey}")
    for imya, ids in mans.items():
        print(f"    {imya}: {len(ids)}")
    if not disk:
        print("ОТКАЗ: каталог кадров пуст — сравнивать нечего")
        return 2
    if not mans:
        print("ОТКАЗ: манифестов нет — сравнивать нечего")
        return 2

    zamechaniy = 0

    def g(*a):
        import subprocess
        return subprocess.run(["git", *a], capture_output=True, text=True,
                              cwd=str(HERE)).stdout.strip()

    # ── счёт по объединению
    sojuz = [i for ids in mans.values() for i in ids]
    unik = set(sojuz)
    peresech = len(sojuz) - len(unik)
    net_v_manifestah = sorted(set(disk) - unik)
    net_na_diske = sorted(unik - set(disk))
    print(f"\nкадров в объединении манифестов: {len(unik)} "
          f"(пересечений между частями: {peresech})")
    if peresech:
        zamechaniy += 1
        print("  ЗАМЕЧАНИЕ: кадр попал в деку дважды — части манифеста пересекаются")
    if net_v_manifestah:
        zamechaniy += 1
        print(f"  ЗАМЕЧАНИЕ: на диске есть, в манифестах нет — {net_v_manifestah}")
        print("    это тот самый класс: генератор не нашёл разделу кадра и выбросил его")
    if net_na_diske:
        zamechaniy += 1
        print(f"  ЗАМЕЧАНИЕ: в манифестах есть, на диске нет — {net_na_diske}")
    if not (peresech or net_v_manifestah or net_na_diske):
        print("  дека и её описание совпадают поимённо")

    # ── ВРЕМЯ ЗАПИСИ артефакта против последнего коммита, тронувшего и
    #    кадры, И КОД. Находка сессии добычи, и она закрывает две дыры
    #    сразу. Первая: сборка устаревает не только от правки кадра, но и
    #    от правки `tools/presentation-build/` или `deck/*.py` — отрисовщик
    #    меняет то, что выходит на экран, при неизменных кадрах. Вторая:
    #    время КОММИТА артефакта не равно времени его СБОРКИ. Именно так в
    #    предыдущую сборку попала забракованная версия формы: правка
    #    отрисовщика легла на 78 секунд позже рендера её части, коммит PDF —
    #    ещё позже, и проверка по коммиту молчала.
    posl = g("log", "-1", "--format=%ct %h %ci", "--",
             "slides/", str(HERE.parents[4] / "tools" / "presentation-build"),
             *[str(x) for x in HERE.glob("*.py")])
    if posl:
        ts_kod = int(posl.split()[0])
        opis = " ".join(posl.split()[1:])
        print(f"\nпоследний коммит, тронувший кадры/ядро/прогоны: {opis}")
        for p_art in (HERE / a.pdf, HERE / a.pdf.replace(".pdf", ".pptx")):
            if not p_art.exists():
                print(f"  {p_art.name}: нет")
                continue
            dt = p_art.stat().st_mtime - ts_kod
            if dt < 0:
                zamechaniy += 1
                print(f"  ЗАМЕЧАНИЕ: {p_art.name} записан на {-dt / 60:.0f} мин "
                      "РАНЬШЕ этого коммита — артефакт собран прежним кодом "
                      "либо прежними кадрами, и замеры по нему не о нынешней деке")
            else:
                print(f"  {p_art.name}: записан на {dt / 60:.0f} мин позже — "
                      "собран нынешним кодом и кадрами")
        # Пакет собирается ОТДЕЛЬНОЙ командой: `render_parts.py` полный pptx
        # не обновляет, и прогоны, читающие пакет, обязаны знать его возраст.
        pk = HERE / a.pdf.replace(".pdf", ".pptx")
        pdf_p = HERE / a.pdf
        if pk.exists() and pdf_p.exists():
            raz = (pk.stat().st_mtime - pdf_p.stat().st_mtime) / 60
            print(f"  пакет против PDF: {raz:+.0f} мин "
                  f"({'пакет свежее' if raz >= 0 else 'ПАКЕТ СТАРШЕ PDF'})")
            if raz < 0:
                zamechaniy += 1
                print("    ЗАМЕЧАНИЕ: `render_parts.py` полный pptx НЕ обновляет "
                      "— его собирают отдельной командой; всё, что читает "
                      "пакет (контраст, ссылки, hero), смотрит прошлую версию")

    # ── чем собран PDF: коммит, а не только время файла
    kom = g("log", "-1", "--format=%h %ci", "--", a.pdf)
    if kom:
        sha = kom.split()[0]
        n_posle = len([x for x in g("diff", "--name-only", f"{sha}..HEAD",
                                    "--", "slides/").splitlines() if x.strip()])
        print(f"\nPDF собран коммитом {kom}")
        if n_posle:
            zamechaniy += 1
            print(f"  ЗАМЕЧАНИЕ: после него правлено кадров: {n_posle} — любой "
                  "замер по этому PDF относится к прошлому состоянию деки")
        else:
            print("  кадров после него не правлено")

    # ── свежесть
    nov_kadr = max(f.stat().st_mtime for f in disk.values())
    imya_nov = max(disk.values(), key=lambda f: f.stat().st_mtime).name
    print(f"\nсамый свежий кадр: {imya_nov}")
    proizvodnye = [HERE / a.pdf, HERE / a.pdf.replace(".pdf", ".pptx")]
    proizvodnye += sorted(HERE.glob("png-*/"))[-1:] + sorted(HERE.glob("snaps*/"))[-1:]
    bylo = False
    for p in proizvodnye:
        if not p.exists():
            print(f"  {p.name}: нет")
            continue
        bylo = True
        t = max([p.stat().st_mtime] + [q.stat().st_mtime for q in p.rglob("*")]
                if p.is_dir() else [p.stat().st_mtime])
        otstal = (nov_kadr - t) / 60
        if otstal > 1:
            zamechaniy += 1
            print(f"  ЗАМЕЧАНИЕ: {p.name} отстал от кадров на {otstal:.0f} мин — "
                  "замеры по нему относятся к прошлой версии деки")
        else:
            print(f"  {p.name}: свежее кадров")
    if not bylo:
        print("  производных нет вовсе — мерить собранное нечем")
        zamechaniy += 1

    print(f"\nзамечаний: {zamechaniy}")
    return 1 if zamechaniy else 0


if __name__ == "__main__":
    sys.exit(main())
