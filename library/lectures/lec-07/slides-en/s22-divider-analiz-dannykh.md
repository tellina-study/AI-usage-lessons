---
# РАЗДЕЛ РАЗРЕЗАН (переделка по канону PR #286, `storozha-i-priyomka.md` §14, первая строка
# таблицы сторожей: раздел деки = одна стадия главы, смесь префиксов — блокирующее).
# Было: один раздел «2. Исследование и постановка диагноза» на 21 кадр, несущих префиксы ТРЁХ
# стадий плана — `s2-*` (8), `s3-*` (11), `s4-*` (2), — при том что глава держит эти стадии
# отдельными разделами со своими дивайдерами и выводами, а карта вечера `s01a` называет их
# отдельными стадиями цикла. Стало: «2. Инструментальная и лабораторная диагностика» (`s2-*`,
# этот дивайдер) и «3. Постановка диагноза» (`s3-*`, дивайдер `s35` возвращён из `_snyato`).
# Третьим разделом стадия наблюдения НЕ заводится — владелец снял её по имени 2026-10-15,
# решение письменно не отменено; разбор сепсиса стоит последним в разделе диагноза с
# переписанным под него префиксом (см. фронтматтер `s49e`).
# ПЕРЕЧЕНЬ РАЗБОРОВ ПЕРЕСОБРАН под §5.16 дословно по заголовкам кадров этого раздела.
# КРУГ 6 (2026-10-19): их стало пять — заказ владельца «не меньше 2х российских» закрыт
# двумя отечественными, и встали они ПЕРВЫМИ, сразу за обзором по странам, потому что
# московская доля 54,8 процента на обзоре взята из первого же из них. Порядок:
# s27a «Пример 1: Москва — профилактические снимки, которые не читает человек» (+ s27b,
# его цена) · s27c «Пример 2: Москва — кровоизлияние в череп, где автономию не дали» ·
# s28 «Пример 3: Таиланд — чтение глазного дна в кабинете первичного звена» · s30
# «Пример 4: кожа и состав набора» (+ s30a, его цена) · s31 «Пример 5: отбор в программу
# повышенного внимания — балл вместо решения врача». Нумерация «Пример N» — счёт ВНУТРИ
# раздела; в разделе диагноза она своя, 1–5.
# ОБЕЩАНИЕ ДИВАЙДЕРА ТЕПЕРЬ ИСПОЛНЕНО НА КАДРЕ: несущая выкладка §2.2 («одна система, две
# группы — 8 из ста против 79 из ста») стоит на `s24`, возвращённом из `_snyato` с экспозицией
# и мостом, которых владелец у него не нашёл (п. 23 его разбора). До этого круга дивайдер
# обещал «у каждой доли есть группа, на которой она посчитана», а ни один из 21 кадра показа
# этого не показывал — ни числом, ни словом «десятикратно».
id: s22
local_id: s2-01
section: "2. Инструментальная и лабораторная диагностика"
type: divider
title: "2. Instrumental and Laboratory Diagnostics"
assertion: "Одна и та же система на двух группах даёт долю верных тревог 8 из ста и 79 из ста — разницу назначает не прибор, а тот, кто решил, кого обследовать"
source: "—"
media: "rework/deck/assets/s22-rentgenkabinet-pacient-u-pribora.jpg"
media_needed: "Поиск: настоящая фотография рабочего места, где снимают диагностические данные — пост медсестры с монитором пульсоксиметрии, кабинет техника флюорографии за пультом или скрининговый кабинет с рентгеновским/ретинальным аппаратом. Нужен реальный, идентифицируемый снимок (пресс-фото клиники, фотобанк с указанием места съёмки), не постановочная иллюстрация с актёрами."
media_note: "ПРОВЕРЕНО ГЛАЗАМИ (#229, класс О12): снимок заказу СООТВЕТСТВУЕТ. Настоящий рентгенкабинет: пациент лежит на столе под потолочной трубкой, гибкие рукава подвеса, защитные фартуки на стене, указатели на китайском. Не постановка с актёрами — заказ этого и требовал. Заметка кадра («настоящее рабочее место, где снимают данные») утверждение подтверждает"
timing_min: 0.5
in_bucket: false
method_steps: ["дивайдер"]
form: []
vfy: false
status: собран
---

## Visible slide text

# 2. Instrumental and Laboratory Diagnostics

**In screening, the decision was who to examine. Here the person is measured by a device, and their condition is turned into a value that will be read somewhere else, at another time.**


In order:

**Example 1: Moscow — preventive scans that no human reads**

