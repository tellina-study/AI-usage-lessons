#!/usr/bin/env python3
"""Аудит грамматики деки: какая форма какую работу несёт и на скольких слайдах.

Зачем. Прожарка измерила у прежней деки: ОДНА кремовая плашка во всю ширину
стояла на 31 слайде из 56 и несла шесть разных работ — вопрос залу, реплику
докладчика, тезис-итог, оговорку о пробеле, факт и технический блок. Если две
разные по смыслу вещи выглядят одинаково, зал не различит их и в зале.

Этот скрипт печатает, сколько слайдов носит каждую форму. Правило простое:
форма «вопрос» обязана быть РЕДКОЙ (она и означает редкое событие), а каждая
работа — иметь свою форму и не делить её с другой.

    python3 audit_grammar.py
"""
from collections import Counter, defaultdict
from pathlib import Path

import yaml

import build_sem05 as B
import slide_parts as SP

ROOT = Path(__file__).resolve().parent.parent


def main():
    deck = yaml.safe_load((ROOT / "deck.yaml").read_text(encoding="utf-8"))
    per_form = defaultdict(set)
    per_kind = Counter()
    rows = []
    for s in deck["slides"]:
        sid = s["id"]
        pattern = (s.get("visual") or {}).get("pattern", "")
        title, assertion, visual, _ = SP.sections((ROOT / s["file"]).read_text(encoding="utf-8"))
        forms = []
        for kind, b in SP.blocks(visual):
            if kind == "quote":
                r = B.quote_role(b, pattern)
                if pattern == "question_with_option_cards":
                    scene, _q = B.split_question(b)
                    forms += (["реплика"] if scene else []) + ["вопрос"]
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
            per_kind[kind] += 1
        for f in forms:
            per_form[f].add(sid)
        rows.append((sid, B.label_for(sid, pattern), " · ".join(forms) or "—"))

    n = len(deck["slides"])
    print(f"Грамматика деки — {n} слайдов\n")
    print(f"{'форма':<14}{'слайдов':>8}   {'доля':>6}")
    for f, ids in sorted(per_form.items(), key=lambda kv: -len(kv[1])):
        print(f"{f:<14}{len(ids):>8}   {len(ids) / n:>5.0%}")
    print("\nБыло до пересборки: одна кремовая плашка — 31 слайд из 56 на шесть разных работ.")
    print("Форма «вопрос» обязана оставаться редкой: это сигнал, а не фон.\n")
    for sid, label, forms in rows:
        print(f"  {sid}  {label:<28} {forms}")


if __name__ == "__main__":
    main()
