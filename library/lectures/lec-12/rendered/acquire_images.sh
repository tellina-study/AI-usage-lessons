#!/bin/bash
# Acquire real images for lec-12 via Wikimedia Commons (Tier 2).
# Per CLAUDE.md no-mock-fallbacks rule.

set -e
UA="-A Mozilla/5.0 (lec-12 educational research; kzlevko@gmail.com)"
DEST=/tmp/lec-12-wt/library/lectures/lec-12/rendered/assets/screenshots
cd "$DEST"

# Helper: get direct image URL from Commons API, then download
fetch_commons() {
    local TITLE="$1"
    local OUT="$2"
    local WIDTH="${3:-1280}"
    local API_URL="https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url&iiurlwidth=${WIDTH}&titles=File:${TITLE}"
    local URL=$(curl -sL $UA "$API_URL" | python3 -c "import json,sys; d=json.load(sys.stdin); pages=list(d['query']['pages'].values()); ii=pages[0].get('imageinfo'); print(ii[0]['thumburl'] if ii else '')")
    if [ -n "$URL" ]; then
        curl -sL $UA "$URL" -o "$OUT"
        echo "OK: $OUT ($(stat -c%s "$OUT" 2>/dev/null || echo 0) bytes) from $TITLE"
    else
        echo "FAIL: $TITLE (no imageinfo)"
    fi
}

echo "=== Acquiring real images for lec-12 ==="

# s01 HERO: Hannover Messe / industrial AI scene → AGV Siemens trade show or robot at expo
fetch_commons "AGV-Siemens_ANS.jpg" "s01-agv-siemens.jpg"
fetch_commons "Flexiv_Hannover_Messe.jpg" "s01-flexiv-hannover.jpg"

# s07: Siemens (digital twin composer logo / Siemens HQ)
fetch_commons "Siemens-logo.svg" "s07-siemens-logo.png" 800
fetch_commons "Siemens_HQ_Munich_2017.jpg" "s07-siemens-hq.jpg"

# s09: Port (Singapore is canonical container port photo)
fetch_commons "Port_of_Singapore.jpg" "s09-port-singapore.jpg"
fetch_commons "Singapore_Port_Coast.jpg" "s09-port-singapore-coast.jpg"

# s10: Vision QC / inspection — Industry 4.0 / factory photo
fetch_commons "Industry_4.0.png" "s10-industry40.png"
fetch_commons "Robot_at_BMW_Factory.jpg" "s10-bmw-robot.jpg"

# s12: PdM — cement / chemical plant
fetch_commons "Heidelberg_Cement_AG_-_Cement_Manufacturing_Plant.jpg" "s12-cement-plant.jpg"
fetch_commons "Cement_plant_in_Pomorzany.jpg" "s12-cement-pomorzany.jpg"

# s15: MES — PLC / industrial control
fetch_commons "SCADA_screen.jpg" "s15-scada.jpg"
fetch_commons "Modicon_Quantum.jpg" "s15-plc.jpg"

# s16: PLC Copilot context — code editor / IDE
fetch_commons "Ladder_diagram_example.png" "s16-ladder.png"

# s20: Yokogawa Chemical / distillation column
fetch_commons "Yokogawa_Headquarters_Musashino.jpg" "s20-yokogawa.jpg"
fetch_commons "Distillation_columns.jpg" "s20-distill.jpg"

# s22: Omniverse / Composer hero — NVIDIA HQ or data center
fetch_commons "Nvidia_headquarters.jpg" "s22-nvidia-hq.jpg"
fetch_commons "NVIDIA_Voyager_HQ.jpg" "s22-nvidia-voyager.jpg"

# s23a: Toyota Digit — humanoid robot
fetch_commons "Toyota_Motor_Manufacturing_Kentucky_assembly_line.jpg" "s23a-toyota-line.jpg"
fetch_commons "Toyota_assembly_line.jpg" "s23a-toyota.jpg"
fetch_commons "BMW_Plant_Leipzig.jpg" "s23a-bmw-leipzig.jpg"

# s25: §5 intro hero — Port (different angle than s09)
fetch_commons "Singapore_Port.jpg" "s25-singapore.jpg"
fetch_commons "Container_Port.jpg" "s25-container-port.jpg"

# s33: WEF / Lighthouse
fetch_commons "World_Economic_Forum_logo.svg" "s33-wef-logo.png" 800

# s35: КАМАЗ / Норникель
fetch_commons "KamAZ-65801.jpg" "s35-kamaz.jpg"
fetch_commons "Norilsk_Nickel.jpg" "s35-nornickel.jpg"
fetch_commons "Bystrinsky_GOK.jpg" "s35-bystrinsky.jpg"

# s39 HERO closing: Toyota Digit RAV4 line / Agility Robotics
fetch_commons "Digit_Agility_Robotics.jpg" "s39-digit.jpg"
fetch_commons "Toyota_RAV4_assembly.jpg" "s39-rav4.jpg"
fetch_commons "Agility_Robotics_Digit.jpg" "s39-digit2.jpg"

echo "=== Done ==="
ls -la "$DEST" | sort -k5 -n -r | head -30
