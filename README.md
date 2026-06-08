# 广州商学院本科毕业论文（设计）LaTeX 模板

这是一个 **Agent-first / Vibe Writing** 取向的非官方广州商学院本科毕业论文（设计）工作流模板。这里的 Vibe Writing 指“人给目标、材料和判断，Agent 负责拆稿、写初稿、排版、编译、审核并迭代”的协作方式。仓库名中的 `gcc` 指 Guangzhou College of Commerce。

它不只是排版模板。它可以支持：

- 从一个毕业设计 idea 生成论文题目、目录、缺口清单和完整初稿骨架。
- 把 Word / Markdown / PDF / 截图 / 代码项目材料迁移到 LaTeX 论文结构。
- 生成 `main.pdf` 论文正文和 `attachments.pdf` 附件材料册。
- 检查 LaTeX 环境、模板结构、学校格式和过程材料完整性。
- 把 `AGENT_REVIEW.md` 交给另一个 Agent 做独立审核。

本模板不是学校官方发布物。正式提交前，请以学院当年通知、导师意见和教务系统要求为准。没有真实项目材料、真实实验结果、真实截图和可核验参考文献时，不应让 Agent 凭空编造内容后直接提交。

## 适用范围

当前版本优先适配：

- 广州商学院本科毕业论文（设计）撰写基本规范
- 现代信息产业学院 2026 届毕业论文（设计）撰写模板
- 现代信息产业学院毕业论文（设计）论文附件模板
- 广州商学院毕业设计（论文）质量标准（试用）

本仓库以广州商学院通用撰写规范为底线，以现代信息产业学院 2026 届模板作为当前可执行样例。其他学院如果封面字段、附件表或签名页不同，应把学院当年模板一起交给 Agent，再局部调整 `extraTex/meta.tex`、`extraTex/attachments/` 或 `styles/gcc-thesis.sty`。

## 先选工作流

| 你的目标 | 入口 |
|---|---|
| 只有一个 idea，想生成完整论文初稿 | 读 [docs/idea-to-thesis-workflow.md](docs/idea-to-thesis-workflow.md) |
| 想用 Agent Skills 串起写作、图表、证据和审核 | 读 [docs/agent-skills-workflow.md](docs/agent-skills-workflow.md) |
| 已经有 Word / Markdown / 截图 / 代码材料，想整理成论文 | 看下面的“Agent 快速开始” |
| 自己会改 LaTeX，只想填模板 | 看下面的“人工快速开始” |
| 只想安装环境、编译 PDF、排查缺包 | 读 [docs/setup.md](docs/setup.md) |
| 想核对学校格式 | 读 [docs/format-checklist.md](docs/format-checklist.md) 和 [docs/compliance-audit.md](docs/compliance-audit.md) |
| 想让另一个 Agent 专门挑错 | 把 [AGENT_REVIEW.md](AGENT_REVIEW.md) 交给它 |

三个 Agent 入口的边界：

- `README.md`：给人看的导航和快速上手。
- `AGENTS.md`：给写作和排版 Agent 的执行说明。
- `AGENT_REVIEW.md`：给审核 Agent 的只读检查说明。

## Idea 到论文初稿

如果你只有一个 idea，可以让 Agent 先跑 idea-to-thesis 工作流：

```text
请使用 gcc-thesis-template 执行 idea-to-thesis 工作流。

我的 idea 是：
【写你的毕业设计想法】

我的专业/方向是：
【例如：软件工程、人工智能、数据分析、信息管理等】

请先阅读 README.md、AGENTS.md 和 docs/idea-to-thesis-workflow.md。
然后判断选题可行性，生成题目、目录、缺口清单和论文初稿。
能根据我提供材料写实的内容直接写入 extraTex/；缺少证据的地方必须标 TODO。
不要编造实验数据、系统截图、用户调研、参考文献或不存在的功能。
最后运行 scripts/check_structure.py 和 scripts/doctor.py；环境允许时再编译 main.pdf 和 attachments.pdf。
```

详细阶段、输入格式和验收要求见 [docs/idea-to-thesis-workflow.md](docs/idea-to-thesis-workflow.md)。

## Agent Skills 工作流

