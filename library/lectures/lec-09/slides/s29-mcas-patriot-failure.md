---
id: s29
type: assertion_visual
duration_min: 3
assertion: "Boeing 737 MAX MCAS — canonical anti-pattern safety-critical AI. Single-AoA + opacity + software-cures-hardware + FMEA не пройден. 346 погибших."
learning_goal: "MCAS — 4 урока для всего safety-critical AI; Patriot 2003 + 2024 callback"
learning_outcomes: [LO1b, LO3]
chapter_ref: "§3.3, §3.4 — MCAS + Patriot"
references: [pmc-2020-boeing, gao-737, trenchart-2018-patriot]
visual:
  pattern: matrix
  primary: "4 lesson cards + side timeline + Patriot mini-callback"
---

# Boeing 737 MAX MCAS — canonical anti-pattern + Patriot callback

## Assertion

Boeing 737 MAX MCAS — canonical anti-pattern safety-critical AI. Single-AoA + opacity + software-cures-hardware + FMEA не пройден. 346 погибших.

## Visual

Под assertion — 2 зоны.

**Слева (60%)** — 4 lesson cards в 2×2 сетке Ocean rounded box, каждая с warning маркером:

**1. ✗ Single-point-of-failure**
- Одна модель, один сенсор, одно решение
- Один AoA-сенсор → MCAS nose-down

**2. ✗ Opacity**
- Пилоты НЕ знали о существовании MCAS
- Если оператор не знает что система делает — override не работает

**3. ✗ Software cures hardware**
- MCAS компенсировал смещение от больших двигателей
- Правильный путь: пересмотр hardware ИЛИ второй AoA-сенсор

**4. ✗ FMEA / FTA не пройден**
- Single-point-of-failure должен быть пойман на анализе отказов
- Failure Mode and Effects Analysis + Fault Tree Analysis — обязательны

**Справа (40%)** — vertical timeline в Ocean rounded box:

- **29 окт 2018** · Lion Air 610 · **189 погибших**
- **10 мар 2019** · Ethiopian Airlines 302 · **157 погибших**
- → **346 погибших** (gold-warning большим)
- **20 месяцев** остановка эксплуатации в США
- FAA un-grounding Nov 2020
- EU Jan 2021; China Dec 2022 (full international until 2022)

Под timeline — **Patriot mini-callback** в Teal-tint боксе:
- Иконка `radar` 24px
- 14pt: «**Patriot 2003** — RAF Tornado GR4 + USN F/A-18C (2 экипажа KIA); IFF не ответил. **Украинский F-16 Patriot 2024**. Урок: automation bias — оператор перестаёт мониторить».

Source 12pt italic: «PMC 2020 · ThinkReliability 2019 · Trenchart 2018 · SOFREP 2003».

## Speaker notes

Первый и канонический провал Act — Boeing 737 MAX MCAS, Maneuvering Characteristics Augmentation System. Два крушения: Lion Air Flight 610, 29 октября 2018 года, погибли 189 человек; Ethiopian Airlines Flight 302, 10 марта 2019 года, погибли 157 человек. Суммарно 346 погибших. 20-месячная остановка эксплуатации в США; международная un-grounding продолжалась до 2022 года — EU January 2021, China December 2022.

Что произошло. Boeing 737 MAX получил двигатели большего размера, чем у предыдущих 737. Это сместило аэродинамический центр и сделало самолёт склонным к задиранию носа на крутых режимах. Решение Boeing — программное: MCAS, система, автоматически корректирующая trim вниз. MCAS активировался по показаниям одного AoA-сенсора — Angle of Attack, — без резервирования. Когда сенсор давал ложное показание, MCAS повторно командовал nose-down trim, и пилот не мог override команду — у него не было ни тренировок, ни понимания, что система делает. Документация была минимальна.

Строго говоря, MCAS — не AI: это classical control system с if-then логикой. Но pedagogically это canonical anti-pattern для всех safety-critical AI, потому что в нём сошлись все ключевые проблемы автоматизации.

Уроки. Все четыре обязательны для любого AI в safety-critical. Один: redundancy — никогда не делать safety-critical системы зависимыми от single sensor. Второй: transparency — operator должен знать, что система делает. Третий: single-point-of-failure analysis — обязателен в FMEA, Failure Mode and Effects Analysis, и FTA, Fault Tree Analysis, до сертификации. И четвёртый, самый дорогой: software cannot solve hardware shortfalls. MCAS добавили, чтобы скомпенсировать аэродинамический сдвиг от больших двигателей. Это инженерный анти-паттерн, перенесённый из «software cheaper than hardware» в безопасностно-критичную область.

Связь с AI. Этот разбор работает дальше во всей главе. F-35 ALIS, который мы разобрали в Sense, — нарушение redundancy и opacity. Patriot 2003, к которому переходим сейчас — нарушение FMEA с IFF-системой. Lavender — нарушение FMEA с false-positive consequence. MCAS — общий шаблон, к которому возвращаются все остальные провалы.

И коротко про Patriot. Friendly fire incidents в двух хронологических точках. Patriot 2003 в Iraqi Freedom — британский RAF Tornado GR4 (две жизни экипажа) и US Navy F/A-18C лейтенанта Натана Уайта — оба сбиты собственными Patriot batteries. Tornado был misclassified как иракская противорадарная ракета; IFF — Identification Friend or Foe — был interrogated, но не ответил. Операторы воспринимали automated mode как «лучше человека» по статистике и ослабили активный мониторинг. Это automation bias в чистом виде. Украинский F-16 в 2024 году — друг-Patriot battery. Обстоятельства полностью не раскрыты.

Когда automation «лучше человека» по статистике, операторы перестают активно мониторить. Mitigation — системный подход, не single ML upgrade.
