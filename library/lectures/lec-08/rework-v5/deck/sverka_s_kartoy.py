#!/usr/bin/env python3
"""Сверка файлов кадров с картой деки: состав, порядок, минуты, пласты.

Карта (DECK-KARTA*.md) владеет составом, порядком, типом, минутой и пластом.
Файл кадра владеет формулировкой заголовка (решение от 2026-10-27, §10 карты).
Поэтому заголовки здесь НЕ сверяются — сверяется всё остальное.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SLIDES = ROOT / "slides"

KARTA = ROOT / "DECK-KARTA.md"


def read_norms():
    """Нормы берутся ИЗ карты, а не вписываются руками.

    Вписанная руками норма — это шестой шанс ошибиться в арифметике; пять
    предыдущих ошибок в этой лекции нашли агенты, а не я.
    """
    rows = {}
    for line in KARTA.read_text().splitlines():
        m = re.match(r"\|\s*([0-7])\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*([\d,]+)\s*\|", line)
        if m:
            key, label, cnt, mins = m.groups()
            rows[key] = (label, int(cnt), float(mins.replace(",", ".")))
    return rows


def load():
    out = {}
    for f in sorted(SLIDES.glob("s*.md")):
        m = re.match(r"s(\d{2})-", f.name)
        if not m:
            continue
        text = f.read_text()
        fm = text.split("---", 2)
        if len(fm) < 3:
            print(f"ОШИБКА {f.name}: нет frontmatter")
            continue
        try:
            data = yaml.safe_load(fm[1])
        except Exception as e:
            print(f"ОШИБКА {f.name}: frontmatter не разбирается — {e}")
            continue
        out[int(m.group(1))] = (f.name, data, text)
    return out


def main():
    SECTIONS = read_norms()
    frames = load()
    nums = sorted(frames)
    print(f"Файлов кадров: {len(frames)}")

    missing = [n for n in range(1, 98) if n not in frames]
    extra = [n for n in nums if n > 97]
    if missing:
        print(f"ПРОПУЩЕНЫ номера: {missing}")
    if extra:
        print(f"ЛИШНИЕ номера: {extra}")

    # минуты по разделам
    per_sec = {}
    total = 0.0
    strict = 0.0
    for n in nums:
        name, d, _ = frames[n]
        t = float(d.get("timing_min") or 0)
        total += t
        if d.get("in_bucket"):
            strict += t
        sec = str(d.get("section", "")).strip()[:1]
        per_sec.setdefault(sec, [0, 0.0])
        per_sec[sec][0] += 1
        per_sec[sec][1] += t

    print(f"\nВсего минут: {total:.1f} (норма 88,0)")
    print(f"Провалы и ограничения: {strict:.1f} мин = {strict / total * 100:.1f} % (порог 30 %)")

    print("\nРаздел                 кадров/норма   минут/норма")
    ok = True
    for key, (label, n_norm, m_norm) in SECTIONS.items():
        cnt, mins = per_sec.get(key, [0, 0.0])
        flag_c = "" if cnt == n_norm else "  ← РАСХОЖДЕНИЕ"
        flag_m = "" if abs(mins - m_norm) < 0.05 else "  ← РАСХОЖДЕНИЕ"
        if flag_c or flag_m:
            ok = False
        print(f"{label:<22} {cnt:>3}/{n_norm:<3}        {mins:>5.1f}/{m_norm:<5.1f}{flag_c}{flag_m}")

    # Карта вечера опознаётся по дословным подписям строк (BRIEF-DEKA §12).
    # Не по типу кадра: в деке есть и другие сетки (s16 — два семейства
    # генерации), и считать их предъявлениями карты было бы враньём.
    CANON_ROWS = [
        "Породить первое приближение",
        "Довести до производственного качества",
        "Восстановить существующее",
        "Соблюсти точные величины",
        "Уложиться в бюджет реального времени",
        "Ответить «кто отвечает»",
    ]
    karta_frames, row_defects = [], []
    for n in nums:
        whole = frames[n][2]
        present = [r for r in CANON_ROWS if r in whole]
        if len(present) >= 4:
            karta_frames.append(n)
            missing_rows = [r for r in CANON_ROWS if r not in whole]
            if missing_rows:
                row_defects.append((n, missing_rows))
    refren = sum(1 for n in nums if "токенизатор" in frames[n][2].lower())
    print(f"\nКарта вечера предъявлена: {len(karta_frames)} раз (норма 6) — кадры {karta_frames}")
    for n, miss in row_defects:
        print(f"   s{n:02d}: подписи строк неполны, нет — {miss}")
    print(f"Рефрен про токенизатор: {refren} кадров (норма ≥4)")

    # внутренние имена файлов в source — дефект 1
    leak = [n for n in nums if re.search(
        r"chapter[-\w]*\.md|PLAN-[0-9]|REESTR|DECK-KARTA|BRIEF-DEKA|research/R[0-9]",
        str(frames[n][1].get("source", "")))]
    print(f"\nsource с внутренним именем файла: {len(leak)} кадров {leak if leak else ''}")

    return 0 if ok and not missing and not leak \
        and len(karta_frames) == 6 and not row_defects else 1


if __name__ == "__main__":
    sys.exit(main())
