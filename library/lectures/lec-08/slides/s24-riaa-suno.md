---
id: s24
type: assertion_visual
duration_min: 2
assertion: "RIAA против Suno/Udio (24.06.2024). UMG settled Udio 29.10.2025 (в переговорах с Suno). Warner settled Suno (litigating Udio). Sony — actively litigating обоих. Suno SJ июль 2026."
learning_goal: "Case 4: лицензирование под давлением исков music"
learning_outcomes: [LO4]
chapter_ref: "§3.5 — RIAA против Suno/Udio"
references: [riaa-suno-press, umg-udio-урегулирование]
visual:
  pattern: assertion_visual
  primary: "RIAA press release screenshot + урегулирование timeline (24.06.2024 → 29.10.2025 UMG → июль 2026 Suno SJ) + «Урок: лицензирование под давлением исков»"
  backup: assets/backup/s24-riaa.png
---

# RIAA против Suno/Udio — лицензирование под давлением исков (Case 4)

## Assertion

RIAA против Suno/Udio (24.06.2024). UMG settled Udio 29.10.2025 (в переговорах с Suno). Warner settled Suno (litigating Udio). Sony — actively litigating обоих. Suno SJ июль 2026.

## Visual

Сверху assertion 22pt. Слева — RIAA press release screenshot мокап в Ocean rounded box: «RIAA Sues AI Music Companies Suno, Udio for Mass Copyright Infringement». Справа — settlement matrix 3×2 (3 majors × 2 defendants): UMG × Udio (зелёный — settled, joint platform 2026); UMG × Suno (light — в переговорах); Warner × Suno (зелёный — settled, royalty + equity сент 2025); Warner × Udio (gold — litigating); Sony × Suno (gold — litigating, SJ июль 2026); Sony × Udio (gold — litigating). Внизу — gold «УРОК ДЛЯ ИНЖЕНЕРА»: «Лицензирование под давлением исков — фактический исход: 4 из 6 lawsuit-комбинаций уже settled или в переговорах. Это новый слой бизнес-модели, не "запрет всей AI-музыки"».

## Speaker notes

Четвёртый кейс по авторскому праву — RIAA против Suno и Udio. Иски поданы двадцать четвёртого июня 2024 года Recording Industry Association of America от имени трёх крупных лейблов (Big Three) — UMG, Warner и Sony. Theory — Suno и Udio обучили music generation моделей на каталогах крупных лейблов без лицензии. Хронология settlements распределяется неравномерно по матрице 3 major × 2 defendants. Двадцать девятого октября 2025 года UMG settled с Udio — образовали joint platform для 2026 года; UMG ↔ Suno в переговорах. В сентябре 2025 года Warner подписала licensing deal с Suno (royalty plus equity), но Warner ↔ Udio — litigation продолжается. Sony Music — actively litigating с обоими defendants, push toward summary judgment. Suno Summary Judgment hearing запланирован на июль 2026 года, точная дата подлежит verification ближе к лекции. Что эта последовательность означает практически. Это не «все AI music banned». Это лицензирование под давлением исков — модель, в которой initial lawsuit'ы переводятся в licensing deals. Из шести lawsuit-комбинаций (3 majors × 2 defendants) — четыре уже settled или в переговорах. Это паттерн, который мы видели в музыкальной индустрии не раз: Napster — banned, потом Spotify — licensed; YouTube — initially lawsuit с Viacom, потом Content ID plus licensing. Generative AI music следует тому же эволюционному пути. Урок для инженера: лицензирование под давлением исков — actual outcome: четыре из шести lawsuit-комбинаций settled или в переговорах. Это новый слой бизнес-модели, не «запрет всей AI-музыки». Если ты строишь music-related AI продукт, ожидай licensing requirement как часть business model. Это не делает продукт unbuildable — это делает его более дорогим и более legally compliant. Те, кто строит без licensing infrastructure, столкнутся с тем же тупиком, что и Suno на этапе initial RIAA lawsuit. Те, кто строит с licensing infrastructure с самого начала — следуют Adobe Firefly playbook'у, где лицензированный корпус — это core business asset, не nice-to-have. И самое важное — даже после всех settlements, проверка сходства результата остаётся обязательным независимо от licensing статуса training data: licensing на input не освобождает от ответственности за output, дословно воспроизводящий конкретный protected song.
