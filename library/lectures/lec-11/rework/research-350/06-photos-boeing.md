# Лог добычи фото Boeing 737 MAX 9 / Alaska Airlines 1282 (issue #353)

Задача: найти ≥5 настоящих фотографий кейса Alaska Airlines 1282 (вырванная дверная заглушка,
5 января 2024) на четыре темы — (а) вырванная заглушка / дыра в фюзеляже, (б) отсутствующие
болты, (в) цех Boeing Renton, (г) салон самолёта. Правила — `CLAUDE.md` hero-images-required +
no-mock-fallbacks, `tools/presentation-build/trebovaniya-k-soderzhaniyu.md` §5.7 (6-tier
acquisition). Разбор кейса уже в деке: `slides/s13-boeing-sobytie-khronologiya.md` +
`slides/s14-boeing-cena-podmena.md` — до этой добычи у s13 был только один общий stock-снимок
самолёта на взлёте (`s15-alaska-737-max9.jpg`, без привязки к инциденту), у s14 `media: ""`.

**Итог: 7 файлов, все — настоящие фотографии, без единой стилизованной подделки.** 5 основных
(по одному на каждую тему + запасной на тему (а)) + 2 бонусных forensic-кадра на тему (б).
Все источники — Wikimedia Commons (переиздание NTSB/госфото, public domain) или сам финальный
отчёт NTSB AIR-25-04 (10.07.2025, он же уже процитирован в `s13` как `source:`).

## Tier сработал: 2 (Wikimedia Commons) для 5 из 7 файлов, прямое извлечение из PDF отчёта NTSB для 2 из 7

Wikimedia Commons категория `Category:Alaska_Airlines_Flight_1282` — 24 файла, почти все
атрибутированы «National Transportation Safety Board», лицензия **Public domain** (работа
федерального агентства США, 17 U.S.C. § 105). Отдельно — категория
`Category:Boeing_Renton_Factory` дала фото цеха из фотоархива Госдепартамента США (тоже public
domain). Для «отсутствующих болтов» ни Wikipedia, ни новостные og:image не дали чистого
специализированного снимка — пришлось скачать сам PDF финального отчёта `AIR-25-04` с
`ntsb.gov` (`curl -sLA "Mozilla/5.0" .../AIR2504.pdf`, прямой curl прошёл HTTP 200, 4.4 МБ —
WebFetch на тот же URL вернул 451, см. ниже) и извлечь встроенные JPEG/PNG через `PyMuPDF`
(`fitz`). 20 встроенных изображений постранично; визуально проверены все кандидаты на
страницах 20, 24, 26, 28–35, 40–43 — большинство оказались line-art диаграммами (не
фотографиями, не годятся под задачу), но страницы 40–43 — настоящие лабораторные фотографии
разобранной заглушки с измерительной линейкой и маркировкой экспертизы.

## 1. (а) Вырванная заглушка / дыра в фюзеляже

**`boeing-door-hole-exterior.jpg`** (основной). Источник:
`https://commons.wikimedia.org/wiki/File:Alaska_Airlines_Flight_1282_NTSB_02.jpg`, автор NTSB,
public domain, снято 7 января 2024 в Портленде. Видно: фюзеляж Alaska Airlines 737-9 MAX
(борт N704AL) на земле, проём от вырванной заглушки заклеен жёлтой плёнкой изнутри (виден
контур проёма на фоне остальных овальных иллюминаторов), рядом оранжевая стремянка техобслуживания
Horizon. Разрешение исходника 2420×1816.

**`boeing-door-plug-recovered.jpg`** (запасной/альтернативный кадр для (а), сама физическая
деталь). Источник:
`https://commons.wikimedia.org/wiki/File:Alaska_1282_door_plug_NTSB_02.jpg`, автор NTSB, public
domain. Два следователя NTSB (куртки с лейблом NTSB) держат найденную заглушку на лужайке в
Cedar Mill, Орегон (двор дома, где заглушку нашёл местный житель-учитель) — виден проём от
иллюминатора в самой панели заглушки, днём, при хорошем освещении. Разрешение 4949×3299.

