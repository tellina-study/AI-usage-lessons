---
# ВТОРАЯ ПОЛОВИНА ШЕСТОГО РАЗБОРА (головной кадр — `s49g`). Здесь стоит цена: единственное в деке
# измерение того, что происходит в точке РАСХОЖДЕНИЯ врача и модели.
# НЮАНС НАДЁЖНОСТИ НА КАДРЕ, НЕ В ЗАМЕТКАХ (§2.3 канона `obzor-stran-i-glubina-razbora.md`).
# Их два, оба в видимом теле: эталон сам нестабилен (на 168 случаях из 3 500 трое опытных врачей
# не сошлись вовсе), и заголовочные проценты — счёт, при котором синонимичный код считается
# верным; строгим счётом врач 90,0, модель 86,1.
# ТЕСТ §12 (`trebovaniya-k-soderzhaniyu-forma-part2.md`): все четыре величины кадра считаны в
# ОДНОЙ единице — доля верных из ста на одном и том же наборе 3 500 случаев, — и у каждой строки
# свой знаменатель подписан числом случаев. Разных оснований счёта на кадре нет, поэтому
# требование «предъявить одно простое число» выполняется само: человек без медицинского
# образования читает «из ста случаев прав столько-то раз» и больше ничего знать не обязан.
# ШОВ С `s49` (кардиограмма, доверие и стаж) НАЗВАН В ЗАМЕТКАХ: опросы этой работы говорят, что
# модель особенно пригодилась молодым специалистам, — тот же разрыв по стажу, который кадр
# кардиограммы уже измерил. Разрыв назван, а не домыслен: опросы качественные, числа у них нет.
id: s49h
local_id: s3-18a
section: "3. Постановка диагноза"
type: case
title: "Example 6, the cost: where the physician and the model disagree"
assertion: "Вся цена шестого разбора лежит в пятой части случаев: там, где врач и модель согласны (2 635 из 3 500), верны оба почти всегда — 99 из ста, и решать там нечего; там, где расходятся (697 случаев, 19,9 процента), врач прав в 64 случаях из ста, а модель в 45 — то есть в точке, где подсказка только и могла бы что-то изменить, не надёжен ни один из двоих; на 965 случаях, где трое экспертов сошлись не полностью, проваливаются оба сразу — врач 78,2, модель 72; при этом сам эталон нестабилен (на 168 случаях из 3 500 трое опытных врачей не сошлись вовсе), а заголовочные проценты получены счётом, в котором синонимичный код МКБ зачтён верным — строгим счётом врач 90,0, модель 86,1"
source: "Umerenkov, Nesterov, Shaposhnikov et al., IJCAI-25, Table 5, p. 9882 — https://www.ijcai.org/proceedings/2025/1098.pdf"
media: ""
media_needed: "иллюстрация не нужна — предмет кадра есть полоса плашек с тремя подмножествами одного набора"
media_note: "второй кадр разбора"
blocks:
  - {label: "Agree — 2,635 cases", value: "99 correct out of a hundred", note: "the easy part of the set: nothing to decide"}
  - {label: "Disagree — 697 cases", value: "physician 64 → model 45 out of a hundred", note: "in one case out of five, neither is reliable: the physician gets it right less than two-thirds of the time, the model less than half", key: true}
  - {label: "Three experts didn't fully agree — 965 cases", value: "physician 78.2 → model 72", note: "both collapse together, by twenty points"}
pol_slov: 155   # ПО ЗАМЕРУ СБОРКИ (`build_lec07.py --only s19,s19a,s49g,s49h`), не по оценке. Предел кадра 140, и он здесь перебран — как перебран у КАЖДОГО разбора этой деки: рядом стоят 256 (`s41`), 252 (`s16`), 244 (`s15`), 214 (`s49b`), 206 (`s49f`), 190 (`s49e`). Новые кадры легче любого из них, и легче медианы семьи. Обязательный состав §5.13 (цена ошибки · оба классических режима · модель рядом · устройство · что переехало) плюс схема потока и нюанс надёжности на кадре (§2.3) в 140 слов не укладывается: пробовано, замерено. Физические пределы — `[высота]`, `[кегль]`, `[пол]` — все чистые, то есть текст в рамке держится и кегль не ужат.
scheme:
  caption: "The same physician resolves the disagreement — there's no third reader at this stage"
  arrows: true
  rows:
    - {label: "Agree — 2,635", steps: [{text: "model suggests a code", ai: true}, "physician agrees", "code goes into the record", "nothing to check"]}
    - {label: "Disagree — 697", steps: [{text: "model suggests a code", ai: true}, "physician disagrees", "physician assigns their own code", "no arbiter"]}
