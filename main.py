"""Write the one-line entry to the output directory."""
import os
from pathlib import Path

# 179 characters, limit 200, one line.
LINE = 'By accepting these terms, you agree your smart toaster may, at its sole discretion, withhold breakfast until you have read the full 47-page privacy policy aloud, in a funny voice.'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
# Second pass: verified the line reads cleanly on its own, no setup needed.
