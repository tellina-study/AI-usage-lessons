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

# 1. Где сидит перехват
im=Image.new("RGB",(2400,640),W); d=ImageDraw.Draw(im)
d.text((20,18),"33 события жизненного цикла · в работе у инженера — четыре",font=f(22),fill=MUTE)
xs=[40,520,1000,1480,1960]; labels=[("Агент решил\nвызвать инструмент",MID),("PreToolUse\nперехват",GOLD),
    ("Инструмент\nисполняется",LIGHT),("PostToolUse\nперехват",TEAL),("Ответ\nагента",MID)]
for x,(t,c) in zip(xs,labels):
    box(d,x,110,400,150,t,c,tc=DEEP if c==GOLD else W,sz=21)
for i in range(4): arrow(d,xs[i]+400,185,xs[i+1],185)
box(d,520,330,400,110,"решение\nдо действия",SURF,tc=INK,sz=20,b=False)
arrow(d,720,268,720,326,GOLD)
center(d,500,"Перехват «до вызова» — единственная точка, где действие ещё не произошло.",22)
center(d,540,"После вызова барьер может сообщить, но остановить уже нет.",22)
im.save(OUT/"lifecycle.png")

# 2. Контракт входа и выхода
im=Image.new("RGB",(2400,760),W); d=ImageDraw.Draw(im)
box(d,60,90,560,170,"агент",MID,sz=26)
box(d,920,90,560,170,"хук\n(ваш код)",GOLD,tc=DEEP,sz=26)
box(d,1780,90,560,170,"агент",MID,sz=26)
arrow(d,620,175,920,175,label="на stdin: JSON")
arrow(d,1480,175,1780,175,label="на stdout: решение")
inp=["session_id","cwd","permission_mode","hook_event_name","tool_name","tool_input.command"]
for i,t in enumerate(inp): d.text((120,310+i*38),"• "+t,font=f(21,m=True),fill=INK)
outp=['permissionDecision:','  deny  — не выполнять','  ask   — спросить человека','  пусто — разрешить']
for i,t in enumerate(outp): d.text((1830,310+i*38),t,font=f(21,m=True),fill=INK)
center(d,600,"Два способа ответить: код возврата или объект на stdout.",22)
center(d,640,"Объект несёт причину, которую увидит агент; код возврата — нет.",22)
im.save(OUT/"contract.png")

# 3. Пять форм, на которых барьер молчит
im=Image.new("RGB",(2400,820),W); d=ImageDraw.Draw(im)
rows=[("git commit","защищённая ветка","ОТКАЗ",GOLD),
      ("git -C . commit","та же ветка","проходит",RED),
      ("/usr/bin/git commit","абсолютный путь","проходит",RED),
      ("env git commit","префикс команды","проходит",RED),
      ("cd . ⏎ git commit","вторая строка","проходит",RED),
      ("git commit","ветка названа trunk","проходит",RED)]
y=60
for cmd,note,verd,col in rows:
    d.text((60,y+18),cmd,font=f(26,m=True),fill=INK)
    d.text((980,y+22),note,font=f(21),fill=MUTE)
    box(d,1700,y,330,62,verd,col,tc=DEEP if col==GOLD else W,sz=21)
    y+=112
center(d,740,"Самотест печатает это сам: 9 проверок пройдено, 5 случаев — барьер молчит по построению.",22)
im.save(OUT/"bypass.png")
print("схемы:", *[p.name for p in sorted(OUT.glob('*.png'))])

# ═══════════════════════════════════════════════════════════════════════════
# Схемы раздела «MCP: доступ наружу» (s39–s50). Холст 1600 px = 12,2 дюйма
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

# ── s39. Ручной цикл: то, что нужно агенту, лежит снаружи ──────────────────
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
print(msave(im, "s39-ruchnoy-tsikl.png"))

# ── s42. Порядок трёх проверок ─────────────────────────────────────────────
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
print(msave(im, "s42-poryadok-treh-proverok.png"))

# ── s43. Вычёркивание прав под названные операции ──────────────────────────
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
print(msave(im, "s43-vycherkivanie-prav.png"))