timing_min: 1.0
in_bucket: true
method_steps: ["③модель рядом", "⑤что переехало"]
vfy: true
status: собран
---

## Visible slide text

**Where they agree, both are right and there's nothing to decide. All the cost sits in the fifth of cases where they disagree.**

**The reference standard itself is unstable:** on 168 of 3,500 cases, three experienced physicians didn't agree on anything at all.

## Speaker notes

All the cost of this sixth case study sits in a fifth of the cases. Where the physician and the model agree — 2,635 of 3,500 cases — both are right almost always, ninety-nine out of a hundred, and there's nothing to decide there. Where they disagree — 697 cases, nineteen and nine tenths percent — the physician is right in sixty-four cases out of a hundred, and the model in forty-five. This is exactly the spot that case studies on AI suggestions almost always skip, and it's the only one where the suggestion makes any difference at all.

The set everything was counted on: three thousand five hundred de-identified cases, pulled from the same city system, but AFTER the training set was frozen — so training cases wouldn't leak into the validation ones. Each case was reviewed independently by three experienced physicians, each seeing the whole history; the reference standard was the diagnosis at least two of them agreed on.

And here's the first thing worth saying slowly, because it's about the measure itself, not about the model. All three agreed in sixty-seven and a half cases out of a hundred. Two of the three agreed in twenty-seven and a half. And in five cases out of a hundred — that's a hundred sixty-eight cases out of three thousand five hundred — three experienced physicians, looking at one person's full history, didn't agree AT ALL: three different diagnoses for one case. Remember this the next time you hear about the accuracy of a diagnostic model: the very line it's measured against is itself shaking. Where the reference standard is assembled by a two-out-of-three vote, "accuracy" means "agreement with the majority," not "correctness."

Now the key figure of the evening for this section, and I'll break it into three subsets of one set. First: cases where the physician and the model gave the same answer — two thousand six hundred thirty-five, or three-quarters of the set. There, both are right almost always: ninety-nine out of a hundred. There's nothing to decide there, no need for a suggestion, and these cases are exactly what drive the bulk of the attractive headline number. Second: cases where the physician and the model DISAGREED — six hundred ninety-seven, almost exactly a fifth. And here it is: the physician is right in sixty-four cases out of a hundred, the model in forty-five. Let me state the conclusion plainly, because it's worth stating: in that fifth of cases, the only place where the suggestion could possibly have changed anything, NEITHER of the two is reliable. The physician is right less than two-thirds of the time, the model less than half. "Listen to the physician" gives you a third wrong there; "listen to the model" gives you more than half wrong.

The third subset finishes the picture. Take the nine hundred sixty-five cases where the three experts didn't fully agree — the objectively hard ones. There, both collapse together: the physician from ninety-seven down to seventy-eight, the model from ninety-four down to seventy-two. They fall together, and by roughly the same amount. So the model isn't hard where it finds things hard on its own terms — it's hard exactly where the human finds things hard, and their errors are correlated. For a pair, that's the worst possible arrangement: insurance that fails at the same moment as the thing it's insuring isn't insurance at all.

And a nuance about the percentages themselves, which the slide carries. Eighty-seven and seven tenths and ninety-one and seven tenths were obtained by a scoring method where a synonymous classification code is counted as correct — meaning the same disease, recorded under a different code, counts as a hit. By strict scoring, code for code: the physician scores exactly ninety, the model eighty-six and one tenth. The difference is small, but the direction matters: the headline figure is always the more generous of the two, and which one was actually used is worth asking before you repeat it.

What shifted. Three things, and none of them is about accuracy. First: the suggestion arrives BEFORE the physician's decision and sits above it on the screen — not alongside it, not on request, but at the top. We named this mechanism earlier, at the opening, and it has a name: anchoring. The conclusion shifts toward the suggestion even when the suggestion is wrong, and the order of presentation is a controllable parameter that's set here to the riskiest possible position. Second: the physician gained a step that wasn't part of their work before — deciding whether to trust the suggested code; in a fifth of the cases, this step is actually carried out, and we've just seen how it turns out. Third, and this comes from the authors' own surveys: the tool proved most useful to younger specialists — they feel more confident with it. We've already met the experience gap on the EKG with the incorrect machine readout; here it shows up from the other side, and honesty requires saying that these surveys are qualitative — there's no figure attached to them.

**Sources.** [Umerenkov, Nesterov, Shaposhnikov et al., IJCAI-25, Table 5, p. 9882](https://www.ijcai.org/proceedings/2025/1098.pdf)
