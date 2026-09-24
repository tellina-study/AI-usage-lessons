"""Full 58-slide build of Лекция 4 v4.5 «AI в жизненном цикле разработки ПО».

v4.5 (issue #162 round 6 — owner page-by-page review of the rendered deck).
Пять тематических блоков правились параллельно в изолированных worktree и
сведены здесь в один сборочный проход. Счётчик: 57 (+1 s14b, блок 1)
(−1 s21, блок 3) (+1 s03b, блок 5) = 58.

  · block 1 «контекст/инструкции»: +1 slide b2.s14b (конкретные артефакты
    четырёх архитектурных практик: ADR-скелет · fitness-функции ·
    Structurizr-C4 DSL · архитектурный гейт) сразу после матрицы b2.s14;
    b2.s18 переписан из schema_architecture в четыре явных УРОВНЯ контекста
    (+ определение JIT-извлечения + блок «что куда класть в репозитории»);
    b2.s18b перестроен в четыре предела, параллельные этим уровням; b2.s19 —
    расшифровка SAST и least-privilege на первом видимом употреблении.
  · block 2 «инструментарий»: переработаны b2.s20b (Skills — категории
    навыков + граница применимости), b2.s20c (MCP уже API/CLI + цепочка
    риск→смягчение), b2.s20e (три уровня логирования задач как прогрессия
    сложности + четвёртый вариант «трекер»), b2.s20d (git-конвенции от
    «зачем», а не от синтаксиса), b2.s20f (worktree — реальные инциденты
    #60295/#55724 + двухпанельная схема). Счёт не менялся.
  · block 3 «тестирование»: display-слайд 32 (anti-hype benchmarks, builder
    b3.s21) УДАЛЁН по прямому указанию владельца («слайд 32 — лишний,
    убрать»). Плюс переработаны три слайда раздела тестирования: TDD-слайд
    получил рецепт «что работает вместо форсинга порядка», BDD/trunk-based —
    явную структуру «+ / −», локальный инструментарий расширен до
    5 категорий (добавлены Playwright и локальная генерация тестов) с
    переосмыслением строк на «что делает / что без него невозможно».
  · block 4 «ревью + доставка/эксплуатация»: b3.s27 — третий кейс ревью
    (Xu et al., arXiv 2510.10165: −19% собственных коммитов у ядра команды,
    явно отделён от METR-исследования на s01); b3.s28 — «летальная триада»
    + четыре контроля как ядро слайда, все акронимы расшифрованы;
    b4.s31 (Replit) — «95» расшифровано на месте, «9 секунд» помечено как
    отдельный инцидент; b4.s33 (доставка) — один входной тезис; b4.s33b —
    возвращён разделитель «отдельное измерение, не тот же тренд» между ~55%
    и 8,4%. Счёт не менялся.
  · block 5 «закрытие + статистика отрасли»: +1 slide b1.s03b (внедрение по
    отрасли — Stack Overflow 2025 / DORA 2025, с базами) между s03 и s04;
    b4.s37b (Uber/Kiro) — «Эффект: не прослеживается» вынесен на видимый
    слой по-русски; b4.s38/b4.s39 переведены из рамки «AI да/нет» в рамку
    «AI — данность, калибруется цена/риск/автономия»; b4.s40 — убрана
    видимая ссылка на Семинар 4 (она принадлежит speech.md).

v4.4 (issue #162 round 3 — QA-fix pass): +7 slides s09b/s17b/s18b/s20g/s30b/
s33b/s37b (AWS Kiro vs 847-deployments contrast · Gemini CLI self-review ·
curation honest limits · Register .env secrets · Amazon Q wiper supply-chain
· BT Group/Azure Triangle vs IaC-insecurity · Uber adoption-without-criterion
+ Kiro dual-register bridge) + s20d/s20e ORDER SWAP (task-logging now
presents before git-conventions, matching book's round-3 §3.3d↔§3.3e
reorder) + content fixes on s16/s21/s25c/s34/s37-matrix/s38-triangulation +
notes-only additions on s20b/s20c/s28. 50 → 57 slides.

Methodology-first re-spine v4 (owner redirect #264) + edit pass v4.1
(#265/#266/#267/#268/#269): NEW foundations slide s05 (2 practice lists со
ссылками), keystone s06 переделан в ЦИКЛ ФАЗ (совпадает с роадмапом 0–7),
дивайдеры без тег-плашек, спека→требования в фазе требований, reqs
структура+процесс, нумерованная система ссылок [N] + кликабельные URL.

v4.2 (issue #162 round 1): +4 slides s20b/s20c/s20d/s20e (Skills · MCP для
кодинг-агента · git-конвенции как контракт · слой логирования задач)
вставлены между display s20 (harness-gate) и display s21 (70-percent-
problem), source §3.3b–§3.3e chapter-part3.md. 41 → 45 слайдов.

v4.3 (issue #162 round 2): +5 slides s11b/s20f/s25b/s25c/s35b — §1.2b
(визуализация требований: Mermaid User Journey + Gherkin, story-mapping
boundary), §3.3f (git worktree, self-referential Lec-2 incident), §4.4 (BDD +
trunk-based, compact), §4.5 (тестовый инструментарий API/БД/visual-
regression, schema_matrix), §6.3 (инструментарий документации на практике).
45 → 50 слайдов.

Source-of-truth: deck.yaml + deck-part2.yaml + slides/*.md (visible content +
visual_brief + readable speaker notes 150–300 слов).

Issue #170 · Branch: hc/lesson4-498d0d8c · #162 (round 1: s20b–s20e; round 2:
s11b/s20f/s25b/s25c/s35b)

Palette LOCKED: Ocean Gradient (#21295C / #065A82 / #1C7293) + Teal (#028090)
secondary + Gold (#F0AB00) ≥1×/slide. Motif «Ocean rounded box» на каждом
content-слайде. Canvas 13.333"×7.5" (16:9).

Structure (plan v4 §4, +4 slides #162):
  Р0 s01–s07 (введение + методическая рамка, без дивайдера) ·
  Р1 [s08] s09–s11 (требования) · Р2 [s12] s13–s15 (архитектура) ·
  Р3 [s16] s17–s18 · s19(harness-gate) · s20b s20c s20d s20e (NEW) ·
     s20(70%-проблема, display s21 area) · s21(anti-hype) ·
  Р4 [s22] s23–s24 (тестирование) ·
  Р5 [s25] s26–s31 (ревью+безопасность) · Р6 [s32] s33–s34 (доставка·ops·docs) ·
  Р7 [s35] s36–s40 (обобщение).
  7 section-dividers: s08 s12 s16 s22 s25 s32 s35 (display positions shift +4
  from s22 onward due to #162 insert; функция-имена НЕ переименованы). Keystone = s05.
  Hero required = s01 (METR chart) + s40 (closing photo, display shifts +4). s11 iceberg illustration.

Build: python3 build_lec04_v4.py  → lec-04.pptx (50 slides monotonic display
order; internal function names keep original v4.1 numbering — see builders
list below for the actual insertion point of s20b–s20e / s11b / s20f /
s25b–s25c / s35b).
Slide builders split into band modules (slides_band1..4.py), each importing
from _helpers.py. Charts pre-generated via gen_charts_v4.py.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _helpers import setup_pres, ROOT, page_number  # noqa: E402
import slides_band1 as b1  # noqa: E402
import slides_band2 as b2  # noqa: E402
import slides_band3 as b3  # noqa: E402
import slides_band4 as b4  # noqa: E402

OUT = ROOT / "rendered/lec-04.pptx"


def main():
    p = setup_pres()
    # v4.1 (#265/#266/#267/#268/#269): base 41 slides.
    # s05 = NEW foundations (b1.s05f); s06 = keystone phase-cycle (b1.s06k);
    # all subsequent builders keep their original function names but their
    # DISPLAY position shifts +1. load_notes keys already shifted to match the
    # renumbered slides/*.md (s05-foundations, s06-keystone, …, s41-bridge-qa).
    # v4.2 (#162): +4 builders b2.s20b/s20c/s20d/s20e inserted between
    # b2.s19 (display s20, harness-gate) and b2.s20 (display s21, 70%-problem).
    # These 4 new functions are named to match their OWN display id directly
    # (s20b..s20e) — they are new slides, not subject to the historical v4.1
    # -1 shift that the rest of the file's function names carry.
    builders = []
    # display s01–s10 (+1 from v4.4: b1.s03b inserted, see below)
    # v4.5 (#162 round 6, block 5): b1.s03b (общая статистика по отрасли —
    # Stack Overflow 2025 / DORA 2025 adoption + trust gap) inserted between
    # b1.s03 (мост из Модуля 1) and b1.s04 (центральный вопрос). Owner note:
    # «и в начале презы надо добавить общую статистику по отрасли». Every
    # display position from b1.s04 onward shifts +1 → 58 slides.
    builders += [b1.s01, b1.s02, b1.s03,
                 b1.s03b,                                    # NEW (r6 b5)
                 b1.s04, b1.s05f,                            # s05 foundations
                 b1.s06k,                                    # s06 keystone
                 b1.s06, b1.s07, b1.s08, b1.s09]             # s07..s10
    builders += [b1.s09b]                                    # NEW (r3): AWS Kiro vs 847-deployments
    # display s11–s20
    builders += [b1.s10,                                     # s11
                 b1.s11b,                                    # NEW (r2): §1.2b requirements viz
                 b2.s11, b2.s12, b2.s13, b2.s14,             # s12..s15
                 b2.s14b,                                     # NEW (r6 b1): конкретные артефакты 4 практик
                 b2.s15,                                      # s16
                 b2.s16, b2.s17]                              # s17..s18
    builders += [b2.s17b]                                     # NEW (r3): Gemini CLI self-review
    builders += [b2.s18]                                      # s19 (persistent-memory, reworked title/framing)
    builders += [b2.s18b]                                     # NEW (r3): curation honest limits
    builders += [b2.s19]                                      # s20 (harness-gate)
    # display s20b/s20c/s20e/s20d/s20g/s20f (NEW #162): Skills · MCP ·
    # task-logging · git-конвенции · secrets(Register) · git worktree.
    # ORDER SWAP (r3 QA-fix): task-logging (s20e) now presents BEFORE
    # git-conventions (s20d), matching book's round-3 §3.3d↔§3.3e reorder
    # (§3.3d is now task-logging, §3.3e is now git-conventions). File/slide
    # ids s20d/s20e themselves are NOT renamed — only presentation order.
    builders += [b2.s20b, b2.s20c,
                 b2.s20e,                                     # task-logging (now §3.3d) — presents first
                 b2.s20d,                                     # git-conventions (now §3.3e) — presents second
                 b2.s20g,                                     # NEW (r3): secrets/.env — Register case
                 b2.s20f]                                     # git worktree
    # display s21–s30 (old "s21" comment kept as historical marker; actual
    # display position shifted further by r3 inserts above)
    builders += [b2.s20,                                     # 70%-проблема (+2026 GitClear addition)
                 # b3.s21 (anti-hype benchmarks) REMOVED — round 6 block 3
                 # (owner: «слайд 32 — лишний, убрать»). SWE-bench Verified/Pro
                 # разрыв введён в Лекции 3; вендор-скепсис держат s20 (70%-
                 # проблема) и s37/s38 (триангуляция, risk-triad).
                 b3.s22, b3.s23, b3.s24,                     # testing..review
                 b3.s25b, b3.s25c,                            # NEW (r2): §4.4 BDD/trunk-based · §4.5 test tooling (rebuilt r3)
                 b3.s25,
                 b3.s26, b3.s27, b3.s28]                       # review..security(complacency)
    builders += [b3.s29]                                       # security (vulnerable+false-confidence)
    builders += [b3.s30b]                                      # NEW (r3): Amazon Q wiper (3rd supply-chain class)
    # display s31–s41 (shifted further in final display order)
    builders += [b3.s30,
                 b4.s31, b4.s32]
    builders += [b4.s33]                                       # cicd-ops (risk-calibrated gate fix)
    builders += [b4.s33b]                                      # NEW (r3): BT Group/Azure Triangle vs IaC-insecurity
    builders += [b4.s34,
                 b4.s35b,                                     # NEW (r2): §6.3 docs tooling
                 b4.s35,
                 b4.s36]                                        # synthesis matrix (vendor column removed)
    builders += [b4.s37]                                       # triangulation (+2026 GitClear addition)
    builders += [b4.s37b]                                      # NEW (r3): Uber + Kiro dual-register bridge
    builders += [b4.s38, b4.s39, b4.s40]

    assert len(builders) == 58, f"expected 58 builders, got {len(builders)}"
    for fn in builders:
        fn(p)

    # Stamp a page number «N / 56» on every slide (bottom-right, muted). Done in
    # the assembler so all 56 slides carry it without touching per-slide builders.
    total = len(builders)
    for i, slide in enumerate(p.slides, start=1):
        page_number(slide, i, total)

    n = len(p.slides.__iter__.__self__._sldIdLst)
    assert n == 58, f"expected 58 slides, got {n}"
    p.save(str(OUT))
    print(f"saved {OUT} — {n} slides")


if __name__ == "__main__":
    main()
