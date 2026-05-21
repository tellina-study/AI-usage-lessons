"""
Russification pass for Лекция 8 — remove anglicisms from visible body + speaker notes.

Strategy: ordered list of replacements (specific phrases first, then individual terms).
- Replacements applied LINE BY LINE so that order matters per file
- YAML frontmatter ID/LO codes preserved
- Brand names (Sora, Midjourney, Suno, etc.) preserved verbatim

Logs each file's before/after suspicious-count to russification-log.md.
"""
import re
from pathlib import Path
from datetime import datetime

ROOT = Path("/tmp/lec-08-wt/library/lectures/lec-08")
SLIDES = ROOT / "slides"
BUILD = ROOT / "rendered/build_lec08.py"
LOG = ROOT / "rendered/russification-log.md"

# === Ordered replacement table ===
# (pattern, replacement) — applied IN ORDER (specific phrases first)
# All replacements are regex; use re.escape for plain phrases where needed.

REPLACEMENTS = [
    # ============ Long phrases (must run FIRST) ============
    # Compound phrases from brief
    (r'AI генерирует production-уровень artefact за секунды', 'AI создаёт артефакт промышленного качества за секунды'),
    (r'AI генерирует production-grade artefact', 'AI создаёт артефакт промышленного качества'),
    (r'Это новая базовая capability creative-индустри[ия]', 'Это новая базовая возможность для творческих индустрий'),
    (r'базовая capability creative-индустри[ия]', 'базовая возможность для творческих индустрий'),
    (r'production-уровень artefact', 'артефакт промышленного качества'),
    (r'production-grade артефакт', 'артефакт промышленного качества'),
    (r'production-grade artefact', 'артефакт промышленного качества'),
    (r'production-grade», но это не равно «production-grade', 'промышленного качества", но это не равно "промышленного качества'),
    (r'«production-grade»', '«промышленного качества»'),
    (r'production-grade', 'промышленного качества'),
    (r'production use в enterprise', 'промышленное применение в корпоративном секторе'),
    (r'production use', 'промышленное применение'),
    (r'production-уровень', 'промышленное качество'),
    (r'production-готовност[иь]', 'промышленной готовности'),
    (r'production pipeline', 'промышленный pipeline'),
    (r'production cinema', 'промышленное кино'),
    (r'production кино', 'промышленное кино'),
    (r'production', 'промышленное применение'),

    # Cost-collapse
    (r'Cost-collapse 100×[—–-]10[\s ]?000× по asset-классам', 'Обвал стоимости 100×–10 000× по типам ассетов'),
    (r'Cost-collapse: 100×[—–-]10[\s ]?000× по asset-классам', 'Обвал стоимости: 100×–10 000× по типам ассетов'),
    (r'Cost-collapse: dubbing на язык', 'Обвал стоимости: дубляж на язык'),
    (r'Cost-collapse', 'Обвал стоимости'),
    (r'cost-collapse', 'обвал стоимости'),
    (r'asset-классам', 'типам ассетов'),
    (r'asset-класс(ы|ам|ов)?', r'типам ассетов'),
    (r'по asset-классам', 'по типам ассетов'),

    # Concept art etc
    (r'Концепт-арт дни → секунды\. Upwork \+70% YoY AI/ML', 'Концепт-арт: дни → секунды. Upwork +70% год к году в AI/ML'),
    (r'\+70% YoY AI/ML', '+70% год к году в AI/ML'),
    (r'YoY AI/ML', 'год к году в AI/ML'),
    (r'YoY', 'год к году'),
    (r'Concept art дни → секунды', 'Концепт-арт: дни → секунды'),
    (r'Concept art draft', 'Концепт-арт черновик'),
    (r'Concept exploration', 'Исследование концепций'),
    (r'concept art', 'концепт-арт'),

    # RIAA, Sony, etc
    (r'RIAA v Suno, Sony millions', 'RIAA против Suno, миллионы Sony'),
    (r'Arup CFO deepfake \$25\.6M\. SI fake authors\. NYT v OpenAI 20M logs',
     'Arup CFO дипфейк $25.6 млн. SI — фейковые авторы. NYT против OpenAI — 20 млн логов'),
    (r'Arup CFO deepfake \$25\.6M', 'Arup CFO дипфейк $25.6 млн'),
    (r'CFO deepfake', 'CFO-дипфейк'),
    (r'CFO-deepfake', 'CFO-дипфейк'),
    (r'deepfake-CFO', 'дипфейк-CFO'),
    (r'SI fake authors', 'SI — фейковые авторы'),
    (r'NYT v OpenAI 20M logs', 'NYT против OpenAI — 20 млн логов'),
    (r'RIAA v Suno', 'RIAA против Suno'),
    (r'NYT v OpenAI', 'NYT против OpenAI'),
    (r'Getty v Stability', 'Getty против Stability'),
    (r'Andersen v Stability', 'Andersen против Stability'),
    (r'Thomson Reuters v Ross', 'Thomson Reuters против Ross'),
    (r'ScarJo v OpenAI', 'ScarJo против OpenAI'),
    (r'Warhol v Goldsmith', 'Warhol против Goldsmith'),
    (r'\bv Stability\b', 'против Stability'),
    (r'\bv OpenAI\b', 'против OpenAI'),
    (r'\bv Suno\b', 'против Suno'),

    # Discovery / motion
    (r'Discovery \+ motion war', 'Истребование доказательств + борьба за процессуальные действия'),
    (r'discovery \+ motion war', 'истребование доказательств + борьба за процессуальные действия'),
    (r'Discovery — это юридическая фаза процесса', 'Истребование доказательств (discovery) — это юридическая фаза процесса'),
    (r'Discovery — обмен документами', 'Истребование доказательств (discovery) — обмен документами'),

    # Output similarity / training corpus
    (r'training\+output similarity', 'обучение + сходство вывода'),
    (r'training \+ output similarity', 'обучение + сходство вывода'),
    (r'Output similarity check обязателен',
     'Проверка сходства результата с обучающими данными — обязательна'),
    (r'output similarity check', 'проверка сходства результата'),
    (r'Output similarity check', 'Проверка сходства результата'),
    (r'Output similarity', 'Сходство вывода'),
    (r'output similarity', 'сходство вывода'),
    (r'training corpus', 'обучающий корпус'),
    (r'licensed corpus', 'лицензированный корпус'),
    (r'curated dataset', 'курируемый датасет'),
    (r'curated corpus', 'выверенный корпус'),
    (r'scraped web', 'данные, спарсенные из веба'),
    (r'scraped from web', 'спарсено из веба'),
    (r'\bscraping\b', 'парсинг данных'),

    # Fair use
    (r'НЕ fair use, это infringement evidence', 'НЕ «добросовестное использование», это доказательство нарушения'),
    (r'fair-use defence', '«добросовестное использование» как защита'),
    (r'fair-use rejection', 'отказ в «добросовестном использовании»'),
    (r'fair-use 4-factor', '«добросовестное использование» — 4-факторный тест'),
    (r'«fair use»', '«добросовестное использование»'),
    (r'«Fair use»', '«Добросовестное использование»'),
    (r'\bfair use\b', '«добросовестное использование»'),
    (r'\bfair-use\b', '«добросовестное использование»'),

    # Class action
    (r'Class action artists', 'Коллективный иск художников'),
    (r'class action', 'коллективный иск'),
    (r'Class actions', 'Коллективные иски'),
    (r'class actions', 'коллективные иски'),

    # Style mimicry
    (r'Style mimicry в стиле named artist — НЕ safe just because стиль не copyrightable',
     'Подражание стилю конкретного художника — НЕБЕЗОПАСНО, даже если стиль не охраняется авторским правом'),
    (r'Style mimicry «в стиле \[named artist\]» — НЕ safe just because стиль не copyrightable',
     'Подражание стилю «в стиле [конкретного художника]» — НЕБЕЗОПАСНО, даже если стиль не охраняется авторским правом'),
    (r'Style mimicry', 'Подражание стилю'),
    (r'style mimicry', 'подражание стилю'),
    (r'named artist', 'конкретный художник'),
    (r'не copyrightable', 'не охраняется авторским правом'),
    (r'copyrightable', 'охраняется авторским правом'),

    # Lawsuit-driven licensing
    (r'Lawsuit-driven licensing — actual outcome', 'Лицензирование под давлением исков — фактический исход'),
    (r'lawsuit-driven licensing', 'лицензирование под давлением исков'),
    (r'Lawsuit-driven licensing', 'Лицензирование под давлением исков'),

    # Business-model layer
    (r'Это новый business-model layer, НЕ «all AI music banned»',
     'Это новый слой бизнес-модели, а не «запрет всей AI-музыки»'),
    (r'business-model layer', 'слой бизнес-модели'),
    (r'all AI music banned', 'запрет всей AI-музыки'),

    # MTD / SJ / discovery
    (r'Class actions выживают MTD на DMCA \+ публичные права',
     'Коллективные иски проходят motion to dismiss по DMCA + публичным правам'),
    (r'выживают MTD', 'проходят motion to dismiss'),
    (r'MTD denied', 'motion to dismiss отклонён'),
    (r'MTD pending', 'motion to dismiss ожидается'),
    (r'SJ deadline', 'дедлайн упрощённого решения суда (SJ)'),
    (r'SJ\* deadline', 'дедлайн упрощённого решения суда (SJ*)'),

    # Deepfake / identity
    (r'Видеозвонок ≠ identity proof в 2024\+', 'Видеозвонок ≠ подтверждение личности в 2024+'),
    (r'identity proof', 'подтверждение личности'),
    (r'out-of-band verification', 'проверка через независимый канал'),
    (r'callback по known number', 'обратный звонок по известному номеру'),
    (r'callback no known number', 'обратный звонок по известному номеру'),
    (r'multi-factor authentication', 'многофакторная аутентификация'),
    (r'documented workflow', 'документированный процесс'),
    (r'safety layer', 'слой безопасности'),
    (r'NSFW detection', 'детекция NSFW-контента'),
    (r'age verification', 'верификация возраста'),
    (r'reporting pipeline', 'процесс обработки жалоб'),

    # Source quality
    (r'Source quality > volume', 'Качество источников важнее объёма'),
    (r'source quality > volume', 'качество источников важнее объёма'),

    # Voice cloning
    (r'voice cloning', 'клонирование голоса'),
    (r'Voice cloning', 'Клонирование голоса'),
    (r'voice clone', 'клон голоса'),
    (r'Voice clone', 'Клон голоса'),

    # Character consistency
    (r'Character consistency: cameos & Omni Reference',
     'Сохранение персонажа: cameos и Omni Reference'),
    (r'character consistency', 'сохранение персонажа между генерациями'),
    (r'Character consistency', 'Сохранение персонажа'),
    (r'Multi-scene narrative стал возможен',
     'Multi-scene нарратив стал возможен'),
    (r'Multi-scene drift', 'Drift между сценами'),
    (r'multi-scene drift', 'drift между сценами'),
    (r'multi-scene prompts', 'multi-scene промптах'),
    (r'multi-scene scripting', 'скриптинг между сценами'),
    (r'multi-shot', 'мульти-кадр'),

    # Settlement / matrix
    (r'MAJORS × STATUS', 'КРУПНЫЕ ЛЕЙБЛЫ × СТАТУС'),
    (r'MAJORS · SETTLEMENT STATUS', 'КРУПНЫЕ ЛЕЙБЛЫ · СТАТУС УРЕГУЛИРОВАНИЯ'),
    (r'Settlement matrix', 'Таблица урегулирований'),
    (r'settlement matrix', 'таблица урегулирований'),
    (r'\bsettled\b', 'урегулирован'),
    (r'\bsettlement\b', 'урегулирование'),
    (r'2 из 3 majors settled', '2 из 3 крупных лейблов урегулировали'),
    (r'\bmajors\b', 'крупных лейблов'),
    (r'major labels', 'крупные лейблы'),
    (r'one of 3 major labels', 'один из 3 крупных лейблов'),

    # Trial chip
    (r'TRIAL DATE', 'ДАТА СУДА'),
    (r'Trial chip / Pending', 'Суд / Ожидание'),

    # Backup
    (r'Backup screenshot', 'Резервный скриншот'),
    (r'backup screenshot', 'резервный скриншот'),
    (r'Backup PNG', 'Резервный PNG'),
    (r'BACKUP PROMPTS', 'РЕЗЕРВНЫЕ ВОПРОСЫ'),
    (r'backup prompts', 'резервные вопросы'),
    (r'Backup prompts', 'Резервные вопросы'),
    (r'Backup variant', 'Резервный вариант'),
    (r'backup variant', 'резервный вариант'),
    (r'backup card', 'резервная карточка'),
    (r'BACKUP', 'РЕЗЕРВ'),
    (r'\bBackup\b', 'Резервный'),

    # Iconic seasonal creative
    (r'iconic seasonal creative БЕЗ human leadership = brand damage',
     'эталонная сезонная кампания БЕЗ человеческого руководства = ущерб бренду'),
    (r'Iconic brand campaigns без human leadership = brand damage',
     'Эталонные брендовые кампании без человеческого руководства = ущерб бренду'),
    (r'iconic seasonal creative', 'эталонная сезонная кампания'),
    (r'iconic creative', 'эталонная кампания'),
    (r'iconic brand campaigns', 'эталонные брендовые кампании'),
    (r'iconic brand campaign', 'эталонная брендовая кампания'),
    (r'iconic seasonal', 'эталонная сезонная'),
    (r'iconic-кампания', 'эталонная кампания'),
    (r'\biconic\b', 'эталонная'),

    # Brand damage / trust
    (r'brand damage', 'ущерб бренду'),
    (r'Brand damage', 'Ущерб бренду'),
    (r'brand-trust failure', 'провал доверия к бренду'),
    (r'brand-trust риск', 'риск доверия к бренду'),
    (r'brand-trust риска', 'риска доверия к бренду'),
    (r'brand-trust', 'доверие к бренду'),
    (r'Brand-trust', 'Доверие к бренду'),
    (r'brand trust', 'доверие к бренду'),
    (r'brand sentiment', 'отношение к бренду'),
    (r'brand asset', 'актив бренда'),
    (r'brand equity', 'капитал бренда'),
    (r'human leadership', 'человеческое руководство'),

    # Sentiment swing
    (r'Sentiment swing — НЕ главная метрика brand-trust failure',
     'Разворот тональности — НЕ главная метрика провала доверия к бренду'),
    (r'Sentiment swing, не CTR — главная metric brand-trust риска',
     'Разворот тональности, а не CTR — главная метрика риска доверия к бренду'),
    (r'Sentiment swing, НЕ CTR — главная metric brand-trust риска',
     'Разворот тональности, а не CTR — главная метрика риска доверия к бренду'),
    (r'Sentiment swing', 'Разворот тональности'),
    (r'sentiment swing', 'разворот тональности'),
    (r'SENTIMENT SWING', 'РАЗВОРОТ ТОНАЛЬНОСТИ'),

    # AI-ad
    (r'AI-ad возможен, но iconic seasonal creative БЕЗ human leadership = brand damage',
     'AI-реклама возможна, но эталонная сезонная кампания БЕЗ человеческого руководства = ущерб бренду'),
    (r'AI-ad', 'AI-реклама'),
    (r'AI ad', 'AI-реклама'),
    (r'ad creative', 'рекламный креатив'),

    # Verbatim / regurgitation
    (r'процитировать твой training corpus verbatim',
     'процитировать твой обучающий корпус дословно'),
    (r'процитировать.*verbatim',
     lambda m: m.group(0).replace('verbatim', 'дословно')),
    (r'\bverbatim\b', 'дословно'),
    (r'NYT regurgitation theory', 'теория дословного цитирования NYT'),
    (r'NYT regurgitation', 'дословное цитирование NYT'),
    (r'Regurgitation theory', 'Теория дословного цитирования'),
    (r'regurgitation theory', 'теория дословного цитирования'),
    (r'regurgitation risk', 'риск дословного цитирования'),
    (r'\bregurgitation\b', 'дословное цитирование'),
    (r'\bRegurgitation\b', 'Дословное цитирование'),

    # SI fake authors block
    (r'19/100 top-bestseller книг — actual humans',
     '19/100 книг из топа бестселлеров — написаны реальными людьми'),
    (r'top-bestseller книг — actual humans',
     'книг из топа бестселлеров — написаны реальными людьми'),
    (r'top-bestseller книг', 'книг из топа бестселлеров'),
    (r'top-bestseller', 'топ-бестселлер'),
    (r'actual humans', 'реальные люди'),
    (r'Остальные — AI-knockoffs · fake author names · stock photos · fictional bios',
     'Остальные — AI-клоны · фейковые имена авторов · стоковые фото · вымышленные био'),
    (r'AI-knockoffs · fake names имитируют jazz figures, financial advisors',
     'AI-клоны · фейковые имена имитируют джазовых музыкантов, финансовых консультантов'),
    (r'AI-knockoffs', 'AI-клоны'),
    (r'fake author names', 'фейковые имена авторов'),
    (r'fake names', 'фейковые имена'),
    (r'sham personas', 'фейковые персоны'),
    (r'sham books', 'фейковые книги'),
    (r'sham authors', 'фейковые авторы'),
    (r'fictional bios', 'вымышленные био'),
    (r'fake profile', 'фейковый профиль'),
    (r'fake authors', 'фейковые авторы'),
    (r'fake bios', 'фейковые био'),
    (r'jazz figures', 'джазовые музыканты'),
    (r'financial advisors', 'финансовые консультанты'),
    (r'jazz personalities', 'джазовые персоналии'),
    (r'jazz characters', 'джазовые персонажи'),
    (r'Drew Ortiz · full fictional · AI bone \+ AI text',
     'Drew Ortiz · полностью вымышленный · AI-портрет + AI-текст'),
    (r'«Drew Ortiz» — full fictional · AI face \+ AI text',
     '«Drew Ortiz» — полностью вымышленный · AI-портрет + AI-текст'),
    (r'full fictional · AI face \+ AI text',
     'полностью вымышленный · AI-портрет + AI-текст'),
    (r'full fictional', 'полностью вымышленный'),
    (r'AI face \+ AI text', 'AI-портрет + AI-текст'),
    (r'AI-generated profile photos', 'AI-сгенерированные фото профилей'),
    (r'AI-pseudonyms', 'AI-псевдонимы'),
    (r'AI pseudonyms', 'AI-псевдонимы'),
    (r'AI-disclosed', 'с раскрытием AI-авторства'),
    (r'явно AI-disclosed', 'авторство AI должно быть раскрыто'),
    (r'AI-detected', 'распознан как AI'),
    (r'AI-generated', 'AI-сгенерированный'),

    # Legacy trust
    (r'Legacy trust = key brand asset\. AI-pseudonyms разрушают его моментально\. Если публикуешь под именем — имя должно быть реальным human ИЛИ всё AI-disclosed',
     'Накопленное доверие — ключевой актив бренда. AI-псевдонимы разрушают его моментально. Если публикуешь под именем — имя должно быть реальным человеком ИЛИ авторство AI должно быть раскрыто'),
    (r'Legacy trust', 'Накопленное доверие'),
    (r'legacy trust', 'накопленное доверие'),
    (r'legacy/iconic', 'эталонный/исторический'),
    (r'reflexively', 'на рефлексе'),
    (r'real human', 'реальный человек'),
    (r'real persons', 'реальные люди'),
    (r'имя должно быть реальным human', 'имя должно быть реальным человеком'),

    # Marketing
    (r'Marketing backlash — Toys R Us \+ Coca-Cola',
     'Маркетинговый провал — Toys R Us + Coca-Cola'),
    (r'Marketing backlash', 'Маркетинговый провал'),
    (r'marketing backlash', 'маркетинговый провал'),
    (r'viral backlash', 'вирусный негатив'),
    (r'viral mockery', 'вирусные насмешки'),
    (r'tepid reception', 'прохладный приём'),
    (r'public backlash', 'публичный негатив'),
    (r'\bbacklash\b', 'негативная реакция'),
    (r'Coca-Cola Holidays 2024 AI ad — viral backlash',
     'Coca-Cola Holidays 2024 AI-реклама — вирусный негатив'),
    (r'Toys R Us Cannes Lions 2024 sentiment swing − 10pp',
     'Toys R Us Cannes Lions 2024 разворот тональности −10 п.п.'),
    (r'Toys R Us Cannes Lions 2024 sentiment swing −10pp',
     'Toys R Us Cannes Lions 2024 разворот тональности −10 п.п.'),
    (r'sentiment swing −10pp', 'разворот тональности −10 п.п.'),

    # SI / displacement
    (r'wage compression снизу — структурная, не временная',
     'снижение зарплат снизу — структурное, не временное'),
    (r'Wage compression снизу — structural, не temp shock',
     'Снижение зарплат снизу — структурное, не временный шок'),
    (r'wage compression снизу', 'снижение зарплат снизу'),
    (r'wage compression', 'снижение зарплат'),
    (r'Wage compression', 'Снижение зарплат'),
    (r'commodity-dubbing displaced', 'коммодити-дубляж вытеснен'),
    (r'Commodity-dubbing displaced', 'Коммодити-дубляж вытеснен'),
    (r'commodity dubbing', 'коммодити-дубляж'),
    (r'\bDisplacement\b', 'Замещение'),
    (r'\bdisplacement\b', 'замещение'),
    (r'displaced класса', 'замещённого класса'),
    (r'AI-deploy сместит', 'твой AI-проект вытеснит'),
    (r'structural shift', 'структурный сдвиг'),
    (r'структурный shift', 'структурный сдвиг'),
    (r'temp shock', 'временный шок'),
    (r'не temp shock', 'не временный шок'),
    (r'Industry consolidation как ответ', 'Консолидация индустрии как ответ'),
    (r'defensive consolidation', 'оборонительная консолидация'),
    (r'Defensive consolidation', 'Оборонительная консолидация'),
    (r'industry consolidation', 'консолидация индустрии'),
    (r'Industry response', 'Ответ индустрии'),
    (r'INDUSTRY RESPONSE', 'ОТВЕТ ИНДУСТРИИ'),
    (r'industry response', 'ответ индустрии'),
    (r'Industry consolidation', 'Консолидация индустрии'),

    # Specific UI/UX strings on slides
    (r'LIVE DEMO', 'ДЕМО В БРАУЗЕРЕ'),
    (r'Live demo', 'Демо в браузере'),
    (r'live demo', 'демо в браузере'),
    (r'PRIMARY · АУДИО', 'ОСНОВНОЕ · АУДИО'),
    (r'FALLBACK · IMAGE', 'РЕЗЕРВ · КАРТИНКА'),
    (r'\bPRIMARY\b', 'ОСНОВНОЕ'),
    (r'\bFALLBACK\b', 'РЕЗЕРВ'),
    (r'text-prompt → photoreal за 5 сек', 'текст-промпт → реалистичное фото за 5 сек'),
    (r'photoreal изображение', 'реалистичное фото'),
    (r'photoreal-картинка', 'реалистичная картинка'),
    (r'Photoreal изображение', 'Реалистичное фото'),
    (r'photoreal', 'реалистичное'),
    (r'тема \+ жанр \+ язык → 30-сек трек', 'тема + жанр + язык → трек 30 сек'),

    # Cover / lecture
    (r'Что AI добавил, изменил и сломал — и где сказать «нет»\.',
     'Что AI добавил, изменил и сломал — и где сказать «нет».'),
    (r'creative-индустри[ия]м', 'творческим индустриям'),
    (r'creative-индустри[ия]х', 'творческих индустриях'),
    (r'creative-индустри[ия]', 'творческая индустрия'),
    (r'creative индустрия', 'творческая индустрия'),
    (r'creative-tools', 'творческие инструменты'),
    (r'creative tools', 'творческие инструменты'),
    (r'creative-инструмент(ов|ам|а)?', lambda m: 'творческих инструментов' if m.group(1) in ('ов',) else ('творческим инструментам' if m.group(1) == 'ам' else ('творческого инструмента' if m.group(1) == 'а' else 'творческие инструменты'))),
    (r'creative AI', 'творческий AI'),
    (r'creative-pipeline', 'творческого pipeline'),
    (r'creative pipeline', 'творческий pipeline'),
    (r'creative-проекте', 'творческом проекте'),
    (r'creative-проект', 'творческий проект'),
    (r'creative deliverable', 'творческий deliverable'),
    (r'creative shoot', 'творческая съёмка'),
    (r'creative output', 'творческий результат'),
    (r'creative direction', 'творческое руководство'),
    (r'creative leadership', 'творческое руководство'),
    (r'creative content', 'творческий контент'),
    (r'creative-segment', 'творческий сегмент'),
    (r'creative-experiments', 'творческие эксперименты'),
    (r'commercial creative', 'коммерческая реклама'),
    (r'\bcreative\b', 'творческий'),

    # MINI-FAILURE
    (r'MINI-FAILURE: ScarJo v OpenAI «Sky» \(май 2024\)\. OpenAI убрал голос за неделю — формально без иска\. De-facto win для likeness rights: voice clone обязывает к explicit consent, даже если технологически «всего лишь похож»\.',
     'МИНИ-ПРОВАЛ: ScarJo против OpenAI «Sky» (май 2024). OpenAI убрал голос за неделю — формально без иска. По факту — победа в правах на образ: клонирование голоса обязывает к явному согласию, даже если технологически «всего лишь похож».'),
    (r'MINI-FAILURE: 86% buyers используют AI, но adoption ≠ success\. Toys R Us Cannes 2024 — sentiment swing −10pp',
     'МИНИ-ПРОВАЛ: 86% закупщиков используют AI, но внедрение ≠ успех. Toys R Us Cannes 2024 — разворот тональности −10 п.п.'),
    (r'86% buyers используют AI', '86% закупщиков используют AI'),
    (r'adoption ≠ success', 'внедрение ≠ успех'),
    (r'Mini-failure:', 'Мини-провал:'),
    (r'mini-failure block', 'мини-провал блок'),
    (r'mini-failure', 'мини-провал'),
    (r'MINI-FAILURE', 'МИНИ-ПРОВАЛ'),
    (r'Mini-failure', 'Мини-провал'),
    (r'likeness rights', 'права на образ'),
    (r'explicit consent', 'явное согласие'),
    (r'consent для real persons', 'согласие для реальных людей'),
    (r'consent infrastructure', 'инфраструктура получения согласия'),

    # Discovery / motion
    (r'Discovery \+ motion war', 'Истребование доказательств + борьба за процессуальные действия'),
    (r'discovery', 'истребование доказательств'),
    (r'Discovery', 'Истребование доказательств'),

    # Decision branch
    (r'ЕСЛИ «НЕТ/РИСК» — 3 OPTION\'А', 'ЕСЛИ «НЕТ/РИСК» — 3 ВАРИАНТА'),
    (r'OPTION\'А', 'ВАРИАНТА'),
    (r'3 OPTION\'А', '3 ВАРИАНТА'),
    (r'\boption\'а\b', 'варианта'),
    (r'Documented business decision', 'Документированное бизнес-решение'),
    (r'Accept risk явно', 'Явно принять риск'),
    (r'Структурно митигировать', 'Структурно митигировать'),
    (r'Human alternative', 'Альтернатива без AI'),
    (r'calibrated mitigation', 'выверенная митигация'),

    # Multilingual dubbing
    (r'multilingual dubbing', 'дубляж на несколько языков'),
    (r'Multilingual dubbing', 'Дубляж на несколько языков'),
    (r'Multilingual · expressive', 'Многоязычный · выразительный'),
    (r'Long-form: недели → минуты', 'Long-form: недели → минуты'),
    (r'long-form', 'длинный формат'),
    (r'Long-form', 'Длинный формат'),
    (r'Long-form coherent narrative', 'Длинный когерентный нарратив'),
    (r'long-form narrative', 'нарратив длинного формата'),
    (r'dubbing на язык', 'дубляж на язык'),
    (r'Dub /мин /язык', 'Дубляж $/мин/язык'),
    (r'Dub long-form', 'Дубляж длинного формата'),
    (r'long-form album', 'альбом длинного формата'),

    # Workflow
    (r'workflow', 'процесс'),
    (r'Workflow', 'Процесс'),
    (r'WORKFLOW', 'ПРОЦЕСС'),

    # Stock
    (r'stock photos', 'стоковые фото'),
    (r'Stock photos', 'Стоковые фото'),
    (r'stock photo', 'стоковое фото'),
    (r'stock images', 'стоковые картинки'),
    (r'stock snapshots', 'стоковые снимки'),
    (r'\$25-100 stock', '$25-100 стоковое фото'),
    (r'stock \$25-100', 'сток $25-100'),
    (r'/ stock \$25-100', '/ сток $25-100'),
    (r'\bstock\b', 'сток'),

    # Freelance
    (r'freelance designer', 'дизайнер-фрилансер'),
    (r'freelance \$50-200', 'фриланс $50-200'),
    (r'freelance', 'фриланс'),
    (r'Freelance', 'Фриланс'),
    (r'bottom freelance', 'низовой фриланс'),

    # Capability — keep as "возможность" / "функция"
    (r'Новые capabilities — то, чего раньше технологически не было',
     'Новые возможности — то, чего раньше технологически не было'),
    (r'Новые capabilities, которых раньше технологически не было',
     'Новые возможности, которых раньше технологически не было'),
    (r'Новые capabilities: text-to-video · character consistency · voice cloning · world models',
     'Новые возможности: text-to-video · сохранение персонажа · клонирование голоса · world models'),
    (r'Новые capabilities: text-to-video, character consistency, voice cloning, world models',
     'Новые возможности: text-to-video, сохранение персонажа, клонирование голоса, world models'),
    (r'Доступная capability \+ слабый enforcement',
     'Доступная возможность + слабый правоприменительный контроль'),
    (r'consumer-facing AI tools', 'AI-инструменты для конечных пользователей'),
    (r'consumer-facing AI visuals', 'AI-визуалы для конечных пользователей'),
    (r'consumer-facing', 'для конечных пользователей'),
    (r'\bconsumer\b', 'конечный пользователь'),
    (r'\bcapabilities\b', 'возможности'),
    (r'\bcapability\b', 'возможность'),
    (r'capability creative-индустри', 'возможность для творческих индустрий'),
    (r'capabilities creative-индустри', 'возможности для творческих индустрий'),
    (r'\benforcement\b', 'правоприменительный контроль'),

    # Hype demo
    (r'hype demo', 'демо для шумихи'),
    (r'hype-demo', 'демо для шумихи'),

    # Cinematic / pipeline / VFX
    (r'Cinematic pipeline', 'Кинематографический pipeline'),
    (r'cinematic pipeline', 'кинематографический pipeline'),
    (r'Pre-production', 'Препродакшн'),
    (r'pre-production', 'препродакшн'),
    (r'Post-production', 'Постпродакшн'),
    (r'post-production', 'постпродакшн'),
    (r'pre/post-production', 'препродакшн/постпродакшн'),
    (r'previsualization', 'предвизуализация'),
    (r'storyboarding', 'сториборды'),
    (r'\bVFX\b', 'VFX'),

    # Cameos
    (r'Sora 2 cameos', 'Sora 2 cameos'),  # keep — established term

    # Adoption / augmentation
    (r'Lionsgate × Runway = augmentation, не replacement',
     'Lionsgate × Runway = усиление, а не замещение'),
    (r'augmentation, не replacement', 'усиление, а не замещение'),
    (r'augmentation, а не replacement', 'усиление, а не замещение'),
    (r'\baugmentation\b', 'усиление'),
    (r'\breplacement\b', 'замещение'),
    (r'replacement layer', 'слой замещения'),
    (r'augments stages', 'усиливает стадии'),

    # Direct revenue / FY
    (r'direct revenue 2024-25', 'прямая выручка 2024-25'),
    (r'direct revenue FY 2024-25', 'прямая выручка фискальный год 2024-25'),
    (r'direct revenue', 'прямая выручка'),
    (r'\bFY 2024-25\b', 'фискальный год 2024-25'),
    (r'\bFY\b', 'фискальный год'),

    # Earnings call
    (r'earnings call', 'звонок по итогам квартала'),

    # Empirical
    (r'Empirical end-user rejection', 'Эмпирическое отторжение конечными пользователями'),
    (r'empirical end-user rejection', 'эмпирическое отторжение конечными пользователями'),
    (r'End-users замечают и наказывают AI shortcut',
     'Конечные пользователи замечают и наказывают AI-срезание углов'),
    (r'end-user', 'конечный пользователь'),
    (r'end-users', 'конечные пользователи'),
    (r'End-users', 'Конечные пользователи'),
    (r'AI shortcut', 'AI-срезание углов'),
    (r'CTR drop', 'падение CTR'),
    (r'drop-off', 'отвал'),
    (r'first-15-sec drop-off', 'отвал в первые 15 сек'),
    (r'creepy skin', 'жуткая кожа'),
    (r'mobile text fail', 'провал текста на мобильных'),
    (r'mismatched promise/content', 'несоответствие обещания и контента'),
    (r'creators dropped', 'креаторов отказались от'),
    (r'creators dropped\nAI thumbnails', 'креаторов отказались от\nAI-превью'),
    (r'AI thumbnails', 'AI-превью'),
    (r'YouTube AI thumbnails', 'YouTube AI-превью'),
    (r'thumbnails', 'превью'),

    # Mockup
    (r'Voice list mockup', 'Список голосов'),
    (r'mockup', 'мокап'),

    # Investigative journalism
    (r'Investigative journalism', 'Расследовательская журналистика'),
    (r'investigative journalism', 'расследовательская журналистика'),
    (r'investigative scandal', 'расследовательский скандал'),
    (r'NYT/WaPo guidelines прохибит AI для original reporting',
     'NYT/WaPo гайдлайны запрещают AI для первичного репортажа'),
    (r'original reporting', 'первичный репортаж'),
    (r'Source verification', 'Проверка источников'),
    (r'source verification', 'проверка источников'),
    (r'On-record interviews', 'Интервью под запись'),
    (r'on-record interviews', 'интервью под запись'),
    (r'Accountability journalism', 'Журналистика подотчётности'),
    (r'accountability journalism', 'журналистика подотчётности'),
    (r'human-only', 'только человеком'),
    (r'human ответственность не делегируема',
     'человеческая ответственность не делегируема'),

    # Original creative
    (r'Original creative direction', 'Оригинальное творческое руководство'),
    (r'original creative direction', 'оригинальное творческое руководство'),

    # Single-word vocabulary
    (r'\bgenerator\b', 'генератор'),
    (r'simulated environment', 'симулированное окружение'),
    (r'edge cases', 'граничные случаи'),
    (r'game proto', 'игровой прототип'),
    (r'location scouting', 'разведка локаций'),
    (r'\bFrontier-grade\b', 'Frontier-grade'),  # keep
    (r'frontier впереди', 'frontier ещё впереди'),
    (r'frontier-quality на видео и музыке', 'frontier-уровень в видео и музыке'),
    (r'не frontier на видео и музыке', 'не frontier-уровень в видео и музыке'),

    # Russian context
    (r'Russian context: local convenience vs frontier',
     'Российский контекст: локальное удобство vs frontier'),
    (r'local convenience vs frontier', 'локальное удобство vs frontier'),
    (r'Local convenience \(бесплатно · RU-промпты · без VPN · рубли · правовой контур\) ≠ frontier-quality на видео и музыке',
     'Локальное удобство (бесплатно · RU-промпты · без VPN · рубли · правовой контур) ≠ frontier-уровень в видео и музыке'),
    (r'Local convenience', 'Локальное удобство'),
    (r'local convenience', 'локальное удобство'),
    (r'RU GenAI функционален для consumer \+ masstige',
     'Российский GenAI функционален для consumer + masstige'),
    (r'\bmasstige\b', 'масс-маркет премиум'),
    (r'RU GenAI', 'российский GenAI'),
    (r'RU-промпты', 'RU-промпты'),  # keep
    (r'правовой контур', 'правовой контур'),
    (r'Структурно \(capex/data\), не идеологически',
     'Структурно (capex/data), а не идеологически'),
    (r'concentration R&D в US/CN — структурное',
     'концентрация R&D в US/CN — структурное'),
    (r'Концентрация R&D в US/CN — структурное \(capex GPU, video-датасеты\), не идеологическое',
     'Концентрация R&D в США/Китае — структурное (capex GPU, video-датасеты), не идеологическое'),
    (r'capex GPU, video-датасеты', 'capex GPU, видео-датасеты'),
    (r'gap structural', 'структурный gap'),
    (r'Frontier gap vs Sora/Veo/Kling', 'Frontier-gap vs Sora/Veo/Kling'),
    (r'ниже ElevenLabs', 'ниже ElevenLabs'),
    (r'в процессе', 'в процессе'),
    (r'конкурентен', 'конкурентен'),

    # Sub-labels in cards / matrices
    (r'INPUT SIDE', 'СО СТОРОНЫ ВХОДА'),
    (r'OUTPUT SIDE', 'СО СТОРОНЫ ВЫХОДА'),
    (r'«В СТИЛЕ NAMED ARTIST»', '«В СТИЛЕ КОНКРЕТНОГО ХУДОЖНИКА»'),
    (r'RIGHT OF PUBLICITY', 'ПРАВО НА ОБРАЗ'),
    (r'PRODUCTION USE', 'ПРОМЫШЛЕННОЕ ПРИМЕНЕНИЕ'),
    (r'production users', 'промышленные пользователи'),
    (r'MIDDLE-TIER ≠ FREE', 'СРЕДНИЙ СЕГМЕНТ ≠ БЕСПЛАТНО'),
    (r'middle-tier растёт', 'средний сегмент растёт'),
    (r'middle-tier', 'средний сегмент'),
    (r'bottom-tier вымывается', 'нижний сегмент вымывается'),
    (r'bottom-tier', 'нижний сегмент'),
    (r'top-tier защищённым', 'верхний сегмент защищённым'),
    (r'top-tier', 'верхний сегмент'),
    (r'\bbottom-tier\b', 'нижний сегмент'),
    (r'enterprise SaaS-стек', 'корпоративный SaaS-стек'),
    (r'enterprise commercial-safe', 'корпоративный коммерчески-безопасный'),
    (r'enterprise', 'корпоративный'),
    (r'\benterprise\b', 'корпоративный сегмент'),
    (r'corporate', 'корпоративный'),

    # 2026 metric labels
    (r'МЕТРИКИ 2026', 'МЕТРИКИ 2026'),  # keep
    (r'ИНСТРУМЕНТЫ 2026', 'ИНСТРУМЕНТЫ 2026'),  # keep
    (r'ХАРАКТЕРИСТИКИ', 'ХАРАКТЕРИСТИКИ'),  # keep
    (r'ХРОНОЛОГИЯ', 'ХРОНОЛОГИЯ'),  # keep
    (r'ИНЖЕНЕРНОЕ СЛЕДСТВИЕ', 'ИНЖЕНЕРНОЕ СЛЕДСТВИЕ'),  # keep
    (r'ПРИНЦИП', 'ПРИНЦИП'),  # keep
    (r'СЦЕНАРИЙ АТАКИ', 'СЦЕНАРИЙ АТАКИ'),  # keep
    (r'ЦИФРЫ КРИЗИСА', 'ЦИФРЫ КРИЗИСА'),  # keep
    (r'4 НОВЫЕ РОЛИ', '4 НОВЫЕ РОЛИ'),  # keep

    # Cost-collapse arrow text labels
    (r'COST-COLLAPSE: dubbing на язык',
     'ОБВАЛ СТОИМОСТИ: дубляж на язык'),
    (r'COST-COLLAPSE', 'ОБВАЛ СТОИМОСТИ'),

    # 4 categories + lessons block
    (r'AI vs copyright', 'AI и авторское право'),
    (r'INPUT SIDE', 'СО СТОРОНЫ ВХОДА'),
    (r'OUTPUT SIDE', 'СО СТОРОНЫ ВЫХОДА'),
    (r'Training scraping', 'Парсинг для обучения'),
    (r'training scraping', 'парсинг для обучения'),

    # Time / iteration loop
    (r'iteration loop становится 10-100× плотнее', 'итерационный цикл становится 10-100× плотнее'),
    (r'iteration loop 10-100× плотнее → новые навыки человека',
     'итерационный цикл 10-100× плотнее → новые навыки человека'),
    (r'итерация плотнее', 'итерация плотнее'),
    (r'iteration loop', 'итерационный цикл'),
    (r'Iteration loop', 'Итерационный цикл'),

    # B-roll / shoot
    (r'B-roll кадр', 'B-roll кадр'),  # keep
    (r'часы съёмки \+ post', 'часы съёмки + постпродакшн'),
    (r'shoot \+ post', 'съёмка + постпродакшн'),
    (r'\$1k-25k full photo', '$1-25 тыс. фотосет'),
    (r'\$1k-50k shoot\+post', '$1-50 тыс. съёмка+постпродакшн'),

    # Models / class
    (r'MoE, GigaChat free', 'MoE, бесплатно через GigaChat'),
    (r'GigaChat free', 'бесплатно через GigaChat'),

    # New professions
    (r'Новые профессии: prompt engineer · AI director · workflow specialist',
     'Новые профессии: prompt-инженер · AI-режиссёр · процесс-специалист'),
    (r'Специализированный класс между AI-инструментом и client deliverable',
     'Специализированный класс между AI-инструментом и итоговым продуктом для клиента'),
    (r'между AI-tool и client deliverable',
     'между AI-инструментом и итоговым продуктом для клиента'),
    (r'client deliverable', 'итоговый продукт для клиента'),
    (r'Prompt engineer / AI artist', 'Prompt-инженер / AI-художник'),
    (r'Prompt engineer · Midjourney expert', 'Prompt-инженер · Midjourney эксперт'),
    (r'AI director / AI music producer', 'AI-режиссёр / AI-музыкальный продюсер'),
    (r'AI director / supervisor', 'AI-режиссёр / супервайзер'),
    (r'AI director', 'AI-режиссёр'),
    (r'GenAI workflow specialist · enterprise', 'GenAI процесс-специалист · корпоративный'),
    (r'GenAI workflow specialist', 'GenAI процесс-специалист'),
    (r'AI continuity supervisor · video', 'AI континьюити-супервайзер · видео'),
    (r'AI continuity supervisor', 'AI континьюити-супервайзер'),
    (r'Continuity-supervisor', 'Континьюити-супервайзер'),
    (r'continuity-supervisor', 'континьюити-супервайзер'),
    (r'Supervisor model output', 'Супервайзер вывода моделей'),
    (r'Интегратор AI-tools', 'Интегратор AI-инструментов'),
    (r'Adobe Firefly Foundry-deploys', 'развёртывания Adobe Firefly Foundry'),
    (r'Проверка character/scene continuity в multi-shot',
     'Проверка непрерывности персонажа/сцены в мульти-кадре'),
    (r'character/scene continuity', 'непрерывность персонажа/сцены'),
    (r'\bcontinuity\b', 'непрерывность'),
    (r'Multi-scene drift control', 'Контроль drift между сценами'),
    (r'Аналог art director\'а', 'Аналог арт-директора'),
    (r'art director', 'арт-директор'),
    (r'Формирует промпты \+ post-processing → production-ready output',
     'Формирует промпты + постобработка → готовый к публикации результат'),
    (r'production-ready output', 'готовый к публикации результат'),
    (r'production-ready', 'готовый к публикации'),
    (r'post-processing', 'постобработка'),
    (r'iterations \+ post \+ multimodal', 'итерации + постобработка + мультимодальность'),
    (r'specialized класс', 'специализированный класс'),

    # Search prompt
    (r'Search: AI / ML / prompt engineering',
     'Поиск: AI / ML / prompt engineering'),
    (r'AI/ML CATEGORY', 'КАТЕГОРИЯ AI/ML'),
    (r'GRAPHIC DESIGN YoY', 'GRAPHIC DESIGN ГОД К ГОДУ'),
    (r'jobs in graphic design', 'работ в графическом дизайне'),
    (r'graphic design jobs\nUpwork YoY', 'работ графического дизайна\nUpwork год к году'),
    (r'graphic design jobs', 'работ графического дизайна'),
    (r'\b40%\s+работ\s+writers\s+\$10-19/час',
     '40% работ копирайтеров $10-19/час'),
    (r'работ writers \$10-19/час — AI-detected',
     'работ копирайтеров $10-19/час — распознаны как AI'),
    (r'работ \$10-19/час vs\n\$60\+/час · AI-detected',
     'работ $10-19/час vs\n$60+/час · распознаны как AI'),
    (r'wage-compression снизу остаётся', 'снижение зарплат снизу остаётся'),
    (r'Понимай, какой класс labor твой AI-deploy сместит',
     'Понимай, какой класс работников твой AI-проект вытеснит'),
    (r'класс labor', 'класс работников'),
    (r'labor', 'труд'),

    # Section labels
    (r'AI ДОБАВИЛ', 'AI ДОБАВИЛ'),  # keep
    (r'AI ИЗМЕНИЛ', 'AI ИЗМЕНИЛ'),  # keep
    (r'AI СЛОМАЛ', 'AI СЛОМАЛ'),  # keep
    (r'AI как ассистент', 'AI как ассистент'),

    # Sora release etc
    (r'OPENAI SORA · LAUNCH DEMO · YOUTUBE', 'OPENAI SORA · ДЕМО ПРИ ЗАПУСКЕ · YOUTUBE'),
    (r'launch demo', 'демо при запуске'),
    (r'Launch Demo', 'Демо при запуске'),
    (r'iconic demo from launch', 'эталонное демо при запуске'),
    (r'release demo frame', 'кадр из демо-релиза'),
    (r'OFFICIAL DEMO REEL', 'ОФИЦИАЛЬНОЕ ДЕМО'),
    (r'official demo reel', 'официальное демо'),
    (r'official partnership announcement', 'официальное объявление о партнёрстве'),
    (r'announcement banner', 'баннер с объявлением'),
    (r'official cover artwork', 'официальная обложка'),

    # Toys / Coca-Cola
    (r'SENTIMENT SWING \(June 2024\)', 'РАЗВОРОТ ТОНАЛЬНОСТИ (Июнь 2024)'),
    (r'AI HOLIDAY · BACKLASH', 'AI-РЕКЛАМА · НЕГАТИВ'),
    (r'AI HOLIDAY', 'AI-РЕКЛАМА К ПРАЗДНИКАМ'),
    (r'«Soulless» · «creepy faces» · «truck wheels spin wrong»',
     '«Бездушно» · «жуткие лица» · «колёса грузовика крутятся не туда»'),
    (r'70 000 AI clips · viral mockery', '70 000 AI-клипов · вирусные насмешки'),
    (r'POSITIVE', 'ПОЛОЖИТЕЛЬНЫЕ'),
    (r'NEGATIVE', 'ОТРИЦАТЕЛЬНЫЕ'),
    (r'\bpp positive\b', 'п.п. положительных'),
    (r'\bpp negative\b', 'п.п. отрицательных'),
    (r'\b−10pp\b', '−10 п.п.'),
    (r'\b−8\.8 pp\b', '−8.8 п.п.'),
    (r'\b\+39\.9 pp\b', '+39.9 п.п.'),
    (r'\bpp\b', 'п.п.'),

    # Photo / hero
    (r'hero image', 'главное изображение'),
    (r'hero artwork', 'главная иллюстрация'),
    (r'hero illustration', 'главная иллюстрация'),
    (r'logos collage', 'коллаж логотипов'),
    (r'ELEVENLABS · OFFICIAL · elevenlabs\.io', 'ELEVENLABS · ОФИЦИАЛЬНО · elevenlabs.io'),
    (r'KELLY McKERNAN \(PLAINTIFF\) · WIKIMEDIA COMMONS', 'KELLY McKERNAN (ИСТЕЦ) · WIKIMEDIA COMMONS'),
    (r'\(PLAINTIFF\)', '(ИСТЕЦ)'),
    (r'\bPLAINTIFF\b', 'ИСТЕЦ'),
    (r'\bplaintiff\b', 'истец'),
    (r'\bdefendant\b', 'ответчик'),
    (r'CHARACTER REFERENCE', 'РЕФЕРЕНС ПЕРСОНАЖА'),
    (r'character reference', 'референс персонажа'),
    (r'Character Reference', 'Референс персонажа'),
    (r'Omni Reference', 'Omni Reference'),  # keep brand-feature name
    (r'cw=0 vs cw=100', 'cw=0 vs cw=100'),  # keep param names
    (r'consistency weight', 'consistency weight'),  # keep param
    (r'knight in forest', '«рыцарь в лесу»'),
    (r'«knight in forest» × «old man»', '«рыцарь в лесу» × «старик»'),
    (r'old man', '«старик»'),

    # ENTERPRISE / users
    (r'ENTERPRISE USERS', 'КОРПОРАТИВНЫЕ КЛИЕНТЫ'),
    (r'enterprise users', 'корпоративные клиенты'),
    (r'enterprise SaaS', 'корпоративный SaaS'),
    (r'enterprise-deploys', 'корпоративные внедрения'),
    (r'video ads — AI-generated \(IAB 2026\)',
     'видеореклама — AI-сгенерирована (IAB 2026)'),
    (r'AI-generated', 'AI-сгенерированный'),
    (r'video ads', 'видеореклама'),
    (r'AI/ML', 'AI/ML'),  # keep

    # Cost rows in table s14
    (r'1 image', '1 картинка'),
    (r'50 product images', '50 продуктовых картинок'),
    (r'1 мин 720p video', '1 мин видео 720p'),
    (r'\$50-500 actor\+studio', '$50-500 актёр+студия'),
    (r'\$1k-25k full photo', '$1-25 тыс. фотосет'),
    (r'\$1k-50k shoot\+post', '$1-50 тыс. съёмка+постпродакшн'),

    # Brief context
    (r'IP-clean tools для commercial use', 'IP-чистые инструменты для коммерческого применения'),
    (r'IP-clean tools', 'IP-чистые инструменты'),
    (r'commercial use', 'коммерческое применение'),
    (r'commercial creative', 'коммерческая реклама'),
    (r'commercial-safety', 'коммерческая безопасность'),
    (r'commercial-safe', 'коммерчески безопасный'),
    (r'video gen', 'видеогенерация'),
    (r'video-датасет', 'видео-датасет'),
    (r'video-датасеты', 'видео-датасеты'),

    # Misc
    (r'measurable backlash', 'измеримая негативная реакция'),
    (r'measurable spending brand equity', 'измеримая потеря капитала бренда'),
    (r'measurable CTR \+ drop-off \+ retention', 'измеримые CTR + отвал + retention'),
    (r'measurable', 'измеримый'),
    (r'main deliverable лекции', 'главный итог лекции'),
    (r'main deliverable', 'главный итог'),
    (r'taxonomy', 'таксономия'),
    (r'Actionable checklist', 'Чек-лист к действию'),
    (r'actionable checklist', 'чек-лист к действию'),
    (r'5-вопросный', '5-вопросный'),  # keep
    (r'critery отказа', 'критерия отказа'),
    (r'4 critery отказа от AI', '4 критерия отказа от AI'),
    (r'Identifiable real persons — всегда consent',
     'Узнаваемые реальные люди — всегда согласие'),
    (r'Identifiable real persons', 'Узнаваемые реальные люди'),

    # Final closing
    (r'СЛЕДУЮЩАЯ ЛЕКЦИЯ', 'СЛЕДУЮЩАЯ ЛЕКЦИЯ'),  # keep
    (r'От публичного contact surface — к safety-critical',
     'От публичной контактной поверхности — к безопасности-критичному'),
    (r'contact surface', 'контактная поверхность'),
    (r'safety-critical', 'безопасности-критичный'),

    # Generic technical
    (r'inherent limits', 'фундаментальные ограничения'),
    (r'inherent limit', 'фундаментальное ограничение'),
    (r'temporal consistency', 'временная консистентность'),
    (r'temporal drift', 'временной drift'),
    (r'autoregressive', 'авторегрессионный'),
    (r'fine-tuning pre-trained foundation', 'дообучение предобученной foundation-модели'),
    (r'foundation-модели', 'foundation-модели'),  # keep — domain term
    (r'pre-trained', 'предобученный'),
    (r'\bfine-tuning\b', 'дообучение'),
    (r'from-scratch', 'с нуля'),
    (r'Reference-image character\'а сохраняет propertion лица/одежды/посадки',
     'Референс-изображение персонажа сохраняет пропорции лица/одежды/посадки'),
    (r'character\'а', 'персонажа'),
    (r'Регистрируется character — вызывается по имени',
     'Регистрируется персонаж — вызывается по имени'),
    (r'Image-to-image accuracy', 'Точность image-to-image'),
    (r'Multi-scene scripting через structured objects',
     'Скриптинг между сценами через structured objects'),
    (r'Character \+ locations \+ motion patterns как constants для всех scenes',
     'Персонаж + локации + паттерны движения как константы для всех сцен'),
    (r'для всех scenes', 'для всех сцен'),
    (r'scene\'ов', 'сцен'),
    (r'5-10 scene\'ов', '5-10 сцен'),

    # Misc body
    (r'audio-version', 'аудио-версия'),
    (r'image-version', 'image-версия'),

    # Russified Korean translation already in s27 — keep
    # Other UI bits
    (r'photo monogram-tile', 'монограммная плитка с фото'),
    (r'inline gloss', 'инлайн-пояснение'),

    # Marketing tooltip text already on slides
    (r'wage-compression снизу остаётся', 'снижение зарплат снизу остаётся'),
    (r'НЕ строй product roadmap на assumption fair-use defence',
     'НЕ строй продуктовый roadmap на предположении «добросовестного использования»'),
    (r'product roadmap', 'продуктовый roadmap'),
    (r'на assumption', 'на предположении'),
    (r'assumption', 'предположение'),
    (r'roadmap', 'дорожная карта'),

    # ScarJo / SAG
    (r'ScarJo-class risk \+ SAG-AFTRA \+ Korea',
     'риск класса ScarJo + SAG-AFTRA + Корея'),
    (r'ScarJo-class', 'класса ScarJo'),

    # Logging
    (r'logos\b', 'логотипы'),
    (r'card', 'карточка'),  # only when not part of "carded"; this is risky — let me undo
]

