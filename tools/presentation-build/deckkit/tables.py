# -*- coding: utf-8 -*-
"""ТАБЛИЦЫ И МАТРИЦЫ — целиком из Лекции 6; в Лекции 7 этого не было вовсе.

Таблица в деке — не украшение: это единственный примитив, который держит
сетку «строка × столбец» (матрицу разбора, сравнение режимов, перечень с
двумя признаками). Лекция 7 обходилась без него и поэтому ни разу не
встретила его главной трудности.

ГЛАВНАЯ ТРУДНОСТЬ — ШИРИНА СТОЛБЦА. Делить ширину пропорционально объёму
текста нельзя: столбцу с коротким словарём достаётся меньше, чем занимает
самое длинное слово в нём, а переноса по слогам в деке нет — LibreOffice
рвёт слово там, где кончилась ширина. На кадре `s20a` левый столбец давал
«классифика/ция» и «распознава/ние». Это читается как брак печати, а не как
плотная вёрстка.

Поэтому у каждого столбца есть НИЖНИЙ ПРЕДЕЛ — самое длинное слово в нём при
выбранном кегле плюс поля ячейки. Порядок уступок, по возрастанию цены:

    просторные поля → кегль таблицы мельче → тесные поля → `[столбец]`

Поля — ДВЕ разные величины, и это не придирка. `TBL_PAD` (0,44") —
просторные, с которыми таблица меряется и обычно живёт: слово не упирается в
линейку. `TBL_TIGHT` (0,38") — последняя уступка: настоящий отступ текста в
ячейке (0,32 = 0,16 слева плюс 0,16 справа) плюс малый запас. Запас нужен:
слову, которому досталось РОВНО по его ширине, LibreOffice всё равно
находит причину уехать на вторую строку — так на `s72` ломалась шапка
(«изображени/е», «структурированны/е»), когда тесный предел был взят встык.

`[столбец]` — блокирующее. Разорванное посреди корня слово — это видимый
дефект печати, и прятать его в раскладке нельзя.
"""
from pptx.enum.text import MSO_ANCHOR

from . import metrics, prims, report
from .markup import plain
from .theme import DEEP, MID, OUTLINE, SURFACE, WHITE

TBL_PAD = 0.44                  # просторные поля, по ним меряются высоты
TBL_TIGHT = 0.38                # 0,32 отступа ячейки плюс запас
TBL_FLOOR = 8.0                 # ниже кегль таблицы не опускается
TBL_DROP = 2.0                  # насколько таблица вправе отстать от тела
TBL_CELL_PAD = 0.16             # настоящий отступ текста в ячейке
TBL_ROW_LS = 1.16
TBL_ROW_MIN = 0.40
TBL_ROW_EXTRA = 0.18

_TBLSZ = {}
_COL_WARNED = set()


def reset_caches():
    """Самопроверке нужно, чтобы предупреждение `[столбец]` сработало в
    КАЖДОЙ пробе. Оно выдаётся один раз на столбец (иначе каждый шаг подбора
    кегля писал бы своё), и без сброса вторая проба молчала бы — а молчание
    по причине «уже говорили» в самопроверке неотличимо от молчания по
    причине «проверка сломана»."""
    _TBLSZ.clear()
    _COL_WARNED.clear()


def rows_of(table):
    """Таблица с выровненным числом ячеек в строках."""
    ncol = max(len(r) for r in table)
    return [list(r) + [""] * (ncol - len(r)) for r in table]


def col_words(rows, j):
    """Все слова столбца. Текст переносится только по пробелам, поэтому
    отдельное слово — неделимый кусок."""
    out = []
    for r in rows:
        out += plain(r[j]).split()
    return out


def col_min(rows, size, pad=TBL_PAD):
    """Нижний предел ширины каждого столбца — самое длинное СЛОВО в нём.

    Меряется ПОЛУЖИРНЫМ: шапка таблицы полужирная, и ячейки с выделением
    тоже. Мера по светлому начертанию дала бы предел ниже настоящего, то
    есть разрешила бы ровно тот разрыв, от которого предел и защищает."""
    out = []
    for j in range(len(rows[0])):
        wmax = max([metrics.text_w(x, size, True) for x in col_words(rows, j)]
                   or [0.0])
        out.append(wmax / 72.0 + pad)
    return out


