"""Build of Лекция 5 «AI-продукт: полный жизненный цикл» — FULL DECK.

Порядок внутри фазы (deck.yaml, пересборка 2026-09-28, issue #212):
  дивайдер → классика одной строкой-определением → что ИИ меняет →
  практика (одна-три) → ограничения → провал фазы.
Приём стоит после названной классики и до разбора провала, чтобы читался как
ответ на только что показанную проблему. В Разделах 4-6 отдельного слайда
«что ИИ меняет» нет — его работу несут сами практики.

Source-of-truth: deck.yaml + deck-part2.yaml + slides/*.md (заметки и источники
подтягиваются из .md автоматически через load_notes / notes_with_sources).

Palette LOCKED: Ocean Gradient + Teal secondary + Gold >=1x/slide. Motif
«Ocean rounded box». Canvas 13.333"x7.5" (16:9).

56 слайдов, Σ 92,6 мин полного прохода при слоте 90.
Снято при пересборке (13): s07b s14b s21b s28b s36b s44b (обзоры-введения) ·
s24 (поглощён s24a) · s31 (поглощён s31a) · s38 (поглощён s38a/s38b) ·
s35 s43 (посекционные синтезы) · s49 (дубль s47/s51/s55) · s52 (в главу).
Их builder-функции остаются в slides_band1..5.py мёртвым кодом и не вызываются.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _helpers import setup_pres, ROOT, page_number  # noqa: E402
import slides_band1 as b1  # noqa: E402
import slides_band2 as b2  # noqa: E402
import slides_band3 as b3  # noqa: E402
import slides_band4 as b4  # noqa: E402
import slides_band5 as b5  # noqa: E402
import slides_band6 as b6  # noqa: E402

OUT = ROOT / "rendered/lec-05.pptx"

# Слайды-практики (band6) — по id, чтобы порядок читался вместе с остальными.
P = {fn.__name__: fn for fn in b6.BUILDERS}


# Порядок показа — модульная константа, чтобы им мог пользоваться не только
# main(), но и почанковый рендер (см. notes/mcp-limitations.md [#212-1]:
# на нагруженной машине LibreOffice не вытягивает деку целиком за один заход).
ORDER = [
    # ── Раздел 0. Введение + keystone (9,0 мин) ──
    b1.s01, b1.s02, b1.s03, b1.s04, b1.s05, b1.s06,
    # ── Раздел 1. Исследование (13,3 мин) ──
    b1.s07,                      # дивайдер
    b1.s08,                      # база: Customer Development
    b1.s10,                      # что ИИ меняет (+ граница Deloitte)
    P["s11a"], P["s11b"],        # практики
    b1.s11,                      # ограничения
    b1.s12, b1.s13a,             # провалы
    # ── Раздел 2. Дизайн (9,3 мин) ──
    b2.s14,                      # дивайдер
    b2.s15,                      # база: Double Diamond
    b2.s17,                      # что ИИ меняет
    P["s17a"],                   # практика
    b2.s18,                      # ограничения (+ iTutorGroup соседним классом)
    b2.s19,                      # провал
    # ── Раздел 3. Сборка и запуск (14,8 мин) ──
    b2.s21,                      # дивайдер
    b2.s22,                      # база: MVP и механика релиза
    b2.s23,                      # что ИИ меняет
    P["s24a"], P["s24b"], P["s24c"],   # практики
    b2.s25,                      # ограничения
    b2.s26, b2.s27,              # провалы
    # ── Раздел 4. Измерение (11,8 мин) ──
    b3.s28,                      # дивайдер
    b3.s29,                      # база: контролируемый эксперимент и OEC
    P["s30a"], P["s31a"],        # практики
    b3.s32,                      # ограничения
    b3.s33, b3.s34,              # провалы
    # ── Раздел 5. Поддержка (13,8 мин) ──
    b3.s36,                      # дивайдер
    b3.s37,                      # база: SRE
    P["s38a"], P["s38b"],        # практики
    b3.s39,                      # ограничения
    b3.s40, b3.s41, b3.s42,      # провалы
    # ── Раздел 6. Управление (11,3 мин) ──
    b4.s44,                      # дивайдер
    b4.s45,                      # база: управление портфелем
    P["s45a"], P["s45b"],        # практики
    b4.s46,                      # подводка к провалу
    b4.s47, b4.s48,              # провалы
    # ── Раздел 7. Обобщение и фреймворк решения (9,3 мин) ──
b5.s50, b5.s51, b5.s53, b5.s54, b5.s55,
]


def main():
    p = setup_pres()
    builders = ORDER

    for fn in builders:
        fn(p)

    total = len(builders)
    for i, slide in enumerate(p.slides, start=1):
        page_number(slide, i, total)

    n = len(p.slides._sldIdLst)
    assert n == total, f"expected {total} slides, got {n}"
    assert n == 56, f"target 56 slides, got {n}"
    p.save(str(OUT))
    print(f"saved {OUT} — {n} slides (FULL DECK)")


if __name__ == "__main__":
    main()
