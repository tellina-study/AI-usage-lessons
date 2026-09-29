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