## 2. (б) Отсутствующие болты

**`boeing-missing-bolts-ntsb-lab.jpg`** (основной). Источник: извлечено из
`https://www.ntsb.gov/investigations/AccidentReports/Reports/AIR2504.pdf`, Figure 13, стр. 30
(«Photographs showing two views of the vertical movement arrestor bolt holes»). Это настоящая
лабораторная макро-фотография — два ракурса нижнего шарнирного узла заглушки с жёлтой
измерительной линейкой-шкалой, именно тех двух вертикальных стопорных болтов (vertical
movement arrestor bolts), которые входят в число четырёх болтов, не возвращённых на место
18–19 сентября 2023 (см. текст отчёта стр. 30: «The vertical movement arrestor bolt holes in
the aft lower hinge guide fitting were intact and undamaged»).

**`boeing-bolt-hole-detail-enamel.jpg`** (бонус, второй forensic-кадр на ту же тему). Источник:
тот же PDF, Figure 12, стр. 29 («Multiple views of the forward upper guide fitting on the left
MED plug») — четыре макро-ракурса отверстий под верхние направляющие болты (upper guide track
bolt) с подписями эксперта «Roller contact», «Intact enamel», «Intact hole» прямо на снимке;
это вторая пара из четырёх снятых и не возвращённых болтов. Отдельная экспертная табличная
подпись к снимку (`Upper guide track bolt holes`) делает кадр читаемым даже без остального
текста отчёта.

**`boeing-door-plug-ntsb-lab-frame.jpg`** (бонус, общий план). Источник:
`https://commons.wikimedia.org/wiki/File:Alaska_Airlines_door_plug_inspected_at_NTSB_lab.jpg`,
автор NTSB, public domain. Общий план материаловедческой лаборатории NTSB в Вашингтоне:
два эксперта осматривают раму заглушки (зелёное защитное покрытие, виден контур
иллюминатора и привалочные отверстия по периметру) на столе, в упаковке bubble wrap. Разрешение
4096×2731. Годится как establishing-кадр перед макро-снимками выше, но сам по себе не
показывает отсутствие болтов крупным планом — поэтому не основной, а бонусный.

**ВАЖНО — что НЕ нашлось и не было сфабриковано.** Широко цитируемое в прессе фото (текстовое
сообщение между сотрудниками Boeing от 19 сентября 2023, показывающее закрытую заглушку без
трёх из четырёх болтов) упоминается в отчёте NTSB текстом и обсуждается в новостях (CNN, NBC,
The Hill — см. цитаты ниже), но сам кадр — скриншот телефона сотрудника Boeing, включённый в
docket NTSB как приложение, а не как Figure в итоговом PDF-отчёте; в открытых источниках
(Wikimedia Commons, og:image новостных статей) идентичного файла найти не удалось за время
добычи. Два лабораторных forensic-снимка выше (Figures 12 и 13 финального отчёта) документируют
ровно то же физическое доказательство — отверстия четырёх снятых болтов — и имеют прямую
ссылку на источник, уже процитированный в `s13` (`NTSB, AIR-25-04`), поэтому гап не критичен для
колоды. Если нужен именно кадр с телефона — он лежит в NTSB docket `DCA24MA063`
(`data.ntsb.gov/Docket/Forms/searchdocket`), это отдельный заход, не входивший в данную выборку.

## 3. (в) Цех Boeing Renton

