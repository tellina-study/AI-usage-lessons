---
lecture: 9
razdel: 2
purpose: "Каталог реальных медиаматериалов для трёх разборов Раздела 2 (телеоперация): Dragon, предсказательная компенсация задержки, Astrobee. Слайды ещё НЕ строятся — это входной материал для дизайнера."
acquisition_method: "6-tier real image acquisition (og:image / Wikimedia Commons / press-release HTML / YouTube thumbnail / Wayback / Google Images), см. tools/presentation-build/README.md"
status: draft
date_compiled: "2026-10-31"
---

# Медиаинвентарь — Раздел 2 («Удалённое управление»), Лекция 9

Файлы на диске: `library/lectures/lec-09/assets/razdel-2/{dragon,latency-compensation,astrobee}/`.
Каждый скачанный файл имеет sidecar `<файл>.url` с полным источником.
Видео и инфографики-ссылки (не скачивались, только каталогизированы) — таблица ниже.

## Фото/иллюстрации — сводка по папкам

| Папка | Файлов | Из них инфографик |
|---|---|---|
| `dragon/` | 7 | 1 (ESA, схема стыковки) |
| `astrobee/` | 10 | 1 (arXiv, warm-start flowchart) |
| `latency-compensation/` | 8 | 1 (arXiv, LSTM-архитектура, НЕ лунно-специфичная — см. честную оговорку в карточке) |

## Таблица: видео + инфографики (ссылки, не скачивались)

