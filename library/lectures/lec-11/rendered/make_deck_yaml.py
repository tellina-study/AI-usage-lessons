#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Пересборка `slides:`-перечня `deck.yaml` Лекции 11 из фронтматтера
`slides/*.md` (issue #353, раздел 3/8 спеки `07-design-review-spec.md`:
«deck.yaml после этого пересобрать МЕХАНИЧЕСКИ из фронтматтера»).

Читает фронтматтер ТЕМ ЖЕ модулем, что сборка (`deckkit.slidefile`), в ТОМ
ЖЕ порядке (`slidefile.slide_files` — сортировка по имени файла), чтобы
`deck.yaml` не мог разойтись со сборкой в порядке или в чтении поля:
расхождение было бы второй копией парсера, которая расходится с первой на
первой же правке.

Верхний блок `deck.yaml` (`deck:`/`sections:`) — рукописный нарратив
(ось, keystone, список разделов), а не перенос фронтматтера; скрипт его
НЕ трогает, читает как есть до строки `slides:` и переписывает только
список ниже неё.

`note:` на уровне слайда — единственное поле списка, которого НЕТ во
фронтматтере (не механический перенос, историческая пометка «новый кадр
issue #353»); значения на существующих id сохраняются явным словарём
`EXTRA_NOTES` ниже, а не изобретаются заново.

Запуск: `python3 make_deck_yaml.py` из каталога `rendered/` (пути строятся
от собственного расположения файла)."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent              # .../lec-11/rendered
LEC_ROOT = HERE.parent                                # .../lec-11
REPO_ROOT = HERE.parents[3]
sys.path.insert(0, str(REPO_ROOT / "tools" / "presentation-build"))

from deckkit import slidefile  # noqa: E402

SLIDES_DIR = LEC_ROOT / "slides"
DECK_YAML = LEC_ROOT / "deck.yaml"

# Пометки, которых не несёт фронтматтер — перенесены вручную один раз при
# первой механической пересборке (issue #353 раздел 3), не выводятся из
# слайда. Добавляй сюда новую запись, когда вводишь кадр, который стоит
# пометить так же (новый кадр вне исходных 45), а не правь список руками
# в `deck.yaml`.
EXTRA_NOTES = {
    "s03a": ("НОВЫЙ кадр issue #353 правка 2 — содержательная сводка оси + "
             "keystone-тройки сразу после карты лекции, до разбора s05"),
    "s43a": ("НОВЫЙ кадр issue #353 правка 2 — три полных разбора одной "
             "строкой + вывод раздела 5 + callback к счёту линии, перед "
             "Q&A"),
    "s08a": ("НОВЫЙ кадр issue #353 раздел 4 спеки 07-design-review-spec.md "
             "— обзор стадии «технический контроль качества» по шаблону "
             "П4, сразу после дивайдера s08"),
    "s16a": ("НОВЫЙ кадр issue #353 раздел 4 спеки 07-design-review-spec.md "
             "— обзор стадии «техническое обслуживание и ремонт» по "
             "шаблону П4, сразу после дивайдера s16"),
    "s21a": ("НОВЫЙ кадр issue #353 раздел 4 спеки 07-design-review-spec.md "
             "— обзор стадии «управление технологическим процессом» по "
             "шаблону П4, сразу после дивайдера s21"),
    "s27a": ("НОВЫЙ кадр issue #353 раздел 4 спеки 07-design-review-spec.md "
             "— обзор стадии «безлюдное производство» по шаблону П4, "
             "сразу после дивайдера s27"),
}


def _q(s):
    """Строка в кавычках deck.yaml — escape `"` и `\\`, пусто → `\"\"`."""
    s = str(s or "")
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def build_entries():
    import re
    last_num = None
    lines = []
    for f in slidefile.slide_files(SLIDES_DIR):
        sl = slidefile.read_slide(f)
        if sl is None:
            print(f"[make_deck_yaml] пропущен (не читается как кадр): {f}",
                  file=sys.stderr)
            continue
        section = str(sl.meta.get("section") or "").strip()
        m = re.match(r"^(\d+)\.\s*(.+)$", section)
        if m and m.group(1) != last_num:
            lines.append(f"  # ===== Раздел {m.group(1)}. {m.group(2)} =====")
            last_num = m.group(1)
        rel_file = f.relative_to(LEC_ROOT).as_posix()
        kind = str(sl.meta.get("type") or "norm").strip()
        assertion = str(sl.meta.get("assertion") or "").strip()
        media = str(sl.meta.get("media") or "").strip()
        lines.append(f"  - id: {sl.sid}")
        lines.append(f"    file: {rel_file}")
        lines.append(f"    type: {kind}")
        lines.append(f"    section: {_q(section)}")
        lines.append(f"    assertion: {_q(assertion)}")
        lines.append(f"    media: {_q(media)}")
        note = EXTRA_NOTES.get(sl.sid)
        if note:
            lines.append(f"    note: {_q(note)}")
        lines.append("")
    return lines


def main():
    old = DECK_YAML.read_text(encoding="utf-8")
    marker = "\nslides:\n"
    if marker not in old:
        print("[make_deck_yaml] строка `slides:` не найдена — верхний блок "
              "не тронут, выхожу без записи", file=sys.stderr)
        return 1
    head = old.split(marker, 1)[0] + marker
    body = "\n".join(build_entries()).rstrip("\n") + "\n"
    DECK_YAML.write_text(head + body, encoding="utf-8")
    n = body.count("\n  - id: ")
    print(f"[make_deck_yaml] deck.yaml пересобран: {n} кадров")
    return 0


if __name__ == "__main__":
    sys.exit(main())
