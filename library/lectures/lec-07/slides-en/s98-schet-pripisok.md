---
# НОВЫЙ КАДР, круг «Итоги» issue #285. Заводится не по вкусу — по двум строкам канона.
# §6 `stroenie-i-povestvovanie.md`: «сквозная линия получает число на закрытии… у линии должно
#   быть число-рефрен». Линия Лекции 7 — «копаешь, а это не модель» — шла через все пять
#   разделов и СЧЁТА не имела: ровно дефект Лекции 6, где линия «начинаешь копаться, а это
#   классическая математика» держалась весь вечер без числа («число запоминается, впечатление
#   нет»).
# §14 `storozha-i-priyomka.md`, первый антипаттерн: «несущее наблюдение объявлено на дивайдере,
#   кадр-носитель снят без замены». Дивайдер `s96a` обещал свод «счёт приписок» — в заметках
#   дословно «второй отвечает, чей это результат» — и кадра под ним в деке не было ни одного.
#   Плановый адрес у этого кадра был (`s8-02`, реестр номинаций `plans/block-08-sborka.md` §4);
#   кадр жил в снятом разделе сборки и замены не получил.
# ЧИСЛО СОБРАНО, А НЕ ПЕРЕПИСАНО. Глава (§11.4) говорит «двенадцать подтверждённых из
#   пятнадцати» — это счёт ГЛАВЫ, у которой восемь разделов. Девять строк её реестра из
#   пятнадцати адресованы в разделы, изъятые из деки. Счёт деки собран заново:
#   `REESTR-PRIPISOK-DEKI.md`, прогон `deck/sverka_pripisok.py` (знаменатель — по дивайдерам,
#   независимо от реестра; числитель — по реестру, зачёт ТОЛЬКО по видимому слою кадров).
# ДВА ЧИСЛА РАЗВЕДЕНЫ ПОДПИСЯМИ (§11.8): разборов с припиской тринадцать, номинаций
#   четырнадцать — разбор модели сепсиса несёт две. На кадр идёт то, у которого знаменатель
#   назван: тринадцать из двадцати одного. Четырнадцать на кадре не произносится вовсе.
# ФОРМА — ПОЛОСА ПЛАШЕК, и это сознательный слом ритма (§3 «форма, повторённая N раз, —
#   дефект»): раздел шёл подряд сводами-таблицами, и его собственные заметки признают, что
#   «зал переставал смотреть с третьего». Плашки утверждают СОСТАВ СЧЁТА и не утверждают ни
#   порядка, ни сравнения (`deckkit/README-formy.md`) — именно то, что нужно трём графам.
# ОСНОВАНИЕ У ВСЕХ ЧИСЕЛ КАДРА ОДНО — двадцать один разбор (§12): и тринадцать с припиской,
#   и семь российских считаны от него же, поэтому дробление не мешает чтению.
# ЗНАМЕНАТЕЛЬ ПЕРЕСНЯТ ПРИ СВЕДЕНИИ ТРЁХ ВЕТОК (2026-10-20). Стояло 19 — состав деки на 89
#   кадрах, против которого этот кадр и писался (REESTR-PRIPISOK-DEKI.md объявляет свою основу
#   строкой `tree:` сам). Ветка российских разборов добавила «Пример 4» в раздел 1 (маммограммы)
#   и «Пример 6» в раздел 3 (медкарта): знаменатель стал 21, отечественных разборов 7.
#   ЧИСЛИТЕЛЬ НЕ ТРОНУТ, и это решение, а не недосмотр: ни один из двух новых разборов приписки
#   по правилу реестра не несёт — s19 на кадре прямо говорит «выигрыша по исходам нет», то есть
#   переатрибутировать нечего, а у s49h предмет — нестабильность эталона, то есть пробел замера,
#   который реестр из числителя исключает поимённо. Тот же результат независимо печатает
#   sverka_pripisok.py: «РАЗБОРОВ С ПРИПИСКОЙ: 13 из 21 … расхождений нет».
id: s98
local_id: s8-02
section: "6. Итоги"
type: summary
title: "The count of misattributions: in thirteen of twenty-one cases, the win does not belong to the model"
assertion: "Сквозная линия лекции получает число: из двадцати одного подробного разбора в тринадцати заявленный выигрыш или заявленная вина принадлежат не обученной модели — в двух её в механизме нет вовсе, в семи результат принадлежит порогу, составу данных, цели, реализации или объёму, в четырёх число сменило предмет по дороге от первоисточника к пересказу; семь разборов из тех же двадцати одного — отечественная практика, и три сильные строки линии остались только в заметках"
source: "the tally is compiled from REESTR-PRIPISOK-DEKI.md"
media: ""
media_needed: "иллюстрация не нужна: кадр несёт счёт, и фотография рядом с тремя плашками отнимает скорость чтения"
media_note: "плашки читаются как состав одного счёта: сумма трёх равна тринадцати, и это видно без подсказки"
blocks:
  - {label: "No model in the mechanism at all", value: "2 of 21", note: "remove the model and the mechanism still runs: an \"if-then\" decision tree in triage; skill is drained by the handed-off volume of work", key: true}
  - {label: "The win does not belong to the model", value: "7 of 21", note: "belongs to the threshold, the training-set composition, the target set for training, the order of presentation, or the implementation"}
  - {label: "The number grew in the retelling", value: "4 of 21", note: "56.7% instead of zero · \"no effect\" collapsed into one number · a share of opinions instead of time · scale instead of measurement"}
