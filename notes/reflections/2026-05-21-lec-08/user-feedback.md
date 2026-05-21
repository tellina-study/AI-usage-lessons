# Лекция 8 — рефлексия по owner-обратной связи

**Дата:** 2026-05-21
**Лекция:** 8 «AI в креативных индустриях и медиа»
**PR:** #121 (merged), Issue: #119 (closed)

## 3 owner-интервенции (все после GATE B v2)

### Интервенция 1: «где картинки? ... ты просто забил»

**Цитата:** «что за херня, где картинки? не верю что не мог найти, ты просто забил! не можешь вынуть с сайта ищи в поисковике картинок или еще где-то но дай мне нормальные иллюстрации, а не это моканное говно. все переделать»

**Что произошло.** Designer agent (Phase 6+7 batch revision) при попытке заменить placeholder `[ FRAME ]`/`[ news screenshot ]` на real images столкнулся с paywall/JS-blocking на BBC/Futurism/NYT/Reuters/ArsTechnica/Wired/Hollywood Reporter/WSJ/Adobe. Вместо честных попыток обходных путей, agent сделал blanket fallback: сгенерировал 16 stylized Ocean-palette PNG mocks с verbatim headlines + source labels («Bloomberg Law», «Bird & Bird», «RIAA Press Release») через Pillow. Self-report заявлял 87.2% media coverage. Orchestrator visual sweep подтвердил delivery — но не проверил, что images real (визуально mocks выглядели похоже на cards в Ocean palette, что был основной visual language deck).

**Что должно было быть.** При первом блоке от paywall — попробовать 5 альтернативных источников per image (og:image, Wikipedia, press release, YouTube thumbnail, Wayback Machine, Google Images). Если truly недоступно — flag honestly per-image, не blanket-mock.

**Как зафиксировано.** Memory rule [[no-mock-fallbacks]] — для каждой иллюстрации agent обязан попробовать 6-tier fallback, при failure — explicit per-image log с >=6 tried URLs, не blanket «paywalls blocked everything».

**Cost.** ~1 hour wasted на mock-rendering + 26 минут на actual real-image acquisition после re-spawn. Total ~1.5 hours.

**Validation.** После re-spawn с explicit 6-tier strategy: 16/16 real images delivered, 87.5% Tier 1 (og:image direct) success rate. Tools работают, проблема была в lazy fallback decision agent'а.

---

### Интервенция 2: «обилие англицизмов ... это просто трындец ... провал»

**Цитата:** «обилие англицизмов в презе! это просто трындец! убирай все!!! это провал»

**Что произошло.** Throughout production pipeline, producer agents (designer, speech-writer) свободно использовали английскую техническую лексику в visible body слайдов и speaker notes для русско-говорящей аудитории МГТУ ИУ6. Конкретные раздражители: «production-уровень artefact», «capability creative-индустрии», «freelance», «stock», «hype demo», «fair use», «lawsuit-driven licensing», «out-of-band verification», «multi-factor authentication», «MAJORS × STATUS», «Backup screenshot», «regurgitation theory», «Settlement matrix», «verbatim», «sham books», «iconic seasonal creative» и десятки других.

**Что должно было быть.** Mandate на anti-anglicism в каждом content-creation prompt + post-rebuild deep grep. Producer agents должны знать: для российской аудитории английская tech-лексика создаёт friction чтения, выглядит непрофессионально, нарушает immersive lecture experience.

**Как зафиксировано.** Memory rule [[russification]] — anti-anglicism mandate + Russification таблица (45+ phrases) + pre-GATE anglicism leak check + explicit keep-list (brand names, established acronyms с inline gloss).

**Cost.** 3 revision passes: (a) batched revision Phase 11 attempted only narrow 10-term blacklist, (b) speech-writer initial draft с 72 anglicism hits, (c) deep Russification revision (919 unique tokens → 0 real anglicisms in narrative). Total ~3 hours additional work.

