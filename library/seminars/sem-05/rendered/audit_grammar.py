#!/usr/bin/env python3
"""Аудит грамматики деки: какая форма какую работу несёт и на скольких слайдах.

Зачем. Прожарка измерила у прежней деки: ОДНА кремовая плашка во всю ширину
стояла на 31 слайде из 56 и несла шесть разных работ — вопрос залу, реплику
докладчика, тезис-итог, оговорку о пробеле, факт и технический блок. Если две
разные по смыслу вещи выглядят одинаково, зал не различит их и в зале.

Этот скрипт печатает, сколько слайдов носит каждую форму. Правило простое:
форма «вопрос» обязана быть РЕДКОЙ (она и означает редкое событие), а каждая
работа — иметь свою форму и не делить её с другой.

Второй раздел вывода — СВЕРКА ПРИЁМОВ: какой набор форм даёт каждый приём и нет
ли двух приёмов с одинаковым набором. Это и есть механическая проверка «новый
приём не совпал со старым»: глазами её делать нельзя, приёмов тридцать.

Пробные слайды нового приёма (`probe_base_edge.py`) входят в сверку наравне с
настоящими. Иначе приём, которого ещё нет ни в одном слайде `deck.yaml`, в
аудит не попадал бы вовсе — а проверять его надо ДО того, как шесть
параллельных сессий напишут по нему тексты, а не после.

    python3 audit_grammar.py
"""
from collections import Counter, defaultdict
from pathlib import Path

import yaml

import build_sem05 as B
import slide_parts as SP

ROOT = Path(__file__).resolve().parent.parent


def forms_of(sid, pattern, visual):
    """Какие формы грамматики окажутся на этом слайде."""
    forms = []
    for kind, b in SP.blocks(visual):
        if kind == "table" and pattern == "base_and_edge":
            # Двухколоночная таблица Такта Б — это не таблица, а ДОРОЖКИ:
            # жанр разбирает её сам и рисует седьмой, бескоробочной формой.
            forms.append("дорожки")
            continue
        if kind == "quote":
            r = B.quote_role(b, pattern)
            if pattern == "question_with_option_cards":
                scene, _q, found = B.split_question(b)
                forms += ((["реплика"] if scene else []) + ["вопрос"]) if found else [
                    {"question": "вопрос", "formula": "формула", "speech": "реплика",
                     "caveat": "оговорка", "fact": "факт"}[r]]
            else:
                forms.append({"question": "вопрос", "formula": "формула",
                              "speech": "реплика", "caveat": "оговорка",
                              "fact": "факт"}[r])
        elif kind == "table":
            forms.append("таблица")
        elif kind == "code":
            forms.append("технический")
        elif kind == "cards":
            forms.append("варианты" if pattern == "question_with_option_cards" else "термины")
        elif kind == "bullets":
            forms.append("список")
        elif kind == "para":
            # Голый абзац несёт ту же работу, что и абзац в плашке `>`, и
            # получает ту же форму. В аудите он обязан считаться наравне —
            # иначе форма, попавшая на слайд, в грамматике не видна.
            forms.append({"question": "вопрос", "formula": "формула",
                          "speech": "реплика", "caveat": "оговорка",
                          "fact": "факт"}[B.para_role(b, pattern)[0]])
    return forms


def probe_slides():
    """Пробные слайды приёмов, которых ещё нет в `deck.yaml`."""
    try:
        import probe_base_edge as P
    except Exception:
        return []
    out = []
    for name, md in P.PROBES.items():
        _t, _a, visual, _n = SP.sections(md)
        out.append((f"проба:{name}", "base_and_edge", visual))
    return out


def main():
    deck = yaml.safe_load((ROOT / "deck.yaml").read_text(encoding="utf-8"))
    per_form = defaultdict(set)
    per_kind = Counter()
    per_pattern = defaultdict(set)
    rows = []
    for s in deck["slides"]:
        sid = s["id"]
        pattern = (s.get("visual") or {}).get("pattern", "")
        _t, _a, visual, _n = SP.sections((ROOT / s["file"]).read_text(encoding="utf-8"))
        for kind, _b in SP.blocks(visual):
            per_kind[kind] += 1
        forms = forms_of(sid, pattern, visual)
        for f in forms:
            per_form[f].add(sid)
        if pattern:
            per_pattern[pattern].add(tuple(forms))
        # Второй столбец был надзаголовком жанра («ХУК · ВОПРОС»), который
        # печатался на слайде. Надзаголовок снят (круг 4, А3) вместе с таблицей
        # `GENRE`, и столбец переведён на то, что в деке осталось: раздел по
        # границам + сам приём. Отчёт стал точнее — приём виден дословно, а не
        # через ярлык, который ещё надо было завести вручную.
        rows.append((sid, f"{B.where(sid)[0]} · {pattern or '—'}",
                     " · ".join(forms) or "—"))

    for sid, pattern, visual in probe_slides():
        forms = forms_of(sid, pattern, visual)
        per_pattern[pattern].add(tuple(forms))
        rows.append((sid, f"проба · {pattern}", " · ".join(forms) or "—"))

    n = len(deck["slides"])
    print(f"Грамматика деки — {n} слайдов\n")
    print(f"{'форма':<14}{'слайдов':>8}   {'доля':>6}")
    for f, ids in sorted(per_form.items(), key=lambda kv: -len(kv[1])):
        print(f"{f:<14}{len(ids):>8}   {len(ids) / n:>5.0%}")
    print("\nБыло до пересборки: одна кремовая плашка — 31 слайд из 56 на шесть разных работ.")
    print("Форма «вопрос» обязана оставаться редкой: это сигнал, а не фон.\n")
    for sid, label, forms in rows:
        print(f"  {sid}  {label:<28} {forms}")

    # ── Сверка приёмов: у двух разных приёмов не должно быть одинакового
    #    набора форм, иначе зал видит один и тот же слайд под двумя работами.
    print("\nНАБОРЫ ФОРМ ПО ПРИЁМАМ\n")
    sig = {}
    for pattern, variants in sorted(per_pattern.items()):
        key = frozenset(frozenset(v) for v in variants)
        sig.setdefault(key, []).append(pattern)
        shown = " | ".join(" · ".join(v) or "—" for v in sorted(variants))
        print(f"  {pattern:<34} {shown}")

    clashes = [ps for ps in sig.values() if len(ps) > 1]
    print()
    if clashes:
        for ps in clashes:
            print("  СОВПАЛИ: " + ", ".join(ps))
        print("\n  Совпадение само по себе не дефект: два приёма могут честно")
        print("  делить форму, если РАБОТА у них одна (например, оба — просто")
        print("  утверждение с формулой). Дефект — когда работы разные.")
    else:
        print("  Одинаковых наборов форм нет.")

    if "base_and_edge" in per_pattern:
        mine = frozenset(frozenset(v) for v in per_pattern["base_and_edge"])
        same = [p for p in sig[mine] if p != "base_and_edge"]
        print(f"\n  base_and_edge → {'совпал с ' + ', '.join(same) if same else 'набор форм уникален'}")


if __name__ == "__main__":
    main()
