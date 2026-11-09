---
# ТЕРМИН ОБЪЯСНЁН НА ПЕРВОМ УПОТРЕБЛЕНИИ (п. 13 наряда; §5.20 + §11.7 — «проход по глоссарию
# термина делается ПО ВСЕМ кадрам раздела разом, а не кадр за кадром»).
# ЗАМЕР ПО ВСЕЙ ДЕКЕ, видимый слой с учётом плашек и столбцов: «площадь под кривой» стоит на
# s30 · s41 · s49b · s102, шкала была только на s49b и s49e — то есть на первых ДВУХ
# употреблениях показа термин стоял голым, а объяснялся на третьем. Шкала перенесена сюда,
# на первое; на s49b она остаётся, там величина головная.
# ВТОРОЙ ДЕФЕКТ ТОГО ЖЕ ПРОХОДА, который покадровая проверка не видит: одна и та же величина
# звалась на s49e «различением», на остальных четырёх — площадью под кривой. Имя сведено к
# одному по всей деке (§5.20, сквозная ревизия); правка s49e — в её собственном фронтматтере.
# ВОССТАНОВЛЕНО (#283, задача 2): кадр был снят структурным разрезом #229 (не по качеству —
# предел «≤140 слов» и попытка свести чувствительность/специфичность/площадь-под-кривой в один
# график, оба основания больше не действуют, см. CLAUDE.md § «Форма подачи слайда»). Возвращён
# в раздел целиком, `section` поправлен на актуальное имя (было дочернее название ДО слияния
# разделов 2+3), добавлена `scheme` (чек-лист инженерной глубины §2 obzor-stran-i-glubina-
# razbora.md), `media_needed` переписан честным отказом вместо указания искать CC BY-NC палитру.
id: s30
local_id: s2-07
section: "2. Инструментальная и лабораторная диагностика"
type: case
title: "Example 4: skin, and the composition of the dataset"
assertion: "Модели дерматологической диагностики теряют площадь под кривой на тёмных тонах кожи, недопредставленных в обучающем наборе, и знаменатель этого замера назван"
source: "Daneshjou et al., Science Advances 2022 — https://doi.org/10.1126/sciadv.abq6147 · Vestergaard et al., British Journal of Dermatology 2008 — https://doi.org/10.1111/j.1365-2133.2008.08713.x"
media: ""
media_needed: "6-tier поиск предпринят: палитра тонов кожи (шкала Фицпатрика) рядом со снимком поражения. Честный отказ: повторяемые источники такой палитры (Wikimedia/научные иллюстрации) лицензируют её CC BY-NC — некоммерческая оговорка не подходит под правило курса (материалы курса публикуются на открытом сайте, лицензия обязана разрешать это использование), поэтому палитра не подставлена. Снимок кожного поражения с идентифицируемым пациентом исключён отдельно (мед. приватность). Media не является мок-заглушкой — это документированный отказ, не пропуск"
media_note: "три модели сравнивались на одном и том же корпусе биопсийно подтверждённых изображений"
blocks:
  - {label: "The cost of both errors", value: "treatment at a late stage · biopsy and a scar"}
  - {label: "Out of 100 sick people found: naked eye → lit magnifier", value: "86 → 91", note: "out of 100 healthy people falsely alarmed, 23 → 26; one meta-analysis"}
  - {label: "How much worse the model distinguishes sick from healthy on dark skin", value: "by 9–15 out of 100", note: "scale: 50 is a coin flip, 100 is no misses. Three models, 656 confirmed-diagnosis images: 208 light · 241 medium · 207 dark", key: true}
scheme:
  arrows: true
  rows:
    - {label: "Without the model", steps: ["naked-eye exam / dermoscopy", "decision: see a physician or not"]}
    - {label: "With the model", steps: ["image taken by phone/camera", {text: "the model", ai: true}, "show to a physician or not"]}
pol_slov: 165   # #283 задача 2: переобъявлен по собранному PDF после восстановления кадра + добавления
  # `scheme` (вход/выход теперь несёт схема, строка «вход — снимок, выход — показать врачу или
  # нет» снята из тела как дублирующая её). 0 блокирующих, 0 предупреждений о поле/кегле.
