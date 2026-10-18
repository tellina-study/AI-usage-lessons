# -*- coding: utf-8 -*-
"""Разметка абзаца и ссылки: `**полужирный**`, `*курсив*`, `` `код` ``, URL.

Разметка превращается в ПРОГОНЫ, а не остаётся звёздочками на экране. Два
сборщика делали это по-разному, и обе версии нужны по-настоящему:

* `inline_runs` (lec-07) разбирает разметку В ЛЮБОМ МЕСТЕ строки, вложенные
  совпадения отбрасывает и кегль у куска оставляет тот же, что у абзаца;
* `runs_md` (lec-06) разбирает ту же разметку, но полужирному даёт ДРУГОЙ
  ЦВЕТ и кегль на полпункта крупнее — то есть читает `**` как «акцент», а
  не как «полужирный».

Это не две реализации одного, а два разных решения о том, что значит `**` в
файле кадра, и ни одно не является ошибкой другого. Обе остаются; дека
выбирает своё в `geometry`/настройке.

Ссылки. URL в поле `source` и в заметках лектора становится НАСТОЯЩЕЙ
гиперссылкой PPTX (`<a:hlinkClick r:id="…">` на внешнее отношение), а не
подчёркнутым синим текстом. Правило владельца, названное им забытым (разбор
2026-10-08). Якорем становится ОСМЫСЛЕННАЯ часть, а не голый адрес:
семьдесят знаков адреса подвал не держит.
"""
import re

from . import report
from .theme import DEEP, GOLD, LIGHT, MID

_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITAL = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)")
ITALIC_LINE = re.compile(r"^\*(?!\*)(.+?)\*$")
PLACEHOLDER = re.compile(r"\{\{([^}]*)\}\}")


# ── разбор разметки ─────────────────────────────────────────────────


def md_chunks(text):
    """'a **b** *c* `d`' → [(текст, полужирный, курсив), …].

    Из lec-06. Разбор идёт ОДНИМ `re.split`, то есть разметка узнаётся
    только когда она обрамляет кусок целиком; `inline_runs` ниже решает ту
    же задачу позиционно и находит `**` посреди слова."""
    out = []
    for part in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)", text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            out.append((part[2:-2], True, False))
        elif part.startswith("*") and part.endswith("*"):
            out.append((part[1:-1], False, True))
        elif part.startswith("`") and part.endswith("`"):
            out.append((part[1:-1], False, False))
        else:
            out.append((part, False, False))
    return out


def plain(text):
    """Снять разметку, оставив слова. Мера идёт по этой строке, а не по той,
    в которой есть звёздочки: звёздочки на экран не попадают, а в ширину
    строки попадали бы."""
    return "".join(t for t, _, _ in md_chunks(text))


def inline_runs(line, size, color=DEEP):
    """`**полужирный**` и `*курсив*` внутри строки — прогонами, не разметкой.

    Из lec-07. Вложенные совпадения не берутся: `**a *b* c**` даёт один
    полужирный кусок, а не три внахлёст."""
    out, pos = [], 0
    toks = sorted(
        [(m.start(), m.end(), "b", m.group(1)) for m in _BOLD.finditer(line)]
        + [(m.start(), m.end(), "i", m.group(1)) for m in _ITAL.finditer(line)])
    keep, last = [], -1
    for t in toks:
        if t[0] >= last:
            keep.append(t)
            last = t[1]
    for st, en, kind, inner in keep:
        if st > pos:
            out.append({"text": line[pos:st], "size": size, "color": color})
        out.append({"text": inner, "size": size, "color": color,
                    "bold": kind == "b", "italic": kind == "i"})
        pos = en
    if pos < len(line):
        out.append({"text": line[pos:], "size": size, "color": color})
    return out or [{"text": line, "size": size, "color": color}]


def runs_md(text, *, size=16, color=DEEP, accent=GOLD, accent_size=None,
            italic_color=None):
    """Абзац файла кадра → прогоны, где `**` читается АКЦЕНТОМ: свой цвет и
    кегль на полпункта крупнее. Из lec-06."""
    out = []
    for t, bold, italic in md_chunks(text):
        cfg = {"text": t, "size": size}
        if bold:
            cfg.update(size=accent_size or size, bold=True, color=accent)
        elif italic:
            cfg.update(italic=True, color=italic_color or LIGHT)
        else:
            cfg["color"] = color
        out.append(cfg)
    return out


