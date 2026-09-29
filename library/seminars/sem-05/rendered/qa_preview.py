#!/usr/bin/env python3
"""Предпросмотр отрендеренных слайдов и проверка, что текст помещается в отведённые рамки.

Конвертера pptx→pdf в окружении нет, поэтому картинка собирается из реальной геометрии
готового .pptx: позиции, размеры, заливки, шрифты и текст читаются из файла, а не из исходников.
Строки переносятся по той же ширине, что задана фигуре, и переполнение печатается списком.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Emu

SC = 120 / 914400          # пикселей на EMU при 120 px/дюйм
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
OUT = Path(__file__).parent / "preview"; OUT.mkdir(exist_ok=True)

def font(pt, bold=False, mono=False):
    return ImageFont.truetype(FM if mono else (FB if bold else FR), max(7, int(pt * 120 / 72)))

def wrap(d, text, fo, w, mono=False):
    out = []
    for para in text.split("\n"):
        if mono:
            out.append(para); continue
        line = ""
        for word in para.split():
            probe = (line + " " + word).strip()
            if d.textlength(probe, font=fo) > w and line:
                out.append(line); line = word
            else:
                line = probe
        out.append(line)
    return out

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def grad_stops(sh):
    """Остановки градиентной заливки, если она есть.

    Без этого предпросмотр рисовал дивайдеры БЕЛЫМИ: градиент задаётся узлом
    `gradFill`, а не `solidFill`, проверка `fill.type == 1` его не видела — и
    белый текст на «белом» фоне пропадал вовсе. Смотреть на такую картинку и
    делать вывод о вёрстке нельзя, поэтому градиент разбирается явно."""
    try: sppr = sh._element.spPr
    except Exception: return None
    g = sppr.find(A + "gradFill")
    if g is None: return None
    out = []
    for gs in g.iter(A + "gs"):
        clr = gs.find(A + "srgbClr")
        if clr is None: continue
        v = clr.get("val")
        out.append((int(gs.get("pos", 0)) / 100000.0,
                    (int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16))))
    return sorted(out) or None


def paint_gradient(im, x, y, w, h, stops):
    """Линейный градиент по диагонали — тот же угол 45°, что задаёт вёрстка."""
    if w <= 0 or h <= 0: return
    box = Image.new("RGB", (max(w, 1), max(h, 1)))
    px = box.load()
    for j in range(box.size[1]):
        for i in range(0, box.size[0], 4):
            t = (i / max(box.size[0] - 1, 1) + j / max(box.size[1] - 1, 1)) / 2
            lo = stops[0]; hi = stops[-1]
            for k in range(len(stops) - 1):
                if stops[k][0] <= t <= stops[k + 1][0]:
                    lo, hi = stops[k], stops[k + 1]; break
            span = max(hi[0] - lo[0], 1e-6)
            f = min(max((t - lo[0]) / span, 0.0), 1.0)
            col = tuple(int(lo[1][c] + (hi[1][c] - lo[1][c]) * f) for c in range(3))
            for d in range(4):
                if i + d < box.size[0]: px[i + d, j] = col
    im.paste(box, (x, y))


def run_info(p):
    r = p.runs[0] if p.runs else None
    sz = (p.font.size or (r.font.size if r else None))
    nm = (p.font.name or (r.font.name if r else None)) or "Arial"
    bo = bool(p.font.bold or (r.font.bold if r else False))
    col = None
    for src in (p.font, r.font if r else None):
        try:
            if src and src.color and src.color.rgb: col = tuple(src.color.rgb); break
        except Exception: pass
    return (sz.pt if sz else 18), nm, bo, col or (20, 27, 46)

def draw_tf(d, tf, x, y, w, h, report, tag):
    pad = 4
    cy, need = y + pad, 0
    for p in tf.paragraphs:
        t = "".join(r.text for r in p.runs) or p.text
        pt, nm, bo, col = run_info(p)
        fo = font(pt, bo, nm.lower().startswith("consol") or nm.lower().startswith("dejavu sans mono"))
        lh = int(pt * 120 / 72 * 1.22)
        mono = nm.lower().startswith("consol")
        for ln in (wrap(d, t, fo, w - 2 * pad, mono) if t else [""]):
            if t: d.text((x + pad, cy), ln, font=fo, fill=col)
            cy += lh; need += lh
    if need > h - 2 * pad + 2:
        report.append(f"{tag}: текст выше рамки на {(need - h) / 120:.2f}\"")

def render(pptx, ids):
    prs = Presentation(pptx)
    import yaml
    deck = yaml.safe_load((Path(__file__).parent.parent / "deck.yaml").read_text())
    order = [s["id"] for s in deck["slides"]]
    problems = []
    for sid in ids:
        sl = prs.slides[order.index(sid)]
        W, H = int(prs.slide_width * SC), int(prs.slide_height * SC)
        bgc = (255, 255, 255)
        try: bgc = tuple(sl.background.fill.fore_color.rgb)
        except Exception: pass
        im = Image.new("RGB", (W, H), bgc); d = ImageDraw.Draw(im)
        for sh in sl.shapes:
            x, y, w, h = [int(v * SC) for v in (sh.left, sh.top, sh.width, sh.height)]
            if sh.shape_type is not None and sh.has_chart if False else False: pass
            if sh.shape_type == 13 or sh.__class__.__name__ == "Picture":
                try:
                    im.paste(Image.open(__import__("io").BytesIO(sh.image.blob)).convert("RGB").resize((w, h)), (x, y))
                except Exception as e: problems.append(f"{sid} картинка: {e}")
                continue
            if getattr(sh, "has_table", False):
                tb = sh.table
                cw = [int(c.width * SC) for c in tb.columns]
                ry = y
                for i, row in enumerate(tb.rows):
                    rh = int(row.height * SC); cx = x
                    for j, cell in enumerate(row.cells):
                        fc = (255, 255, 255)
                        try: fc = tuple(cell.fill.fore_color.rgb)
                        except Exception: pass
                        d.rectangle([cx, ry, cx + cw[j], ry + rh], fill=fc, outline=(200, 210, 220))
                        draw_tf(d, cell.text_frame, cx, ry, cw[j], rh, problems, f"{sid} ячейка [{i},{j}]")
                        cx += cw[j]
                    ry += rh
                if ry > H: problems.append(f"{sid}: таблица уходит за нижний край на {(ry - H) / 120:.2f}\"")
                continue
            if sh.has_text_frame and not sh.text_frame.text.strip():
                pass
            if sh.shape_type == 1 or getattr(sh, "fill", None) is not None and not sh.has_text_frame:
                pass
            grad = grad_stops(sh)
            if grad:
                paint_gradient(im, x, y, w, h, grad)
                continue
            try:
                fill = tuple(sh.fill.fore_color.rgb) if sh.fill.type == 1 else None
            except Exception: fill = None
            try:
                line = tuple(sh.line.color.rgb) if sh.line.fill.type == 1 else None
            except Exception: line = None
            if fill or line:
                d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=fill, outline=line, width=2)
            if sh.has_text_frame and sh.text_frame.text.strip():
                draw_tf(d, sh.text_frame, x, y, w, h, problems, f"{sid} «{sh.text_frame.text[:28]}…»")
            if x < 0 or y < 0 or x + w > W + 2 or y + h > H + 2:
                problems.append(f"{sid}: фигура вне канвы ({x},{y},{w},{h})")
        im.save(OUT / f"{sid}.png")
    return problems

if __name__ == "__main__":
    ids = sys.argv[1:] or ["s01","s02","s03","s04","s05","s06","s07","s54","s55","s56"]
    for p in render(Path(__file__).parent / "sem-05.pptx", ids):
        print("•", p)
    print("предпросмотр:", ", ".join(ids))
