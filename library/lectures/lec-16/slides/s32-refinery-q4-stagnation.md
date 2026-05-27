---
id: s32
type: failure_case
duration_min: 2
assertion: "Refinery plant-wide stagnation в Q4 frame: multi-physics (mass + energy + reaction + corrosion) ломает ML-суррогаты на edge cases. Yokogawa Idemitsu single-column success → plant-wide пилот тихо закрыт."
learning_goal: "Failure 2 Q4 + multi-physics surrogate gap"
failure_bucket: strict_in
chapter_ref:
  parts: [chapter-part3.md]
  sections: ["§4.5 Провал 2: refinery plant-wide stagnation в Q4 frame"]
visual:
  type: image
  description: "НПЗ aerial photo (Idemitsu Japan OR similar refinery) — illustration multi-unit complexity"
  source_url: "https://www.idemitsu.com/en/business/"
  acquisition_tier: 3
visible_numbers: ["40-50 лет field life refinery", "1-2 года ML model decay", "Yokogawa Idemitsu plant-wide пилот 2018+ закрыт [VFY]"]
russification_check: "Yokogawa, Idemitsu, Japan, OpreX, Aspen Mtell, Honeywell — brand list; «multi-physics constraint», «многоюнитная координация», «нефтепереработка», «колонна ректификации» — RU."
speaker_notes_target_words: 230
---

# Refinery plant-wide stagnation в Q4 frame: multi-physics ломает ML.

## Visible content

Заголовок: «Refinery plant-wide stagnation = Q4 структурная проблема» (28pt deep ocean).
Sub: «Cross-link к s07b: тот же failure pattern, новый frame — long horizons + multi-physics + edge cases.» (16pt italic)

**Слева — Ocean rounded box «Что НПЗ shares с Q4»:**

- **Multi-physics constraints:** mass + energy + reaction kinetics + corrosion. То же, что в CCS.
- **Long horizons:** НПЗ 40-50 лет; ML model decay **1-2 года** (gold accent — gap).
- **Edge cases:** изменение feedstock, equipment wear, regulatory changes → ML surrogates **lose consistency**.

**Справа — Ocean rounded box «Конкретный кейс»:**

- **Yokogawa OpreX + Idemitsu Japan (2018)** — пилот plant-wide AI process control на одном НПЗ.
- Single distillation column success — документировано.
- **Plant-wide пилот тихо закрыт после 2018** [VFY-day-of].
- Public materials остались только single-unit success stories.

**Применимость к Q4:**

- CCS injection plant = **многоюнитная инсталляция**: capture + transport + injection wells + monitoring.
- Координация на 30-50 летнем horizon = multi-physics coupling.
- AI делает узкую оптимизацию (один well rate). **Не делает координированное plant-wide управление с multi-decade outlook.**

**Bottom bar (gold tint) — Фундаментальный урок:**

«**Когда задача = multi-physics coupling + long horizons + edge cases → AI struggles фундаментально.** Не «больше данных решит», а **ограничение ML-методологии**: NN хорошо в интерполяции, плохо в экстраполяции, очень плохо в multi-physics экстраполяции.»

## Speaker notes

Этот провал мы видели в седьмом-би слайде в Q1 frame — Aspen Mtell усталость от ложных тревог plus общезаводская стагнация. Здесь мы переформулируем его в Q4 frame, как многослойная физика constraint, который AI не закрывает на длинных временных горизонтах.

Что refinery process control share с Q4. Первое — многослойная физика constraints: mass plus energy plus reaction kinetics plus corrosion. То же, что в CCS. Второе — длинные горизонты: НПЗ работает сорок-пятьдесят лет; ML model decay один-два года. Тот же gap, что в CCS миграция шлейфа. Третье — нестандартные режимы: при изменении feedstock, equipment wear, regulatory changes — ML surrogates lose consistency.

Cross-link к Yokogawa Idemitsu. Yokogawa в 2018 году объявила пилот общезаводской AI process control на одном из НПЗ Idemitsu в Японии. Пилот общезаводской тихо закрыт после 2018 года; в публичных материалах остались только single-column success stories. Это типичный паттерн: AI хорошо берёт локальную оптимизацию — один column, один heater. Плохо берёт многоюнитную координацию, где многослойная физика constraints ломают ML-суррогаты на нестандартные режимы.

Применимость к Q4. закачка CCS plant — это многоюнитная инсталляция: кап.ture unit плюс transport pipeline плюс закачка wells плюс мониторинг wells. Координация этих компонентов на тридцать-пятидесятилетнем горизонте требует многослойное сопряжение физики. AI может делать узкую оптимизацию — один закачка well rate, один кап.ture absorber. AI не может делать координированное общезаводской управление с multi-decade outlook. То же касается Fervo EGS.

Фундаментальный урок. Когда задача требует многослойное сопряжение физики плюс длинные горизонты плюс краевых случаев — развёртывание AI затрудняется фундаментально, не из-за нехватки обучающих данных. Это не «больше данных решит проблему»; это ограничение самой ML-методологии. Обобщение нейронных сетей хорошо работает в режиме интерполяции, плохо — в режиме экстраполяции, очень плохо — в режиме многослойная физика экстраполяции.
