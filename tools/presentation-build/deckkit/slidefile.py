# -*- coding: utf-8 -*-
"""Читатель файла кадра: `slides/sNN-*.md` → разобранный кадр.

ИСТОЧНИК ИСТИНЫ ВИДИМОГО ТЕКСТА — файл кадра, и только он. В сборщике
литералов видимого текста быть не должно: правка файла обязана доходить до
деки без правки кода. Служебные поля фронтматтера (`assertion`, `timing_min`,
`in_bucket`, `method_steps`, `form`, `media_needed`, `media_note`, `status`,
`learning_outcomes`) на экран не выводятся НИ ОДНОЙ СТРОКОЙ — их место в
отчёте сборки и в `deck.yaml`.

Формат файла один на оба сборщика:

    ---
    id: s42
    type: case
    title: "Заголовок-утверждение"
    source: "Работа, автор — https://…"
    ---

    ## Видимый текст слайда
    …
    ## Заметки лектора
    …

ДВА РАЗБОРА ТЕЛА, и это не дубль. Сборщики раскладывают тело по-разному, и
разница не в стиле, а в единице:

* `body_blocks` (lec-07) — единица АБЗАЦ: тело режется по пустой строке,
  перечень склеивается в один блок буллитов. Виды: head · bullet · cap ·
  para. Нужен раскладке «одна надпись на всё тело, кегли масштабируются».
* `body_ordered` (lec-06) — единица СТРОКА, с сохранением порядка, и среди
  видов есть `table` и `quote`. Нужен раскладке «по надписи на блок, один
  кегль на тело», где таблица обязана встать там, где стояла в файле.

Обе остаются. Перевести первую на вторую нельзя, не потеряв таблицы;
вторую на первую — не потеряв масштабирование кеглей внутри абзаца.
"""
import re
from pathlib import Path

import yaml

from . import report
from .markup import ITALIC_LINE, PLACEHOLDER, URL, short_url

# Заголовок раздела отделяется от содержимого ОДНИМ переводом строки, а не
# `\s*\n`. Разница видна только на ПУСТОМ разделе — и там она переворачивала
# смысл файла: `\s*` съедал пустую строку вместе с переводом, после чего
# впереди не оставалось `\n##` для просмотра вперёд, и в видимый текст
# уезжали ЗАМЕТКИ ЦЕЛИКОМ. Поймано на первом же кадре, у которого видимый
# раздел пуст по замыслу (кадр-удар `s01_1`, #293): сборка насчитала ему 614
# слов видимого слоя вместо тридцати, то есть пересказала залу заметки
# лектора. На непустом разделе поведение не меняется ни на знак: ведущий
# перевод строки снимает `.strip()` ниже.
_SEC_VIS = r"##[ \t]*Видимый текст слайда[ \t]*\r?\n(.*?)(?=\n##\s|\Z)"
_SEC_NOTES = r"##[ \t]*Заметки лектора[ \t]*\r?\n(.*?)(?=\n##\s|\Z)"
_EMPTY_CELL = {"", "null", "none", "nil", "~"}


class Slide:
    """Разобранный файл кадра. Поля раскладки (`tick_y`, `media_w`) дека
    дописывает сама — здесь их нет, потому что это не свойство файла."""

    __slots__ = ("sid", "path", "meta", "body", "notes", "title",
                 "tick_y", "media_w", "_cache")

    def __init__(self):
        self.tick_y = None
        self.media_w = None
        self._cache = {}


_ORDER = re.compile(r"^s(\d+)(?:_(\d+))?([a-z]*)")


