# -*- coding: utf-8 -*-
"""РАЗБОР НА ИЗОБРАЖЕНИИ `vynoski:` — дефект вот ЗДЕСЬ, а не вообще.

Перенос приёма §2.1 + §2.2 из `library/lectures/lec-08/rework-v5/
PERENOS-PRIYOMOV.md`. В образце (`image/s09` чужой деки) к трём конкретным
местам картинки притянуты указателями три бокса разбора. Владелец назвал это
лучшим приёмом обеих образцовых презентаций, и назвал почему: «у нас отказы
названы словами рядом с картинкой — и читатель обязан сам найти на ней, о чём
речь. Тут искать не надо».

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ: «названное словом находится вот в этой точке
изображения». Этого не утверждает ни одна другая форма ядра. Боковая
иллюстрация (`media.py`) УТВЕРЖДАЕТ «вот как это выглядит» и оставляет поиск
залу; полоса плашек утверждает состав счёта; схема — порядок. Привязка слова
к пикселю — здесь и больше нигде, и ради неё одной форма и заведена.

ЧЕМ ЭТА ФОРМА НЕ ЯВЛЯЕТСЯ — иллюстрацией с подписями. Если указателю не во
что упереться (на картинке нет РАЗЛИЧИМОГО места, про которое идёт речь), то
кадру нужна не эта форма, а боковой снимок с подписью: указатель, ткнувший в
произвольную точку однородного фона, утверждает ложь — «дефект вот здесь», —
и утверждает её тем убедительнее, чем аккуратнее нарисован.

Разметка кадра:

    vynoski:
      image: assets/screenshots/s26-sgenerirovannaya-ruka.png
      caption: "подпись под изображением"      # необязательно
      crop: false                              # необязательно, см. ниже
      points:
        - at: [0.22, 0.31]        # доля ШИРИНЫ и ВЫСОТЫ изображения
          side: left              # left | right — с какой стороны бокс
          head: "Отказ 1: псевдобуквы"
          text: "Сжатие в 48 раз в автокодировщике…"

`at` — доли САМОГО ИЗОБРАЖЕНИЯ, не кадра. Это не придирка к формулировке: в
рамку изображение вписывается по своей пропорции и почти никогда не занимает
её целиком, так что доли кадра указали бы мимо на величину полей — и мимо
по-разному на разных кадрах, то есть незаметно.

ПОЧЕМУ ЗОЛОТО ЗДЕСЬ ТОЛЬКО ЗАЛИВКОЙ. Номер выноски — кружок с ЗОЛОТОЙ
ЗАЛИВКОЙ и тёмной цифрой поверх, 6,85 : 1. Золотая цифра на светлом боксе
дала бы 1,99 при пороге 3,0 (`contrast.py`, замер владельца) — ровно тот
дефект P0, который прожарка 2026-10-14 нашла на 60 кадрах Лекции 7 из 109.
Правило §1 переноса («где в образце золотой ТЕКСТ — у нас золотая ЗАЛИВКА с
тёмным текстом поверх») здесь не рекомендация, а то, из-за чего форма не
имеет настройки цвета цифры.

ПОЧЕМУ БОКСЫ ЛЕЖАТ НА ИЗОБРАЖЕНИИ, А НЕ РЯДОМ С НИМ. Требование §2.2 —
изображение ≥55% площади кадра. Это измеримо несовместимо с боксами в полях:
две колонки по 3,1" оставляют изображению 5,9" ширины, то есть при любой
пропорции не больше 33% площади. Боксы поэтому ложатся ПОВЕРХ краёв
изображения, как в образце, а `check_vynoski` следит за единственным, что при
этом нельзя нарушить: ни один бокс не накрывает ни одной точки `at` — ни
своей, ни чужой. Бокс, закрывший место, на которое указывает, отменяет всю
форму.

ЧЕГО ЭТА ФОРМА НЕ ДЕЛАЕТ. Не ужимает кегль, чтобы вместить пятую выноску:
предел 2–4 назван отказом (`[выноски]`), а не подгонкой. Не обрезает
изображение сама: вертикальный снимок 55% не наберёт, и об этом сказано
числом с названной причиной — выбор между «взять кадр шире» и «обрезать»
(`crop: true`) принадлежит владельцу, как и везде в этом пакете.

ТЕГ `[выноски]` НЕ БЛОКИРУЮЩИЙ, и это не решение формы: перечень блокирующих
тегов закреплён в `report.BLOCKING`, а этот модуль чужих файлов не трогает.
Пятая выноска и бокс поверх своей точки — дефекты того же рода, что
`[высота]`, и место им там же; завести их туда — отдельный шаг, за тем, кто
связывает форму со сборщиком.
"""
from dataclasses import dataclass
from pathlib import Path

