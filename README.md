# MacroPhotonic Lab 网站

南方科技大学 MacroPhotonic Lab 课题组网站（[www.jwma-lab.com](https://www.jwma-lab.com)）的源码与构建产物。

## 目录结构

| 路径 | 说明 |
|------|------|
| `pages/*.py` | **页面源码（唯一编辑入口）**，每页定义 TITLE / NAV_ACTIVE / HEAD_EXTRA / CSS / BODY / SCRIPT |
| `_template.html` | 页面模板（导航栏、页脚、语言切换、公共 meta 标签） |
| `common.css` / `common.js` | 全站样式与语言切换逻辑 |
| `build.py` | 构建脚本：模板 + 页面源码 → 各 .html |
| `*.html` | 构建产物（GitHub Pages 直接发布，**请勿手改**） |
| `images/` `files/` | 图片与文档资源（cv.pdf 等） |
| `sitemap.xml` / `robots.txt` | SEO 配置 |
| `CNAME` | GitHub Pages 自定义域名 |

## 构建

需要 Python 3.10+（本机路径：`D:\Users\Administrator\miniconda3\python.exe`）。

```powershell
cd E:\Sustech Group\Website\jwma-lab-main\jwma-lab
D:\Users\Administrator\miniconda3\python.exe build.py
```

在本目录原地生成 7 个 HTML。

## 发布

```powershell
git add -A
git commit -m "更新说明"
git push origin main
```

推送后 GitHub Pages 会自动更新线上站点。

## 常见维护操作

### 加一条 News（首页）
编辑 `pages/home.py`，在 news-section 里按「最新在上」插入 news-item。中英文各一个 span（id 用 `newsN-en` / `newsN-cn`，cn 版加 `style="display: none;"`）。

### 加一位成员
1. 头像（建议 ≤500KB）放到 `images/members/姓名.jpg`
2. 在 `pages/people.py` 的 members-grid 里插入 member-card（参考现有卡片结构，id 前缀自定，如 `hz-`、`yz-`），元素加 `hover-card` 类

### 加一篇论文
编辑 `pages/publications.py`，在对应年份的 year-group 里加 pub-item：
- 有配图：`has-img` + `pub-img-container`（图片放 `images/publications/`）
- 无配图：`no-img` + `pub-content`

## 双语约定

- 每个需要翻译的元素准备两份：id 以 `-en` / `-cn` 结尾
- cn 版本默认 `style="display: none;"`，由 common.js 切换显示
- 页面 TITLE 字典提供 en / cn：en 用作 HTML title，cn 用于切换浏览器标签页标题（common.js 读取 `cn-title` meta）

## 样式约定

- 页面大标题用 `.page-title`（各页可按需覆盖 margin-bottom），小节标题用 `.section-subtitle`（均定义在 common.css）
- 卡片悬浮特效（顶部渐变条 + 上浮 + 阴影）：给元素加 `hover-card` 类
- 成员头像为圆形居中裁切（`.member-avatar`，196×196），照片中人脸宜居中
