#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`deck.yaml` Лекции 8 v5 — ВЫГРУЖАЕТСЯ из файлов кадров, руками не пишется.

Манифест деки — ПРОИЗВОДНОЕ от `slides/*.md`, и правится только здесь.
Руками правленный манифест расходится с файлами кадров молча: ничего не
ломается, сборка его не читает (`build_lec08_v5.py` берёт фронтматтер
напрямую и этот файл не импортирует ни строкой), — а потом по нему считают
минуты и состав.

Чем отличается от генератора v4. Там `chapter_ref` назначался ЧЕЛОВЕКОМ,
чтением главы, и жил в самом генераторе таблицей на 71 строку. Здесь такой
таблицы нет и выдумывать её нельзя: у v5 адрес в главе уже стоит в самом
кадре, полем `source`, и переносится сюда дословно. Поле, которого в
кадрах нет, манифест не изобретает — он его не показывает.

    python3 make_deck_yaml_v5.py
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))
import yaml  # noqa: E402
from deckkit import slidefile  # noqa: E402

SLIDES = HERE.parent / "slides"
PART_LIMIT = 560          # предел 600 строк на файл (CLAUDE.md), с запасом

TYPE_MEANING = {
    "hero_cover": "обложка с обязательной иллюстрацией",
    "hero_closing": "закрывающий кадр с обязательной иллюстрацией",
    "section_divider": "дивайдер раздела",
    "analitika": "разбор с числами: плашки, столбцы, счёт",
    "assertion_visual": "утверждение, предъявленное формой",
    "comparison": "два столбца «что получается / что не получается»",
    "schema_matrix": "сетка: строки против колонок",
    "schema_timeline": "хронология",
    "schema_pipeline": "порядок работы",
    "schema_architecture": "устройство: части и связи",
    "schema_layered": "слои, вложенные друг в друга",
    "live_demo": "живой показ",
}


def q(s):
    """YAML-строка в двойных кавычках, без сюрпризов на кириллице."""
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def chislo(v, default=0.0):
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


def media_status(d):
    if str(d.get("media") or "").strip():
        return "wired"
    if str(d.get("media_needed") or "").strip():
        return "needs_media"
    return "no_decision"


def read_all():
    out = []
    for f in slidefile.slide_files(SLIDES):
        m = re.match(r"^---\n(.*?)\n---\n", f.read_text(encoding="utf-8"),
                     re.S)
        if not m:
            continue
        d = yaml.safe_load(m.group(1)) or {}
        d["_file"] = f.name
        out.append(d)
    return out


