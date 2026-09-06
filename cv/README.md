# 中英文 LaTeX 简历

这里是网站及个人简历 PDF 的源文件，以 2026-09-06 核对后的新版内容为基础。
直接编辑 `.tex` 即可，无需先编辑 Python 或从 PDF 反向转换。

## 文件分工

| 文件 | 修改内容 |
| --- | --- |
| `CV_zh.tex` | 中文正文：教育、科研、实习、项目、技能、奖项 |
| `CV_en.tex` | 英文正文：与中文对应的经历和表述 |
| `profile.tex` | 两份共用的联系方式、头像路径和内容核对日期 |
| `publication.tex` | 两份共用的论文标题、完整作者顺序、期刊与 DOI |
| `cv-style.sty` | 字体、颜色、页边距、章节、经历条目和页脚 |
| `assets/portrait.jpg` | 从网站头像缩小生成的打印用照片 |
| `fonts/` | 可随项目分发的中文字体、许可证和来源说明 |

修改经历时同步编辑两种语言。`profile.tex` 中的日期是**内容核对日期**，
不会随每次编译自动变化，确认信息后再更新。

## 编译

推荐 Tectonic；也支持 `latexmk -xelatex` 或 `xelatex`。
Tectonic 首次编译可能联网下载 TeX 宏包和字体，之后使用本地缓存。
样式使用 TeX 分发的 TeX Gyre Heros，以及工程内附带的开源 Noto Sans SC 中文字体，无需 macOS 专有字体。
中文字体含完整字符集，来源和许可证见 `fonts/README.md` 与 `fonts/OFL.txt`。

从项目根目录执行：

```sh
python3 scripts/build_cv.py
```

输出：`output/pdf/CV_en.pdf`、`output/pdf/CV_zh.pdf`，日志也在该目录。
Python 脚本仅使用标准库调度 LaTeX 编译器。
它会在编译失败、日志出现缺字或溢出警告时停止，并且在所有指定语言编译成功后才同步文件。

只编译一种语言，或指定编译器：

```sh
python3 scripts/build_cv.py --lang zh
python3 scripts/build_cv.py --engine tectonic
```

检查 PDF 排版后更新网站下载文件：

```sh
python3 scripts/build_cv.py --sync
```

需要同时更新其他目录时，显式指定目标目录：

```sh
python3 scripts/build_cv.py --sync --copy-to "$HOME/personal/CV"
```

`--sync` 更新本地 `data/`，并按每份 PDF 的 SHA-256 内容哈希刷新主页链接的
`?v=...` 参数，避免同名 PDF 的旧缓存。不会提交、推送或发布网站。
也可在任何工作目录通过脚本的绝对路径执行，源文件及输出路径会自动定位。

若 PDF 已经是最新版，仅需修复链接版本，可运行：

```sh
python3 scripts/build_cv.py --refresh-links
```

## 直接使用 LaTeX 编辑器 / Overleaf

将本目录内的文件、`assets/` 及 `fonts/` 上传到同一工程中，选择 **XeLaTeX**，
主文档选 `CV_zh.tex` 或 `CV_en.tex`。不要选择 pdfLaTeX。
无需上传旧简历工程或 Python 脚本。本轮实际验证了本地 Tectonic 编译，
未在 Overleaf 上实测。

也可在本目录直接执行：

```sh
tectonic CV_zh.tex
tectonic CV_en.tex
```

此时 PDF 输出在本目录，不会自动替换网站文件。

## 新增经历

```tex
\begin{cventry}{经历标题}{日期}{机构与角色}
\begin{cvitems}
\item 描述本人实际工作与可核实成果。
\item 另一项工作；百分号写为 98\%，英文与号写为 \&。
\end{cvitems}
\end{cventry}
```

当前主动在实习经历前使用 `\newpage`，保持两页结构。
条目会整体排版；新增较多内容后应检查两页是否仍合适。

本工程不依赖旧简历模板、专有字体或 Downloads 中的原目录。
