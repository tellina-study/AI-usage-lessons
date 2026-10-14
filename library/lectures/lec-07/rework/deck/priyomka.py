#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ПРИЁМКА деки: один прогон вместо семи, одна сводка вместо семи выводов.

ЗАЧЕМ. Прогонов у деки семь, у каждого свой каталог запуска, свой формат
вывода и свой код возврата. Собирать из них приёмку руками — значит
читать семь выдач подряд и держать в голове, какая из них про файлы
кадров, а какая про собранный PDF. Первое же расхождение между ними при
таком чтении не замечается: оно не в одном выводе, а МЕЖДУ двумя.

ЧТО ЭТОТ ПРОГОН ДЕЛАЕТ СВЕРХ ЗАПУСКА СЕМИ КОМАНД — три вещи, и каждая
куплена ошибкой этого производства.

1. **Проверяет, что прогон сообщил, ЧТО он прочитал.** Дважды за это
   производство инструмент молча терял вход и выдавал правдоподобный
   ответ: `git ls-tree` с путём от корня репозитория вернул ноль файлов,
   и счёт разборных кадров вышел нулевым вместо тридцати; разбор числа
   по частям кадра считал подвал по сырому полю и завышал его втрое. С
   тех пор печать прочитанного — требование ко всем прогонам, и приёмка
   его ПРОВЕРЯЕТ: прогон, не сказавший, сколько файлов он открыл,
   помечается отдельно. Это не придирка к формату — это единственный
   способ отличить «чисто» от «не читал».

2. **Отличает отказ от чистого результата.** Упавший прогон, прогон с
   пустым выводом и прогон, не нашедший замечаний, в сводке выглядят
   по-разному и считаются по-разному. `zamer-osi.py`, запущенный не из
   того каталога, падает с `FileNotFoundError` — и если смотреть только
   на последние строки вывода, это читается как «ничего не нашлось».

3. **Сводит то, что меряют двое.** Вес кадра меряют `ocenka.py` (по
   файлу, секунды) и `render_sec.py` (по собранному PDF, минуты).
   Числа отчёта даёт только второй; первый нужен, чтобы не гонять
   сборку на каждую правку абзаца. Расхождение между ними — предмет
   приёмки, а не мелочь: именно на таком расхождении в этом
   производстве дважды ошиблись (112 против 183 по PDF).

ЧТО БЛОКИРУЕТ ПРИЁМКУ. Самопроверка раскладки, запреты видимого слоя,
повторы в заметках и — когда зовут со сборкой — замер собранного PDF.
Перепись форм, счёт повествования и ось главы приёмку НЕ блокируют:
это измерения, а не пороги, и решение по ним принимает человек.

    python3 priyomka.py                 # всё, кроме сборки (быстро)
    python3 priyomka.py --sborka        # + собрать деку и замерить PDF
    python3 priyomka.py --sborka 0 1 4  # сборка только названных разделов
    python3 priyomka.py --polno         # печатать вывод каждого прогона целиком

Код возврата: 0 — приёмка пройдена; 1 — есть блокирующие замечания;
2 — какой-то прогон отказал, и приёмка не состоялась (это НЕ «чисто»).
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

DECK = Path(__file__).resolve().parent
GLAVA = DECK.parent
VYVOD = DECK / "priyomka-vyvod"

# Строка, которой прогон сообщает, что он прочитал. Отсутствие такой
# строки — само по себе замечание: см. пункт 1 в шапке файла.
CHTO_PROCHITAL = re.compile(
    r"(прочитано:[^\n]*|кадров просмотрено:[^\n]*|кадров:\s*\d+[^\n]*|"
    r"страниц\s+\d+[^\n]*|кадров в деке[^\n]*|файлов[^\n]*прочт[^\n]*|"
    r"проверок доказано:[^\n]*)")


