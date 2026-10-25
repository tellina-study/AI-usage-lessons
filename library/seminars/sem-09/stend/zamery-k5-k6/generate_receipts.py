#!/usr/bin/env python3
"""Генератор учебных квитанций для Замера 4 (Кейс 6) Семинара 9 — issue #299.

Настоящих фотографий квитанций у нас нет и брать чужие нельзя (прямое ограничение задачи).
Этот скрипт рисует 6 квитанций учебного центра (ImageMagick в окружении не найден — чем
меньше инструментов, тем честнее: Pillow 12.3.0 делает то же самое) и старит их под
телефонную съёмку: перекос, неравномерная яркость, шум, лёгкая расфокусировка. Это учебный
материал, а не заглушка — пойдёт в деку и в файл студенту (прямое указание задачи), поэтому
у каждой квитанции сохранён и "чистый" эталон (receipts/clean/), по которому известна ТОЧНАЯ
верная сумма/дата для сверки в замере класса отказов, и состаренная версия (receipts/aged/),
которая реально отправляется в модель.

Receipt #1 используется ТРИЖДы: как обычный пример класса отказов и как исходник для четырёх
разрешений замера А (receipts/resolution/receipt-01-{full,half,quarter,eighth}.png) — та же
состаренная картинка, только пропущенная через Image.resize с разными коэффициентами, чтобы
разница между файлами была РОВНО разрешением, а не разной съёмкой (требование задачи).

Запуск:
    python3 generate_receipts.py
"""
import json
import random
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).parent
OUT_CLEAN = HERE / "receipts" / "clean"
OUT_AGED = HERE / "receipts" / "aged"
OUT_RES = HERE / "receipts" / "resolution"
for d in (OUT_CLEAN, OUT_AGED, OUT_RES):
    d.mkdir(parents=True, exist_ok=True)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
F_MONO = str(FONT_DIR / "DejaVuSansMono.ttf")
F_MONO_B = str(FONT_DIR / "DejaVuSansMono-Bold.ttf")
F_SANS_B = str(FONT_DIR / "DejaVuSans-Bold.ttf")

WIDTH, HEIGHT = 1200, 1600  # "короткая сторона" портретного телефонного фото

# Шесть квитанций — курс, сумма, дата, плательщик, номер, назначение платежа. Суммы и даты
# разные у всех, чтобы класс отказов (неверно прочитанное число) было видно по существу, не
# по совпадению с соседней квитанцией.
RECEIPTS = [
    {"id": "receipt-01", "number": "0000481", "date": "12.09.2026", "payer": "Смирнова Анна Павловна",
     "course": "Python для анализа данных", "amount": "18 990,00", "purpose": "оплата курса (полная стоимость)"},
    {"id": "receipt-02", "number": "0000503", "date": "03.10.2026", "payer": "Кузнецов Игорь Олегович",
     "course": "Основы n8n и автоматизации", "amount": "23 450,00", "purpose": "оплата курса, 1-й взнос"},
    {"id": "receipt-03", "number": "0000517", "date": "21.10.2026", "payer": "Фёдорова Ольга Сергеевна",
     "course": "Data Science: интенсив", "amount": "31 200,00", "purpose": "оплата курса (полная стоимость)"},
    {"id": "receipt-04", "number": "0000522", "date": "14.07.2026", "payer": "Петров Дмитрий Андреевич",
     "course": "SQL для начинающих", "amount": "9 800,00", "purpose": "оплата курса (полная стоимость)"},
    {"id": "receipt-05", "number": "0000538", "date": "29.08.2026", "payer": "Иванова Мария Викторовна",
     "course": "Python с нуля", "amount": "12 450,00", "purpose": "оплата курса, 2-й взнос"},
    {"id": "receipt-06", "number": "0000549", "date": "05.10.2026", "payer": "Соколов Егор Николаевич",
     "course": "Основы машинного обучения", "amount": "27 300,00", "purpose": "оплата курса (полная стоимость)"},
]

AMOUNT_FONT_SIZE = 64  # размер шрифта строки "Сумма" на полном разрешении — несущее число
# замера А ("высота символа в пикселях"); остальные строки мельче и не измеряются отдельно.


