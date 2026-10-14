# -*- coding: utf-8 -*-
"""РЕНДЕР И ПРОВЕРКА ПАКЕТА: PDF и PNG по требованию, живые ссылки в XML.

Оба сборщика держали это у себя, и оба одинаково: `soffice --convert-to pdf`,
затем `pdftoppm`. Здесь оно одно, и по двум причинам сверх общей.

РЕНДЕР ВСЕГДА ПО ТРЕБОВАНИЮ И ВСЕГДА С ТАЙМАУТОМ. `soffice` на деках этого
курса дважды вешал машину на часы (`notes/mcp-limitations.md` [#223-6],
[#229-2]). Предупреждения считаются при сборке PPTX и от рендера не зависят,
поэтому обычный прогон его не трогает.

ОКРУЖЕНИЕ НУЖНО ОБЕИМ КОМАНДАМ. `pdftoppm` лежит в том же переносном наборе
(`lo-sysroot/usr/bin`), что и `soffice`, а не в системном `PATH`. Пока
подготовка окружения стояла только у первой команды, рендер падал кодом 127
(«pdftoppm: command not found») УЖЕ ПОСЛЕ того, как PDF собран: сборка
сообщала об ошибке, PDF лежал на диске, снимков не было. Чинится тем, что
окружение готовится один раз и для обеих.
"""
import subprocess
import zipfile
from pathlib import Path

from lxml import etree

LO_ENV = Path("/home/harness/.local/lo-portable-env.sh")
TIMEOUT = 115                 # секунд на команду; дальше — снимаем


def render_cmds(pptx, snaps, dpi, env):
    """Две команды рендера строками. Вынесено из `render`, чтобы путь можно
    было проверить, НЕ запуская LibreOffice: обе команды делают `cd` в папку
    деки, и относительный путь в них складывал PDF в `<папка>/<папка>/`, а
    `pdftoppm` затем падал «Couldn't open file». Пути здесь обязаны быть
    абсолютными — это и проверяет проба `[рендер-путь]`."""
    pdf = pptx.with_suffix(".pdf")
    return [
        f'{env}cd "{pptx.parent}" && soffice --headless --convert-to pdf '
        f'--outdir "{pptx.parent}" "{pptx.name}"',
        f'{env}cd "{pptx.parent}" && pdftoppm -r {dpi} -png "{pdf.name}" '
        f'"{snaps}/k"',
    ]


def render(pptx, snaps_dir, *, dpi=110, timeout=TIMEOUT, env_sh=LO_ENV):
    """PPTX → PDF рядом с ним → PNG по кадру в `snaps_dir`. 0 — вышло."""
    # АБСОЛЮТНЫЕ пути, и это не вкусовщина: обе команды делают `cd` в папку
    # деки, поэтому относительный путь после `cd` указывает уже не туда,
    # куда указывал у вызывающего. Найдено сессией заключения круга #229:
    # PDF уезжал в `<папка>/<папка>/`, снимки не снимались вовсе.
    pptx, snaps = Path(pptx).absolute(), Path(snaps_dir).absolute()
    snaps.mkdir(parents=True, exist_ok=True)
    env = f". {env_sh} && " if Path(env_sh).exists() else ""
    pdf = pptx.with_suffix(".pdf")
    cmds = render_cmds(pptx, snaps, dpi, env)
    for c in cmds:
        try:
            r = subprocess.run(["bash", "-lc", c], timeout=timeout,
                               capture_output=True, text=True)
            if r.returncode:
                print(f"рендер: код {r.returncode}\n{r.stderr[-600:]}")
                return 1
        except subprocess.TimeoutExpired:
            print(f"рендер: таймаут {timeout} с — снято, см. "
                  "notes/mcp-limitations.md [#223-6]")
            return 1
    print(f"рендер готов: {pdf.name}, снимки в {snaps.name}/")
    return 0


def verify_links(path):
    """`r:id` в XML сохранённого файла. Самоотчёт не принимается: ссылка
    считается поставленной только тогда, когда отношение лежит в пакете."""
    A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
    body, notes, targets = 0, 0, 0
    with zipfile.ZipFile(path) as z:
        for nm in z.namelist():
            if not nm.endswith(".xml"):
                continue
            if nm.startswith("ppt/slides/slide"):
                body += sum(1 for e in etree.fromstring(z.read(nm))
                            .iter(f"{A}hlinkClick") if e.get(f"{R}id"))
            elif nm.startswith("ppt/notesSlides/notesSlide"):
                notes += sum(1 for e in etree.fromstring(z.read(nm))
                             .iter(f"{A}hlinkClick") if e.get(f"{R}id"))
        for nm in z.namelist():
            if ".rels" in nm and ("slides/_rels" in nm
                                  or "notesSlides/_rels" in nm):
                targets += sum(1 for e in etree.fromstring(z.read(nm)).iter()
                               if e.get("Type", "").endswith("/hyperlink"))
    print(f"\nгиперссылки в XML: подвал {body} · заметки {notes} · "
          f"отношений в пакете {targets}")
    return body + notes, targets
