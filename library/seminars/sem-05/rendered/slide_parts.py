"""Разбор исходного .md слайда на структурные части.

Изменение против прежней версии: разметка внутри строки (`**жирный**`,
`` `моноширинный` ``) БОЛЬШЕ НЕ ВЫРЕЗАЕТСЯ здесь. Прежний `strip_md()` убирал
`**` без замены, и целевой ответ, помеченный в исходнике жирным, выходил на
слайд обычной строкой среди четырёх таких же. Теперь разметка доезжает до
вёрстки, которая превращает её в жирный прогон (`deck_kit.inline_runs`) и
заодно узнаёт по ней целевую строку таблицы.
"""
import re


def sections(md):
    def sect(name):
        m = re.search(rf"^##\s+{name}\s*$(.*?)(?=^##\s+|\Z)", md, re.M | re.S)
        return m.group(1).strip() if m else ""
    t = re.search(r"^#\s+(.+)$", md, re.M)
    return (t.group(1).strip() if t else ""), sect("Assertion"), sect("Visual"), sect("Speaker notes")


def _clean(s):
    """Только ссылки: они не несут оформления, которое вёрстка могла бы показать."""
    return re.sub(r"\[(.+?)\]\(.+?\)", r"\1", s).strip()


def blocks(visual):
    """Последовательность блоков в порядке источника:
    ('table', (headers, rows)) | ('code', lines) | ('quote', lines)
    | ('cards', items) | ('bullets', items) | ('para', text).
    """
    out, buf, i = [], [], 0
    lines = visual.splitlines()

    def flush():
        nonlocal buf
        t = " ".join(x.strip() for x in buf if x.strip())
        if t:
            out.append(("para", _clean(t)))
        buf = []

    while i < len(lines):
        ln = lines[i]
        if ln.strip().startswith("```"):
            flush(); i += 1; code = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i].rstrip()); i += 1
            i += 1
            if code:
                out.append(("code", code))
            continue
        if ln.strip().startswith("|") and ln.strip().endswith("|"):
            flush(); rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [_clean(c) for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c.strip()) for c in cells if c.strip()):
                    rows.append(cells)
                i += 1
            if rows:
                # первая строка — шапка, если под ней в исходнике был разделитель
                out.append(("table", (rows[0], rows[1:]) if len(rows) > 1 else ([], rows)))
            continue
        if ln.strip().startswith(">"):
            flush(); q = []
            while i < len(lines) and (lines[i].strip().startswith(">") or not lines[i].strip()):
                if lines[i].strip().startswith(">"):
                    q.append(_clean(re.sub(r"^\s*>\s?", "", lines[i])))
                elif q:
                    break
                i += 1
            if q:
                out.append(("quote", q))
            continue
        if "·" in ln and ln.count("`") >= 4:
            flush()
            items = [_clean(x) for x in ln.split("·") if x.strip()]
            if len(items) >= 3:
                out.append(("cards", items)); i += 1; continue
        if re.match(r"^\s*[-*]\s+", ln):
            flush(); items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(_clean(re.sub(r"^\s*[-*]\s+", "", lines[i]))); i += 1
            out.append(("bullets", items)); continue
        buf.append(ln); i += 1
    flush()
    return out
