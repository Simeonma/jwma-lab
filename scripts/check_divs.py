import re
from pathlib import Path

for f in sorted(Path("pages").glob("*.py")):
    text = f.read_text(encoding="utf-8")
    m = re.search(r'BODY = """(.*?)"""', text, re.S)
    if not m:
        continue
    body = m.group(1)
    # strip the CSS string to avoid counting divs inside CSS text
    opens = len(re.findall(r"<div\b", body))
    closes = len(re.findall(r"</div>", body))
    status = "OK" if opens == closes else "<<< MISMATCH"
    print(f.name, "open:", opens, "close:", closes, status)
