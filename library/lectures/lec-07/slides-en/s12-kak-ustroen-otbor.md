---
id: s12
local_id: s1-02
section: "1. Первичный скрининг и отбор на обследование"
type: norm
title: "Seven actions of the screening stage — and three where the model switches on"
assertion: "Первичный скрининг состоит из семи действий — назначить порог, позвать по списку, снять исследование, прочесть двумя независимыми читателями, разрешить расхождение арбитражем, сообщить исход, отсортировать пришедших без приглашения; без модели каждое из семи делает человек по записанному правилу, а модель включается на трёх из них, и каждый из трёх назван своим разбором: чтение — шведская программа, исход — съёмка глазного дна, сортировка потока — чат-бот первой линии, стоящий при этом на другом входе стадии"
source: "NHS England breast screening program, GOV.UK, accessed 13 October 2026 — https://www.gov.uk/guidance/breast-screening-programme-overview"
opyt_net: "карта стадии: семь действий скрининга и три, которые заняла модель. Источник кадра — страница программы скрининга, то есть документ, а не замер. Цена обеих ошибок с базами — на s13, измеренные опыты раздела — s15, s16, s18"
media: "rework/deck/assets/s12-stranitsa-programmy-kogo-zovut.png"
media_needed: "настоящий снимок приглашения на скрининг или страницы программы с правилами приглашения — документ, по которому видно, что человека позвали, а не он пришёл; запасной сюжет — лаборант за маммографом, настоящий клинический снимок"
media_note: "вкручен снимок страницы АНГЛИЙСКОЙ программы. РАСХОЖДЕНИЕ БЫЛО И СНЯТО (#229, сессия содержания): в видимом тексте стояло «шведская программа скрининга молочной железы берёт список жителей» — прямо под снимком английской страницы, при том что эта самая строка поля объявляла, что страны в тексте нет. Слово снято, тело говорит «программа берёт список жителей»; шведские числа живут на s13, и там же названы своей программой. Подвал называет показанную программу прямо. На s13, где в видимом тексте стоит шведская программа, этот снимок ставить НЕЛЬЗЯ. Права: OGL v3.0, deck/images.md §3.2"
pol_slov: 118   # О10 (#229): картина работы стадии (CLAUDE.md § «Строение раздела») и семь действий схемой. #229 п.13 (владелец: «тут как будто универсальный процесс; подсветить, на каком этапе включается модель; примеры привязать к шагам»): третий ряд схемы перестал быть безымянным — каждый из трёх шагов, на которых модель включается, подписан своим разбором (чтение — шведская программа, исход — глазное дно, сортировка потока — чат-бот первой линии). Привязка стоит В СХЕМЕ, а не в теле, и это замер, а не вкус: те же три привязки телом (+45 слов) дали блокирующую [высота] и кегль 8,5 пт — кадр несёт снимок документа, и тело у него узкое. По той же причине с кадра снята строка «за нет не следует ничего» — она ушла в заметки, где и названа как обязательная к произнесению. Страна из тела убрана («программа берёт список жителей»): на кадре стоит снимок страницы АНГЛИЙСКОЙ программы, а шведские числа живут на s13 — расхождение снимка и текста, которое media_note объявлял отсутствующим ЗАМЕР ПО СОБРАННОМУ PDF полосы Входа и раздела 1 (render_sec.py 0 1, 2026-10-15, 14 страниц): 118 слов на этом кадре; медиана полосы 142,5, максимум 263, блокирующих 0. Поле выставлено ПО ЗАМЕРУ, не по оценке: прежнее число в этой строке называло состав до правки по замечаниям владельца и после неё было бы разрешением на чужой вес.
timing_min: 0.6
in_bucket: false
method_steps: ["заземление"]
form: ["вопрос залу"]
vizforma: "ряды"
vfy: false
status: собран
scheme:
  caption: "Seven actions of the stage — and three steps where the model switches on"
  arrows: true
  rows:
    - {label: "Without a model", steps: ["Set the threshold", "Call in by list", "Take the scan", "Read it by two"]}
    - {label: "…and further", steps: ["Arbitration", "Report the outcome", "Sort the flow"]}
    - {label: "Where the model switches on", steps: ["Read it by two\nthe Swedish program", "Report the outcome\nretinal fundus at the visit", "Sort the flow\nfirst-line chatbot"], arrows: false}
