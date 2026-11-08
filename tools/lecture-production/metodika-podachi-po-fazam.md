---
status: canon
owner: владелец курса
issue: 307
дата: "2026-11-03"
---

# Методика подачи по фазам конвейера (ENFORCED)

Вынесено из [`README.md`](README.md) §3.7g по лимиту в 600 строк. **Любой агент, занятый фазами
1, 2, 5, 6, 7, 9, 10 или проходом перед гейтом, читает этот файл и названные в нём разделы
методики.**

**Канон:** [`../metodika-podachi/README.md`](../metodika-podachi/README.md) (два потока, что где
лежит, карта потока повествования целиком) → [`../metodika-podachi/00-RAMKA.md`](../metodika-podachi/00-RAMKA.md)
(маршрут из 11 шагов) → файл нужного слоя. Решением владельца 2026-11-03 методика переехала из
заметок исследования в канонический слой инструментов и действует в производстве.

**Зачем ENFORCED.** Замер перед переносом: 7709 строк методики в 24 файлах, и ни `CLAUDE.md`, ни
один из 14 агентов, ни один навык, ни `../presentation-build/README.md`, ни `README.md` этой же
папки на неё не ссылались. Агент, собиравший деку, не узнавал о ней никогда.

## Таблица обязанностей — двумя потоками

| Фаза | Поток 1: повествование (чем рассказываем) | Поток 2: кадр (чем показываем) |
|---|---|---|
| **1** — критика плана | план назван в терминах повествования: ось, вопрос лекции, keystone, строение раздела из пяти шагов, реестр разборов — [`../metodika-podachi/povestvovanie/09-POVESTVOVANIE-SBORKA.md`](../metodika-podachi/povestvovanie/09-POVESTVOVANIE-SBORKA.md) §2 (шаги 1–10); чеклист из 14 проверок линии — `-part2.md` §5. Исполняет `methodology-critic` | — (кадров ещё нет) |
| **2** — черновик главы | четыре источника материала и грамматика разбора — `../metodika-podachi/povestvovanie/09-POVESTVOVANIE-SBORKA.md` §1, §3; поля записи линии — [`../metodika-podachi/povestvovanie/08-POVESTVOVANIE-ZAPIS.md`](../metodika-podachi/povestvovanie/08-POVESTVOVANIE-ZAPIS.md) §1–2. Исполняет `book-editor` | — |
| **5** — слайды из главы | линия, прошедшая чеклист, подаётся на вход разнарядке | **шов:** разнарядка **до рисования первого кадра** — [`../metodika-podachi/shov/03-RAZNARYADKA.md`](../metodika-podachi/shov/03-RAZNARYADKA.md) §1–3, дерево выбора формы §3, три исхода отказа §4. Сдаёт `presentation-designer`, принимает `methodology-critic` |
| **6** — рисование | — | язык кадра [`../metodika-podachi/kadr/01-YAZYK-KADRA.md`](../metodika-podachi/kadr/01-YAZYK-KADRA.md) (+`-part2`); поле заполнения формы [`../metodika-podachi/kadr/02-KATALOG-FORM.md`](../metodika-podachi/kadr/02-KATALOG-FORM.md) (33 формы); роль кадра в ритме [`../metodika-podachi/kadr/04-RITM-KOLODY.md`](../metodika-podachi/kadr/04-RITM-KOLODY.md). Исполняет `presentation-designer`, `/build-deck` |
| **7** — критика деки | смысловой ритм раздела и сквозная линия с числом на закрытии — `../metodika-podachi/povestvovanie/09-POVESTVOVANIE-SBORKA-part2.md` §4. Исполняет `methodology-critic` | приёмка: пол из 14 числовых порогов — [`../metodika-podachi/priyomka/07-PRIYOMKA.md`](../metodika-podachi/priyomka/07-PRIYOMKA.md) §1.1–1.14; потолок — `-part2.md` §2.1; зелёный пол приёмки сам не даёт — `-part2.md` §4.5. Исполняет `presentation-critic` |
| **8.5** — перед гейтом B | — | порядок проверки: числом на полном прогоне файла раньше, чем глазами на распечатке разворотами по 12–16 кадров — [`../metodika-podachi/priyomka/07-PRIYOMKA-part2.md`](../metodika-podachi/priyomka/07-PRIYOMKA-part2.md) §3. Исполняет `/pre-user-gate mode=slides` |
| **9** — черновик речи | швы между разборами и порядок пяти шагов раздела в речи — `../metodika-podachi/povestvovanie/09-POVESTVOVANIE-SBORKA.md` §2 (шаги 7–10). Исполняет `speech-writer` | — |
| **10** — критика речи, сверка артефактов | линия речи совпадает с записанной линией повествования — `../metodika-podachi/povestvovanie/08-POVESTVOVANIE-ZAPIS.md` §2. Исполняет `methodology-critic`, `consistency-checker` | — |

**Жанр.** Семинар читает те же файлы обоих потоков плюс жанровую дельту
[`../metodika-podachi/05-ZHANRY.md`](../metodika-podachi/05-ZHANRY.md): несущая единица, действие
зала, устройство арки, глубина опоры, заметки, формы только одного жанра.

**Чем проверен каждый поток.** Поток кадра — пробой #307 (пять кругов, 42 записи трения). Поток
повествования — ни разу; см. `../metodika-podachi/README.md` §3.

## Чего методика не закрывает

Фактчек, долю провалов и ограничений ≥30%, контраст и кегль на настоящем проекторе в настоящем
зале, и всё, что видно только живым проведением занятия (`README.md` §3.8). Перечень —
`../metodika-podachi/00-RAMKA.md` §7.

## Прежде чем доверять нулю

Показатель меряет то, что легко достать, а не то, про что спрашивают — формулировка владельца,
шесть случаев в [`../metodika-podachi/PERENOSIMOE.md`](../metodika-podachi/PERENOSIMOE.md) §1.
Назови предмет вопроса; назови, что программа физически берёт; придумай случай, где эти два
расходятся. Придумался за минуту — показатель сломан, и ноль на нём ничего не значит. Прогон,
показавший ноль, ничего не значит и до тех пор, пока не доказано, что проверка умеет находить
(`../presentation-build/deckkit/probes.py`).