from pptx.enum.shapes import MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

from . import floor, metrics, prims, report
from .theme import (DEEP, GOLD, LIGHT, MID, SLIDE_H, SLIDE_W, SURFACE,
                    WHITE)

SIDES = ("left", "right")


@dataclass(frozen=True)
class VynoskiStyle:
    # ── колонка выносок ──────────────────────────────────────────────
    col_w: float = 3.10          # ширина бокса выноски
    box_pad: float = 0.14
    box_gap: float = 0.16        # просвет между боксами одной стороны
    core_min: float = 4.60       # полоса изображения, которую колонки не
                                 # вправе съесть целиком: уже этого от
                                 # «крупного изображения» остаётся лента
    # ── текст выноски ────────────────────────────────────────────────
    head_pt: float = 14.0        # пол видимого слоя, см. `floor.py`
    head_ls: float = 1.10
    body_pt: float = 12.0        # «на кегль меньше» (§2.1), и он же пол
    body_ls: float = 1.16
    head_gap: float = 0.08
    # ── номер ────────────────────────────────────────────────────────
    num_d: float = 0.34          # поперечник золотого кружка
    num_pt: float = 12.0
    num_gap: float = 0.10        # просвет между кружком и заголовком
    # ── указатель ────────────────────────────────────────────────────
    lead_pt: float = 1.5         # толщина линии указателя
    dot_d: float = 0.13          # точка на конце, в самой точке `at`
    halo_pt: float = 2.5         # НАДБАВКА к толщине линии: белая
                                 # подложка под ней, см. `_leader`
    halo_d: float = 0.06         # белый ободок точки, та же причина
    min_lead: float = 0.40       # короче — указатель не читается указателем
    # ── подпись под изображением ─────────────────────────────────────
    cap_pt: float = 12.0         # пол видимого слоя
    cap_ls: float = 1.14
    cap_gap: float = 0.10
    # ── пределы ──────────────────────────────────────────────────────
    max_points: int = 4
    min_points: int = 2
    max_img_h: float = 6.10      # высота, больше которой тело кадра не
                                 # бывает: поле сверху под заголовок
    min_share: float = 0.55      # §2.2: доля площади кадра под изображение


DEFAULT = VynoskiStyle()


# ── разбор поля ──────────────────────────────────────────────────────


def _pt_pair(raw):
    """`at` → пара долей или None. Форму проверяем здесь, диапазон — в
    `check_vynoski`: «не два числа» мешает СЧИТАТЬ раскладку, а «0,22 и 1,4»
    посчитать не мешает, мешает смотреть, и сказать об этом надо иначе."""
    if not isinstance(raw, (list, tuple)) or len(raw) != 2:
        return None
    try:
        return (float(raw[0]), float(raw[1]))
    except (TypeError, ValueError):
        return None


