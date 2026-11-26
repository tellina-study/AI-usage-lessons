#!/usr/bin/env python3
"""Веха 2 (issue #351) — реконструкция «состояния счёта» (аналог старой 5-строчной
таблицы README) на n=100. Разовый анализ для отчёта, не часть production score.py —
не меняет raw/scored_all.json, ничего не записывает, кроме stdout.

Правки применяются кумулятивно в том же порядке, что в README:
  0. до всех правок — 369 полей, простое сравнение ПО ПОЗИЦИИ (без перебора
     перестановок внутри группы), базовый normalize (только пробелы/дефисы/скобки
     схлопнуты в один пробел, регистр снижен).
  1. + склейка дат (83553333_3334 November+1999 И новая 92091873 6/+12/+95) +
     исключение дефектов эталона (zbulan И новая Check#) + группировка ПО МНОЖЕСТВУ
     (перебор перестановок), но ПО КАТЕГОРИИ (не по точному тексту подписи) —
     тот же базовый normalize.
  2. + полное снятие пробелов (не только схлопывание).
  3. + полное снятие пунктуации (сегодняшний normalize()).
  4. + группировка по ТОЧНОМУ ТЕКСТУ ПОДПИСИ (финал — совпадает с score.py).
"""
import itertools
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent

OLD_EXCLUDE = {("82254765", "DATE FORWARDED TO PROMOTION SERVICES:", "zbulan")}
NEW_EXCLUDE = {("71341634", "Date", "Check#")}


