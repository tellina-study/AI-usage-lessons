"""Fetch + recolor the extra Lucide icons needed by Band 6 (двенадцать
слайдов-практик, issue #212). Тот же механизм и те же цвета, что в
gen_icons.py — отдельный файл, чтобы не трогать общий gen_icons.py, пока по
каталогу работает другой агент. Идемпотентен: уже лежащие иконки пропускает.
"""
import os
import sys

sys.path.insert(
    0,
    "/home/harness/harness-control-data/accounts/256/"
    "claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages",
)
os.environ.setdefault(
    "LD_LIBRARY_PATH",
    "/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu",
)

from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from gen_icons import COLORS, OUT, recolor_and_render  # noqa: E402

BAND6_ICONS = [
    # s11a — панель субагентов
    "file-diff", "target", "octagon-alert",
    # s11b — поиск по корпусу обращений
    "search-check", "group",
    # s17a — дизайн-система как гейт
    "palette", "component", "eye-off",
    # s24a — лестница агентности
    "trending-up", "undo-2",
    # s24b — эталонный набор
    "file-json", "git-pull-request-closed",
    # s24c — чем исполняется гейт
    "terminal", "repeat-2",
    # s30a — пред-регистрация
    "file-lock", "git-commit-horizontal", "calendar-clock",
    # s31a — петля оценок
    "refresh-cw", "trending-down",
    # s38a — наблюдаемость
    "activity", "shield-off",
    # s38b — учение
    "timer", "siren",
    # s45a — стоимость на запрос
    "calculator", "chart-line",
    # s45b — финансовый критерий
    "clipboard-check", "user-check", "door-open",
]


def main():
    done = skipped = failed = 0
    for name in BAND6_ICONS:
        for variant in ("deep", "mid", "light", "teal", "gold", "white", "slate"):
            if (OUT / f"{name}-{variant}.png").exists():
                skipped += 1
                continue
            try:
                recolor_and_render(name, COLORS[variant], 96, variant)
                done += 1
            except Exception as e:
                failed += 1
                print(f"FAILED {name}-{variant}: {e}")
    print(f"done: {done} generated, {skipped} already present, {failed} failed")


if __name__ == "__main__":
    main()
