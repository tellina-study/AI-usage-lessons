# Требования к содержанию слайдов (ENFORCED)

Вынесено из [README.md](README.md) по лимиту в 600 строк. **Нумерация разделов сохранена**:
ссылка вида «`tools/presentation-build/README.md` §5.8» ведёт сюда, в §5.8 — README на этом месте
оставил указатель. Здесь лежат обязательные требования к тому, ЧТО на слайде; в README —
устройство конвейера: архитектура, стек, типы слайдов, визуальный цикл, схема `deck.yaml`,
раскладка каталогов, агенты и антипаттерны.

## 5.6 Visual Loop iteration cap (ENFORCED)

| Cap | Значение | Действие |
|---|---|---|
| **Min** | 3 итерации на слайд (existing Anthropic principle) | Без 3-iter — slide не может быть declared done. |
| **Max** | **7 итераций на слайд (NEW)** | Hard cap. На 7-й итерации если schema всё ещё не проходит §5.5 gate → **escalate**. |

### Escalation (на iter 7 без pass)

Designer **обязан** остановиться и emit escalation report:

```
## ESCALATION — sNN, iter 7
- Subtype: schema_cycle
- Что пробовали: 6 vertical steps → linear flow → 2 USER icons → ...
- Что не сходится: «cycle direction» не считывается студентом за 5 сек
- Гипотеза: schema concept may need redesign — возможно cycle не подходит, нужен dialogue-form
- Recommend: orchestrator + book-editor пересмотреть assertion слайда
```

Escalation = **stop** для designer, **trigger** для orchestrator: пересмотреть концепт слайда (assertion / type / source-of-truth chapter §) **до** продолжения visual loop. Не перерасходовать iteration capacity на неправильный концепт.

### Per-iteration log контракт

Каждая итерация логируется в `rendered/iteration-log.md`:

```
## sNN [iter K]
- Inspected: snapshots/iter{K-1}/sNN.png — что увидел (1-3 фразы)
- Changed: что поменял (per element: shape coords / text / color / icon)
- Re-snapshot: snapshots/iter{K}/sNN.png
- Schema Readability Checklist: PASS / FAIL (что fail)
- 5-Second Test: PASS / FAIL
- Verdict: continue / accept / escalate
```

Без per-iter лога — итерация не считается проведённой.

---

## 5.7 Image acquisition — 6-tier fallback (ENFORCED — [[no-mock-fallbacks]])