def normalize_basic(s):
    """Исходная (до правок) версия — пробелы/дефисы/скобки в пробел, схлопнуть, регистр."""
    if s is None:
        return ""
    s = str(s).lower()
    s = re.sub(r"[-()]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def normalize_nospace(s):
    """+ полное снятие пробелов (не только схлопывание) — пунктуация, кроме убранной
    выше, ещё сохраняется (точки/запятые/двоеточия остаются)."""
    if s is None:
        return ""
    s = str(s).lower()
    s = re.sub(r"[-()]", "", s)
    s = re.sub(r"\s+", "", s)
    return s


def normalize_full(s):
    """Финальная версия (= score.py::normalize) — любая пунктуация убрана целиком."""
    if s is None:
        return ""
    s = str(s).lower()
    return re.sub(r"[^0-9a-zа-яё]", "", s)


def load_corpus():
    return json.load(open(HERE / "korpus" / "vyborka.json"))


def build_targets(corpus, use_exclude, use_merge):
    """Возвращает {fid: [items]} с опциональным исключением/склейкой."""
    out = {}
    for form in corpus:
        fid = form["form_id"]
        items = []
        for i, t in enumerate(form["targets"], 1):
            key3 = (fid, t["q_text"], t["a_text"])
            if use_exclude and (key3 in OLD_EXCLUDE or key3 in NEW_EXCLUDE):
                continue
            items.append({"field_key": f"field_{i}", "q_text": t["q_text"], "cat": t["cat"],
                          "a_text": t["a_text"]})
        if use_merge:
            # 83553333_3334: field_3(November)+field_5(1999) -> одно поле
            if fid == "83553333_3334":
                keys = [it["field_key"] for it in items if it["q_text"] == "Date"]
                if set(keys) == {"field_3", "field_5"}:
                    items = [it for it in items if it["q_text"] != "Date"] + [
                        {"field_key": "field_3+5", "q_text": "Date", "cat": "date",
                         "a_text": "November 1999"}]
            # 92091873: field_1(6/)+field_2(12/)+field_3(95) -> одно поле
            if fid == "92091873":
                keys = [it["field_key"] for it in items if it["q_text"] == "Date"]
                if set(keys) == {"field_1", "field_2", "field_3"}:
                    items = [it for it in items if it["q_text"] != "Date"] + [
                        {"field_key": "field_1+2+3", "q_text": "Date", "cat": "date",
                         "a_text": "6/ 12/ 95"}]
        out[fid] = items
    return out


def get_pred(method_data, fid, field_key):
    parsed = (method_data.get(fid) or {}).get("parsed")
    if not isinstance(parsed, dict):
        return None
    if field_key in ("field_3+5",):
        p3, p5 = parsed.get("field_3"), parsed.get("field_5")
        return " ".join(p for p in (p3, p5) if p) or None
    if field_key == "field_1+2+3":
        p1, p2, p3 = parsed.get("field_1"), parsed.get("field_2"), parsed.get("field_3")
        return " ".join(p for p in (p1, p2, p3) if p) or None
    return parsed.get(field_key)


def rules_pred_all(rules, fid, items):
    extracted = rules.get(fid, {})
    cursor = {}
    out = {}
    for it in items:
        # для склеенных полей (field_3+5 / field_1+2+3) берём по категории как обычно,
        # считая это ОДНИМ полем в последовательности (упрощение для этого анализа —
        # правила и так почти всегда возвращают None на этих полях)
        cat = it["cat"]
        idx = cursor.get(cat, 0)
        vals = extracted.get(cat, [])
        out[it["field_key"]] = vals[idx] if idx < len(vals) else None
        cursor[cat] = idx + 1
    return out


def score_state(corpus, targets_by_form, pred_getter, normalize_fn, group_key_fn, use_permutation):
    total, exact = 0, 0
    for form in corpus:
        fid = form["form_id"]
        items = targets_by_form[fid]
        pred_by_key = pred_getter(fid, items)
        if not use_permutation:
            for it in items:
                total += 1
                p = normalize_fn(pred_by_key.get(it["field_key"]))
                g = normalize_fn(it["a_text"])
                if p and p == g:
                    exact += 1
            continue
        by_group = {}
        for it in items:
            by_group.setdefault(group_key_fn(it), []).append(it)
        for gkey, its in by_group.items():
            preds = [pred_by_key.get(it["field_key"]) for it in its]
            gts = [it["a_text"] for it in its]
            n = len(its)
            npreds = [normalize_fn(p) for p in preds]
            ngts = [normalize_fn(g) for g in gts]
            best = -1
            for perm in itertools.permutations(range(n)):
                s = sum(1 for i in range(n) if npreds[i] and npreds[i] == ngts[perm[i]])
                if s > best:
                    best = s
            total += n
            exact += best
    return exact, total


def main():
    corpus = load_corpus()
    vision = json.load(open(HERE / "raw" / "vision_results.json"))["per_form"]
    hybrid = json.load(open(HERE / "raw" / "hybrid_results.json"))["per_form"]
    rules = json.load(open(HERE / "raw" / "rules_extraction.json"))
    # Четвёртый метод (задание владельца 2026-11-25) — ДОБАВЛЕН в тот же прогон состояний,
    # ни одна из пяти ступеней не переписана под него: он проходит ровно те же правки,
    # в том же порядке, что три прежних (иначе таблица перестала бы быть доказательством
    # «правки не подгонка» и стала бы четырьмя разными лестницами рядом).
    vision_ocr = json.load(open(HERE / "raw" / "vision_ocr_results.json"))["per_form"]

    def vision_pred(fid, items):
        return {it["field_key"]: get_pred(vision, fid, it["field_key"]) for it in items}

    def hybrid_pred(fid, items):
        return {it["field_key"]: get_pred(hybrid, fid, it["field_key"]) for it in items}

    def rules_predfn(fid, items):
        return rules_pred_all(rules, fid, items)

    def vision_ocr_pred(fid, items):
        return {it["field_key"]: get_pred(vision_ocr, fid, it["field_key"]) for it in items}

    methods = [("vision", vision_pred), ("hybrid", hybrid_pred), ("ocr_rules", rules_predfn),
               ("vision_ocr", vision_ocr_pred)]

    # --- Состояние 0: без исключений/склейки, без перестановок, базовый normalize ---
    targets0 = build_targets(corpus, use_exclude=False, use_merge=False)
    print("Состояние 0 (369 полей, простое сравнение по позиции, базовый normalize):")
    for name, predfn in methods:
        e, t = score_state(corpus, targets0, predfn, normalize_basic, None, use_permutation=False)
        print(f"  {name}: {e}/{t} = {e/t:.3f}")

    # --- Состояние 1: + склейка дат + исключение дефектов + группировка по КАТЕГОРИИ, базовый normalize
    targets1 = build_targets(corpus, use_exclude=True, use_merge=True)
    n1 = sum(len(v) for v in targets1.values())
    print(f"\nСостояние 1 (+ склейка дат x2, исключение x2, группировка по категории, {n1} полей):")
    for name, predfn in methods:
        e, t = score_state(corpus, targets1, predfn, normalize_basic,
                            lambda it: it["cat"], use_permutation=True)
        print(f"  {name}: {e}/{t} = {e/t:.3f}")

    # --- Состояние 2: + полное снятие пробелов, та же группировка по категории ---
    print(f"\nСостояние 2 (+ полное снятие пробелов, группировка по категории, {n1} полей):")
    for name, predfn in methods:
        e, t = score_state(corpus, targets1, predfn, normalize_nospace,
                            lambda it: it["cat"], use_permutation=True)
        print(f"  {name}: {e}/{t} = {e/t:.3f}")

    # --- Состояние 3: + полное снятие пунктуации, та же группировка по категории ---
    print(f"\nСостояние 3 (+ полное снятие пунктуации, группировка по категории, {n1} полей):")
    for name, predfn in methods:
        e, t = score_state(corpus, targets1, predfn, normalize_full,
                            lambda it: it["cat"], use_permutation=True)
        print(f"  {name}: {e}/{t} = {e/t:.3f}")

    # --- Состояние 4 (финал): группировка по ТОЧНОМУ ТЕКСТУ ПОДПИСИ ---
    print(f"\nСостояние 4 / финал (группировка по точному тексту подписи, = score.py):")
    for name, predfn in methods:
        e, t = score_state(corpus, targets1, predfn, normalize_full,
                            lambda it: (it["q_text"]), use_permutation=True)
        print(f"  {name}: {e}/{t} = {e/t:.3f}")


if __name__ == "__main__":
    main()