# ── s45. Анатомия .mcp.json ────────────────────────────────────────────────
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
print(msave(im, "s45-anatomiya-mcp-json.png"))

# ── s46. Области видимости, приоритет, исполняемая команда ─────────────────
im = Image.new("RGB", (MW, 500), W); d = ImageDraw.Draw(im)
mtext(d, 20, 8, "Область видимости — это три физически разных файла", 25, DEEP, b=True)
cards = [(15, "local — по умолчанию", ["личная запись,", "только этот проект"], "не коммитится", LIGHT),
         (550, "project", ["файл .mcp.json", "в корне репозитория"], "коммитится — виден всем, кто клонирует", GOLD),
         (1085, "user", ["личная запись,", "все ваши проекты"], "не коммитится", LIGHT)]
for x, t, body, foot, col in cards:
    mpanel(d, x, 48, 500, 142, None, fill=SURF, stroke=col)
    mtext(d, x+20, 60, t, 23, DEEP, b=True)
    for j, ln in enumerate(body): mtext(d, x+20, 94+j*26, ln, 20, INK)
    mtext(d, x+20, 152, foot, 18, DEEP if col == GOLD else MUTE, b=(col == GOLD))
mtext(d, 20, 204, "Приоритет при совпадении имени — левее значит выше:", 20, MUTE)
prio = ["политика организации", "local", "project", "user", "плагин", "коннектор"]
for i, t in enumerate(prio):
    box(d, 21+i*262, 232, 248, 48, t, MID if i == 0 else LIGHT, sz=17)
    if i < 5: d.polygon([(283+i*262, 256), (269+i*262, 249), (269+i*262, 263)], fill=MUTE)
box(d, 15, 306, 440, 66, '"command": "npx  …"', CODEBG, sz=21, m=True)
arrow(d, 468, 339, 538, 339, col=DEEP)
box(d, 552, 306, 500, 66, "при старте сессии запускается\nпроцесс на вашей машине", TEAL, sz=20)
mtext(d, 1085, 306, "пакет заранее не проверяется:", 20, RED, b=True)
mtext(d, 1085, 332, "что записано в command —", 20, INK)
mtext(d, 1085, 356, "то и будет выполнено", 20, INK)
mpanel(d, 15, 398, MW-30, 62, None, fill=SURF, stroke=MUTE)
mcent(d, 416, "http — рекомендованный способ для удалённых серверов  ·  sse официально помечен устаревшим", 21, INK)
print(msave(im, "s46-oblasti-vidimosti.png"))

# ── s47. Что грузится при старте, что — по требованию ──────────────────────
im = Image.new("RGB", (MW, 430), W); d = ImageDraw.Draw(im)
mtext(d, 20, 8, "Что происходит сразу после того, как транспорт поднялся", 25, DEEP, b=True)
box(d, 40, 52, 265, 80, "Claude Code", MID, sz=22)
arrow(d, 318, 92, 735, 92, label="tools/list · prompts/list · resources/list", sz=16)
box(d, 748, 52, 265, 80, "сервер", LIGHT, sz=22)
mtext(d, 1055, 56, "спрашивает сам,", 20, DEEP, b=True)
mtext(d, 1055, 80, "без участия модели", 20, DEEP, b=True)
mtext(d, 1055, 108, "временная ошибка — до трёх повторов;", 18, MUTE)
mtext(d, 1055, 130, "ошибка авторизации не повторяется", 18, MUTE)
mpanel(d, 40, 162, 730, 132, "В контекст при старте сессии", stroke=LIGHT)
for j, t in enumerate(["имена инструментов", "инструкции сервера — общим текстом"]):
    mtext(d, 66, 212+j*32, "•  " + t, 21, INK)
mpanel(d, 830, 162, 730, 132, "По требованию модели", stroke=GOLD)
for j, t in enumerate(["полная схема конкретного инструмента —", "отдельным запросом, когда модель сама", "решит, что он может понадобиться"]):
    mtext(d, 856, 208+j*28, t, 20, INK)
box(d, 380, 316, 840, 56, "mcp__<имя-сервера>__<имя-инструмента>", CODEBG, sz=25, m=True)
mcent(d, 386, "эту форму — не короткое имя — требуют правило прав, список инструментов скилла и совпадение в хуке", 19, MUTE)
print(msave(im, "s47-chto-gruzitsya.png"))