def vynoski_of(sl, st=DEFAULT, root=None):
    """Поле `vynoski` → разобранный разбор или None.

    `root` — каталог выпуска, от которого считается `image`, ровно как
    `media.media_path` считает `media`: от папки выпуска, а не от корня
    репозитория (`notes/mcp-limitations.md` [#301-4] — тринадцать «недобытых»
    снимков Лекции 8 оказались ровно этой ошибкой). Путь резолвится ЗДЕСЬ, а
    не при рисовании, потому что пропорция изображения нужна уже мере высоты.

    Чужая форма поля сборку не роняет: она называется `[выноски]`, и кадр
    собирается без разбора — тот же договор, что у `figure_of`/`scheme_of`."""
    raw = sl.meta.get("vynoski")
    if raw in (None, "", [], {}):
        return None
    sid = sl.sid
    if not isinstance(raw, dict):
        report.warn(f"[выноски] {sid}: поле `vynoski` — "
                    f"{type(raw).__name__}, а должно быть image/points")
        return None
    img = str(raw.get("image") or "").strip()
    if not img:
        report.warn(f"[выноски] {sid}: в `vynoski` не названо `image` — "
                    "разбору не на чем стоять: эта форма привязывает слово "
                    "к месту ИЗОБРАЖЕНИЯ, и без него она не иллюстрация "
                    "без картинки, а разбор без предмета")
        return None
    path = Path(img) if Path(img).is_absolute() else Path(root or ".") / img
    pts_raw = raw.get("points")
    if not isinstance(pts_raw, (list, tuple)):
        report.warn(f"[выноски] {sid}: в `vynoski` нет списка `points` — "
                    f"стоит {type(pts_raw).__name__}")
        return None
    points = []
    for i, p in enumerate(pts_raw, 1):
        if not isinstance(p, dict):
            report.warn(f"[выноски] {sid}: выноска {i} — "
                        f"{type(p).__name__}, а должна быть at/side/head/text")
            continue
        side = str(p.get("side") or "left").strip().lower()
        points.append({
            "n": i,
            "at": _pt_pair(p.get("at")),
            "at_raw": p.get("at"),
            "side": side,
            "head": str(p.get("head") or "").strip(),
            "text": str(p.get("text") or "").strip(),
        })
    if not points:
        report.warn(f"[выноски] {sid}: в `points` не разобрано ни одной "
                    "выноски")
        return None
    return {"image": img, "path": path, "exists": path.exists(),
            "caption": str(raw.get("caption") or "").strip(),
            "crop": bool(raw.get("crop")), "points": points}


# ── мера ─────────────────────────────────────────────────────────────


def _col_w(v, w, st):
    """Ширина колонки: названная — или ужатая так, чтобы между колонками
    осталась полоса изображения `core_min`. Ужатие МОЛЧА: оно спасает кадр от
    двух колонок, сомкнувшихся посередине, и о том, что места мало, скажет
    своим голосом проверка доли площади."""
    sides = {p["side"] for p in v["points"]}
    n = 2 if len(sides & set(SIDES)) > 1 else 1
    room = (w - st.core_min) / n if n else w
    return max(1.60, min(st.col_w, room))


def _box_h(p, cw, st):
    """Высота одного бокса: поле · заголовок рядом с кружком · тело · поле."""
    inner = cw - 2 * st.box_pad
    head_w = inner - st.num_d - st.num_gap
    hh = max(st.num_d,
             metrics.est_h(p["head"] or "—", st.head_pt, max(0.4, head_w),
                           st.head_ls, True))
    h = 2 * st.box_pad + hh
    if p["text"]:
        h += st.head_gap + metrics.est_h(p["text"], st.body_pt,
                                         max(0.4, inner), st.body_ls)
    return h


def _cap_h(v, w, st):
    if not v["caption"]:
        return 0.0
    return metrics.est_h(v["caption"], st.cap_pt, w, st.cap_ls, False, True)


def _ar(v):
    """Пропорция изображения, или None — файла нет."""
    if not v["exists"]:
        return None
    try:
        iw, ih = prims.img_size(v["path"])
        return iw / max(1, ih)
    except Exception:                                    # noqa: BLE001
        return None


def _stack(items, top, bottom, gap):
    """Вертикальная раскладка боксов одной стороны: каждый как можно ближе к
    своей точке, но без наложений и в границах.

    СЧИТАЕТСЯ, А НЕ УГАДЫВАЕТСЯ, и вот чем именно. Проход сверху вниз ставит
    бокс на его желаемое место либо под нижний край предыдущего — что ниже.
    Если последний вылез за нижнюю границу, вся стопка сдвигается вверх на
    величину выезда и проход повторяется с зажимом по верхней границе: иначе
    сдвиг вверх вылезает за верх так же молча, как вылезал за низ.

    `items` — список (желаемый верх, высота) В ПОРЯДКЕ СВЕРХУ ВНИЗ по
    желаемому верху. Возвращает список верхов и признак «не уместилось»."""
    if not items:
        return [], False
    tops, cur = [], top
    for want, hh in items:
        t = max(cur, want)
        tops.append(t)
        cur = t + hh + gap
    over = (tops[-1] + items[-1][1]) - bottom
    if over > 0:
        tops = [t - over for t in tops]
        cur = top
        for i, (_want, hh) in enumerate(items):
            tops[i] = max(tops[i], cur)
            cur = tops[i] + hh + gap
    need = sum(hh for _w, hh in items) + gap * (len(items) - 1)
    return tops, need > (bottom - top) + 1e-6


