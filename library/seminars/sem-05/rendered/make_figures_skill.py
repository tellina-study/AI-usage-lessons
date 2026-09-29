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

# ─────────────────────────────────────────────────────────────────────────────
# Раздел «скилл» (s24–s37) — схемы механики. Имена файлов: sNN-*.png
# ─────────────────────────────────────────────────────────────────────────────
WARN=[]
def lbox(d,x,y,w,h,lines,fc,tc=INK,sz=21,pad=20,b=False,m=False):
    d.rounded_rectangle([x,y,x+w,y+h],radius=10,fill=fc)
    fo=f(sz,b,m); th=len(lines)*(sz+9)-9; cy=y+(h-th)//2
    for i,ln in enumerate(lines):
        if d.textlength(ln,font=fo)>w-2*pad: WARN.append(f"шире блока: {ln[:48]!r}")
        d.text((x+pad,cy+i*(sz+9)),ln,font=fo,fill=tc)
def cbox(d,x,y,w,h,txt,fc,tc=W,sz=21,b=True,m=False):
    fo=f(sz,b,m)
    for ln in txt.split("\n"):
        if d.textlength(ln,font=fo)>w-16: WARN.append(f"шире блока: {ln[:48]!r}")
    box(d,x,y,w,h,txt,fc,tc=tc,sz=sz,b=b,m=m)
def cline(d,y,txt,sz=21,col=INK,b=False,Wd=2400):
    fo=f(sz,b)
    if d.textlength(txt,font=fo)>Wd-60: WARN.append(f"шире канвы: {txt[:48]!r}")
    center(d,y,txt,sz,col,b,Wd)

# ── s32. Три уровня загрузки ─────────────────────────────────────────────────
im=Image.new("RGB",(2400,620),W); d=ImageDraw.Draw(im)
d.text((40,16),"Три уровня загрузки: что уже в контексте, что попадёт позже, а что не попадёт никогда",
       font=f(23,True),fill=DEEP)
bands=[(70,GOLD,DEEP,["Уровень 1","метаданные"],
        ["всегда, при старте сессии,","для каждого установленного скилла"],
        ["в системном промпте — только имя и описание.","Больше ничего: ни первой строки тела, ни списка файлов."]),
       (240,LIGHT,W,["Уровень 2","тело SKILL.md"],
        ["только после того, как описание","совпало с запросом"],
        ["одно сообщение в истории диалога;","на следующих ходах повторно не перечитывается."]),
       (410,TEAL,W,["Уровень 3","вложения и код"],
        ["только при обращении","из тела скилла"],
        ["вспомогательный файл — целиком при чтении.","Код скрипта не попадает вовсе — только его вывод."])]
for y,fc,tc,lab,when,what in bands:
    cbox(d,40,y,520,150,"\n".join(lab),fc,tc=tc,sz=23)
    lbox(d,600,y,680,150,when,SURF,sz=21)
    lbox(d,1320,y,1040,150,what,SURF,sz=21)
cline(d,578,"Иллюстрация, не измерение: 13 скиллов × ≈100 токенов ≈ 1300 на весь перечень; бюджет 1% окна на 200 000 ≈ 2000 — обрезка не наступает.",21,MUTE)
im.save(OUT/"s32-tri-urovnya.png")

# ── s33. Подстановка по умолчанию ────────────────────────────────────────────
im=Image.new("RGB",(2400,740),W); d=ImageDraw.Draw(im)
d.text((40,14),"Условие, при котором фронтматтер вообще читается — и что подставляется, когда его нет",
       font=f(23,True),fill=DEEP)
d.text((40,62),"есть фронтматтер — 1 скилл из 13",font=f(20,True),fill=TEAL)
lbox(d,40,92,1080,210,["---                       ← первая строка файла",
                       "name: pre-user-gate",
                       "description: Pre-USER-GATE walkthrough …",
                       "---"],SURF,sz=20,m=True)
arrow(d,1130,197,1230,197,TEAL)
lbox(d,1250,92,1110,210,["открывающая --- стоит первой строкой →",
                         "фронтматтер читается",
                         "имя и описание — из своих полей"],(0xE4,0xF2,0xF0),sz=22,tc=INK)
d.text((40,338),"фронтматтера нет — 12 скиллов из 13",font=f(20,True),fill=RED)
lbox(d,40,368,1080,210,["# build-deck        ← эта строка и станет описанием",
                        "",
                        "Build/rebuild a PowerPoint presentation …",
                        "                    ← а годилась бы вот эта"],SURF,sz=20,m=True)
arrow(d,1130,473,1230,473,RED)
lbox(d,1250,368,1110,210,["--- первой строкой нет → парсер не запускается",
                          "имя ← имя каталога",
                          "описание ← ПЕРВАЯ НЕПУСТАЯ СТРОКА"],(0xF7,0xE6,0xE4),sz=22,tc=INK)