# Remove the broad "card" → "карточка" rule (too risky)
REPLACEMENTS = [r for r in REPLACEMENTS if r[0] != r'card']


def count_anglicisms(text):
    """Count occurrences of all major suspicious anglicism patterns."""
    patterns = [
        r'production-уровень', r'capability', r'capabilities', r'freelance ', r' stock ',
        r'hype demo', r'fair use', r'fair-use', r'lawsuit-driven', r'out-of-band',
        r'multi-factor', r'MAJORS', r'Settlement matrix', r'verbatim', r'regurgitation',
        r'sham books', r'top-bestseller', r'AI-pseudonyms', r'AI-disclosed',
        r'Backup screenshot', r'iconic seasonal creative', r'brand damage',
        r'training corpus', r'curated dataset', r'licensed corpus', r'scraped web',
        r'reflexively', r'legacy trust', r'brand asset', r'class action',
        r'Sentiment swing', r'identity proof', r'documented workflow',
        r'callback no known number', r'creative-индустри', r'asset-классам',
        r'Cost-collapse', r'training\+output similarity', r'enterprise users',
        r'wage compression', r'sham author',
    ]
    total = 0
    for p in patterns:
        total += len(re.findall(p, text, flags=re.IGNORECASE))
    return total


def apply_replacements(text, replacements):
    out = text
    for pat, repl in replacements:
        try:
            out = re.sub(pat, repl, out)
        except Exception as e:
            print(f"  WARN: pattern '{pat}' failed: {e}")
    return out


