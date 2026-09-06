# Yun Hong · 个人主页与简历

[个人主页](https://16yunh.github.io/)的源代码，以及可持续维护的中英文 LaTeX 简历。
网站为静态 HTML/CSS，无需 Node.js 或前端构建步骤。

## 目录

| 路径 | 用途 |
| --- | --- |
| `index.html` | 主页内容与搜索/分享元数据 |
| `stylesheet.css` | 桌面与手机端样式 |
| `images/` | 网站头像与图标 |
| `data/CV_en.pdf`、`data/CV_zh.pdf` | 网站提供下载的正式简历，纳入 Git |
| [`cv/`](cv/README.md) | 中英文 LaTeX 正文、共享样式、个人信息、论文信息及字体，纳入 Git |
| `scripts/build_cv.py` | 调用 Tectonic / XeLaTeX 编译并按需同步 PDF |
| `output/` | 本地构建文件与日志，不纳入 Git |
| `robots.txt`、`sitemap.xml`、`.nojekyll` | 搜索索引与静态托管配置 |

## 更新简历

编辑 `cv/CV_zh.tex` 和 `cv/CV_en.tex`；共用联系方式与内容核对日期在
`cv/profile.tex`，论文书目信息在 `cv/publication.tex`。
每次修改研究、教育、实习、项目或奖项等个人信息，必须同步更新
`index.html`、`cv/CV_zh.tex` 与 `cv/CV_en.tex`，并重新生成两份正式 PDF。
维护约定记录在 [`AGENTS.md`](AGENTS.md)。

安装 Tectonic，或包含 XeLaTeX 的 TeX 发行版后，在仓库根目录编译：

```sh
python3 scripts/build_cv.py
```

检查 `output/pdf/` 下两份 PDF 的文字、分页和链接，然后同步正式下载文件：

```sh
python3 scripts/build_cv.py --sync
```

`--sync` 同时更新主页简历链接的内容哈希版本参数，防止浏览器继续使用旧 PDF 缓存。
该命令只更新本地文件，不会提交或推送。字体、编辑器配置、单语言编译等
详细说明见 [`cv/README.md`](cv/README.md)。

## 本地预览与发布

在仓库根目录启动静态服务器：

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

打开 `http://127.0.0.1:8000/`，检查桌面/手机布局及两份简历下载。
内容更新时同步修改主页页脚与 `sitemap.xml` 的更新时间。

检查变更后，将网站、LaTeX 源文件和更新后的 `data/` PDF 一起提交并推送到
`master`。GitHub Pages 从该分支的仓库根目录发布，推送后应检查部署结果与线上页面。

`.gitignore` 仅排除生成文件和本机设置，不排除 LaTeX 源文件、字体或正式下载 PDF。

修改下载或同步流程后，运行缓存回归检查：

```sh
python3 -m unittest discover -s tests -v
```

## 来源

网站模板改编自 [Jon Barron 的主页](https://github.com/jonbarron/jonbarron_website)。
中文字体来源与许可证见 [`cv/fonts/`](cv/fonts/README.md)。
