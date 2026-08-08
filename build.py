"""build.py — Assemble MacroPhotonic Lab website from template + page content.

Usage:  python build.py   (run from this directory)
Source: _template.html, pages/*.py, common.css, common.js (this directory)
Output: *.html written into this directory
"""

from pathlib import Path

ROOT = Path(__file__).parent
TEMPLATE = (ROOT / "_template.html").read_text(encoding="utf-8")
OUTPUT = ROOT
PAGES_DIR = ROOT / "pages"

PAGE_FILES = {
    "home": "index.html",
    "people": "people.html",
    "research": "research.html",
    "publications": "publications.html",
    "facilities": "facilities.html",
    "openings": "openings.html",
    "contact": "contact.html",
}


def build():
    OUTPUT.mkdir(parents=True, exist_ok=True)

    for name, filename in PAGE_FILES.items():
        mod = {}
        page_path = PAGES_DIR / f"{name}.py"
        exec(page_path.read_text(encoding="utf-8"), mod)

        # Nav active classes
        nav = {f"nav_{p}": "" for p in PAGE_FILES}
        nav[f"nav_{mod['NAV_ACTIVE']}"] = "active"

        # Only emit a <script> block when the page has inline script
        page_script = mod.get("SCRIPT", "").strip()
        script_block = (
            f"    <script>\n{page_script}\n    </script>" if page_script else ""
        )

        html = TEMPLATE.format(
            title=mod["TITLE"]["en"],
            cn_title=mod["TITLE"]["cn"],
            page_url=(
                "https://www.jwma-lab.com/"
                if filename == "index.html"
                else f"https://www.jwma-lab.com/{filename}"
            ),
            head_extra=mod.get("HEAD_EXTRA", ""),
            css=mod.get("CSS", ""),
            body=mod.get("BODY", ""),
            script_block=script_block,
            **nav,
        )

        out = OUTPUT / filename
        out.write_text(html, encoding="utf-8")
        print(f"  OK  {filename}")

    print(f"\nDone!  Output: {OUTPUT}")


if __name__ == "__main__":
    build()
