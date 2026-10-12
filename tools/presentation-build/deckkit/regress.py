# -*- coding: utf-8 -*-
"""РЕГРЕССИЯ: сравнить собранный PPTX с доставленным — по СОДЕРЖИМОМУ.

Зачем не по байтам. `python-pptx` пишет в пакет метки времени (`docProps/
core.xml`: `dcterms:created` / `dcterms:modified`), и у двух сборок одного и
того же файла они разные. Плюс порядок записей в zip и поля сжатия. Поэтому
побайтовое сравнение даёт «отличается» на идентичной деке всегда. Это замерено
и записано: `notes/mcp-limitations.md` [#211-5] — три подряд пересборки
неизменённой деки Семинара 5 дали три разных sha256. Байтовая проверка здесь
не строгая, она просто неработающая; и та запись называет своей бедой, что «у
ревьюера НЕТ хеша, которым можно показать, что русский рендер не тронут» —
отпечаток ниже и есть ответ на неё.

ЧТО ЗНАЧИТ «ТО ЖЕ САМОЕ». Отпечаток кадра — это:

  * число кадров и их порядок;
  * по каждой фигуре: вид (автофигура / надпись / картинка), геометрия в
    EMU (x, y, ширина, высота) — то есть РОВНО то число, которое уехало в
    файл, без округления до дюймов, — тип автофигуры, заливка, цвет и
    толщина обводки, наличие `<p:style>`;
  * по каждой надписи: привязка, перенос, и по каждому прогону — текст,
    кегль, полужирный, курсив, подчёркивание, цвет, адрес гиперссылки;
  * отбивка абзаца и межстрочный — те две величины, вокруг которых и
    крутилась вся правка меры;
  * заметки лектора целиком, прогонами, вместе с их ссылками;
  * внешние отношения кадра (адреса гиперссылок в `.rels`).

ЧЕГО В ОТПЕЧАТКЕ НЕТ, НАРОЧНО: метки времени, порядок записей в zip,
название файла картинки внутри пакета (`image7.png` против `image7_1.png` —
нумерация зависит от порядка вставки, а не от того, что на экране). Вместо
имени берётся РАЗМЕР и контрольная сумма самого потока картинки: подмена
снимка это ловит, перенумерация — нет.

Запуск:
    python3 -m deckkit.regress эталон.pptx проба.pptx
    python3 -m deckkit.regress --dump эталон.pptx > эталон.json
"""
import argparse
import hashlib
import json
import re
import sys
import zipfile
from collections import OrderedDict

from lxml import etree

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
PIC_R = "{http://schemas.openxmlformats.org/drawingml/2006/main}blip"

_SLIDE = re.compile(r"ppt/slides/slide(\d+)\.xml$")
_NOTES = re.compile(r"ppt/notesSlides/notesSlide(\d+)\.xml$")


def _t(el, path):
    f = el.find(path)
    return f


def _xfrm(spPr):
    x = spPr.find(A + "xfrm") if spPr is not None else None
    if x is None:
        return None
    off, ext = x.find(A + "off"), x.find(A + "ext")
    return {
        "x": int(off.get("x")) if off is not None else None,
        "y": int(off.get("y")) if off is not None else None,
        "cx": int(ext.get("cx")) if ext is not None else None,
        "cy": int(ext.get("cy")) if ext is not None else None,
        "rot": x.get("rot"),
    }


def _color(el):
    """Цвет из любого носителя: srgbClr, schemeClr, отсутствие."""
    if el is None:
        return None
    s = el.find(A + "srgbClr")
    if s is not None:
        return s.get("val")
    sc = el.find(A + "schemeClr")
    if sc is not None:
        return "scheme:" + (sc.get("val") or "")
    if el.find(A + "noFill") is not None:
        return "none"
    return "?"


def _fill(spPr):
    if spPr is None:
        return None
    if spPr.find(A + "noFill") is not None:
        return "none"
    sf = spPr.find(A + "solidFill")
    if sf is not None:
        return _color(sf)
    if spPr.find(A + "gradFill") is not None:
        return "grad"
    if spPr.find(A + "blipFill") is not None:
        return "blip"
    return None


def _line(spPr):
    if spPr is None:
        return None
    ln = spPr.find(A + "ln")
    if ln is None:
        return None
    return {"w": ln.get("w"), "fill": _fill(ln) or _color(
        ln.find(A + "solidFill"))}


def _prst(spPr):
    if spPr is None:
        return None
    g = spPr.find(A + "prstGeom")
    if g is None:
        return "custom" if spPr.find(A + "custGeom") is not None else None
    adj = [(a.get("name"), a.get("fmla"))
           for a in g.iter(A + "gd")]
    return {"prst": g.get("prst"), "adj": adj}


