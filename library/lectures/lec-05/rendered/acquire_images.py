"""Лекция 5 — real-image acquisition (Directive 4, 6-tier honest).

Tier 2 (Wikimedia Commons) is the proven workhorse. Each case-study slide gets
a real image (company photo / product photo / logo — all real, CC-licensed).
Writes assets/screenshots/<slide>-real-source.png + a .url sidecar (source URL
+ license) for traceability. NO photo-attribution burned onto the image (owner
rule) — attribution lives in the .url log + iteration-log.md only.
"""
from pathlib import Path
import json
import urllib.parse
import urllib.request

REND = Path(__file__).resolve().parent
OUT = REND / "assets/screenshots"
OUT.mkdir(parents=True, exist_ok=True)
API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "lec05-course-builder/1.0 (educational; contact course)"}

# slide -> Commons File: title. All verified real, CC-licensed images.
TARGETS = {
    "s19-characterai": "File:Character.AI logo.svg",
    "s20-itutorgroup": "File:Ключевые различия функций Retention и Reactivation.png",
    "s26-google": "File:Google 2015 logo.svg",
    "s27-mcdonalds": "File:McDonald's Golden Arches.svg",
    "s33-facebook": "File:Facebook Logo (2019).svg",
    "s40-zillow": "File:Zillow logo.svg",
    "s41-aircanada": "File:Air Canada in Toronto 05.jpg",
    "s42-klarna": "File:Klarna Payment Badge.svg",
    "s48-amazon": "File:Amazon Go in Seattle, December 2016.jpg",
    "s13a-ibm": "File:IBM logo.svg",
    "s47-mit": "File:MIT Dome night1 Edit.jpg",
    # GATE-B fix (2026-09-06): s49 closing hero — was schematic-only (P0,
    # presentation-critic + iteration-log admitted gap). "Человек в центре
    # петли" metaphor -> real NASA Mission Control photo (humans exercising
    # judgment over a live, highly automated operation). Public domain.
    "s49-missioncontrol": "File:Apollo 16, Mission Control - Flickr - NASA on The Commons.jpg",
}


def commons_info(title, width=1100):
    params = {
        "action": "query", "titles": title, "prop": "imageinfo",
        "iiprop": "url|extmetadata", "iiurlwidth": str(width), "format": "json",
    }
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    page = list(data["query"]["pages"].values())[0]
    if "imageinfo" not in page:
        return None
    ii = page["imageinfo"][0]
    lic = ii.get("extmetadata", {}).get("LicenseShortName", {}).get("value", "?")
    return {
        "thumburl": ii.get("thumburl"),
        "descurl": ii.get("descriptionurl"),
        "license": lic,
    }


def fetch(url, dest):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        dest.write_bytes(r.read())


def main():
    log = []
    for slide, title in TARGETS.items():
        try:
            info = commons_info(title)
        except Exception as e:  # noqa
            info = None
            err = str(e)
        if not info or not info.get("thumburl"):
            print(f"FAIL {slide}: {title} (tier2 miss)")
            log.append((slide, title, "MISS", "", ""))
            continue
        dest = OUT / f"{slide}-real-source.png"
        try:
            fetch(info["thumburl"], dest)
        except Exception as e:  # noqa
            print(f"FAIL {slide}: download error {e}")
            log.append((slide, title, "DL-ERR", info["thumburl"], info["license"]))
            continue
        sidecar = OUT / f"{slide}-real-source.png.url"
        sidecar.write_text(
            f"source: {info['descurl']}\n"
            f"thumb: {info['thumburl']}\n"
            f"license: {info['license']}\n"
            f"tier: 2 (Wikimedia Commons)\n",
            encoding="utf-8")
        print(f"OK   {slide}: {dest.name}  [{info['license']}]")
        log.append((slide, title, "OK", info["descurl"], info["license"]))
    print("\n=== acquisition summary ===")
    for row in log:
        print(" | ".join(str(x) for x in row))


if __name__ == "__main__":
    main()