def main():
    sl = read_all()
    n = len(sl)
    # разделы в порядке первого появления, кадры и минуты сложены по файлам
    sections, order = {}, []
    for d in sl:
        s = str(d.get("section") or "—")
        if s not in sections:
            sections[s] = {"slides": 0, "min": 0.0, "ids": []}
            order.append(s)
        sections[s]["slides"] += 1
        sections[s]["min"] += chislo(d.get("timing_min"))
        sections[s]["ids"].append(str(d.get("id")))
    types = {}
    for d in sl:
        types[str(d.get("type"))] = types.get(str(d.get("type")), 0) + 1
    total_min = sum(chislo(d.get("timing_min")) for d in sl)
    bucket_min = sum(chislo(d.get("timing_min")) for d in sl
                     if d.get("in_bucket") is True)
    ms = {}
    for d in sl:
        k = media_status(d)
        ms[k] = ms.get(k, 0) + 1
    st = {}
    for d in sl:
        k = str(d.get("status") or "—")
        st[k] = st.get(k, 0) + 1

    L = []
    w = L.append
    w("# library/lectures/lec-08/rework-v5/deck/deck.yaml  --  часть {i} из {np}")
    w("#")
    w("# Служебная опись деки Лекции 8 v5 (issue #301, ветка")
    w("# issue-301-lec-08-rebuild). ВЫГРУЖЕНА программой")
    w("# `make_deck_yaml_v5.py` из `slides/*.md` — руками не правится, при")
    w("# любой правке фронтматтера перезапускается.")
    w("#")
    w("# ЧЕМ ЭТО НЕ ЯВЛЯЕТСЯ — входом сборки. `deck/build_lec08_v5.py`")
    w("# читает фронтматтер файлов кадров напрямую и этот файл не")
    w("# импортирует. Два описания одного состава способны разойтись, ничего")
    w("# не сломав, если одно читает сборка, а другое — только человек;")
    w("# поэтому здесь каждое поле выгружено, а не записано.")
    w("#")
    w("# Тайминг и методические поля живут ЗДЕСЬ и во фронтматтере — на")
    w("# видимом слое кадра они запрещены (CLAUDE.md § «No Timing / No")
    w("# Methodology in Slides»).")
    w("#")
    w(f"# СОСТАВ, посчитанный с диска: {n} кадров.")
    w("")
    w("deck:")
    w("  lecture_number: 8")
    w("  issue: 301")
    w("  version: v5")
    w("  language: ru")
    w("  status: draft")
    w(f"  total_slides: {n}")
    w(f"  sum_timing_min: {total_min:.2f}"
      "           # сложено по `timing_min` файлов кадров")
    w("  builder: deck/build_lec08_v5.py"
      "        # относительно library/lectures/lec-08/rework-v5/")
    w("  generator: deck/make_deck_yaml_v5.py")
    w("  rendered: rendered/lec-08-v5.pptx")
    w("")
    w("palette:                         # Ocean Gradient, зафиксирована курсом")
    for k, v in (("primary_deep", "#21295C"), ("primary_mid", "#065A82"),
                 ("primary_light", "#1C7293"), ("teal", "#028090"),
                 ("gold", "#F0AB00"), ("surface", "#F4F7FA"),
                 ("background", "#FFFFFF")):
        w(f"  {k}: {q(v)}")
    w("")
    w("slide_types:                     # значения поля `type`, с числом кадров")
    for k in sorted(types, key=lambda x: (-types[x], x)):
        w(f"  {k + ':':22} {{ count: {types[k]:3}, meaning: "
          f"{q(TYPE_MEANING.get(k, '—'))} }}")
    w("")
    w("sections:                        # разделы показа, сложено по файлам кадров")
    for s in order:
        d = sections[s]
        w(f"  - {{ name: {q(s)},")
        w(f"      slides: {d['slides']}, timing_min: {d['min']:.2f}, "
          f"range: [{d['ids'][0]}, {d['ids'][-1]}] }}")
    w("")
    w("slides:")
    w("")
    cur = None
    for d in sl:
        s = str(d.get("section") or "—")
        if s != cur:
            cur = s
            w(f"  # ─── {s} · {sections[s]['slides']} кадров · "
              f"{sections[s]['min']:.2f} мин ───")
        w(f"  - id: {d.get('id')}")
        w(f"    file: slides/{d['_file']}")
        w(f"    type: {d.get('type')}")
        w(f"    title: {q(d.get('title') or '')}")
        src = str(d.get("source") or "").strip()
        if src:
            w(f"    source: {q(src)}")
        w(f"    timing_min: {chislo(d.get('timing_min')):.2f}")
        marks = [f"in_bucket: {str(bool(d.get('in_bucket'))).lower()}"]
        if "vfy" in d:
            marks.append(f"vfy: {str(bool(d.get('vfy'))).lower()}")
        marks.append(f"status: {q(d.get('status') or '—')}")
        marks.append(f"media_status: {media_status(d)}")
        w(f"    marks: {{ {', '.join(marks)} }}")
        if isinstance(d.get("matrix"), dict):
            mx = d["matrix"]
            if mx.get("state") or mx.get("columns_to_come"):
                w(f"    karta_vechera: {{ columns: "
                  f"{len(mx.get('columns') or [])}, to_come: "
                  f"{len(mx.get('columns_to_come') or [])} }}")
    w("")
    w("totals:")
    w(f"  slides: {n}")
    w(f"  timing_min: {total_min:.2f}")
    w(f"  timing_missing: {sum(1 for d in sl if not d.get('timing_min') and chislo(d.get('timing_min')) == 0.0 and d.get('type') != 'section_divider')}")
    w(f"  strict_in_min: {bucket_min:.2f}"
      "            # кадры с `in_bucket: true`, сложено по минутам")
    w(f"  strict_in_share: {q(f'{100 * bucket_min / total_min:.1f}%')}"
      "       # порог курса 30%; partial → out")
    w(f"  vfy_slides: {sum(1 for d in sl if d.get('vfy') is True)}")
    w("  by_status:")
    for k in sorted(st):
        w(f"    {q(k)}: {st[k]}")
    w("  media:")
    for k in ("wired", "needs_media", "no_decision"):
        w(f"    {k}: {ms.get(k, 0)}")
    w(f"  karta_vechera_predyavleniy: "
      f"{sum(1 for d in sl if isinstance(d.get('matrix'), dict) and (d['matrix'].get('state') or d['matrix'].get('columns_to_come')))}")

    # разрезать по пределу строк
    parts, buf = [], []
    for line in L:
        buf.append(line)
        if len(buf) >= PART_LIMIT and line.startswith("  - id: "):
            buf.pop()
            parts.append(buf)
            buf = [line]
    parts.append(buf)
    np_ = len(parts)
    for i, body in enumerate(parts, 1):
        fn = "deck.yaml" if i == 1 else f"deck-part{i}.yaml"
        body = [ln.replace("{i}", str(i)).replace("{np}", str(np_))
                for ln in body]
        if i > 1:
            body = [f"# library/lectures/lec-08/rework-v5/deck/{fn}"
                    f"  --  часть {i} из {np_}",
                    "# Продолжение `deck.yaml`. Выгружено"
                    " `make_deck_yaml_v5.py`, руками не правится.",
                    "", "slides:", ""] + body
        (HERE / fn).write_text("\n".join(body) + "\n", encoding="utf-8")
        print(f"{fn}: {len(body)} строк")
    print(f"кадров {n} · минут {total_min:.2f} · частей {np_}")


if __name__ == "__main__":
    main()