def order_key(name):
    """`s49` → `s49a` → `s49b` → `s50`: буквенный хвост идёт за номером.

    ВСТАВКА ПЕРЕД БУКВЕННЫМ ХВОСТОМ: `s01` → `s01_1` → `s01_2` → `s01a`.
    Заведена под кадр, которому место СРАЗУ за кадром без хвоста, и
    заведена потому, что буквенной схемой это место недостижимо: между
    пустым хвостом и `a` строк нет — `''` наименьшая строка, `'a'`
    наименьшая непустая, и ничего третьего между ними не лежит. Прежде
    такое место добывали переименованием соседа (так `s01aa`…`s01af`
    встали между `s01a` и `s01b`), но сосед здесь — сам кадр `s01`, и
    переименование обложки увело бы с первой страницы и обязательный hero
    §5.9, и единственную проверку, которая его там мерит.

    Порядок существующих имён этим НЕ двинут: у имени без `_` подномер
    равен нулю, то есть каждое старое имя сравнивается ровно так, как
    сравнивалось (`(номер, хвост)` → `(номер, хвост, 0)`). Подномер стоит
    в ключе ТРЕТЬИМ, после хвоста: иначе `s01_1` ушёл бы за `s01a`, то
    есть ровно не туда, зачем он и нужен.
    """
    m = _ORDER.match(name)
    if not m:
        return (9999, name, 0)
    return (int(m.group(1)), m.group(3), int(m.group(2) or 0))


def slide_files(slides_dir, only=None):
    """Файлы кадров по порядку. Два файла на один номер — не редкость, когда
    кадр переписывают: старый остаётся рядом с новым, и читатель молча берёт
    первый по алфавиту. Молчать об этом нельзя — выходит `[файлы]` с обоими
    именами и тем, которое пошло в деку."""
    files = sorted(Path(slides_dir).glob("s*.md"), key=lambda f: order_key(f.name))
    by_sid = {}
    for f in files:
        by_sid.setdefault(f.name.split("-")[0], []).append(f)
    out = []
    for sid in sorted(by_sid, key=order_key):
        group = by_sid[sid]
        if len(group) > 1:
            report.warn(
                f"[файлы] {sid}: файлов {len(group)} на один номер — "
                + ", ".join(f.name for f in group)
                + f"; в деку пошёл {group[0].name}")
        out.append(group[0])
    if only:
        want = {x.strip() for x in str(only).split(",") if x.strip()}
        out = [f for f in out if f.name.split("-")[0] in want]
    return out


def read_slide(path, *, check_body_urls=True):
    """Файл кадра → `Slide`. Возвращает None, если файл не читается как кадр.

    `[ссылка]` — URL в ВИДИМОМ теле. Место ссылки — подвал, поле `source`:
    адрес на экране не нажимается, а место занимает, и зал его не наберёт."""
    path = Path(path)
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.S)
    if not m:
        report.warn(f"[файл] {path.name}: нет фронтматтера")
        return None
    sl = Slide()
    sl.path = path
    try:
        sl.meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        report.warn(f"[файл] {path.name}: фронтматтер не читается — {e}")
        return None
    sl.sid = str(sl.meta.get("id") or path.stem.split("-")[0])
    sl.title = str(sl.meta.get("title") or "").strip()
    rest = m.group(2)
    vis = re.search(_SEC_VIS, rest, re.S)
    nts = re.search(_SEC_NOTES, rest, re.S)
    if vis is None:
        report.warn(f"[файл] {path.name}: нет раздела «Видимый текст слайда»")
    sl.body = (vis.group(1) if vis else "").strip()
    sl.notes = (nts.group(1) if nts else "").strip()
    if not sl.notes:
        report.warn(f"[заметки] {sl.sid}: раздела «Заметки лектора» нет")
    report.PLACEHOLDERS[sl.sid] = len(PLACEHOLDER.findall(sl.body))
    if check_body_urls:
        for u in URL.finditer(sl.body):
            report.warn(
                f"[ссылка] {sl.sid}: адрес «{short_url(u.group(0), 34)}» "
                "стоит в теле слайда — место ссылки в подвале, поле `source`")
    return sl


# ── разбор тела, вариант «абзац» (lec-07) ───────────────────────────