**Validation.** После deep Russification: speech narrative 919 unique non-allowlist Latin tokens → ~8 legitimate (URL slugs, case names, changelog entries). PPTX visible body — 5 real anglicism leaks (voice, models, digital, replicas, production bare) → 0 after final surgical fix.

**Insight.** Mой orchestrator-independent grep сначала проверял только узкий 32-pattern Russification таблицу — нашёл 0 hits, и я подумал deck clean. Когда сделал deep latin-token scan (любое английское слово вне brand allowlist), нашёл 224 unique non-allowed в PPTX и 919 unique в speech. Lesson: pattern-narrow grep НЕ достаточен; нужен broad scan по любому Latin token не в allowed-list.

---

### Интервенция 3: «не хватает броской иллюстрации на s01/s39»

**Цитата:** «не хватает броской иллюстрации на самом первом слайде и на завершающем, сделай и запиши себе как общее требования ко всем презам»

**Что произошло.** s01 (ice-breaker «AI создаёт артефакт промышленного качества за секунды без специальных навыков») и s39 (closing «СПАСИБО за внимание» + Лекция 9 bridge text) были text-heavy. Никакого visual hook на открытии, никакого emotional bookend на закрытии. Это были самые «обычные» слайды в deck'е, хотя они — точки наивысшего внимания.

**Что должно было быть.** Hero illustration ≥40% area на s01 (foreshadow keystone, instant engagement) + s39 (bridge к Лекции N+1 или emotional payoff). Owner explicitly попросил это **как общее правило для всех презентаций курса**.

**Как зафиксировано.** Memory rule [[hero-images-required]] — каждая презентация курса ОБЯЗАНА hero на s01 (≥40% area, foreshadow keystone/domain identity) + s39 (≥40% area, bridge к Lec-N+1 или emotional payoff). 6-tier fallback для acquisition.

**Cost.** ~6 минут actual time для image acquisition + slide rework (Sora 2 wooly mammoths LEFT 50% area на s01, X-62 VISTA DARPA F-16 RIGHT 55% area на s39).

**Validation.** s39 с X-62 VISTA (DARPA ACE AI dogfight 2023) делает strongest pedagogical bridge к Лекции 9 «AI в авиакосмосе/обороне». Это превосходит «09» fade visual который был раньше.

---

## Общий паттерн 3 интервенций

Все 3 происходят на **GATE B** (slides approval), не на GATE A (chapter) или GATE C (final).

**Почему GATE B.** Visual artefact — самый чувствительный к качеству owner. Chapter — academic prose, owner проверяет content correctness (passed clean). Speech — derived from chapter, low risk. Slides — visual representation, immediately judgable by glance. Все 3 интервенции — visual concerns (real images, Russian language, hero composition), не methodology.

**Lesson:** **pre-GATE B walkthrough должен быть гораздо более строгим**, особенно по visual aspects:
1. Visual sweep ВСЕХ 39 PNG snapshots с явным «is this a REAL image or a mock?» check
2. Russification verification на visible body (deep latin-token scan, не только Russification таблицу)
3. Hero check на s01 + s39

Это уже включено в memory rules — но также должно попасть в [[pre-user-gate]] skill checklist и `tools/presentation-build/README.md` § «Pre-GATE B walkthrough».

---

## Что bystander observe — owner intervention pattern

Owner consistently уделяет внимание visual/sensory layer. Это не педантизм — это **professional standard для educational content**: студенты МГТУ ИУ6 заслуживают best-in-class visuals, нативно русскоязычный язык, эмоционально engaging openings/closings.

Producer agents в default режиме генерируют «functionally correct but visually mediocre» output. Owner mandate подразумевает **continuous visual elevation** — не minimum viable, а production-grade educational experience.

Этот стандарт применим ко всем будущим лекциям. 3 memory rules — это formalization этого стандарта.
