#!/usr/bin/env bash
# Съёмка веб-страниц для слайдов: поднимает браузер в среде, где нет ни браузера, ни прав root.
#
# ЗАПУСКАТЬ ТОЛЬКО ТАК — без конвейера:
#
#   source tools/presentation-build/setup_page_shots.sh
#   python3 tools/presentation-build/shoot_page.py <url> <выход.png>
#
# `source … | tail -5`, `source … 2>&1 | head`, `$(source …)` — НЕЛЬЗЯ: конвейер исполняет
# скрипт в подоболочке, экспорт LD_LIBRARY_PATH умирает вместе с ней, и chromium падает с
# exitCode=127 — то есть выглядит это точно как «библиотек нет», отправляя читателя в тот самый
# тупик, который скрипт и существует закрыть. Вывод смотреть отдельной командой после source.
# Скрипт сам предупреждает об этом вслух (см. ниже), но предупреждение в конвейере можно
# и не заметить. Цена ошибки — один потерянный прогон (notes/mcp-limitations.md, поправка 1
# к `[#229-3]`).
#
# Зачем это здесь. Снимок страницы — единственный честный способ добыть кадр для слайда,
# который предъявляет страницу регулятора, карточку испытания или ленту отзыва. Рисовать
# «похожую на источник» карточку правилам курса запрещено, поэтому без браузера такие кадры
# просто не добываются — и сессия добычи иллюстраций Лекции 7 упёрлась ровно в это: восемь
# кадров, включая обязательный hero, остались не добыты.
#
# Почему так сложно. В среде нет браузера; `apt-get install` требует root; sudo запрещён
# флагом ядра «no new privileges» — не паролем, а конфигурацией, то есть обойти нечем.
# Единственный работающий путь: скачать системные пакеты как обычный пользователь,
# распаковать их в свой каталог и подложить браузеру через LD_LIBRARY_PATH.
set -u
LIBDIR="${PAGE_SHOT_LIBS:-$HOME/.cache/page-shot-libs}"
# Файл-сигнал: пишется ТОЛЬКО после последней успешной распаковки. Пропуск загрузки
# проверяется по нему, а не по наличию каталога: прогон, убитый на середине (а здесь убивают —
# дроссель cgroup, `[#229-4]`), оставляет каталог с неполным набором библиотек, и симптом
# у него тот же exitCode=127.
STAMP="$LIBDIR/.page-shot-libs-complete"
PKGS="libasound2t64 libatk1.0-0t64 libatk-bridge2.0-0t64 libatspi2.0-0t64 libcairo2
libcups2t64 libpango-1.0-0 libpangocairo-1.0-0 libxcomposite1 libxdamage1 libxfixes3
libxrandr2 libnspr4 libnss3 libxkbcommon0 libgbm1 libdrm2 libxshmfence1 libpixman-1-0
libfontconfig1 libfreetype6 libharfbuzz0b libfribidi0 libthai0 libgraphite2-3 libdatrie1
libcloudproviders0 libavahi-client3 libavahi-common3 libdbus-1-3 libexpat1
libxcb-render0 libxi6 libxrender1 libxcb-shm0 libxcursor1 libxinerama1"

# --- проверка способа запуска -------------------------------------------------------------
# Экспорт LD_LIBRARY_PATH доживает до следующей команды только если скрипт прочитан `source`
# в той самой оболочке, которая потом вызовет shoot_page.py. Два способа это испортить:
# запустить скрипт как программу (свой процесс — экспорту некуда деться) и завернуть source
# в конвейер или $(…) (подоболочка — то же самое). Оба распознаются; скрипт не падает,
# а предупреждает: автор мог знать, что делает (например, ставит библиотеки «на будущее»).
PAGE_SHOT_BADCALL=""
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  PAGE_SHOT_BADCALL="скрипт запущен как программа, а не прочитан через source"
elif [[ "${BASHPID:-$$}" != "$$" ]]; then
  PAGE_SHOT_BADCALL="source завёрнут в подоболочку (конвейер или \$(…))"
elif [[ -p /dev/stdout ]]; then
  PAGE_SHOT_BADCALL="вывод уходит в конвейер — похоже на source … | …"
fi
if [[ -n "$PAGE_SHOT_BADCALL" ]]; then
  echo "!!! ВНИМАНИЕ: $PAGE_SHOT_BADCALL." >&2
  echo "!!! Экспорт LD_LIBRARY_PATH не выживет, и chromium упадёт с exitCode=127 —" >&2
  echo "!!! это будет выглядеть как «нет библиотек», хотя они на месте." >&2
  echo "!!! Правильно: source tools/presentation-build/setup_page_shots.sh (без конвейера)." >&2
fi

# --- библиотеки ----------------------------------------------------------------------------
if [[ -f "$STAMP" ]]; then
  echo "набор библиотек на месте ($LIBDIR), загрузка не нужна"
else
  if [[ -d "$LIBDIR/x" ]]; then
    echo "набор библиотек неполон — предыдущий прогон не доработал, загружаю заново"
    echo "  (каталог $LIBDIR/x есть, файла-сигнала нет: значит последняя распаковка не дошла)"
  else
    echo "раскладываю системные библиотеки в $LIBDIR (один раз)"
  fi
  mkdir -p "$LIBDIR/x" && cd "$LIBDIR" || { return 1 2>/dev/null || exit 1; }
  rm -f ./*.deb
  failed=""
  for p in $PKGS; do
    apt-get download "$p" -q 2>/dev/null >/dev/null || { echo "  не вышло: $p"; failed="$failed $p"; }
  done
  for d in *.deb; do
    [[ -e "$d" ]] || continue
    dpkg-deb -x "$d" x 2>/dev/null || { echo "  не распаковалось: $d"; failed="$failed $d"; }
  done
  rm -f ./*.deb
  cd - >/dev/null || { return 1 2>/dev/null || exit 1; }
  if [[ -z "$failed" ]]; then
    # Последняя распаковка дошла — только теперь набор можно считать полным.
    date -u +"%Y-%m-%dT%H:%M:%SZ" > "$STAMP"
    echo "$PKGS" | tr -s ' \n' '\n' | sed '/^$/d' >> "$STAMP"
    echo "набор библиотек собран целиком, записан файл-сигнал $STAMP"
  else
    rm -f "$STAMP"
    echo "НАБОР НЕПОЛОН, файл-сигнал не записан. Не добыто:$failed" >&2
    echo "Следующий запуск повторит загрузку целиком — это ожидаемо, не сбой." >&2
  fi
fi

python3 -c "import playwright" 2>/dev/null || {
  echo "ставлю playwright и браузер"
  pip install --quiet --break-system-packages --user playwright
  python3 -m playwright install chromium
}

export LD_LIBRARY_PATH="$(find "$LIBDIR/x" -name '*.so*' -type f 2>/dev/null \
  | xargs -n1 dirname | sort -u | tr '\n' ':')${LD_LIBRARY_PATH:-}"
echo "готово. LD_LIBRARY_PATH подложен, браузер поднимается."
if [[ -n "$PAGE_SHOT_BADCALL" ]]; then
  # Повтор в самом конце: предупреждение сверху срезается `| tail -5`, то есть именно тем
  # вызовом, о котором оно и предупреждает.
  echo "!!! НО: $PAGE_SHOT_BADCALL — LD_LIBRARY_PATH подложен в оболочку, которая сейчас" >&2
  echo "!!! умрёт. Повторите: source tools/presentation-build/setup_page_shots.sh" >&2
fi