| Кейс | Тип | Описание | Ссылка | Источник | Дата доступа | Оценка качества |
|---|---|---|---|---|---|---|
| Dragon | видео | «SpaceX Demo-2 Docking: Crew Dragon arrives at the Space Station with NASA astronauts» — трансляция стыковки Demo-2, 31 мая 2020 | https://www.youtube.com/watch?v=BWprk5ODQ_I | YouTube (заголовок соответствует официальной трансляции NASA TV; канал-издатель не подтверждён независимо — см. честную оговорку ниже) | 2026-10-31 | Высокая (релевантность 1:1, оригинальная съёмка момента) |
| Dragon | видео | «SpaceX Demo-2 Crew Dragon docking» — автономная стыковка с астронавтами Бенкеном и Хёрли на борту | https://www.youtube.com/watch?v=yvmcG1VNYV8 | YouTube | 2026-10-31 | Высокая |
| Dragon | видео | «WATCH: SpaceX/DM-2 Crew Dragon Docking and Hatch Opening — Livestream» — полная трансляция стыковки и открытия люка | https://www.youtube.com/watch?v=zNklfC6jgBs | YouTube (маркирован как Livestream-запись) | 2026-10-31 | Высокая (длинная форма, захватывает весь процесс, не только кульминацию) |
| Dragon | инфографика | «Dragon Docking to the International Space Station» — официальная ESA-инфографика, 8 шагов стыковки (final approach → 220m/20m waypoints → hard capture → 24 hooks → люк) | https://www.esa.int/ESA_Multimedia/Images/2023/08/Dragon_docking_to_the_International_Space_Station | ESA (К. Lochtenberg), 27.08.2023, обновлено 2026 | 2026-10-31 | Отличная — скачана в `dragon/07-INFOGRAPHIC-esa-docking-sequence.png` |
| Предсказательная компенсация задержки | видео | «LUNA ANALOG FACILITY» — обзорное видео объекта DLR/ESA в Кёльне, где проводятся испытания телеоперации в условиях, симулирующих Луну | https://www.youtube.com/watch?v=bUqLjzfbOPk | YouTube | 2026-10-31 | Средняя-высокая (показывает сам полигон, не конкретно ML-эксперимент по компенсации задержки — честная оговорка) |
| Предсказательная компенсация задержки | видео | «LUNA analog facility — The Moon on Earth» — официальное видео ESA Television о назначении и устройстве полигона | https://www.esa.int/esatv/Videos/2024/09/LUNA_analog_facility_The_Moon_on_Earth | ESA Television, сентябрь 2024 | 2026-10-31 | Высокая (официальный источник ESA) |
| Предсказательная компенсация задержки | видео | «Moon mission in preparation — rover tests in the LUNA hall» — испытания микроровера Tenacious (ispace-Europe) под телеоперацией в LUNA | упоминается на https://www.dlr.de/en/latest/news/2024/a-swarm-of-sensors-rovers-and-astronauts-explore-the-moon (точный YouTube ID не извлечён — честный пробел) | DLR | 2026-10-31 | Средняя (релевантно теме телеоперации на лунном аналоге, но не найден прямой видео-URL) |
| Предсказательная компенсация задержки | инфографика | Физически-информированная LSTM-архитектура компенсации задержки (forward/backward predictor, delayed vs predicted signal) | https://arxiv.org/abs/2402.16587 (рис. 2) | arXiv (Physics-Informed LSTM-Based Delay Compensation Framework for Teleoperated UGVs) | 2026-10-31 | Хорошая, но с honest caveat: это наземная робототехника (UGV), НЕ лунный аналог и НЕ тот же метод, что в разборе §2.5 главы (LSTM/TCN для видео-предсказания сцены) — иллюстрирует общий принцип «предсказание вместо задержанного сигнала», не конкретный эксперимент. Скачана в `latency-compensation/08-INFOGRAPHIC-lstm-delay-compensation-architecture.png` |
| Astrobee | видео | «Deep Learning Warm Starts for Trajectory Optimization on the ISS» — официальное демо-видео Stanford ASL (проектная страница) с кадрами полёта Astrobee на МКС с warm-start планированием | https://youtu.be/NVDMd88XFhs (встроено на https://somritabanerjee.github.io/astrobee-learning/) | Stanford Autonomous Systems Lab, проектная страница | 2026-10-31 | Отличная — прямой первоисточник эксперимента, упомянутого в разборе §2.6 |
| Astrobee | видео | «Video: NASA's cute cube robot flies autonomously for first time on ISS» — журналистский разбор с видеовставкой демонстрации | https://interestingengineering.com/ai-robotics/nasa-robot-flies-autonomously-on-iss | Interesting Engineering, декабрь 2025 | 2026-10-31 | Хорошая (вторичный источник, но видео то же событие) |
| Astrobee | видео | «NASA's Astrobee Robot First Free Flight in Space» | https://www.youtube.com/watch?v=hk-1j3sXTqA | YouTube | 2026-10-31 | Средняя (общий ролик про Astrobee, не специфично про warm-start демонстрацию дек. 2025) |
| Astrobee | инфографика | Flowchart cold-start vs warm-start SCP (Sequential Convex Programming): offline training → online deployment | https://arxiv.org/abs/2505.05588 (рис. 2, HTML: `2505.05588v2/Broken_Down_Flowchart.png`) | arXiv (Banerjee et al., Deep Learning Warm Starts for Trajectory Optimization on the ISS) | 2026-10-31 | Отличная — скачана в `astrobee/10-INFOGRAPHIC-warm-start-flowchart.png`, прямо иллюстрирует механизм warm start из §2.3а главы |

## Честные пробелы (что НЕ найдено и почему)

