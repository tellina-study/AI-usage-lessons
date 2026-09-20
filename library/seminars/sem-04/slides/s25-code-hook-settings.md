---
id: s25
type: assertion_visual
duration_min: 1.5
assertion: "git symbolic-ref --short HEAD, а не git rev-parse --abbrev-ref HEAD — у свежего репозитория без единого коммита rev-parse падает и молча оставляет проверку нерабочей"
learning_goal: "Решение ступени 3 — рабочий PreToolUse-хук из шаблона курса целиком, разбор построчно"
visual:
  pattern: code_block_card
  primary: "Блок кода целиком, дословно из 29-code-settings.json.txt: hooks.PreToolUse, matcher Bash, command — jq извлекает команду, grep ищет git commit, проверка is-inside-work-tree, проверка ветки main/master, hookSpecificOutput с permissionDecision deny/ask, timeout 10."
  backup: "Готово — источник library/seminars/sem-04/assets/captures/29-code-settings.json.txt, перенесено дословно"
---

# `.claude/settings.json`: хук защиты main

## Assertion

git symbolic-ref --short HEAD, а не git rev-parse --abbrev-ref HEAD — у свежего репозитория без единого коммита rev-parse падает и молча оставляет проверку нерабочей.

## Visual

Блок кода на всю ширину слайда, моноширинный шрифт, JSON-подсветка, дословно из капчура:

```jsonc
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.command' | { read -r cmd; if echo \"$cmd\" | grep -qE '(^|[;&|]\\s*)git\\s+commit\\b'; then if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then echo '{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"ask\",...}}'; exit 0; fi; branch=$(git symbolic-ref --short HEAD 2>/dev/null); if [ \"$branch\" = \"main\" ] || [ \"$branch\" = \"master\" ]; then echo '{\"hookSpecificOutput\":{...,\"permissionDecision\":\"deny\",\"permissionDecisionReason\":\"BLOCKED: direct commit to main/master. Create a feature branch first.\"}}'; exit 0; fi; fi; }",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

## Speaker notes

Процитируем рабочий хук из шаблона курса целиком и разберём по частям. `"matcher": "Bash"` — хук вызывается только перед вызовами инструмента `Bash`, не перед чтением файлов или другими действиями. `jq -r '.tool_input.command'` вытаскивает саму команду из JSON, который Claude Code передаёт хуку через stdin, — хук не видит весь диалог, только конкретный вызов. `grep -qE` ищет `git commit` как отдельную команду в начале строки или после `;`, `&`, `|`, не как подстроку внутри чего-то другого.

Ключевая деталь — выбор команды определения ветки: `git symbolic-ref --short HEAD`, а не более привычная `git rev-parse --abbrev-ref HEAD`. У свежего репозитория, в котором ещё нет ни одного коммита, «unborn HEAD», `rev-parse` завершается ошибкой и молча оставляет проверку ветки нерабочей — хук как будто есть, а определить текущую ветку не может вообще. `symbolic-ref` резолвит имя ветки корректно в обоих случаях, и с коммитами, и без них.

Вторая деталь — проверка `! git rev-parse --is-inside-work-tree`. Если это вообще не git-репозиторий — например, шаблон скопировали в обычную папку до `git init` — хук не пропускает коммит молча, что выглядело бы как защита без защиты, а возвращает `"ask"` с явным предупреждением: гейт неактивен, потому что репозитория ещё нет.

Наконец, формат ответа — `hookSpecificOutput.permissionDecision`, современный JSON-контракт хука. Отдельный нюанс, не показанный живой демонстрацией: код возврата `2` блокирует действие безусловно, даже если тот же хук вернул JSON с `"allow"` — код выхода побеждает JSON-решение внутри него.

Обратите внимание и на `"timeout": 10` в конце блока — десять секунд на всю проверку, включая запуск `jq` и двух вызовов `git`. Это не случайное число: слишком короткий таймаут рискует отвалиться на медленной машине и пропустить коммит без проверки, слишком длинный — заметно тормозит каждую попытку коммита, даже безопасную. Файл, который вы видите на слайде, — не абстрактный пример из документации, а рабочий файл из шаблона курса, тот же самый, который будет скопирован в `signup-landing/.claude/settings.json` без сокращений. Сейчас посмотрим, как этот хук ведёт себя на реальной попытке коммита.
