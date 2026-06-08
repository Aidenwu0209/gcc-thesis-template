# 广州商学院本科毕业论文（设计）LaTeX 模板

本项目是一个非官方的广州商学院本科毕业论文（设计）LaTeX 模板，仓库名中的 `gcc` 指 Guangzhou College of Commerce。当前版本优先适配现代信息产业学院 2026 届毕业论文（设计）撰写模板和学校本科毕业论文（设计）撰写基本规范。

## 适配范围

- 学校：广州商学院
- 学院：现代信息产业学院
- 类型：本科毕业论文（设计）
- 重点格式：封面、原创性声明、版权使用授权书、中英文摘要、目录、正文、附录、参考文献、致谢
- 附件材料：任务书、开题报告、进展情况记录表、答辩记录表、评语评分表

本模板不是学校官方发布物。正式提交前，请以学院当年通知、导师意见和教务系统要求为准。

## 快速开始

1. 修改 `extraTex/meta.tex` 中的姓名、学号、学院、专业班级、指导教师、题目、日期和关键词。
2. 修改 `extraTex/front/abstract_zh.tex` 和 `extraTex/front/abstract_en.tex`。
3. 按章节修改 `extraTex/body/` 下的正文。
4. 修改 `extraTex/back/references.bib` 和致谢。
5. 如需附件材料册，修改 `attachments.tex` 和 `extraTex/attachments/` 下的表格内容。
6. 使用 XeLaTeX + Biber 编译。

推荐命令：

```bash
bash scripts/build.sh
```

等价手动命令：

```bash
xelatex -interaction=nonstopmode main.tex
biber main
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode attachments.tex
xelatex -interaction=nonstopmode attachments.tex
```

## 目录结构

```text
.
├── main.tex
├── attachments.tex
├── styles/gcc-thesis.sty
├── extraTex/
│   ├── meta.tex
│   ├── attachments/
│   ├── front/
│   ├── body/
│   └── back/
├── assets/branding/gcc_logo.png
├── docs/format-checklist.md
└── scripts/
```

## 与学校格式的对应关系

- A4 纵向打印，页边距为上 2.5 cm、下 2.5 cm、左 2 cm、右 2 cm、左侧装订线 0.5 cm。
- 正文中文宋体，英文 Times New Roman，小四，1.25 倍行距，首行缩进 2 个汉字。
- 封面、原创性声明和版权使用授权书不显示页眉页码。
- 摘要、英文摘要、目录使用罗马数字页码。
- 正文从第 1 页开始使用阿拉伯数字页码。
- 页眉居中显示论文题目，右侧放广州商学院 Logo。
- 章节编号使用 `1`、`1.1`、`1.1.1`。
- 图、表、公式按章编号。
- 参考文献使用 GB/T 7714-2015 顺序编码制。
- 附件册单独由 `attachments.tex` 生成，包含学校附件模板中的过程材料表。

更详细的核对项见 `docs/format-checklist.md`。

## 空白页设置

学校 Word/PDF 模板为双面打印预留了空白页。本模板默认开启封面后、声明页后的空白页：

```tex
\gccDoubleSidedBlankPagestrue
```

如果只需要单面打印或电子版，可以在 `extraTex/@config.tex` 中改为：

```tex
\gccDoubleSidedBlankPagesfalse
```

## 许可与来源

本项目代码采用 MIT License。

模板工程结构参考了 `huangwb8/ChineseResearchLaTeX` 中的 `thesis-just-bachelor`，该项目同样采用 MIT License。广州商学院校名、Logo 和学校模板文本属于其各自权利方，本仓库仅用于论文排版学习与非官方模板维护。
