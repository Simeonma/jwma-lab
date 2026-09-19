import json
import re
from pathlib import Path

TITLE = {"en": "Publications - MacroPhotonic Lab", "cn": "发表论文 - MacroPhotonic Lab"}
NAV_ACTIVE = "publications"

CSS = """
        .title-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 16px;
            padding-bottom: 16px;
            border-bottom: 2px solid #E2E8F0;
        }

        .pub-note {
            font-size: 14px;
            color: #64748B;
            margin-bottom: 32px;
        }

        .card h3 {
            font-size: 28px;
            color: #1E3A8A;
        }

        .scholar-button {
            padding: 8px 16px;
            background: #1E3A8A;
            color: white;
            border-radius: 8px;
            text-decoration: none;
            font-size: 16px;
            font-weight: 500;
            white-space: nowrap;
            transition: all 0.2s ease;
        }

        .scholar-button:hover {
            opacity: 0.9;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(30, 58, 138, 0.15);
        }

        .year-timeline {
            position: relative;
            padding-left: 48px;
            margin-bottom: 16px;
        }

        .year-timeline::before {
            content: '';
            position: absolute;
            left: 12px;
            top: 0;
            bottom: 0;
            width: 2px;
            background-color: #E2E8F0;
            z-index: 1;
        }

        .year {
            font-size: 22px;
            font-weight: 600;
            color: #1E3A8A;
            margin-bottom: 24px;
            position: relative;
            padding-left: 16px;
            display: inline-block;
            cursor: pointer;
            user-select: none;
        }

        .year::before {
            content: '';
            position: absolute;
            left: -40px;
            top: 50%;
            transform: translateY(-50%);
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background-color: #3B82F6;
            border: 4px solid #F8FAFC;
            box-shadow: 0 0 0 2px #3B82F6;
            z-index: 2;
            transition: transform 0.2s ease;
        }

        .year:hover::before {
            transform: translateY(-50%) scale(1.2);
        }

        .year::after {
            content: ' \\25B2';
            font-size: 14px;
            opacity: 0.6;
        }

        .year.collapsed::after {
            content: ' \\25BC';
        }

        .year-group {
            margin-bottom: 60px;
        }

        .year-group.collapsed .pub-item,
        .year-group.collapsed .year-timeline::before {
            display: none;
        }

        .year-group.collapsed .year-timeline {
            margin-bottom: 0;
        }

        .year-group.collapsed {
            margin-bottom: 24px;
        }

        .pub-item {
            margin-bottom: 20px;
            padding-bottom: 20px;
            border-bottom: 1px solid #E2E8F0;
            position: relative;
            padding-left: 8px;
        }

        .pub-item.has-img {
            display: flex;
            flex-direction: column;
            gap: 16px;
            align-items: center;
        }

        .pub-img-container {
            position: relative;
            width: 80%;
            max-width: 80%;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(30, 58, 138, 0.08);
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .pub-img {
            width: 100%;
            height: auto;
            display: block;
            transition: transform 0.35s ease;
        }

        .pub-img-container:hover .pub-img {
            transform: scale(1.02);
        }

        .pub-desc {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: auto;
            max-height: 80%;
            background: rgba(0, 0, 0, 0.8);
            color: #ffffff;
            padding: 20px 24px;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            display: block !important;
            white-space: normal !important;
            overflow-wrap: break-word !important;
            line-height: 1.6;
            font-size: 16px;
            overflow-y: auto;
            flex: none !important;
            align-items: normal !important;
            pointer-events: none;
        }

        .pub-desc a {
            color: #93C5FD;
            font-weight: 500;
            text-decoration: none;
            display: inline !important;
            white-space: normal !important;
            word-break: break-word !important;
            pointer-events: auto;
        }

        .pub-desc a:hover {
            text-decoration: underline;
        }

        .pub-img-container:hover .pub-desc {
            opacity: 1;
            visibility: visible;
        }

        .pub-img-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(30, 58, 138, 0.12);
        }

        /* Click-to-toggle state for mobile */
        .pub-img-container.show-desc .pub-desc {
            opacity: 1;
            visibility: visible;
        }

        .pub-item.no-img {
            display: block;
        }

        .pub-content {
            flex: 1;
            width: 100%;
        }

        .pub-title {
            font-size: 20px;
            font-weight: 600;
            color: #1E3A8A;
            margin-bottom: 5px;
            line-height: 1.5;
        }

        .pub-title a {
            color: #1E3A8A;
            text-decoration: none;
            transition: all 0.2s ease;
        }

        .pub-title a:hover {
            color: #3B82F6;
            text-decoration: underline;
        }

        .pub-authors {
            font-size: 16px;
            color: #4B5563;
            margin-bottom: 5px;
            line-height: 1.5;
        }

        .pub-journal {
            font-size: 16px;
            font-style: italic;
            font-weight: 600;
            color: #1F2937;
            margin-bottom: 5px;
            display: inline;
            margin-left: 0px;
        }

        @media (max-width: 768px) {
            .card h3 { font-size: 24px; }
            .year-timeline { padding-left: 40px; }
            .year::before { left: -34px; width: 12px; height: 12px; }
            .pub-img-container { width: 90%; max-width: 90%; }
            .pub-desc { font-size: 15px; padding: 16px 20px; max-height: 90%; }
            .pub-title { font-size: 18px; }
        }

        @media (max-width: 600px) {
            .title-row { flex-direction: column; align-items: flex-start; gap: 12px; }
            .year-timeline { padding-left: 34px; }
            .year::before { left: -29px; width: 10px; height: 10px; }
            .pub-img-container { width: 95%; max-width: 95%; }
            .pub-desc { font-size: 14px; padding: 12px 16px; max-height: 90%; }
        }

        @media (max-width: 375px) {
            .pub-title { font-size: 17px; }
            .pub-authors { font-size: 15px; }
            .year-timeline { padding-left: 30px; }
            .year::before { left: -26px; }
        }
"""

