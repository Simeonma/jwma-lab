"""subset_heading_font.py — Regenerate the CJK serif subset used by page headings.

Usage:  py scripts/subset_heading_font.py   (run from repo root, needs fonttools+brotli)

It collects every CJK character that appears inside heading markup
(<h1>..<h5>, TITLE=, plus _template.html nav) across pages/*.py, then
subsets Noto Serif SC (600/700) down to just those characters + CJK
punctuation, writing fonts/NotoSerifSC-sub-{600,700}.woff2.

Re-run this after adding new Chinese heading text, then commit the
regenerated .woff2 files.
"""
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
FONTS = ROOT / "fonts"
SUBSETS = {
    600: "https://cdn.jsdelivr.net/fontsource/fonts/noto-serif-sc@latest/chinese-simplified-600-normal.woff2",
    700: "https://cdn.jsdelivr.net/fontsource/fonts/noto-serif-sc@latest/chinese-simplified-700-normal.woff2",
}

CJK_RANGE = (
    "\u2e80-\u2eff\u3000-\u303f\u31c0-\u31ef\u3200-\u32ff\u3400-\u4dbf"
    "\u4e00-\u9fff\uf900-\ufaff\ufe30-\ufe4f\uff00-\uffef"
)
CJK_RE = re.compile(f"[{CJK_RANGE}]")


def collect_heading_text() -> str:
    parts = []
    for page in sorted((ROOT / "pages").glob("*.py")):
        text = page.read_text(encoding="utf-8")
        for line in text.splitlines():
            # heading markup lines + page TITLE dict
            if re.search(r"<h[1-5]\b", line) or line.startswith("TITLE"):
                parts.append(line)
    template = (ROOT / "_template.html").read_text(encoding="utf-8")
    # nav + footer live in the template; grab the whole file to be safe
    parts.append(template)
    return "\n".join(parts)


def main() -> None:
    text = collect_heading_text()
    chars = sorted(set(CJK_RE.findall(text)))
    # safety margin: ASCII-adjacent punctuation + fullwidth forms already
    # covered by the CJK range; add a few extras commonly typed in titles
    chars.extend("、·—…！？；：（）“”‘’《》")
    unique = "".join(sorted(set(chars) - {"\n"}))
    print(f"{len(unique)} unique CJK chars collected")

    txt = FONTS / "heading-chars.txt"
    txt.write_text(unique, encoding="utf-8")

    for weight, url in SUBSETS.items():
        src = FONTS / f"_src-notoserifsc-{weight}.woff2"
        if not src.exists() or src.stat().st_size < 1_000_000:
            print(f"downloading source font (weight {weight})...")
            urllib.request.urlretrieve(url, src)
        out = FONTS / f"NotoSerifSC-sub-{weight}.woff2"
        import subprocess as sp
        import sys
        r = sp.run(
            [sys.executable, "-m", "fontTools.subset", str(src),
             f"--text-file={txt}", "--flavor=woff2", f"--output-file={out}",
             "--layout-features=*", "--no-hinting", "--desubroutinize"],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            raise SystemExit(r.stderr)
        print(f"OK  {out.name}  {out.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