def col_want(rows, size):
    """Сколько столбец занял бы, умести он самую длинную свою ячейку в одну
    строку. Это ПОЖЕЛАНИЕ, которое уступает пределу."""
    return [max(metrics.text_w(plain(r[j]), size, True) for r in rows) / 72.0
            + TBL_PAD for j in range(len(rows[0]))]


def table_widths(rows, size, w):
    """Ширины столбцов: по содержимому, но ни один не уже своего предела.

    Остаток делится между незажатыми столбцами снова пропорционально, и так,
    пока деление не устоится — отсюда цикл, а не одна формула."""
    mins, want = col_min(rows, size), col_want(rows, size)
    if sum(mins) >= w:                      # просторные поля не влезли —
        mins = col_min(rows, size, TBL_TIGHT)   # последняя уступка: тесные
    if sum(mins) >= w:                      # не влезли и они —
        k = w / sum(mins)                   # ужимаем пропорционально,
        return [x * k for x in mins]        # зовущий выдаст `[столбец]`
    if sum(want) <= w:                      # места больше, чем нужно
        k = w / sum(want)
        return [x * k for x in want]
    fixed = [False] * len(mins)
    widths = list(want)
    for _ in range(len(mins) + 1):
        taken = sum(mins[j] for j in range(len(mins)) if fixed[j])
        tot = sum(want[j] for j in range(len(want)) if not fixed[j]) or 1.0
        widths = [mins[j] if fixed[j] else (w - taken) * want[j] / tot
                  for j in range(len(mins))]
        hit = [j for j in range(len(mins))
               if not fixed[j] and widths[j] < mins[j] - 1e-9]
        if not hit:
            break
        for j in hit:
            fixed[j] = True
    tot = sum(widths)
    if tot < w - 1e-9:                      # все столбцы на пределе, а
        k = w / tot                         # место осталось — раздаём его:
        widths = [x * k for x in widths]    # вверх двигать пределы можно
    return widths


def tbl_size(table, size, w):
    """Кегль таблицы: на полпункта мельче тела — а если при нём пределы
    столбцов не умещаются в ширину, ещё мельче, до `TBL_FLOOR`."""
    rows = rows_of(table)
    key = (tuple(tuple(r) for r in rows), round(size, 1), round(w, 3))
    if key not in _TBLSZ:
        f = max(TBL_FLOOR, size - 0.5)
        while f > TBL_FLOOR and sum(col_min(rows, f)) > w:
            f -= 0.5
        _TBLSZ[key] = f
    return _TBLSZ[key]


def tbl_ok(blocks, size, w):
    """Не отстала ли таблица от тела кадра больше, чем на `TBL_DROP`.

    Кегль таблицы подбирается отдельно от тела, и без этой проверки они
    расходятся до нелепого: таблица, ужатая до 8 пт ради целых слов,
    становится короче, свободная высота достаётся тексту, и тело вырастает
    до 17 пт. На `s72` это давало ровно такую пару — восьмипунктовая матрица
    рядом с семнадцатипунктовым рассказом."""
    return all(size - tbl_size(v, size, w) <= TBL_DROP + 1e-9
               for k, v in blocks if k == "table")


def table_geom(table, size, w):
    """Ширины столбцов и высоты строк при данном кегле."""
    rows = rows_of(table)
    widths = table_widths(rows, size, w)
    heights = []
    for r in rows:
        n = max(metrics.n_lines(plain(c), size,
                                max(0.12, widths[j] - TBL_PAD), True)
                for j, c in enumerate(r))
        heights.append(max(TBL_ROW_MIN,
                           n * size * TBL_ROW_LS * metrics.LH / 72.0
                           * metrics.SAFE + TBL_ROW_EXTRA))
    return widths, heights, rows


def check_cols(table, size, w, tag):
    """`[столбец]`: столбец всё равно уже своего самого длинного слова.

    Выдаётся один раз на столбец при ОТРИСОВКЕ, а не при подборе кегля:
    иначе каждый шаг подбора писал бы своё предупреждение."""
    rows = rows_of(table)
    widths = table_widths(rows, size, w)
    mins = col_min(rows, size, TBL_TIGHT)   # за этой границей слово рвётся
    hit = 0
    for j in range(len(mins)):
        if widths[j] + 1e-6 >= mins[j] or (tag, j) in _COL_WARNED:
            continue
        _COL_WARNED.add((tag, j))
        hit += 1
        longest = max(col_words(rows, j),
                      key=lambda x: metrics.text_w(x, size, True))
        report.warn(
            f"[столбец] {tag}: столбец {j + 1} вышел {widths[j]:.2f}\" при "
            f"{size:.1f} пт, а слову «{longest}» нужно {mins[j]:.2f}\" — "
            f"оно будет разорвано переносом")
    return hit


