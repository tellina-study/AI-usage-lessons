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

# ── s34. Ручной цикл: то, что нужно агенту, лежит снаружи ──────────────────
im = Image.new("RGB", (MW, 350), W); d = ImageDraw.Draw(im)
mtext(d, 20, 12, "Один и тот же цикл — несколько раз в неделю", 25, DEEP, b=True)
xs = mrow(d, 58, [("Заказчик заводит\nissue в трекере", MID),
                  ("Разработчик\nоткрывает браузер", LIGHT),
                  ("Текст issue —\nв чат агенту", GOLD),
                  ("Агент готовит\nправку", TEAL),
                  ("Ответ — обратно\nв комментарий", GOLD)], 270, 112, 50, sz=20)
d.line([xs[-1]+135, 170, xs[-1]+135, 212], fill=MUTE, width=3)
d.line([xs[-1]+135, 212, xs[0]+135, 212], fill=MUTE, width=3)
arrow(d, xs[0]+135, 212, xs[0]+135, 176, col=MUTE)
mcent(d, 222, "цикл повторяется целиком, вручную", 20, MUTE)
mcent(d, 268, "Правило, барьер, процедура — внутри репозитория, в файлах.", 23, INK)
mcent(d, 302, "Список открытых задач — снаружи, и меняется без разработчика.", 23, INK)
print(msave(im, "s34-ruchnoy-tsikl.png"))

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
print(msave(im, "s37-poryadok-treh-proverok.png"))

# ── s38. Вычёркивание прав под названные операции ──────────────────────────
im = Image.new("RGB", (MW, 460), W); d = ImageDraw.Draw(im)
mtext(d, 20, 10, "Права вычёркиваются под названные операции, а не выдаются впрок", 25, DEEP, b=True)
mpanel(d, 25, 56, 620, 300, "Агент должен уметь")
for i, t in enumerate(["читать открытые issue", "писать комментарий к issue", "создавать черновик правки"]):
    mtext(d, 50, 112+i*44, "•  " + t, 23, INK)
mtext(d, 50, 262, "Ничего про удаление, про настройки", 20, MUTE)
mtext(d, 50, 288, "репозитория, про другие репозитории.", 20, MUTE)
mpanel(d, 745, 56, 830, 300, "Широкий персональный токен даёт", stroke=RED)
rows = [("все репозитории пользователя, включая приватные", True),
        ("чтение и запись", False), ("управление настройками", True), ("удаление", True)]
for i, (t, st) in enumerate(rows):
    mtext(d, 772, 112+i*44, t, 23, MUTE if st else INK, strike=st)
mtext(d, 772+d.textlength("чтение и запись", font=f(23))+22, 158, "→ только этот репозиторий", 20, TEAL, b=True)
mtext(d, 772, 296, "вопрос по каждой строке: наш список из трёх этого требует?", 20, MUTE)
arrow(d, 660, 200, 730, 200, col=DEEP, label="нужно?")
box(d, 25, 382, MW-50, 62, "Остаётся: один репозиторий  ·  чтение issue  ·  создание черновика правки", GOLD, tc=DEEP, sz=24)
print(msave(im, "s38-vycherkivanie-prav.png"))

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
print(msave(im, "s40-anatomiya-mcp-json.png"))

# Прежние схемы s41 (области видимости), s47 (что грузится) и s42 (статус)
# удалены вместе со слиянием тактов: их содержание живёт в двух новых схемах
# ниже — s41-ot-fayla-do-instrumenta и s42-poryadok-otladki.

# ── s43. Эксфильтрация в связке и смертельное трио ─────────────────────────
# Золото по грамматике деки = ЦЕЛЕВОЙ ОТВЕТ. Здесь оно стояло дважды и оба
# раза не на нём: рамкой вокруг строки прав, которую мы ВЫЧЁРКИВАЕМ, и на
# переломном шаге самой атаки. Теперь золото на фигуре ровно одно — на исходе,
# ради которого вычёркивание делалось; шаги цепочки красные там, где это
# действие атакующего или его результат, и синие там, где агент честно делает
# ровно то, что от него ждут.
im = Image.new("RGB", (MW, 500), W); d = ImageDraw.Draw(im)
mtext(d, 20, 8, "Утечка без единой строчки эксплойта — и что делает её невозможной", 25, DEEP, b=True)
mrow(d, 50, [("публичный issue\nс инструкцией внутри", RED), ("агент читает\nоткрытые задачи", MID),
             ("инструкция в контексте\nкак обычная задача", RED), ("широкий токен —\nчитает приватные", LIGHT),
             ("публикует в публичном\nчерновике правки", RED)], 280, 108, 40, sz=19)
