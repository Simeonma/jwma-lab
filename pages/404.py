TITLE = {"en": "Page Not Found - MacroPhotonic Lab", "cn": "页面未找到 - MacroPhotonic Lab"}
NAV_ACTIVE = "404"

CSS = """
        .notfound {
            max-width: 720px;
            margin: 96px auto;
            padding: 0 24px;
            text-align: center;
        }

        .notfound .code {
            font-size: 88px;
            font-weight: 700;
            color: #1E3A8A;
            line-height: 1;
            margin-bottom: 12px;
        }

        .notfound p {
            font-size: 17px;
            color: #4B5563;
            margin-bottom: 28px;
        }

        .notfound a {
            display: inline-block;
            padding: 12px 28px;
            background: #1E3A8A;
            color: #ffffff;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            transition: background 0.2s;
        }

        .notfound a:hover {
            background: #3B82F6;
        }
"""

BODY = """
    <div class="notfound">
        <div class="code">404</div>
        <p id="nf-text-en">The page you are looking for does not exist or has been moved.</p>
        <p id="nf-text-cn" style="display: none;">您访问的页面不存在或已被移动。</p>
        <a href="index.html" id="nf-home-en">Back to Home</a>
        <a href="index.html" id="nf-home-cn" style="display: none;">返回首页</a>
    </div>
"""

SCRIPT = ""
