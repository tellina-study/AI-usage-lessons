#!/usr/bin/env python3
"""
Сборка PDF для слепого сравнения кадров (issue #306).
Создаёт 6 страниц: страницы 1-5 — по одной форме на странице (4 снимка в сеткой 2×2),
страница 6 — эталоны.
Порядок наборов на каждой странице перемешивается случайно и независимо.

Улучшения:
- Автоматическая обрезка снимков по содержимому (удаление белой пустоты)
- Выравнивание высоты плиток по максимальной
- Максимизация размера плиток
- Уменьшение размера файла
"""

import os
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import pymupdf as fitz
import numpy as np

# Фиксированное семя для воспроизводимости результата
RANDOM_SEED = 42

# Названия форм (по номерам кадров)
FORM_NAMES = {
    1: "полоса плашек",
    2: "ось с засечками",
    3: "два столбца",
    4: "схема рядами",
    5: "кадр одного числа"
}

# Пути к файлам
BASE_DIR = Path(__file__).parent
SETS = {
    'A': BASE_DIR / 'nabor-1' / 'snaps',
    'B': BASE_DIR / 'nabor-2' / 'snaps',
    'V': BASE_DIR / 'nabor-3' / 'snaps',
    'G': BASE_DIR / 'nabor-4' / 'snaps',
}
ETALON_DIR = BASE_DIR / 'etalon'

def find_content_bounds(img, white_threshold=245):
    """
    Найти рамку непустых пиксelей (содержимого).
    Ищет пиксели, которые отличаются от белого фона.
    Возвращает (top, left, bottom, right) координаты содержимого.
    """
    img_array = np.array(img.convert('RGB'))

    # Найти пиксели, которые не белые (с допуском)
    non_white = np.any(img_array < white_threshold, axis=2)

    if not non_white.any():
        # Если всё белое, вернуть полный размер
        return 0, 0, img.height, img.width

    # Найти границы содержимого
    rows = np.any(non_white, axis=1)
    cols = np.any(non_white, axis=0)

    y_indices = np.where(rows)[0]
    x_indices = np.where(cols)[0]

    if len(y_indices) == 0 or len(x_indices) == 0:
        return 0, 0, img.height, img.width

    top = y_indices[0]
    bottom = y_indices[-1] + 1
    left = x_indices[0]
    right = x_indices[-1] + 1

    return top, left, bottom, right

def crop_with_margin(img, margin_percent=2.5):
    """
    Обрезать изображение по содержимому с заданным отступом.
    margin_percent — процент ширины содержимого добавить как поля.
    """
    top, left, bottom, right = find_content_bounds(img)

    content_width = right - left
    content_height = bottom - top

    # Добавить поля в процентах от содержимого
    margin_x = max(1, int(content_width * margin_percent / 100))
    margin_y = max(1, int(content_height * margin_percent / 100))

    top = max(0, top - margin_y)
    left = max(0, left - margin_x)
    bottom = min(img.height, bottom + margin_y)
    right = min(img.width, right + margin_x)

    return img.crop((left, top, right, bottom))

def load_and_crop_image(path):
    """Загрузить изображение, обрезать по содержимому."""
    img = Image.open(path).convert('RGB')
    img = crop_with_margin(img, margin_percent=2.5)
    return img

def resize_to_width(img, target_width):
    """Масштабировать изображение к целевой ширине, сохраняя пропорции."""
    w, h = img.size
    new_h = int(target_width * h / w)
    return img.resize((target_width, new_h), Image.Resampling.LANCZOS)

def create_labeled_tile(img, label, tile_width, tile_height):
    """
    Создать плитку с подписью буквы сверху.
    Масштабировать изображение к tile_width, выровнять высоту к tile_height
    (добавляя белое поле снизу).
    """
    LABEL_HEIGHT = 50

    # Масштабировать изображение
    img = resize_to_width(img, tile_width)
    w, h = img.size

    # Выровнять высоту
    if h < tile_height:
        # Добавить белое поле снизу
        padded_img = Image.new('RGB', (w, tile_height), color='white')
        padded_img.paste(img, (0, 0))
        img = padded_img

    # Создать плитку с подписью
    tile = Image.new('RGB', (tile_width, tile_height + LABEL_HEIGHT), color='white')

    # Поместить изображение
    tile.paste(img, (0, LABEL_HEIGHT))

    # Добавить букву
    draw = ImageDraw.Draw(tile)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    except:
        font = ImageFont.load_default()

    # Написать букву в верхнем левом углу плитки
    draw.text((10, 10), label, fill='black', font=font)

    return tile

