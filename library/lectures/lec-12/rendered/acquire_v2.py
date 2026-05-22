#!/usr/bin/env python3
"""Acquire real images via Wikimedia Commons SEARCH.

For each subject, search Commons → pick top file result with imageinfo → download.
"""
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (lec-12 educational research; kzlevko@gmail.com)"
DEST = Path("/tmp/lec-12-wt/library/lectures/lec-12/rendered/assets/screenshots")
DEST.mkdir(parents=True, exist_ok=True)


def api_get(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())


def search_commons(query: str, limit: int = 8):
    """Return a list of File: titles ranked by Commons search."""
    q = urllib.parse.quote(query)
    url = (
        f"https://commons.wikimedia.org/w/api.php?"
        f"action=query&format=json&list=search&srnamespace=6&srlimit={limit}&srsearch={q}"
    )
    try:
        data = api_get(url)
        hits = data.get("query", {}).get("search", [])
        return [h["title"] for h in hits]
    except Exception as e:
        print(f"  search err for '{query}': {e}", file=sys.stderr)
        return []


def get_thumb_url(title: str, width: int = 1280):
    """Return thumb URL for a File: title, or None."""
    t = urllib.parse.quote(title)
    url = (
        f"https://commons.wikimedia.org/w/api.php?"
        f"action=query&format=json&prop=imageinfo&iiprop=url|size&iiurlwidth={width}&titles={t}"
    )
    try:
        data = api_get(url)
        pages = list(data.get("query", {}).get("pages", {}).values())
        if not pages or "imageinfo" not in pages[0]:
            return None
        ii = pages[0]["imageinfo"][0]
        # Skip tiny images (<400px width)
        if ii.get("thumbwidth", 0) < 400:
            return None
        return ii["thumburl"]
    except Exception:
        return None


def download(url: str, out_path: Path):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            content = r.read()
        out_path.write_bytes(content)
        return len(content)
    except Exception as e:
        print(f"  download err {url}: {e}", file=sys.stderr)
        return 0


# Skip patterns: avoid logos, signs, low-quality
def is_bad(title: str) -> bool:
    t = title.lower()
    bad = ["logo", "sign", "patent", "diagram", ".pdf", ".djvu", ".webm", ".ogv", ".tif",
           "1900", "1920", "1930", "1940", "1950", "1960", "1880", "1890", "thumbnail"]
    return any(b in t for b in bad)


SUBJECTS = [
    # (subject keyword for Commons search, output filename, fallback queries)
    ("Hannover Messe industrial fair Siemens robot",  "s01-hannover-messe.jpg",
     ["Hannover Messe robot", "Industrial 4.0 factory exhibition", "Siemens Hannover Messe"]),
    ("Siemens digital industries Amberg factory",     "s07-siemens-amberg.jpg",
     ["Siemens factory Amberg electronics", "Siemens HQ Munich", "Siemens Industrial"]),
    ("container port abandoned project",               "s09-container-port.jpg",
     ["container port Singapore terminal", "port of Singapore Tuas", "container terminal"]),
    ("BMW factory robot assembly line",                "s12-bmw-factory.jpg",
     ["BMW Leipzig plant interior", "BMW factory Munich", "BMW production line"]),
    ("cement plant industrial facility",               "s13-cement-plant.jpg",
     ["cement factory plant", "cement industry rotary kiln", "Heidelberg Cement"]),
    ("MES manufacturing execution system SCADA panel", "s16-mes-scada.jpg",
     ["SCADA control room", "industrial control room operator", "Manufacturing operator panel"]),
    ("PLC programmable logic controller cabinet",      "s17-plc-cabinet.jpg",
     ["Siemens S7 PLC", "Allen Bradley PLC", "programmable logic controller industrial"]),
    ("Yokogawa chemical plant distillation column",    "s20-yokogawa-plant.jpg",
     ["distillation column chemical plant", "naphtha cracker", "petrochemical plant Yokohama"]),
    ("NVIDIA Omniverse industrial digital twin",       "s21-nvidia-omniverse.jpg",
     ["NVIDIA office Santa Clara", "NVIDIA RTX GPU", "NVIDIA headquarters"]),
    ("Agility Robotics Digit humanoid logistics",      "s25-digit-humanoid.jpg",
     ["humanoid robot manufacturing", "Agility Robotics Cassie", "bipedal robot warehouse"]),
    ("container port harbor crane terminal",           "s27-port-harbor.jpg",
     ["container port aerial view Singapore", "Hong Kong port terminal", "Tuas Singapore container"]),
    ("WEF Davos conference factory of future",         "s35-wef-davos.jpg",
     ["World Economic Forum meeting Davos", "Davos congress center", "industry leaders conference"]),
    ("KAMAZ truck factory Tatarstan",                  "s37-kamaz.jpg",
     ["KAMAZ Naberezhnye Chelny truck", "Kamaz vehicle Russian", "KAMAZ assembly"]),
    ("Norilsk Nickel mining processing",               "s37-nornickel.jpg",
     ["Norilsk Nickel Bystrinsky", "Norilsk mining Russia", "Norilsk smelter copper"]),
    ("Toyota assembly line RAV4 vehicle production",   "s39-toyota-line.jpg",
     ["Toyota Motor Manufacturing", "Toyota plant Kentucky assembly", "Toyota production line"]),
    # Additional case-supporting images
    ("computer vision quality inspection factory",     "s12-vision-qc.jpg",
     ["machine vision camera factory", "industrial camera inspection", "automated optical inspection"]),
    ("predictive maintenance sensor equipment",        "s13-pdm-sensor.jpg",
     ["vibration sensor industrial", "rotating equipment maintenance", "industrial IoT sensor"]),
    ("manufacturing factory floor smart sensors",      "s33-smart-factory.jpg",
     ["Industry 4.0 factory floor", "smart manufacturing", "automated factory line"]),
]


def acquire_for_subject(query_primary: str, out_name: str, fallbacks: list) -> bool:
    queries = [query_primary] + fallbacks
    seen = set()
    for q in queries:
        titles = search_commons(q, limit=10)
        for t in titles:
            if t in seen:
                continue
            seen.add(t)
            if is_bad(t):
                continue
            url = get_thumb_url(t, 1280)
            if not url:
                continue
            out = DEST / out_name
            size = download(url, out)
            if size > 30000:  # at least 30KB to be real photo
                print(f"OK    {out_name} ({size} bytes) ← {t} (query: '{q}')")
                return True
            else:
                # delete tiny file
                if out.exists():
                    out.unlink()
    print(f"FAIL  {out_name} (all queries exhausted)")
    return False


if __name__ == "__main__":
    ok = 0
    fail = 0
    for primary, out_name, fallbacks in SUBJECTS:
        out_path = DEST / out_name
        if out_path.exists() and out_path.stat().st_size > 30000:
            print(f"SKIP  {out_name} (already present, {out_path.stat().st_size} bytes)")
            ok += 1
            continue
        if acquire_for_subject(primary, out_name, fallbacks):
            ok += 1
        else:
            fail += 1
    print(f"\n=== Done: OK={ok}, FAIL={fail} ===")
