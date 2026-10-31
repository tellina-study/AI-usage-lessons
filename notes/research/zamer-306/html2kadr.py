#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Переводчик закрытого словаря HTML (`slovar-tegov.md`) в поля фронтматтера
кадра (`blocks:`/`scheme:`/`columns:`/`figure:`), которые читает
`deckkit.slidefile`/`deckkit.plates`/`deckkit.scheme`/`deckkit.axis`/
`deckkit.columns`/`deckkit.figure`.

Это часть доказательства замера issue #306, а не черновик: перевод не
бросает исключение молча и не придумывает значение — каждое расхождение со
словарём (`slovar-tegov.md`) называется `[словарь]` и копится в список
`WARNINGS`, который попадает в REZULTAT.md как счётчик «изобретённая
разметка».

Контракт входа — РОВНО один корневой `<kadr>` на файл, внутри — РОВНО один
из пяти корней формы (`<plashki>`/`<os>`/`<stolbcy>`/`<shema>`/`<chislo>`).
Парсится `xml.etree.ElementTree` (вход должен быть well-formed XML — теги
закрыты, атрибуты в кавычках).

Запуск:
    python3 html2kadr.py <kadr-N.html> [<kadr-N.html> ...]
    — печатает для каждого файла разобранный YAML-фрагмент и список
      предупреждений `[словарь]`, если были.

Как библиотека:
    from html2kadr import parse_kadr_html
    field_yaml_dict, warnings = parse_kadr_html(text)