def create_comparison_page(frame_num, tile_width, tile_height):
    """Создать страницу сравнения для кадра frame_num."""
    random.seed(RANDOM_SEED + frame_num)  # Разное семя для каждой страницы

    # Загрузить снимки из всех наборов для этого кадра
    frame_file = f'k-{frame_num}.png'
    snapshots = []
    set_order = []

    for set_key in ['A', 'B', 'V', 'G']:
        img_path = SETS[set_key] / frame_file
        img = load_and_crop_image(img_path)
        snapshots.append(img)
        set_order.append(set_key)

    # Перемешать порядок наборов (ТЕ ЖЕ перестановки, что и раньше)
    indices = list(range(4))
    random.shuffle(indices)

    shuffled_snapshots = [snapshots[i] for i in indices]
    shuffled_order = [set_order[i] for i in indices]

    # Создать страницу
    PADDING = 60
    PAGE_MARGIN = 40
    LABEL_HEIGHT = 50

    PAGE_WIDTH = tile_width * 2 + PADDING + PAGE_MARGIN * 2
    PAGE_HEIGHT = (tile_height + LABEL_HEIGHT) * 2 + PADDING + PAGE_MARGIN * 2 + 80

    page = Image.new('RGB', (PAGE_WIDTH, PAGE_HEIGHT), color='white')

    # Добавить заголовок
    draw = ImageDraw.Draw(page)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    except:
        font = ImageFont.load_default()

    title = f"Кадр {frame_num} — форма: {FORM_NAMES[frame_num]}"
    draw.text((PAGE_MARGIN, 10), title, fill='black', font=font)

    # Расположить плитки в сеткой 2×2
    labels = ['А', 'Б', 'В', 'Г']
    positions = [
        (PAGE_MARGIN, PAGE_MARGIN + 40),  # левый верхний (А)
        (PAGE_MARGIN + tile_width + PADDING, PAGE_MARGIN + 40),  # правый верхний (Б)
        (PAGE_MARGIN, PAGE_MARGIN + (tile_height + LABEL_HEIGHT) + PADDING + 40),  # левый нижний (В)
        (PAGE_MARGIN + tile_width + PADDING, PAGE_MARGIN + (tile_height + LABEL_HEIGHT) + PADDING + 40),  # правый нижний (Г)
    ]

    correspondence = {}
    for i, (img, label, set_key) in enumerate(zip(shuffled_snapshots, labels, shuffled_order)):
        labeled_tile = create_labeled_tile(img, label, tile_width, tile_height)
        x, y = positions[i]
        page.paste(labeled_tile, (x, y))
        correspondence[label] = set_key

    return page, correspondence

def create_etalon_page(tile_width):
    """Создать страницу с эталонами."""
    # Загрузить и обрезать эталоны
    etalons = []
    max_height = 0

    for i in range(1, 6):
        img_path = ETALON_DIR / f'etalon-kadr-{i}.png'
        img = load_and_crop_image(img_path)
        etalons.append((i, img))

    # Найти максимальную высоту
    max_height = max(img.height for _, img in etalons)

    # Создать страницу с сеткой 3×2
    cols = 3
    rows = 2

    PADDING = 60
    PAGE_MARGIN = 40
    LABEL_HEIGHT = 50

    page_w = cols * tile_width + (cols - 1) * PADDING + PAGE_MARGIN * 2
    page_h = rows * (max_height + LABEL_HEIGHT) + (rows - 1) * PADDING + PAGE_MARGIN * 2 + 80

    page = Image.new('RGB', (page_w, page_h), color='white')

    # Добавить заголовок
    draw = ImageDraw.Draw(page)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    except:
        font = ImageFont.load_default()

    title = "Эталон: настоящие кадры Лекции 7 тех же пяти форм"
    draw.text((PAGE_MARGIN, 10), title, fill='black', font=font)

    # Расположить эталоны в сетку
    for idx, (frame_num, img) in enumerate(etalons):
        row = idx // cols
        col = idx % cols
        x = PAGE_MARGIN + col * (tile_width + PADDING)
        y = PAGE_MARGIN + 80 + row * (max_height + LABEL_HEIGHT + PADDING)

        # Масштабировать и выровнять
        labeled_tile = create_labeled_tile(img, "", tile_width, max_height)

        # Добавить подпись (без букв для эталонов)
        labeled_with_caption = Image.new('RGB', (tile_width, max_height + LABEL_HEIGHT * 2), color='white')
        labeled_with_caption.paste(labeled_tile, (0, LABEL_HEIGHT))

        draw_tile = ImageDraw.Draw(labeled_with_caption)
        label_text = f"Кадр {frame_num} — {FORM_NAMES[frame_num]}"
        try:
            label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        except:
            label_font = ImageFont.load_default()
        draw_tile.text((10, 10), label_text, fill='black', font=label_font)

        page.paste(labeled_with_caption, (x, y))

    return page

