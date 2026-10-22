---
id: s23
type: assertion_visual
duration_min: 2
assertion: "Andersen против Stability/Midjourney/DeviantArt — коллективный иск artists. motion to dismiss отклонён → истребование доказательств; trial 8 сент 2026. Подражание стилю."
learning_goal: "Case 3: подражание стилю коллективный иск"
learning_outcomes: [LO4]
chapter_ref: "§3.4 — Andersen против Stability"
references: [andersen-docket, judge-orrick-2024]
visual:
  pattern: assertion_visual
  primary: "Court docket screenshot + timeline (Jan 2023 → Aug 2024 motion to dismiss отклонён → 8 sep 2026 trial) + «Урок про подражание стилю»"
  backup: assets/backup/s23-andersen-docket.png
---

# Andersen против Stability — подражание стилю коллективный иск (Case 3)

## Assertion

Andersen против Stability/Midjourney/DeviantArt — коллективный иск artists. motion to dismiss отклонён → истребование доказательств; trial 8 сент 2026. Подражание стилю.

## Visual

Сверху assertion 24pt. Слева — Court docket screenshot мокап в Ocean rounded box (US District Court, Northern District of California). Справа — vertical timeline: Январь 2023 (filing — Andersen, McKernan, Ortiz, Andersen + 7 other artists) → Август 2024 (motion to dismiss отклонён by Judge Orrick → истребование доказательств) → 27 февраля 2026 (третий amended complaint) → 8 сентября 2026 (trial). Под timeline — chip «Подражание стилю "in the style of [artist]" theory». Внизу — gold «УРОК ДЛЯ ИНЖЕНЕРА»: «Подражание стилю "in the style of [конкретный художник]" — не безопасно только потому что стиль не охраняется авторским правом. Коллективные иски проходят motion to dismiss на DMCA + публичные права».

## Speaker notes

Третий кейс по авторскому праву — Andersen плюс McKernan плюс Ortiz плюс ещё семь художников против Stability AI, Midjourney и DeviantArt. Это коллективный иск, поданный в январе 2023 года через US District Court, Northern District of California. Главный аргумент — инструменты генеративного AI позволяют пользователям генерировать изображения «в стиле [конкретный художник]», что художники считают нарушением их публичных прав plus авторское право плюс DMCA. Это иск категории три по таксономии предыдущего слайда — подражание стилю. Хронология. В августе 2024 года Judge Orrick отказал в Motion to Dismiss большинства claims. Это означает, что коллективный иск survived initial procedural challenge и переходит в истребование доказательств. Это критически важно — истребование доказательств в коллективном иске в США для AI-компаний означает doсументированные внутренние коммуникации, списки обучающих данных, model checkpoints, всё, что юристы истцов могут истребовать через судебный запрос (subpoena). Третье изменённое заявление (amended complaint) подан двадцать седьмого февраля 2026 года; судебный процесс запланирован на восьмое сентября 2026, то есть через четыре месяца после нашей лекции. Что эта дело уже изменило. Многие смежные AI-компании по изображениям — например, Adobe Firefly — позиционируют себя как коммерчески безопасный именно потому, что Adobe обучает Firefly на Adobe Stock плюс лицензированный контент, не на данных, спарсенных из веба. Это позиционирование напрямую является ответом на риск класса Andersen. Урок для инженера: подражание стилю «в стиле конкретный художник» — не безопасно только потому что стиль формально не охраняется авторским правом. Коллективные иски проходят motion to dismiss по DMCA плюс публичным правам. Если твой продукт позволяет генерировать «в стиле [конкретного живого художника]» — у тебя есть риск класса Andersen, и его нужно учитывать в продуктовый дорожная карта не как теоретический сценарий, а как реалистичный исход. Практическое решение — не разрешать users в промптах называть имена живых художников; маска на этапе фильтрации ввода.
