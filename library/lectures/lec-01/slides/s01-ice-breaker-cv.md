---
id: s01
type: live_demo
duration_min: 3
assertion: "Идентификация людей в реальном времени — уже с 2023 года на простом ноутбуке."
learning_goal: "Открывающий hook: показать, что AI — рабочий инструмент, который запускается локально без облака"
learning_outcomes: [LO1, LO7]
references: [yolov8-ultralytics-2023, mediapipe-google]
visual:
  pattern: external_demo
  primary: "Live-камера на проекторе: real-time bounding-box детекция лиц/людей в зале + счётчик 'N people detected'. Слайд минимальный — главное на проекторе вне слайда."
  backup: assets/code/ice-breaker-cv/backup/screenshot.png
interaction: live_demo
---

## Visible content

**Минимальный слайд** — фокус на проекторе с live-демо.

Заголовок (assertion, hook на открытие):
Идентификация людей в реальном времени — уже с 2023 года на простом ноутбуке.

Определение (мелким шрифтом под заголовком):
*Narrow AI — модель решает одну задачу (обнаружение людей в кадре) и больше ничего.*

Подпись под скриншотом (caption):
Кадр модели в момент демо: 2 человека в боксах, локально, без интернета.

## Speaker notes

Live-демо: ноутбук + веб-камера, проектор показывает аудиторию в real-time с bounding-box детекцией лиц/людей и счётчиком «N people detected». Модель работает локально (YOLOv8 или MediaPipe Face Detection), без интернета, **~30 fps real-time на CPU ноутбука**.

Нарратив: «Эта модель обучена в 2023, видит вас впервые, работает на моём ноутбуке без облака. Это narrow AI — рабочая инженерная лошадка. Сегодня разберём весь зоопарк AI-инструментов и как инженеру в нём ориентироваться.»

Backup при отказе HDMI/камеры: `library/lectures/lec-01/assets/code/ice-breaker-cv/backup/screenshot.png` + 10-сек видео (если есть). Файл backup может отсутствовать на момент пилота — предусмотреть это до проведения лекции.

Источники: Ultralytics YOLOv8 (2023); MediaPipe (Google). Код демо — `library/lectures/lec-01/assets/code/ice-breaker-cv/` (`README.md`, `requirements.txt`, `run.py`, `backup/`).