def layout(v, w, h, st=DEFAULT, x=0.0, y=0.0):
    """Вся геометрия формы одной функцией: изображение, боксы, точки.

    Одна функция на меру, проверку и рисование нарочно. Проверка, считающая
    раскладку ВТОРЫМ кодом, проверяет не то, что нарисуется, — и расходится с
    рисованием ровно в тех случаях, ради которых её писали."""
    cap_h = _cap_h(v, w, st)
    img_h = max(0.5, h - (st.cap_gap + cap_h if cap_h else 0.0))
    ar = _ar(v)
    if v["crop"] or ar is None:
        ix, iy, iw, ih = x, y, w, img_h
    else:
        dx, dy, iw, ih = prims.fit(v["path"], w, img_h)
        ix, iy = x + dx, y + dy
    cw = _col_w(v, w, st)
    out = {"img": (ix, iy, iw, ih), "cap_h": cap_h, "img_h": img_h,
           "col_w": cw, "boxes": [], "overflow": set()}
    for p in v["points"]:
        at = p["at"] or (0.5, 0.5)
        p["_px"] = ix + at[0] * iw
        p["_py"] = iy + at[1] * ih
    anchor_dy = st.box_pad + st.num_d / 2
    for side in SIDES:
        mine = [p for p in v["points"] if p["side"] == side]
        mine.sort(key=lambda p: p["_py"])
        items = [(p["_py"] - anchor_dy, _box_h(p, cw, st)) for p in mine]
        tops, over = _stack(items, y, y + img_h, st.box_gap)
        if over:
            out["overflow"].add(side)
        bx = x if side == "left" else x + w - cw
        for p, t, (_want, hh) in zip(mine, tops, items):
            sx = bx + cw if side == "left" else bx
            ay = t + anchor_dy
            lead = ((p["_px"] - sx) ** 2 + (p["_py"] - ay) ** 2) ** 0.5
            # Указатель, идущий НАЗАД (точка с изнанки своего бокса),
            # считается отрицательной длиной: иначе стержень длиной 0,8",
            # ушедший под бокс, читался бы мерой как хороший указатель.
            if (side == "left" and p["_px"] < sx) or \
                    (side == "right" and p["_px"] > sx):
                lead = -lead
            out["boxes"].append({"p": p, "x": bx, "y": t, "w": cw, "h": hh,
                                 "anchor_y": ay, "lead_x": sx, "lead": lead,
                                 "side": side})
    out["boxes"].sort(key=lambda b: b["p"]["n"])
    return out


def vynoski_h(v, w, st=DEFAULT):
    """Высота формы — она же всё тело кадра: это форма «во весь кадр».

    Изображению отдаётся вся ширина и столько высоты, сколько берёт его
    пропорция, но не больше `max_img_h` и не меньше, чем нужно самой высокой
    стопке боксов: бокс, вылезший под изображение, висит на белом и теряет
    привязку к предмету."""
    cap_h = _cap_h(v, w, st)
    cw = _col_w(v, w, st)
    need = 0.0
    for side in SIDES:
        mine = [p for p in v["points"] if p["side"] == side]
        if not mine:
            continue
        s = sum(_box_h(p, cw, st) for p in mine) + st.box_gap * (len(mine) - 1)
        need = max(need, s)
    ar = _ar(v)
    img_h = st.max_img_h if ar is None else min(st.max_img_h, w / ar)
    img_h = min(st.max_img_h, max(img_h, need))
    return img_h + (st.cap_gap + cap_h if cap_h else 0.0)


def img_share(v, w, st=DEFAULT):
    """Доля площади КАДРА под изображением — та же величина, которую потом
    замерит `media.page_image_share` по собранному файлу."""
    lay = layout(v, w, vynoski_h(v, w, st), st)
    _ix, _iy, iw, ih = lay["img"]
    return iw * ih / (SLIDE_W * SLIDE_H)


# ── проверка ─────────────────────────────────────────────────────────


