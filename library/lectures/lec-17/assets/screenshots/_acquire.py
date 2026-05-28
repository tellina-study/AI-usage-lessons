#!/usr/bin/env python3
"""6-tier image acquisition helper for Lec-17 case images.
Tier 2 focus: Wikimedia Commons search -> imageinfo thumburl (free license, best success).
Falls back to direct upload.wikimedia URLs for known-good files.
Writes <slug>.<ext> + <slug>.url (source/tier/attribution/license).
"""
import sys, json, urllib.parse, subprocess, os, re

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
DEST = os.path.dirname(os.path.abspath(__file__))

def curl(url, binary=False, timeout=30):
    args = ["curl", "-sL", "--max-time", str(timeout), "-A", UA, url]
    if binary:
        r = subprocess.run(args, capture_output=True)
        return r.stdout
    r = subprocess.run(args, capture_output=True, text=True, errors="replace")
    return r.stdout

def commons_search(query, want=8):
    """Return list of (title, descurl) image File: pages from Commons search."""
    api = ("https://commons.wikimedia.org/w/api.php?action=query&format=json"
           "&generator=search&gsrnamespace=6&gsrlimit=%d&gsrsearch=%s"
           "&prop=imageinfo&iiprop=url|extmetadata|size&iiurlwidth=1280"
           % (want, urllib.parse.quote(query)))
    try:
        d = json.loads(curl(api))
    except Exception as e:
        return []
    pages = d.get("query", {}).get("pages", {})
    out = []
    for p in pages.values():
        ii = p.get("imageinfo", [{}])[0]
        thumb = ii.get("thumburl") or ii.get("url")
        w = ii.get("thumbwidth") or ii.get("width") or 0
        meta = ii.get("extmetadata", {})
        lic = meta.get("LicenseShortName", {}).get("value", "?")
        artist = re.sub("<[^>]+>", "", meta.get("Artist", {}).get("value", "")).strip()
        out.append({
            "title": p.get("title"),
            "thumb": thumb,
            "descurl": ii.get("descriptionurl", ""),
            "width": w,
            "license": lic,
            "artist": artist[:120],
        })
    return out

def save(slug, url, ext, tier, attribution, license_):
    binpath = os.path.join(DEST, f"{slug}.{ext}")
    data = curl(url, binary=True)
    if not data or len(data) < 3000:
        return False, f"empty/too-small ({len(data) if data else 0}b)"
    with open(binpath, "wb") as f:
        f.write(data)
    # verify dimensions via Pillow
    try:
        from PIL import Image
        im = Image.open(binpath)
        w, h = im.size
    except Exception as e:
        os.remove(binpath)
        return False, f"not-an-image: {e}"
    if max(w, h) < 700:
        os.remove(binpath)
        return False, f"too-small {w}x{h}"
    with open(os.path.join(DEST, f"{slug}.url"), "w") as f:
        f.write(f"source: {url}\ntier: {tier}\nattribution: {attribution}\n"
                f"license: {license_}\ndimensions: {w}x{h}\n")
    return True, f"OK {w}x{h} ({len(data)//1024}KB)"

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "search":
        for r in commons_search(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 8):
            print(f"[{r['width']}px] {r['license']:18} {r['title']}")
            print(f"      thumb: {r['thumb']}")
    elif cmd == "thumb":
        # thumb "File:Foo.jpg"  -> print thumburl @1280
        title = urllib.parse.quote(sys.argv[2])
        api = ("https://commons.wikimedia.org/w/api.php?action=query&format=json"
               "&titles=%s&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=1280" % title)
        try:
            d = json.loads(curl(api))
            p = list(d["query"]["pages"].values())[0]
            ii = p.get("imageinfo", [{}])[0]
            meta = ii.get("extmetadata", {})
            lic = meta.get("LicenseShortName", {}).get("value", "?")
            print((ii.get("thumburl") or ii.get("url") or "") + "\t" + lic)
        except Exception as e:
            print("\tERR " + str(e))
    elif cmd == "catfiles":
        # catfiles "Category:Foo" limit
        cat = urllib.parse.quote(sys.argv[2])
        lim = sys.argv[3] if len(sys.argv) > 3 else "15"
        api = ("https://commons.wikimedia.org/w/api.php?action=query&format=json"
               "&list=categorymembers&cmtitle=%s&cmtype=file&cmlimit=%s" % (cat, lim))
        try:
            d = json.loads(curl(api))
            for m in d.get("query", {}).get("categorymembers", []):
                print(m["title"])
        except Exception as e:
            print("ERR " + str(e))
    elif cmd == "ogimage":
        # ogimage <page_url>  -> print og:image / twitter:image
        html = curl(sys.argv[2])
        for pat in (r'property="og:image"[^>]*content="([^"]+)"',
                    r'content="([^"]+)"[^>]*property="og:image"',
                    r'name="twitter:image"[^>]*content="([^"]+)"',
                    r'name="twitter:image:src"[^>]*content="([^"]+)"'):
            m = re.search(pat, html)
            if m:
                print(m.group(1)); break
        else:
            print("")
    elif cmd == "save":
        # save <slug> <url> <ext> <tier> <attribution> <license>
        ok, msg = save(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
        print(("OK " if ok else "FAIL ") + sys.argv[2] + ": " + msg)
