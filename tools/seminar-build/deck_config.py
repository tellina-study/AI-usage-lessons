"""Что у семинара своё: разметка занятия, словарь его приёмов, пути.

Зачем этот модуль существует. До октября 2026 сборщик деки копировался в
папку каждого занятия целиком — и копии расходились: `build_sem06.py` и
`build_sem07.py` отличались 1247 строками из ~1400, при том что
`deck_kit.py`/`metrics.py`/`slide_parts.py` в тех же папках лежали
побайтово одинаковые. Из 1247 строк кодом (не комментарием) отличалось
около четырёхсот, и почти всё это — ТАБЛИЦЫ: где границы блоков, какой
приём какой жанровой функцией рисуется, у каких слайдов цитата золотая.
Таблицы уехали сюда, в `rendered/deck-config.yaml` занятия; код остался
один на все семинары.

Правило, которое этот модуль обязан держать (канон
`tools/presentation-build/seminar-deck-kit.md`, «Зачем это правило»): дека
собирается из ИМЕНОВАННОЙ БИБЛИОТЕКИ ПРИЁМОВ, приём выбирается по полю
`visual.pattern`. Поэтому конфиг занятия не описывает раскладку («сложить
блоки сверху вниз»), а НАЗЫВАЕТ приём на каждое имя из своих слайдов —
`genres:`. Универсальные раскладки вместо словаря приёмов уже стоили
Семинару 5 отклонённой деки.

Состояние здесь модульное, а не объект-контекст: сборка в одном процессе
всегда идёт по ОДНОМУ занятию и ОДНОМУ языку, и притворяться, что их может
быть два, значило бы протаскивать контекст сквозь сорок функций вёрстки
ради случая, которого нет. `configure()` зовётся один раз из `build.py`
до первой отрисовки.
"""

import os
import re
from pathlib import Path

import yaml

# Корень репозитория — три уровня вверх от этого файла
# (tools/seminar-build/deck_config.py).
REPO = Path(__file__).resolve().parent.parent.parent

# Где лежат папки занятий. Переменная среды `SEMINARS_DIR` переводит все
# скрипты этой папки на ДРУГОЕ дерево семинаров, не трогая живое. Это не
# отладочный крючок: критерий приёмки пересборки — побайтовое совпадение
# деки «до» и «после» (канон §7, «свойство проверяется замером»), а проверить
# его, перезаписывая ту самую деку, которую проверяешь, нельзя. Прогон идёт
# на замороженной копии дерева, живая папка занятия при этом не меняется.
SEMINARS = Path(os.environ.get("SEMINARS_DIR") or (REPO / "library" / "seminars"))

# ── Рабочее поле полотна ────────────────────────────────────────────────────
#
# Одно на все семинары: 16:9 при 13,33″ × 7,5″, поля под подпись и номер
# слайда. Эти четыре числа совпадали во всех трёх копиях сборщика, поэтому
# они здесь константы, а не поля конфига: параметр, который никто ни разу
# не менял, в конфиге только предлагает его поменять.
TOP, BOTTOM = 0.34, 6.92
LEFT, WIDTH = 0.55, 12.23
GAP = 0.18                      # шаг между блоками

# ── Сигналы языка ───────────────────────────────────────────────────────────
#
# Свойство ЯЗЫКА, не занятия: по этим признакам `quote_role` отличает
# реплику докладчика от вопроса залу и от оговорки. Поэтому таблица живёт
# в общем коде, а не в конфиге семинара — расходиться ей между занятиями
# незачем.
#
# Шаблон `ask` — объединение шаблонов Семинаров 6 и 7: Семинар 7 добавил
# «не выбирайте». Замерено на всех 64 слайдах Семинара 6: ни один блок
# добавленной альтернативой не ловится, то есть объединение не меняет ни
# одной роли в принятой деке.
LANG_SIGNALS = {
    "ru": {
        "open": ("«",),
        "pairs": (("«", "»"), ("**", "**")),
        "ask": r"выберите|что бы вы|как бы вы|назовите|подумайте|не выбирайте",
        "caveat_open": r"^\W*(оговорка|честный пробел|честно про|честно о\b)",
        "caveat": (r"не проверен|не провер[её]н|не измер|нет данных|не подтвер|"
                   r"не удалось|честного пробела|честный пробел|нечестн"),
    },
    "en": {
        "open": ('"', "“"),
        "pairs": (('"', '"'), ("“", "”"), ("**", "**")),
        "ask": (r"\b(?:pick|choose)\b|\bname (?:yours|both|your|the piece|a |one )"
                r"|what would you|how would you|\bthink (?:about|through)\b"
                r"|say out loud"),
        "caveat_open": r"^\W*(an honest gap|a caveat|honestly about)",
        "caveat": (r"not been verified|not verified|unverified|not measured"
                   r"|no data|not confirmed|an honest gap|honest gap|dishonest"),
    },
}

