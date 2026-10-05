"""Разбор исходного .md слайда на структурные части.

Изменение против прежней версии: разметка внутри строки (`**жирный**`,
`` `моноширинный` ``) БОЛЬШЕ НЕ ВЫРЕЗАЕТСЯ здесь. Прежний `strip_md()` убирал
`**` без замены, и целевой ответ, помеченный в исходнике жирным, выходил на
слайд обычной строкой среди четырёх таких же. Теперь разметка доезжает до
вёрстки, которая превращает её в жирный прогон (`deck_kit.inline_runs`) и
заодно узнаёт по ней целевую строку таблицы.
"""
import re


_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
_HEAD = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def _outline(md):
    r"""Заголовки документа — ТОЛЬКО настоящие, то есть вне блоков в ограждении.

    Прежде секции резались регуляркой `^##\s+…(?=^##\s+|\Z)` по всему тексту.
    Регулярка не знает про ограждение, и на слайде, который показывает файл
    инструкций ЦЕЛИКОМ, разбор обрывался на первом `## Safety / scope
    boundaries` ВНУТРИ листинга: из 20 строк на слайд доезжали 4 — то есть
    ровно то, ради чего слайд и существует, терялось.

    Обход, которым это чинили на стороне слайда (сдвинуть листинг на два
    пробела вправо, чтобы `##` перестал начинать строку), работает, но платит
    за это враньём: слайд обещает показать файл дословно, а показывает файл с
    добавленным отступом. Поэтому чинится здесь.

    Ограждение открывается и закрывается строкой из трёх и более «гравис» или
    «тильда», возможно с отступом (`  ```` ```markdown ```` `). Закрывающей
    считается строка с тем же знаком и не короче открывающей — иначе `~~~`
    внутри блока на грависах закрыл бы его.
    """
    out, fence = [], None
    for i, ln in enumerate(md.splitlines()):
        m = _FENCE.match(ln)
        if m:
            tok = m.group(1)
            if fence is None:
                fence = tok
            elif tok[0] == fence[0] and len(tok) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue
        h = _HEAD.match(ln)
        if h:
            out.append((i, len(h.group(1)), h.group(2)))
    return out


def sections(md):
    """(заголовок, Assertion, Visual, Speaker notes) — по настоящим заголовкам."""
    lines = md.splitlines()
    heads = _outline(md)
    title = next((t for _i, lvl, t in heads if lvl == 1), "")

    def sect(name):
        low = name.lower()
        for k, (i, lvl, t) in enumerate(heads):
            if lvl != 2 or t.lower() != low:
                continue
            end = len(lines)
            for j, lvl2, _t2 in heads[k + 1:]:
                if lvl2 <= 2:
                    end = j
                    break
            return "\n".join(lines[i + 1:end]).strip()
        return ""

    return title, sect("Assertion"), sect("Visual"), sect("Speaker notes")


def _clean(s):
    """Только ссылки: они не несут оформления, которое вёрстка могла бы показать."""
    return re.sub(r"\[(.+?)\]\(.+?\)", r"\1", s).strip()


def _split_row(s):
    """Разбить строку таблицы по `|`, учитывая экранирование `\\|` — тот же
    escape, что принят в обычных markdown-таблицах: обратная косая черта
    перед `|` делает его содержимым ячейки (например, `|`-пайп в shell-
    команде), а не разделителем столбцов. Наивный `.split("|")` этого не
    знает и режет такую ячейку на две — живой случай, найденный на n68:
    `` `ls .../*.md \\| wc -l` `` стало двумя ячейками вместо одной, с
    голой обратной косой чертой и парой лишних обратных кавычек на слайде."""
    SENTINEL = "\x00"
    return [p.replace(SENTINEL, "|") for p in s.replace("\\|", SENTINEL).split("|")]


def blocks(visual):
    """Последовательность блоков в порядке источника:
    ('table', (headers, rows)) | ('code', (язык, lines)) | ('quote', lines)
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
            # Язык ограждения — не украшение исходника, а ЗАЯВЛЕНИЕ автора о
            # том, что внутри. Вёрстке он нужен, чтобы отличить листинг файла
            # разметки (где обратные кавычки — разметка этого файла) от вывода
            # команды (где они — настоящие знаки, и трогать их нельзя).
            flush(); lang = ln.strip().lstrip("`~").strip().lower()
            i += 1; code = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i].rstrip()); i += 1
            i += 1
            if code:
                out.append(("code", (lang, code)))
            continue
        if ln.strip().startswith("|") and ln.strip().endswith("|"):
            flush(); rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [_clean(c) for c in _split_row(lines[i].strip().strip("|"))]
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
        if re.match(r"^\s*(?:[-*]|\d+\.)\s+", ln):
            # `\d+\.` — нумерованный список markdown, не только `-`/`*`.
            # Живой случай (n36/n48/n58, issue 225): «## Visual» писал сцену
            # нумерованным списком (`1. … 2. … 3. … 4. …`), разборщик знал
            # только дефис/звёздочку — нумерованные строки не попадали ни в
            # одну ветку и схлопывались через `flush()` в один жирный абзац
            # без переносов (та же форма, что и обычный текст). Починка —
            # распознаём оба маркера.
            #
            # Второй круг той же починки (сведение круга владельца, issue 225):
            # распознать — ещё не нарисовать. Оба вида шли в `numbered_list`
            # без признака нумерации, то есть шаги сцены печатались такими же
            # кружками, как перечисление, и порядок шагов с экрана не читался.
            # Теперь вид списка едет вместе с пунктами: `(items, numbered)`.
            flush(); items = []
            numbered = bool(re.match(r"^\s*\d+\.\s+", lines[i]))
            while i < len(lines) and re.match(r"^\s*(?:[-*]|\d+\.)\s+", lines[i]):
                items.append(_clean(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", lines[i]))); i += 1
            out.append(("bullets", (items, numbered))); continue
        buf.append(ln); i += 1
    flush()
    return out
