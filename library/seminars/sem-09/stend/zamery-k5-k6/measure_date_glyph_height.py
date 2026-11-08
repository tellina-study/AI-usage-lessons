#!/usr/bin/env python3
"""Измеряет высоту символа ПОЛЯ "дата" отдельно от поля "сумма" — issue #299,
починка протечки промта на Кейсе 6 (2026-10-27).

До этого момента дека ПЕРЕИСПОЛЬЗОВАЛА `amount_glyph_height_px` (высоту символа
СУММЫ, кегль 64) как якобы высоту, на которой ломается ДАТА, хотя дата набрана
вдвое мельче (кегль 32, `generate_receipts.py:76` — `f_value = ImageFont.truetype(
F_MONO_B, 32)`) и собственного замера её высоты в протоколе никогда не было (это
честно признано в backup-блоке `n71`). Теперь, когда честный (не утёкший) замер
дал РЕАЛЬНЫЙ порог суммы (0/5 на thirtysecond, 5/5 на sixteenth — т.е. сумма ТОЖЕ
ломается, просто на другом разрешении), старая экономия стала видимой проблемой:
нужно измерить высоту символа даты тем же методом, что и для суммы, а не
предполагать её через пропорцию кеглей.

Метод — ДОСЛОВНО тот же, что `generate_receipts.amount_glyph_height_px`: берём
шрифт `DejaVuSansMono-Bold` нужного кегля, рендерим `"0123456789"`, берём bbox
(`ImageFont.getbbox`), высота = bbox[3] - bbox[1]. Единственная разница — кегль:
32 (дата) вместо 64 (сумма). Это реальный рендер шрифта, не предположение и не
линейная пропорция от числа суммы (bbox не масштабируется идеально линейно
из-за хинтинга/округления шрифта на разных кеглях — отличие от простого деления
49,0 / 2 = 24,5 нужно увидеть, а не постулировать).

Затем те же 6 коэффициентов масштаба, что уже использованы в
`generate_receipts.py` для получения `resolution_variants` (receipts-manifest.json),
применяются к этой высоте — это чистая геометрия того же ресайза (LANCZOS
масштабирует линейные размеры ровно на `scale`), не новое измерение по фото:
новый файл с разрешением уже отресайзенной даты не нужен, потому что высота
символа даты на каждом шаге — просто `date_glyph_height_px_full_res * scale`,
той же арифметикой, что уже применена к сумме в `generate_receipts.py:217`.

Результат дописывается в `receipts-manifest.json` → `resolution_variants[].
date_glyph_height_px` (новое поле, существующее `amount_glyph_height_px` не
трогается).

Запуск:
    python3 measure_date_glyph_height.py
"""
import json
from pathlib import Path

from PIL import ImageFont

import generate_receipts as GR

HERE = Path(__file__).parent
MANIFEST_PATH = HERE / "receipts-manifest.json"

DATE_FONT_SIZE = 32  # generate_receipts.py:76 — f_value для строки "Дата" (и всех
# остальных value-строк, кроме суммы); сумма — 64 (generate_receipts.py:59 AMOUNT_FONT_SIZE).

# Честные результаты (не утёкшие — из results-k6-resolution.json, executions
# 1075-1104) для таблицы в выводе скрипта. Не используются в вычислении высоты
# символа — только для печати сводной таблицы по заданию.
SUM_CORRECT = {"full": "5/5", "half": "5/5", "quarter": "5/5",
               "eighth": "5/5", "sixteenth": "5/5", "thirtysecond": "0/5"}
DATE_CORRECT = {"full": "5/5", "half": "5/5", "quarter": "5/5",
                "eighth": "0/5", "sixteenth": "0/5", "thirtysecond": "0/5"}


def date_glyph_height_px(font_size=DATE_FONT_SIZE):
    """Высота цифры строки "Дата" в пикселях — тот же метод, что
    `generate_receipts.amount_glyph_height_px`, другой кегль."""
    f = ImageFont.truetype(GR.F_MONO_B, font_size)
    bbox = f.getbbox("0123456789")
    return bbox[3] - bbox[1]


def main():
    if not MANIFEST_PATH.exists():
        raise SystemExit(f"не найден {MANIFEST_PATH} — сначала запусти generate_receipts.py")
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    amount_h_full = GR.amount_glyph_height_px()  # 49 — сверка с уже записанным числом
    date_h_full = date_glyph_height_px()

    assert manifest["amount_glyph_height_px_full_res"] == amount_h_full, (
        "высота символа суммы в манифесте разошлась с пересчётом — "
        "generate_receipts.py менялся без пересборки манифеста?")

    rows = []
    for variant in manifest["resolution_variants"]:
        scale = variant["scale"]
        date_h = date_h_full * scale
        variant["date_glyph_height_px"] = round(date_h, 1)
        rows.append((variant["name"], variant["amount_glyph_height_px"], round(date_h, 1)))

    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"высота символа суммы (кегль {GR.AMOUNT_FONT_SIZE}) на полном размере: "
          f"{amount_h_full} px (сверено с receipts-manifest.json)")
    print(f"высота символа даты  (кегль {DATE_FONT_SIZE}) на полном размере: "
          f"{date_h_full} px (новый замер, тем же методом)")
    print()
    header = f"{'разрешение':<14}{'высота суммы, px':<18}{'высота даты, px':<18}" \
             f"{'сумма верна':<13}{'дата верна':<10}"
    print(header)
    print("-" * len(header))
    for name, amount_h, date_h in rows:
        print(f"{name:<14}{amount_h:<18}{date_h:<18}{SUM_CORRECT[name]:<13}{DATE_CORRECT[name]:<10}")

    print(f"\n-> {MANIFEST_PATH} (добавлено поле date_glyph_height_px к каждому "
          f"элементу resolution_variants)")


if __name__ == "__main__":
    main()