trio = ["доступ к приватным данным", "недоверенный внешний текст", "канал наружу"]
for i, t_ in enumerate(trio):
    box(d, 105+i*480, 194, 430, 92, t_, TEAL, sz=21)
for i in range(2): mtext(d, 553+i*480, 224, "+", 34, DEEP, b=True)

# Ход, а не факт: подпись называет, что именно сделано, и золото — на исходе.
mpanel(d, 105, 308, 1390, 92, None, fill=SURF, stroke=LIGHT)
mtext(d, 130, 318, "ход, который мы уже сделали на этом занятии:", 19, MUTE)
w = mtext(d, 130, 350, "вычеркнули «все репозитории, включая приватные»", 22, MUTE, strike=True)
arrow(d, 130+w+24, 364, 130+w+94, 364, col=MID)
res = "сценарий не проходит: читать нечего"
rw = d.textlength(res, font=f(22, True))
d.rounded_rectangle([130+w+112, 342, 130+w+152+rw, 386], radius=10, fill=GOLD)
mtext(d, 130+w+132, 350, res, 22, DEEP, b=True)

mpanel(d, 105, 418, 1390, 64, None, fill=SURF, stroke=RED)
mcent(d, 430, "Без модели вообще: сетевой вход сервера слушает без проверки, кто обратился,", 20, INK)
mcent(d, 454, "а защита от чужих сайтов обходится подменой DNS — 2 запроса, 0 учётных данных.", 20, INK)
print(msave(im, "s43-svyazka-treh-usloviy.png"))


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
        "использования в дикой природе не зафиксировано: это знание про устройство, не про частоту"]),
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
print(msave(im.crop((0, 0, MW, y + gh + 12)), "s36-lestnitsa-svidetelstv.png"))

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
print(msave(im, "s41-ot-fayla-do-instrumenta.png"))

# ── s42. Порядок отладки: тот же приём, что на s37 ─────────────────────────
# Ревью назвало s37 образцом: целевой ответ там не карточка, а ПОРЯДОК —
# нумерованные ворота, золото на первом, красная строка про частый неверный
# старт, приглушённая панель про то, что ответом не является. Здесь ровно та
# же грамматика приложена к отладке: раздел доводил до диагноза и обрывался.
im = Image.new("RGB", (MW, 430), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "Не работает — порядок в проверках и здесь часть ответа", 25, DEEP, b=True)
STEPS = [(GOLD, "1 · Повторить статус", "первая проверка честно\nврёт, пока качается пакет"),
         (TEAL, "2 · Именной вызов", "«используя этот сервер…» —\nдоказывает работу, не транспорт"),
         (LIGHT, "3 · Строка Issue:", "401/403 — авторизация,\n404/405 — путь, пусто — сеть"),
         (DEEP, "4 · Запуск команды", "прямо в терминале —\nоба отказа нашлись тут")]
cw, gap = 360, 32
for i, (c, head, sub) in enumerate(STEPS):
    x = (MW - (4 * cw + 3 * gap)) // 2 + i * (cw + gap)
    d.rounded_rectangle([x, 48, x + cw, 186], radius=12, fill=c)
    tc = DEEP if c is GOLD else W
    hw = d.textlength(head, font=f(22, True)); d.text((x + (cw - hw) / 2, 66), head, font=f(22, True), fill=tc)
    for k, ln in enumerate(sub.split("\n")):
        lw = d.textlength(ln, font=f(20)); d.text((x + (cw - lw) / 2, 108 + k * 30), ln, font=f(20), fill=tc)
    if i < 3: arrow(d, x + cw + 4, 117, x + cw + gap - 4, 117)
mcent(d, 202, "Начать с лога — самый дорогой шаг первым: он отвечает на то,", 21, RED)
mcent(d, 228, "что первые четыре уже закрыли бы за минуту.", 21, RED)
mpanel(d, 60, 268, MW - 120, 146, None, fill=SURF, stroke=MUTE)
mcent(d, 286, "Зелёный статус проверяет ровно ОДИН класс отказа из четырёх — поднялся ли процесс.", 22, DEEP)
for k, ln in enumerate(["сервер отвечает «успех», не делая заявленного — не видит",
                        "доступ отозван, транспорт формально жив — не видит",
                        "подключён, но ни один инструмент не доступен модели — отдельной строкой, если список не получен"]):
    d.ellipse([92, 328 + k * 30, 104, 340 + k * 30], fill=MUTE)
    mtext(d, 120, 322 + k * 30, ln, 20, INK)
print(msave(im, "s42-poryadok-otladki.png"))