**Источник:** рефлексия Лекции 8 (#122), owner feedback «что за херня, где картинки? не верю что не мог найти, ты просто забил! ... все переделать». Designer Phase 6+7 столкнулся с paywall/JS на BBC/Futurism/NYT/Reuters → blanket-fallback 16 stylized Ocean-palette PNG mocks с verbatim headlines. Self-report «87.2% media coverage» прошёл orchestrator visual sweep (mocks выглядели похоже на cards).

**Правило:** для каждого слайда, требующего real visual (case studies, news screenshots, product UI) — designer **не уходит в stylized primitive** без attempting 6-tier acquisition. Mock fallback допустим **только** при documented 6/6 failure в `iteration-log.md`.

### 6-tier acquisition table

| Tier | Источник | Пример URL / запрос | Note |
|---|---|---|---|
| **1. og:image / twitter:card** | `<meta property="og:image">` из article page | `curl -sLA "Mozilla/5.0" https://nytimes.com/...article.html \| grep -oP 'og:image[^>]*content="\K[^"]+'` | Almost always public, обходит paywall на image |
| **2. Wikipedia / Wikimedia Commons** | Free CC infobox / featured images | Commons API `prop=imageinfo&iiurlwidth=960` thumbnails. **PROVEN: Tier 2 = 17/15 в lec-09 production.** | Smaller bypass rate-limits лучше full-size |
| **3. Press release / official pages** | RIAA / OpenAI / DeepMind / NPR / CNN press rooms | `curl -sLA "Mozilla/5.0" https://openai.com/blog/...` + extract `<figure>` / first `<img>` | Usually open, no paywall |
| **4. YouTube thumbnails** | Canonical video frame | `https://img.youtube.com/vi/{VIDEO_ID}/maxresdefault.jpg` | Always public, no auth |
| **5. Wayback Machine** | Archived version of blocked live pages | `https://web.archive.org/web/2024*/https://blocked.com/article` | Bypass JS-block / 404 |
| **6. Google / Bing / DuckDuckGo Images** | Last resort image search | DuckDuckGo HTML scrape (no JS); verify CC license перед use | Manual licensing check |

### Acceptance criteria

- **N/N mocks replaced with real images** — minimum target. Self-report «X% coverage» НЕ trustworthy без per-image source URL.
- **Per-image attempt log** при failure: если subagent flags failure on слайде X — must show ≥6 tried URLs в `iteration-log.md` (не blanket «paywalls blocked everything»).
- **Educational fair use mandate** — для учебных лекций ANY copyrighted image OK с reference attribution. Sub-agent должен явно знать это разрешение.
- **Orchestrator MUST visually verify final result** через PNG snapshot read — designer self-report «13 real images embedded» может означать 13 stylized mocks. Need to LOOK.

### Storage convention

```
library/lectures/lec-NN/assets/screenshots/sNN-real-source.png
library/lectures/lec-NN/assets/screenshots/sNN-real-source.url   # source URL текстом
```

Attribution label visible на slide: source name + date (e.g. «CNN · 16 мая 2024», «Wikimedia · CC-BY-SA»).

### Sample acquisition snippet

```bash
# Tier 1: og:image
URL="https://nytimes.com/2024/05/15/tech/some-article.html"
OG=$(curl -sLA "Mozilla/5.0" "$URL" | grep -oP 'og:image[^>]*content="\K[^"]+' | head -1)
[ -n "$OG" ] && curl -sLo "library/lectures/lec-NN/assets/screenshots/s12-real.jpg" "$OG"

# Tier 2: Wikimedia Commons (через API thumb)
ENTITY="Kelly_McKernan"
curl -sL "https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&pithumbsize=960&titles=$ENTITY" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(list(d['query']['pages'].values())[0].get('thumbnail',{}).get('source',''))" \
  | xargs -I{} curl -sLo "library/lectures/lec-NN/assets/screenshots/s05-real.jpg" "{}"
```

**Cost-of-omission lec-08:** v1 designer reported «87.2% media coverage» при 16 mocks → owner reject «провал» → ~1.5h cycle wasted. Lec-09 v2 acquisition после re-spawn — 87.5% Tier 1 success, 17/15 real photos.

**Связанные правила:** [[no-mock-fallbacks]], [[hero-images-required]], `presentation-designer.md` § ENFORCED — 6-tier real image acquisition.

---

## 5.8 Russification — anti-anglicism mandate (ENFORCED — [[russification]])

**Источник:** рефлексия Лекции 8 (#122), owner feedback «обилие англицизмов в презе! это просто трындец! убирай все!!! это провал». Producer agents (designer + speech-writer) свободно использовали English tech-лексику в visible body для RU-аудитории. Pattern-narrow grep (32 patterns) показал 0-72 hits; **deep latin-token scan** (любое English word вне brand allowlist) показал 224 unique в PPTX и 919 unique в speech.

**Правило:** все content words в visible slide body + speaker notes + chapter prose — на русском. Whitelisted: brand names, established acronyms с inline gloss при первом упоминании, mode names (text-to-video, text-to-image), legal jurisdiction terms (fair use, CDPA, DMCA — с RU расшифровкой).

### Russification table (45+ canonical replacements)

| English | Russian |
|---|---|
| production use / production-уровень | промышленное применение |
| capability | возможность / функция |
| hype demo | демо для хайпа / реклама без production-готовности |
| freelance | фрилансер / независимый исполнитель |
| stock photo | сток-фотография (русифицировано) |
| out-of-band verification | проверка через независимый канал |
| multi-factor authentication | многофакторная аутентификация |
| lawsuit-driven licensing | лицензирование под давлением исков |
| Settlement matrix | таблица урегулирований |
| MAJORS × STATUS | КРУПНЫЕ ЛЕЙБЛЫ × СТАТУС |
| regurgitation theory | теория воспроизведения тренировочных данных |
| verbatim | дословно |
| Trial chip / Pending | Суд / Ожидание |
| Backup screenshot | резервный скриншот |
| character consistency | сохранение персонажа между генерациями |
| voice cloning | клонирование голоса |
| model collapse / Model Autophagy Disorder | коллапс модели (MAD) |
| identity proof | подтверждение личности |
| likeness rights | права на использование образа |
| predictive maintenance | прогностическое обслуживание |
| ground truth | эталонная разметка |
| automation bias | склонность доверять автомату |
| multi-sensor fusion | слияние нескольких сенсоров |
| decision-support | поддержка принятия решений |
| accuracy (метрика) | точность |
| big-tech | большие ИИ-компании |
| edge case | краевой случай |
| safety-critical | критичный к безопасности |
| life-and-death | жизненно важный / решающий жизни и смерти |
| mental model | модель в голове |
| takeaway | вывод / то, что унести |
| wingman / supervises / executes | ведомый / наблюдает / исполняет |
| callout | акцент / выделение |
| adversarial | состязательный |
| use case | сценарий использования |
| best practice | проверенный подход / лучшая практика |
| deploy / deployment | развёртывание |
| insight | вывод / находка / наблюдение |
| tradeoff | компромисс |
| baseline | базовый уровень / отправная точка |
| stack | стек технологий |
| review | обзор / проверка |
| override | перекрытие / отмена |
| self-contained | самодостаточный |
| pipeline | конвейер / последовательность |

### Keep-list (whitelisted — НЕ заменять)

- **Brand names** без хорошего перевода: Sora 2, Midjourney, Suno, ElevenLabs, Adobe Firefly, OpenAI, Anthropic, NYT, Bloomberg, Reuters, BBC, RIAA.
- **Established acronyms** с **inline расшифровкой при первом появлении**: NYT (New York Times), RIAA (Recording Industry Association of America), DMCA, CDPA, GDPR, API, ML, GenAI, LLM, RAG, MCP, OODA, HITL, LAWS.
- **Mode/method names** без принятого русского эквивалента: text-to-video, text-to-image, prompt (но «инженер промптов» вместо «promt-engineer»), fine-tuning (с inline «дообучение»).
- **Legal terms** с inline gloss: fair use (доктрина «добросовестного использования»), opt-out (право отказа).
- **URLs, case names, dates** — естественно латиница.

### Pre-GATE deep latin-token scan (mandatory, ENFORCED)

Pattern-narrow grep маскирует depth — Лекция 8 verification (32-pattern) показал 0-4 hits → подумал deck clean. Deep scan показал 919 в speech. Поэтому ОБЯЗАТЕЛЕН **deep latin-token scan** перед каждым USER GATE B/C:

```python
# deep_latin_scan.py — broad regex + brand allowlist
import re, sys, pathlib

BRAND_ALLOWLIST = {
    # Brands
    "Sora", "Midjourney", "Suno", "ElevenLabs", "OpenAI", "Anthropic", "Adobe",
    "Firefly", "NYT", "Bloomberg", "Reuters", "BBC", "CNN", "RIAA", "DMCA", "CDPA",
    "GDPR", "Wikipedia", "Wikimedia", "YouTube", "GitHub", "Google", "Microsoft",
    "Meta", "Apple", "DeepMind", "DeepSeek", "Claude", "GPT", "ChatGPT", "Gemini",
    "Copilot", "Llama", "Mistral", "Cursor", "Maxar", "Palantir", "Anduril",
    # Tech acronyms (с RU расшифровкой обычно где-то)
    "AI", "ML", "LLM", "RAG", "MCP", "API", "GenAI", "RLHF", "CV", "NLP", "UI",
    "UX", "SaaS", "PaaS", "OS", "GPU", "CPU", "TPU", "CC", "PDF", "PNG", "JPG",
    "SVG", "HTML", "CSS", "JSON", "YAML", "URL", "URI", "HTTP", "HTTPS", "OAuth",
    "JWT", "REST", "gRPC", "SQL", "OODA", "HITL", "LAWS", "SAR", "ATR", "MCAS",
    "ROE", "ARC", "AGI", "MMLU", "HumanEval", "BPE", "v1", "v2", "v3",
    # Slide markers / mode names
    "text", "image", "video", "audio", "fair", "use", "opt", "out",
}

def scan(path: str):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    # Strip frontmatter + code blocks (не считать)
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    # Strip URLs
    text = re.sub(r"https?://\S+", "", text)
    # Latin word: ≥3 chars, начинается с буквы
    tokens = re.findall(r"\b[A-Za-z][A-Za-z\-]{2,}\b", text)
    hits = [t for t in tokens if t not in BRAND_ALLOWLIST and t.lower() not in {b.lower() for b in BRAND_ALLOWLIST}]
    unique = sorted(set(hits))
    print(f"{path}: {len(hits)} occurrences, {len(unique)} unique")
    for tok in unique[:50]:
        cnt = hits.count(tok)
        print(f"  {cnt}× {tok}")

if __name__ == "__main__":
    for p in sys.argv[1:]:
        scan(p)
```

Run:
```bash
python3 deep_latin_scan.py library/lectures/lec-NN/speech.md library/lectures/lec-NN/slides/*.md
# Также на extracted PPTX visible text:
python3 -c "from pptx import Presentation; p=Presentation('library/lectures/lec-NN/rendered/lec-NN.pptx'); \
  [print(s.text) for sl in p.slides for s in sl.shapes if s.has_text_frame]" > /tmp/pptx-visible.txt
python3 deep_latin_scan.py /tmp/pptx-visible.txt
```

### Acceptance criteria

- **0 critical anglicism hits** (top-30 blacklist) в narrative body.
- **Deep scan results** показывают только legitimate Latin tokens: brand names, URLs, case names (people / orgs), slide markers `[sNN]`, tech acronyms whitelisted.
- **Whitelist-only unique** (i.e. `unique - whitelist = ∅` для narrative body content; URLs / case names / markers OK).

**Cost-of-omission lec-08:** speech v1 self-report «0 hits» при 107 patterns / 186 occurrences → owner reject → 3h, 3 revision passes.

**Связанные правила:** [[russification]], `speech-writer.md` § ENFORCED Anti-anglicism, `book-editor.md` § RUSSIFICATION в chapter body, `presentation-designer.md` § ENFORCED — Russification для RU lectures.

---

## 5.8b Acronym glossing (ENFORCED — [[feedback_acronym_glossing]])

**Правило.** Каждая ключевая аббревиатура на слайде (MTTR, IaC, DORA, RCT, SDD, BDD, TDD, ADR, EARS, NFR и т.п.) должна быть раскрыта/пояснена на **первом видимом употреблении** — inline, в скобках, прямо на слайде. Пояснение только во frontmatter (`assertion:`, `chapter_ref`) или в speaker notes **не считается** — студент видит только visible body.

**Как применять:**
- Первое употребление в деке: "MTTR (mean time to repair, время восстановления после сбоя)".
- Далее в том же деке — можно использовать без повтора глоссы (не на каждом слайде).
- Не путать с базовыми, аудитории и так знакомыми терминами (API, HTTP, JSON, CI/CD, LLM — см. Audience Profile в CLAUDE.md: аудитория курса — практикующие инженеры, разжёвывать очевидное не нужно). Глоссировать именно domain-specific/менее очевидные акронимы.
- presentation-critic должен проверять это отдельным пунктом наравне с anglicism-сканом — чистый `deep_latin_scan.py` **не ловит** голые акронимы (они не всегда triggers pattern/latin-token скана).

**Cost-of-omission:** Лекция 4 round-3 (issue #162) — даже после полного presentation-critic + student-simulator прохода MTTR и IaC остались голыми акронимами на слайде (RU-гло́сса была только в frontmatter). Поймано вручную владельцем при просмотре, не автоматической проверкой.

---

## 5.9 Hero images на s01 + s39 (ENFORCED — [[hero-images-required]])

**Источник:** рефлексия Лекции 8 (#122), owner explicit запрос «не хватает броской иллюстрации на самом первом слайде и на завершающем, сделай и запиши себе как общее требования ко всем презам».

**Правило:** **каждая** презентация курса ОБЯЗАНА иметь hero-иллюстрацию на первом (s01 / ice-breaker / cover) и последнем (s39 / closing / bridge) слайдах. **≥40% площади слайда** или full-bleed background.

### s01 (ice-breaker / cover) — что делать

- Hero ≥40% площади или full-bleed background с текстом сверху.
- **Foreshadow keystone axis лекции** (визуально намекать на main концепцию).
- ИЛИ показывать **iconic visual из домена** (real product screenshot, demo frame, signature image).
- ИЛИ создавать **«wow factor»** — что-то, что заставит студента сразу заинтересоваться.
- **Не подходит:** stock illustration с laptop + brain icon, generic «AI» visual, plain Ocean palette card, чисто текстовый cover.
- **Подходит:** collage of generated outputs (Sora 2 frame + Midjourney work + Suno waveform), iconic product screenshot, viral case visual.

### s39 (closing / bridge) — что делать

- Hero ≥40% площади.
- **Замыкать emotional arc** — повторить keystone visual из s05 / показать «после AI» state.
- ИЛИ **bridge к следующей лекции** — visual hint на тему Лекции N+1.
- ИЛИ **iconic case visual** — самый запоминающийся artefact из лекции (e.g., Drew Ortiz fake profile, Kelly McKernan plaintiff portrait, X-62 VISTA DARPA).
- **Не подходит:** thank you slide, Q&A repeat, sources list только.

### Source images

Используй **6-tier acquisition** (§5.7). При truly unavailable real image → custom data-viz hero (NOT plain text card), e.g. cost-collapse chart full-bleed для finance lecture.

### Acceptance criteria

- s01: hero image present, ≥40% площади, links to keystone OR domain identity, attribution label visible.
- s39: hero image present, ≥40% площади, links to emotional payoff OR Lec-N+1 bridge, attribution label visible.
- Captions на русском (см. §5.8 Russification).
- Ocean palette consistency (см. §5.5 + дизайн-плейбук).

**Cost-of-omission lec-08:** 6 min — простое улучшение, но владелец заметил отсутствие сразу — упущенная возможность hook + payoff.

**Слайд-инвентарь:** добавить `hero_cover` + `hero_closing` к mandatory slide types (см. §4 «Slide-types library»). Каждый deck должен иметь оба типа.

**Связанные правила:** [[hero-images-required]], [[no-mock-fallbacks]] (Hero images REAL, не stylized mock), [[russification]] (captions на русском), `presentation-designer.md` § ENFORCED — Hero images на s01 + s39.

---

## 5.10 Deep notes / base-before-depth / real cases / formal-vs-meme (ENFORCED — Лекция 3 v5, owner 2026-09-14)

Owner дал 20 правок на v4-дек Лекции 3; сквозная тема — «тезисно на слайде + бедно в заметках + мало реальных примеров + перескок в глубину без базы». Четыре правила, обязательные для всех деков курса (memory: [[slides-deep-notes-base-cases]] + [[slides-meme-forward-minimal-text]] п.1a):

1. **Глубокие speaker notes — для лекции 500–800 слов связного нарратива** (решение владельца №10, 2026-10; прежние 250–450 действуют для семинаров — `../seminar-production/README.md` §5; ещё более раннее 150–300 отменено). Не тезисно, не layout-описание. Выводятся book-first из главы: определение → механизм → пример → провал/граница. Слайд несёт assertion + минимум evidence; ЗАМЕТКА несёт полное объяснение. **Каждый** содержательный слайд обязан иметь заметки (0 пустых — owner поймал 4 типовые задачи без notes).
2. **База ДО глубины.** Не открывать слайд/заметку продвинутым числом/приёмом без установленной базы. Перед «recursive-512 69%» — что такое чанкирование; перед «0.95^n≈36%» — что такое p^n; перед MCP — транспорт/REST. Мини-база перед каждым advanced-тезисом (сверх §-классической базы [[lecture-section-classic-base-first]]).
3. **Реальные кейсы в КАЖДОЙ секции.** Каждая крупная тема (RAG, агенты, обучение, промпт-задачи) несёт слайды-кейсы: реальная задача → архитектура → что трудно → типовой провал → как чинит → baseline. Привязка к реальным реализациям; выдуманные детали — «иллюстративный».
4. **Formal-vs-meme.** Мем ТОЛЬКО на hook / judgment / контраст-слайдах. Слайды-процедуры/техники/сравнения (how-to, decision-table, how-each-works — напр. JSON-спека, eval-методы, agent-when-логика) — **формальные, без мема**. Тест: «мем несёт тезис-суждение?» да → ок; «слайд объясняет КАК делать?» → формальный.

### Pre-GATE проверки (добавить к §9.5)
- Sample 5–7 заметок → длина 500–800 слов связного текста для лекции (250–450 для семинара), не буллеты. `grep` слайдов с пустыми notes = 0.
- Каждая крупная секция имеет ≥1 кейс-слайд с реальной привязкой + baseline.
- Мемы: нет мема на формальном how-to/сравнительном слайде.
- Sample advanced-тезисов → у каждого база предъявлена рядом/до.

**Cost-of-omission Лекция 3:** owner дал 20 правок v4→v5 из-за нарушения этих 4 пунктов (бедные заметки, перескок в глубину, мало кейсов, мемы на формальных слайдах). Структурный gap, не polish.

---

## 5.11 Библиотека приёмов деки семинара (ENFORCED — Семинар 5, issue #211)

Дека семинара собирается из **именованной библиотеки приёмов**, а не укладкой блоков сверху вниз.
Точка подключения — поле `visual.pattern` в `deck.yaml`. Три правила, каждое куплено дефектом
реальной деки:

1. **Одна работа слайда — одна форма, и форма не переиспользуется.** Вопрос залу выглядит только
   как вопрос; итог, факт, реплика докладчика, оговорка, технический блок — иначе. В Семинаре 5 до
   пересборки одна кремовая плашка несла шесть разных работ на 31 слайде из 56 — отсюда
   владельческое «толи вопрос, толи утверждение».
2. **Таблица — коробка с текстом и тонкими линиями, а не сетка PowerPoint.** `add_table()` в деке
   семинара не вызывается ни разу.
3. **Высота считается по измеренному тексту, а не по числу элементов.** Замер делает тот же код,
   который рисует.

**Полный словарь приёмов, грамматика форм, правила измерения и расчёт ширины колонок —
[`seminar-deck-kit.md`](seminar-deck-kit.md). Чем проверяется работа и почему проверки врут —
[`proverki-i-pravila.md`](proverki-i-pravila.md): пять правил, каждое из живого случая.**
Эталонная реализация: `library/seminars/sem-05/rendered/` — `deck_kit.py`, `metrics.py`,
`build_sem05.py`, аудит `audit_grammar.py`.

---

## 5.12 Форма подачи кадра (ENFORCED — владелец 2026-10-08; уточнено чтением Лекции 6 2026-10-10)

**Запреты этого раздела перечислены одной строкой каждый в `CLAUDE.md` § «Форма подачи слайда» и
блокируют приёмку независимо от того, прочитан ли этот файл.** Здесь — полный текст, цитаты
владельца и приёмка. Раздел заведён 2026-10-14 (#238): до этого `CLAUDE.md` ссылался на §5.12–5.17
семь раз, а разделов не существовало — файл кончался на §5.11.

**Правило.** Слайд не имеет права быть текстом, в котором надо искать главное.

Владелец, разбирая деку Лекции 6 (она прошла отбор кейсов, нормативную сверку, контроль плотности
и визуальный свод): **«текстовая стена»**. Содержание было верным, показано не было.

### Что обязательно

| Элемент | Как | Приёмка |
|---|---|---|
| **Числа** | плашками (полоса «было · стало · к чему привело»), не внутри абзаца | ключевое число кадра вне абзаца; пара «было → стало» — **одна** плашка, не два числа на разных кадрах |
| **Иерархия** | измеренное число набирается заголовком | эталон Лекции 6 — около 39 кадров из 100; у Лекции 7 было ноль, и это P1 прожарки |
| **Порядок работы** | схемой не длиннее четырёх шагов в ряду | длинные конвейеры запрещены отдельно |
| **Сплошной текст** | в буллиты; лирика и оговорки — в заметки | абзацев сплошняком на кадре нет |
| **Два столбца** | только под противопоставление «что получается / что не получается» | перечни кейсов — буллитами друг за другом, не колонками |
| **Заголовок** | называет кейс: «Пример: оптимизация колеса центробежного насоса» | заголовок-тезис вместо имени кейса — дефект |
| **Сопоставление «без ИИ / с ИИ»** | читается с одного взгляда | отсутствие владелец назвал системной ошибкой |
| **Кейс** | по-человечески: какую задачу решали, как решали, что получилось | см. §5.13 |
| **Тип задачи и модальность** | словами: «классификация изображений» | отсылку «по сетке курса» не писать |
| **Картинка** | лучше не ставить вовсе, чем ставить слабую | источники фотографий на слайде **не** подписывать |
| **Ссылки** | источник на кадре и каждый URL в заметках — настоящая гиперссылка (`run.hyperlink.address`) | проверка — `r:id` в XML сохранённого файла; самоотчёт агента не принимается. Ссылка из тела кадра убрана в подвал; на себя не ссылаемся |

**Жёсткое ограничение «3–5 строк видимого текста» снято** (владелец, 2026-10-06). Кадры могут быть
тяжёлыми там, где этого требует разбор. Остаётся единственный физический предел: текст не наезжает
сам на себя при рендере — это ловится предупреждениями сборки (`[высота]`, `[кегль]`), и они
блокирующие. Замер, который снял ограничение: у деки Лекции 7 медиана 91,5 слова на кадр против
120,5 у **принятой** Лекции 6 — то есть претензия «супер текстовая» к ней не применялась, дело было
в раскладке.

**Пол кегля замеряется по собранному PDF.** Отчёт сборки смотрит масштаб прогона тела и молчит о
подписях: по PDF деки Лекции 7 ниже 12 пт набрано **24% всех видимых знаков на 87 кадрах из 122**
(у Лекции 6 — 7%), потому что пол стоял на абзацах тела и не стоял на плашках: шапка 10 пт
капителью, подпись под числом 10,5 пт курсивом. **Оговорка, которая делает число честным,
оказалась самым нечитаемым текстом на кадре.** Инструмент — `deckkit/pdfmeasure.py`.

---

## 5.13 Раскладка подробного разбора на кадре (ENFORCED)

**Правило.** Подробный разбор строится в одной форме, и у каждого шага своё место на кадре:

> **цена обеих ошибок → оба классических режима, посчитанные в той же цене → модель рядом с ними →
> как это устроено → что переехало.**

**Откуда форма.** Единственный разбор Лекции 6, прошедший со сцены без заминки, — Scania. Владелец
назвал все числа подряд: «10 единиц осмотр, 500 поломка, 156 000 на сплошном осмотре». Из разбора
прочтения: «**потому что цена обеих ошибок там назначена до всякой точности и стоит на слайде
плашками.** Это образец того, как должен выглядеть каждый разбор».

### Приёмка кадра разбора

- [ ] **Обе цены ошибки** — на кадре плашками, в одних единицах, до всякой точности. В заметках —
      недостаточно.
- [ ] **Оба классических режима** посчитаны той же ценой. Графа второго шага названа: **(а)** оба
      числом в одной единице · **(б)** второй назван без своего числа, и это сказано на месте ·
      **(в)** второго режима в задаче нет, и это сказано с причиной.
- [ ] **Модель сравнена с этими режимами.** Выигрыш, посчитанный **от нуля** вместо классического
      режима, не принимается.
- [ ] **Как это устроено:** что на входе, что на выходе, на чём обучено, **имя изделия** — на
      кадре, не только в поле источника.
- [ ] **Что переехало** — форма словаря названа по имени либо назван отказ присвоить форму с
      причиной.
- [ ] **Пара «дало — потребовало — в сумме»** читается с одного взгляда.

**Цена пропуска шага «как это устроено», замеренная:** «как решали» — 0 кадров из 122 у Лекции 7
против 19 из 100 у принятой Лекции 6; «вход»/«выход» — 2 против 17; имя изделия на разборе — 9 (7%)
против 30 (30%). Несущие случаи стояли безымянными, при том что поле источника тех же кадров их
называло. Студент на прожарке: «не могу это загуглить вечером и не могу пересказать товарищу».

**Разбор не обязан помещаться в один кадр**, и дробить его ради экономии места запрещено
(`CLAUDE.md` § «Строение раздела отраслевой лекции»). Повествовательная сторона формы, правило трёх
и шести, три условия отбора примера — `../lecture-production/stroenie-i-povestvovanie.md` §3–4.

---

## 5.14 Числа пишутся так, как произносятся (ENFORCED)

**Правило.** Запись числа на кадре рассчитана на произнесение вслух.

- **Научная запись в видимом теле запрещена.** «169 тысяч часов», не «1,687·10⁵». Со сцены степень
  теряется: на чтении Лекции 6 «1,687·10⁵ часов» прочиталось как **«16,6 тысяч»**.
- **Два похожих числа не ставятся в одну фразу.** Разводятся подписями. На чтении Лекции 6 лектор
  сказал «36, они примерно были» про число участников: участников было 68, а 36 — число настоящих
  указаний на картах, и оба числа стояли в одной фразе кадра.
- **Если число ключевое — оно на плашке**, а не внутри абзаца. Из рекомендаций по ведению (9.8):
  «числа писать так, как произносишь».
- **Снятый кадр с числом, которое лектор хочет произносить, возвращается.** Дословно из разбора:
  «**это моя ошибка круга 6: я снял слайд, число с которого ты хочешь произносить**» — точка
  окупаемости суррогата ушла в заметки, лектор произносил её по памяти и назвал 12 000 там, где
  записано 10 000.
- **Каждая заминка лектора на числе означает недостающую строку на кадре.** Падение точности
  ставится одной парой «было → стало»; когда числа живут на двух соседних кадрах, их приходится
  собирать вслух.

**Приёмка.** Греп видимого слоя на `·10` / `\d+[.,]\d+\s*[·×]\s*10` — ноль. Пары похожих чисел в
одной фразе — просмотром, с подписями у каждого. Измеримое утверждение без базы — P1 «missing
denominator» (`CLAUDE.md` § «Baseline / Counterfactual Mandate»).

---

## 5.15 Список упоминаний несёт наблюдения, а не имена (ENFORCED)

**Правило.** Каждая строка списка упоминаний несёт **одно наблюдение**: «здесь то же, но платили
разметкой», «здесь эффект заявлен без базы». Список из имён — библиография, её место в заметках.

**Цена, измеренная со сцены.** На чтении Лекции 6 лектор **четыре раза** объявил залу, что смотреть
не будем, и все четыре — такие списки:

- «тут поможет… ничего такого интересного нету, если захотите, потом почитайте»;
- «есть ещё много разных других примеров, которые наверное, здесь сейчас можно не проходить»;
- «если захотите подробнее, почитайте — здесь ещё много всяких разных историй»;
- «очень много конечно, ещё работ есть, если они тоже приведены».

Списки были сведены в кругах 6–8 намеренно, чтобы уложиться в правило трёх разборов и шести
упоминаний. Вывод разбора: **«не „вернуть разборы", а „список должен делать работу на экране".
Шесть имён без мысли — это библиография. Шесть строк, где каждая несёт одно наблюдение, — это
слайд, который произносится за минуту.»**

**Исключение, которое само себя оправдало:** список «эффект заявлен без базы» лектор использовал
приёмом — «всегда, если видите какие-то эффекты, спрашивайте, есть ли они действительно от
чего-то». Список, у которого есть работа на экране, остаётся.

**Приёмка.** На кадре-списке: у каждой строки есть сказуемое и наблюдение. Строка из одного имени
(или имя + год) — дефект. Упоминание без числа и базы не нужно вовсе.

---

## 5.16 Дивайдер называет разборы раздела по порядку (ENFORCED)

**Правило.** Дивайдер раздела несёт **имена разборов по порядку**, дословно совпадающие с
заголовками их кадров. Смысл раздела — одной строкой; тег вида «3 working cases · 2 провала» —
без минут (`CLAUDE.md` § «No Timing / No Methodology in Slides»).

**Откуда.** На чтении Лекции 6 лектор **семь раз** узнавал слайд на экране: «я не помню, здесь
нет… о да, да, да, здесь будет замечательный пример» · «давайте я посмотрю, есть ли что-нибудь ещё
у меня здесь интересное» · «что я прыгаю» · «что тут у нас ещё интересного, было или нет?
наверное» · «я не помню, из чего он, металл». Из разбора: «это не про подготовку. Это про то, что
**дека не подсказывает, что будет дальше**. Дивайдер говорит, о чём раздел, но не говорит, какие
три разбора в нём и в каком порядке».

**Приёмка.** Имена на дивайдере сверяются с заголовками кадров раздела **дословно** — расхождение
в формулировке означает, что лектор прочтёт на дивайдере одно, а на кадре увидит другое. Плюс шов:
переход «свод кончился → дивайдер начался» несёт взгляд назад или вперёд; замер Лекции 7 — пять
швов из восьми не несли ни одного.

---

## 5.17 Карта стадии предъявляется без оговорки (ENFORCED)

**Правило.** Карта стадии (матрица «тип задачи × модальность» в конце раздела) предъявляется без
оговорки «наверняка что-то пропущено». Пробел называется **содержательно и на кадре**.

**Откуда.** На чтении Лекции 6 сетка в конце каждого раздела сработала — лектор прошёл её семь раз,
как обещал на входе. Но каждый раз оговаривался «наверняка что-то пропущено» и один раз нашёл
пробел вслух: «забыл включить генерацию чертежей по описанию». Из разбора: «карта стадии должна
быть полной настолько, чтобы её можно было предъявлять без оговорки».

**Правила заполнения.**

- Оси наследуются **дословно по Лекции 1**, своих разрядов не вводить: тип задачи — классификация ·
  распознавание · поиск · генерация · прогноз · планирование; модальность — текст · изображение ·
  звук · видео · структурированные данные · код · мультимодальные комбинации.
- Клетка занимается, если применение на стадии **распространено**, даже когда разбора у нас нет.
- Наши разборы выделяются; клетка без нашего случая несёт только класс применения, без чисел.
- **Честная пустая клетка лучше выдуманной занятой.** Декларировать пробел отбора на кадре
  запрещено.
- Подпись под таблицей считает те клетки, которые на ней нарисованы.

**Порог заполнения — 75%.** Замер Лекции 7: 8–33%, у пяти карт из восьми занята **одна клетка из
двенадцати**, а подпись под таблицей на двенадцать клеток говорила «занято три из сорока двух» —
сорок два не показаны нигде ни разу. Карты переведены в накопительные, чтобы сетка заполнялась по
ходу вечера, как обещает вход.

**Что это требует от охоты за кейсами:** отдельный проход «что на этой стадии делают все»,
независимый от прохода «что мы можем разобрать с числами». В Лекции 6 источником незанятых клеток
служили реестры случаев, не прошедших три условия отбора.