**Example 2: Moscow — intracranial hemorrhage, where autonomy was withheld**

**Example 3: Thailand — fundus reading in a primary-care office**

**Example 4: skin, and the composition of the dataset**

**Example 5: selection into a high-attention program — a score instead of a physician's decision**

## Speaker notes

Instrumental and laboratory diagnostics is the second stage in the order of work. In the first section, the decision was whom to call in for examination at all; here the person is already in view, and data is taken on them — an image is made, a sample is taken, a device is connected, a load protocol is applied, and the measured value is watched for change. The industry itself names this stage exactly this way: instrumental and laboratory diagnostics. The term splits into two halves by where the measurement comes from. Instrumental is what a device took directly off the person. Laboratory is what was measured in a sample taken from the person and carried off to a lab. Both halves do the same job: turn the person's state into a value that can be recorded, transmitted, and read somewhere else, at another time.

The boundary with the third section is worth drawing right away, because without it the two sections blur together. Here the stage produces values. A conclusion about disease from these values will be reached in the next section, and by a different person. So everything on these slides is about whether the measurement is fit for use and what it means, not about what diagnosis follows from it.

Now a point that is hard to hold onto when reading marketing materials, and it is why this section exists in the lecture at all. Any share — sensitivity, specificity, accuracy — is computed on a specific group of people, and when carried over to a different group it stops meaning the same thing. The numbers on the slide show exactly this: one system with one trigger threshold gives eight correct alarms out of a hundred in a general population stream and seventy-nine out of a hundred in a specialized department. Not one line changes inside the system — only the share of sick people in the group changes, and that share was set by whoever decided who to call in for examination. The full count, in people, comes two slides from now.

Hence the order of the section: first what AI intervenes in, then the intervention. First, what the stage's work is made of — what actions happen in it, who sets the threshold, who decides whether a measurement is usable. Then, on its own slide, the classical regime done entirely without a model: image quality control. Then a country-by-country overview — what volume of images and analyses within an ordinary referral stream passes through a trained model. And only after that, five breakdowns, the first two of them domestic.

They are worth naming right here, so the slide gets recognized later by a name already heard. Each of the five will come up on screen under exactly this heading.

Moscow, preventive scans — the only breakdown in the lecture where autonomous use of the model did not fail, and where its cost was counted as a number. Sensitivity was set to one, specificity was declared not significant, and a human stopped reading more than half the preventive stream: 315,491 of 575,549 scans. The cost: 290 clinically significant misses, and the fact that in ordinary work nobody would have found them.

Moscow, intracranial hemorrhage — the same city, the same circle of registered products, the opposite answer. On 3,409 head CT scans, the model alone raised 293 false alarms against four from the physician. This is the only breakdown in the section where the reading itself failed, rather than the setting, the dataset, or the target.

The remaining three take their place where it is possible to fail without the reading itself being wrong.

Thailand — a deployment failure. Autonomous reading of fundus images in eleven clinics rejects twenty-one images out of a hundred for quality, and both causes are about the room where the image was taken, not about the model: the room's lighting and a slow connection.

Skin, and the composition of the dataset — a failure of training-data composition. Three models lose nine to fifteen points of area under the curve on darker skin tones, which were underrepresented in the training sets. This is the only breakdown in the lecture where the subject is the training set itself, not the algorithm, the deployment, or the target. And the only one where the fix is measured: fine-tuning on a representative set closes the gap, while three algorithmic bias-correction methods did not close it.

Selection into a high-attention program — a failure of target definition. Future treatment spending was taken as the target variable, while the decision being made was about illness, and spending reflects utilization, which differs across groups with the same underlying health.

Two mentions come with a number and do not become breakdowns: a systematic review of imaging studies in COVID-19 pneumonia — sixty-two selected out of two thousand two hundred twelve, and not one fit for clinical use — and the bias in a blood-oxygen-saturation device, in which there is no trained model at all.

What this section does not have, and why. No comparison of models against one another: this is not a market survey. No laboratory accuracy figures detached from their group — by the same rule the section follows throughout. And not a single case where the reading itself failed: there was none among those broken down, and the section's conclusion says so directly.

The image alongside is a real workstation where data is taken. The conversation about shares starts here: first, someone puts the person in front of the device.

About the woman with the letter — her thread runs through the whole lecture, and in this section it lands in the most uncomfortable spot. She came in with no complaints, by age alone — that is, right in the general-population stream, where there is roughly one sick person per hundred. So every share anyone quotes her is computed on a group that is not hers, and the share of correct alarms for her own group is the worst one possible. The slide that counts the two groups leads exactly here, and her name is spoken directly there.