def _inside(bx, by, bw, bh, px, py, pad=0.0):
    return (bx - pad <= px <= bx + bw + pad
            and by - pad <= py <= by + bh + pad)


def check_vynoski(sid, v, w, st=DEFAULT):
    """`[выноски]`: всё, из-за чего разбор на изображении перестаёт быть
    разбором. Каждое — про то, что видно на экране, а не про вкус."""
    pts = v["points"]
    n = len(pts)

    if not v["exists"]:
        report.warn(
            f"[выноски] {sid}: изображения «{v['image']}» нет на диске "
            f"(искали {v['path']}). Путь считается от папки выпуска, а не от "
            "корня репозитория — это та самая ошибка, из-за которой на "
            "Лекции 8 тринадцать лежащих на диске снимков читались как "
            "недобытые (`notes/mcp-limitations.md` [#301-4])")

    if n < st.min_points:
        report.warn(
            f"[выноски] {sid}: выноска одна. Одна выноска — это ПОДПИСЬ, и "
            "кадру с подписью нужен боковой снимок (`media`), а не эта "
            "форма: разбор на изображении утверждает «вот это здесь, а вот "
            "то там», и утверждать это одной точкой нечем")
    if n > st.max_points:
        report.warn(
            f"[выноски] {sid}: выносок {n} при пределе {st.max_points}. "
            f"{n}-ю не ужимают кеглем — её выносят на отдельный кадр: "
            "боксы делят с изображением одну высоту, и каждый следующий "
            "отнимает место у того самого предмета, на который указывает")

    for p in pts:
        tag = f"выноска {p['n']}"
        if p["at"] is None:
            report.warn(
                f"[выноски] {sid}: у {tag} `at` — {p['at_raw']!r}, а должно "
                "быть две доли изображения, [0.22, 0.31]")
        else:
            bad = [f"{a:.2f}" for a in p["at"] if not (0.0 <= a <= 1.0)]
            if bad:
                report.warn(
                    f"[выноски] {sid}: у {tag} `at` = "
                    f"[{p['at'][0]:.2f}, {p['at'][1]:.2f}] — "
                    f"{'доля' if len(bad) == 1 else 'доли'} вне диапазона "
                    "[0, 1]: это ДОЛИ самого изображения, а не дюймы кадра и "
                    "не проценты. Указатель уехал бы мимо предмета")
        if p["side"] not in SIDES:
            report.warn(
                f"[выноски] {sid}: у {tag} `side` = «{p['side']}», а бывает "
                f"{' или '.join(SIDES)}")
        if not p["head"]:
            report.warn(
                f"[выноски] {sid}: у {tag} пуст `head` — бокс без заголовка "
                "не называет, ЧТО он нашёл в этой точке")

    if not v["exists"] or any(p["at"] is None for p in pts):
        return                      # дальше геометрия всё равно вымышленная

    h = vynoski_h(v, w, st)
    lay = layout(v, w, h, st)

    for side in sorted(lay["overflow"]):
        hh = sum(b["h"] for b in lay["boxes"] if b["side"] == side)
        where = "слева" if side == "left" else "справа"
        report.warn(
            f"[выноски] {sid}: боксы {where} не укладываются по высоте — "
            f"{hh:.2f}\" текста на {lay['img_h']:.2f}\" кадра. Сокращают "
            "разбор или переносят выноску на другую сторону; кегль здесь "
            "уже на полу видимого слоя")

    for b in lay["boxes"]:
        for p in pts:
            if _inside(b["x"], b["y"], b["w"], b["h"], p["_px"], p["_py"]):
                own = " (свою же)" if p is b["p"] else ""
                report.warn(
                    f"[выноски] {sid}: бокс выноски {b['p']['n']} накрывает "
                    f"точку выноски {p['n']}{own} — место, на которое "
                    "указывают, закрыто тем, что на него указывает. Это "
                    "отменяет всю форму: сдвиньте `at` ближе к середине "
                    "изображения либо переставьте выноску на другую `side`")

    for b in lay["boxes"]:
        if b["lead"] >= st.min_lead - 1e-9:
            continue
        where = "уходит назад, под свой же бокс" if b["lead"] < 0 else \
            f"всего {b['lead']:.2f}\" при пороге {st.min_lead:.2f}\""
        report.warn(
            f"[выноски] {sid}: указатель выноски {b['p']['n']} {where}. "
            "Такой указатель не читается указателем — он читается обрывком "
            "рамки, и привязка слова к месту пропадает. Точка `at` стоит "
            "почти вплотную к краю изображения: сдвиньте её к середине либо "
            "переставьте выноску на противоположную `side`")

    _ix, _iy, iw, ih = lay["img"]
    share = iw * ih / (SLIDE_W * SLIDE_H)
    if share < st.min_share - 1e-9:
        ar = _ar(v)
        report.warn(
            f"[выноски] {sid}: изображение занимает {100 * share:.1f}% "
            f"площади кадра при пороге {100 * st.min_share:.0f}% (§2.2 "
            f"переноса: «крупное изображение как предмет разбора»). "
            f"Пропорция снимка {ar:.2f} — при ней шире его не сделать. "
            "Починка не одна: взять кадр шире, либо `crop: true` (обрезка по "
            "длинной стороне), либо отдать кадру боковой снимок с подписью. "
            "Выбор меняет кадр — решение владельца, не сборки")


