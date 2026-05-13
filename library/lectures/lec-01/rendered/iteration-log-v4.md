# Iteration log v4 — Phase 8.5 P2 polish

**Дата:** 2026-05-12
**Источник:** `qa-reports/2026-05-12-deck-v2/sanity-check-presentation.md` (APPROVE-WITH-MINOR-FIXES) — секция «New issues introduced в v2».
**Базис:** `build_lec01_full_v3.py` → `build_lec01_full_v4.py`.
**Target time:** ~15-20 минут точечного полиша. **Actual:** ~18 минут.

---

## Applied fixes (4/4 P2 + 1 бонус)

### P2-1 — Footer-tax cleanup (anti-pattern #14) ✅ applied

3 слайда содержали footers, видимые в зале и не релевантные аудитории — methodist comments или backup инструкции. Перенесены в speaker notes (как требует anti-pattern #14 footer-tax).

**s12** — удалена строка «Demo: live + видео-backup. Код: assets/code/three-ways/». Информация про backup и путь к коду демо перенесена в speaker notes (расширены до полного methodist context: 14.04.2026 дата теста, путь к коду, fallback на видео).

**s18** — gold callout сокращён: «Конвейер 10K/час → Q1 ДА · Q2 НЕТ · Q3 НЕТ · Q4 (если коробки нет) → МОДЕЛЬ.» (убрано «Полный разбор — методичка §3.8»). Ссылка на методичку оставлена в speaker notes — лектор даёт устно или в раздатке.

**s26** — удалена footer-строка «Точные группы и темы — в каталоге 00-course/...». NB для course-curator (с Google Drive ID `1sHXoLaIqCpBRv1IaLjS6lNtBdwI5cPc0`) оставлен в speaker notes — аудитории это нерелевантно.

**Slide markdown speaker notes обновлены** в `slides/s12-three-ways-demo.md`, `slides/s18-checklist-4-questions.md`, `slides/s26-course-roadmap.md` (добавлена секция *v4 P2-1* с пояснением, что и куда переехало).

### P2-2 — s29 provocation как visible assertion ✅ applied (Variant A)

Старая структура: «Q&A» 200pt gold по центру + «Открытый микрофон» subtitle + 2 Backup boxes (с провокациями).

Новая структура:
- **Top assertion (28pt Ocean DEEP, центр):** «Кто после этой лекции изменил мнение о чём-то?» — главная провокация теперь видна сразу при открытии слайда.
- **«Q&A» уменьшен с 200pt → 130pt** gold, по центру — wow-фактор сохранён, но не давит всё пространство.
- **Subtitle «Открытый микрофон.»** 18pt Ocean light italic (было 22pt DEEP).
- **Backup 1** прежний («…коллега не умеет ставить AI в систему»).
- **Backup 2 заменён** на свежий «Что из услышанного вы попробуете до семинара?» — оригинальный «Кто изменил мнение» promoted в главное assertion.

Speaker notes обновлены: указано, что главная провокация задаётся сразу после открытия Q&A.

### P2-3 — s17 real logos ✅ applied (8 of 9)

В сетке «Приложения с AI внутри» (3×3) text-only брендовые лейблы заменены на реальные PNG-лого:

| App | Logo file | Source |
|---|---|---|
| Google Translate | `logo-googletranslate.png` | simple-icons CDN |
| DeepL | `logo-deepl.png` | existing (LobeHub) |
| Grammarly | `logo-grammarly.png` | simple-icons CDN |
| Notion AI | `logo-notion.png` | simple-icons CDN |
| Copilot inline | `logo-copilot.png` | existing |
| Яндекс.Навигатор | `logo-yandex.png` | existing |
| Adobe Firefly | `logo-adobefirefly.png` | LobeHub `adobefirefly` |
| **Алиса** | — (text fallback) | no clean asset найден в LobeHub/simple-icons |
| Spotify | `logo-spotify.png` | simple-icons CDN |

5 новых лого (Google Translate, Grammarly, Notion, Adobe Firefly, Spotify) скачаны из simple-icons / LobeHub, recoloured `currentColor` / `#000` → `#1C7293` (Ocean light), конвертированы 96×96px PNG через `rsvg-convert`. Embedded в каждую ячейку (`logo_h = 0.5"`, центрировано над текстовым лейблом).

«Алиса» оставлен text-only fallback в той же ячейке — не блокер, единственный из 9, без чистого свободного asset'а.

### P2-4 — s27 callback box density ✅ applied

Старая структура: один gold callback box, содержащий 3 элемента подряд (camera mini + question label + question text + checklist note) — плотно, без явных gaps.

Новая структура:
- **Camera mini-photo** (s01 callback) — прежняя позиция, прежняя caption «s1 — узнала за 30мс / кадр».
- **Gold question box** (высота уменьшена с 1.45" → 1.05", только question + label) — компактный, выделенный.
- **Visible gap 0.18"** между gold box и checklist badge.
- **Separate checklist badge** (Ocean light stroke, SURFACE fill, более pill-shaped) — «Чек-лист s18 = операционализованный ответ» отдельным smaller badge.

Density visible улучшен: 3 элемента → camera + question (gold) + checklist badge (separate Ocean) с явной иерархией.

---

## Bonus — Backup 2 на s29

Поскольку P2-2 promoted оригинальный Backup 2 в главное assertion, его освободившееся место заполнено fresh provocation «Что из услышанного вы попробуете до семинара?» — переход к действию (action-oriented), не повторяющий «изменили мнение». Это улучшает структуру Q&A: главная провокация (промежуточный mindset) → action-trigger backup.

---

## Регрессии

Проверены 30 PNG (libreoffice + pdftoppm @100dpi).

- **s04 (charts)** — donut + bar charts in motif boxes, без overlap. Multi-select caveat в гридах. ОК ✅
- **s05a–s05b** — palette/motif consistent. ОК ✅
- **s11 (layered model)** — concentric nested boxes intact. ОК ✅
- **s18** — после удаления § 3.8 worked example смотрится чище. ОК ✅
- **s23 (ARC-AGI)** — bars + percents + prices без overlap. ОК ✅
- **s25 (Pearl pyramid)** — Ocean+gold palette сохранена. ОК ✅
- **s28 (takeaways)** — 3 cards + homework intact. ОК ✅

**Регрессий не найдено.** Все 30 слайдов рендерятся без ошибок.

---

## Готовность к Phase 9

✅ Deck готов к speech-writer Phase 9.

3 P2 footer-tax cleanups + s29 provocation + s17 real logos + s27 density — производственные улучшения, не структурные изменения. Палитра LOCKED. Visual motif consistent. Источники прозрачны. LO coverage не затронуто.

Файлы:
- `library/lectures/lec-01/rendered/build_lec01_full_v4.py` (новый build script v4).
- `library/lectures/lec-01/rendered/lec-01.pptx` (overwrite v2.1, 30 slides).
- `library/lectures/lec-01/rendered/lec-01.pdf` (1.92 MB).
- `library/lectures/lec-01/rendered/snapshots/s01.png` .. `s29.png` (30 re-rendered).
- 5 новых logo assets: `assets/icons/logo-{googletranslate,grammarly,notion,adobefirefly,spotify}.png`.
- 3 обновлённых speaker notes в `slides/s12,s18,s26`.
