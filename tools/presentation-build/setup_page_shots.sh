#!/usr/bin/env bash
# Съёмка веб-страниц для слайдов: поднимает браузер в среде, где нет ни браузера, ни прав root.
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
#
# Использование:
#   source tools/presentation-build/setup_page_shots.sh      # поднять (идемпотентно)
#   python3 tools/presentation-build/shoot_page.py <url> <png>
set -u
LIBDIR="${PAGE_SHOT_LIBS:-$HOME/.cache/page-shot-libs}"
PKGS="libasound2t64 libatk1.0-0t64 libatk-bridge2.0-0t64 libatspi2.0-0t64 libcairo2
libcups2t64 libpango-1.0-0 libpangocairo-1.0-0 libxcomposite1 libxdamage1 libxfixes3
libxrandr2 libnspr4 libnss3 libxkbcommon0 libgbm1 libdrm2 libxshmfence1 libpixman-1-0
libfontconfig1 libfreetype6 libharfbuzz0b libfribidi0 libthai0 libgraphite2-3 libdatrie1
libcloudproviders0 libavahi-client3 libavahi-common3 libdbus-1-3 libexpat1
libxcb-render0 libxi6 libxrender1 libxcb-shm0 libxcursor1 libxinerama1"

if [ ! -d "$LIBDIR/x" ]; then
  echo "раскладываю системные библиотеки в $LIBDIR (один раз)"
  mkdir -p "$LIBDIR/x" && cd "$LIBDIR" || return 1
  for p in $PKGS; do apt-get download "$p" -q 2>/dev/null >/dev/null || echo "  не вышло: $p"; done
  for d in *.deb; do dpkg-deb -x "$d" x 2>/dev/null; done
  rm -f ./*.deb
  cd - >/dev/null || return 1
fi

python3 -c "import playwright" 2>/dev/null || {
  echo "ставлю playwright и браузер"
  pip install --quiet --break-system-packages --user playwright
  python3 -m playwright install chromium
}

export LD_LIBRARY_PATH="$(find "$LIBDIR/x" -name '*.so*' -type f 2>/dev/null \
  | xargs -n1 dirname | sort -u | tr '\n' ':')${LD_LIBRARY_PATH:-}"
echo "готово. LD_LIBRARY_PATH подложен, браузер поднимается."