# ── рисование ────────────────────────────────────────────────────────


def _line(s, x1, y1, x2, y2, color, width_pt):
    """Прямая линия от точки к точке.

    СОБСТВЕННЫЙ ПРИМИТИВ, И ЭТО НАЗВАНО ВСЛУХ. В `prims.py` линии нет: его
    словарь — прямоугольник, скруглённая коробка, стрелка-фигура, чип,
    надпись, снимок. Указатель под произвольным углом ни одним из них не
    рисуется (повёрнутый тонкий прямоугольник потребовал бы угла, которого
    `prims.rect` не принимает), а править общий файл этой нити нельзя —
    параллельно работают другие. Поэтому примитив лежит здесь, в том же
    договоре, что и остальные: тень снимается, рисунок считается.

    Тому, кто будет связывать форму со сборщиком: это кандидат на переезд в
    `prims.py` под именем `line`."""
    shp = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1),
                                 Inches(y1), Inches(x2), Inches(y2))
    shp.line.color.rgb = color
    shp.line.width = Pt(width_pt)
    prims.no_shadow(shp)
    return shp


def _leader(s, x1, y1, x2, y2, st):
    """Указатель: синяя линия `#065A82` 1,5 пт по БЕЛОЙ подложке.

    Подложка — не украшение. Указатель идёт ПО СНИМКУ, а снимок бывает любой:
    на тёмном кадре (ночной план, тёмная студия, чёрный фон генерации) линия
    `#065A82` 1,5 пт пропадает целиком, и форма молча превращается в боксы
    без привязки — тот самый дефект, ради устранения которого она заведена.
    Белая линия шире синей на `halo_pt` держит её видимой на любом снимке, а на
    светлом читается как тонкая окантовка, а не как вторая линия.

    Проверить это в сборке нечем: цвет пикселя под линией из XML не
    читается — то же место, где `contrast.background` честно говорит «снимок
    — не измерен». Подложка здесь поэтому не настройка под кадр, а то, что
    стоит всегда."""
    _line(s, x1, y1, x2, y2, WHITE, st.lead_pt + st.halo_pt)
    shp = _line(s, x1, y1, x2, y2, MID, st.lead_pt)
    report.PRIM["указатель"] += 1
    return shp


def _dot(s, cx, cy, d, color, count, *, halo=0.0):
    """Кружок поперечником `d` с центром в (cx, cy), при `halo` — с белым
    ободком той же толщины, что подложка указателя, и по той же причине.

    Круг — это скруглённый прямоугольник с полным скруглением: `prims.rect`
    принимает долю скругления, и 0,5 от половины короткой стороны квадрата
    даёт ровно окружность. Отдельной овальной фигуры ради этого не заводим."""
    if halo:
        prims.rect(s, cx - (d + halo) / 2, cy - (d + halo) / 2,
                   d + halo, d + halo, WHITE, radius=True, radius_adj=0.5,
                   count=None)
    return prims.rect(s, cx - d / 2, cy - d / 2, d, d, color,
                      radius=True, radius_adj=0.5, count=count)


