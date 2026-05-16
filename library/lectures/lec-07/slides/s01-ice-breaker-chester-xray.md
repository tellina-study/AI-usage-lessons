---
id: s01
type: live_demo
duration_min: 3
assertion: "AI ставит метку патологии на рентгене за ~3 секунды — локально в браузере, без облака. Это narrow CV, не ChatGPT."
learning_goal: "Открывающий hook: medical AI — работающий локальный инструмент, narrow CV"
learning_outcomes: [LO1]
frame_mapping: ["Другой AI", "Безопасность"]
chapter_ref: "§0.1 — Что AI делает в медицине сегодня"
references: [cohen-2019-chester, rajpurkar-2017-chexnet, wang-2017-cxr8]
visual:
  pattern: external_demo
  primary: "Live drag-drop Chester AI X-ray в браузер — heatmap + probability scores для 18 патологий; обрамлено Ocean rounded box; assertion слева"
  illustration:
    type: live_demo
    sources:
      - "https://mlmed.org/tools/xray/ (Chester AI tool, Mila Quebec / McGill — primary live demo)"
      - "https://arxiv.org/abs/1901.11210 (Cohen et al. 2019 — Chester paper)"
      - "Backup PNG: assets/backup/chester-pneumonia-result.png — pre-saved screenshot heatmap + 18-class probabilities"
    caption: "Chester AI (Cohen et al. 2019, Mila/McGill) — runs locally in browser"
  backup: assets/backup/chester-pneumonia-result.png
interaction: live_demo
---

# AI ставит метку патологии на рентгене за ~3 секунды

## Assertion

AI ставит метку патологии на рентгене за ~3 секунды — локально в браузере, без облака. Это narrow CV, не ChatGPT.

## Visual

Слева assertion крупно (28pt) + под ней определение narrow CV мелким шрифтом. Справа — обрамлённое Ocean rounded box окно браузера со страницей Chester AI: рентгеновский снимок грудной клетки и heatmap красно-жёлтых пятен над предполагаемой патологией, ниже — таблица из 18 строк с probability scores (pneumonia, cardiomegaly, atelectasis, pleural effusion и т. д.). Подпись под скриншотом: «Chester AI · runs locally in browser · ~3 sec».

## Speaker notes

Перед вами один конкретный пример того, что AI делает в медицине сегодня. На сайте `mlmed.org/tools/xray/` открыт публичный инструмент Chester AI, разработанный группой Cohen et al. в Mila Quebec и McGill University. Если перетащить в окно браузера любой рентгеновский снимок грудной клетки, модель примерно за три секунды выдаёт вероятностный профиль по восемнадцати патологиям — пневмония, кардиомегалия, ателектаз, плевральный выпот и так далее — и тепловую карту, показывающую, в какие области изображения «смотрела» модель.

Три свойства этой демонстрации задают тон лекции. Во-первых, модель работает локально в браузере: изображение не загружается на сервер, не покидает устройство. Это design choice разработчиков, отражающий тот факт, что медицинские данные — особая категория, требующая privacy-by-design. Во-вторых, это не LLM, а narrow computer vision: конкретная свёрточная архитектура, потомок CheXNet (Rajpurkar et al. 2017), обученная на сотнях тысяч размеченных рентгеновских снимков. ChatGPT не умеет ставить метку патологии на рентгене за три секунды; Chester умеет, но не умеет писать стихи. Каждая система — узкая. И в-третьих, это уровень технологий 2017–2024 годов в рутинно работающей сегодня форме: пять лет назад такая возможность была демонстрационной, сейчас — производственной. AI в медицине, о котором мы будем говорить в этой главе, — это технологически зрелое поле, а не лабораторный эксперимент.