class Progon:
    def __init__(self, imya, cmd, cwd, blokiruet, vedro=None):
        self.imya, self.cmd, self.cwd = imya, cmd, cwd
        self.blokiruet, self.vedro = blokiruet, vedro
        self.kod = None
        self.out = ""
        self.otkaz = None          # причина отказа, если прогон не состоялся

    def zapustit(self, timeout=1800):
        try:
            r = subprocess.run([sys.executable, *self.cmd], cwd=self.cwd,
                               capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            self.otkaz = f"не уложился в {timeout} с"
            return
        except OSError as e:
            self.otkaz = f"не запустился: {e}"
            return
        self.kod = r.returncode
        self.out = (r.stdout or "") + (r.stderr or "")
        if not self.out.strip():
            self.otkaz = "пустой вывод"
        elif "Traceback (most recent call last)" in self.out:
            # Падение с ненулевым кодом поймает сам код; но прогон может
            # упасть ВНУТРИ и вернуть ноль — такое здесь уже было.
            self.otkaz = "упал с исключением"

    @property
    def prochital(self):
        m = CHTO_PROCHITAL.search(self.out)
        return m.group(1).strip() if m else None

    @property
    def verdikt(self):
        if self.otkaz:
            return "ОТКАЗ"
        if not self.blokiruet:
            return "справка"
        return "чисто" if self.kod == 0 else "ЕСТЬ ЗАМЕЧАНИЯ"


def progony(sborka, razdely):
    """Состав приёмки. Каталог запуска у прогонов разный — это их свойство,
    и приёмка его знает за человека: `zamer-osi.py` вне каталога главы
    падает, а `storozh_dublej.py` вне `deck/` не находит кадров."""
    p = [
        # Первым — свежесть входа: приёмка, собранная по устаревшему PDF, это
        # не приёмка. Канон §11 называет три случая за одно производство, и
        # он же называет счёт кадров против манифестов дешёвой проверкой,
        # ловящей весь класс «генератор молча выбросил кадр».
        Progon("свежесть входа и счёт кадров", ["svezhest_vkhoda.py"],
               DECK, True),
        Progon("самопроверка раскладки", ["build_lec07.py", "--selftest"],
               DECK, True),
        Progon("запреты видимого слоя", ["scan_deck_visible.py"], DECK, True),
        Progon("повторы в заметках", ["storozh_dublej.py"], DECK, True),
        Progon("вес кадров, заметки, минуты", ["ocenka.py"], DECK, True),
        Progon("перепись форм", ["perepis_form.py"], DECK, False),
        Progon("счёт повествования", ["qa/zamer-povestvovaniya.py"],
               GLAVA, False),
        Progon("ось главы", ["qa/zamer-osi.py"], GLAVA, False),
    ]
    p.append(Progon("кромка кадра по PDF", ["storozh_kromki.py"], DECK, True))
    if sborka:
        p.append(Progon("замер собранного PDF",
                        ["render_sec.py", *(razdely or ALL_SEC)], DECK, True))
    # Пол кегля, наезды текста и полупустые коробки — по СОБРАННОМУ PDF.
    # Прогон был в деке и в составе приёмки не стоял, а это ровно та мера,
    # про которую канон говорит «числа этого прогона — единственные, на
    # которые в отчёте о раскладке можно ссылаться»: отчёт сборки смотрит
    # масштаб прогона тела и сказал «один кадр ниже пола» там, где по PDF
    # их было шесть.
    if (DECK / "lec-07-karkas.pdf").exists():
        p.append(Progon("пол кегля и раскладка по PDF", ["zamer_pdf.py"],
                        DECK, True))
    return p


ALL_SEC = [str(i) for i in range(0, 13)]


def vydelit(out, patterns):
    """Строки вывода, которые стоит поднять в сводку."""
    out_lines = []
    for ln in out.splitlines():
        if any(re.search(pat, ln) for pat in patterns):
            out_lines.append(ln.strip())
    return out_lines


ITOGI = {
    "свежесть входа и счёт кадров": [r"^\s*ЗАМЕЧАНИЕ", r"^кадров в объединении",
                                     r"совпадают поимённо", r"^замечаний:"],
    "пол кегля и раскладка по PDF": [r"ниже\s+\d+[.,]\d+\s*пт", r"^знаков",
                                     r"наезд", r"полупуст", r"^замечаний"],
    "повторы в заметках": [r"^повторов найдено", r"^повторов с общностью"],
    "запреты видимого слоя": [r"^кадров просмотрено"],
    "вес кадров, заметки, минуты": [r"^минут |^\s*заметки |тяжелее|ПОЛ НЕ ОБЪЯВЛЕН",
                                    r"ошибка ЭТОГО прогона", r"^прочитано:",
                                    r"РАЗМЕТКА ВЫХОДИТ НА ЭКРАН",
                                    r"пол \d+ объявлен"],
    "замер собранного PDF": [r"^страниц "],
    "кромка кадра по PDF": [r"^выходов за кромку", r"^\s+стр\.", r"^ОТКАЗ"],
    "самопроверка раскладки": [r"^проверок доказано|НЕ ЛОВИТ"],
    "счёт повествования": [r"разделов без|сцен"],
    "ось главы": [r"^\s*(МОЛЧАТ|называют|разделов)[^\n]*"],
}


def svodka(ps, polno):
    print("\n" + "=" * 72)
    print("СВОДКА ПРИЁМКИ")
    print("=" * 72)
    print(f"{'прогон':32} {'код':>4}  {'вердикт':16} что прочитал")
    nemye = []
    for q in ps:
        kod = "—" if q.kod is None else str(q.kod)
        pr = q.prochital or "— не сообщил —"
        if q.prochital is None and not q.otkaz:
            nemye.append(q.imya)
        print(f"{q.imya:32} {kod:>4}  {q.verdikt:16} {pr[:70]}")

    print("\nЧТО НАШЛОСЬ")
    for q in ps:
        if q.otkaz:
            print(f"\n  {q.imya}: ОТКАЗ — {q.otkaz}")
            print("     " + "\n     ".join(q.out.strip().splitlines()[-4:]))
            continue
        lines = vydelit(q.out, ITOGI.get(q.imya, [r"(?!)"]))
        if lines:
            print(f"\n  {q.imya}:")
            for ln in lines[:12]:
                print(f"     {ln}")
            if len(lines) > 12:
                print(f"     … ещё {len(lines) - 12} строк, "
                      f"целиком в {VYVOD.name}/")

    if nemye:
        print("\nНЕ СООБЩИЛИ, ЧТО ПРОЧИТАЛИ: " + ", ".join(nemye))
        print("  Это замечание к самим прогонам, а не к деке: без такой "
              "строки\n  «ничего не нашлось» неотличимо от «нечего было "
              "читать».")

    otkazy = [q.imya for q in ps if q.otkaz]
    zamech = [q.imya for q in ps if not q.otkaz and q.blokiruet and q.kod != 0]
    print("\n" + "-" * 72)
    if otkazy:
        print("ПРИЁМКА НЕ СОСТОЯЛАСЬ: отказали — " + ", ".join(otkazy))
        print("Это не «чисто»: часть проверок не выполнена вовсе.")
        return 2
    if zamech:
        print("ПРИЁМКА НЕ ПРОЙДЕНА: блокирующие замечания — "
              + ", ".join(zamech))
        return 1
    print("ПРИЁМКА ПРОЙДЕНА: блокирующих замечаний нет.")
    print("Справочные прогоны приёмку не блокируют — их числа читает человек.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("razdely", nargs="*", help="разделы для сборки")
    ap.add_argument("--sborka", action="store_true",
                    help="собрать деку и замерить PDF (минуты)")
    ap.add_argument("--polno", action="store_true",
                    help="печатать вывод каждого прогона целиком")
    a = ap.parse_args()

    VYVOD.mkdir(exist_ok=True)
    ps = progony(a.sborka, a.razdely)
    for q in ps:
        otkuda = q.cwd.name
        print(f"→ {q.imya}  ({' '.join(q.cmd)}, из {otkuda}/)", flush=True)
        q.zapustit()
        fn = VYVOD / (re.sub(r"[^а-яё]+", "-", q.imya.lower()) + ".txt")
        fn.write_text(q.out, encoding="utf-8")
        if a.polno:
            print(q.out)
    return svodka(ps, a.polno)


if __name__ == "__main__":
    sys.exit(main())