def bold_head(text):
    """'**Шапка:** тело' → ('Шапка:', 'тело'). Полужирного нет → (None, текст)."""
    ch = md_chunks(text)
    if ch and ch[0][1]:
        return ch[0][0].strip(), "".join(t for t, _, _ in ch[1:]).strip()
    return None, text.strip()


# ── ссылки ──────────────────────────────────────────────────────────
URL = re.compile(r"(?:https?://|www\.)[^\s<>\"«»'()\[\]]+", re.I)
MDLINK = re.compile(r"\[([^\]\n]+)\]\((https?://[^)\s]+)\)")
_TAIL = ".,;:!?…»\"'"


def abs_url(u):
    u = u.rstrip(_TAIL)
    return u if u.lower().startswith(("http://", "https://")) else "https://" + u


def short_url(u, lim=46):
    t = re.sub(r"^https?://", "", u).rstrip("/")
    t = re.sub(r"^www\.", "", t)
    return t if len(t) <= lim else t[:lim - 1] + "…"


def _bare(text):
    out, pos = [], 0
    for m in URL.finditer(text):
        raw = m.group(0).rstrip(_TAIL)
        if m.start() > pos:
            out.append((text[pos:m.start()], None))
        out.append((raw, abs_url(raw)))
        pos = m.start() + len(raw)
    if pos < len(text):
        out.append((text[pos:], None))
    return out


def link_parts(text):
    """Строка → [(видимое, адрес или None), …]. Это разбор ЗАМЕТОК: адрес
    остаётся виден, потому что заметки читают как текст (и они идут на сайт
    курса, где адрес нужен глазами)."""
    out, pos = [], 0
    for m in MDLINK.finditer(text):
        if m.start() > pos:
            out += _bare(text[pos:m.start()])
        out.append((m.group(1), abs_url(m.group(2))))
        pos = m.end()
    if pos < len(text):
        out += _bare(text[pos:])
    return [p for p in out if p[0]]


def _seg_parts(seg, lim=46, lim2=30):
    """Одна работа из поля `source` → прогоны подвала. Голый адрес из
    ВИДИМОЙ строки убирается: ссылкой становится название работы перед ним.
    Названия нет — якорем идёт сокращённый адрес."""
    if MDLINK.search(seg):
        return link_parts(seg)
    urls = [abs_url(m.group(0)) for m in URL.finditer(seg)]
    if not urls:
        return [(seg, None)]
    vis = re.sub(r"\s{2,}", " ", URL.sub("", seg))
    vis = re.sub(r"\s*[—–-]\s*$", "", vis).strip(" ,;:·—–")
    if not vis:
        return [(short_url(urls[0], lim), urls[0])]
    out = [(vis, urls[0])]
    for u in urls[1:]:
        out += [(" · ", None), (short_url(u, lim2), u)]
    return out


def source_parts(src, lim=46, lim2=30):
    """Поле `source` целиком → [(видимое, адрес или None), …]."""
    out = []
    for i, seg in enumerate(str(src).split(" · ")):
        if i:
            out.append((" · ", None))
        out += _seg_parts(seg, lim, lim2)
    return [p for p in out if p[0]]


def notes_with_links(slide, text, color=MID):
    """Заметки лектора с ЖИВЫМИ ссылками.

    `.text = …` кладёт заметки одной строкой, а у строки нет прогонов, на
    которые можно поставить ссылку. Эта версия у двух сборщиков совпадала
    посимвольно — редкий случай, когда объединять было нечего."""
    tf = slide.notes_slide.notes_text_frame
    tf.text = ""
    n = 0
    for i, ln in enumerate((text or "").split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        for seg, url in (link_parts(ln) or [(ln, None)]):
            r = p.add_run()
            r.text = seg
            if url:
                r.hyperlink.address = url
                r.font.underline = True
                r.font.color.rgb = color
                n += 1
    report.LINKS["заметки"] += n
    return n