def draw_vynoski(s, sid, v, x, y, w, h, st=DEFAULT, tag=None):
    """Изображение во весь кадр, боксы разбора поверх его краёв, указатели к
    точкам. Возвращает занятую высоту.

    ПОРЯДОК РИСОВАНИЯ НЕСЁТ СМЫСЛ, и не только видимый. Сначала изображение,
    затем указатели, затем точки, затем боксы с текстом: указатель уходит ПОД
    бокс (его начало не торчит из-под рамки), а каждая надпись ложится на
    сплошную заливку, которая нарисована РАНЬШЕ неё. Второе — не косметика:
    `contrast.background` читает фон по z-порядку собранного файла, и надпись,
    под которой оказался снимок, а не коробка, уходит в «не измерено», то есть
    выпадает из-под сторожа контраста целиком."""
    tag = tag or sid
    lay = layout(v, w, h, st, x=x, y=y)
    ix, iy, iw, ih = lay["img"]

    if v["crop"] and v["exists"]:
        prims.add_image_cover(s, v["path"], ix, iy, iw, ih, tag=f"{tag}/кадр")
    else:
        prims.add_image(s, v["path"], x, y, w, lay["img_h"], tag=f"{tag}/кадр")

    for b in lay["boxes"]:
        p = b["p"]
        _leader(s, b["lead_x"], b["anchor_y"], p["_px"], p["_py"], st)
    for b in lay["boxes"]:
        _dot(s, b["p"]["_px"], b["p"]["_py"], st.dot_d, MID, "точка",
             halo=st.halo_d)

    for b in lay["boxes"]:
        p = b["p"]
        prims.ocean_box(s, b["x"], b["y"], b["w"], b["h"],
                        fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
        inner = b["w"] - 2 * st.box_pad
        ncx = b["x"] + st.box_pad + st.num_d / 2
        ncy = b["y"] + st.box_pad + st.num_d / 2
        _dot(s, ncx, ncy, st.num_d, GOLD, "номер")
        report.GOLD_SEEN.add(sid)
        floor.pt(st.num_pt, tag, "номер выноски")
        prims.text_box(s, ncx - st.num_d / 2, ncy - st.num_d / 2 + 0.015,
                       st.num_d, st.num_d, str(p["n"]), size=st.num_pt,
                       bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                       anchor=MSO_ANCHOR.MIDDLE, ls=1.0,
                       tag=f"{tag}/номер{p['n']}", quiet=True)
        b_w = inner - st.num_d - st.num_gap
        hx = b["x"] + st.box_pad + st.num_d + st.num_gap
        hh = max(st.num_d, metrics.est_h(p["head"] or "—", st.head_pt,
                                         max(0.4, b_w), st.head_ls, True))
        floor.pt(st.head_pt, tag, "заголовок выноски")
        prims.text_box(s, hx, b["y"] + st.box_pad, b_w, hh, p["head"] or "—",
                       size=st.head_pt, bold=True, color=DEEP,
                       ls=st.head_ls, tag=f"{tag}/выноска{p['n']}/заголовок")
        if p["text"]:
            floor.pt(st.body_pt, tag, "тело выноски")
            th = metrics.est_h(p["text"], st.body_pt, max(0.4, inner),
                               st.body_ls)
            prims.text_box(s, b["x"] + st.box_pad,
                           b["y"] + st.box_pad + hh + st.head_gap,
                           inner, th, p["text"], size=st.body_pt, color=DEEP,
                           ls=st.body_ls, tag=f"{tag}/выноска{p['n']}/тело")

    if lay["cap_h"]:
        floor.pt(st.cap_pt, tag, "подпись под изображением")
        prims.text_box(s, x, y + lay["img_h"] + st.cap_gap, w, lay["cap_h"],
                       v["caption"], size=st.cap_pt, italic=True, color=LIGHT,
                       ls=st.cap_ls, tag=f"{tag}/подпись")
    report.PRIM["разбор на изображении"] += 1
    return h


# ── переходник под общий договор форм (`axis.py`, `figure.py`) ───────


def parse(sl, root=None):
    return vynoski_of(sl, root=root)


def height(v, w):
    return vynoski_h(v, w)


def check(sid, v, w):
    return check_vynoski(sid, v, w)


def draw(s, sid, v, x, y, w, h, tag=None):
    return draw_vynoski(s, sid, v, x, y, w, h, tag=tag)
