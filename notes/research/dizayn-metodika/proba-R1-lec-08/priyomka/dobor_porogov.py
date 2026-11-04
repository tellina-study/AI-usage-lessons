#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dobor_porogov.py — добор показателей пола приёмки, issue #307, проба R1 Лекции 8.

ЗАЧЕМ ЭТОТ ФАЙЛ. `07-PRIYOMKA.md` §1 требует тринадцать числовых показателей на готовой
колоде. Назначенная программа замера (`zamer/zamer.py`) меряет часть из них одной линейкой
по 13 внешним эталонам и 3 колодам курса — но её метод для показателя 1.3 (пол кегля)
нарочно МЯГЧЕ порога владельца (наименьшая ступень, покрывающая ≥1% текста, с исключением
верхних 5%/нижних 8% высоты кадра как колонтитула) — это метод для СРАВНЕНИЯ эталонов между
собой, не метод приёмки одной колоды против порога 15,0 пт на 100% знаков. Показатели
1.8 (контраст), 1.11 (поле/безопасная зона), 1.12 (длина строки) и 1.13 (бюджет знаков на
слот) `zamer.py` не меряет вовсе. Этот файл меряет ровно эти пять показателей на собранном
файле — не переписывая `zamer.py`, а импортируя его модулем там, где нужно его же число для
сравнения (п.1.3), и переиспользуя `deckkit.contrast` как библиотеку для п.1.8 (см. README
проекта, инструкция прямо требует не переписывать измеритель контраста, если он пригоден).

Показатели 1.9 (заполненность обязательных слотов формы) и 1.10 (соответствие формы
утверждению) этот файл НЕ меряет — это сверка кадра с нарядом (`03-RAZNARYADKA.md` +
описание формы в `02-KATALOG-FORM.md`), то есть работа человека по разнарядке, а не измерение
геометрии файла (см. `07-PRIYOMKA.md` §1.9–§1.10: порог там — «сверка», не формула).

ЧТО ИЗМЕРЯЕТСЯ (номера — из `07-PRIYOMKA.md` §1):

  1.3  пол кегля — 15,0 пт на 100% знаков видимого слоя, ПОЛНЫЙ прогон, без фильтра доли и
       без исключения колонтитула. Плюс — для сравнения — тот же файл методом zamer.py
       (наименьшая ступень, покрывающая ≥1% взвешенного объёма текста, с исключением верхних
       5%/нижних 8% высоты кадра).
  1.8  контраст «текст на фактическом фоне» — WCAG AA, 4,5:1 обычный / 3,0:1 крупный.
       Измеряется через `tools/presentation-build/deckkit/contrast.py` (библиотека, не
       переписана — см. `report_contrast()` ниже).
  1.11 поле и безопасная зона — 48 пт слева/справа, 24 пт сверху/снизу от рабочей области,
       для критичных рамок (кегль ≥23 пт или нижняя десятая часть кадра — подвал).
  1.12 длина строки — 37–74 знака, идеал ≈55; строка — ФИЗИЧЕСКАЯ строка из PDF-слоя
       (PyMuPDF `get_text("dict")`), потому что в .pptx физический перенос не хранится.
  1.13 бюджет знаков на слот — `(ширина_пт / 9,0) × число_строк`, округлено вниз; нарушение —
       текст слота больше бюджета более чем вдвое. «Слот» = текстовая рамка .pptx; число строк
       — сопоставленные физические строки PDF (по вхождению центра строки в рамку слота), а
       при отсутствии PDF или совпадения — число непустых абзацев рамки (с явной пометкой).

ЗАПУСК:
    python3 dobor_porogov.py --pptx <путь> [--pdf <путь>]
    python3 dobor_porogov.py                      # по умолчанию ../rendered/proba-R1.{pptx,pdf}

ВЫВОД: человекочитаемый отчёт на русском в stdout + `priyomka/dobor-porogov.json` рядом со
скриптом со всеми сырыми числами.

