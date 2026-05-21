---
id: s26
type: assertion_visual
duration_min: 2.5
assertion: "Arup CFO-дипфейк scam: Hong Kong Jan 2024, $25.6M за 15 транзакций. Финансист на видеозвонке с дипфейк-CFO + colleagues."
learning_goal: "Case 6: deepfake корпоративный fraud"
learning_outcomes: [LO4, LO5]
chapter_ref: "§3.7 — Deepfakes: Arup CFO scam"
references: [arup-cnn, arup-fortune]
visual:
  pattern: assertion_visual
  primary: "CNN article screenshot + attack diagram (Финансист → видеозвонок с дипфейк-CFO+colleagues → 15 транзакций → $25.6M) + «Урок: проверка через независимый канал»"
  backup: assets/backup/s26-arup.png
---

# Arup CFO-дипфейк scam — $25.6M (Case 6)

## Assertion

Arup CFO-дипфейк scam: Hong Kong Jan 2024, $25.6M за 15 транзакций. Финансист на видеозвонке с дипфейк-CFO + colleagues.

## Visual

Сверху assertion 24pt. Слева — CNN article headline screenshot мокап в Ocean rounded box: «Finance worker pays out $25 million after video call with deepfake CFO». Справа — attack diagram (5-этапный horizontal pipeline с right-arrows): (1) Финансист в Hong Kong получает email от «CFO» → (2) приглашение на видеозвонок → (3) видеозвонок с дипфейк-CFO + 5-6 deepfake colleagues → (4) 15 transactions → (5) $25.6M (HK$200M) gone. Под diagram — Arup chip: «Engineering firm, Sydney Opera House designer». Внизу — gold «УРОК ДЛЯ ИНЖЕНЕРА»: «Видеозвонок ≠ подтверждение личности в 2024+. Финансовые транзакции требуют проверка через независимый канал (обратный звонок по известному номеру, многофакторная аутентификация)».

## Speaker notes

Шестой кейс — Arup CFO-дипфейк scam. Январь 2024 года, Hong Kong. Arup — крупная британская инженерная firm, известная как designer Sydney Opera House и многих других эталонная строений. Сценарий атаки. Финансист Arup в Hong Kong получил email от человека, представившегося CFO компании, с приглашением на видеозвонок для обсуждения confidential transaction. Финансист принял приглашение. На видеозвонке были «CFO» plus пять-шесть других сотрудников компании, узнаваемых лиц и голосов. Все были deepfakes. На звонке «CFO» дал инструкции совершить пятнадцать транзакций на общую сумму двести миллионов гонконгских долларов — двадцать пять и шесть миллиона долларов США. Финансист, следуя инструкциям того, кого он узнал как своего CFO в видеозвонке, выполнил все пятнадцать транзакций. Деньги пропали. Arup обнаружила scam только когда финансист задал routine question CFO напрямую через другой канал. CNN и Fortune опубликовали детальный coverage этого случая. Это первый publicly documented случай корпоративный fraud такого масштаба через deepfake video, и он установил новый baseline корпоративный security risk. Что эта инцидент означает практически. Видеозвонок перестал быть подтверждение личности. В 2024 году технология deepfake-video в реальном времени стала commercially available и cheap. Один scammer с access к public photos и videos target persons может организовать видеозвонок с реалистичными deepfakes одиннадцати-двенадцати человек одновременно. Урок для инженера: видеозвонок не равно подтверждение личности в 2024 году и позже. Финансовые транзакции требуют проверка через независимый канал — обратный звонок по известному номеру, многофакторная аутентификация, в идеале — face-to-face confirmation для крупных сумм. Этот случай — wake-up call для финансовых процесс внутри компаний. Если в твоей компании authorization транзакций основана только на recognition «лица CFO» через видеозвонок — у тебя Arup-class риск, и его нужно закрывать структурно: процессно через mandatory callback, технологически через cryptographic signatures или MFA на транзакциях.