从 0 到初稿只是第一步。完成初稿后，可以继续使用 [docs/agent-skills-workflow.md](docs/agent-skills-workflow.md) 把研究选题、论文写作、图表设计、过程证据整理和最终审核串起来。

这个工作流已经直接内置 [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) 的毕业论文高相关子集，包括 research ideation、ML paper writing、academic plotting 和 ARA rigor review。用户不需要先安装上游仓库才能让 Agent 阅读这些 Skill。

使用时不要让 Agent 一次性加载所有 Skills。推荐先读 `skills/gcc-thesis-template/SKILL.md` 和 [docs/agent-skills-workflow.md](docs/agent-skills-workflow.md)，再按当前阶段选择 1-3 个 Orchestra Skill。

## Agent 快速开始

在 Codex / Claude Code / Cursor 中打开本仓库，然后给 Agent 这样的任务：

```text
请使用这个仓库整理我的广州商学院本科毕业论文（设计）。
先阅读 README.md、AGENTS.md、docs/format-checklist.md、main.tex、attachments.tex 和 extraTex/meta.tex。
然后根据我提供的论文题目、学生信息、正文草稿、参考文献和学校要求，更新 meta、摘要、正文、参考文献、致谢和附件材料。
完成后运行 scripts/check_structure.py、scripts/doctor.py，并在环境允许时编译 main.pdf 和 attachments.pdf。
最后按学校格式清单检查封面、声明、摘要、目录、正文首页、参考文献、致谢和附件表格。
```

适合交给 Agent 的材料：

- 学生姓名、学号、学院、专业班级、指导教师、日期
- 论文题目和中英文关键词
- Word / Markdown / PDF / 截图形式的正文草稿
- 参考文献列表或 `.bib`
- 代码仓库、系统截图、实验记录、测试结果
- 导师或学院新增格式要求

如果你的 Agent 支持 Skills，也可以让它读取 `skills/gcc-thesis-template/SKILL.md`。

## 人工快速开始

```bash
git clone https://github.com/Aidenwu0209/gcc-thesis-template.git
cd gcc-thesis-template
python3 scripts/check_structure.py
python3 scripts/doctor.py
```

`check_structure.py` 检查模板文件是否齐全。`doctor.py` 检查本机是否装好了 LaTeX 编译环境；如果提示缺少 `xelatex`、`biber` 或 `kpsewhich`，先看 [docs/setup.md](docs/setup.md)。

主要修改这些文件：

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
bash scripts/build.sh all
```

只编正文或附件：

```bash
bash scripts/build.sh main
bash scripts/build.sh attachments
```

## 产物和目录

本仓库会生成两个文件：

```text
main.pdf          毕业论文（设计）正文
attachments.pdf   论文附件材料册
```

如果只需要正文，可以暂时不管 `attachments.tex` 和 `extraTex/attachments/`。

核心目录：

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
├── docs/idea-to-thesis-workflow.md
├── docs/agent-skills-workflow.md
├── docs/setup.md
├── docs/format-checklist.md
├── docs/compliance-audit.md
├── AGENTS.md
├── AGENT_REVIEW.md
└── skills/
    ├── gcc-thesis-template/SKILL.md
    └── orchestra-research/AI-Research-SKILLs/
```

## 质量门

Agent 完成一次论文整理后，至少应说明：

- `scripts/check_structure.py` 是否通过。
- `scripts/doctor.py` 是否通过。
- 是否成功生成 `main.pdf` 和 `attachments.pdf`。
- 是否检查过封面、声明、摘要、目录、正文首页、参考文献、致谢和附件表格。
- 若无法编译，缺少的是 TeX 环境、Biber、字体还是某个 LaTeX 包。

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

模板工程结构参考了 `huangwb8/ChineseResearchLaTeX` 中的 `thesis-just-bachelor`，该项目同样采用 MIT License。

本仓库还内置了 `Orchestra-Research/AI-Research-SKILLs` 的毕业论文高相关子集，来源和许可见 [skills/orchestra-research/README.md](skills/orchestra-research/README.md) 与 [NOTICE.md](NOTICE.md)。

广州商学院校名、Logo 和学校模板文本属于其各自权利方，本仓库仅用于论文排版学习与非官方模板维护。