# ── Состояние: заполняется `configure()` ────────────────────────────────────
SEM = ""                 # «06», «07» — номер занятия строкой, как в именах файлов
ROOT = None              # library/seminars/sem-NN
HERE = None              # .../rendered
FIGDIR = None            # .../rendered/figures
CFG = {}                 # разобранный deck-config.yaml
LANG = "ru"
SPEECH_OPEN = ASK = CAVEAT_OPEN = CAVEAT = None
WRAP_PAIRS = ()

_DECK_CACHE = {}


def configure(seminar, lang="ru"):
    """Прочитать конфиг занятия и встать на него. `seminar` — «07» или «7»."""
    global SEM, ROOT, HERE, FIGDIR, CFG
    SEM = f"{int(seminar):02d}"
    ROOT = SEMINARS / f"sem-{SEM}"
    HERE = ROOT / "rendered"
    FIGDIR = HERE / "figures"
    path = HERE / "deck-config.yaml"
    if not path.exists():
        raise SystemExit(
            f"нет конфига занятия: {path}\n"
            f"Он описывает то, что у семинара своё (разметка, словарь приёмов, "
            f"пути) — см. tools/seminar-build/README.md.")
    CFG = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    _DECK_CACHE.clear()
    set_lang(lang)
    # Длина дорожки кейсов обязана совпадать с числом записей в `case_idx`:
    # расхождение этих двух таблиц даёт не падение, а ТИХО недорисованную
    # дорожку — дека соберётся, и четвёртый кейс просто не появится на
    # дорожке ни на одном дивайдере.
    track, idx = case_track(), case_idx()
    if track or idx:
        if not (len(track) == len(idx) == len(set(idx.values()))):
            raise SystemExit(
                f"Семинар {SEM}: `case_track` ({len(track)}) и `case_idx` "
                f"({len(idx)}, различных {len(set(idx.values()))}) разошлись — "
                f"дорожка кейсов нарисуется неполной")


def set_lang(lang):
    global LANG, SPEECH_OPEN, ASK, CAVEAT_OPEN, CAVEAT, WRAP_PAIRS
    if lang not in LANG_SIGNALS:
        raise SystemExit(f"--lang принимает {'/'.join(LANG_SIGNALS)}, передано «{lang}»")
    if CFG and lang not in (CFG.get("langs") or {}):
        raise SystemExit(
            f"у Семинара {SEM} нет трека «{lang}»: в deck-config.yaml объявлены "
            f"{'/'.join(CFG.get('langs') or {})}. Пока английских слайдов нет, "
            f"собирать EN-деку нечем — это не поломка, а отсутствующий трек.")
    cfg = LANG_SIGNALS[lang]
    LANG = lang
    SPEECH_OPEN = cfg["open"]
    WRAP_PAIRS = cfg["pairs"]
    ASK = re.compile(cfg["ask"], re.I)
    CAVEAT_OPEN = re.compile(cfg["caveat_open"], re.I)
    CAVEAT = re.compile(cfg["caveat"], re.I)
    _DECK_CACHE.clear()


set_lang("ru")


# ── Пути трека ──────────────────────────────────────────────────────────────

def _lang_cfg(lang=None):
    return (CFG.get("langs") or {}).get(lang or LANG) or {}


def slides_dir():
    return _lang_cfg().get("slides", "slides")


def deck_file():
    return _lang_cfg().get("deck", "deck.yaml")


def out_name():
    return _lang_cfg().get("out", f"sem-{SEM}.pptx")


def blocks_names():
    """Имена блоков занятия на текущем языке — ими подписана дорожная карта."""
    return tuple(_lang_cfg().get("blocks") or ())


# ── Таблицы приёмов (всё из конфига, с пустым значением по умолчанию) ───────

def table(name):
    return CFG.get(name) or {}


def pattern_role():
    return table("pattern_role")


def vote_patterns():
    """Приёмы, где зал ГОЛОСУЕТ карточками. Читается в двух местах, и это
    один и тот же список намеренно: блок `cards` такого приёма рисуется рядом
    «ВЫБЕРИ» (`option_row`), а не рядом «ЗАПОМНИ» (пилюли терминов, другая
    работа — §1 канона), И аудит «ответ рядом с вопросом» применяется именно
    к нему. Два почти-одинаковых списка на эти два применения однажды
    разошлись бы молча."""
    return set(CFG.get("vote_patterns") or ())


def divider_patterns():
    """Приёмы-дивайдеры: у них другая грамматика, и аудит «ответ рядом с
    вопросом» к ним не применяется — риторический вопрос в заголовке
    перехода не голосование."""
    return set(CFG.get("divider_patterns") or ())


def case_track():
    return tuple(CFG.get("case_track") or ())


def case_idx():
    return table("case_idx")


# ── Разметка: где мы ────────────────────────────────────────────────────────
#
# Границы блоков заданы ЯВНО парой чисел на блок. Семинар 6 выводил их по
# опорным приёмам (`_anchor_sections`: пять развилок + последняя
# `recap_table`) — защита от того, что параллельные сессии сдвинут номера.
# Замерено на принятой деке Семинара 6: вывод по якорям даёт РОВНО ту же
# таблицу, что статическая, строка в строку. Поэтому вывода здесь нет: два
# источника границ, из которых один повторяет другой, однажды разойдутся
# молча, и чинить придётся тот, который никто не читал.