def draw_table(s, x, y, table, size, w, tag, *, head_fill=MID,
               head_color=WHITE, zebra=(SURFACE, WHITE)):
    """Таблица полосами: шапка залита, строки через одну. Возвращает высоту.

    `zebra` — пара «нечётная строка, чётная строка», в том порядке, в каком
    их берёт `i % 2`: первая строка после шапки идёт на ПОВЕРХНОСТИ, вторая
    белая. Порядок проверяется регрессией — переставленная пара даёт ровную
    шахматку наоборот, и на снимке это почти не видно, а в XML видно сразу.

    Таблица рисуется прямоугольниками и надписями, а не `add_table`: у
    таблицы python-pptx свои поля, свой шрифт темы и своя тень, и ни одно из
    трёх не подчиняется мере этого пакета."""
    widths, heights, rows = table_geom(table, size, w)
    cy = y
    for i, r in enumerate(rows):
        cx = x
        for j, cell in enumerate(r):
            if i == 0:
                prims.rect(s, cx, cy, widths[j], heights[i], head_fill,
                           count="ячейка")
                col, bold = head_color, True
            else:
                prims.rect(s, cx, cy, widths[j], heights[i],
                           zebra[i % 2], stroke=OUTLINE, stroke_pt=1.0,
                           count="ячейка")
                col, bold = DEEP, "**" in cell
            prims.text_box(s, cx + TBL_CELL_PAD, cy,
                           widths[j] - 2 * TBL_CELL_PAD, heights[i],
                           plain(cell), size=size, bold=bold, color=col,
                           anchor=MSO_ANCHOR.MIDDLE, ls=TBL_ROW_LS,
                           tag=f"{tag}/ячейка")
            cx += widths[j]
        cy += heights[i]
    report.PRIM["таблица"] += 1
    return cy - y


# ── матрица, нарисованная В ПУСТУЮ ──────────────────────────────────
# Владелец, разбор 2026-10-08: «можно прям матрицу, кстати, в пустую
# нарисовать, которую мы будем заполнять, как пример». Оси матрицы — шапка и
# первый столбец — остаются; очищаются только клетки внутри.


def matrix_is_empty(meta):
    """Фронтматтер просит показать матрицу НЕЗАПОЛНЕННОЙ: `matrix_empty:
    true` либо `matrix: {empty: true}` (принимается и `matrix: empty`)."""
    if meta.get("matrix_empty"):
        return True
    m = meta.get("matrix")
    if isinstance(m, dict):
        return bool(m.get("empty"))
    return str(m or "").strip().lower() in ("empty", "пустая", "пустую")


def blank_cells(blocks):
    """Оставить шапку и первый столбец, остальные клетки очистить. Правит
    блоки НА МЕСТЕ — поэтому `slidefile.body_ordered` отдаёт их списками."""
    n = 0
    for kind, val in blocks:
        if kind != "table":
            continue
        for i, row in enumerate(val):
            if i == 0:
                continue
            for j in range(1, len(row)):
                if row[j]:
                    row[j] = ""
                    n += 1
    return n


def apply_matrix_empty(sid, meta, blocks):
    """Применить `matrix_empty` и сказать об этом в отчёте. Заявленная пустая
    матрица без таблицы в теле — это не «нечего делать», а расхождение
    фронтматтера с телом, и оно выходит предупреждением."""
    if not matrix_is_empty(meta):
        return 0
    n = blank_cells(blocks)
    if not any(k == "table" for k, _ in blocks):
        report.warn(f"[матрица] {sid}: заявлена пустая матрица, а таблицы в "
                    "теле слайда нет — рисовать нечего")
    elif n:
        report.warn(f"[матрица] {sid}: показана НЕЗАПОЛНЕННОЙ — очищено "
                    f"клеток {n}, оси (шапка и первый столбец) оставлены")
    return n
