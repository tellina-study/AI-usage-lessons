"""Временная сборка ТОЛЬКО двенадцати слайдов-практик (Band 6, issue #212).

Полную деку этим файлом не собрать и не нужно: её раскладку в это же время
меняет другой агент, поэтому пишем в собственный временный pptx и не трогаем
rendered/lec-05.pptx. Оркестратор повторяет цикл так:

    python3 library/lectures/lec-05/rendered/build_band6.py
    library/lectures/lec-05/rendered/render_band6.sh          # все 12
    library/lectures/lec-05/rendered/render_band6.sh 3 7      # только 3-й и 7-й
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _helpers import setup_pres, page_number  # noqa: E402
import slides_band6 as b6  # noqa: E402

OUT = Path("/tmp/b6-check.pptx")


def main():
    p = setup_pres()
    for fn in b6.BUILDERS:
        fn(p)
    total = len(b6.BUILDERS)
    for i, slide in enumerate(p.slides, start=1):
        page_number(slide, i, total)
    p.save(str(OUT))
    print(f"saved {OUT} — {total} slides (band 6 only)")
    if b6.WARN:
        print("--- переполнения (надо править высоты) ---")
        for wln in b6.WARN:
            print("  " + wln)
    else:
        print("переполнений нет")


if __name__ == "__main__":
    main()
