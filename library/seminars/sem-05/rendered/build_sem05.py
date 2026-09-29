#!/usr/bin/env python3
"""
Финальный рендер деки Семинара 5 из source-of-truth: ../deck.yaml + ../slides/sNN-*.md

Раскладка выбирается по типу слайда: таблицы становятся настоящими таблицами,
блоки кода — моноширинными карточками, карточки-варианты — плашками, цитаты —
блоками в золотой рамке. Текст берётся из секции `## Visual` один к одному;
заметки — из `## Speaker notes`. Ничего не досочиняется.

Палитра Ocean Gradient (зафиксирована курсом), канва 16:9.
"""
import re, yaml
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import slide_parts as SP

DEEP, MID, LIGHT = RGBColor(0x21,0x29,0x5C), RGBColor(0x06,0x5A,0x82), RGBColor(0x1C,0x72,0x93)
TEAL, GOLD, SURF = RGBColor(0x02,0x80,0x90), RGBColor(0xF0,0xAB,0x00), RGBColor(0xF4,0xF7,0xFA)
WHITE, INK, MUTE = RGBColor(0xFF,0xFF,0xFF), RGBColor(0x14,0x1B,0x2E), RGBColor(0x5B,0x6B,0x7F)
CODEBG = RGBColor(0x18,0x20,0x3A)

root = Path(__file__).resolve().parent.parent
deck = yaml.safe_load((root/"deck.yaml").read_text(encoding="utf-8"))
DARK = {"hero_cover","section_divider","keystone_axis","closing_question"}
STAGES = [("Хук","s08"),("Скилл","s24"),("MCP","s38")]

prs = Presentation(); prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
BLANK = prs.slide_layouts[6]

def bg(sl,c):
    f=sl.background.fill; f.solid(); f.fore_color.rgb=c
def rect(sl,l,t,w,h,fill=None,line=None,rounded=True):
    sh=sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,l,t,w,h)
    if fill: sh.fill.solid(); sh.fill.fore_color.rgb=fill
    else: sh.fill.background()
    if line: sh.line.color.rgb=line; sh.line.width=Pt(1.25)
    else: sh.line.fill.background()
    sh.shadow.inherit=False; return sh
def txt(sl,l,t,w,h,lines,size,color,bold=False,align=PP_ALIGN.LEFT,anchor=MSO_ANCHOR.TOP,mono=False,spc=4):
    tb=sl.shapes.add_textbox(l,t,w,h); tf=tb.text_frame; tf.word_wrap=True; tf.vertical_anchor=anchor
    ls = lines if isinstance(lines,list) else [lines]
    for i,ln in enumerate(ls):
        p = tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.text=ln; p.alignment=align
        p.font.size=Pt(size); p.font.bold=bold; p.font.color.rgb=color
        p.font.name = "Consolas" if mono else "Arial"
        p.space_after=Pt(spc)
    return tb
def table(sl,rows,l,t,w,h,fs=12):
    ncol=max(len(r) for r in rows); nrow=len(rows)
    gt=sl.shapes.add_table(nrow,ncol,l,t,w,h).table
    for j,cell in enumerate(rows[0]):
        c=gt.cell(0,j); c.text=cell
        for p in c.text_frame.paragraphs:
            p.font.size=Pt(fs); p.font.bold=True; p.font.color.rgb=WHITE; p.font.name="Arial"
        c.fill.solid(); c.fill.fore_color.rgb=MID
    for i,row in enumerate(rows[1:],1):
        for j in range(ncol):
            c=gt.cell(i,j); c.text=row[j] if j<len(row) else ""
            for p in c.text_frame.paragraphs:
                p.font.size=Pt(fs); p.font.color.rgb=INK; p.font.name="Arial"
            c.fill.solid(); c.fill.fore_color.rgb=WHITE if i%2 else SURF
    return gt