def process_file(path):
    text = path.read_text(encoding='utf-8')
    before_count = count_anglicisms(text)
    new_text = apply_replacements(text, REPLACEMENTS)
    after_count = count_anglicisms(new_text)
    changed = (new_text != text)
    if changed:
        path.write_text(new_text, encoding='utf-8')
    return before_count, after_count, changed


def main():
    log_lines = [f"# Russification Log — Лекция 8\n\nGenerated: {datetime.now().isoformat()}\n\n"]
    log_lines.append("## Per-file anglicism counts (before → after)\n\n")

    # Process slides
    log_lines.append("### Slides\n\n")
    log_lines.append("| Slide | Before | After | Changed |\n")
    log_lines.append("|---|---|---|---|\n")
    md_files = sorted(SLIDES.glob("*.md"))
    total_before, total_after = 0, 0
    for f in md_files:
        b, a, c = process_file(f)
        total_before += b
        total_after += a
        marker = "yes" if c else "no"
        log_lines.append(f"| {f.name} | {b} | {a} | {marker} |\n")
    log_lines.append(f"\n**Total slides: {total_before} → {total_after}**\n\n")

    # Process build script
    log_lines.append("### Build script\n\n")
    b, a, c = process_file(BUILD)
    log_lines.append(f"| build_lec08.py | {b} | {a} | {'yes' if c else 'no'} |\n")

    # Sample suspicious leftover patterns
    log_lines.append("\n## Sample leftover patterns (after pass)\n\n")
    suspicious = [
        'production-уровень', 'capability', 'capabilities', 'freelance ',
        'hype demo', 'fair use', 'fair-use', 'lawsuit-driven', 'out-of-band',
        'multi-factor', 'MAJORS', 'Settlement matrix', 'verbatim', 'regurgitation',
        'top-bestseller', 'AI-pseudonyms', 'AI-disclosed',
        'Backup screenshot', 'iconic seasonal creative', 'brand damage',
        'training corpus', 'curated dataset', 'licensed corpus', 'scraped web',
        'reflexively', 'legacy trust', 'brand asset', 'class action',
        'Sentiment swing', 'identity proof', 'documented workflow',
        'callback no known number', 'creative-индустри', 'asset-классам',
        'Cost-collapse',
    ]
    leftover = {}
    for f in md_files + [BUILD]:
        text = f.read_text(encoding='utf-8')
        for pat in suspicious:
            cnt = len(re.findall(pat, text, flags=re.IGNORECASE))
            if cnt:
                leftover.setdefault(pat, []).append((f.name, cnt))
    if leftover:
        log_lines.append("Patterns still present (need manual review):\n\n")
        for pat, hits in sorted(leftover.items()):
            log_lines.append(f"- `{pat}`: {sum(c for _, c in hits)} hits across {len(hits)} files\n")
            for fn, cnt in hits[:5]:
                log_lines.append(f"  - {fn}: {cnt}\n")
    else:
        log_lines.append("All sample patterns cleaned.\n")

    LOG.write_text(''.join(log_lines), encoding='utf-8')
    print(f"Total slides anglicisms: {total_before} → {total_after}")
    print(f"Log written to {LOG}")


if __name__ == "__main__":
    main()
