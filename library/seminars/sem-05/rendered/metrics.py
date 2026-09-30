"""Измерение текста: сколько места он реально займёт в рамке заданной ширины.

Зачем отдельный модуль. Прежняя вёрстка считала высоту по ЧИСЛУ элементов
(`0.32 × пунктов + 0.26`, `0.40 × строк + 0.2`) — то есть предполагала, что
каждый пункт и каждая строка таблицы занимают ровно одну строку текста. Любой
пункт длиннее одной строки ломал расчёт, и коробка переполнялась: ревью нашло
три вываливающихся рамки и 14 таблиц из 28, которые в настоящем PowerPoint
вырастут выше отведённого. Здесь высота считается по РЕАЛЬНОМУ переносу.

Честная оговорка про шрифт. Дека задаёт Arial, в окружении его нет — есть
только DejaVu. Для кириллицы DejaVu шире Arial примерно на 5–10%. Поэтому
ширина, измеренная по DejaVu, умножается на ARIAL_K, и все выводы о влезании
остаются консервативными: если по этой мерке текст влезает, в настоящем Arial
он влезает с запасом. Обратное неверно, и это ровно та сторона, в которую
ошибаться безопасно.
"""
from functools import lru_cache
from PIL import ImageFont

# ВАЖНО: поправка на шрифт нужна В ДВЕ РАЗНЫЕ СТОРОНЫ, и перепутать их — значит
# systematically недооценивать высоту рамок.
#
#   * Когда РАЗМЕЧАЕМ рамку, безопасно считать текст ШИРОКИМ: если высота
#     посчитана по DejaVu, в настоящем Arial (он у́же) текст займёт столько же
#     или меньше — и уж точно не вылезет. Поэтому K_LAYOUT = 1.0.
#   * Когда ОБЪЯВЛЯЕМ переполнение дефектом, безопасно считать текст УЗКИМ:
#     иначе предупреждение окажется артефактом чужого шрифта. Поэтому
#     K_REPORT = 0.88 — та же поправка, которой пользовалось ревью дизайна.
#
# Прежняя версия этого файла применяла 0.88 и к разметке тоже: рамки выходили
# у́же нужного, и золотая коробка вопроса на s09 не вмещала последнюю строку.
K_LAYOUT = 1.00
K_REPORT = 0.88
MONO_K = 1.0            # Consolas и DejaVu Sans Mono совпадают по ширине знака

_FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
_FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
_FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

# Кегль в pt → растр в 4× для устойчивого измерения коротких строк
_RASTER = 4


@lru_cache(maxsize=256)
def _font(size_pt, bold, mono):
    path = _FM if mono else (_FB if bold else _FR)
    return ImageFont.truetype(path, max(4, int(round(size_pt * _RASTER))))


@lru_cache(maxsize=20000)
def text_w(s, size_pt, bold=False, mono=False):
    """Ширина строки в дюймах при кегле `size_pt` — по мерке РАЗМЕТКИ (K_LAYOUT)."""
    if not s:
        return 0.0
    raw = _font(size_pt, bold, mono).getlength(s) / _RASTER / 72.0
    return raw * (MONO_K if mono else K_LAYOUT)


def wrap(s, size_pt, width_in, bold=False, mono=False):
    """Разбиение строки по словам на ширину `width_in` — тот же перенос, что
    сделает PowerPoint. Слово длиннее строки не режется: оно и в PowerPoint
    вылезет, и пусть это будет видно в предупреждении, а не спрятано."""
    if not s:
        return [""]
    out = []
    for para in s.split("\n"):
        line = ""
        for word in para.split():
            probe = (line + " " + word).strip()
            if line and text_w(probe, size_pt, bold, mono) > width_in:
                out.append(line)
                line = word
            else:
                line = probe
        out.append(line)
    return out


def nlines(s, size_pt, width_in, bold=False, mono=False):
    return len(wrap(s, size_pt, width_in, bold, mono))


def line_h(size_pt, spacing=1.18):
    """Высота строки в дюймах. 1.18 — межстрочный, который python-pptx ставит
    по умолчанию для Arial; та же величина используется при задании фигур."""
    return size_pt * spacing / 72.0


def text_h(s, size_pt, width_in, *, spacing=1.18, bold=False, mono=False, pad=0.0):
    """Высота, которую текст займёт в рамке ширины `width_in`, в дюймах."""
    return nlines(s, size_pt, width_in, bold, mono) * line_h(size_pt, spacing) + pad


def block_h(lines, size_pt, width_in, *, spacing=1.18, space_after=0.0,
            bold=False, mono=False, pad=0.0):
    """То же для списка абзацев — каждый переносится сам по себе."""
    total = 0.0
    for i, ln in enumerate(lines):
        total += nlines(ln, size_pt, width_in, bold, mono) * line_h(size_pt, spacing)
        if i < len(lines) - 1:
            total += space_after / 72.0
    return total + pad


def rich_h(s, size_pt, width_in, *, spacing=1.18, bold=False, pad=0.0):
    """Высота текста, в котором могут быть `моноширинные` куски.

    Consolas заметно шире Arial, поэтому строку с кодом внутри нельзя мерить
    пропорциональным шрифтом: замер даст меньше строк, чем отрисовка, и текст
    вылезет из ячейки. Если моноширинный кусок в строке есть, вся строка
    меряется по моноширинному — оценка консервативная в безопасную сторону.
    Так переполнялись ячейки таблицы вывода хука."""
    mono = "`" in s
    return text_h(s.replace("`", ""), size_pt, width_in, spacing=spacing,
                  bold=bold, mono=mono, pad=pad)


def fit_size(s, width_in, height_in, sizes, *, spacing=1.18, bold=False, mono=False):
    """Наибольший кегль из `sizes` (по убыванию), при котором текст влезает в
    рамку. Если не влезает ни один — возвращается наименьший: вёрстка обязана
    что-то нарисовать, а о переполнении скажет `fits()`."""
    for size in sizes:
        if text_h(s, size, width_in, spacing=spacing, bold=bold, mono=mono) <= height_in:
            return size
    return sizes[-1]


_WARNINGS = []


def fits(s, size_pt, width_in, height_in, *, label="", spacing=1.18,
         bold=False, mono=False, tol=0.02):
    """Диагностика влезания. Копит предупреждения и печатает их при сборке —
    приём Семинара 4 (`_fits`), но высота меряется, а не оценивается по числу
    знаков в строке. Возвращает True/False, чтобы вёрстка могла не только
    пожаловаться, но и подстроиться."""
    if not s or width_in <= 0 or height_in <= 0:
        return True
    # предупреждение печатается по мерке ОТЧЁТА: то, что переживает поправку
    # на более узкий Arial, — настоящее переполнение, а не артефакт DejaVu
    need = text_h(s, size_pt, width_in / K_REPORT, spacing=spacing, bold=bold, mono=mono)
    if need > height_in + tol:
        _WARNINGS.append(
            f"ПЕРЕПОЛНЕНИЕ [{label}]: «{s[:46]}…» при {size_pt} pt в {width_in:.2f}″ "
            f"требует {need:.2f}″, отведено {height_in:.2f}″ (+{need - height_in:.2f}″)")
        return False
    return True


def report():
    """Список накопленных предупреждений; вызывается в конце сборки."""
    return list(_WARNINGS)


def reset():
    _WARNINGS.clear()