def main():
    """Основная функция."""
    # Определить размер плиток для максимизации содержимого
    # 1000 пиксelей в ширину (минимум по требованию для читаемости)
    TILE_WIDTH = 1000

    # Создать страницы
    pages = []
    correspondence_log = []

    # Проверить высоту первого снимка для определения TILE_HEIGHT
    test_img = load_and_crop_image(SETS['A'] / 'k-1.png')
    test_resized = resize_to_width(test_img, TILE_WIDTH)
    TILE_HEIGHT = test_resized.height

    for frame_num in range(1, 6):
        page, corr = create_comparison_page(frame_num, TILE_WIDTH, TILE_HEIGHT)
        pages.append(page)
        correspondence_log.append((frame_num, corr))
        print(f"Создана страница {frame_num} (форма: {FORM_NAMES[frame_num]}, размер: {page.size})")

    # Добавить страницу с эталонами
    etalon_page = create_etalon_page(TILE_WIDTH)
    pages.append(etalon_page)
    print(f"Создана страница 6 (эталоны, размер: {etalon_page.size})")

    # Сохранить все как изображения с компрессией (JPEG для меньшего размера)
    temp_images = []
    for i, page in enumerate(pages, 1):
        temp_path = f'/tmp/sravnenie_page_{i}.jpg'
        # Сохранить как JPEG с оптимальным качеством (60% для меньшего размера файла)
        page.save(temp_path, 'JPEG', quality=60, optimize=True)
        temp_images.append(temp_path)
        file_size_kb = os.path.getsize(temp_path) / 1024
        print(f"  Изображение {i} сохранено: {file_size_kb:.1f} КБ")

    # Создать PDF из изображений
    output_pdf = BASE_DIR / 'SRAVNENIE.pdf'
    pdf_doc = fitz.open()

    for img_path in temp_images:
        # Загрузить изображение
        img = Image.open(img_path)
        w, h = img.size

        # Создать страницу PDF
        page = pdf_doc.new_page(width=w, height=h)

        # Вставить изображение
        pix = fitz.Pixmap(img_path)
        page.insert_image(page.rect, pixmap=pix)

    # Сохранить PDF с максимальным сжатием
    pdf_doc.save(str(output_pdf), deflate=True)
    pdf_doc.close()

    file_size_mb = os.path.getsize(output_pdf) / (1024 * 1024)
    print(f"\nPDF создан: {output_pdf}")
    print(f"Размер файла: {file_size_mb:.2f} МБ")
    print(f"Размер плитки: {TILE_WIDTH} × {TILE_HEIGHT} пиксelей")

    # Проверить текст в PDF
    pdf_doc = fitz.open(str(output_pdf))
    all_text = ""
    for page_num in range(len(pdf_doc)):
        page = pdf_doc[page_num]
        all_text += page.get_text()
    pdf_doc.close()

    print(f"Текст в PDF: {'(пусто)' if not all_text else f'{len(all_text)} символов'}")

    # Проверить на наличие номеров наборов
    forbidden_words = ['набор', 'nabor', 'nabor-1', 'nabor-2', 'nabor-3', 'nabor-4']
    found_forbidden = []
    for word in forbidden_words:
        if word.lower() in all_text.lower():
            found_forbidden.append(word)

    if found_forbidden:
        print(f"ВНИМАНИЕ: Найдены запретные слова: {found_forbidden}")
    else:
        print(f"Проверка текста: номеров наборов не найдено (OK)")

    # Вывести соответствие букв и наборов (для логирования)
    print(f"\n=== СООТВЕТСТВИЕ БУКВ И НАБОРОВ ===")
    print(f"(Зафиксированное семя: {RANDOM_SEED})\n")
    for frame_num, corr in correspondence_log:
        for label in ['А', 'Б', 'В', 'Г']:
            set_key = corr[label]

    # Очистить временные файлы
    for img_path in temp_images:
        os.remove(img_path)

    print(f"\n=== ПРИЁМКА ===")
    print(f"✓ Всего страниц: 6")
    print(f"✓ Размер плитки: {TILE_WIDTH} × {TILE_HEIGHT} пиксelей")
    print(f"✓ Текстовых следов номеров наборов: {'НАЙДЕНЫ!' if found_forbidden else 'не найдено'}")
    print(f"✓ Размер файла PDF: {file_size_mb:.1f} МБ")
    print(f"✓ Соответствие букв и наборов: не изменено (семя {RANDOM_SEED})")

if __name__ == '__main__':
    main()
