#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HTML-фрагменты (`kadr-N.html`) → настоящие файлы кадра (`sNN-kadrN.md`),
той же "шапкой", что у записи слотов (см. `skelet-slotov.md`/агентские
промпты) — чтобы сравнение шло по ОДНОМУ и тому же остальному кадру,
расходясь только в способе заполнения формы."""
import sys
from pathlib import Path

ZAMER_DIR = Path("/home/harness/harness-projects/256/.worktrees/folder-288/session-0b2adb13-7ee7af40/notes/research/zamer-306")
sys.path.insert(0, str(ZAMER_DIR))
import html2kadr
import yaml

SHAPKI = {
    1: dict(id="s01", type="norm",
            title="Пример 1, без модели: шведская программа зовёт по возрасту"),
    2: dict(id="s02", type="norm",
            title="Пример работы системы человек–ИИ: 50 врачей читают описания случаев"),
    3: dict(id="s03", type="comparison",
            title="Вывод раздела: инструмент один, исходы противоположные"),
    4: dict(id="s04", type="norm",
            title="Семь действий стадии скрининга — и три, на которых включается модель"),
    5: dict(id="s05", type="norm",
            title="Москва, профилактический поток: сколько снимков не открывает человек"),
}


def assemble(nabor):
    sd = ZAMER_DIR / nabor
    total_warn = []
    for n in range(1, 6):
        src = sd / f"kadr-{n}.html"
        if not src.exists():
            print(f"{nabor}: {src.name} не найден — пропуск")
            continue
        text = src.read_text(encoding="utf-8")
        field, warns = html2kadr.parse_kadr_html(text, where=f"{nabor}/kadr-{n}")
        total_warn += warns
        sh = SHAPKI[n]
        meta = {"id": sh["id"], "type": sh["type"], "title": sh["title"],
                "source": "—", "media": ""}
        if field:
            meta.update(field)
        front = yaml.safe_dump(meta, allow_unicode=True,
                               default_flow_style=False, sort_keys=False,
                               width=100)
        out = (f"---\n{front}---\n\n## Видимый текст слайда\n\n"
               "## Заметки лектора\n\nЗамер issue #306.\n")
        dest = sd / f"s0{n}-kadr{n}.md"
        dest.write_text(out, encoding="utf-8")
        print(f"{nabor}: {src.name} -> {dest.name}"
              + (f"  [{len(warns)} предупреждений словаря]" if warns else ""))
    return total_warn


if __name__ == "__main__":
    naborees = sys.argv[1:] or ["nabor-2", "nabor-3"]
    for nb in naborees:
        assemble(nb)
