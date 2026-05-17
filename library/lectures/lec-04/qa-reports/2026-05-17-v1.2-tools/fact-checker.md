# Fact-Checker Report — Re-QA delta Лекции 4 (v1.2 tools-addition, Решение #102) — 2026-05-17

VERDICT: APPROVE-WITH-POLISH

**Scope:** delta-проверка tool-контента, добавленного по Решению #102 во ВСЕ 3 артефакта — chapter v1.1→**v1.2** (§0.4 mode≠brand, §1.2[s06], §1.3[s07], §2.2[s12], §3.2[s15], §5.4[s28], Deep-dive box 5, В6, Источники 83→88); deck→**v3.3** (рендер `lec-04.pptx`, врезки «Инструменты 2026» на PPTX-слайдах 7/8/13/16 = deck s06/s07/s12/s15); speech v1.1→**v1.2** (устные тул-фрагменты s06/s07/s12/s15 + mode≠brand s03 + day-of preflight). Свежесть = высший приоритет (урок ARC-AGI).

**Источники verification:** research-файл `notes/research/lecture-4/tools-landscape.md` «2026-05-17 update» + независимая live-веб-верификация 2026-05-17 (JetBrains blog, github.blog, danilchenko.dev, The Register, swebench.com/marc0.dev, labs.scale.com, arXiv 2506.17208/2506.12286, Cognition/Devin).

---

## Severity counts

- **P0 (false fact / broken citation / direction inversion / phantom / misquote):** 0
- **P1 (missing source / suspicious number / freshness expired / book-first нарушение):** 2
- **P2 (cite format / minor / spec-hygiene):** 3

---

## Tool-маппинг A/B/C/D — verified (book-first == research == live-web)