1. **Dragon — точный скриншот сенсорного экрана во время реальной стыковки Demo-2 (не тренировки).** Найдены: (а) реальные фото тренировочного симулятора с теми же экранами (2015/2020, идентичный UI), (б) официальная инфографика ESA с полной последовательностью. Скриншот именно момента автономной стыковки на борту во время самой миссии 2020 года в открытых источниках не публиковался отдельным кадром экрана — NASA/SpaceX публикуют видео трансляции, не изолированные кадры дисплея. Честный пробел; две фотографии, которые есть (тренировка в Hawthorne и демо-макет интерьера), покрывают тот же UI, но не тот момент.
2. **Dragon — архитектурная схема системы управления (GNC).** Глава сама отмечает (§2.4, п.5 инженерной глубины), что архитектура не раскрыта SpaceX публично — соответственно, диаграммы/инфографики внутреннего устройства системы управления не существует в открытых источниках. Это не пробел поиска, а пробел первоисточника, уже названный в главе.
3. **Предсказательная компенсация задержки — скриншот ИМЕННО того интерфейса с LSTM/TCN-предсказанием кадра, упомянутого в §2.5 (эффект «до 26%»).** Конкретная публикация Frontiers in Space Technologies 2026 (номер DOI 10.3389/frspt.2026.1920649, LUNA Analog Facility, Lopez-Contreras et al.) при детальной проверке оказалась про нагрузку/психофизиологию оператора, а НЕ про LSTM/TCN-компенсацию видео — то есть это другая публикация из того же «нескольких независимых публикаций», на которые ссылается глава. Прямую публикацию с LSTM/TCN-предиктором видео именно для лунного аналога в открытом доступе с иллюстрациями найти не удалось за время поиска (близкие по методу публикации — общая робототехника/телехирургия, что сама глава тоже честно отмечает). **Взамен найдено и использовано:** (а) реальные фото полигона LUNA (DLR/ESA, Wikimedia Commons, CC BY-SA 4.0) — лунный аналоговый полигон как таковой; (б) официальный технический отчёт NASA (NTRS, LTV Teleoperation Studies, Litaker et al. 2024) с реальными фотографиями оператора за консолью с **предиктивным индикатором** («predictive circle function») на экране навигации — это классический (не ML) предиктивный приём для той же задачи (компенсация задержки при лунной телеоперации), не тот же метод, что в §2.5, но из того же физического контекста и достаточно близкий для иллюстрации идеи «что видит оператор». Помечено честной оговоркой в `.url`-сайдкарах.
4. **Предсказательная компенсация задержки — видео именно эксперимента с LSTM/TCN.** Не найдено (сама публикация, судя по доступным данным, —исследовательская статья без сопроводительного видео). Взамен — видео самого полигона LUNA (где проводятся испытания телеоперации в принципе) и общие материалы ESA/DLR.
5. **Astrobee — фото передачи роботу Arkisys (операция передачи, лето 2025).** Найдены новостные статьи о сделке (Aviation Week, USC, AzoRobotics), но ни одна не содержала фотографии самого момента передачи/церемонии — только текстовые пресс-релизы и логотипы компаний. Честный пробел; не стилизованный мок, просто отсутствие фотографии в открытых источниках на момент поиска.
6. **YouTube-канал для некоторых видео Dragon/Astrobee не подтверждён независимо** (WebFetch не рендерит JS-метаданные YouTube) — атрибуция канала в таблице выше основана на заголовке/сниппете поиска, а не на прямом просмотре страницы видео. Это методологический пробел инструмента, а не находки — честно отмечено в таблице.

## Что сделано (кратко)

- **Dragon**: 6 фото + 1 инфографика. Источники — Wikimedia Commons (NASA, public domain) + Wikimedia Commons (SpaceX, CC0) + ESA official infographic. 3 видео на YouTube.
- **Предсказательная компенсация задержки**: 7 фото + 1 инфографика. Источники — Wikimedia Commons (DLR/ESA LUNA Analog Facility, CC BY-SA 4.0, фото Raimond Spekking) + NASA Technical Reports Server (LTV Teleoperation Studies, госдокумент, public domain) + arXiv (LSTM delay-compensation architecture, с честной оговоркой о нерелевантности области). 3 видео-ссылки (1 — косвенная, без точного URL).
- **Astrobee**: 9 фото + 1 инфографика. Источники — Wikimedia Commons (NASA Johnson Space Center, public domain) + arXiv (Banerjee et al. 2025, Fig.1/2/3 — официальные фигуры из научной публикации о той самой демонстрации warm-start, упомянутой в §2.6 главы). 3 видео, включая прямой первоисточник (Stanford ASL project page).

Все изображения — реальные фотографии или фигуры из научных публикаций/официальных пресс-материалов. Stylized-mock заглушки не использовались ни разу; там, где точного совпадения с описанием из главы не нашлось, honest caveat зафиксирован явно (см. раздел «Честные пробелы» и соответствующие `.url`-сайдкары).
