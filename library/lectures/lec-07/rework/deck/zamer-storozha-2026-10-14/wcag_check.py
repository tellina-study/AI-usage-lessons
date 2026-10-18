# -*- coding: utf-8 -*-
"""Независимая сверка формулы WCAG 2.x на пяти парах палитры курса."""
def lin(c):
    c /= 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
def L(h):
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)
def ratio(a, b):
    la, lb = L(a), L(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)
PAIRS = (("F0AB00", "FFFFFF", 1.99), ("028090", "FFFFFF", 4.67),
         ("1C7293", "FFFFFF", 5.42), ("21295C", "FFFFFF", 13.67),
         ("F0AB00", "21295C", 6.85))
for fg, bg, want in PAIRS:
    got = ratio(fg, bg)
    print(f"{fg} на {bg}: мой счёт {got:.4f} (округл. {got:.2f}) · "
          f"заказчик {want:.2f} · расхождение {abs(got - want):.4f}")
# поиск серой пары, у которой контраст МАКСИМАЛЬНО близок к ровно 3,0 и 4,5
for thr in (3.0, 4.5):
    best = min(((abs(ratio(f'{a:02X}'*3, f'{b:02X}'*3) - thr), a, b)
                for a in range(256) for b in range(256) if a != b),
               key=lambda t: t[0])
    d, a, b = best
    print(f"ближайшая серая пара к ровно {thr}: #{a:02X}{a:02X}{a:02X} на "
          f"#{b:02X}{b:02X}{b:02X} → {ratio(f'{a:02X}'*3, f'{b:02X}'*3):.6f} "
          f"(отклонение {d:.2e})")