"""
import re
import sys
import xml.etree.ElementTree as ET

# ── закрытые словари: тег → разрешённые атрибуты, тег → разрешённые дети ──

PLASHKI_PLATE_ATTRS = {"klyuch"}
OS_ATTRS = {"edinica", "podpis_osi"}
OS_ZASECHKA_ATTRS = {"znachenie", "podpis", "klyuch"}
SHEMA_ATTRS = {"arrows", "podpis_shemy"}
SHEMA_RYAD_ATTRS = {"podpis", "arrows"}
CHISLO_ATTRS = {"znachenie", "edinica", "baza", "ogovorka"}
STOLBEC_ATTRS = {"zagolovok"}

WARNINGS = []


def warn(text):
    WARNINGS.append(text)


def _num(raw):
    if raw is None:
        return None
    s = str(raw).strip().replace("−", "-").replace(" ", "").replace(" ", "") \
        .replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def _bool_attr(raw, default=None):
    if raw is None:
        return default
    return str(raw).strip().lower() in ("true", "1", "да", "истина")


def _unknown_attrs(tag, el, allowed, where):
    extra = [k for k in el.attrib if k not in allowed]
    if extra:
        warn(f"[словарь] {where}: у тега <{tag}> атрибут"
             f"{'ы' if len(extra) > 1 else ''} вне словаря — "
             + ", ".join(f"`{k}`" for k in extra))


def _unknown_children(tag, el, allowed, where):
    extra = sorted({c.tag for c in el if c.tag not in allowed})
    if extra:
        warn(f"[словарь] {where}: внутри <{tag}> тег"
             f"{'и' if len(extra) > 1 else ''} вне словаря — "
             + ", ".join(f"`<{k}>`" for k in extra))


def _text(el, tag_name):
    """Текст дочернего тега `tag_name`, либо пусто."""
    child = el.find(tag_name)
    if child is None:
        return ""
    return (child.text or "").strip()


def parse_plashki(root, where):
    _unknown_children("plashki", root, {"plashka"}, where)
    plates = root.findall("plashka")
    if not plates:
        warn(f"[словарь] {where}: <plashki> без ни одной <plashka>")
        return None
    out = []
    n_klyuch = 0
    for i, p in enumerate(plates, 1):
        _unknown_attrs("plashka", p, PLASHKI_PLATE_ATTRS, f"{where}/плашка{i}")
        _unknown_children("plashka", p, {"podpis", "znachenie", "ogovorka"},
                           f"{where}/плашка{i}")
        klyuch = _bool_attr(p.get("klyuch"), False)
        if klyuch:
            n_klyuch += 1
        out.append({
            "label": _text(p, "podpis"),
            "value": _text(p, "znachenie"),
            "note": _text(p, "ogovorka"),
            "key": klyuch,
        })
    if n_klyuch > 1:
        warn(f"[словарь] {where}: `klyuch=\"true\"` стоит на {n_klyuch} "
             "плашках — словарь требует не больше одной")
    return {"blocks": out}


def parse_os(root, where):
    _unknown_attrs("os", root, OS_ATTRS, where)
    _unknown_children("os", root, {"zasechka"}, where)
    marks_el = root.findall("zasechka")
    if not marks_el:
        warn(f"[словарь] {where}: <os> без ни одной <zasechka>")
        return None
    marks = []
    n_klyuch = 0
    for i, z in enumerate(marks_el, 1):
        _unknown_attrs("zasechka", z, OS_ZASECHKA_ATTRS, f"{where}/засечка{i}")
        v = _num(z.get("znachenie"))
        if v is None:
            warn(f"[словарь] {where}/засечка{i}: `znachenie` "
                 f"«{z.get('znachenie')}» не число")
        klyuch = _bool_attr(z.get("klyuch"), False)
        if klyuch:
            n_klyuch += 1
        marks.append({"value": z.get("znachenie"), "label": z.get("podpis") or "",
                       "key": klyuch})
    if n_klyuch > 1:
        warn(f"[словарь] {where}: `klyuch` стоит на {n_klyuch} засечках — "
             "словарь требует не больше одной")
    return {"scheme": {
        "kind": "shkala",
        "unit": root.get("edinica") or "",
        "caption": root.get("podpis_osi") or "",
        "marks": marks,
    }}


def parse_stolbcy(root, where):
    _unknown_children("stolbcy", root, {"levyy", "pravyy"}, where)
    levyy, pravyy = root.find("levyy"), root.find("pravyy")
    if levyy is None or pravyy is None:
        warn(f"[словарь] {where}: <stolbcy> без <levyy> и/или <pravyy>")
        return None

    def _col(el, name):
        _unknown_attrs(name, el, STOLBEC_ATTRS, f"{where}/{name}")
        _unknown_children(name, el, {"punkt"}, f"{where}/{name}")
        items = [(p.text or "").strip() for p in el.findall("punkt")]
        return {"head": el.get("zagolovok") or "", "items": items}

    left, right = _col(levyy, "levyy"), _col(pravyy, "pravyy")
    if len(left["items"]) != len(right["items"]):
        warn(f"[словарь] {where}: число <punkt> не совпадает — "
             f"левый {len(left['items'])}, правый {len(right['items'])}")
    return {"columns": {"left": left, "right": right}}


def parse_shema(root, where):
    _unknown_attrs("shema", root, SHEMA_ATTRS, where)
    _unknown_children("shema", root, {"ryad"}, where)
    ryady = root.findall("ryad")
    if not ryady:
        warn(f"[словарь] {where}: <shema> без ни одного <ryad>")
        return None
    rows = []
    for i, r in enumerate(ryady, 1):
        _unknown_attrs("ryad", r, SHEMA_RYAD_ATTRS, f"{where}/ряд{i}")
        _unknown_children("ryad", r, {"shag"}, f"{where}/ряд{i}")
        steps = [(s.text or "").strip() for s in r.findall("shag")]
        if not steps:
            warn(f"[словарь] {where}/ряд{i}: без ни одного <shag>")
        row = {"label": r.get("podpis") or "", "steps": steps}
        if r.get("arrows") is not None:
            row["arrows"] = _bool_attr(r.get("arrows"))
        rows.append(row)
    sch = {"caption": root.get("podpis_shemy") or "", "rows": rows}
    if root.get("arrows") is not None:
        sch["arrows"] = _bool_attr(root.get("arrows"))
    # arrows ряда, если назван явно, идёт отдельным ключом в rows[i]["arrows"];
    # если схемный `arrows` задан, а ряд не переопределил — ряд наследует
    # схемный (это и так поведение ядра: `row_arrows` берёт схемный, если
    # ряд None). Здесь явность СОХРАНЯЕТСЯ как есть, ядро решит само.
    return {"scheme": sch}


def parse_chislo(root, where):
    _unknown_attrs("chislo", root, CHISLO_ATTRS, where)
    if list(root):
        warn(f"[словарь] {where}: <chislo> не принимает дочерних тегов — "
             "все четыре поля атрибутами")
    val = root.get("znachenie") or ""
    if not val:
        warn(f"[словарь] {where}: <chislo> без `znachenie`")
        return None
    return {"figure": {
        "value": val,
        "unit": root.get("edinica") or "",
        "base": root.get("baza") or "",
        "note": root.get("ogovorka") or "",
    }}


ROOT_PARSERS = {
    "plashki": parse_plashki,
    "os": parse_os,
    "stolbcy": parse_stolbcy,
    "shema": parse_shema,
    "chislo": parse_chislo,
}


def parse_kadr_html(text, where="kadr"):
    """Текст `<kadr>...</kadr>` → (словарь полей фронтматтера, предупреждения).

    Возвращает (None, warnings) при неразборе — то же правило, что у
    `plates_of`/`scheme_of`/`figure_of`/`columns_of`: чужая форма не роняет
    перевод, она называется предупреждением."""
    WARNINGS.clear()
    try:
        root = ET.fromstring(text)
    except ET.ParseError as e:
        warn(f"[словарь] {where}: XML не разбирается — {e}")
        return None, list(WARNINGS)
    if root.tag != "kadr":
        warn(f"[словарь] {where}: корневой тег «{root.tag}», ожидался <kadr>")
        return None, list(WARNINGS)
    forms = [c for c in root if c.tag in ROOT_PARSERS]
    unknown_roots = [c.tag for c in root if c.tag not in ROOT_PARSERS]
    if unknown_roots:
        warn(f"[словарь] {where}: внутри <kadr> корень формы вне словаря — "
             + ", ".join(f"`<{t}>`" for t in sorted(set(unknown_roots))))
    if len(forms) != 1:
        warn(f"[словарь] {where}: внутри <kadr> форм {len(forms)} — "
             "ожидается ровно одна (одна из <plashki>/<os>/<stolbcy>/"
             "<shema>/<chislo>)")
        if not forms:
            return None, list(WARNINGS)
    field = ROOT_PARSERS[forms[0].tag](forms[0], where)
    return field, list(WARNINGS)


def to_yaml_fragment(field):
    """Словарь поля → YAML-текст того же вида, что пишет заполнитель слотов
    руками. `yaml.safe_dump` с `allow_unicode` даёт корректные отступы без
    ручной сборки строк — и ровно то же самое дерево, что прочитал бы
    `yaml.safe_load` из настоящего файла кадра."""
    import yaml
    return yaml.safe_dump(field, allow_unicode=True, default_flow_style=False,
                          sort_keys=False, width=100)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        field, warnings = parse_kadr_html(text, where=path)
        print(f"=== {path} ===")
        if field:
            print(to_yaml_fragment(field))
        else:
            print("(не разобрано)")
        for w in warnings:
            print(" ", w)
        print()