def _runs(txBody):
    """Абзацы надписи прогонами. Всё, что влияет на видимое, и ничего, что
    не влияет."""
    out = []
    if txBody is None:
        return out
    for p in txBody.findall(A + "p"):
        pPr = p.find(A + "pPr")
        para = {"align": pPr.get("algn") if pPr is not None else None,
                "space_before": None, "ls": None, "runs": []}
        if pPr is not None:
            sb = pPr.find(A + "spcBef")
            if sb is not None:
                pts = sb.find(A + "spcPts")
                pct = sb.find(A + "spcPct")
                para["space_before"] = (pts.get("val") if pts is not None
                                        else (pct.get("val")
                                              if pct is not None else None))
            lnsp = pPr.find(A + "lnSpc")
            if lnsp is not None:
                pct = lnsp.find(A + "spcPct")
                pts = lnsp.find(A + "spcPts")
                para["ls"] = (pct.get("val") if pct is not None
                              else (pts.get("val") if pts is not None
                                    else None))
        for r in p.findall(A + "r"):
            rPr = r.find(A + "rPr")
            t = r.find(A + "t")
            hl = rPr.find(A + "hlinkClick") if rPr is not None else None
            latin = rPr.find(A + "latin") if rPr is not None else None
            para["runs"].append({
                "text": t.text if t is not None else "",
                "sz": rPr.get("sz") if rPr is not None else None,
                "b": rPr.get("b") if rPr is not None else None,
                "i": rPr.get("i") if rPr is not None else None,
                "u": rPr.get("u") if rPr is not None else None,
                "color": _color(rPr.find(A + "solidFill"))
                if rPr is not None else None,
                "font": latin.get("typeface") if latin is not None else None,
                "link": hl.get(R + "id") if hl is not None else None,
            })
        out.append(para)
    return out


def _bodyPr(txBody):
    if txBody is None:
        return None
    b = txBody.find(A + "bodyPr")
    if b is None:
        return None
    return {k: b.get(k) for k in ("anchor", "wrap", "lIns", "rIns", "tIns",
                                  "bIns")}


def _rels(z, name):
    """Внешние цели отношений кадра: адрес каждой гиперссылки и имя
    картинки. Ключ отношения (`rId3`) в отпечаток идёт, потому что прогон
    ссылается именно на него."""
    rel = name.replace("slides/", "slides/_rels/") + ".rels"
    if rel not in z.namelist():
        return {}
    root = etree.fromstring(z.read(rel))
    out = {}
    for e in root.iter():
        t = e.get("Type") or ""
        if t.endswith("/hyperlink"):
            out[e.get("Id")] = {"kind": "link", "target": e.get("Target")}
        elif t.endswith("/image"):
            out[e.get("Id")] = {"kind": "image"}
    return out


def _img_digest(z, zipname):
    data = z.read(zipname)
    return {"bytes": len(data),
            "md5": hashlib.md5(data).hexdigest()[:16]}


def _shape(z, name, rels, el):
    tag = etree.QName(el).localname
    if tag == "sp":
        spPr = el.find(P + "spPr")
        return {
            "kind": "autoshape",
            "geom": _xfrm(spPr), "prst": _prst(spPr),
            "fill": _fill(spPr), "line": _line(spPr),
            "p_style": el.find(P + "style") is not None,
            "effectLst_empty": _effect_state(spPr),
            "bodyPr": _bodyPr(el.find(P + "txBody")),
            "paras": _runs(el.find(P + "txBody")),
        }
    if tag == "pic":
        spPr = el.find(P + "spPr")
        blip = el.find(P + "blipFill")
        rid = None
        if blip is not None:
            b = blip.find(A + "blip")
            if b is not None:
                rid = b.get(R + "embed")
        img = None
        if rid and rid in rels:
            # Имя файла картинки в пакете нарочно НЕ берётся: его нумерация
            # зависит от порядка вставки. Берётся сам поток.
            zn = _image_zipname(z, name, rid)
            if zn:
                img = _img_digest(z, zn)
        src = blip.find(A + "blip") if blip is not None else None
        crop = None
        if blip is not None:
            sr = blip.find(A + "srcRect")
            if sr is not None:
                crop = {k: sr.get(k) for k in ("l", "r", "t", "b")}
        return {"kind": "picture", "geom": _xfrm(spPr), "image": img,
                "crop": crop,
                "p_style": el.find(P + "style") is not None}
    return {"kind": tag}


def _effect_state(spPr):
    if spPr is None:
        return None
    e = spPr.findall(A + "effectLst")
    if not e:
        return "absent"
    return "empty" if all(len(x) == 0 for x in e) else "set"


def _image_zipname(z, slide_name, rid):
    rel = slide_name.replace("slides/", "slides/_rels/") + ".rels"
    root = etree.fromstring(z.read(rel))
    for e in root.iter():
        if e.get("Id") == rid:
            tgt = (e.get("Target") or "").replace("../", "ppt/")
            return tgt if tgt in z.namelist() else None
    return None


