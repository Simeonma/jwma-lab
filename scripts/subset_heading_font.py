"""subset_heading_font.py — Regenerate the self-hosted CJK font subsets.

Usage:  py scripts/subset_heading_font.py   (run from repo root, needs fonttools+brotli)

Two subsets are generated from fontsource full files:

1. Serif headings  (fonts/NotoSerifSC-sub-{600,700}.woff2)
   Chars: CJK found in heading markup (<h1>..<h5>, TITLE=, _template.html).
2. Sans body       (fonts/NotoSansSC-sub-{400,500,700}.woff2)
   Chars: every CJK character used anywhere on the site (pages + template).

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
HEADING_RE = re.compile(r"<h[1-5]\b")

JOBS = [
    # (family, source-url-template, weights, char-collection mode, out-prefix)
    ("serif", "https://cdn.jsdelivr.net/fontsource/fonts/noto-serif-sc@latest/chinese-simplified-{w}-normal.woff2",
     [600, 700], "headings", "NotoSerifSC-sub"),
    ("sans", "https://cdn.jsdelivr.net/fontsource/fonts/noto-sans-sc@latest/chinese-simplified-{w}-normal.woff2",
     [400, 500, 700], "all", "NotoSansSC-sub"),
]


def page_texts() -> str:
    parts = [p.read_text(encoding="utf-8") for p in sorted((ROOT / "pages").glob("*.py"))]
    parts.append((ROOT / "_template.html").read_text(encoding="utf-8"))
    return "\n".join(parts)


def chars_for(mode: str, everything: str) -> str:
    if mode == "all":
        chars = set(CJK_RE.findall(everything))
    else:  # headings only
        chars = set()
        for line in everything.splitlines():
            if HEADING_RE.search(line) or line.startswith("TITLE"):
                chars.update(CJK_RE.findall(line))
    # punctuation safety margin
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
    everything = page_texts()
    for family, url_tpl, weights, mode, prefix in JOBS:
        chars = chars_for(mode, everything)
        chars_file = FONTS / f"{'heading' if mode == 'headings' else 'body'}-chars.txt"
        chars_file.write_text(chars, encoding="utf-8")
        print(f"{family}: {len(chars)} chars")
        for w in weights:
            src = FONTS / f"_src-{family}-{w}.woff2"
            download(url_tpl.format(w=w), src)
            subset(src, chars_file, FONTS / f"{prefix}-{w}.woff2")


if __name__ == "__main__":
    main()
