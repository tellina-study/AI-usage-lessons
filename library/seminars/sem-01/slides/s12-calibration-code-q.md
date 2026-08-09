---
id: s12
type: comparison
duration_min: 1.3
assertion: "Кто автор — код: AI или человек?"
learning_goal: "Калибровка 3/5 — код, акцент на измеримом выигрыше"
learning_outcomes: []
references: [requests-library-psf]
visual:
  pattern: two_code_voting_cards
  primary: "2 code-блока Ocean rounded box карточки (monospace шрифт): реальная функция из библиотеки requests + AI-сгенерированный аналог"
---

# Кто автор — код: AI или человек?

## Assertion

Кто автор — код: AI или человек?

## Visual

Round-2: убран voting badge «рука+камера» и AI/человек pill-кнопки под карточками
(голосуем поднятием руки, объяснено на s05) — code-карточки теперь занимают полную
высоту блока. 2 Ocean rounded box карточки с monospace-шрифтом (JetBrains Mono /
Courier New fallback), тёмный code-block фон. Код A:

```python
def prepare_method(self, method):
    """Prepares the given HTTP method."""
    self.method = method
    if self.method is not None:
        self.method = to_native_string(self.method.upper())
```

Код B: AI-сгенерированная маленькая функция похожего масштаба (например,
нормализация имени HTTP-заголовка).

## Speaker notes

Третья категория — код. Две маленькие функции, примерно одного масштаба. Голосуем: какую написал человек, какую — AI.

Здесь тоже важен не только вопрос авторства: в чём измеримая разница в продуктивности между «получить функцию от AI» и «использовать проверенную библиотеку»? Обсудим это в разборе.

После голосования спросите: что натолкнуло на выбор — стиль именования переменных, docstring, структура условной проверки?
