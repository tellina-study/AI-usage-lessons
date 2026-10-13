#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Кегль тела каждого кадра деки — замер, а не на слово.

Сборщик ужимает тело молча: `metrics.fit_runs` возвращает МАСШТАБ, при
котором прогон уложился, и ни отчёт, ни снимок не говорят, каким кеглем в
итоге набрано тело. Этот прогон подменяет `fit_runs`/`fit_blocks` на себя,
запоминает выбранный кегль по тегу и печатает таблицу: кадр · кегль тела.
Ничего не собирает заново и ничего не правит — только читает.

    python3 measure_body.py            # все кадры
    python3 measure_body.py s17,s24    # только эти
"""
import sys

import build_lec07 as B
from deckkit import flow, metrics, report, wrap

SEEN = {}

_fit_runs, _fit_blocks = metrics.fit_runs, flow.fit_blocks
_fit_wrap, _fit_push = wrap.fit_runs_wrap, wrap.fit_pushed
WRAPPED, PUSHED = set(), set()


def fit_runs(runs, w, h, **kw):
    k = _fit_runs(runs, w, h, **kw)
    tag = kw.get("tag", "")
    if tag.endswith("/тело"):
        SEEN[tag.split("/")[0]] = max((r.get("size", 0.0) for r in runs),
                                      default=0.0)
    return k


def fit_runs_wrap(runs, *a, **kw):
    """Обтекание: кегль берётся из прогонов ПОСЛЕ подбора, как и у `fit_runs`
    — но тела тут две надписи, и кадр считается один раз, по верхней.
    Без этой подмены замер молча пропускал бы обтекающие кадры."""
    res = _fit_wrap(runs, *a, **kw)
    tag = kw.get("tag", "")
    if res and tag.endswith("/тело"):
        SEEN[tag.split("/")[0]] = max((r.get("size", 0.0) for r in runs),
                                      default=0.0)
        WRAPPED.add(tag.split("/")[0])
    return res


def fit_pushed(runs, *a, **kw):
    """Тело ушло ПОД снимок целиком — вырожденный случай обтекания."""
    k = _fit_push(runs, *a, **kw)
    tag = kw.get("tag", "")
    if k and tag.endswith("/тело"):
        SEEN[tag.split("/")[0]] = max((r.get("size", 0.0) for r in runs),
                                      default=0.0)
        PUSHED.add(tag.split("/")[0])
    return k


def fit_blocks(blocks, w, h, **kw):
    size = _fit_blocks(blocks, w, h, **kw)
    tag = kw.get("tag", "")
    if tag.endswith("/тело"):
        SEEN[tag.split("/")[0]] = size
    return size


metrics.fit_runs = fit_runs
flow.fit_blocks = fit_blocks
wrap.fit_runs_wrap = fit_runs_wrap
wrap.fit_pushed = fit_pushed
B.metrics.fit_runs = fit_runs
B.flow.fit_blocks = fit_blocks
B.wrap.fit_runs_wrap = fit_runs_wrap
B.wrap.fit_pushed = fit_pushed
wrap.fit_pushed = fit_pushed


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    out = B.HERE / "lec-07-zamer.pptx"
    B.build(only=only, out=out)
    rows = sorted(SEEN.items(), key=lambda kv: kv[1])
    print(f"кегль тела, {len(rows)} кадров с телом "
          f"(порог проекции 12 пт, рабочий 15 пт):")
    for sid, pt in rows:
        mark = "  НИЖЕ 12" if pt < 12.0 else ("  ниже 13" if pt < 13.0 else "")
        print(f"  {sid:<6} {pt:5.1f} пт{mark}"
              + ("   (обтекает снимок)" if sid in WRAPPED else
                 "   (тело под снимком)" if sid in PUSHED else ""))
    print(f"ниже 13 пт: {sum(1 for _, p in rows if p < 13.0)} · "
          f"ниже 12 пт: {sum(1 for _, p in rows if p < 12.0)} · "
          f"обтекают снимок: {len(WRAPPED)} ({', '.join(sorted(WRAPPED))}) · "
          f"тело под снимком: {len(PUSHED)} ({', '.join(sorted(PUSHED))})")
    out.unlink(missing_ok=True)
    report.reset()
    return 0


if __name__ == "__main__":
    sys.exit(main())