| Уровень | Chapter v1.2 | Deck v3.3 (PPTX) | Speech v1.2 | Research «2026-05-17» | Live-web 2026-05-17 | Verdict |
|---|---|---|---|---|---|---|
| **A** автодополнение | §1.2 [s06]: Copilot ghost-text / Cursor Tab / JetBrains full-line·AI Assistant | PPTX s7: «Copilot ghost-text / Cursor Tab / JetBrains AI» | s06: «Copilot ghost-text, Cursor Tab, ассистент JetBrains» | A = Copilot inline/tab + Cursor Tab + JetBrains line-completion | JetBrains: Copilot 29%/76% (stalled); JetBrains AI 9%+Junie 5% | **VERIFIED** ✓ |
| **B** мелкие задачи (чат/inline) | §1.3 [s07]: ChatGPT/Claude/Gemini чат + Copilot Chat / Cursor Cmd-K | PPTX s8: «ChatGPT-чат / Copilot Chat / Cursor Cmd-K» | s07: «ChatGPT, Claude, Gemini … Copilot Chat, Cursor Cmd-K» | B = ChatGPT-as-chat (28%) + Copilot/Cursor inline-chat + Claude/Gemini чат | ChatGPT-чат массовый (SO: OpenAI-чат-модели доминируют) | **VERIFIED** ✓ |
| **C** кодинг-агент | §2.2 [s12]: Claude Code / Cursor Composer·Agent / Codex CLI·Cloud | PPTX s13: «Claude Code / Cursor Composer / Codex CLI» | s12: «Claude Code, Cursor Composer, Codex CLI» | C = Claude Code (6×) + Cursor Composer ($2B ARR) + Codex CLI (3%) | Claude Code 18% (24% US/CA), CSAT 91%/NPS 54, 6×; Cursor 18% | **VERIFIED** ✓ |
| **D** оркестратор+трекер | §3.2 [s15]: Copilot coding agent GA / Devin 2.0 / Jules / Codex Cloud; мульти-агент emerging | PPTX s16: «Copilot agent / Devin 2.0 / Jules / Codex Cloud» | s15: «Copilot coding agent, Devin два-ноль, Jules, Codex Cloud» | D = Copilot agent GA + Devin 2.0 + Jules + Codex Cloud; multi-agent emerging | Copilot coding agent GA (github.blog #159068); 17M PR/5 outages/kill switch (danilchenko 2026-04-11, Register 2026-02-03) | **VERIFIED** ✓ |

**0 фантомов.** Каждый инструмент/вендор/режим во всех 3 артефактах присутствует в research-файле «2026-05-17 update». Маппинг точно соответствует §0.4-правилу «режим, не бренд»: Copilot показан в A+B+C+D, Cursor в A+B+C, Claude Code в C+D, Codex в C+D — корректно атрибутировано как режим, не дублирование-ошибка.

---

## Book-first: deck/speech derive == chapter v1.2 (0 утверждений вне главы)

**deck v3.3 (rendered `lec-04.pptx`, PPTX-слайды 7/8/13/16):** все «Инструменты 2026» врезки + speaker notes — прямой derive из chapter v1.2 §1.2/§1.3/§2.2/§3.2. Текст врезок hardcoded в `rendered/build_lec04.py` (строки 885/966/1203/1333) — дословно сверен с §1.2/§1.3/§2.2/§3.2, расхождений в утверждениях НЕТ. Adoption-строки = «направление», anti-hype-оговорки = главы. **0 фактов вне chapter v1.2.**

**speech v1.2 (s06 l.139, s07 l.153, s12 l.233, s15 l.279, mode≠brand s03 l.83, landscape s28 l.479):** устные тул-фрагменты — устная развёртка chapter v1.2, не дубль и не новые факты. «Примерно в десятой части задач решение есть прямо в тексте issue, часть прошедших патчей некорректна» (s12 l.233) = §2.2 / Источники arXiv:2506.17208. «17 миллионов PR — 5 отказов и аварийный выключатель» (s15 l.279) = §3.2. **0 фактов вне chapter v1.2.**

**Вывод:** book-first каскад соблюдён (chapter → build_lec04.py/PPTX → speech). Нарушений P0/P1 по book-first нет.

---

## `[VFY-day-of]` freshness-дисциплина — соблюдена (с 2 уточнениями ниже)

**Видимый слой deck (PPTX 7/8/13/16) — точных волатильных тул-чисел НЕТ.** Только имена инструментов + направление словами («рост лидера остановился», «самый массовый», «самый быстрорастущий уровень», «emerging, не мейнстрим»). Adoption %, ARR, число подписчиков, «most-loved 46%», 6×-множитель — НЕ на видимом слое. Решение #100/#9 соблюдено, рецидива Л1 ARC-AGI нет.

**Видимый слой speech — точных волатильных тул-чисел НЕТ.** «Номер один по охвату», «самый быстрорастущий», «emerging» — направление. Числа `[VFY-day-of]` вынесены в day-of preflight (speech l.27–30).

**chapter v1.2 + speech preflight — `[VFY-day-of]` проставлены** с источником и cadence: §1.2 (Copilot adoption — JetBrains+ideaplan quarterly), §1.3 (ChatGPT-доля — annual), §2.2 (Claude Code 6×/CSAT quarterly; SWE-bench дыры — направление стабильно/лидерборд weekly), §3.2 (Devin overclaim — stepchange/theplanettools; Copilot agent 17M/5/kill — event-dated), §5.4 + Deep-dive box 5 (вся картина quarterly/monthly). speech l.27–30 — отдельный day-of preflight-блок с источниками и «обновить число устно, направление не менять».

**Единственное точное benchmark-число на видимом слое — SWE-bench Verified 88,7% / Pro 64,3% (PPTX s13).** Это НЕ новый tool-факт Решения #102 — это v1.1-факт §2.2, уже одобренный GATE B. На видимом слое footer-flag присутствует («лидеры меняются почти еженедельно; цифра без среза и без даты не информативна»), в notes — устный ARC-AGI-disclaimer, в chapter — жёсткий `[VFY-day-of: …ОБЯЗАТЕЛЬНО переверить в день лекции]`, в speech preflight l.29 — «weekly volatility, обязательно переверить swebench.com/labs.scale.com». Дисциплина соблюдена; см. P1-2 (freshness drift уже наблюдается).

---

## DISPUTED / FALSE facts

**Нет.** 0 P0. Все tool-факты подтверждены research + независимой live-веб-верификацией 2026-05-17.

---

## Anti-hype формулировки — НЕ инвертированы (verified)

| Утверждение | Chapter/Deck/Speech | Корректность | Live-web |
|---|---|---|---|
| «Copilot — №1 по охвату, рост встал ≠ умер» | §1.2/§5.4/box5; PPTX s7 «стагнация ≠ умер»; speech l.139 «встал ≠ умер» | ✓ стагнация, не смерть; «теряет лидерство по динамике» | JetBrains: «growth … has stalled since last year», 29%/76% всё ещё #1 ✓ |
| «Devin fully-autonomous = overclaim» | §3.2; PPTX s16 «overclaim, не факт»; speech l.279 «растиражированный overclaim» | ✓ vendor-claim, не measured fact; frontier+scaffolding обгоняют | Web: reproducibility concerns, human oversight needed, scaffolded frontier > Devin ✓ |
| «SWE-bench дыряв (~10% issue с решением, ~28% некорректных патчей)» | §2.2/box2/box5; speech l.233 «⅒ задач решение в тексте, часть некорректна» | ✓ направление верно, не overclaim; flagged weekly | arXiv:2506.12286 SWE-Bench Illusion (memorization); 2506.17208 leaderboard profiling ✓ направление |
| «чат-LLM строго B даже при агентном маркетинге» | §1.3; PPTX s8; speech l.153 «строго B, петля copy-paste» | ✓ не повышен до C без обвязки | research §гранич.4 (чат-LLM строго B) ✓ |
| «маргинализированы ≠ мертвы, LOW confidence» | §5.4/box5 «не фигурируют в свежих топ-данных — НЕ мертвы (нет decline-чисел)» | ✓ honest, не overclaim в сторону «умерли» | research §5/6 (LOW confidence, не overclaim) ✓ |
| «mode≠brand» | §0.4; В6; speech l.83 «уровень — режим, а не бренд» | ✓ режим определяет уровень, не логотип | research «граничные случаи» п.1 ✓ |

**Смысл сохранён, не overclaim ни в одну сторону.** Инверсий anti-hype НЕТ (ни «Copilot умер», ни «Devin реально автономен», ни «SWE-bench доказывает автономию», ни «инструменты мертвы»).

---

## v1.1-факты НЕ регрессировали (verified)

Все ключевые v1.1-числа присутствуют и не изменены добавлением тулов (grep-сверка по 3 файлам chapter):

- METR: «на 19% больше» / прогноз «примерно на 24%» / вера «примерно на 20%» / «+19% времени»; arXiv:2507.09089; n=16; 246 задач ✓
- Copilot RCT: «примерно на 56% (точно — 55,8%)»; arXiv:2302.06590; CI[21,89] ✓
- SWE-bench: Verified 88,7% / Opus 4.7 87,6% / GPT-5.3-Codex 85,0% / Pro 64,3% ✓
- GitClear: 211 миллионов LOC; клоны 8,3→12,3%; рефакторинг 24,1→9,5%; churn 5,5→7,9% ✓
- SO 2025: 66% «почти правильно» / 45,2% отладка дольше ✓
- NYU: ~40% (arXiv:2108.09293, Pearce et al.); Schreiber 12,1% CWE (arXiv:2510.26103); Stanford dl.acm.org/3716848 ✓
- slopsquatting: 576 000 сэмплов / ~20% / 43% / 58% / open ~21,7% / комм ~5,2% ✓
- Anthropic: n=52 / −17% / «How AI Impacts Skill Formation» (arXiv:2601.20245) ✓
- Replit: 95 из 100; >1200 руководителей / >1190 компаний; AIID cite/1152 ✓
- Meta TestGen: 32% vs 5,3% / 2,4% vs 15%; arXiv:2506.02954 (gen) / 2501.12862 (TestGen-LLM) ✓
- curl: >15%→<5%; ×8; сворачивание 2026-02-01 ✓
- CamoLeak: CVE-2025-59145, CVSS 9.6; Lovable CVE-2025-48757 ✓

**0 регрессий.** Tool-добавление было strictly additive (changelog v1.2 подтверждает: «финализированный контент v1.1 НЕ менялся»).

---

## Источники с датами — атрибутированы, даты верны

Новые/расширенные строки в Источники (chapter-part3.md l.351–355), references 83→88:

- **JetBrains «Which AI Coding Tools Do Developers Actually Use at Work?» 2026-04, n>10k** — ✓ существует (blog.jetbrains.com/research/2026/04/…), числа дословно совпадают с live-web (Copilot 29%/76% stalled; Claude Code 18%/24% US-CA, CSAT 91%/NPS 54, 6×; Cursor 18%; JetBrains AI 9%+Junie 5%). quarterly. **VERIFIED**
- **ideaplan.io «AI Coding Assistant Market Share 2026»** — Copilot 4,7M/+75% YoY, $12,8B, сегмент-сплит. MEDIUM (market-research), quarterly. Атрибуция корректна (числа НЕ на видимом слое, `[VFY-day-of]`). **VERIFIED (MEDIUM tier правильно помечен)**
- **danilchenko.dev «GitHub's AI Agent Problem» 2026-04 + github.blog/community#159068** — Copilot coding agent GA; 17M PR / 5 outages / kill switch. ✓ live-web подтвердил (danilchenko.dev 2026-04-11; The Register 2026-02-03 kill-switch; github.blog changelog GA). event-dated. **VERIFIED**
- **theplanettools.ai / stepchange-blog.ghost.io 2026** — multi-agent волна февр-2026; Devin consistency varies; net +8–13% vs «+50%». ✓ направление подтверждено live-web (Devin overclaim, scaffolded frontier > Devin). monthly/quarterly. **VERIFIED (направление)**
- **arXiv:2506.17208 + cognition.ai SWE-bench tech report** — ✓ arXiv:2506.17208 = «Dissecting the SWE-Bench Leaderboards» (Martinez & Franch) реально существует. Специфичные числа (~10% / ~28,4%) — из broader SWE-bench critique (combined w/ cognition.ai report + arXiv:2506.12286 «SWE-Bench Illusion»). Направление (SWE-bench как proof-of-autonomy дыряв) solidly verified. lederboard weekly / дыры stable. **VERIFIED (направление; точные доли flagged re-verify — корректно)**
- **Gartner «Hype Cycle for Agentic AI» 2026** — ~17% deployed, Peak of Inflated Expectations. `[FACT-CHECK annual]` помечен. Не на видимом слое. **NEEDS-CITATION → mitigated (помечен FACT-CHECK, annual, не несущий)**

---

## NEEDS-CITATION / freshness items

### P1-1 — Gartner Hype Cycle for Agentic AI: точный отчёт не верифицирован независимо
**Quote (Deep-dive box 5):** «~17% организаций развернули агентов; "fully autonomous" — Peak of Inflated Expectations»
**Источник:** «Gartner (2026). Hype Cycle for Agentic AI. gartner.com» — помечен `[FACT-CHECK annual]`.
**Issue:** Gartner-отчёт за paywall, конкретный «~17%» независимо не подтверждён в этой сессии (Gartner press-release не зачитан). Направление (agentic на Peak of Inflated Expectations) — общеизвестно и правдоподобно, но точное число «~17%» — single-source.
**Mitigation present:** число НЕ на видимом слое (deck/speech), `[FACT-CHECK]` стоит, annual cadence, не несущий тезис (несущий — anti-hype, не цифра).
**Recommendation:** перед GATE C подтвердить «~17%» по конкретному Gartner press-release/дате ИЛИ смягчить до «меньшинство организаций развернули агентов (Gartner 2026)» без точного числа. **Severity: P1** (missing independent source for specific stat; mitigated, не блокирует show — show-able с caveat).

### P1-2 — Freshness drift УЖЕ наблюдается: SWE-bench Verified/Pro числа дрейфуют быстрее quarterly
**Quote (PPTX s13 видимый + chapter §2.2):** «Verified ~88,7% (GPT-5.5), Opus 4.7 ~87,6%, GPT-5.3-Codex ~85,0%; Pro ~64,3%»
**Источник:** swebench.com / Anthropic-reported апрель 2026.
**Live-web 2026-05-17:** marc0.dev May-2026 подтверждает GPT-5.5 88,7% / Opus 4.7 87,6% / GPT-5.3-Codex 85,0% (точное совпадение). НО BenchLM.ai (2026-05-13) уже показывает Claude Mythos Preview 93,9%; Local AI Master — Sonnet 5 92,4%. SWE-bench **Pro public** (labs.scale.com) сейчас gpt-5.4 xHigh 59,10 (≠ 64,3% Anthropic-reported full Pro — разные датасеты).
**Issue:** числа всё ещё корректны на дату источника, НО лидерборд уже сместился за ~2 недели (новые модели 92–94% Verified). Это точно тот ARC-AGI-сценарий Л1. Direction (Verified ≫ Pro, разрыв ~24 п.п.) — стабильна и НЕ инвертирована.
**Mitigation present:** жёсткий `[VFY-day-of: …ОБЯЗАТЕЛЬНО переверить в день лекции]` в chapter §2.2; deck footer «лидеры меняются почти еженедельно»; speech preflight l.29 «weekly, обязательно переверить swebench.com/labs.scale.com в день лекции, направление ~24 п.п. не менять».
**Recommendation:** **ОБЯЗАТЕЛЬНО** обновить устно Verified-лидера/число и Pro-число в день лекции (см. freshness top-N ниже). Дисциплина в материале корректна — это flag для lecturer pre-flight, не дефект контента. **Severity: P1** (freshness — weekly cadence, days_delta уже > cadence к моменту лекции).

---

## P2 (minor / spec-hygiene)

- **P2-1 — slides/*.md spec не обновлён под v3.3.** `slides/s06|s07|s12|s15-*.md` НЕ содержат «Инструменты 2026» блок, хотя rendered PPTX (binding artifact, через `build_lec04.py` hardcoded) содержит. Binding student-facing артефакт (PPTX) корректен и book-first; рассинхрон только в human-readable spec-файлах. **Recommendation:** синхронизировать slides/*.md с rendered v3.3 ИЛИ задокументировать, что source-of-truth рендера = build_lec04.py + deck.yaml (build header так и говорит). Не блокирует show.
- **P2-2 — speech l.479 (s28) использует старый маркер `[VERIFY-DAY-OF: …]`** вместо канонического `[VFY-day-of: …]` (как в l.27–30 и chapter). Cite-format inconsistency. **Recommendation:** унифицировать на `[VFY-day-of]`.
- **P2-3 — speech l.597 ссылается на «chapter v1.1»** в self-аудите («сверены с chapter v1.1»), хотя источник истины теперь v1.2. Числа не изменились (v1.2 additive), фактически корректно, но версия-ссылка устарела. **Recommendation:** обновить «v1.1»→«v1.2 (v1.1-числа неизменны)».

---

## UNVERIFIABLE

- Точные доли «~10% issue с решением в тексте / ~28,4% некорректных патчей под расширенными тестами» (SWE-bench critique): arXiv:2506.17208 abstract не содержит этих точных цифр; они из combined cognition.ai SWE-bench tech report + broader critique (arXiv:2506.12286 подтверждает memorization-направление: 76%→53% bug-path accuracy off-benchmark). **Направление SOLIDLY VERIFIED**; точные доли — UNVERIFIABLE на abstract-уровне, НО корректно помечены `[VFY-day-of]` и поданы как «примерно/около», не как точные. Не P0/P1 (направление — несущее, цифры хеджированы).

---

## Freshness top-N — ПЕРЕВЕРИТЬ В ДЕНЬ ЛЕКЦИИ (для lecturer pre-flight)

| # | Item | Cadence | Источник для re-verify | Действие |
|---|---|---|---|---|
| 1 | **SWE-bench Verified лидер/число** (s12: 88,7% GPT-5.5) | **weekly** | swebench.com / marc0.dev / BenchLM | Обновить число+лидера устно; разрыв ~24 п.п. и «знакомый ≫ незнакомый» НЕ менять. Уже дрейфует (Mythos 93,9% / Sonnet5 92,4%) |
| 2 | **SWE-bench Pro число** (s12: ~64,3%) | **weekly** | labs.scale.com/leaderboard/swe_bench_pro_public | Обновить устно (Scale public сейчас ~59; Anthropic-reported full Pro ≠ public dataset — указать срез) |
| 3 | **Per-level adoption** (Copilot 29/76, Claude Code 18/6×, Cursor 18) | quarterly | JetBrains «Which AI Coding Tools…» 2026-04 | Сверить; направление (A зрелый/широкий; B массовый; C быстрорастущий; D молодой) не менять — на видимом слое только направление |
| 4 | **Copilot coding agent масштаб** (s15: 17M PR / 5 outages / kill switch) | event-dated | danilchenko.dev / github.blog / githubstatus | Число обновить устно; вывод «гейты обязательны на D» не менять |
| 5 | **Devin SWE-bench-сравнение / overclaim** (s15) | quarterly | stepchange / theplanettools / cognition.ai | Конкретные benchmark-сравнения re-verify; «overclaim» формулировку не менять (направление стабильно) |
| 6 | **Gartner ~17% deployed** (box5) | annual | gartner.com press-release | Подтвердить точное число или смягчить (P1-1) |

> Полная freshness-разметка зеркалит research-файл «Правило волатильности» и speech preflight l.27–30. Все 6 — flagged в материале; ни одно число не подаётся как вечное.

---

## Топ-правок до публикации (GATE C)

1. **P1-2 (обязательно):** в день лекции переверить SWE-bench Verified/Pro (items 1–2 freshness top-N) — числа дрейфуют быстрее quarterly, это точный ARC-AGI-сценарий. Контент-дисциплина корректна; нужен только lecturer pre-flight execute.
2. **P1-1:** подтвердить Gartner «~17%» по конкретному press-release ИЛИ смягчить до «меньшинство организаций» без числа.
3. **P2-1:** синхронизировать `slides/s06|s07|s12|s15-*.md` с rendered v3.3 (или явно зафиксировать build_lec04.py+deck.yaml как render source-of-truth).
4. **P2-2:** унифицировать `[VERIFY-DAY-OF]`→`[VFY-day-of]` в speech l.479.
5. **P2-3:** speech l.597 «chapter v1.1»→«v1.2».

---

## Verdict rationale

**APPROVE-WITH-POLISH** (≤4 P1, фактически 2 P1 — оба mitigated в материале, show-able с known caveats):
- **0 P0** — нет фантом-фактов, нет book-first нарушений, нет инверсии anti-hype, нет misquote, нет точных волатильных тул-чисел на видимом слое.
- **2 P1** — оба смягчены: P1-1 (Gartner single-source, число не на видимом слое, FACT-CHECK помечен); P1-2 (SWE-bench freshness drift — но жёстко flagged `[VFY-day-of]` во всех 3 артефактах + day-of preflight). Ни одно не блокирует показ.
- Tool-маппинг A/B/C/D — полностью verified (research == live-web == book-first deck/speech).
- v1.1-факты — 0 регрессий (additive-only подтверждено).
- Freshness-дисциплина — образцовая (рецидива Л1 ARC-AGI нет: направление словами на видимом слое, числа в day-of preflight).

Не REVISE: P1 < 5 и нет critical missing source (несущие тезисы — anti-hype/направление — verified; хеджированы только волатильные цифры, что корректно). Не APPROVE-CLEAN: P1-2 freshness требует обязательного day-of действия + P1-1 Gartner.
