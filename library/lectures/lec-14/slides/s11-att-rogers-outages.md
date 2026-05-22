---
id: s11
type: assertion_visual
duration_min: 1
version: v2.3
assertion: "AT&T 22 февраля 2024 — это CrowdStrike-pattern до CrowdStrike. Один не проверенный конфиг — 125 миллионов устройств без связи."
learning_goal: "Telco outage failures + foreshadow к каскадным сбоям инфры"
failure_bucket: strict_in
media_tier: "Tier 2 — AT&T HQ Dallas + Rogers Building Toronto Wikimedia CC-BY-SA (v2.3 embedded)"
media:
  - asset: assets/screenshots/s11-att-hq.jpg
    source_url: https://commons.wikimedia.org/wiki/File:AT%26THQDallas.jpg
    acquisition_tier: 2
    attribution_label: "AT&T HQ Dallas · Wikimedia CC-BY-SA"
  - asset: assets/screenshots/s11-rogers-hq.jpg
    source_url: https://commons.wikimedia.org/wiki/File:Rogers_Building_Toronto_Canada_2007.jpg
    acquisition_tier: 2
    attribution_label: "Rogers Building Toronto · Wikimedia CC-BY-SA"
---

# AT&T 22.02.2024 — это CrowdStrike-паттерн ДО CrowdStrike

## Visible content

2 карточки рядом:

• AT&T US (22.02.2024, 12 часов простоя):
  - Изменение в network management — не проверенное
  - ~125 миллионов устройств без связи
  - Расследование FCC: «нарушение процедур управления изменениями»
  - Все экстренные вызовы (E911) частично недоступны
  Урок: «Конфиг ≠ код. Но автоматический деплой обращается с ним как с кодом.»

• Rogers Canada (08.07.2022, 15+ часов простоя):
  - Ошибка в распространении IPv6-маршрутов
  - ~10 миллионов абонентов без связи
  - Платёжная система Interac упала
  - CRTC: «отсутствие network resilience»
  Урок: «Точка отказа в конфиге — каскад через всю инфру.»

Внизу — teal-tint foreshadow box:
«ПЕРЕХОД к разделу AIOps — каскадные сбои инфры. AT&T и Rogers — это "CrowdStrike до CrowdStrike". Дальше — полная картина: четыре каскада 2024–2025 на верхнем уровне лестницы.»

## Speaker notes

AT&T двадцать второго февраля 2024 года — это карта CrowdStrike в миниатюре, за пять месяцев до собственно CrowdStrike. Что произошло. Команда сетевой инженерии в AT&T делает изменение в network management конфигурации. Стандартная процедура, изменение прошло внутренний review. Деплой автоматический. Конфиг распространяется по сети. И вызывает каскадное отключение услуг.

Двенадцать часов простоя. Сто двадцать пять миллионов устройств без связи в Штатах. Самое серьёзное — частичная недоступность экстренной службы E911. FCC начинает расследование, формулировка вывода: «нарушение процедур управления изменениями». Конкретнее — отсутствие поэтапной раскатки, отсутствие канареечного деплоя, отсутствие независимого тестирования на реальной нагрузке.

Это шаблон ровно тот же, что у CrowdStrike. Конфиг, не код. Автоматический одновременный деплой. Без канарейки. Без отката. Это и есть «CrowdStrike-pattern до CrowdStrike».

Rogers Canada восьмого июля 2022 — ещё ранее, но та же физика. Ошибка в распространении IPv6-маршрутов. Около десяти миллионов абонентов без связи на пятнадцать часов. Параллельно упала платёжная система Interac — потому что банки маршрутизировали платежи через Rogers. Урок от регулятора CRTC: «отсутствие network resilience», точка отказа.

Зачем я показываю эти два кейса именно сейчас, перед разделом про AIOps. Чтобы вы поняли: то, что в разделе AIOps мы увидим четыре крупных каскада 2024–2025 — CrowdStrike, Cloudflare, AWS, Azure — это не AI-специфическая проблема. Это проблема архитектуры автоматического деплоя в инфраструктуре, которая существует и в pre-AI индустрии. AI только усиливает паттерн.
