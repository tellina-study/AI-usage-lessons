#!/usr/bin/env bash
# Самопроверка круга по КЛОНУ, а не по своей пересборке.
#
# Зачем именно клон. Измерено на круге 2026-10-19 и записано в sobrat_razdel.py:
# сессия пересобрала раздел, получила чистый PDF — и закоммитила при этом СТАРЫЙ
# артефакт. Фикс был реален, а тот, кто открыл бы PDF по ссылке из ветки, увидел
# бы ровно тот баг, о котором отчитались как о закрытом. Поймала это соседняя
# сессия, прогнав сторож по ЗАКОММИЧЕННОМУ файлу. Отсюда правило: проверяется
# то, что лежит в ветке, а не то, что лежит в рабочем каталоге.
set -euo pipefail

VETKA="${1:-sec5-r2-otziv}"
KLON="${2:-/tmp/sec5-r2-klon}"
RAZDEL=4   # section: кадров раздела 5 (см. IMENA в sobrat_razdel.py)
IMYA=sec5-kvalifikaciya-i-iznos

rm -rf "$KLON"
git clone --branch "$VETKA" --single-branch \
  https://github.com/tellina-study/AI-usage-lessons.git "$KLON"

cd "$KLON/library/lectures/lec-07/rework/deck"
. /home/harness/.local/lo-portable-env.sh

echo "################ 1. СБОРКА: блокирующие предупреждения"
IDS=$(python3 - <<'PY'
import re, sys, yaml
sys.path.insert(0, '.')
import build_lec07 as B
from deckkit import slidefile
out = []
for f in slidefile.slide_files(B.SLIDES_DIR):
    m = re.match(r"^---\n(.*?)\n---", f.read_text(encoding="utf-8"), re.S)
    meta = yaml.safe_load(m.group(1)) if m else {}
    if str((meta or {}).get("section") or "").split(".")[0] == "4":
        out.append(f.name.split("-")[0])
print(",".join(out))
PY
)
echo "кадры раздела: $IDS"
python3 build_lec07.py --only "$IDS"

echo "################ 2. ПРЕДГЕЙТОВЫЙ СКАН по собранному pptx"
python3 pregeyt_skan.py chastichnaya-sborka.pptx

echo "################ 3. СВЕРКА ДИВАЙДЕРА С ЗАГОЛОВКАМИ РАЗБОРОВ"
# Общий код сторожа не роняет прогон: он ненулевой, пока расхождения есть хоть где,
# а в разделе 2 их семь и они пре-существующие. Проверяется СВОЙ раздел.
python3 sverka_reestra.py > /tmp/sverka.txt 2>&1 || true
cat /tmp/sverka.txt
python3 "$(dirname "$0")/proverit_svoy_razdel.py" "$RAZDEL" /tmp/sverka.txt

echo "################ 4. НАЛОЖЕНИЯ — по ЗАКОММИЧЕННОМУ файлу, ДО всякой пересборки"
# Порядок здесь несущий. Если сначала пересобрать, сторож проверит пересборку,
# а не то, что лежит в ветке, — то есть ровно тот зазор, от которого скрипт заведён.
python3 proverka_nalozheniy.py "$IMYA.pdf"
pdftotext -layout "$IMYA.pdf" /tmp/zakommichen.txt
STR_DO=$(pdfinfo "$IMYA.pdf" | awk '/^Pages/{print $2}')
echo "страниц в закоммиченном: $STR_DO"

echo "################ 5. ПЕРЕСБОРКА РАЗДЕЛА + замер слов по PDF"
python3 sobrat_razdel.py "$RAZDEL"

echo "################ 5а. СВЕЖЕСТЬ АРТЕФАКТА: текстовый слой до и после пересборки"
# Двоичного равенства у PDF не будет (метки времени), поэтому сверяется ТЕКСТ.
# Расхождение здесь означает одно: в ветке лежит артефакт старше своих исходников.
pdftotext -layout "$IMYA.pdf" /tmp/peresobran.txt
STR_POSLE=$(pdfinfo "$IMYA.pdf" | awk '/^Pages/{print $2}')
echo "страниц после пересборки: $STR_POSLE"
if diff -q /tmp/zakommichen.txt /tmp/peresobran.txt >/dev/null; then
  echo "СВЕЖИЙ: текстовый слой закоммиченного PDF совпал с пересборкой"
else
  echo "УСТАРЕЛ: закоммиченный PDF расходится со своими исходниками"
  diff /tmp/zakommichen.txt /tmp/peresobran.txt | head -40
  exit 1
fi
python3 proverka_nalozheniy.py "$IMYA.pdf"

echo "################ 6. АНГЛИЦИЗМЫ в видимом слое"
python3 ../../../../../tools/presentation-build/deep_latin_scan.py "$IMYA.pdf" || true

echo
echo "ГОТОВО. Числа выше сняты с клона ветки $VETKA, не с рабочего каталога."