def sections_for(sid):
    """(строки разметки, имена ступеней) для префикса идентификатора слайда.

    Строка — `[от, до, индекс блока, индекс ступени или null]`. Имя блока
    берётся по индексу из `langs.<язык>.blocks`, а не пишется в строке: так
    EN-трек получает английские имена блоков без второй таблицы границ —
    границы свойство нумерации, а нумерация у двух дек одна."""
    razm = table("razmetka")
    got = razm.get(sid[0]) or razm.get("n") or {}
    names = blocks_names()
    rows = [(lo, hi, names[bi] if bi < len(names) else "", st)
            for lo, hi, bi, st in (got.get("rows") or [])]
    stages = [names[i] for i in (got.get("stages") or []) if i < len(names)]
    return rows, stages


def where(sid):
    n = num(sid)
    for lo, hi, name, stage in sections_for(sid)[0]:
        if lo <= n <= hi:
            return name, stage
    return "", None


# ── Чтение манифеста и слайдов ──────────────────────────────────────────────

_NUM = re.compile(r"^[a-zA-Z]*(\d+)([a-zA-Z]*)$")


def num(sid):
    import metrics as M
    m = _NUM.match(sid)
    if not m:
        M._WARNINGS.append(f"ИМЯ СЛАЙДА [{sid}]: из идентификатора не читается "
                           f"номер — слайд попадёт в конец и без раздела")
        return 10 ** 6
    return int(m.group(1))


def deck_slides(prefix):
    """Слайды из манифеста, а если манифест не про этот префикс — из файлов."""
    key = (LANG, prefix)
    if key in _DECK_CACHE:
        return _DECK_CACHE[key]
    out = None
    try:
        sl = yaml.safe_load(
            (ROOT / deck_file()).read_text(encoding="utf-8"))["slides"]
        if sl and sl[0]["id"][0] == prefix:
            out = sl
    except Exception:
        pass
    if out is None:
        out = deck_from_files(prefix)
    _DECK_CACHE[key] = out
    return out


def deck_from_files(prefix):
    out = []
    sub = slides_dir()
    for f in sorted((ROOT / sub).glob(f"{prefix}*.md")):
        md = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", md, re.S)
        fm = (yaml.safe_load(m.group(1)) if m else {}) or {}
        out.append({"id": fm.get("id") or f.name.split("-")[0],
                    "file": f"{sub}/{f.name}",
                    "visual": fm.get("visual") or {}})
    return sorted(out, key=lambda s: s["id"])


def invalidate():
    """Сбросить кэш манифеста — после того, как `refresh_manifest` его
    перезаписал. Без этого номера слайдов считались бы по прежнему чтению."""
    _DECK_CACHE.clear()


def slide_number(sid):
    ids = [s["id"] for s in deck_slides(sid[0])]
    return ids.index(sid) + 1 if sid in ids else None


def divider_index(sid):
    """Порядковый номер РАЗДЕЛЬНОГО дивайдера в деке, считая с единицы; 0 —
    не такой дивайдер. Считает только приём, названный в конфиге
    `badge_pattern` (по умолчанию `section_divider_macro`): у лёгких
    дивайдеров кейса номерного значка нет вовсе."""
    pat = CFG.get("badge_pattern", "section_divider_macro")
    div = [s["id"] for s in deck_slides(sid[0])
           if (s.get("visual") or {}).get("pattern") == pat]
    return div.index(sid) + 1 if sid in div else 0


def badge_for(sid):
    over = table("badge_override")
    if sid in over:
        return over[sid]
    n = divider_index(sid)
    return n or None


def tag_for(sid, visual_meta):
    """Ярлык развилки. Ни на одной деке курса после круга 2 замечаний
    владельца (правило А6) ярлыков нет — поэтому появление ярлыка это
    предупреждение, а не тихое исполнение."""
    import metrics as M
    tag = (visual_meta or {}).get("tag") or table("tags").get(sid)
    if tag:
        M._WARNINGS.append(
            f"ЯРЛЫК НА РАЗВИЛКЕ [{sid}]: `tag: {tag}` — ярлыков на развилках "
            f"нет ни на одной деке курса (правило А6); уберите строку `tag:`")
    return tag


# ── Схемы ───────────────────────────────────────────────────────────────────

def figs():
    """Таблица «слайд → файл схемы» на случай, когда схему объявляет не сам
    слайд. Пустая на Семинарах 6 и 7: схему объявляет фронтматтер слайда,
    и это правильное место — слайд главнее таблицы."""
    return table("figs")


def slide_figure(sid):
    for s in deck_slides(sid[0]):
        if s["id"] == sid:
            return (s.get("visual") or {}).get("figure")
    return None


def figure_for(sid):
    fn = slide_figure(sid) or figs().get(sid)
    if not fn:
        return None
    path = FIGDIR / fn
    return path if path.exists() else None