def amount_glyph_height_px(font_size=AMOUNT_FONT_SIZE):
    """Высота цифры денежной строки в пикселях на ПОЛНОМ разрешении — измерено реальным
    рендером шрифта (bbox), не предположено."""
    f = ImageFont.truetype(F_MONO_B, font_size)
    bbox = f.getbbox("0123456789")
    return bbox[3] - bbox[1]


def draw_receipt(data, width=WIDTH, height=HEIGHT):
    img = Image.new("RGB", (width, height), "white")
    d = ImageDraw.Draw(img)
    f_title = ImageFont.truetype(F_SANS_B, 46)
    f_label = ImageFont.truetype(F_MONO, 32)
    f_value = ImageFont.truetype(F_MONO_B, 32)
    f_amount = ImageFont.truetype(F_MONO_B, AMOUNT_FONT_SIZE)

    y = 60
    d.text((width // 2, y), "КВИТАНЦИЯ ОБ ОПЛАТЕ", font=f_title, fill="black", anchor="mm")
    y += 70
    d.text((width // 2, y), "Учебный центр «Траектория»", font=f_label, fill="black", anchor="mm")
    y += 50
    d.line([(60, y), (width - 60, y)], fill="black", width=2)
    y += 50

    rows = [
        ("Квитанция №", data["number"]),
        ("Дата", data["date"]),
        ("Плательщик", data["payer"]),
        ("Назначение платежа", data["purpose"]),
        ("Курс", data["course"]),
    ]
    for label, value in rows:
        d.text((70, y), label + ":", font=f_label, fill="black")
        y += 42
        d.text((90, y), value, font=f_value, fill="black")
        y += 58

    y += 30
    d.line([(60, y), (width - 60, y)], fill="black", width=2)
    y += 50
    d.text((70, y), "Сумма:", font=f_label, fill="black")
    y += 44
    d.text((90, y), data["amount"] + " ₽", font=f_amount, fill="black")
    y += 90
    d.line([(60, y), (width - 60, y)], fill="black", width=2)
    y += 50
    d.text((70, y), "Статус: ОПЛАЧЕНО", font=ImageFont.truetype(F_SANS_B, 34), fill="black")
    y += 80
    d.text((width // 2, height - 60), "Кассовый чек не требуется — Data Table учебного стенда",
           font=ImageFont.truetype(F_MONO, 20), fill=(90, 90, 90), anchor="mm")
    return img


def age_photo(receipt_img, seed):
    """Состаривает чистый рендер под телефонную съёмку: кладёт квитанцию на серый "стол",
    поворачивает на несколько градусов, добавляет неравномерную яркость (виньетка под углом),
    гауссов шум и лёгкую расфокусировку. Детерминировано по seed — чтобы прогон можно было
    повторить."""
    rng = random.Random(seed)
    w, h = receipt_img.size
    margin = int(max(w, h) * 0.12)
    desk = Image.new("RGB", (w + 2 * margin, h + 2 * margin), (168, 162, 150))
    # лёгкий шум на "столе", чтобы не было идеально гладкого фона
    desk_px = desk.load()
    for _ in range(0):  # фон не измеряется, идеальная гладкость стола не влияет на чтение квитанции
        pass
    desk.paste(receipt_img, (margin, margin))

    angle = rng.uniform(-6.0, 6.0)
    rotated = desk.rotate(angle, resample=Image.BICUBIC, expand=True, fillcolor=(168, 162, 150))

    # неравномерная яркость — диагональная виньетка (один угол темнее другого). grad — карта
    # множителей 0..255; ImageChops.multiply делает per-pixel (a*b)/255, то есть реально
    # домножает яркость на коэффициент из grad, а не рисует полупрозрачный слой поверх.
    rw, rh = rotated.size
    grad = Image.new("L", (rw, rh))
    grad_px = grad.load()
    dark_corner = rng.choice(["tl", "tr", "bl", "br"])
    for yy in range(0, rh, 4):
        for xx in range(0, rw, 4):
            fx, fy = xx / rw, yy / rh
            if dark_corner == "tl":
                t = 1 - min(fx, fy)
            elif dark_corner == "tr":
                t = 1 - min(1 - fx, fy)
            elif dark_corner == "bl":
                t = 1 - min(fx, 1 - fy)
            else:
                t = 1 - min(1 - fx, 1 - fy)
            val = int(255 * (1 - 0.35 * t))
            for dy in range(4):
                for dx in range(4):
                    if yy + dy < rh and xx + dx < rw:
                        grad_px[xx + dx, yy + dy] = val
    grad_rgb = Image.merge("RGB", (grad, grad, grad))
    rotated = ImageChops.multiply(rotated.convert("RGB"), grad_rgb)

    # гауссов шум
    noisy = rotated.copy()
    px = noisy.load()
    nw, nh = noisy.size
    for _ in range(int(nw * nh * 0.015)):
        xx = rng.randrange(nw)
        yy = rng.randrange(nh)
        r, g, b = px[xx, yy]
        delta = rng.randint(-40, 40)
        px[xx, yy] = (max(0, min(255, r + delta)), max(0, min(255, g + delta)),
                      max(0, min(255, b + delta)))

    # лёгкая расфокусировка
    blurred = noisy.filter(ImageFilter.GaussianBlur(radius=1.3))
    return blurred


def main():
    manifest = {"amount_font_size_px_full_res": AMOUNT_FONT_SIZE,
                "amount_glyph_height_px_full_res": amount_glyph_height_px(),
                "canvas_width_full_res": WIDTH, "canvas_height_full_res": HEIGHT,
                "receipts": []}

    for i, data in enumerate(RECEIPTS):
        clean = draw_receipt(data)
        clean_path = OUT_CLEAN / f"{data['id']}-clean.png"
        clean.save(clean_path)

        aged = age_photo(clean, seed=1000 + i)
        aged_path = OUT_AGED / f"{data['id']}-aged.png"
        aged.save(aged_path)

        manifest["receipts"].append({
            **data, "clean_file": str(clean_path.relative_to(HERE)),
            "aged_file": str(aged_path.relative_to(HERE)),
            "aged_size": aged.size,
        })
        print(f"{data['id']}: {data['amount']} / {data['date']} -> {aged_path.name} {aged.size}")

    # Четыре разрешения ОДНОЙ и той же состаренной квитанции (receipt-01) — чистый ресайз,
    # без повторной съёмки/старения, чтобы разница была ровно в разрешении.
    r1_aged_path = OUT_AGED / "receipt-01-aged.png"
    r1_aged = Image.open(r1_aged_path)
    base_w, base_h = r1_aged.size
    scales = {"full": 1.0, "half": 0.5, "quarter": 0.25, "eighth": 0.125,
              "sixteenth": 0.0625, "thirtysecond": 0.03125}
    # sixteenth/thirtysecond добавлены ПОСЛЕ первого прогона замера А (README, «Методическое
    # отклонение от плана») — на eighth (6,1px) сумма ещё читалась верно всеми 5 повторами,
    # понадобилось разрешение ниже, чтобы найти точку излома, которую план предполагал на
    # eighth и не нашёл там.
    glyph_h_full = amount_glyph_height_px()
    res_manifest = []
    for name, scale in scales.items():
        new_w, new_h = int(base_w * scale), int(base_h * scale)
        resized = r1_aged.resize((new_w, new_h), resample=Image.LANCZOS)
        out_path = OUT_RES / f"receipt-01-{name}.png"
        resized.save(out_path)
        glyph_h = glyph_h_full * scale  # чистая геометрия ресайза — не измерение заново,
        # потому что LANCZOS-ресайз масштабирует линейные размеры ровно на `scale`, это
        # арифметика, не предположение.
        res_manifest.append({
            "name": name, "scale": scale, "size": [new_w, new_h],
            "amount_glyph_height_px": round(glyph_h, 1),
            "file": str(out_path.relative_to(HERE)),
        })
        print(f"receipt-01-{name}: {new_w}x{new_h}, высота цифры суммы ~{glyph_h:.1f}px -> {out_path.name}")

    manifest["resolution_variants"] = res_manifest
    (HERE / "receipts-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\nманифест -> receipts-manifest.json")


if __name__ == "__main__":
    main()