cline(d,606,"Снаружи похоже на «описание = имя». Механизм другой: берётся не имя, а не та строка — совпадает с именем лишь потому, что файл открывает «# имя-скилла».",20,INK)
cline(d,644,"В этом репозитории курса — 12 из 13. Проверяется одной командой:   head -5 .claude/skills/*/SKILL.md",20,MUTE)
cline(d,682,"Опечатка в имени поля (descripton) ошибки не даёт: YAML валиден, поле молча не срабатывает. Не подтверждено: обрезается ли ведущая «#» при подстановке.",20,MUTE)
im.save(OUT/"s33-podstanovka.png")

# ── s34. Порядок отладки ─────────────────────────────────────────────────────
im=Image.new("RGB",(2400,470),W); d=ImageDraw.Draw(im)
d.text((40,12),"Порядок вопросов, а не порядок команд",font=f(23,True),fill=DEEP)
steps=[(40,MID,W,"/skills",["виден ли скилл","системе вообще"]),
       (620,LIGHT,W,"/deploy",["сработал явный вызов,","а словами — нет → дело в описании"]),
       (1200,TEAL,W,"claude --debug",["не сработал и явный вызов →","ошибка разбора YAML"]),
       (1780,GOLD,DEEP,"/skill-doctor",["сработал не тот из похожих →","стоимость и частота вызовов"])]
for x,fc,tc,cmd,cap in steps:
    cbox(d,x,58,540,96,cmd,fc,tc=tc,sz=25,m=True)
    lbox(d,x,166,540,96,cap,SURF,sz=19)
for i in range(3): arrow(d,steps[i][0]+540,106,steps[i+1][0],106)
cline(d,300,"Отдельно: /context — сколько перечень скиллов занял в этой сессии, уже после обрезки, а не сумма полных описаний.",21,INK)
cline(d,342,"Пропустить первый шаг и сразу читать тело файла — самая частая потеря времени: половина причин лежит вне содержимого.",21,MUTE)
cline(d,398,"Ни один из четырёх не скажет «скилл выбран неверно»: это видно только по частоте вызовов, и только если спросить.",21,RED,b=True)
im.save(OUT/"s34-otladka.png")

# ── s35. Два слоя вреда ──────────────────────────────────────────────────────
im=Image.new("RGB",(2400,600),W); d=ImageDraw.Draw(im)
d.text((40,12),"Слой 1 — вред от сработавшего скилла. База сравнения — тот же набор задач без него",
       font=f(23,True),fill=DEEP)
cbox(d,40,60,400,140,"те же задачи,\nтот же агент",MID,sz=22)
lbox(d,490,58,400,64,["прогон без скилла"],SURF,sz=21)
lbox(d,490,136,400,64,["прогон со скиллом"],SURF,sz=21)
arrow(d,440,130,486,92); arrow(d,440,130,486,166)
arrow(d,890,130,946,130)
cbox(d,950,60,420,140,"разница =\n307 случаев вреда",GOLD,tc=DEEP,sz=22)
arrow(d,1370,130,1426,92); arrow(d,1370,130,1426,166)
lbox(d,1430,52,420,72,["125 функциональных провалов"],(0xE4,0xF2,0xF0),sz=20)
lbox(d,1430,136,420,72,["182 регрессии по стоимости"],(0xE4,0xF2,0xF0),sz=20)
arrow(d,1850,88,1906,88)
lbox(d,1910,44,450,88,["86 из 125 = 68,8% —","от скиллов, что выглядели нужными"],(0xF7,0xE6,0xE4),sz=19)
cline(d,222,"Рядом, две другие работы: +451% токенов на задачу (49 скиллов, 565 задач) · падение успеха на 16 задачах из 84 того же набора.",20,MUTE)
d.text((40,276),"Слой 2 — скилл это каталог с исполняемым кодом: одобрение разовое, права постоянные",
       font=f(23,True),fill=DEEP)
l2=[(40,"скилл = каталог,\nв нём могут лежать скрипты"),(820,"агент запускает их\nс правами вашей сессии"),
    (1600,"одобряется один раз,\nправа живут сколько угодно")]
for i,(x,t) in enumerate(l2):
    cbox(d,x,324,720,124,t,LIGHT,sz=21)
    if i<2: arrow(d,x+720,386,x+778,386)
cline(d,474,"Официальный открытый скилл Anthropic «GIF Creator»: одна вставленная функция — тихая загрузка и запуск программы-шифровальщика.",20,INK)
cline(d,512,"Снаружи — тот же конвертер картинок: ни описание, ни видимое поведение не изменились.",20,INK)
cline(d,556,"Проверок после одобрения не происходит: это установка чужого программного обеспечения, а не чтение чужого текста.",20,RED,b=True)
im.save(OUT/"s35-vred.png")

print("схемы раздела «скилл»:", *[p.name for p in sorted(OUT.glob('s3*.png'))])
if WARN:
    print("ПРЕДУПРЕЖДЕНИЯ ПО ШИРИНЕ:", len(WARN))
    for w in dict.fromkeys(WARN): print("  -", w)
else:
    print("по ширине всё влезло")
