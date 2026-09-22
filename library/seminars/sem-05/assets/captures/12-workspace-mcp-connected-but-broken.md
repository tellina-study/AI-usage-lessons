# Контрпример: `claude mcp list` показывает "Connected", сервер фактически не работает

Не воспроизведено живой командой (нет реального `workspace-mcp` в demo-окружении) — взято
дословной цитатой из уже существующего, независимо задокументированного инцидента этого же
проекта. Это честнее, чем имитировать вывод `claude mcp list`, который я не могу воспроизвести
без реально сломанного сервера.

Источник: `notes/mcp-limitations.md`, запись `[#49] OAuth refresh token отзывается каждые 7 дней`:

> - **Server:** `workspace-mcp`
> - **Tool / feature:** все Drive/Docs/Sheets/Slides tools.
> - **Symptom:** Все вызовы возвращают `ACTION REQUIRED: Google Authentication Needed`, хотя
>   `claude mcp list` показывает сервер как `✓ Connected`.
> - **Root cause:** OAuth-приложение в Google Cloud Console находится в **Testing** publishing
>   status. В этом режиме refresh_token автоматически отзывается через 7 дней неактивности.
> - **Severity:** P0 (всё лежит)
> - **First seen in:** #49 (2026-04-29).

Второй, независимый инцидент того же сервера (та же таблица, запись `[#86]`) — `claude mcp list`
показывает `✗ Failed to connect` (регрессия транзитивной зависимости `aiofile` 3.10.0). Обе записи
живые, из фактической эксплуатации этого проекта, не сочинены для семинара.