# [ПРЕЖНЕЕ, #229] pol_slov: 162   # О13 (#229): вставлен классический режим — задача человека и работа врача до модели («находит на коже образование и хочет знать, идти ли с ним к врачу»; «смотрел врач глазом, обученный специалист — через дермоскоп»), пункт 1 «кто и что делал». Кадр открывался устройством модели, и человек, которого она заменяет, на экране не появлялся; плашка 86 → 91 называла режимы числом, но не работой. Плюс (#229, описание опыта): +18 слов, строка «Как сравнивали». Чем заняты: «Три модели прогнали по одному и тому же проверочному набору» — один набор на три модели, то есть разрыв мерен не разными выборками (11); слово «проверочному» стоит там, чтобы его не спутали с обучающими наборами, о которых следующая строка говорит «свои»; «и сравнивали светлые тона с тёмными» — что с чем сопоставляли (6). Счёт, состав и биопсия остаются на плашке («656 изображений с биопсией: 208 светлых · 241 средних · 207 тёмных»), единица — там же («пункты площади под кривой»), и в теле ни то, ни другое не повторяется. Источник — chapter-part1c.md:162 и :174 (Daneshjou и соавт., набор DDI). Основание пола — 143 по собранному PDF плюс 18 и слово запаса; ОЦЕНКА читает 161
timing_min: 0.85
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель против них", "④как это устроено"]
form: []
vfy: true
status: собран
---

## Visible slide text

**What was done before the model.** A person finds a lesion on their skin and wants to know whether to see a physician. A physician looked with the naked eye; a trained specialist, through a dermoscope.

**How it's built.** Three models on one validation set, light tones against dark. Each of the three has its own training set, and dark tones are scarce in them — that is the whole matter. *Image classification.*

*The classical regimes are from one head-to-head meta-analysis.*

## Speaker notes

A person finds a lesion on their skin and wants to know whether to see a physician. Before the model, this question was settled two ways: a physician looked with the naked eye; a trained specialist, through a dermoscope, a lit magnifier. Here the same question is answered by a model from an image, and three such models were tested on one set of six hundred fifty-six images with confirmed biopsies. On darker skin tones, all three distinguish sick from healthy nine to fifteen points worse than on lighter tones.

The cost of both errors is named by stage. A missed malignant skin lesion means treatment at a late stage rather than an early one; there is no single survival figure by group, computed on one cohort over one period, in the open summaries, so the cost is named by stage rather than by percentage. An unnecessary alarm means a biopsy, a scar, and months of waiting for the result.

Both classical regimes come from one study and one methodology: a head-to-head meta-analysis showed that a naked-eye exam finds eighty-six sick people out of a hundred at a specificity of seventy-seven, and dermoscopy by a trained specialist finds ninety-one at a specificity of seventy-four. A more recent review of the same task gives different numbers for the naked-eye exam, and gives no pooled estimate for dermoscopy at all, due to the heterogeneity of the studies; the two methodologies are not placed side by side, or the comparison would run between counting methods rather than between regimes.

The composition of the validation set is named item by item: two hundred eight light tones, two hundred forty-one medium, two hundred seven of the darkest. The denominator is respectable, and there is no basis here for talking about "a handful of examples."

Here is how it's built: input is an image of a skin lesion, output is a "show to a physician or not" score. The three models each have their own training set, and dark tones are scarce in them — that is the entire breakdown, and it is the only case in the lecture where the subject is the composition of the training data, rather than the algorithm, the deployment, or the choice of target. The publication gives no names for the models themselves; the validation sample is named — DDI — and the study can be found by it.

This breakdown does not take one commonly circulated figure, and the refusal is worth stating directly. The phrasing "sensitivity drops twenty to thirty percent on dark skin" was not found in the publication, and its source cannot be identified. The nearest actually measured figure looks different and belongs to one of the three models: sixty-nine sick people out of a hundred on light tones against twenty-three on dark. The section's rule is applied to a number that would have flattered this breakdown — and that is exactly why it is applied.

The unit of measurement is named precisely: these are points of area under the curve, a measure of distinguishing sick from healthy, not a share of sick people found. One cannot be substituted for the other — they are quantities of a different nature, and a gap in area-under-the-curve points does not translate into a percentage of misses. If anyone in the room converts it into a percentage, they will get a number nobody measured.

The strength of the evidence. This is a test on a curated, biopsy-confirmed corpus, not a field observation of deployment: the study says nothing about how these models behave in an actual clinical setting. The denominator is named, the composition is named, the unit is named — and that is where its value ends. The finding cannot be carried over to a specific product: there are three models, and none of them is named.

What to take from this case. The model works, and it works unevenly for different people, and the difference lies in whose images it was trained on. The task here is a familiar one — image classification; the subject of this breakdown became the training set, and this is the only place in the lecture that asks not about the algorithm and not about the deployment, but about the composition of the data.

**Sources.** [Daneshjou et al., Science Advances 2022](https://doi.org/10.1126/sciadv.abq6147) · [Vestergaard et al., British Journal of Dermatology 2008](https://doi.org/10.1111/j.1365-2133.2008.08713.x)