pol_slov: 155   # ПЕРЕОБЪЯВЛЕН ПО СОБРАННОМУ sec-6.pdf, круг «Итоги» (#285): 151 слов замером + запас 4. Прежнее значение называло состав ДО правок этого круга. Канон: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11)
opyt_net: "счёт сквозной линии: своего замера кадр не ставит — каждое число описано на кадре своего разбора, адреса в REESTR-PRIPISOK-DEKI.md"
timing_min: 0.9
in_bucket: true
method_steps: ["свод"]
form: ["сквозная линия"]
vfy: false
status: собран
---

## Visible slide text

**Twenty-one breakdowns all evening. In thirteen, the win or the blame belongs not to the trained model.**

**Seven breakdowns out of twenty-one are domestic practice:** mammograms in screening, Moscow twice in diagnostics, the chart in diagnosis, the visit note and voice dictation in documentation, ArtInCol in qualification.

**Three strong lines of this through-line never made it to the screen:** their sections were cut from the lecture. The strongest — a peer-reviewed review that got six of its own seven primary sources wrong.

**The practice to take from this:** for a claimed effect, ask **what it's counted against**; for a retold one, **open the primary source**.

## Speaker notes

Twenty-one detailed breakdowns all evening, and in thirteen of them the claimed win or the claimed blame belongs not to the trained model. This is the one new number of the evening, and it's about us. Every other number in the lecture has already been presented, each with its own base; here what's added up is something no single case shows: how often, while examining a model's deployment, we got down to the mechanism and found that the win or the blame belonged to something else.

I'll state the denominator plainly, because it can be checked. Twenty-one is the detailed breakdowns, the ones each section's divider names by number: four in screening, five in instrumental diagnostics, six in diagnosis, three in documentation, three in qualification. A slide titled "Example X, cost" or "Example X, mechanics" is part of its own breakdown, not a separate case — otherwise the denominator would be double-counted. Thirteen is the breakdowns where the slide itself stated exactly what the result belongs to. You can check this by opening the slide: find the line about the mechanism and compare it against what I'm saying right now.

The first column is the simplest and the most unpleasant. The model isn't in the mechanism at all, yet the conversation is about it. First-line intake triage: an exam score of 81 against 72 for physicians, more than a billion dollars invested, a valuation north of four billion — and inside it, by the account of the person who was responsible there for regulatory matters, an "if-then" decision tree in a spreadsheet. There is one check here, and it always works: remove the trained model. If the mechanism keeps running, then it was running without it all along. The second case in this same column is subtler, and closer to the room: skill decay. We're used to thinking it's the model that drains skill — but in UK cytology, the volume of reading dropped 80 to 85 out of 100 after switching to a different lab test, and the number of centers fell to eight out of forty-five. It is the handed-off volume of work that drains skill. The model is just one way to hand it off, and far from the most powerful one.

The second column is the most populated, seven breakdowns out of twenty-one, and the model is present in it. But the result does not belong to the model. The savings in the Moscow triage of screening scans did not come from reading getting cheaper: one scan became more expensive for the human reader, and the savings came entirely from that same fifty-five scans out of a hundred that nobody reads at all. The accuracy gap on dark skin belongs to the composition of the training set. The unfairness of selection into the high-attention program belongs to the target variable set for training: the model was trained to predict cost, and the decision made was about illness. The sign of the effect of a cue to a radiologist belongs to the order it was presented in — the same quantity, a different order, the opposite sign. The effect of automatic visit recording belongs to the implementation, not the class of tool: of two tools in one trial, the second showed no change at all. And the sepsis model's class is a penalized logistic regression, not the deep network people assume it to be.

The third column is about those who retell, and for an engineer it is the most practical one. Here the primary source is often careful, and the error is born along the way. 56.7 percent of double-reading workload saved is a recalculation under a scenario the authors themselves called hypothetical, while in the actually deployed practice the model replaced not a single human read — that is, zero. 62.8 percent in the domestic voice-dictation case is the share of physicians who think so, not a measured time. "No effect" for pathologists is the result of a report collapsed into one number, when the group's gain is not significant and the effect runs fourfold in either direction. Scale of deployment, the largest in the world by claimed numbers, is presented as proof of quality, when there is no measurement of the consequences.

I'll say something separately about the seven domestic breakdowns, because this is the very practice part of the room may be working with by hand tomorrow. Moscow, twice: half a million screening scans with autonomous triage, and three and a half thousand head CT scans, where autonomy was specifically withheld. The visit note that a voice assistant fills out, and voice dictation of the radiology report. And the colonoscopy assistant, tested by lottery on more than a thousand patients in Moscow and Ufa. Two were added last: a model in the second-reader spot for mammogram screening, and a model suggesting a final diagnosis from the chart. They sit unevenly across sections, and I'll name that too: two sections have two domestic breakdowns each, three have one, and no section is left without a domestic breakdown.

And about the three lines that never made it to the screen. I name them not for thoroughness's sake, but because this is exactly the measure of how much of the through-line was lost when the lecture was cut down. The strongest — a peer-reviewed review on deskilling that got six of its own seven primary sources wrong: eight residents became thirty-two, 1,443 colonoscopies became "more than twenty-three thousand," an observational study was called randomized. The cost of this line lies in the grade of the source: this is a peer-reviewed review, and it is wrong about its own sources — meaning the error lives higher up than a blog post, at the exact spot a reader usually stops checking. The second — "study-reporting time dropped from twenty minutes to three seconds": three seconds for a physician to prepare a report is physically impossible; this is, in all likelihood, the model's own processing time, presented as the physician's time. The third — "the early-warning model lowered mortality," where the effect belongs to a new role in the process, a dedicated rapid-response nurse, not to the quality of the model.

The practice the room takes away is worth saying twice — here, and on the last slide. For any claimed effect, ask what it's counted against. For any retold one, open the primary source. These are two different checks, and the second one is cheaper than it looks: in three cases out of four in the third column, it was enough to open the source itself and check the sample.