---

## Visible slide text




The letter the lecture opened with came out of exactly this: the program takes the list of residents, selects by age and sex, and sends out invitations. The person didn't come in on their own — they were called.

**The threshold, the invitation, the scan, and arbitration stayed with people. The new step is getting a usable scan.**

**Whose working loop has an automatic filter in it — and who reviews what got filtered?**

## Speaker notes

The stage has been named, and now, step by step: what actions it's made of, and who does each one. The woman with the letter the lecture opened with has arrived — and from here on a system decides about her in which she takes part at no step at all. On the slide, seven actions of that system are named in one line each; here, each gets its own.

Set the threshold. The age at which people get called in, and the interval between invitations, are written into a health-authority document. They're set not by the developer and not by the doctor at the monitor, but by whoever decided what's worse — missing something or calling in someone unnecessarily.

Call in by list. The letter reaches a person who hasn't complained about anything: they were picked by a group criterion — age, sex, occupation, prior diagnosis.

Take the study. The scan is taken by a technician, and that's its own qualification, its own workstation, its own queue.

Read it by two. Double reading was invented before any automation at all, for one reason: so that one person's mistake doesn't become the decision. The payoff comes from the mismatch of errors — two people's misses land on different scans — and it rests on the second reader not seeing the first one's conclusion.

Resolve a disagreement. A third reader is brought in only where the two disagreed, and resolving the disagreement falls to someone who wrote neither of the two conclusions.

Report the outcome. Either a "normal" letter, or a call inviting further testing — and weeks of waiting in between.

Sort those who came in with no appointment. Here it's decided who gets seen today and who in two weeks. Someone walking into an emergency department is assigned to one of five severity categories: a nurse asks a few questions, takes a few readings, and checks them against a table. Each category gets a mandated time to be seen by a doctor. Underestimating it — someone with a developing heart attack sits in the waiting room; overestimating it — a resource gets tied up that someone else needed. Both errors are paid for by the same shift.

Now the same field with a model, and it has to be said precisely at which step it switches on in each of this section's breakdowns — otherwise the examples and the stage end up living on two separate layers. The third row of the diagram names this by name.

The step "read it by two" — the Swedish screening program. The first reading stays human; no study bypasses the radiologist. The model scores the scan for risk, and that score decides whether the study needs a second independent reading. It doesn't work as a second reader: for most of the flow, the second-reading step is simply removed.

The step "report the outcome" — retinal fundus photography with no ophthalmologist. There, the model switches on right after the photograph is taken and takes over both the reading and the outcome: "refer or not" gets decided on the spot, in under a minute, and there's no arbitration step in this order at all.

The step "sort the flow" — the first-line chatbot. And here there's an important caveat the diagram can't state: the chatbot sits at a different entry point of the stage. Nobody is called in here by a list — people come in on their own, with a complaint, and the slot the model now occupies was previously occupied by a phone triage line with an operator working from protocol. The stage has no single pipeline, and that's not nitpicking: the cost of error at the no-complaint entry and the complaint-driven entry is different, while the construction of the step is the same.

What the model doesn't take over. It doesn't set the threshold: behind that sits the cost of both errors and a signature under it. It doesn't touch the invitation, the scan, or arbitration. And it adds exactly one step: getting a usable scan — an operation the specialist never had before, since they used to compensate for shooting conditions themselves.

Nothing follows "no," and nowhere is it written down: an event that didn't happen leaves no trace in the chart.

And a property of this scale that will come up more than once: its weights are set by people and published. A trained model, standing at the same spot, produces the same output — a category or a priority — and doesn't present its own weights. Comparing it becomes possible only by result.

That woman's path through this system looks like this: a technician takes the scan; it's read by two radiologists who have never seen her and don't talk to each other about her; if they disagree, the scan goes to a third; a few weeks later a "normal" letter arrives, or a call inviting further testing. At none of these steps is she asked anything.

The woman with the letter the lecture opened with has arrived — and from here on a system works around her in which she takes part at no step at all: a technician takes the scan, it's read by two radiologists who have never seen her and don't talk to each other about her, if they disagree the scan goes to a third, and a few weeks later a "normal" letter arrives, or a call inviting further testing.
