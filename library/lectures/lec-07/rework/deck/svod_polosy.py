#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Свод по полосе ОДНИМ прогоном: вес · запас кегля · пол · описание опыта.

Зачем. Полосу правят пять-шесть исполнителей, и каждый считает свои кадры
сам. Склейка их отчётов даёт число, которого НИКТО НЕ МЕРИЛ: у каждого свой
счётчик, своя граница округления и свой кусок деки. Этот прогон считает всё
по ОДНОМУ собранному PDF и по одному списку кадров.

Он ничего не собирает сам — собирает `render_sec.py`, а блокирующие берутся
отдельной сборкой. Сюда приходит уже готовый PDF, и прогон говорит, какой
именно и когда записан: число с чужого или старого файла — ровно та ошибка,
которую весь круг и ловим.

    python3 render_sec.py 0 1 2 3 4 5        # сначала собрать
    python3 svod_polosy.py sec-0-1-2-3-4-5.pdf [zamer-r5-ves-do.txt]
"""
import re
import statistics as st
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from vidimyy_sloy_polnyy import kadry_polosy          # noqa: E402
import zapas_keglya as zk                             # noqa: E402

POLOSA = ["0. Вход", "1. Первичный", "2. Инструментальная",
          "3. Постановка", "4. Динамическое", "5. Ведение"]
PREDEL = 140


def do_iz(path):
    """Вес ДО правки — из записанного замера, а не из памяти."""
    d = {}
    if path and Path(path).exists():
        for ln in Path(path).read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*(\d+)\s+(s\S+?)\.md", ln)
            if m:
                d[m.group(2).split("-")[0]] = int(m.group(1))
    return d


def main(pdf, do_file=None):
    import pymupdf
    import time
    fs = kadry_polosy(POLOSA)
    ids = [f.stem.split("-")[0] for f in fs]
    d = pymupdf.open(pdf)
    if d.page_count != len(ids):
        print(f"СТОП: в PDF {d.page_count} страниц, в полосе {len(ids)} кадров — "
              "это разные вещи, числа считать нельзя")
        return 1
    # СОВПАДЕНИЯ СЧЁТА НЕ ХВАТАЕТ, и это куплено собственной ошибкой: склеенный
    # из двух кусков PDF (разделы 0-3-5 + 1-2-4) имеет РОВНО столько же страниц,
    # сколько кадров в полосе, и проходит проверку по счёту — а порядок у него
    # другой. Тогда каждое число садится на чужой кадр, и отчёт выглядит
    # нормально: «s20 194 слова» вместо 85. Поэтому сверяем ЗАГОЛОВОК каждой
    # страницы с заголовком её кадра.
    # Сверку порядка делает НЕ этот файл: её умеет `sverka_stranits.py` из
    # приёмки, и умеет лучше — он сравнивает по ДОЛЕ слов заголовка и знает,
    # что у обложки и дивайдеров `title` на экран не выводится вовсе, а
    # заголовок стоит первой строкой тела. Это 7 кадров полосы, которые моя
    # прежняя версия молча пропускала.
    #
    # Зачем тогда сверка здесь. Свод полосы обязан отказываться считать САМ,
    # не дожидаясь приёмки: его зовут посреди работы, когда приёмку ещё не
    # гоняли. Разные роли, не дублирование.
    try:
        import sverka_stranits as ss
        nakhodki, _prochitano = ss.proverit(pdf, fs)
        ploho = [f"стр.{x['stranitsa']} ждали {x['kadr']}" for x in nakhodki]
    except Exception as e:                       # noqa: BLE001
        print(f"СТОП: сверку порядка страниц выполнить не удалось ({e}). "
              "Считать нельзя:\nчисла сядут на чужие кадры, и отчёт будет "
              "выглядеть правдоподобно.")
        return 1
    if ploho:
        print("СТОП: страницы PDF не на своих кадрах — числа сядут на чужих.")
        print("  " + ", ".join(ploho[:8])
              + (f" … всего {len(ploho)}" if len(ploho) > 8 else ""))
        print("  Похоже, PDF склеен из кусков в другом порядке. Соберите одним "
              "прогоном:\n  python3 render_sec.py 0 1 2 3 4 5")
        return 1
    ves = {i: len(d[n].get_text().split()) for n, i in enumerate(ids)}
    zap = {i: t for i, t, _m, _v in
           [(x[0], x[1], x[2], x[3]) for x in zk.po_kadram(pdf, ids)]
           if t is not None}
    svezh = time.strftime("%H:%M:%S", time.localtime(Path(pdf).stat().st_mtime))
    print(f"PDF: {pdf}, записан {svezh}; кадров {len(ids)}")

    do = do_iz(do_file)
    v = list(ves.values())
    print(f"\nВЕС: медиана {st.median(v):g} · среднее {st.mean(v):.0f} · "
          f"максимум {max(v)} · тяжелее {PREDEL} — {sum(1 for x in v if x > PREDEL)}")
    if do:
        ros = [(i, do[i], ves[i]) for i in ids if i in do and ves[i] != do[i]]
        print(f"  изменилось кадров: {len(ros)}; "
              f"выросли {sum(1 for _i, a, b in ros if b > a)}, "
              f"снизились {sum(1 for _i, a, b in ros if b < a)}")

    na_polu = [i for i in zap if abs(zap[i] - zk.POL) < 0.05]
    nizhe = [i for i in zap if zap[i] < zk.POL - 0.05]
    print(f"\nКЕГЛЬ: наименьший по телу {min(zap.values()):.1f} пт (пол {zk.POL:.1f}) · "
          f"ровно на полу {len(na_polu)}"
          + (f" — {', '.join(sorted(na_polu))}" if na_polu else "")
          + f" · ниже пола {len(nizhe)}"
          + (f" — {', '.join(sorted(nizhe))}" if nizhe else ""))

    # Пол объявленный — по файлам кадров, и отдельно те, кто его перевесил.
    bez, perevis = [], []
    for f, i in zip(fs, ids):
        t = f.read_text(encoding="utf-8")
        m = re.search(r"^pol_slov:\s*(\d+)", t, re.M)
        if not m:
            if ves[i] > 75:
                bez.append(f"{i} ({ves[i]})")
        elif ves[i] > int(m.group(1)):
            perevis.append(f"{i} {ves[i]}>{m.group(1)}")
    print(f"\nПОЛ: выше 75 без объявленного — {len(bez)}"
          + (f": {', '.join(bez)}" if bez else "")
          + f" · перевесили свой пол — {len(perevis)}"
          + (f": {', '.join(perevis)}" if perevis else ""))

    r = subprocess.run([sys.executable, "zamer_opisaniya_opyta.py"],
                       cwd=HERE, capture_output=True, text=True)
    moi = set(ids)
    net = [ln.strip() for ln in r.stdout.splitlines()
           if ln.strip().split(" ")[0] in moi and "нет:" in ln]
    print(f"\nОПИСАНИЕ ОПЫТА: кадров полосы без всех трёх частей — {len(net)}")
    for ln in net:
        print("   " + ln)
    print("\nчего этот свод НЕ знает: блокирующие предупреждения (их берут "
          "отдельной сборкой) и\nсквозные сторожа, которым нужна вся дека.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