DATA_FILE = Path(__file__).parent / "pubs_data.json"
_DATA = json.loads(DATA_FILE.read_text(encoding="utf-8"))


def _authors_html(authors_md):
    """md 作者行 -> HTML：**粗体**→<strong>，$^*$→*，通讯†→&dagger;，逗号→分号"""
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", authors_md)
    s = s.replace("$^*$", "*").replace("$^\\dagger$", "&dagger;")
    s = s.replace(", ", "; ")
    return s.rstrip(".") + "."


def _render_publications():
    years = {}
    for p in _DATA:
        years.setdefault(p["year"], []).append(p)

    groups = []
    for year in sorted(years, reverse=True):
        items = []
        for p in years[year]:
            img = ""
            if p.get("image"):
                img = (
                    f'<div class="pub-img-container" onclick="togglePubDesc(this)">'
                    f'<img src="{p["image"]}" alt="{p["image_alt"]}" loading="lazy" class="pub-img">'
                    f'<div class="pub-desc">{p.get("desc_html") or ""}</div>'
                    f"</div>"
                )
            if p.get("doi"):
                title = f'<a href="https://doi.org/{p["doi"]}" target="_blank">{p["title"]}</a>'
            else:
                title = p["title"]
            journal = f'<span class="pub-journal">{p["journal_name"]}</span>'
            if p.get("journal_rest"):
                journal += ", " + p["journal_rest"]
            journal += f' ({p["year"]})'
            if p.get("notes"):
                journal += " [" + p["notes"] + "]"
            cls = "pub-item has-img" if p.get("image") else "pub-item no-img"
            items.append(
                f'''                    <div class="{cls}">
                        {img}
                        <div class="pub-content">
                            <div class="pub-title">{title}</div>
                            <div class="pub-authors">
                                {_authors_html(p["authors_md"])}
                                {journal}
                            </div>
                        </div>
                    </div>'''
            )
        groups.append(
            f'''                <div class="year-group">
                    <div class="year-timeline">
                        <div class="year" onclick="toggleYear(this)">{year}</div>
{chr(10).join(items)}
                    </div>
                </div>'''
        )
    return "\n".join(groups)


BODY = f"""
    <div class="container">
        <div class="card">
            <div class="title-row">
                <h3 id="pub-title-en">Selected Publications</h3>
                <h3 id="pub-title-cn" style="display: none;">发表论文</h3>
                <a href="https://scholar.google.com/citations?user=-2sAiXwAAAAJ&hl=en" class="scholar-button" target="_blank">
                    <span id="scholar-btn-en">Full Publications in Google Scholar</span>
                    <span id="scholar-btn-cn" style="display: none;">在 Google Scholar 查看全部论文</span>
                </a>
            </div>

            <p class="pub-note" id="pub-note-en">A selection of representative publications. The complete list is available on Google Scholar.</p>
            <p class="pub-note" id="pub-note-cn" style="display: none;">以下为代表性论文，完整列表请见 Google Scholar。</p>

{_render_publications()}
        </div>
    </div>
"""


SCRIPT = """
        function toggleYear(el) {
            var group = el.closest('.year-group');
            group.classList.toggle('collapsed');
            el.classList.toggle('collapsed');
        }

        function togglePubDesc(el) {
            el.classList.toggle('show-desc');
        }
"""