def roadmap(sl,cur):
    x=Inches(0.55)
    for name,sid in STAGES:
        on = sid==cur
        rect(sl,x,Inches(6.62),Inches(2.25),Inches(0.42),fill=GOLD if on else RGBColor(0x2E,0x3A,0x6B))
        txt(sl,x,Inches(6.66),Inches(2.25),Inches(0.36),[name],13,DEEP if on else RGBColor(0x9F,0xAE,0xC4),
            bold=on,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        x+=Inches(2.45)

FIGS={"s09":"khuk-scene.png","s13":"khuk-cobuild.png","s16":"lifecycle.png",
      "s17":"khuk-stdin.png","s18":"contract.png","s19":"khuk-debug.png",
      "s20":"bypass.png","s21":"khuk-blindspot.png"}
TAGS={"s08":"1 кейс · 2 слоя провала · 5 форм обхода",
      "s24":"1 кейс · 2 слоя провала · 6 причин молчания",
      "s38":"1 кейс · 3 слоя провала · 3 области видимости"}

def render(sl, stype, sid, title, blocks):
    figdir = Path(__file__).parent/"figures"
    cand = sorted(figdir.glob(f"{sid}.png")) + sorted(figdir.glob(f"{sid}-*.png"))
    if not cand and sid in FIGS and (figdir/FIGS[sid]).exists():
        cand=[figdir/FIGS[sid]]
    fig = cand[0] if cand else None
    tables=[b for k,b in blocks if k=="table"]; codes=[b for k,b in blocks if k=="code"]
    quotes=[b for k,b in blocks if k=="quote"]; cards=[b for k,b in blocks if k=="cards"]
    bullets=[b for k,b in blocks if k=="bullets"]; paras=[b for k,b in blocks if k=="para"]

    if stype in DARK:
        bg(sl,DEEP); rect(sl,Inches(0),Inches(2.62),Inches(13.333),Inches(0.08),fill=GOLD,rounded=False)
        txt(sl,Inches(0.9),Inches(1.15),Inches(11.5),Inches(1.35),[title],38,WHITE,bold=True,anchor=MSO_ANCHOR.BOTTOM)
        y=Inches(3.0)
        if quotes:
            rect(sl,Inches(0.9),y,Inches(11.5),Inches(1.75),fill=RGBColor(0x2A,0x34,0x70),line=GOLD)
            txt(sl,Inches(1.2),y+Inches(0.18),Inches(10.9),Inches(1.4),quotes[0][:4],19,WHITE,anchor=MSO_ANCHOR.MIDDLE)
            y+=Inches(2.0)
        if tables:
            table(sl,tables[0][:6],Inches(0.9),y,Inches(11.5),Inches(2.4),fs=12); y+=Inches(2.5)
        elif cards:
            x=Inches(0.9); cw=Inches(11.5/len(cards[0]))-Inches(0.12)
            for it in cards[0]:
                rect(sl,x,y,cw,Inches(0.85),fill=RGBColor(0x2A,0x34,0x70),line=LIGHT)
                txt(sl,x+Inches(0.08),y+Inches(0.08),cw-Inches(0.16),Inches(0.7),[it],12,WHITE,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
                x+=cw+Inches(0.12)
            y+=Inches(1.05)
        elif paras:
            txt(sl,Inches(0.9),y,Inches(11.5),Inches(1.3),paras[:3],18,RGBColor(0xD6,0xE2,0xEC))
            y+=Inches(1.45)
        if stype=="section_divider":
            if sid in TAGS:
                # тег идёт ПОД содержимым дивайдера, а не поверх него
                txt(sl,Inches(0.9),y,Inches(11.5),Inches(0.5),[TAGS[sid]],17,GOLD,bold=True)
            roadmap(sl,sid)
        return

    bg(sl,WHITE)
    rect(sl,Inches(0),Inches(0),Inches(13.333),Inches(1.02),fill=DEEP,rounded=False)
    rect(sl,Inches(0),Inches(1.02),Inches(13.333),Inches(0.055),fill=GOLD,rounded=False)
    txt(sl,Inches(0.55),Inches(0.14),Inches(12.2),Inches(0.78),[title],24,WHITE,bold=True,anchor=MSO_ANCHOR.MIDDLE)
    txt(sl,Inches(12.0),Inches(6.95),Inches(1.0),Inches(0.32),[sid],11,MUTE,align=PP_ALIGN.RIGHT)
    y=Inches(1.35); bottom=Inches(6.80); L=Inches(0.55); WIDTH=Inches(12.2)

    if fig:
        from PIL import Image as _I
        iw,ih=_I.open(fig).size
        fh=min(Inches(12.2*ih/iw), bottom-y-Inches(0.2))
        sl.shapes.add_picture(str(fig), L, y, width=int(fh*iw/ih))
        y += fh + Inches(0.16)

    # блоки выводятся В ПОРЯДКЕ ИСТОЧНИКА и ВСЕ, пока есть вертикальный бюджет
    for kind,b in blocks:
        if y >= bottom - Inches(0.3): break
        avail = bottom - y
        if kind=="quote":
            lines=b[:5]; h=min(avail,Inches(0.34*len(lines)+0.34))
            rect(sl,L,y,WIDTH,h,fill=RGBColor(0xFF,0xF7,0xE2),line=GOLD)
            txt(sl,L+Inches(0.3),y+Inches(0.1),WIDTH-Inches(0.6),h-Inches(0.2),lines,15,INK,anchor=MSO_ANCHOR.MIDDLE)
            y+=h+Inches(0.14)
        elif kind=="cards":
            items=b; cw=(WIDTH-Inches(0.1)*(len(items)-1))/max(len(items),1)
            h=min(avail,Inches(0.92)); x=L
            for it in items:
                rect(sl,x,y,cw,h,fill=SURF,line=LIGHT)
                txt(sl,x+Inches(0.07),y+Inches(0.06),cw-Inches(0.14),h-Inches(0.12),[it],11.5,INK,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
                x+=cw+Inches(0.1)
            y+=h+Inches(0.16)
        elif kind=="table":
            rows=[r[:5] for r in b]; keep=min(len(rows),9)
            h=min(avail,Inches(0.40*keep+0.2))
            table(sl,rows[:keep],L,y,WIDTH,h,fs=11 if len(rows[0])>3 else 12)
            y+=h+Inches(0.16)
        elif kind=="code":
            code=[c[:104] for c in b[:16]]; h=min(avail,Inches(0.225*len(code)+0.26))
            rect(sl,L,y,WIDTH,h,fill=CODEBG,line=LIGHT)
            txt(sl,L+Inches(0.22),y+Inches(0.11),WIDTH-Inches(0.44),h-Inches(0.2),code,11,RGBColor(0xE8,0xEF,0xF7),mono=True,spc=1)
            y+=h+Inches(0.14)
        elif kind=="bullets":
            items=["• "+x for x in b[:8]]; h=min(avail,Inches(0.32*len(items)+0.26))
            rect(sl,L,y,WIDTH,h,fill=SURF,line=LIGHT)
            txt(sl,L+Inches(0.3),y+Inches(0.1),WIDTH-Inches(0.6),h-Inches(0.2),items,13.5,INK,spc=3)
            y+=h+Inches(0.14)
        # 'para' — спецификация для дизайнера, на слайд не выводится никогда

built=0
for s in deck["slides"]:
    md=(root/s["file"]).read_text(encoding="utf-8")
    title,_,visual,notes = SP.sections(md)
    sl=prs.slides.add_slide(BLANK)
    render(sl, s.get("type",""), s["id"], title or s["id"], SP.blocks(visual))
    if notes: sl.notes_slide.notes_text_frame.text=notes
    built+=1

out=Path(__file__).parent/"sem-05.pptx"; prs.save(out)
print(f"слайдов: {built}   файл: {out.name} ({out.stat().st_size//1024} КБ)")
