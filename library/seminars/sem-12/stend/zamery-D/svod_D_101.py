#!/usr/bin/env python3
"""Свод замера D на корпусе-101: recall@1 по классу и ветке, с базами.

База случайного угадывания пересчитана: было 1/40 = 0,025 при сорока кандидатах,
стало 1/101 = 0,0099 при ста одном. Все отношения «во сколько раз выше базы»
пересчитываются отсюда, а не переносятся из круга 1.

Двусмысленный запрос (3.13 — после расширения корпуса у него появился второй
верный ответ) ИСКЛЮЧЁН из головных чисел; число исключённых печатается.

Запуск:  python3 svod_D_101.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"
CLASSES = {1: "К-слово", 2: "К-пересказ", 3: "К-деталь"}


def load_rows(path, lang=None):
    d = json.loads(path.read_text(encoding="utf-8"))
    return d[lang]["details"] if lang else d["details"]


def recall(rows, drop, cls=None, k=1):
    key = "correct_at_1" if k == 1 else "correct_at_3"
    rs = [r for r in rows if r["num"] not in drop and (cls is None or r["class"] == cls)]
    if not rs:
        return None, 0
    return sum(bool(r[key]) for r in rs) / len(rs), len(rs)


def main():
    qdoc = json.loads((HERE / "zaprosy_101.json").read_text(encoding="utf-8"))
    drop = set(qdoc.get("ambiguous", {}))
    n_corpus = 101
    base = 1 / n_corpus

    branches = [
        ("1. Слова (pymorphy3, обратный индекс)", load_rows(RAW / "branch1_results_101.json")),
        ("2. Смысл (text-embedding-3-small)", load_rows(RAW / "branch2_results_101.json")),
        ("3. Картинка EN (siglip-base-patch16-224)", load_rows(RAW / "branch3_results_101.json", "EN")),
        ("3. Картинка RU (тот же вектор, запрос по-русски)", load_rows(RAW / "branch3_results_101.json", "RU")),
    ]
    h = json.loads((RAW / "branch4_results_101.json").read_text(encoding="utf-8"))
    for k in h:
        if isinstance(h[k], dict) and "details" in h[k]:
            branches.append((f"4. Гибрид {k}", h[k]["details"]))

    print(f"корпус: {n_corpus} снимков · запросов 100, исключено двусмысленных "
          f"{len(drop)} ({', '.join(sorted(drop)) or '—'}) → СЧИТАЕТСЯ {100 - len(drop)}")
    print(f"база случайного угадывания: 1/{n_corpus} = {base:.4f}  "
          f"(в круге 1 было 1/40 = {1/40:.4f} — база изменилась, выводы «во сколько раз выше» пересчитаны)")
    print()
    cols = " | ".join(f"{CLASSES[c]:>11s}" for c in (1, 2, 3))
    print(f"{'ветка':52s} | {cols} | {'итого':>11s}")
    print("-" * 110)
    print(f"{'Случайное угадывание (1/101)':52s} | " +
          " | ".join(f"{base:11.3f}" for _ in (1, 2, 3)) + f" | {base:11.3f}")
    for name, rows in branches:
        cells = []
        for c in (1, 2, 3):
            r, n = recall(rows, drop, c)
            cells.append(f"{r:.3f} ({n:2d})")
        tot, ntot = recall(rows, drop)
        print(f"{name:52s} | " + " | ".join(f"{c:>11s}" for c in cells) + f" | {tot:.3f} ({ntot:2d})")

    print()
    print("=== Цена языка (ветка 3): EN против RU, recall@1 ===")
    en = load_rows(RAW / "branch3_results_101.json", "EN")
    ru = load_rows(RAW / "branch3_results_101.json", "RU")
    print(f"{'класс':14s} {'EN':>8s} {'RU':>8s} {'разница':>9s}")
    for c in (1, 2, 3):
        e, _ = recall(en, drop, c); r, _ = recall(ru, drop, c)
        print(f"{CLASSES[c]:14s} {e:8.3f} {r:8.3f} {e-r:+9.3f}")
    e, _ = recall(en, drop); r, _ = recall(ru, drop)
    print(f"{'ИТОГО':14s} {e:8.3f} {r:8.3f} {e-r:+9.3f}")

    print()
    print("=== recall@3 (та же выборка) ===")
    for name, rows in branches:
        t3, n = recall(rows, drop, k=3)
        t1, _ = recall(rows, drop, k=1)
        print(f"  {name:52s} @1 {t1:.3f}  @3 {t3:.3f}")


if __name__ == "__main__":
    main()
