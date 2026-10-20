"""Расхождения сверки реестра В СВОЁМ разделе, отдельно от чужих.

Зачем отдельный файл. `sverka_reestra.py` отдаёт ненулевой код, пока расхождения
есть хоть где в лекции, а в разделе 2 их семь и они пре-существующие — проверено
по базовой ветке `sec5-r1-rework`, там те же семь. Под `set -e` это обрывало
самопроверку на третьем шаге, и до наложений она не доходила ни разу: чужой долг
маскировал свой. Здесь код возврата считается по одному разделу.
"""
import re
import sys

NOMER = sys.argv[1] if len(sys.argv) > 1 else "4"
vyvod = open(sys.argv[2] if len(sys.argv) > 2 else "/tmp/sverka.txt", encoding="utf-8").read()

bloki = [b for b in re.split(r"\n(?=\d+\. )", vyvod) if b.startswith(NOMER + ". ")]
if not bloki:
    print(f"свой раздел {NOMER} в выводе сторожа НЕ НАЙДЕН — это сама по себе поломка")
    sys.exit(1)

svoy = bloki[0]
net = len(re.findall(r"^\s*НЕТ ", svoy, re.M))
ok = len(re.findall(r"^\s*ok ", svoy, re.M))
chuzhie = len(re.findall(r"^\s*НЕТ ", vyvod, re.M)) - net

print(f"свой раздел {NOMER}: дословных совпадений {ok}, расхождений {net}")
print(f"чужие расхождения в остальной лекции: {chuzhie} (пре-существующие, этим кругом не тронуты)")
sys.exit(1 if net else 0)
