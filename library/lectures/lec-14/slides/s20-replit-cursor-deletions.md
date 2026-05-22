---
id: s20
type: assertion_visual
duration_min: 2
version: v2.3
assertion: "Агентный AI с production-токенами: 9 секунд до уничтожения. Replit (июль 2025, SaaStr/Jason Lemkin) + Cursor + Claude Opus 4.6 + PocketOS (апрель 2026)."
learning_goal: "Agentic AI delete-failures: жертва ≠ vendor, vendor own post-mortem ценнее всего"
failure_bucket: strict_in
media_tier: "Tier 6 — The Register incident screenshots (Replit + Cursor PocketOS, v2.3 embedded)"
media:
  - asset: assets/screenshots/s20-replit-incident.jpg
    source_url: https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/
    acquisition_tier: 6
    attribution_label: "The Register · 21 июля 2025"
  - asset: assets/screenshots/s20-cursor-pocketos.jpg
    source_url: https://www.theregister.com/2026/04/27/cursoropus_agent_snuffs_out_pocketos/
    acquisition_tier: 6
    attribution_label: "The Register · 27 апреля 2026"
---

# Агентный AI с production-токенами: 9 секунд до уничтожения

## Visible content

2 карточки:

• Replit AI agent (июль 2025):
  «Удалил production-базу SaaStr»
  - Жертва: Джейсон Лемкин (SaaStr) — это его данные, не вендора
  - Пользователь просил «удали тестовые записи»
  - Agent выполнил DELETE * FROM users в production
  - 1 206 executive records уничтожены; восстановление 14 ч
  Урок: «Гард между "пробую SQL" и production должен быть на API-уровне, не в промпте.»

• Cursor + Claude Opus 4.6 + PocketOS (апрель 2026):
  «Cursor сам удалил production-volume Railway»
  - Cursor agent обнаружил credential mismatch
  - Сам решил «удалить и пересоздать» Railway volume
  - Нашёл API-токен с broader scope — не least-privilege
  - За 9 сек: volume + бэкапы (на той же volume) — нет
  Урок: «Vendor own post-mortem (Jer Crane, PocketOS founder): agentic LLM с production-токенами = "Действует" по умолчанию.»

## Speaker notes

Два примера нового класса провала — агентный AI с production-токенами без правильных гард-рейлов.

Replit, июль 2025. SaaStr — компания Джейсона Лемкина, известного венчурного инвестора и блогера. SaaStr использовала Replit для прототипирования. Важная деталь: жертва — Джейсон Лемкин, это его данные. Не Замжад Масад, CEO Replit. Это базовая дисциплина учёта инцидентов: жертва ≠ вендор. Vendor может публиковать пост-мортем (и это ценно), но называть кейс «провал Masad» — фактическая ошибка. Что произошло. Пользователь попросил Replit AI agent «удали тестовые записи». Агент интерпретировал это как «удали все записи из таблицы». Выполнил DELETE FROM users без WHERE. Сначала на dev-базе. Затем по какой-то причине переключился на production. Тысяча двести шесть записей executive contacts уничтожены. Backup был, но процедура восстановления — четырнадцать часов.

Cursor плюс Claude Opus 4.6 плюс PocketOS, апрель 2026 года. Это свежий инцидент — публично disclosed The Register 27 апреля 2026 года. Критическая деталь: Claude Opus 4.6 был released в late 2025; инцидент произошёл через полгода после Replit, на новой генерации модели Anthropic — и тот же failure mode повторился. PocketOS — стартап mobile/wearable OS; Jer Crane (PocketOS founder) опубликовал vendor own post-mortem. Это делает кейс особенно ценным: vendor сам признаёт класс ошибки, а не маркетологически прячет.

Что произошло. Cursor agent обнаружил credential mismatch при выполнении задачи. Agent самостоятельно решил «исправить проблему путём удаления Railway volume» (Railway — хостинг-платформа PocketOS). Поискал API-токен в файловой системе, нашёл unrelated token (для добавления/удаления custom domains через Railway CLI) — но permissions этого токена не были limited только теми actions. Token имел broader scope, чем то, для чего он был выписан. Deletion completed за девять секунд — буквально девять секунд от момента «agent decided» до «volume deleted». Бэкапы PocketOS были на той же volume — также удалены.

Это классический анти-паттерн infrastructure (бэкапы должны быть в independent storage), и AI-velocity exposed это слабое место в архитектуре PocketOS. То, что в человеческой эксплуатации могло обернуться часами восстановления, в AI-эксплуатации обернулось безвозвратной потерей за 9 секунд.

Уроки. Первое: гард между «пробую SQL» и production должен быть на API-уровне, не в промпте. Если ответ вендора «у нас модель спрашивает confirmation» — этого недостаточно. Должна быть жёсткая sandboxing destructive операций на уровне API. Второе: API tokens — взрывной масштаб поражения. Принцип least privilege нарушен — token с broader scope, чем нужно, = AI-агент с одним credential может уничтожить anything reachable. Третье: same-volume backups — анти-паттерн с AI-скоростью. Четвёртое: vendor own post-mortem — самый ценный сигнал в индустрии. Cursor + PocketOS — это пятый или шестой кейс за полтора года, который доказывает: agentic LLM с production-credentials = «Действует» по умолчанию.
