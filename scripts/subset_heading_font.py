"""subset_heading_font.py — Regenerate the self-hosted CJK serif subset (whole site).

Usage:  py scripts/subset_heading_font.py   (run from repo root, needs fonttools+brotli)

The entire site uses one typeface pair: Source Serif 4 (Latin) +
Noto Serif SC (Chinese). This script subsets Noto Serif SC to exactly
the CJK characters used anywhere on the site (pages + template),
for weights 400/500/600/700, writing fonts/NotoSerifSC-sub-*.woff2.

Re-run after adding new Chinese text, then commit the regenerated
fonts/*.woff2 files (source caches fonts/_src-* are gitignored).
"""
import re
import subprocess as sp
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
FONTS = ROOT / "fonts"

CJK_RANGE = (
    "\u2e80-\u2eff\u3000-\u303f\u31c0-\u31ef\u3200-\u32ff\u3400-\u4dbf"
    "\u4e00-\u9fff\uf900-\ufaff\ufe30-\ufe4f\uff00-\uffef"
)
CJK_RE = re.compile(f"[{CJK_RANGE}]")
WEIGHTS = [400, 500, 600, 700]
URL = "https://cdn.jsdelivr.net/fontsource/fonts/noto-serif-sc@latest/chinese-simplified-{w}-normal.woff2"


def collect_chars() -> str:
    parts = [p.read_text(encoding="utf-8") for p in sorted((ROOT / "pages").glob("*.py"))]
    parts.append((ROOT / "_template.html").read_text(encoding="utf-8"))
    chars = set(CJK_RE.findall("\n".join(parts)))
    chars.update("、·—…！？；：（）“”‘’《》〈〉【】％℃")
    return "".join(sorted(c for c in chars if c != "\n"))


def download(url: str, dest: Path) -> None:
    if dest.exists() and dest.stat().st_size > 1_000_000:
        return
    print(f"  downloading {url.rsplit('/', 1)[-1]} ...")
    urllib.request.urlretrieve(url, dest)


def subset(src: Path, chars_file: Path, out: Path) -> None:
    r = sp.run(
        [sys.executable, "-m", "fontTools.subset", str(src),
         f"--text-file={chars_file}", "--flavor=woff2", f"--output-file={out}",
         "--layout-features=*", "--no-hinting", "--desubroutinize"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        raise SystemExit(r.stderr)
    print(f"  OK  {out.name}  {out.stat().st_size / 1024:.0f} KB")


def main() -> None:
    chars = collect_chars()
    chars_file = FONTS / "all-chars.txt"
    chars_file.write_text(chars, encoding="utf-8")
    print(f"{len(chars)} unique CJK chars collected")
    for w in WEIGHTS:
        src = FONTS / f"_src-serif-{w}.woff2"
        download(URL.format(w=w), src)
        subset(src, chars_file, FONTS / f"NotoSerifSC-sub-{w}.woff2")


if __name__ == "__main__":
    main()
