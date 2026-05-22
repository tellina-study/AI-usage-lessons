---
id: s17
type: assertion_visual
duration_min: 3
assertion: "PLC Copilot purpose-built: 3-4 дня → 10 минут, 85% точности. Generic ChatGPT на PLC — провал."
---

## Visible content

Purpose-built vs generic LLM на PLC; engineer-in-loop обязателен.

## Speaker notes

Конкретный пример провала generic LLM на PLC. ChatGPT на запрос «оптимизируй этот блок Siemens S7-1500» выдаёт инструкцию MOV %M99999. Что не так. В Siemens S7-1500 M-область — флаги памяти — ограничена до M65535. Адрес %M99999 не существует. PLC откажется компилировать программу. Это не «иногда галлюцинирует», это структурное ограничение. Generic LLM не знает scan-based execution PLC (циклы 1–10 мс), не знает legal addresses конкретной модели контроллера, не различает Siemens S7 от Allen-Bradley ControlLogix.

Альтернатива — purpose-built инструменты. PLC Copilot, PLCAutoPilot, Wipro PARI. Они знают IEC 61131-3 — ladder logic, structured text, function block diagram. Валидируют адреса памяти по модели контроллера до выдачи кода. Понимают scan time. С engineer-in-loop дают 85% точности. Скорость: то, что раньше занимало 3-4 дня инженерной работы, делается за 10 минут. 15% ошибок ловит инженер на стадии review.

Это правильный паттерн A1 — AI предлагает, инженер ревьюит, симулятор валидирует, safety-проверка пропускает только то, что прошло, и только тогда deployment. Структурное ограничение: AI-генерация PLC-кода применима, только если есть симулятор для валидации, safety-протоколы перед deployment, инженер с правом veto.
