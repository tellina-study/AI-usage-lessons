# Phase 3 SYNTHESIS — chapter v1 Лекции 4 «AI в разработке ПО»

**Дата:** 2026-05-16 · **Issue:** #99 · **Артефакт:** `library/lectures/lec-04/{chapter.md,chapter-part2.md,chapter-part3.md}` v1.

## Сводный вердикт: **APPROVE-WITH-POLISH** (0 P0 у всех 3)

| Критик | Verdict | P0 | P1 | Ключевое |
|---|---|---|---|---|
| methodology-critic | APPROVE-WITH-POLISH | 0 | 3 | strict-in честно **~69%** (выше заявл. 62%); распределён 57–94% по 6 разделам, single-cluster снят; LO1/4/7 pass; Forbidden 0 |
| fact-checker | APPROVE-WITH-POLISH | 0 | 4 | ~35 фактов verified, 0 инверсий/мисквотов; 4 citation-ID/число ошибки (каскад из research) |
| reader-text-only | APPROVE-WITH-POLISH | 0 | 0 structural | каркас сильный; A→D-прогрессия — сильнейшая часть; 0 структурных блокеров; всё inline-fixable |

Условие «critics APPROVE-WITH-POLISH/CLEAN, 0 P0» — выполнено. Правки точечные, без переписывания нарратива.

## Phase 4 fix-list (book-editor)

**P1 (обязательно):**
1. **§0.3 битые указатели возврата** [meth-P1-1 + reader]: «§4.13»→**§4.4+§4.7**, «§5.3»→**§5.2**. + cascade-grep ВСЕХ несуществующих §-ссылок по 3 файлам, исправить.
2. **Inline-define до первого использования** [meth-P1-3 + reader-P1]: `supply-chain` (§4.5, до §4.6); усилить мини-глосс `vibe-coding` (§1.5, до строгого §5.1); `least-privilege` (§3.4 уровень D); `essential/accidental` (inline-скобка §1.4, до Brooks §5.2); `confused-deputy` (глосс в Replit-кульминации §3).
3. **slopsquatting число** [fact-P1-1]: «756 000»→**«576 000»** сэмплов (§4.6) + **синхрон research**: `notes/research/lecture-4/sources.md` #10 + `failures-and-limitations.md` #6 (та же транспозиция — иначе chapter↔research разойдётся).
4. **arXiv NYU Pearce** [fact-P1-2]: `arXiv:2310.02059`→**`arXiv:2108.09293`** («Asleep at the Keyboard?», Pearce et al., ~40%/89 сценариев) — §4.4 + Источники + синхрон `sources.md` #36. (2310.02059 = чужая статья Fu et al.)
5. **arXiv GraphRAG+TDD** [fact-P1-3 + meth-P1-2]: `arXiv:2603.17973` указывает на «TDAD» (про регрессии), НЕ «GraphRAG+TDD −72/−81%». §5.1: **вести структурным аргументом «TDD = паттерн §1.5 (тест=исполняемая спека для LLM)»**, конкретные −72/−81% снять или пометить illustrative без ложной attribution к 2603.17973 (демота числа).
6. **Название статьи Anthropic** [fact-P1-4]: →**«How AI Impacts Skill Formation»** (Shen & Tamkin, arXiv:2601.20245) в 3 местах (§6.3, Источники, Дальнейшее чтение). Числа (n=52/−17%/Trio) верны — не трогать.

**P2 (тот же проход):**
- frontmatter strict-in 62→**69%** (consistency-checker downstream) [meth-P2-4].
- Meta TestGen числа (32%/5,3%; 2,4%/15%) — атрибутировать **arXiv:2506.02954** (не 2501.12862) [fact-P2-1] + синхрон sources.md #64.
- Copilot «+55%»→«~56% (55,8%)» [fact-P2-2].

**Cascade-flag:** P1-3/P1-4/P2-1 — синхронизировать research-файлы при правке (иначе следующая сверка chapter↔research разойдётся). Research-файлы committed — правка в scope (citation-ошибка в самом research).

**Не фиксить (намеренно):** late-2025 METR reversal в deep-dive (framing подтверждён корректным fact-checker'ом); `[VFY-day-of]`/`[FACT-CHECK]` метки адекватны; Kiro/PocketOS/curl recent — corroborate day-of (метки на месте).

**После правок:** status `draft→reviewed`, version `v1→v1.1`, Changelog в chapter.md. → Phase 4.5 pre-gate (mode=chapter) → USER GATE A.
