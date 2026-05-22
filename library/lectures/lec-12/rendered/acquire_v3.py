#!/usr/bin/env python3
"""Refine images: re-acquire weak matches with better-targeted queries."""
import json, sys, urllib.parse, urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (lec-12 educational research; kzlevko@gmail.com)"
DEST = Path("/tmp/lec-12-wt/library/lectures/lec-12/rendered/assets/screenshots")

def api_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())

def search_commons(q, limit=10):
    qe = urllib.parse.quote(q)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&list=search&srnamespace=6&srlimit={limit}&srsearch={qe}"
    try:
        d = api_get(url)
        return [h["title"] for h in d.get("query",{}).get("search",[])]
    except: return []

def thumb(title, width=1280):
    t = urllib.parse.quote(title)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url|size&iiurlwidth={width}&titles={t}"
    try:
        d = api_get(url)
        p = list(d.get("query",{}).get("pages",{}).values())
        if not p or "imageinfo" not in p[0]: return None
        ii = p[0]["imageinfo"][0]
        if ii.get("thumbwidth",0) < 400: return None
        return ii["thumburl"]
    except: return None

def download(url, out):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            content = r.read()
        out.write_bytes(content)
        return len(content)
    except: return 0

def is_bad(t):
    t = t.lower()
    bad = ["logo",".svg",".pdf",".djvu",".webm",".ogv",".tif",".gif","model",
           "patent","logo","1800","1850","1900","1920","1930","1940","plan",
           "diagram","drawing","cuba","torpedo","palace","democracy","civil",
           "patriotic","war","arafat","peres","windsock","floor plan"]
    return any(b in t for b in bad)

# Better queries for weak matches
REFINE = [
    # s12 — vision QC: existing s12-vision-qc.jpg was borescope (not good)
    ("automated optical inspection assembly line",  "s12-vision-qc.jpg",
     ["camera quality control manufacturing", "machine vision industrial inspection",
      "vision system production line", "visual inspection robot factory"]),
    # s13 — PdM was torpedos (wrong)
    ("industrial sensors monitoring equipment", "s13-pdm-sensor.jpg",
     ["IoT industrial sensor", "predictive maintenance vibration monitor",
      "industrial bearing health monitoring", "rotating machinery condition"]),
    # s33 — smart factory was floor plan
    ("smart factory automation assembly", "s33-smart-factory.jpg",
     ["Industry 4.0 manufacturing automation", "smart manufacturing robot",
      "automated production line car factory", "BMW Leipzig automated"]),
    # s35 — WEF was Arafat 2001 (irrelevant)
    ("Davos congress center World Economic Forum", "s35-wef-davos.jpg",
     ["Davos winter conference building", "World Economic Forum 2024 plenary",
      "WEF annual meeting Davos congress"]),
    # s20 — Yokogawa was windsock (wrong)
    ("oil refinery distillation tower", "s20-yokogawa-plant.jpg",
     ["petrochemical refinery distillation column", "chemical plant distillation tower",
      "naphtha refinery petrochemical", "JSR petrochemical plant"]),
    # s12 BMW factory was 325i car (wrong)
    ("BMW manufacturing plant interior assembly", "s12-bmw-factory.jpg",
     ["BMW Group factory production line", "BMW Welt Munich vehicle",
      "BMW Leipzig assembly hall", "BMW production hall robot"]),
    # s37 KAMAZ was truck in cuba (wrong)
    ("KAMAZ factory Naberezhnye Chelny", "s37-kamaz.jpg",
     ["KAMAZ vehicle Tatarstan", "KAMAZ-43118 military", "KamAZ truck Russian"]),
    # s27 - Antwerp port at sunset - fine, OK
    # Other new images we need:
    ("Toyota humanoid robot Digit warehouse", "s25-toyota-digit.jpg",
     ["Agility Digit robot logistics", "humanoid bipedal warehouse", "humanoid factory robot"]),
    ("control room operator industrial", "s16-control-room.jpg",
     ["chemical plant control room operator", "process control room display", "DCS distributed control room"]),
    ("Hannover Messe 2024 trade show booth", "s01-hannover-2024.jpg",
     ["Hannover Messe 2023 expo", "industrial trade show robotic arm", "Hannover Messe industrial exhibition"]),
]


if __name__ == "__main__":
    ok = 0
    for primary, out_name, fallbacks in REFINE:
        queries = [primary] + fallbacks
        success = False
        seen = set()
        for q in queries:
            titles = search_commons(q, 12)
            for t in titles:
                if t in seen: continue
                seen.add(t)
                if is_bad(t): continue
                u = thumb(t)
                if not u: continue
                out = DEST / out_name
                size = download(u, out)
                if size > 50000:
                    print(f"OK    {out_name} ({size}b) ← {t}")
                    success = True
                    break
                elif out.exists():
                    out.unlink()
            if success: break
        if success:
            ok += 1
        else:
            print(f"KEEP-OLD  {out_name} (refinement failed, keeping previous if exists)")
    print(f"\nRefined {ok} images")