**`boeing-renton-factory-floor.jpg`** (основной). Источник:
`https://commons.wikimedia.org/wiki/File:Boeing_Co._Officials_Show_Secretary_Kerry_737_Assembly_Line_Following_Trade_Speech_at_Plant_in_Washington_(17685396230).jpg`,
фото Госдепартамента США, public domain, снято 19.05.2015. Вид с галереи на линию окончательной
сборки 737 в цехе Renton: несколько фюзеляжей в зелёной защитной грунтовке на стапелях,
подъёмные леса, рабочие места вдоль линии, виден реальный производственный масштаб цеха. Это
не фото конкретно станции установки MED-заглушки (такого кадра в открытом доступе найти не
удалось — внутренние фотографии конкретных рабочих мест Boeing не публикуются), но это
подлинное фото того же цеха (Renton), где по NTSB происходил разбираемый эпизод.
Разрешение 4544×3023.

**Что проверено и отклонено:** второе фото той же серии
(`Secretary Kerry Greets Workers As He Tours the Boeing Co.'s 737 Airplane Factory.jpg`) —
тоже реальный цех Renton, но в кадре превалируют люди на переднем плане (рукопожатие), сам
цех виден хуже; не взято, т.к. один representative-кадр цеха логичнее для слайда.

## 4. (г) Салон самолёта

**`boeing-cabin-interior-hole.jpg`** (основной). Источник:
`https://commons.wikimedia.org/wiki/File:Alaska_Airlines_Flight_1282_NTSB_05.jpg`, автор NTSB,
public domain. Вид изнутри салона на ряд кресел у проёма от вырванной заглушки: виден сам проём
(яркий дневной свет снаружи, обрывки жёлтой тепло-шумоизоляции по краям), свисающие кислородные
маски над соседними рядами, обложки инструкций по безопасности 737-8MAX/9MAX в карманах кресел.
Разрешение 5472×3648 — самый детальный кадр салона из всех найденных.

## 5. Проверка инструментов (для `notes/mcp-limitations.md`, если пригодится)

- **WebFetch на `ntsb.gov` вернул HTTP 451** («Unavailable For Legal Reasons») на прямой URL
  PDF-отчёта. Прямой `curl -sLA "Mozilla/5.0" <url>` с тем же URL отдал HTTP 200 и валидный PDF
  (4 440 843 байт). Разошлось с правилом «не доверять отрицательному ответу WebFetch без прямой
  проверки curl» (`feedback_webfetch_unreliable_on_large_json` в памяти ассистента, тот же
  урок — другой инструмент и другая причина отказа, не JSON-суммаризация, а, похоже,
  геоблокировка/anti-bot на уровне самого WebFetch-прокси).
- `PyMuPDF` (`fitz`) был уже установлен в окружении — извлечение embedded-изображений из PDF
  отчёта прошло без дополнительной установки пакетов.

## 6. Итоговый список файлов (`library/lectures/lec-11/rendered/assets/screenshots/`)

| Файл | Тема | Источник | Лицензия |
|---|---|---|---|
| `boeing-door-hole-exterior.jpg` | (а) дыра в фюзеляже | Wikimedia / NTSB | Public domain |
| `boeing-door-plug-recovered.jpg` | (а) заглушка | Wikimedia / NTSB | Public domain |
| `boeing-missing-bolts-ntsb-lab.jpg` | (б) отсутствующие болты | NTSB AIR-25-04 Fig.13 | Public domain (US govt) |
| `boeing-bolt-hole-detail-enamel.jpg` | (б) бонус | NTSB AIR-25-04 Fig.12 | Public domain (US govt) |
| `boeing-door-plug-ntsb-lab-frame.jpg` | (б) бонус, общий план | Wikimedia / NTSB | Public domain |
| `boeing-renton-factory-floor.jpg` | (в) цех Boeing Renton | Wikimedia / US State Dept | Public domain |
| `boeing-cabin-interior-hole.jpg` | (г) салон самолёта | Wikimedia / NTSB | Public domain |

Существовавший до этой задачи `s15-alaska-737-max9.jpg` (Wikipedia, общий stock-снимок
самолёта на взлёте, без привязки к инциденту) не тронут — остаётся на усмотрение дизайнера,
заменить ли его на `boeing-door-hole-exterior.jpg` при следующей сборке деки.