def fingerprint(path):
    """PPTX → отпечаток содержимого (упорядоченный словарь, пригодный для
    JSON и для диффа)."""
    z = zipfile.ZipFile(path)
    slides = sorted((n for n in z.namelist() if _SLIDE.match(n)),
                    key=lambda n: int(_SLIDE.match(n).group(1)))
    pres = etree.fromstring(z.read("ppt/presentation.xml"))
    sz = pres.find(P + "sldSz")
    out = OrderedDict()
    out["slide_count"] = len(slides)
    out["slide_size"] = {"cx": sz.get("cx"), "cy": sz.get("cy")} if sz is not None else None
    out["slides"] = []
    notes_map = _notes_map(z)
    for n in slides:
        root = etree.fromstring(z.read(n))
        rels = _rels(z, n)
        tree = root.find(P + "cSld")
        spTree = tree.find(P + "spTree") if tree is not None else None
        shapes = []
        if spTree is not None:
            for el in spTree:
                t = etree.QName(el).localname
                if t in ("sp", "pic", "graphicFrame", "grpSp", "cxnSp"):
                    shapes.append(_shape(z, n, rels, el))
        out["slides"].append({
            "name": n,
            "bg": _bg(tree),
            "shapes": shapes,
            "links": {k: v["target"] for k, v in rels.items()
                      if v["kind"] == "link"},
            "notes": notes_map.get(n),
        })
    return out


def _bg(cSld):
    if cSld is None:
        return None
    bg = cSld.find(P + "bg")
    if bg is None:
        return None
    pr = bg.find(P + "bgPr")
    return _fill(pr) if pr is not None else "ref"


def _notes_map(z):
    """Кадр → его заметки прогонами. Связь кадр↔заметка идёт через
    отношения кадра, а не через номер: нумерация `notesSlideN` своя."""
    out = {}
    for n in z.namelist():
        if not _SLIDE.match(n):
            continue
        rel = n.replace("slides/", "slides/_rels/") + ".rels"
        if rel not in z.namelist():
            continue
        root = etree.fromstring(z.read(rel))
        for e in root.iter():
            if (e.get("Type") or "").endswith("/notesSlide"):
                tgt = (e.get("Target") or "").replace("../", "ppt/")
                if tgt not in z.namelist():
                    continue
                nroot = etree.fromstring(z.read(tgt))
                paras = []
                for sp in nroot.iter(P + "sp"):
                    ph = sp.find(f"{P}nvSpPr/{P}nvPr/{P}ph")
                    if ph is not None and ph.get("type") == "body":
                        paras = _runs(sp.find(P + "txBody"))
                        break
                nrels = {}
                nrel = tgt.replace("notesSlides/", "notesSlides/_rels/") + ".rels"
                if nrel in z.namelist():
                    nr = etree.fromstring(z.read(nrel))
                    for x in nr.iter():
                        if (x.get("Type") or "").endswith("/hyperlink"):
                            nrels[x.get("Id")] = x.get("Target")
                out[n] = {"paras": paras, "links": nrels}
    return out


# ── сравнение ───────────────────────────────────────────────────────


def _walk(a, b, path, out, limit):
    if len(out) >= limit:
        return
    if type(a) is not type(b) and not (isinstance(a, (int, float))
                                       and isinstance(b, (int, float))):
        out.append((path, repr(a)[:120], repr(b)[:120]))
        return
    if isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append((f"{path}.{k}",
                            "—" if k not in a else repr(a[k])[:120],
                            "—" if k not in b else repr(b[k])[:120]))
                continue
            _walk(a[k], b[k], f"{path}.{k}", out, limit)
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append((f"{path}[]", f"длина {len(a)}", f"длина {len(b)}"))
        for i in range(min(len(a), len(b))):
            _walk(a[i], b[i], f"{path}[{i}]", out, limit)
    elif a != b:
        out.append((path, repr(a)[:120], repr(b)[:120]))


def compare(fa, fb, limit=40):
    """Два отпечатка → перечень расхождений: (где, в эталоне, в пробе).
    Пустой перечень значит «то же содержимое»."""
    out = []
    _walk(fa, fb, "", out, limit)
    return out


def check(ref, probe, *, limit=40, label=""):
    """Сравнить два файла и напечатать итог. Возвращает число расхождений
    (0 — совпало)."""
    d = compare(fingerprint(ref), fingerprint(probe), limit)
    head = f"{label}: " if label else ""
    if not d:
        fa = fingerprint(ref)
        shapes = sum(len(s["shapes"]) for s in fa["slides"])
        print(f"{head}СОВПАЛО — кадров {fa['slide_count']}, фигур {shapes}, "
              "расхождений содержимого 0")
        return 0
    print(f"{head}РАСХОЖДЕНИЙ {len(d)}"
          + (f" (показаны первые {limit})" if len(d) >= limit else ""))
    for where, x, y in d:
        print(f"  {where}\n      эталон: {x}\n      проба : {y}")
    return len(d)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--dump", action="store_true")
    ap.add_argument("--limit", type=int, default=40)
    ap.add_argument("--label", default="")
    a = ap.parse_args(argv)
    if a.dump:
        json.dump(fingerprint(a.files[0]), sys.stdout, ensure_ascii=False,
                  indent=1)
        return 0
    if len(a.files) != 2:
        ap.error("нужны два файла: эталон и проба")
    return 1 if check(a.files[0], a.files[1], limit=a.limit,
                      label=a.label) else 0


if __name__ == "__main__":
    sys.exit(main())