def body_blocks(sl):
    """Тело → [(вид, текст)]. Вид: head · bullet · cap · para.

    Единица — абзац: режется по пустой строке. Перечень отдаётся отдельными
    буллитами, но они идут подряд и склеиваются раскладкой в один блок."""
    key = "body_blocks"
    if key in sl._cache:
        return sl._cache[key]
    out = []
    for blk in re.split(r"\n\s*\n", sl.body):
        blk = blk.strip()
        if not blk:
            continue
        if blk.startswith("#"):
            out.append(("head", blk.lstrip("# ").strip()))
        elif (all(l.strip().startswith(("- ", "* ", "• ")) or not l.strip()
                  for l in blk.split("\n"))
              and blk.lstrip().startswith(("- ", "* ", "• "))):
            for l in blk.split("\n"):
                if l.strip():
                    out.append(("bullet", "• " + l.strip()[2:].strip()))
        elif ITALIC_LINE.fullmatch(blk) and "\n" not in blk:
            out.append(("cap", ITALIC_LINE.fullmatch(blk).group(1)))
        else:
            out.append(("para", blk.replace("\n", " ")))
    sl._cache[key] = out
    return out


# ── разбор тела, вариант «строка с порядком» (lec-06) ───────────────


def _is_sep(cells):
    """Разделительная строка таблицы: только дефисы и двоеточия, и дефис
    ОБЯЗАН быть.

    Без требования дефиса строка пустой матрицы («| |  |  |») принималась за
    разделитель и пропадала целиком — а матрица, нарисованная в пустую как
    образец для заполнения, ровно из таких строк и состоит."""
    return "-" in "".join(cells) and all(set(c) <= set("-: ") for c in cells)


def _cell(text):
    """Клетка матрицы. `null`, `~` и пустое — клетка ПОД ЗАПОЛНЕНИЕ: рисуется
    рамкой без текста. Длинное тире клеткой под заполнение НЕ считается: им
    в деке сказано «тут ничего нет», а это другое утверждение."""
    t = text.strip()
    return "" if t.lower() in _EMPTY_CELL else t


def body_ordered(sl):
    """Тело → (заголовок раздела, блоки, подписи-кандидаты).

    Единица — строка; порядок сохраняется. Виды: table · italic · quote ·
    bullet · para. Блоки отдаются СПИСКАМИ (а не парами), потому что
    `tables.blank_cells` правит клетки таблицы на месте.

    Порядок нужен по-настоящему: на кадре `s78` Лекции 6 таблица стоит
    ПЕРВЫМ блоком, а прежний читатель раскладывал тело по трём отдельным
    спискам и порядок терял."""
    key = "body_ordered"
    if key in sl._cache:
        return sl._cache[key]
    heading, blocks = None, []
    for ln in (l.strip() for l in sl.body.split("\n")):
        if not ln:
            continue
        if ln.startswith("# "):
            heading = ln[2:].strip()
        elif ln.startswith("|"):
            raw = [c.strip() for c in ln.strip("|").split("|")]
            if _is_sep(raw):
                continue
            cells = [_cell(c) for c in raw]
            if blocks and blocks[-1][0] == "table":
                blocks[-1][1].append(cells)
            else:
                blocks.append(["table", [cells]])
        elif ITALIC_LINE.match(ln):
            blocks.append(["italic", ln])
        elif ln.startswith(">"):
            t = ln.lstrip("> ").rstrip()
            if blocks and blocks[-1][0] == "quote":
                blocks[-1][1] += "\n" + t
            else:
                blocks.append(["quote", t])
        elif ln.startswith("- ") or ln.startswith("* "):
            blocks.append(["bullet", ln[2:].strip()])
        else:
            blocks.append(["para", ln])
    out = (heading, blocks)
    sl._cache[key] = out
    return out


def blk_kind(text):
    """Вид блока по его первому знаку — для кода, который держит блоки
    плоскими строками, а не парами (`probe_v4`)."""
    if text.startswith(">"):
        return "quote"
    if text.startswith("- ") or text.startswith("* "):
        return "bullet"
    return "para"


def blk_width(kind, w):
    """Цитата и буллит отступают от левого края: отступ съедает ширину, и
    мера обязана считать по суженной, иначе блок с отступом недомеривается
    ровно на этот отступ."""
    return w - 0.42 if kind in ("quote", "bullet") else w
