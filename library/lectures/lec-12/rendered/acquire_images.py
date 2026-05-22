#!/usr/bin/env python3
"""Acquire real images for lec-12 via Wikimedia Commons (Tier 2).

Per CLAUDE.md no-mock-fallbacks rule.
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (lec-12 educational research; kzlevko@gmail.com)"
DEST = Path("/tmp/lec-12-wt/library/lectures/lec-12/rendered/assets/screenshots")
DEST.mkdir(parents=True, exist_ok=True)


def fetch_commons(title: str, out_name: str, width: int = 1280) -> bool:
    """Fetch a Wikimedia Commons image by title; save to DEST/out_name."""
    title_enc = urllib.parse.quote(title)
    api = (
        f"https://commons.wikimedia.org/w/api.php?"
        f"action=query&format=json&prop=imageinfo&iiprop=url&iiurlwidth={width}"
        f"&titles=File:{title_enc}"
    )
    try:
        req = urllib.request.Request(api, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read())
        pages = list(data.get("query", {}).get("pages", {}).values())
        if not pages or "imageinfo" not in pages[0]:
            print(f"FAIL  {title}: no imageinfo (missing on Commons)")
            return False
        url = pages[0]["imageinfo"][0]["thumburl"]
        # Download image
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            content = r.read()
        out = DEST / out_name
        out.write_bytes(content)
        size = len(content)
        print(f"OK    {out_name} ({size} bytes) from {title}")
        return True
    except Exception as e:
        print(f"FAIL  {title}: {e}")
        return False


TARGETS = [
    # s01 hero — industrial AI scene
    ("AGV-Siemens_ANS.jpg", "s01-agv-siemens.jpg"),
    ("Flexiv_Hannover_Messe.jpg", "s01-flexiv-hannover.jpg"),
    ("Industrie_4.0.jpg", "s01-industry40.jpg"),
    # s07 / s10 — Siemens HQ
    ("Siemens-headquarters-2017.jpg", "s07-siemens-hq.jpg"),
    ("Siemens_Berlin_2024-04-08.jpg", "s07-siemens-berlin.jpg"),
    ("Siemens_AG_Headquarter_Munich.jpg", "s07-siemens-munich.jpg"),
    # s09 — container port
    ("Port_of_Singapore-Keppel_Terminal.jpg", "s09-singapore-keppel.jpg"),
    ("Singapore_-_Container_Port_-_panoramio.jpg", "s09-port-singapore.jpg"),
    ("Maersk_Mc-Kinney_Moller_at_Aarhus.jpg", "s09-maersk-ship.jpg"),
    # s10 — vision QC / factory
    ("Robot_at_BMW_Factory.jpg", "s12-bmw-robot.jpg"),
    ("BMW_Welt,_München,_Alemania16.jpg", "s12-bmw-welt.jpg"),
    ("BMW_Group_Plant_Munich.jpg", "s12-bmw-plant.jpg"),
    # s13 — cement plant / chemical plant
    ("Cement_Mill.jpg", "s13-cement-mill.jpg"),
    ("Hima_Cement_Plant.jpg", "s13-cement-himalaya.jpg"),
    ("Cement_Plant_Pannonia_Heat_Exchanger.jpg", "s13-cement-pannonia.jpg"),
    # s16 — SCADA / PLC / industrial control panel
    ("Modicon_Quantum.jpg", "s16-modicon-plc.jpg"),
    ("SCADA_HMI.jpg", "s16-scada-hmi.jpg"),
    ("Industrial_Control_Panel.jpg", "s16-control-panel.jpg"),
    # s17 — code / programming
    ("Ladder_diagram_example.png", "s17-ladder.png"),
    # s20 — Yokogawa / distillation
    ("Yokogawa_Electric_Headquarters.jpg", "s20-yokogawa-hq.jpg"),
    ("Distillation_column_Petrokimia_Gresik.jpg", "s20-distill-column.jpg"),
    ("Naphtha_Cracker_2.jpg", "s20-naphtha-cracker.jpg"),
    # s21 — NVIDIA / Omniverse
    ("Nvidia_headquarters_logo.jpg", "s21-nvidia-hq.jpg"),
    ("NVIDIA_Voyager_HQ.jpg", "s21-nvidia-voyager.jpg"),
    # s25 — Toyota / BMW humanoid
    ("BMW_Plant_Leipzig.JPG", "s25-bmw-leipzig.jpg"),
    ("Toyota_Motor_Manufacturing_Kentucky.jpg", "s25-toyota-kentucky.jpg"),
    ("Toyota_assembly_line_LA_Auto_Show_2014.jpg", "s25-toyota-assembly.jpg"),
    # s27 — Port hero §5
    ("Port_of_Hong_Kong-Kwai_Chung-Aerial.jpg", "s27-hk-port-aerial.jpg"),
    ("Aerial_view_of_Port_of_Singapore.jpg", "s27-singapore-aerial.jpg"),
    # s35 — Lighthouse / WEF
    ("World_Economic_Forum_Annual_Meeting_2018.jpg", "s35-wef-davos.jpg"),
    ("Davos_2024_(Open_Forum).jpg", "s35-davos-2024.jpg"),
    # s37 — КАМАЗ / Норникель
    ("KAMAZ_Sokol.jpg", "s37-kamaz-truck.jpg"),
    ("KAMAZ-43509.jpg", "s37-kamaz-43509.jpg"),
    ("Norilsk_Nickel_Bystrinsky_GOK.jpg", "s37-nornickel-bystrinsky.jpg"),
    ("Норильск_Никель_(2017-08-30).jpg", "s37-nornickel-norilsk.jpg"),
    # s39 closing hero — Toyota Digit / humanoid logistics
    ("Toyota_Motor_Manufacturing_Kentucky_assembly_line.jpg", "s39-toyota-assembly.jpg"),
    ("Agility_Robotics_Digit.jpg", "s39-digit.jpg"),
    ("Toyota_RAV4_2.jpg", "s39-rav4.jpg"),
]


if __name__ == "__main__":
    print(f"=== Acquiring {len(TARGETS)} target images via Tier 2 Wikimedia ===\n")
    ok = 0
    fail = 0
    for title, out_name in TARGETS:
        if fetch_commons(title, out_name):
            ok += 1
        else:
            fail += 1
    print(f"\n=== Done: OK={ok}, FAIL={fail} ===")
