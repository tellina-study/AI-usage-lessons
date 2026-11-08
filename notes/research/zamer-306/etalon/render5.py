import sys
from pathlib import Path
REPO = Path("/home/harness/harness-projects/256/.worktrees/folder-288/session-0b2adb13-7ee7af40")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO / "tools" / "presentation-build"))
sys.path.insert(0, str(REPO / "library" / "lectures" / "lec-07" / "rework" / "deck"))
import build_lec07 as b
from deckkit import render as rnd, report

out = HERE / "etalon5.pptx"
report.reset()
n = b.build(only="s13,s05,s50,s12,s27_1", out=out)
print("built", n, "slides ->", out)
rnd.render(out, HERE / "snaps")
