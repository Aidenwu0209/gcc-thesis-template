# 广州商学院本科毕业论文（设计）LaTeX 模板

这是一个 **Agent-first / Vibe Writing** 取向的非官方广州商学院本科毕业论文（设计）LaTeX 模板。仓库名中的 `gcc` 指 Guangzhou College of Commerce。

本项目不是只给人手动填空的模板，而是给 Codex、Claude Code、Cursor 等 Agent 使用的工作流脚手架：人提供学校要求、研究内容和最终判断，Agent 负责拆分材料、更新 LaTeX 源文件、安装/检查编译环境、编译 PDF、按格式清单验收并迭代修正。

当前版本优先适配：

- 广州商学院本科毕业论文（设计）撰写基本规范
- 现代信息产业学院 2026 届毕业论文（设计）撰写模板
- 现代信息产业学院毕业论文（设计）论文附件模板
- 广州商学院毕业设计（论文）质量标准（试用）

本模板不是学校官方发布物。正式提交前，请以学院当年通知、导师意见和教务系统要求为准。

## 你应该怎么用

### 方法一（推荐）：让 Agent 自主接管

在 Codex / Claude Code / Cursor 中打开本仓库，然后直接给 Agent 这样的任务：

```text
请使用这个仓库整理我的广州商学院本科毕业论文（设计）。
先阅读 README.md、AGENTS.md、docs/format-checklist.md、main.tex、attachments.tex 和 extraTex/meta.tex。
然后根据我提供的论文题目、学生信息、正文草稿、参考文献和学校要求，更新 meta、摘要、正文、参考文献、致谢和附件材料。
完成后运行 scripts/check_structure.py、scripts/doctor.py，并在环境允许时编译 main.pdf 和 attachments.pdf。
最后按学校格式清单检查封面、声明、摘要、目录、正文首页、参考文献、致谢和附件表格。
```

适合的输入材料：

- 学生姓名、学号、学院、专业班级、指导教师、日期
- 论文题目和中英文关键词
- Word / Markdown / PDF / 截图形式的正文草稿
- 参考文献列表或 `.bib`
- 代码仓库、系统截图、实验记录、测试结果
- 导师或学院新增格式要求

Agent 的标准执行入口见 `AGENTS.md`。

如果你的 Agent 支持 Skills，也可以让它读取 `skills/gcc-thesis-template/SKILL.md`。这个 Skill 把“更新内容 → 检查环境 → 编译 → 视觉验收”的流程写成了更短的执行规范。

如果你想让另一个 Agent 专门审核这个模板，不要让它直接读普通 README 后自由发挥，而是把 `AGENT_REVIEW.md` 交给它。这个文件规定了只读审核流程、严重级别、必须检查的学校格式项和报告输出结构。

### 方法二：本地硬编码使用

```bash
git clone https://github.com/Aidenwu0209/gcc-thesis-template.git
cd gcc-thesis-template
python3 scripts/check_structure.py
python3 scripts/doctor.py
```

然后修改这些文件：

```text
extraTex/meta.tex                 学生信息、题目、关键词
extraTex/front/abstract_zh.tex    中文摘要
extraTex/front/abstract_en.tex    英文摘要
extraTex/body/*.tex               正文章节
extraTex/back/references.bib      参考文献
extraTex/back/thanks.tex          致谢
extraTex/attachments/*.tex        附件材料表
```

编译：

```bash
bash scripts/build.sh
```

只编正文或附件：

```bash
bash scripts/build.sh main
bash scripts/build.sh attachments
```

### 方法三：手动编译

```bash
xelatex -interaction=nonstopmode main.tex
biber main
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex

xelatex -interaction=nonstopmode attachments.tex
xelatex -interaction=nonstopmode attachments.tex
```

### 方法四：VS Code / LaTeX Workshop

用 VS Code 打开：

```text
gcc-thesis-template.code-workspace
```

LaTeX Workshop 中提供三个 recipe：

- `gcc-thesis-template`：编译正文和附件
- `gcc-main-only`：只编译 `main.tex`
- `gcc-attachments-only`：只编译 `attachments.tex`

## LaTeX 环境与包安装

### 最小要求

- TeX Live / MacTeX / MiKTeX
- XeLaTeX
- Biber
- Python 3（用于环境检查和结构检查）

关键 LaTeX 包：

```text
ctex
fontspec
xeCJK
geometry
setspace
fancyhdr
titlesec
titletoc
enumitem
caption
booktabs
longtable
tabularx
multirow
biblatex
biblatex-gb7714-2015
```

运行环境检查：

```bash
python3 scripts/doctor.py
```

### macOS

完整安装，最省心：

```bash
brew install --cask mactex
```

轻量安装：

```bash
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install ctex fontspec xecjk geometry setspace fancyhdr titlesec titletoc enumitem caption booktabs tools multirow biblatex biblatex-gb7714-2015 biber latexmk
```

安装后如果命令行找不到 `xelatex`，重开终端，或确认 `/Library/TeX/texbin` 已加入 `PATH`。

### Ubuntu / Debian / WSL

```bash
sudo apt update
sudo apt install texlive-xetex texlive-lang-chinese texlive-bibtex-extra biber latexmk
```

### Windows

推荐安装 TeX Live 或 MiKTeX，并确保 `xelatex` 与 `biber` 在 PowerShell / CMD 的 `PATH` 中可用。

安装后检查：

```powershell
xelatex --version
biber --version
python scripts/doctor.py
```

### Overleaf

可以上传本仓库 zip 到 Overleaf，编译器选择 **XeLaTeX**。如果参考文献没有自动刷新，手动 Recompile 两到三次，或检查 Overleaf 是否启用了 Biber。

## 模板编译产物

```text
main.pdf          论文正文
attachments.pdf   附件材料册
```

`.gitignore` 默认忽略 PDF 和 LaTeX 中间文件。正式发布 release 时再按需要上传 PDF。

## 目录结构

```text
.
├── main.tex                         # 论文正文入口
├── attachments.tex                  # 附件材料册入口
├── styles/gcc-thesis.sty            # 广州商学院格式规则
├── extraTex/
│   ├── meta.tex                     # 元信息
│   ├── front/                       # 声明、摘要
│   ├── body/                        # 正文章节
│   ├── back/                        # 附录、参考文献、致谢
│   └── attachments/                 # 附件材料表
├── assets/branding/gcc_logo.png
├── docs/format-checklist.md
├── AGENT_REVIEW.md
├── scripts/check_structure.py
├── scripts/doctor.py
├── scripts/build.sh
└── skills/gcc-thesis-template/SKILL.md
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
- 表题在表格上方，图题在图片下方。
- 参考文献使用 GB/T 7714-2015 顺序编码制。
- 附件册单独由 `attachments.tex` 生成，包含学校附件模板中的过程材料表。

更详细的核对项见 `docs/format-checklist.md`。

当前静态合规审计见 `docs/compliance-audit.md`。注意：未编译并逐页检查 PDF 前，不能宣称模板已经完全满足学校要求。

## Agent 质量门

Agent 完成一次论文整理后，至少应说明：

- `scripts/check_structure.py` 是否通过
- `scripts/doctor.py` 是否通过
- 是否成功生成 `main.pdf`
- 是否成功生成 `attachments.pdf`
- 是否检查过封面、声明、摘要、目录、正文首页、参考文献、致谢和附件表格
- 若无法编译，缺少的是 TeX 环境、Biber、字体还是某个 LaTeX 包

没有实际编译和视觉检查时，不应声称“完全符合学校要求”。

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
