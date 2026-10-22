#!/usr/bin/env python3
"""Кадры «как это выглядит в Telegram» для Семинара 8 — РИСОВАННЫЕ МОКАПЫ.

════════════════════════════════════════════════════════════════════════════
ЧЕСТНАЯ ПОМЕТКА. Это рисованные иллюстрации, а не снимки экрана. Рамку чата
(шапку, пузыри, время, фон) рисует этот скрипт. Делать так разрешено прямым
решением владельца курса 2026-10-22: «скрины сообщений Telegram просто сами
сгенерим — нарисуй что-то похожее». Общее правило курса «никаких моков»
(`notes/mcp-limitations.md`, канон §2) для ЭТИХ кадров снято тем же решением
и только для них.

ТЕКСТЫ СООБЩЕНИЙ — НАСТОЯЩИЕ, ДОСЛОВНЫЕ. Каждая строка в пузыре взята из
поля `result.text` (для фото — `result.caption`) в выводе Telegram-узла
живого стенда n8n, прочитанном через `GET /executions/<id>?includeData=true`.
Ни одно слово не сочинено здесь и не отредактировано. Первоисточник со
ссылками на номера выполнений —
`stend/n8n-screenshots-raw/telegram-messages-2026-10-22.txt`; полные выгрузки
выполнений лежат там же рядом (`exec-<id>-*.json`). Картинка Кейса 4 — тот
самый файл, который Telegram принял в выполнении 594, скачанный обратно из
Telegram по `file_id` сообщения (почему 594, а не 593 — см. комментарий в
`main()`: картинка у этого узла случайная, и выбор между двумя одинаково
настоящими прогонами назван вслух, а не спрятан).

ЧТО ОПУЩЕНО И ПОЧЕМУ. Telegram-узел n8n по умолчанию дописывает в конец
сообщения строку «This message was sent automatically with n8n» со ссылкой на
n8n.io. В пузырях её нет: это подпись инструмента, а не содержание сообщения,
и на слайде она уводила бы взгляд с текста, ради которого кадр и ставится.
В первоисточнике выше она приведена целиком — опущено на кадре, не в записи.

ПОЧЕМУ НЕТ ГАЛОЧЕК ДОСТАВКИ. В Telegram галочки стоят только на ИСХОДЯЩИХ
сообщениях — на тех, которые отправил владелец экрана. Здесь экран чужой:
это вид координатора (Кейсы 1 и 4) и вид клиента (Кейс 3), то есть все пузыри
входящие, и галочек у них не бывает. Нарисовать их значило бы подделать ровно
ту деталь, которую зал, живущий в Telegram, замечает первой. Время у каждого
пузыря на месте. Если кадр всё-таки нужен с галочками (вид отправителя) —
это одна строка: `incoming=False` у сообщения.

ЧТО ЗАПИСАНО В ШАПКЕ ЧАТА. «Уведомления учебного центра» — название рабочего
чата из сцены кейса, подтверждённое владельцем 2026-10-22. Кейсы 1 и 4 идут
в него: там сообщения адресованы координатору. Кейс 3 — личная переписка с
клиентом, туда его сообщение попасть не может, и шапка у него своя
(`CHAT_NAME_CLIENT`). Обе строки — константы ниже, меняются в одном месте.

════════════════════════════════════════════════════════════════════════════

Что собирает (всё — НОВЫЕ имена, существующие фигуры не трогаются):

    figures/tg-k1-uvedomlenie.png  Кейс 1: два уведомления координатору подряд —
                                   версия модели (выполнение 591) и версия
                                   шаблона (выполнение 592)
    figures/tg-k1-oshibka.png      Кейс 1, провал версии 1: обращение «Привет,
                                   Имя координатора!» (выполнение 42)
    figures/tg-k3-klient.png       Кейс 3: сообщение клиенту с ветки «одобрено»
                                   (выполнение 590, узел добавлен этой волной)
    figures/tg-k4-kartochka.png    Кейс 4: карточка — фото с подписью
                                   (выполнение 594)

Запуск: `python3 make_figures_telegram.py` (из `rendered/`).
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SEM = HERE.parent
RAW = SEM / "stend" / "n8n-screenshots-raw"
OUT = HERE / "figures"

CHAT_NAME = "Уведомления учебного центра"
CHAT_SUB = "3 участника, 1 бот"
CHAT_NAME_CLIENT = "Учебный центр"
CHAT_SUB_CLIENT = "бот"

BOT_NAME = "n8n demo"          # как бот подписан в самом Telegram (из result.from)

# Время у пузыря — настоящее время отправки сообщения (поле `result.date`
# выполнения, переведённое в московское), а не красивое круглое число.

# Дата на «пилюле» — день того выполнения, из которого взят текст пузыря, а не
# день сборки кадра. Три кадра прогнаны 22 октября, кадр провала Кейса 1 — это
# выполнение 42 от 18 октября, и подписывать его сегодняшним числом значило бы
# соврать ровно в той детали, которую кадр и предъявляет.
DATE_TODAY = "22 октября"
DATE_ERR = "18 октября"

# ── палитра светлой темы Telegram ─────────────────────────────────────────
C_HEADER = (255, 255, 255)
C_HEADER_LINE = (226, 231, 235)
C_CANVAS = (232, 237, 241)
C_BUBBLE = (255, 255, 255)
C_TEXT = (15, 20, 25)
C_SUB = (112, 117, 121)
C_TIME = (161, 170, 179)
C_SENDER = (51, 144, 236)
C_CHIP_BG = (255, 255, 255, 170)
C_AVATAR_A = (46, 134, 222)
C_AVATAR_B = (33, 169, 199)

W = 1400
PAD = 44                        # поле слева/справа в области чата
HEADER_H = 116

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FB if bold else F, size)


FT_TITLE = font(31, bold=True)
FT_SUB = font(23)
FT_MSG = font(28)
FT_SENDER = font(23, bold=True)
FT_TIME = font(21)
FT_CHIP = font(22, bold=True)
FT_AVA = font(28, bold=True)

LINE_H = 40                     # шаг строки в пузыре
BUB_PAD_X = 26
BUB_PAD_Y = 20
BUB_MAX = int(W * 0.70)
BUB_RADIUS = 18
GAP = 20                        # просвет между пузырями


def wrap(draw, text, fnt, max_w):
    """Перенос по словам с уважением к явным переводам строки: текст пришёл
    из Telegram как есть, а там `\\n` — часть сообщения, не оформление."""
    out = []
    for para in text.split("\n"):
        if not para.strip():
            out.append("")
            continue
        line = ""
        for word in para.split(" "):
            probe = (line + " " + word).strip()
            if draw.textlength(probe, font=fnt) <= max_w or not line:
                line = probe
            else:
                out.append(line)
                line = word
        out.append(line)
    return out


def avatar(img, box, letters, a=C_AVATAR_A, b=C_AVATAR_B):
    """Кружок-аватар с вертикальной растяжкой цвета — так он выглядит в
    самом Telegram, когда у чата нет загруженной картинки."""
    x0, y0, x1, y1 = box
    d = x1 - x0
    grad = Image.new("RGB", (1, d))
    gd = ImageDraw.Draw(grad)
    for i in range(d):
        t = i / max(1, d - 1)
        gd.point((0, i), fill=tuple(int(a[k] + (b[k] - a[k]) * t) for k in range(3)))
    grad = grad.resize((d, d))
    mask = Image.new("L", (d, d), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, d - 1, d - 1), fill=255)
    img.paste(grad, (x0, y0), mask)
    dr = ImageDraw.Draw(img)
    tw = dr.textlength(letters, font=FT_AVA)
    dr.text((x0 + (d - tw) / 2, y0 + d / 2 - 18), letters, font=FT_AVA,
            fill=(255, 255, 255))


def header(img, title, sub):
    dr = ImageDraw.Draw(img)
    dr.rectangle((0, 0, W, HEADER_H), fill=C_HEADER)
    dr.line((0, HEADER_H, W, HEADER_H), fill=C_HEADER_LINE, width=2)
    avatar(img, (36, 24, 36 + 68, 24 + 68), "УЦ")
    dr.text((128, 30), title, font=FT_TITLE, fill=C_TEXT)
    dr.text((128, 70), sub, font=FT_SUB, fill=C_SUB)


def chip(img, y, date_s):
    """Серая «пилюля» с датой — разделитель дня."""
    dr = ImageDraw.Draw(img, "RGBA")
    tw = dr.textlength(date_s, font=FT_CHIP)
    w, h = tw + 44, 46
    x = (W - w) / 2
    dr.rounded_rectangle((x, y, x + w, y + h), radius=23, fill=C_CHIP_BG)
    dr.text((x + 22, y + 10), date_s, font=FT_CHIP, fill=(94, 103, 112))
    return y + h + GAP + 6


def ticks(dr, x, y):
    """Две галочки «прочитано» — рисуются только для исходящих пузырей."""
    col = (77, 166, 234)
    for off in (0, 11):
        dr.line((x + off, y + 9, x + off + 6, y + 15), fill=col, width=3)
        dr.line((x + off + 6, y + 15, x + off + 17, y + 2), fill=col, width=3)


def bubble(img, y, text, time_s, sender=None, photo=None, incoming=True):
    """Один пузырь. Возвращает нижнюю границу (для следующего)."""
    dr = ImageDraw.Draw(img)
    inner_max = BUB_MAX - 2 * BUB_PAD_X
    lines = wrap(dr, text, FT_MSG, inner_max)

    ph_w = ph_h = 0
    if photo is not None:
        ph_w = inner_max
        ph_h = int(photo.height * ph_w / photo.width)

    text_w = max([dr.textlength(l, font=FT_MSG) for l in lines] + [0])
    body_w = max(text_w, ph_w)
    if sender:
        body_w = max(body_w, dr.textlength(sender, font=FT_SENDER))

    time_w = dr.textlength(time_s, font=FT_TIME) + (34 if not incoming else 0)
    # Время садится в строку с последней строкой текста, если та оставила место.
    last_w = dr.textlength(lines[-1], font=FT_MSG) if lines else 0
    inline = (last_w + 24 + time_w) <= inner_max and photo is None
    if not inline:
        body_w = max(body_w, time_w)

    bw = body_w + 2 * BUB_PAD_X
    bh = BUB_PAD_Y * 2 + len(lines) * LINE_H
    if sender:
        bh += 32
    if photo is not None:
        bh += ph_h + 14
    if not inline:
        bh += 30

    bx = PAD if incoming else W - PAD - bw
    fill = C_BUBBLE if incoming else (239, 253, 222)
    dr.rounded_rectangle((bx, y, bx + bw, y + bh), radius=BUB_RADIUS, fill=fill)
    # Хвостик пузыря у нижнего угла — та деталь, без которой кадр перестаёт
    # читаться как Telegram и становится просто карточкой.
    if incoming:
        dr.polygon([(bx + 4, y + bh - 20), (bx + 4, y + bh),
                    (bx - 14, y + bh)], fill=fill)
    else:
        dr.polygon([(bx + bw - 4, y + bh - 20), (bx + bw - 4, y + bh),
                    (bx + bw + 14, y + bh)], fill=fill)

    cy = y + BUB_PAD_Y
    cx = bx + BUB_PAD_X
    if sender:
        dr.text((cx, cy), sender, font=FT_SENDER, fill=C_SENDER)
        cy += 32
    if photo is not None:
        ph = photo.resize((ph_w, ph_h), Image.LANCZOS)
        mask = Image.new("L", (ph_w, ph_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, ph_w - 1, ph_h - 1),
                                               radius=12, fill=255)
        img.paste(ph, (int(cx), int(cy)), mask)
        cy += ph_h + 14
    for l in lines:
        dr.text((cx, cy), l, font=FT_MSG, fill=C_TEXT)
        cy += LINE_H

    ty = cy - LINE_H + 10 if inline else cy
    tx = bx + bw - BUB_PAD_X - time_w
    dr.text((tx, ty), time_s, font=FT_TIME, fill=C_TIME)
    if not incoming:
        ticks(dr, tx + dr.textlength(time_s, font=FT_TIME) + 10, ty)

    return y + bh + GAP


def canvas(title, sub, msgs, date_s=DATE_TODAY, tail=36):
    """Собирает кадр в два прохода: первый считает высоту, второй рисует.
    Иначе высота пузырей (перенос строк зависит от шрифта) не известна до
    отрисовки, а холст PIL после создания не растягивается."""
    probe = Image.new("RGB", (W, 4000), C_CANVAS)
    y = chip(probe, HEADER_H + 26, date_s)
    for m in msgs:
        y = bubble(probe, y, **m)
    h = int(y - GAP + tail)

    img = Image.new("RGB", (W, h), C_CANVAS)
    header(img, title, sub)
    y = chip(img, HEADER_H + 26, date_s)
    for m in msgs:
        y = bubble(img, y, **m)
    return img


# ── дословные тексты (источник: telegram-messages-2026-10-22.txt) ──────────
T_K1_LLM = ("Привет! У нас новая многотемная заявка от Марии Величко на "
            "перенос занятия, в которой также упоминается оплата. "
            "Подробности прилагаю, если нужно!")
T_K1_TPL = "Новая заявка от Мария Величко: тема «перенос занятия», также: оплата."
T_K1_ERR = ("Привет, Имя координатора! 😊 У нас новая многотемная заявка от "
            "Олега по вопросу переноса занятия и об оплате. Посмотри, "
            "пожалуйста!")
T_K3 = ("Здравствуйте! Ваш запрос на возврат рассмотрен: одобрено.\n"
        "Сумма: 2500 ₽.\n"
        "Деньги вернутся на карту в течение трёх рабочих дней.")
T_K4 = "Новая заявка от Мария Величко: тема «перенос занятия», также: оплата."


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    # Кейс 1 — два уведомления подряд: сочинённое моделью и собранное шаблоном.
    # Рядом в одном чате видно то, ради чего кейс и существует: модель
    # склоняет имя верно и обещает несуществующее вложение, шаблон не обещает
    # ничего лишнего и не умеет склонять.
    canvas(CHAT_NAME, CHAT_SUB, [
        dict(text=T_K1_LLM, time_s="13:05", sender=BOT_NAME),
        dict(text=T_K1_TPL, time_s="13:06", sender=BOT_NAME),
    ]).save(OUT / "tg-k1-uvedomlenie.png")

    # Кейс 1, провал версии 1 (выполнение 42, 2026-10-18).
    canvas(CHAT_NAME, CHAT_SUB, [
        dict(text=T_K1_ERR, time_s="12:42", sender=BOT_NAME),
    ], date_s=DATE_ERR).save(OUT / "tg-k1-oshibka.png")

    # Кейс 3 — сообщение клиенту с ветки «одобрено».
    canvas(CHAT_NAME_CLIENT, CHAT_SUB_CLIENT, [
        dict(text=T_K3, time_s="13:04"),
    ]).save(OUT / "tg-k3-klient.png")

    # Кейс 4 — карточка: то самое фото, которое Telegram принял в выполнении
    # 594, скачанное обратно из Telegram по file_id сообщения.
    #
    # Почему 594, а не 593. Узел `Fetch card image (HTTP)` тянет картинку с
    # picsum.photos, то есть КАЖДЫЙ прогон приносит другую случайную
    # фотографию, никак не связанную с заявкой. В выполнении 593 случайной
    # картинкой оказался обнажённый пловец — содержательно это ровно то же
    # самое (случайный кадр из стока), но на экране в аудитории он забирает
    # всё внимание на себя и уводит разговор с механики отправки фото. Прогон
    # повторён один раз, взят следующий кадр (выполнение 594). Оба файла
    # сохранены в `stend/n8n-screenshots-raw/`, подмены нет — есть выбор между
    # двумя одинаково настоящими прогонами, названный вслух.
    photo = Image.open(RAW / "k4-card-photo-exec594-telegram-delivered.jpg").convert("RGB")
    canvas(CHAT_NAME, CHAT_SUB, [
        dict(text=T_K4, time_s="13:12", sender=BOT_NAME, photo=photo),
    ]).save(OUT / "tg-k4-kartochka.png")

    for n in ("tg-k1-uvedomlenie", "tg-k1-oshibka", "tg-k3-klient",
              "tg-k4-kartochka"):
        p = OUT / f"{n}.png"
        print(f"{p.name:26} {Image.open(p).size}")


if __name__ == "__main__":
    main()
