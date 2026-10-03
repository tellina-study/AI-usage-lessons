#!/usr/bin/env python3
"""Схемы механики — рисуются программно (PIL), а не описываются словами."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

F="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FM="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
DEEP=(0x21,0x29,0x5C); MID=(0x06,0x5A,0x82); LIGHT=(0x1C,0x72,0x93)
GOLD=(0xF0,0xAB,0x00); TEAL=(0x02,0x80,0x90); SURF=(0xF4,0xF7,0xFA)
INK=(0x14,0x1B,0x2E); MUTE=(0x5B,0x6B,0x7F); RED=(0xB3,0x26,0x1E); W=(255,255,255)
OUT=Path(__file__).parent/"figures"; OUT.mkdir(exist_ok=True)
def f(sz,b=False,m=False): return ImageFont.truetype(FM if m else (FB if b else F), sz)
def box(d,x,y,w,h,txt,fc,tc=W,sz=20,b=True,m=False,pad=8):
    d.rounded_rectangle([x,y,x+w,y+h],radius=10,fill=fc)
    fo=f(sz,b,m); lines=txt.split("\n")
    th=len(lines)*(sz+6)-6; cy=y+(h-th)//2
    for i,ln in enumerate(lines):
        tw=d.textlength(ln,font=fo); d.text((x+(w-tw)//2,cy+i*(sz+6)),ln,font=fo,fill=tc)
def arrow(d,x1,y1,x2,y2,col=MID,label=None,sz=17):
    d.line([x1,y1,x2,y2],fill=col,width=4)
    import math; a=math.atan2(y2-y1,x2-x1); L=14
    d.polygon([(x2,y2),(x2-L*math.cos(a-0.4),y2-L*math.sin(a-0.4)),
               (x2-L*math.cos(a+0.4),y2-L*math.sin(a+0.4))],fill=col)
    if label:
        fo=f(sz,True); tw=d.textlength(label,font=fo)
        d.text(((x1+x2-tw)//2,min(y1,y2)-sz-9),label,font=fo,fill=col)
def center(d,y,txt,sz=21,col=INK,b=False,Wd=2400):
    fo=f(sz,b); tw=d.textlength(txt,font=fo); d.text(((Wd-tw)//2,y),txt,font=fo,fill=col)



print("схемы:", *[p.name for p in sorted(OUT.glob('*.png'))])

# ═══════════════════════════════════════════════════════════════════════════
# Схемы раздела «MCP: доступ наружу» (s34–s43). Холст 1600 px = 12,2 дюйма
# на слайде, поэтому кегль здесь крупнее, чем в схемах выше: 20 px ≈ 11 pt.
# ═══════════════════════════════════════════════════════════════════════════
MW = 1600
CODEBG = (0x18, 0x20, 0x3A)

def mtext(d, x, y, t, sz=23, col=INK, b=False, m=False, strike=False):
    fo = f(sz, b, m); d.text((x, y), t, font=fo, fill=col)
    w = d.textlength(t, font=fo)
    if strike: d.line([x-5, y+sz*0.60, x+w+5, y+sz*0.60], fill=RED, width=3)
    return w

def mcent(d, y, t, sz=23, col=INK, b=False):
    fo = f(sz, b); d.text(((MW - d.textlength(t, font=fo))//2, y), t, font=fo, fill=col)

def mpanel(d, x, y, w, h, title=None, fill=SURF, stroke=LIGHT, tsz=23, tcol=DEEP):
    d.rounded_rectangle([x, y, x+w, y+h], radius=12, fill=fill, outline=stroke, width=3)
    if title: d.text((x+20, y+14), title, font=f(tsz, True), fill=tcol)

def mrow(d, y, items, w, h, gap, sz=21, tc=None):
    total = len(items)*w + (len(items)-1)*gap
    x = (MW - total)//2
    xs = []
    for t, c in items:
        box(d, x, y, w, h, t, c, tc=(tc or (DEEP if c in (GOLD, SURF) else W)), sz=sz)
        xs.append(x); x += w + gap
    for i in range(len(items)-1):
        arrow(d, xs[i]+w, y+h//2, xs[i+1], y+h//2)
    return xs

def msave(im, name):
    im.save(OUT/name); return name

# ── s34. Сцена кейса: три кадра, как на s08 ────────────────────────────────
# Раньше здесь стояла пятикоробочная схема цикла — обобщение процесса, а не
# случай. Студент так и написал: «схема процесса, а не случай». Теперь тут та
# же грамматика, что на s08, который он же назвал единственным настоящим
# кейсом: три кадра подряд, подтверждённый артефакт с пересчитываемым числом,
# дословные слова заказчика и пересчитываемое число ручных шагов.
im = Image.new("RGB", (MW, 430), W); d = ImageDraw.Draw(im)
mtext(d, 25, 8, "Один репозиторий, три кадра подряд — та же неделя", 25, MUTE)
cards = [
    (MID, "Что уже лежит в репозитории", [
        "ветка seminar-5-hook, коммит 9803643",
        "27 файлов: правило, барьер, процедура",
        "агент читает их сам, без доступа наружу",
        "файла .mcp.json в дереве нет"]),
    (TEAL, "Что пришло снаружи за неделю", [
        "«Форма не отправляется с телефона»",
        "«Добавьте поле — откуда вы о нас узнали»",
        "обе — задачами в трекере, не в файлах",
        "обе появились без разработчика"]),
    (RED, "Как это доезжает до агента сейчас", [
        "1 открыть задачу · 2 скопировать текст",
        "3 вставить в чат · 4 скопировать ответ",
        "5 вернуться в трекер · 6 вставить в комментарий",
        "шесть ручных шагов на одну задачу"]),
]
cw, gap = 496, 31
x = 25
for col, head, lines in cards:
    mpanel(d, x, 48, cw, 296, None, fill=SURF, stroke=col)
    d.rounded_rectangle([x, 48, x + cw, 104], radius=12, fill=col)
    hw = d.textlength(head, font=f(21, True))
    d.text((x + (cw - hw)//2, 66), head, font=f(21, True), fill=W)
    for i, ln in enumerate(lines):
        bold = (i == 3)
        sz = 19
        while d.textlength(ln, font=f(sz, bold)) > cw - 36 and sz > 15:
            sz -= 1
        mtext(d, x + 18, 128 + i*52, ln, sz, DEEP if bold else INK, b=bold)
    x += cw + gap
for i in range(2):
    arrow(d, 25 + cw + i*(cw+gap) + 2, 196, 25 + cw + gap + i*(cw+gap) - 2, 196, col=MUTE)
mcent(d, 362, "Третий месяц, несколько раз в неделю. Сколько правил ни допиши в файл — этих шести шагов в нём нет:", 21, INK)
mcent(d, 390, "задача появляется снаружи и меняется без нас.", 21, INK)
print(msave(im, "mcp-stsena.png"))

# ── s37. Порядок трёх проверок ─────────────────────────────────────────────
im = Image.new("RGB", (MW, 348), W); d = ImageDraw.Draw(im)
mtext(d, 20, 10, "Три проверки — и порядок в них тоже часть ответа", 25, DEEP, b=True)
mrow(d, 54, [("1 · Нужно ли вообще?\nне хватит ли обычной команды", GOLD),
             ("2 · С какими правами?\nвычеркнуть всё лишнее", TEAL),
             ("3 · По какой цене?\nсколько добавит в контекст", MID)], 440, 116, 60, sz=21)
mcent(d, 190, "Начать с третьего — отлично оптимизировать стоимость того,", 22, RED)
mcent(d, 218, "что вообще не следовало подключать.", 22, RED)
mpanel(d, 60, 252, MW-120, 76, fill=SURF, stroke=MUTE)
mcent(d, 266, "«официальный» и «сколько звёзд» — оценка источника, а не проверка:", 20, MUTE)
mcent(d, 294, "ни один из трёх вопросов они не закрывают", 20, MUTE)
print(msave(im, "mcp-poryadok-proverok.png"))

# ── s38. Операции — и экран, на котором права вычёркивают ──────────────────
# Раньше правая панель была авторским пересказом («широкий токен даёт: все
# репозитории · чтение и запись · управление настройками · удаление»), и
# студент честно спросил: где именно это вычёркивают и как называются галочки.
# Теперь справа — сам экран, с настоящими именами строк.
im = Image.new("RGB", (MW, 560), W); d = ImageDraw.Draw(im)
mtext(d, 20, 8, "Сначала список операций — потом экран, на котором вычёркивают", 25, DEEP, b=True)

mpanel(d, 25, 54, 560, 386, "Агент должен уметь")
for i, t in enumerate(["читать открытые задачи", "писать комментарий к задаче",
                       "готовить черновик правки"]):
    mtext(d, 50, 112 + i*46, "•  " + t, 22, INK)
mtext(d, 50, 268, "Ничего про удаление, про настройки", 20, MUTE)
mtext(d, 50, 294, "репозитория, про другие репозитории.", 20, MUTE)
mpanel(d, 50, 334, 510, 90, None, fill=(0xFD, 0xF0, 0xEE), stroke=RED)
mtext(d, 70, 346, "Классический токен одной галочкой repo", 19, INK)
mtext(d, 70, 372, "даёт все репозитории, включая приватные —", 19, INK)
mtext(d, 70, 398, "ровно условие 1 из инцидента впереди.", 19, INK)

mpanel(d, 620, 54, 955, 386, "Экран создания токена — что на нём вычёркивают")
mtext(d, 645, 100, "Settings → Developer settings → Personal access tokens → Fine-grained tokens",
      17, MID, m=True)
mtext(d, 645, 136, "Repository access", 21, DEEP, b=True)
mtext(d, 665, 168, "All repositories", 21, MUTE, strike=True)
mtext(d, 665, 200, "Only select repositories  →  signup-landing", 21, TEAL, b=True)
mtext(d, 645, 240, "Repository permissions", 21, DEEP, b=True)
perms = [("Issues", "Read and write", "читать задачи и писать комментарий"),
         ("Pull requests", "Read and write", "открыть черновик правки"),
         ("Contents", "Read and write", "ветка с правкой, без неё черновика нет"),
         ("Metadata", "Read-only", "ставится сама, снять нельзя")]
for i, (name, lvl, why) in enumerate(perms):
    y = 274 + i*34
    mtext(d, 665, y, name, 20, INK, b=True)
    mtext(d, 830, y, lvl, 20, TEAL, m=True)
    mtext(d, 1055, y, why, 18, MUTE)
mtext(d, 645, 414, "Остальные строки остаются No access — это значение по умолчанию.", 19, MUTE)

box(d, 25, 458, MW-50, 58, "Остаётся: один репозиторий  ·  четыре строки прав  ·  всё прочее — No access",
    GOLD, tc=DEEP, sz=24)
mcent(d, 528, "Имена строк — с экрана создания токена GitHub, сверены по документации; живого снимка в захватах занятия нет.",
      18, MUTE)
print(msave(im, "mcp-vycherkivanie.png"))

# ── s39. Ключ, команда подключения, область ────────────────────────────────
# Этой схемы раньше не было, и это был главный провал раздела: слайд ссылался
# на «команду подключения», а самой команды в деке не встречалось ни разу — ни
# на слайдах, ни в заметках. Повторить ступень дома было нельзя. Здесь стоят
# три вещи, которых не хватало: куда класть ключ, чем подключать, что делает
# каждый флаг.
im = Image.new("RGB", (MW, 470), W); d = ImageDraw.Draw(im)
mtext(d, 20, 8, "Куда положить ключ, чем подключить, куда ляжет запись", 25, DEEP, b=True)

mpanel(d, 25, 50, MW-50, 92, None, fill=SURF, stroke=LIGHT)
mtext(d, 48, 60, "Шаг 1. Ключ живёт в окружении той оболочки, из которой вы запускаете claude —",
      19, DEEP, b=True)
mtext(d, 48, 86, "не в репозитории и не в самом файле конфигурации.", 19, DEEP, b=True)
mtext(d, 48, 112, "export GITHUB_PAT=github_pat_…", 20, MID, m=True)
mtext(d, 470, 112, "строкой в ~/.zshrc или ~/.bashrc — иначе пропадёт вместе с окном терминала",
      18, MUTE)

mtext(d, 25, 156, "Шаг 2. Команда подключения", 21, DEEP, b=True)
d.rounded_rectangle([25, 188, MW-25, 320], radius=12, fill=CODEBG)
cmd = ["claude mcp add --scope project \\",
       "  --env GITHUB_PERSONAL_ACCESS_TOKEN='${GITHUB_PAT}' \\",
       "  --transport stdio github \\",
       "  -- npx -y @modelcontextprotocol/server-github"]
for i, ln in enumerate(cmd):
    mtext(d, 48, 202 + i*29, ln, 19, (0xE8, 0xEF, 0xF7), m=True)

notes = [("--scope project", "запись ляжет в .mcp.json в корне\nрепозитория. Без флага — в личную\nконфигурацию, и у коллеги её не будет", TEAL),
         ("одинарные кавычки", "в файл попадёт имя ${GITHUB_PAT},\nа не значение: оболочка его\nне раскроет до записи", GOLD),
         ("--", "всё после разделителя запускается\nкак есть. Пропустите его — запустится\nне то, что вы набрали", LIGHT)]
x = 25
for title, body, col in notes:
    mpanel(d, x, 340, 508, 118, None, fill=W, stroke=col)
    mtext(d, x+18, 350, title, 20, DEEP, b=True, m=True)
    for j, ln in enumerate(body.split("\n")):
        mtext(d, x+18, 378 + j*22, ln, 17, INK)
    x += 508 + 14
print(msave(im, "mcp-podklyuchenie.png"))

# ── s40. Анатомия .mcp.json ────────────────────────────────────────────────
im = Image.new("RGB", (MW, 420), W); d = ImageDraw.Draw(im)
mtext(d, 20, 8, "Четыре решения разговора — и где каждое лежит в файле", 25, DEEP, b=True)
d.rounded_rectangle([25, 50, 780, 362], radius=12, fill=CODEBG)
code = ['{', '  "mcpServers": {', '    "github": {', '      "command": "npx",',
        '      "args": ["-y", "@modelcontextprotocol/server-github"],', '      "env": {',
        '        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PAT}"', '      }', '    }', '  }', '}']
for i, ln in enumerate(code):
    mtext(d, 46, 66+i*26, ln, 18, (0xE8, 0xEF, 0xF7), m=True)
notes = [(70, "чем запускается — это исполняемая команда", LIGHT),
         (140, "что запускается — пакет самого сервера", LIGHT),
         (206, "ключ подставляется из окружения;\nзначения в файле нет", TEAL),
         (292, "права этого ключа — вне файла:\nодин репозиторий, не вся учётная запись", GOLD)]
for y, t, c in notes:
    lines = t.split("\n")
    for j, ln in enumerate(lines): mtext(d, 870, y+j*28, ln, 21, DEEP if c == GOLD else INK, b=(c == GOLD))
    d.rounded_rectangle([845, y-6, 852, y+28*len(lines)-2], radius=3, fill=c)
    arrow(d, 792, y+14, 836, y+14, col=c)
mcent(d, 380, "Файл лежит в корне репозитория — и коммитится вместе с кодом.", 22, INK)
print(msave(im, "mcp-anatomiya.png"))

# Прежние схемы s41 (области видимости), s47 (что грузится) и s42 (статус)
# удалены вместе со слиянием тактов: их содержание живёт в двух новых схемах
# ниже — s41-ot-fayla-do-instrumenta и s42-poryadok-otladki.

# ── s43. Инцидент 26.05.2025: разбор, а не схема ───────────────────────────
# Раньше здесь стояли пять абстрактных коробок («публичный issue с инструкцией
# внутри»), а сам инцидент — дата, продукт, что утекло — жил только в заметках.
# Студент честно написал, что запомнит трио наполовину. Теперь на схеме стоят
# имена: дата, исследователь, продукт, репозиторий-приманка, дословная просьба
# разработчика и три названные позиции утечки. Золото по-прежнему одно — на
# исходе, ради которого вычёркивание делалось. Плитка «без модели вообще»
# уехала на s42, где у неё есть починка.
im = Image.new("RGB", (MW, 478), W); d = ImageDraw.Draw(im)
mtext(d, 20, 8, "26 мая 2025  ·  Invariant Labs  ·  официальный сервер GitHub, 14 000 звёзд",
      25, DEEP, b=True)
mrow(d, 48, [("задача в публичном\nukend0464/pacman", RED),
             ("разработчик: «разберись\nс открытыми задачами»", MID),
             ("инструкция из задачи —\nв контексте как своя", RED),
             ("токен на все репозитории:\nчитает приватные", LIGHT),
             ("агент сам открыл правку\nв том же публичном репо", RED)],
     286, 112, 34, sz=18)
mpanel(d, 105, 178, 1390, 62, None, fill=(0xFD, 0xF0, 0xEE), stroke=RED)
mcent(d, 196, "Утекло: список приватных проектов (среди них «Jupiter Star»)  ·  планы переезда  ·  зарплата",
      22, INK)
mtext(d, 105, 256, "Смертельное трио", 24, DEEP, b=True)
trio = ["1 · доступ к приватным данным", "2 · недоверенный чужой текст", "3 · канал наружу"]
for i, t_ in enumerate(trio):
    box(d, 105 + i*480, 292, 430, 84, t_, TEAL, sz=21)
for i in range(2):
    mtext(d, 553 + i*480, 318, "+", 32, DEEP, b=True)
mpanel(d, 105, 392, 1390, 74, None, fill=SURF, stroke=LIGHT)
mtext(d, 130, 402, "что мы сделали десять минут назад:", 19, MUTE)
w = mtext(d, 130, 430, "вычеркнули «все репозитории, включая приватные»", 22, MUTE, strike=True)
arrow(d, 130+w+24, 444, 130+w+94, 444, col=MID)
res = "условие 1 снято — цепочка рвётся: читать нечего"
rw = d.textlength(res, font=f(22, True))
d.rounded_rectangle([130+w+112, 422, 130+w+152+rw, 466], radius=10, fill=GOLD)
mtext(d, 130+w+132, 430, res, 22, DEEP, b=True)
print(msave(im, "mcp-trio.png"))


# ── s44. Подмена уже одобренного: разобранный случай ───────────────────────
# Прежний mcp-podmena.png лежал в репозитории бинарником, которого не делал ни
# один генератор, и показывал случай из раздела про скиллы, а не про серверы.
# Здесь — настоящий случай этого раздела, в той же трёхкадровой грамматике,
# что и сцена s34: пятнадцать честных версий, шестнадцатая, и отдельный
# эксперимент, который объясняет, почему повторно никто не спросил.
im = Image.new("RGB", (MW, 430), W); d = ImageDraw.Draw(im)
mtext(d, 25, 8, "postmark-mcp — один разобранный случай подмены после одобрения", 25, MUTE)
cards = [
    (MID, "Пятнадцать версий — всё честно", [
        "пакет назвался именем известной почтовой службы",
        "письма отправляет ровно так, как обещает",
        "около 1 643 загрузок в неделю",
        "одобрили один раз — и забыли"]),
    (RED, "Шестнадцатая, 17 сентября 2025", [
        "добавлена одна строка кода",
        "скрытая копия каждого письма — на чужой адрес",
        "имя, описание и поведение снаружи те же",
        "повторно никто ничего не спросил"]),
    (TEAL, "Почему не спросили — измерено", [
        "инструкцию спрятали в описание инструмента",
        "8 попыток из 8 дошли до модели",
        "0 из 8 вызвали повторный вопрос",
        "на 25 безобидных описаниях — ни одного ложного"]),
]
cw, gap = 496, 31
x = 25
for col, head, lines in cards:
    mpanel(d, x, 48, cw, 296, None, fill=SURF, stroke=col)
    d.rounded_rectangle([x, 48, x + cw, 104], radius=12, fill=col)
    hw = d.textlength(head, font=f(21, True))
    d.text((x + (cw - hw)//2, 66), head, font=f(21, True), fill=W)
    for i, ln in enumerate(lines):
        bold = (i == 3)
        sz = 19
        while d.textlength(ln, font=f(sz, bold)) > cw - 36 and sz > 15:
            sz -= 1
        mtext(d, x + 18, 128 + i*52, ln, sz, DEEP if bold else INK, b=bold)
    x += cw + gap
for i in range(2):
    arrow(d, 25 + cw + i*(cw+gap) + 2, 196, 25 + cw + gap + i*(cw+gap) - 2, 196, col=MUTE)
mcent(d, 362, "Вы одобряете имя инструмента. Текст за этим именем может смениться в любой момент —", 21, INK)
mcent(d, 390, "и по умолчанию вас об этом не спросят.", 21, INK)
print(msave(im, "mcp-podmena.png"))

# ── s36. Лестница свидетельств: кто мог это перепроверить ──────────────────
# Третья таблица «источник · что показал · сила» подряд по деке (s10, s24, s36)
# — зал перестаёт их различать. Здесь способ показа другой: организующая ось —
# не сила как оценка, а ПРОВЕРЯЕМОСТЬ как её причина, и нижняя ступень пуста.

def mwrap(d, t, sz, maxw, b=False):
    """Перенос по словам под измеренную ширину — иначе длинная строка молча
    уезжает за правый край холста, а на слайде это уже не видно."""
    fo = f(sz, b); out, cur = [], ""
    for wd in t.split():
        probe = (cur + " " + wd).strip()
        if d.textlength(probe, font=fo) <= maxw or not cur:
            cur = probe
        else:
            out.append(cur); cur = wd
    if cur: out.append(cur)
    return out

def mdash_rect(d, x, y, x2, y2, col, w=3, dash=14, gap=10):
    for a in range(x, x2, dash + gap):
        b = min(a + dash, x2)
        d.line([a, y, b, y], fill=col, width=w); d.line([a, y2, b, y2], fill=col, width=w)
    for a in range(y, y2, dash + gap):
        b = min(a + dash, y2)
        d.line([x, a, x, b], fill=col, width=w); d.line([x2, a, x2, b], fill=col, width=w)

RUNGS = [
    (MID, "Может перепроверить кто угодно", "принимаем целиком", [
        "скан 7973 живых серверов: 40,55% отдают инструменты, не проверяя, кто обратился —"
        " это весь отсканированный набор, а не выборка из него",
        "сокрытие инструкции: 8 из 8 доставлены модели, 0 из 8 спросили заново,"
        " 0 ложных на 25 безобидных описаниях — и всё это на 3 независимых библиотеках"]),
    (LIGHT, "Раскрыто официально, с заплаткой", "механизм точен, частота — нет", [
        "флаг «только чтение» не включал режим; сетевой вход слушает, не проверяя, кто обратился",
        "в живых атаках такого не находили: это знание про устройство, не про частоту"]),
    (MUTE, "Со слов заинтересованной стороны", "механизм принимаем, масштаб — нет", [
        "команда из конфигурации исполняется в любом случае; безобиден первые 3 вызова,"
        " и только потом меняет описания",
        "замер «команда против сервера» воспроизводим, но на узком круге задач;"
        " жертва не названа, методика раскрыта не полностью"]),
]

TXTW = MW - 40 - 76          # от левого края текста до правого поля
im = Image.new("RGB", (MW, 700), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "Сколько веса у источника — это про то, кто мог его перепроверить", 25, DEEP, b=True)
y = 46
for col, rung, verdict, lines in RUNGS:
    wrapped = [mwrap(d, ln, 21, TXTW) for ln in lines]
    h = 50 + sum(len(w_) * 30 + 16 for w_ in wrapped)
    d.rounded_rectangle([20, y, MW - 20, y + h], radius=12, fill=SURF, outline=col, width=3)
    d.rounded_rectangle([20, y, 27, y + h], radius=3, fill=col)          # корешок яруса
    mtext(d, 46, y + 11, rung, 23, col, b=True)
    vw = d.textlength(verdict, font=f(20, True))
    d.rounded_rectangle([MW - 58 - vw, y + 9, MW - 36, y + 41], radius=9, fill=col)
    mtext(d, MW - 47 - vw, y + 14, verdict, 20, W, b=True)
    ly = y + 54
    for w_ in wrapped:
        d.ellipse([50, ly + 8, 62, ly + 20], fill=col)
        for k, ln in enumerate(w_):
            mtext(d, 78, ly + k * 30, ln, 21, INK)
        ly += len(w_) * 30 + 16
    y += h + 14

# Пустая ступень — честный пробел как часть той же лестницы, а не сноска под ней.
# Пунктир = оговорка по грамматике деки, поэтому и рамка здесь пунктирная.
gap_lines = mwrap(d, "сколько времени занимает сама проверка сервера перед подключением —"
                     " поэтому критерий дальше строится на признаках, а не на цене процедуры",
                  21, TXTW)
gh = 52 + len(gap_lines) * 30
mdash_rect(d, 20, y, MW - 20, y + gh, MUTE)
mtext(d, 46, y + 11, "Не измерил никто", 23, MUTE, b=True)
for k, ln in enumerate(gap_lines):
    mtext(d, 78, y + 46 + k * 30, ln, 21, MUTE)
print(msave(im.crop((0, 0, MW, y + gh + 12)), "mcp-lestnitsa.png"))

# ── s41. От файла до инструмента: слияние «областей» и «что грузится» ──────
# Три механики подряд (области → контекст → отладка) шли 7 минут в одном
# регистре. Первые две сведены в ОДИН большой такт по общей оси времени.
# Колонки, а не ярусы: вертикальная раскладка давала холст 1600×724, слайд
# ужимал его под свою высоту, и подписи внутри схемы становились нечитаемы.
CW, CX = 500, (30, 550, 1070)
im = Image.new("RGB", (MW, 500), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "Путь от строки в файле до инструмента, который видит модель", 25, DEEP, b=True)
for cx, head in zip(CX, ("1 · где лежит", "2 · что исполняется", "3 · что попадает в контекст")):
    mtext(d, cx, 44, head, 21, MID, b=True)

def cpanel(x, y, txt, *, stroke=LIGHT, fill=SURF, col=INK, sz=19, head=None, hcol=DEEP):
    """Колонка узкая — текст переносится по измеренной ширине, а высота панели
    считается по числу получившихся строк."""
    lines = mwrap(d, txt, sz, CW - 44)
    h = 20 + (30 if head else 0) + len(lines) * 27
    d.rounded_rectangle([x, y, x + CW, y + h], radius=10, fill=fill, outline=stroke, width=3)
    if head: mtext(d, x + 20, y + 9, head, 20, hcol, b=True)
    for k, ln in enumerate(lines):
        mtext(d, x + 20, y + 11 + (30 if head else 0) + k * 27, ln, sz, col)
    return h

# ── 1 · где лежит
y = 76
for txt, c in (("local — только у меня, не коммитится", MUTE),
               ("project — .mcp.json в корне, коммитится", TEAL),
               ("user — во всех моих проектах", MUTE)):
    box(d, CX[0], y, CW, 50, txt, c, sz=19); y += 58
y += 6
y += cpanel(CX[0], y, "Совпало имя сервера в двух областях — побеждает вся запись "
                      "приоритетной области целиком; поля не сливаются.") + 10
cpanel(CX[0], y, "политика организации → личная → проектная → общая личная → плагин → коннектор",
       stroke=SURF, col=MUTE, sz=18, head="приоритет при совпадении имени", hcol=MUTE)

# ── 2 · что исполняется
y = 76
d.rounded_rectangle([CX[1], y, CX[1] + CW, y + 76], radius=10, fill=CODEBG)
mtext(d, CX[1] + 22, y + 12, '"command": "npx",', 19, W, m=True)
mtext(d, CX[1] + 22, y + 42, '"args": ["-y", "@scope/server"]', 19, W, m=True)
arrow(d, CX[1] + CW // 2, y + 82, CX[1] + CW // 2, y + 116)
y += 124
y += cpanel(CX[1], y, "при старте сессии это запускается как процесс на вашей машине",
            stroke=TEAL) + 10
y += cpanel(CX[1], y, "Пакет заранее никто не проверяет — поэтому ключ значением в файле "
                      "стал бы частью исполняемой строки.", stroke=RED) + 10
cpanel(CX[1], y, "для удалённого сервера способ — http; sse официально помечен устаревшим",
       stroke=SURF, col=MUTE, sz=18)

# ── 3 · что попадает в контекст
y = 76
y += cpanel(CX[2], y, "имена инструментов и инструкции сервера",
            head="при старте сессии", hcol=MID) + 10
y += cpanel(CX[2], y, "полная схема инструмента — и только та, что понадобилась",
            fill=(0xFD, 0xF3, 0xD6), stroke=GOLD, head="по требованию модели") + 16
d.rounded_rectangle([CX[2], y, CX[2] + CW, y + 46], radius=10, fill=CODEBG)
mtext(d, CX[2] + 22, y + 11, "сервер__инструмент", 21, W, m=True)
y += 56
cpanel(CX[2], y, "полное имя — именно его требуют правило прав, список инструментов скилла "
                 "и совпадение в хуке", stroke=SURF, col=MUTE, sz=18)
print(msave(im, "mcp-ot-fayla.png"))

# ── s42. Порядок отладки: тот же приём, что на s37 ─────────────────────────
# Ревью назвало s37 образцом: целевой ответ там не карточка, а ПОРЯДОК —
# нумерованные ворота, золото на первом, красная строка про частый неверный
# старт, приглушённая панель про то, что ответом не является. Здесь та же
# грамматика приложена к отладке. Правка после прожарки: каждый шаг теперь
# назван КОМАНДОЙ — раньше первый шаг назывался «повторить статус», и студент
# честно написал, что не знает, чем его повторяют.
im = Image.new("RGB", (MW, 436), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "Не работает — порядок в проверках и здесь часть ответа", 25, DEEP, b=True)
STEPS = [(GOLD, "1 ·  claude mcp list", "первые тридцать секунд статус\nкрасный, пока качается пакет"),
         (TEAL, "2 ·  именной вызов", "«используя сервер github…» —\nответ подписан именем сервера"),
         (LIGHT, "3 ·  claude mcp get github", "строка Issue:  401/403 — права,\n404/405 — путь, пусто — сеть"),
         (DEEP, "4 ·  запуск в терминале", "ту же команду npx — руками:\nоба наших отказа нашлись тут")]
cw, gap = 360, 32
for i, (c, head, sub) in enumerate(STEPS):
    x = (MW - (4 * cw + 3 * gap)) // 2 + i * (cw + gap)
    d.rounded_rectangle([x, 48, x + cw, 186], radius=12, fill=c)
    tc = DEEP if c is GOLD else W
    hw = d.textlength(head, font=f(20, True, m=True))
    d.text((x + (cw - hw) / 2, 66), head, font=f(20, True, m=True), fill=tc)
    for k, ln in enumerate(sub.split("\n")):
        lw = d.textlength(ln, font=f(19)); d.text((x + (cw - lw) / 2, 110 + k * 28), ln, font=f(19), fill=tc)
    if i < 3: arrow(d, x + cw + 4, 117, x + cw + gap - 4, 117)
mcent(d, 202, "Начать с журнала отладки — самый дорогой шаг первым: он отвечает на то,", 21, RED)
mcent(d, 228, "что первые четыре закрыли бы за минуту.", 21, RED)
mpanel(d, 60, 268, MW - 120, 152, None, fill=SURF, stroke=MUTE)
mcent(d, 286, "Зелёный статус проверяет ровно ОДИН класс отказа из четырёх — поднялся ли процесс.", 22, DEEP)
for k, ln in enumerate(["сервер отвечает «успех», не делая заявленного — не видит",
                        "доступ отозван, связь при этом жива — не видит",
                        "подключён, но ни один инструмент до модели не дошёл — отдельной строкой, если список не получен"]):
    d.ellipse([92, 328 + k * 30, 104, 340 + k * 30], fill=MUTE)
    mtext(d, 120, 322 + k * 30, ln, 20, INK)
print(msave(im, "mcp-poryadok-otladki.png"))