# ── s48. Что различает статус и куда смотреть дальше ───────────────────────
im = Image.new("RGB", (MW, 560), W); d = ImageDraw.Draw(im)
mtext(d, 20, 8, "Что различает статус — и куда смотреть, когда он зелёный, а работы нет", 25, DEEP, b=True)
mpanel(d, 25, 48, 780, 232, "Статусов не два, а несколько")
st = [(TEAL, "Connected", "готов к использованию"),
      (GOLD, "Connected · tools fetch failed", "поднялся, но инструментов нет"),
      (GOLD, "Needs authentication", "жив, но требует входа"),
      (RED, "Failed to connect", "не ответил")]
for i, (c, code_t, desc) in enumerate(st):
    y = 96 + i*44
    d.rounded_rectangle([48, y+4, 64, y+20], radius=4, fill=c)
    mtext(d, 78, y, code_t, 18, INK, m=True)
    mtext(d, 450, y, desc, 19, MUTE)
mpanel(d, 830, 48, 745, 232, "Два разных таймера")
mtext(d, 856, 100, "старт сервера — 30 с", 23, DEEP, b=True)
mtext(d, 856, 130, "MCP_TIMEOUT", 18, MUTE, m=True)
mtext(d, 856, 172, "исполнение инструмента — ≈28 ч", 23, DEEP, b=True)
mtext(d, 856, 202, "MCP_TOOL_TIMEOUT", 18, MUTE, m=True)
mtext(d, 856, 240, "первая проверка честно покажет отказ, пока качается пакет", 18, MUTE)
steps = [("1 · статус\nclaude mcp list  ·  /mcp", LIGHT), ("2 · назвать сервер\nв самом запросе", TEAL),
         ("3 · включить журнал\nclaude --debug=mcp,startup", MID), ("4 · запустить команду\nиз конфигурации руками", GOLD)]
mrow(d, 316, steps, 360, 110, 40, sz=19)
mcent(d, 456, "Журнал сессии по умолчанию — ~/.claude/debug/<идентификатор-сессии>.txt", 20, INK)
mcent(d, 486, "Оба реальных отказа ниже нашлись четвёртым шагом, а не из самой сессии.", 20, MUTE)
print(msave(im, "s48-status-i-otladka.png"))

# ── s50. Эксфильтрация в связке и смертельное трио ─────────────────────────
im = Image.new("RGB", (MW, 470), W); d = ImageDraw.Draw(im)
mtext(d, 20, 8, "Утечка без единой строчки эксплойта — и что делает её невозможной", 25, DEEP, b=True)
mrow(d, 50, [("публичный issue\nс инструкцией внутри", RED), ("агент читает\nоткрытые задачи", MID),
             ("инструкция в контексте\nкак обычная задача", GOLD), ("широкий токен —\nчитает приватные", LIGHT),
             ("публикует в публичном\nчерновике правки", RED)], 280, 108, 40, sz=19)
trio = ["доступ к приватным данным", "недоверенный внешний текст", "канал наружу"]
for i, t in enumerate(trio):
    box(d, 105+i*480, 194, 430, 92, t, TEAL, sz=21)
for i in range(2): mtext(d, 553+i*480, 224, "+", 34, DEEP, b=True)
mpanel(d, 105, 308, 1390, 64, None, fill=SURF, stroke=GOLD)
w = mtext(d, 130, 326, "все репозитории, включая приватные", 22, MUTE, strike=True)
arrow(d, 140+w+20, 340, 140+w+90, 340, col=GOLD)
mtext(d, 140+w+110, 326, "сценарий не проходит: читать нечего", 22, DEEP, b=True)
mpanel(d, 105, 392, 1390, 64, None, fill=SURF, stroke=RED)
mcent(d, 404, "Без модели вообще: сетевой вход сервера слушает без проверки, кто обратился,", 20, INK)
mcent(d, 428, "а защита от чужих сайтов обходится подменой DNS — 2 запроса, 0 учётных данных.", 20, INK)
print(msave(im, "s50-svyazka-treh-usloviy.png"))
