# 合规审计记录

审计对象：

- `广州商学院本科毕业论文（设计）撰写基本规范.doc`
- `【2026届】现代信息产业学院毕业论文（设计）撰写模板.pdf`
- `广州商学院毕业设计（论文）质量标准（试用）.xlsx`

当前结论：

- 源代码结构和关键格式规则已经按学校文件做了静态对齐。
- 仓库提供结构检查、环境检查和 PDF 编译脚本，用于每次改动后重新验证。
- 因不同学院当年通知、导师要求和用户填写内容可能变化，不能仅凭源码声称“完全满足学校要求”；正式提交前仍需要编译 PDF 后逐页视觉验收。

## 已静态对齐的要求

| 学校要求 | 当前实现 |
|---|---|
| A4 纵向打印 | `styles/gcc-thesis.sty` 使用 `a4paper` |
| 页边距上 2.5 cm、下 2.5 cm、左 2 cm、右 2 cm、左装订线 0.5 cm | `geometry` 已设置 |
| 中文宋体，英文 Times New Roman | `fontspec` / `xeCJK` 已设置，并提供 fallback |
| 正文小四、1.25 倍行距、首行缩进 2 字符 | `\zihao{-4}`、`\setstretch{1.25}`、`\parindent=2em` |
| 封面不显示页眉页码 | `\gccMakeCover` 使用 `\thispagestyle{empty}` |
| 封面右上角论文编号和横线 | `\gccPaperNoLine` |
| 原创性声明和版权授权页无页眉页码 | `extraTex/front/statement.tex` 使用 `\thispagestyle{empty}` |
| 封面后、声明后、单页目录后按模板补空白页 | `\gccMaybeBlankPage`、`\gccClearToRecto` |
| 摘要页开始有页眉，页眉为论文题目，右侧学校 Logo，下划线 | `gcc-front` / `gcc-main` 页眉样式 |
| 摘要、英文摘要、目录罗马页码，从 I 开始 | `main.tex` 中 `\pagenumbering{Roman}` |
| 目录本身进入目录条目 | `\gccTableOfContents` 写入 `目录` |
| 正文阿拉伯页码，从 1 开始 | `main.tex` 中 `\pagenumbering{arabic}` |
| 摘要/Abstract 标题小二黑体居中 | `\gccFrontHeading` |
| 章节编号 `1`、`1.1`、`1.1.1`，默认 5 章结构 | `ctexset`、`secnumdepth`、`extraTex/body/chapter-05.tex` |
| 一级标题四号加粗居中，二/三级标题小四加粗顶格 | `gccChapterFont`、`gccSectionFont` |
| 图题在图下方，表题在表上方 | `caption` 设置 |
| 图、表、公式按章编号 | `\thefigure`、`\thetable`、`\theequation` |
| 参考文献 GB/T 7714-2015 顺序编码制 | `biblatex` 使用 `style=gb7714-2015`、`sorting=none` |
| 致谢单独成页 | `main.tex` 在致谢前 `\clearpage` |
| 后置目录只列 `附录`、`参考文献`、`致谢` 一级条目 | `extraTex/back/appendix.tex` 不把 `附录 A` 写入目录 |
| 可选附件材料册 | `attachments.tex` 和 `extraTex/attachments/` 保留可选入口，默认正文流程不包含评分表 |

## 需要 PDF 视觉验收的项目

这些项目不能仅靠源码确认，必须编译后逐页看：

- 封面字段位置、横线长度、题目两行位置是否贴近学校模板。
- 页眉右侧 Logo 尺寸、位置是否与 Word/PDF 模板一致。
- 页眉横线和正文版心是否有偏移。
- 摘要、目录、正文首页的页码位置和字体观感。
- 目录点线、标题缩进、长标题换行。
- 表格是否跨页或文字是否溢出。
- 如果用户明确启用附件材料册，再检查附件表格高度是否足够、是否出现压线或换页异常。

## 规范冲突与当前取舍

学校《撰写基本规范》和 2026 届现代信息产业学院模板存在少量口径不完全一致：

- `附录` 顺序：基本规范列在致谢后；2026 届撰写模板明确说明“正文后、参考文献前设立附录”。当前模板优先按 2026 届学院模板放在参考文献前。
- `关键词` 缩进：基本规范写“首行空两格”；2026 届撰写模板批注写“关键词：顶格”。当前模板优先按 2026 届学院模板顶格。
- `页码字体`：摘要页批注写罗马页码 Times New Roman 五号；基本规范写页码五号黑体加粗。当前模板拆分为前置页 Times New Roman 五号，正文页黑体五号加粗。

## 当前缺口

- 每次替换真实论文内容后，都需要重新生成 `main.pdf`。
- 需要按学院当年通知、导师意见和教务系统要求复核封面、正文结构和日期字段。
- 正式提交前仍建议做 WPS/Word/PDF 视觉对照。

## 下一步验收命令

```bash
python3 scripts/check_structure.py
python3 scripts/doctor.py
bash scripts/build.sh clean
bash scripts/build.sh main
```

如果编译成功，应打开 `main.pdf`，按本文件“需要 PDF 视觉验收的项目”逐项检查。