Этот измеритель НИЧЕГО не чинит в колоде — только меряет и печатает вердикт.
"""

import argparse
import json
import math
import os
import re
import statistics as st
import sys
from collections import Counter, defaultdict

import fitz  # PyMuPDF
import numpy as np
from pptx import Presentation

# --------------------------------------------------------------------------------------
# Пути и импорт соседних измерителей — zamer.py (для сравнения по 1.3) и
# deckkit.contrast (библиотека для 1.8, НЕ переписана).
# --------------------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
_MARKER = os.sep + os.path.join("notes", "research", "dizayn-metodika") + os.sep
_idx = HERE.find(_MARKER)
if _idx == -1:
    raise RuntimeError(
        "не нахожу маркер notes/research/dizayn-metodika в пути скрипта — "
        "запусти его с места, не переносимого вручную"
    )
REPO_ROOT = HERE[:_idx]

ZAMER_DIR = os.path.join(REPO_ROOT, "tools", "metodika-podachi", "zamer")
DECKKIT_PARENT = os.path.join(REPO_ROOT, "tools", "presentation-build")
# До коммита 001c083a3f ("Методика подачи вынесена в канон и подключена к конвейеру") zamer.py
# жил по пути notes/research/dizayn-metodika/zamer/ — этот путь больше не существует. Находка
# #307 (приёмка Лекции 9, issue #317): скрипт падал с ModuleNotFoundError на любой колоде, не
# только на Лекции 9, потому что путь не был обновлён вместе с переносом. Починено здесь.

sys.path.insert(0, ZAMER_DIR)
import zamer  # noqa: E402  — модуль с методом сравнения для 1.3, не переписан

sys.path.insert(0, DECKKIT_PARENT)
try:
    from deckkit import contrast as deckkit_contrast  # noqa: E402
    CONTRAST_LIB_OK = True
    CONTRAST_LIB_NOTE = (
        "deckkit.contrast импортирован как библиотека (функции rows_of/ratio/background/"
        "lum — чистые, зависят только от python-pptx, не от состояния сборки) — переиспользован, "
        "не переписан, по прямому требованию задания"
    )
except Exception as exc:  # pragma: no cover
    CONTRAST_LIB_OK = False
    CONTRAST_LIB_NOTE = f"deckkit.contrast НЕ импортировался ({exc!r}) — мерил контраст сам"
    deckkit_contrast = None

DEFAULT_PPTX = os.path.normpath(os.path.join(HERE, "..", "rendered", "proba-R1.pptx"))
DEFAULT_PDF = os.path.normpath(os.path.join(HERE, "..", "rendered", "proba-R1.pdf"))
OUT_JSON = os.path.join(HERE, "dobor-porogov.json")

# --------------------------------------------------------------------------------------
# Константы метода — пороги ДОСЛОВНО из 07-PRIYOMKA.md §1 (см. цитаты в PRAG_* ниже) и
# 01-YAZYK-KADRA.md (§1.2 поле, §2.1 пол кегля, §2.2 ступень-порог критичного текста,
# §2.3 длина строки).
# --------------------------------------------------------------------------------------

FLOOR_PT = 15.0                  # 1.3 — пол кегля (01-YAZYK-KADRA §2.1, решение владельца)
MARGIN_LR_PT = 48.0              # 1.11 — поле слева/правого (01-YAZYK-KADRA §1.2)
MARGIN_TB_PT = 24.0              # 1.11 — поле сверху/снизу (01-YAZYK-KADRA §1.2)
CRITICAL_FONT_PT = 23.0          # 1.11 — ступень 2 шкалы (заголовок/число), от этого кегля рамка «критичная»
FOOTER_ZONE_FRAC = 0.90          # 1.11 — «нижняя десятая часть кадра» = подвал/подпись-источник
LINE_MIN, LINE_MAX, LINE_IDEAL = 37, 74, 55   # 1.12 (01-YAZYK-KADRA §2.3)
CHAR_WIDTH_PT_AT_15 = 9.0        # 1.13 — ширина кириллического знака на кегле 15 пт (02-KATALOG-FORM §0)
EPS = 1e-6

PRAG_1_3 = "15,0 пт на 100% знаков видимого слоя (включая подписи и подвал)"
PRAG_1_8 = ("WCAG — ≥4,5:1 для обычного текста, ≥3,0:1 для крупного "
            "(кегль ≥18 пт либо ≥14 пт полужирным)")
PRAG_1_11 = ("ничего критичного (заголовок, ключевое число, подпись-источник) не стоит "
             "ближе 48 пт от левого/правого края и 24 пт от верхнего/нижнего")
PRAG_1_12 = "37–74 знака в строке, идеал ≈55 (кириллическая поправка к внешнему канону)"
PRAG_1_13 = ("бюджет = (ширина_пт / 9,0) × число_строк, округлено вниз; нарушение — текст "
             "слота превышает бюджет более чем вдвое")


def emu_to_pt(v):
    return float(v) / 12700.0


def norm_ws(s):
    return re.sub(r"\s+", " ", s or "").strip()


# ========================================================================================
# 1.3 — пол кегля, ПОЛНЫЙ прогон без фильтра доли и без исключения колонтитула
# ========================================================================================

def measure_1_3(pptx_path):
    prs = Presentation(pptx_path)
    total_runs = 0
    no_size_runs = 0
    all_rows = []       # все прогоны с известным кеглем, char-weighted для сравнения
    below_rows = []
    all_sizes_weighted = Counter()   # {size: n_chars} — ПОЛНЫЙ пул, без исключений, для char-weighted доли

    for si, slide in enumerate(prs.slides, start=1):
        for shp in zamer.walk_shapes(slide.shapes):
            if not getattr(shp, "has_text_frame", False):
                continue
            for para in shp.text_frame.paragraphs:
                for run in para.runs:
                    text = (run.text or "").strip()
                    if not text:
                        continue
                    total_runs += 1
                    size_pt = None
                    try:
                        if run.font.size is not None:
                            size_pt = round(run.font.size.pt, 2)
                    except Exception:
                        size_pt = None
                    if size_pt is None:
                        no_size_runs += 1
                        continue
                    all_sizes_weighted[size_pt] += len(text)
                    rec = {"slide": si, "shape": shp.name, "size_pt": size_pt, "text": text[:40]}
                    all_rows.append(rec)
                    if size_pt < FLOOR_PT - EPS:
                        below_rows.append(rec)

    measured_runs = total_runs - no_size_runs
    n_below = len(below_rows)
    share_below_runs = (n_below / measured_runs) if measured_runs else None
    affected_slides = sorted({r["slide"] for r in below_rows})
    worst10 = sorted(below_rows, key=lambda r: r["size_pt"])[:10]

    total_chars = sum(all_sizes_weighted.values()) or 1
    chars_below = sum(w for s, w in all_sizes_weighted.items() if s < FLOOR_PT - EPS)
    share_below_chars_my_method = chars_below / total_chars

    # --- сравнение с методом zamer.py на ТОМ ЖЕ файле (та же линейка показателя 1.3) ---
    frames = zamer.parse_pptx(pptx_path, log=lambda *a, **k: None)
    zamer_pool = Counter()
    for fr in frames:
        zamer_pool.update(fr.body_font_sizes_weighted)
    zamer_total = sum(zamer_pool.values()) or 1
    zamer_steps = sorted(s for s, w in zamer_pool.items() if w / zamer_total >= zamer.MIN_SIZE_SHARE)
    zamer_min_filtered = zamer_steps[0] if zamer_steps else None
    zamer_raw_min = min(zamer_pool) if zamer_pool else None
    zamer_chars_below = sum(w for s, w in zamer_pool.items() if s < FLOOR_PT - EPS)
    zamer_share_below_chars = zamer_chars_below / zamer_total

    verdict_ok = (n_below == 0)

    return {
        "porog": PRAG_1_3,
        "moy_metod": {
            "opisanie": "каждый текстовый прогон (run) всей колоды, без фильтра доли и без "
                         "исключения верхней/нижней зоны кадра — полный прогон",
            "vsego_progonov": total_runs,
            "progonov_bez_zadannogo_keglya": no_size_runs,
            "izmereno_progonov": measured_runs,
            "nizhe_pola_progonov": n_below,
            "dolya_nizhe_pola_po_progonam": share_below_runs,
            "dolya_nizhe_pola_po_simvolam": share_below_chars_my_method,
            "zadeto_kadrov": len(affected_slides),
            "nomera_kadrov": affected_slides,
            "desyat_khudshikh": worst10,
        },
        "metod_zamer_py_na_etom_zhe_fayle": {
            "opisanie": "zamer.summarize_pdf_or_pptx: наименьшая ступень, покрывающая ≥1% "
                         "взвешенного по символам объёма текста (MIN_SIZE_SHARE), пул уже "
                         "очищен от верхних 5%/нижних 8% высоты кадра и от span'ов-номеров "
                         "страниц (is_footer_zone)",
            "minimalnyy_kegl_s_filtrom_1_protsenta": zamer_min_filtered,
            "minimalnyy_kegl_bez_filtra_1_protsenta_no_s_iskl_kolontitula": zamer_raw_min,
            "dolya_nizhe_pola_po_simvolam_v_etom_pule": zamer_share_below_chars,
            "stupeni_s_filtrom": zamer_steps,
        },
        "raznitsa_metodov_chislom": {
            "dolya_nizhe_15pt_moy_metod_po_simvolam": round(share_below_chars_my_method, 4),
            "dolya_nizhe_15pt_metod_zamer_po_simvolam": round(zamer_share_below_chars, 4),
            "razlichie_v_p_p": round(
                (share_below_chars_my_method - zamer_share_below_chars) * 100, 2
            ),
            "kommentariy": "обе доли посчитаны по одной единице (доля символов), различие — "
                            "ровно то, что даёт исключение zamer.py верхних 5%/нижних 8% "
                            "высоты кадра и фильтр ступеней ≥1% веса; на очень маленьком "
                            "тестовом файле (2 кадра) различие может быть нулевым или "
                            "минимальным — смысл числа проявляется на полной колоде",
        },
        "fakt": f"{n_below} прогонов из {measured_runs} измеренных (доля "
                f"{share_below_runs:.4f} по прогонам, {share_below_chars_my_method:.4f} по "
                f"символам) ниже 15,0 пт, задето {len(affected_slides)} кадр(ов)" if measured_runs
                else "нет измеримых прогонов",
        "verdikt": "проходит" if verdict_ok else "НЕ ПРОХОДИТ",
    }


# ========================================================================================
# 1.8 — контраст «текст на фактическом фоне» — через deckkit.contrast как библиотеку
# ========================================================================================

def _contrast_via_deckkit(pptx_path):
    prs = Presentation(pptx_path)
    rows = deckkit_contrast.rows_of(prs)
    measured = [r for r in rows if r["ok"] is not None]
    unmeasured = [r for r in rows if r["ok"] is None]
    bad = [r for r in measured if r["ok"] is False]
    worst10 = sorted(bad, key=lambda r: r["ratio"])[:10]
    return rows, measured, unmeasured, bad, worst10


def _contrast_fallback(pptx_path):
    """Самостоятельный замер того же порога WCAG, на случай если deckkit.contrast
    непригоден для импорта (например, переехал/сломался) — тот же метод: формула
    относительной яркости §3.1, фон — собственная заливка фигуры либо белый по
    умолчанию (без z-порядкового поиска под фигурой — это единственное отличие
    от deckkit.contrast, см. report)."""
    def srgb_to_linear(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    def lum(hexcolor):
        h = str(hexcolor).lstrip("#")
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return (0.2126 * srgb_to_linear(r) + 0.7152 * srgb_to_linear(g)
                + 0.0722 * srgb_to_linear(b))

    def ratio(fg, bg):
        l1, l2 = lum(fg), lum(bg)
        hi, lo = max(l1, l2), min(l1, l2)
        return (hi + 0.05) / (lo + 0.05)

    prs = Presentation(pptx_path)
    rows = []
    for si, slide in enumerate(prs.slides, start=1):
        shapes = list(slide.shapes)
        for i, shp in enumerate(shapes):
            if not getattr(shp, "has_text_frame", False):
                continue
            own_fill = None
            try:
                if shp.fill.type is not None and int(shp.fill.type) == 1:
                    rgb = shp.fill.fore_color.rgb
                    own_fill = str(rgb)
            except Exception:
                own_fill = None
            bg = own_fill or "FFFFFF"
            for para in shp.text_frame.paragraphs:
                for run in para.runs:
                    if not (run.text or "").strip():
                        continue
                    fg = None
                    try:
                        if run.font.color.type is not None:
                            fg = str(run.font.color.rgb)
                    except Exception:
                        fg = None
                    size = run.font.size.pt if run.font.size else None
                    bold = bool(run.font.bold)
                    row = {"page": si, "shape": shp.name, "text": run.text.strip()[:40],
                           "size": size, "bold": bold, "fg": fg, "bg": bg,
                           "ratio": None, "thr": None, "ok": None}
                    if fg and bg and size is not None:
                        large = size >= (14.0 if bold else 18.0) - EPS
                        thr = 3.0 if large else 4.5
                        r = ratio(fg, bg)
                        row["ratio"], row["thr"], row["ok"] = r, thr, (r >= thr - EPS)
                    rows.append(row)
    measured = [r for r in rows if r["ok"] is not None]
    unmeasured = [r for r in rows if r["ok"] is None]
    bad = [r for r in measured if r["ok"] is False]
    worst10 = sorted(bad, key=lambda r: r["ratio"])[:10]
    return rows, measured, unmeasured, bad, worst10


def measure_1_8(pptx_path):
    if CONTRAST_LIB_OK:
        rows, measured, unmeasured, bad, worst10 = _contrast_via_deckkit(pptx_path)
        metod_note = CONTRAST_LIB_NOTE
    else:
        rows, measured, unmeasured, bad, worst10 = _contrast_fallback(pptx_path)
        metod_note = CONTRAST_LIB_NOTE

    worst_out = []
    for r in worst10:
        worst_out.append({
            "kadr": r.get("page"), "figura": r.get("shape"), "text": r.get("text"),
            "kegl": r.get("size"), "zhirnyy": r.get("bold"), "tsvet": r.get("fg"),
            "fon": r.get("bg"), "kontrast": round(r["ratio"], 2), "porog": r["thr"],
        })

    verdict_ok = (len(bad) == 0)
    return {
        "porog": PRAG_1_8,
        "kak_merili": metod_note,
        "vsego_par_izmereno": len(measured),
        "ne_izmereno_tsvet_ili_fon_ne_nazvany": len(unmeasured),
        "nizhe_poroga": len(bad),
        "desyat_khudshikh": worst_out,
        "fakt": f"{len(bad)} пар из {len(measured)} измеренных ниже порога WCAG",
        "verdikt": "проходит" if verdict_ok else "НЕ ПРОХОДИТ",
    }


# ========================================================================================
# 1.11 — поле и безопасная зона
# ========================================================================================

def measure_1_11(pptx_path):
    prs = Presentation(pptx_path)
    sw, sh = emu_to_pt(prs.slide_width), emu_to_pt(prs.slide_height)
    footer_y0 = sh * FOOTER_ZONE_FRAC

    rows = []
    for si, slide in enumerate(prs.slides, start=1):
        for shp in zamer.walk_shapes(slide.shapes):
            if not getattr(shp, "has_text_frame", False):
                continue
            text = norm_ws(shp.text_frame.text)
            if not text:
                continue
            try:
                left, top = emu_to_pt(shp.left), emu_to_pt(shp.top)
                width, height = emu_to_pt(shp.width), emu_to_pt(shp.height)
            except (TypeError, ValueError):
                continue
            right, bottom = left + width, top + height
            max_size = 0.0
            for para in shp.text_frame.paragraphs:
                for run in para.runs:
                    if (run.text or "").strip() and run.font.size is not None:
                        try:
                            max_size = max(max_size, run.font.size.pt)
                        except Exception:
                            pass
            is_footer_pos = top >= footer_y0 - EPS
            is_critical = (max_size >= CRITICAL_FONT_PT - EPS) or is_footer_pos

            dist_left, dist_right = left, sw - right
            dist_top, dist_bottom = top, sh - bottom
            violations = []
            if dist_left < MARGIN_LR_PT - EPS:
                violations.append(("слева", round(dist_left, 1)))
            if dist_right < MARGIN_LR_PT - EPS:
                violations.append(("справа", round(dist_right, 1)))
            if dist_top < MARGIN_TB_PT - EPS:
                violations.append(("сверху", round(dist_top, 1)))
            if dist_bottom < MARGIN_TB_PT - EPS:
                violations.append(("снизу", round(dist_bottom, 1)))

            rows.append({
                "slide": si, "shape": shp.name, "text": text[:40],
                "max_size_pt": round(max_size, 1), "footer_zone": is_footer_pos,
                "critical": is_critical,
                "dist_left": round(dist_left, 1), "dist_right": round(dist_right, 1),
                "dist_top": round(dist_top, 1), "dist_bottom": round(dist_bottom, 1),
                "violations": violations,
            })

    critical_viol = [r for r in rows if r["critical"] and r["violations"]]
    all_viol = [r for r in rows if r["violations"]]
    verdict_ok = (len(critical_viol) == 0)

    return {
        "porog": PRAG_1_11,
        "kak_merili": f"рабочая область 864×492 пт на холсте {sw:.1f}×{sh:.1f} пт — поле "
                      f"{MARGIN_LR_PT:.0f} пт слева/справа, {MARGIN_TB_PT:.0f} пт сверху/"
                      f"снизу; критичная рамка — кегль ≥{CRITICAL_FONT_PT:.0f} пт (заголовок/"
                      f"число) либо верх рамки в нижних {int((1-FOOTER_ZONE_FRAC)*100)}% высоты "
                      f"кадра (подвал/подпись-источник)",
        "vsego_tekstovykh_ramok": len(rows),
        "narusheniy_vsego_ramok": len(all_viol),
        "narusheniy_kriticheskikh_ramok": len(critical_viol),
        "narushiteli_kriticheskie": critical_viol,
        "fakt": f"{len(critical_viol)} критичных рамок из {len(rows)} нарушают поле/безопасную "
                f"зону ({len(all_viol)} нарушений среди всех текстовых рамок, не только "
                f"критичных)",
        "verdikt": "проходит" if verdict_ok else "НЕ ПРОХОДИТ",
    }


# ========================================================================================
# 1.12 / 1.13 — физические строки PDF (общая извлекающая функция) + длина строки + бюджет
# ========================================================================================

def iter_pdf_lines(pdf_path):
    """Физические строки текстового слоя PDF — PyMuPDF get_text("dict") уже отдаёт строки
    после переноса (в отличие от .pptx, где переноса в файле просто нет)."""
    doc = fitz.open(pdf_path)
    out = []
    for pno, page in enumerate(doc, start=1):
        d = page.get_text("dict")
        for block in d.get("blocks", []):
            if block.get("type", 0) != 0:   # 0 — текстовый блок, 1 — изображение
                continue
            for line in block.get("lines", []):
                raw = "".join(sp.get("text", "") for sp in line.get("spans", []))
                stripped = norm_ws(raw)
                if not stripped:
                    continue
                bbox = line.get("bbox", (0, 0, 0, 0))
                out.append({"page": pno, "text": stripped, "n_chars": len(stripped), "bbox": bbox})
    doc.close()
    return out


def measure_1_12(pdf_path):
    lines = iter_pdf_lines(pdf_path)
    if not lines:
        return {
            "porog": PRAG_1_12, "kak_merili": "физическая строка из PDF-слоя (PyMuPDF "
            "get_text('dict'), уже после переноса) — выбран .pdf, а не .pptx, потому что "
            ".pptx не хранит точку физического переноса строки внутри абзаца",
            "fakt": "строк текста в PDF-слое не найдено", "verdikt": "НЕ ПРОХОДИТ",
        }
    lengths = [l["n_chars"] for l in lines]
    median = st.median(lengths)
    p10 = float(np.percentile(lengths, 10))
    p90 = float(np.percentile(lengths, 90))
    out_of_band = [l for l in lines if not (LINE_MIN <= l["n_chars"] <= LINE_MAX)]
    share_out = len(out_of_band) / len(lines)

    def deviation(l):
        n = l["n_chars"]
        return (LINE_MIN - n) if n < LINE_MIN else (n - LINE_MAX)

    worst10 = sorted(out_of_band, key=lambda l: -deviation(l))[:10]
    worst_out = [{"kadr": l["page"], "znakov": l["n_chars"], "text": l["text"][:40]} for l in worst10]

    verdict_ok = (len(out_of_band) == 0)
    return {
        "porog": PRAG_1_12,
        "kak_merili": "физическая строка из PDF-слоя (PyMuPDF get_text('dict'), уже после "
                      "переноса) — выбран .pdf, а не .pptx, потому что .pptx не хранит точку "
                      "физического переноса строки внутри абзаца; счёт знаков — len() "
                      "строки после свёртки пробелов (норм. пробел), без учёта регистра",
        "vsego_strok": len(lines),
        "mediana_znakov": median,
        "p10_znakov": round(p10, 1),
        "p90_znakov": round(p90, 1),
        "idealnaya_dlina": LINE_IDEAL,
        "strok_vne_polosy": len(out_of_band),
        "dolya_vne_polosy": round(share_out, 4),
        "desyat_khudshikh": worst_out,
        "fakt": f"{len(out_of_band)} строк из {len(lines)} вне полосы {LINE_MIN}–{LINE_MAX} "
                f"знаков (доля {share_out:.4f}); медиана {median:.0f}, p10={p10:.0f}, "
                f"p90={p90:.0f}",
        "verdikt": "проходит" if verdict_ok else "НЕ ПРОХОДИТ",
    }


def _match_pdf_lines_to_shape(pdf_lines, rect):
    l, t, r, b = rect
    out = []
    for line in pdf_lines:
        bx0, by0, bx1, by1 = line["bbox"]
        cx, cy = (bx0 + bx1) / 2.0, (by0 + by1) / 2.0
        if l - 1.0 <= cx <= r + 1.0 and t - 1.0 <= cy <= b + 1.0:
            out.append(line)
    return out


def measure_1_13(pptx_path, pdf_path=None):
    prs = Presentation(pptx_path)
    pdf_lines_by_page = defaultdict(list)
    pdf_available = bool(pdf_path and os.path.exists(pdf_path))
    if pdf_available:
        for l in iter_pdf_lines(pdf_path):
            pdf_lines_by_page[l["page"]].append(l)

    rows = []
    for si, slide in enumerate(prs.slides, start=1):
        for shp in zamer.walk_shapes(slide.shapes):
            if not getattr(shp, "has_text_frame", False):
                continue
            raw_text = shp.text_frame.text or ""
            n_chars = len(norm_ws(raw_text))
            if n_chars == 0:
                continue
            try:
                left, top = emu_to_pt(shp.left), emu_to_pt(shp.top)
                width, height = emu_to_pt(shp.width), emu_to_pt(shp.height)
            except (TypeError, ValueError):
                continue
            rect = (left, top, left + width, top + height)

            matched = (_match_pdf_lines_to_shape(pdf_lines_by_page.get(si, []), rect)
                       if pdf_available else [])
            if matched:
                n_lines = len(matched)
                n_lines_src = "физические строки PDF, сопоставленные по вхождению центра в рамку"
            else:
                n_lines = sum(1 for p in shp.text_frame.paragraphs if norm_ws(p.text))
                n_lines = max(n_lines, 1)
                n_lines_src = ("оценка по числу непустых абзацев рамки — PDF не задан/не "
                                "сопоставлен ни одной строкой")

            budget = math.floor((width / CHAR_WIDTH_PT_AT_15) * n_lines)
            over_2x = n_chars > 2 * budget if budget > 0 else (n_chars > 0)
            rows.append({
                "slide": si, "shape": shp.name, "width_pt": round(width, 1),
                "n_lines": n_lines, "n_lines_src": n_lines_src, "n_chars": n_chars,
                "budget": budget, "over_2x": over_2x,
                "ratio_to_budget": round(n_chars / budget, 2) if budget > 0 else None,
                "text_head": norm_ws(raw_text)[:40],
            })

    violations = [r for r in rows if r["over_2x"]]
    verdict_ok = (len(violations) == 0)
    pdf_note = ("число строк сопоставлено по физическим строкам PDF там, где совпадение "
                "нашлось" if pdf_available else
                "PDF не передан (--pdf) — число строк оценено по числу непустых абзацев "
                "рамки, это явно помечено в каждой строке результата (n_lines_src)")

    return {
        "porog": PRAG_1_13,
        "kak_merili": f"слот = текстовая рамка .pptx; ширина — геометрия фигуры в пт; число "
                      f"строк — {pdf_note}; знаков — длина текста рамки после свёртки "
                      f"пробелов; бюджет = floor((ширина/{CHAR_WIDTH_PT_AT_15:.1f})×строк)",
        "vsego_ramok_s_tekstom": len(rows),
        "narusheniy_vdvoe": len(violations),
        "narushiteli": violations,
        "fakt": f"{len(violations)} рамок из {len(rows)} превышают пересчитанный бюджет "
                f"более чем вдвое",
        "verdikt": "проходит" if verdict_ok else "НЕ ПРОХОДИТ",
    }


# ========================================================================================
# Отчёт
# ========================================================================================

def fmt_pct(x):
    return "—" if x is None else f"{x*100:.2f}%"


def print_section(num, title, data):
    lines = []
    lines.append("")
    lines.append(f"{'='*78}")
    lines.append(f"Показатель {num} — {title}")
    lines.append(f"{'='*78}")
    lines.append(f"Порог (дословно, 07-PRIYOMKA.md §1): {data['porog']}")
    if "kak_merili" in data:
        lines.append(f"Как мерил: {data['kak_merili']}")
    lines.append(f"Факт: {data['fakt']}")
    lines.append(f"ВЕРДИКТ: {data['verdikt']}")
    return "\n".join(lines)


def build_report(res):
    out = []
    out.append("ДОБОР ПОРОГОВ ПРИЁМКИ — показатели 1.3 (полный пол), 1.8, 1.11, 1.12, 1.13")
    out.append("issue #307, проба R1 Лекции 8 — tools/metodika-podachi/priyomka/07-PRIYOMKA.md §1")
    out.append(f"Файл .pptx: {res['_meta']['pptx']}")
    out.append(f"Файл .pdf:  {res['_meta']['pdf'] or '(не передан)'}")

    # 1.3
    d = res["1.3"]
    out.append(print_section("1.3", "пол кегля — ПОЛНЫЙ прогон, без фильтра и исключений", d))
    m = d["moy_metod"]
    out.append(f"  Всего прогонов: {m['vsego_progonov']} "
               f"(без заданного кегля: {m['progonov_bez_zadannogo_keglya']}, "
               f"измерено: {m['izmereno_progonov']})")
    out.append(f"  Ниже 15,0 пт: {m['nizhe_pola_progonov']} прогонов "
               f"(доля по прогонам {fmt_pct(m['dolya_nizhe_pola_po_progonam'])}, "
               f"по символам {fmt_pct(m['dolya_nizhe_pola_po_simvolam'])})")
    out.append(f"  Задето кадров: {m['zadeto_kadrov']} — номера: {m['nomera_kadrov']}")
    out.append("  Десять худших (кадр · кегль · текст):")
    for r in m["desyat_khudshikh"]:
        out.append(f"    кадр {r['slide']:>2} · {r['size_pt']:>5.1f} пт · «{r['text']}»")
    z = d["metod_zamer_py_na_etom_zhe_fayle"]
    out.append("  Для сравнения — метод zamer.py на том же файле:")
    out.append(f"    минимальный кегль с фильтром ≥1% веса (его «пол»): {z['minimalnyy_kegl_s_filtrom_1_protsenta']}")
    out.append(f"    минимальный кегль без этого фильтра (но с иск. колонтитула): "
               f"{z['minimalnyy_kegl_bez_filtra_1_protsenta_no_s_iskl_kolontitula']}")
    out.append(f"    доля символов ниже 15 пт в этом (отфильтрованном) пуле: "
               f"{fmt_pct(z['dolya_nizhe_pola_po_simvolam_v_etom_pule'])}")
    rz = d["raznitsa_metodov_chislom"]
    out.append(f"  РАЗНИЦА МЕТОДОВ ЧИСЛОМ (доля символов ниже 15 пт): мой метод "
               f"{fmt_pct(rz['dolya_nizhe_15pt_moy_metod_po_simvolam'])} против "
               f"метода zamer.py {fmt_pct(rz['dolya_nizhe_15pt_metod_zamer_po_simvolam'])} "
               f"— различие {rz['razlichie_v_p_p']:+.2f} п.п.")

    # 1.8
    d = res["1.8"]
    out.append(print_section("1.8", "контраст «текст на фактическом фоне» (WCAG)", d))
    out.append(f"  Пар измерено: {d['vsego_par_izmereno']}, не измерено (цвет/фон не названы): "
               f"{d['ne_izmereno_tsvet_ili_fon_ne_nazvany']}, ниже порога: {d['nizhe_poroga']}")
    out.append("  Десять худших (кадр · фигура · текст · кегль · цвет на фоне · контраст/порог):")
    for r in d["desyat_khudshikh"]:
        out.append(f"    кадр {r['kadr']:>2} · {r['figura']:<12} · «{r['text']}» · "
                   f"{r['kegl']} пт{'ж' if r['zhirnyy'] else ''} · {r['tsvet']} на {r['fon']} · "
                   f"{r['kontrast']:.2f}:1 (порог {r['porog']:.1f})")

    # 1.11
    d = res["1.11"]
    out.append(print_section("1.11", "поле и безопасная зона", d))
    out.append(f"  Текстовых рамок всего: {d['vsego_tekstovykh_ramok']}; нарушений среди всех: "
               f"{d['narusheniy_vsego_ramok']}; среди КРИТИЧНЫХ: {d['narusheniy_kriticheskikh_ramok']}")
    for r in d["narushiteli_kriticheskie"]:
        v = ", ".join(f"{side} {pt:.1f} пт" for side, pt in r["violations"])
        out.append(f"    кадр {r['slide']:>2} · {r['shape']:<12} · «{r['text']}» · {v}")

    # 1.12
    d = res["1.12"]
    out.append(print_section("1.12", "длина строки (физическая, из PDF)", d))
    if "vsego_strok" in d:
        out.append(f"  Строк всего: {d['vsego_strok']}; медиана {d['mediana_znakov']:.0f}, "
                   f"p10 {d['p10_znakov']:.0f}, p90 {d['p90_znakov']:.0f} знаков")
        out.append(f"  Вне полосы {LINE_MIN}–{LINE_MAX}: {d['strok_vne_polosy']} "
                   f"({fmt_pct(d['dolya_vne_polosy'])})")
        out.append("  Десять худших (кадр · знаков · текст):")
        for r in d["desyat_khudshikh"]:
            out.append(f"    кадр {r['kadr']:>2} · {r['znakov']:>3} знаков · «{r['text']}»")

    # 1.13
    d = res["1.13"]
    out.append(print_section("1.13", "бюджет знаков на слот", d))
    out.append(f"  Рамок с текстом: {d['vsego_ramok_s_tekstom']}; превышают бюджет более чем "
               f"вдвое: {d['narusheniy_vdvoe']}")
    for r in d["narushiteli"]:
        out.append(f"    кадр {r['slide']:>2} · {r['shape']:<12} · ширина {r['width_pt']:.0f} "
                   f"пт · строк {r['n_lines']} ({r['n_lines_src']}) · знаков {r['n_chars']} · "
                   f"бюджет {r['budget']} · «{r['text_head']}»")

    out.append("")
    out.append("=" * 78)
    out.append("СВОДНЫЙ ВЕРДИКТ ПО ПЯТИ ДОБОРНЫМ ПОКАЗАТЕЛЯМ:")
    for num in ("1.3", "1.8", "1.11", "1.12", "1.13"):
        out.append(f"  {num}: {res[num]['verdikt']}")
    out.append("=" * 78)
    out.append(f"Контраст (1.8) мерился: {CONTRAST_LIB_NOTE}")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pptx", default=DEFAULT_PPTX, help="путь к собранному .pptx")
    ap.add_argument("--pdf", default=DEFAULT_PDF, help="путь к собранному .pdf (для 1.12/1.13)")
    args = ap.parse_args()

    if not os.path.exists(args.pptx):
        print(f"ОШИБКА: .pptx не найден: {args.pptx}", file=sys.stderr)
        sys.exit(1)
    pdf_path = args.pdf if (args.pdf and os.path.exists(args.pdf)) else None
    if args.pdf and not pdf_path:
        print(f"ПРЕДУПРЕЖДЕНИЕ: .pdf не найден ({args.pdf}) — 1.12 будет пропущен, "
              f"1.13 будет измерен с оценкой числа строк по абзацам", file=sys.stderr)

    res = {"_meta": {"pptx": args.pptx, "pdf": pdf_path}}
    res["1.3"] = measure_1_3(args.pptx)
    res["1.8"] = measure_1_8(args.pptx)
    res["1.11"] = measure_1_11(args.pptx)
    res["1.13"] = measure_1_13(args.pptx, pdf_path)
    if pdf_path:
        res["1.12"] = measure_1_12(pdf_path)
    else:
        res["1.12"] = {"porog": PRAG_1_12, "fakt": "PDF не передан — показатель не измерен",
                        "verdikt": "НЕ ИЗМЕРЕН"}

    report = build_report(res)
    print(report)

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
    print(f"\n[json] {OUT_JSON}")


if __name__ == "__main__":
    main()
