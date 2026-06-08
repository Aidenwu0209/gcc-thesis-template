# 广州商学院本科毕业论文（设计）LaTeX 模板

这是一个面向 Agent 协作的非官方广州商学院本科毕业论文（设计）模板。它不只是排版模板，也可以让 Agent 帮你从 idea 推进到论文初稿、附件材料、编译检查和格式审核。

用户入口只有一个：打开这个仓库，把下面的启动语复制给 Codex / Claude Code / Cursor，然后写清楚你的目标。你可以只做排版，也可以整理已有草稿，或从一个 idea 生成论文初稿。

本模板不是学校官方发布物。正式提交前，请以学院当年通知、导师意见和教务系统要求为准。没有真实项目材料、真实实验结果、真实截图和可核验参考文献时，不应让 Agent 凭空编造内容后直接提交。

## 可以做什么

- 从一个 idea 判断选题是否适合作为本科毕业论文（设计）。
- 生成论文题目、目录、材料缺口清单和可继续修改的初稿。
- 把 Word / Markdown / 截图 / 代码说明整理进 LaTeX 模板。
- 生成 `main.pdf` 论文正文和 `attachments.pdf` 附件材料册。
- 检查 LaTeX 环境、模板结构和学校格式要求。
- 让另一个 Agent 按 `AGENT_REVIEW.md` 做最终审核。

## 快速开始

下载仓库：

```bash
git clone https://github.com/Aidenwu0209/gcc-thesis-template.git
cd gcc-thesis-template
```

不熟悉 GitHub 的话，也可以在页面点击 **Code -> Download ZIP**，解压后用 Codex / Claude Code / Cursor 打开文件夹。

然后复制这段话给 Agent，把“我的目标是”改成你的真实目标：

```text
请使用这个仓库帮助我完成广州商学院本科毕业论文（设计）。

我的目标是：【只做 LaTeX 排版和格式检查 / 整理已有草稿 / 从一个 idea 生成论文初稿】

我会直接在对话里提供 idea、学生信息、专业方向、草稿、代码、截图、参考文献、导师要求和学校补充要求。请你先判断我属于哪种情况，再执行：

1. 如果我只想排版：不要改写正文内容，只处理模板字段、LaTeX 格式、编译问题和学校格式检查。
2. 如果我已有草稿或项目材料：保留真实内容，把它整理进 extraTex/，补齐摘要、正文结构、参考文献和附件 TODO。
3. 如果我只有 idea：先判断选题是否适合本科毕业论文（设计），给出题目建议、目录和材料缺口清单；等我确认后再写初稿。
4. 每种情况都要运行 python3 scripts/check_structure.py 和 python3 scripts/doctor.py。
5. 环境允许时编译 main.pdf 和 attachments.pdf，并按 AGENT_REVIEW.md 做审核。

约束：不要编造实验数据、系统截图、用户调研、参考文献、导师意见、签字日期或不存在的系统功能。每一步完成后说明已经产出什么、还缺什么真实材料。
```

之后你只需要继续补充材料，例如：

```text
我的目标是：只做 LaTeX 排版和格式检查。
我已经有正文草稿和参考文献，下面发给你。
请尽量不改正文，只帮我放进模板、检查格式并尝试编译。
```

## 编译和检查

先检查结构和环境：

```bash
python3 scripts/check_structure.py
python3 scripts/doctor.py
```

如果环境通过，再编译：

```bash
bash scripts/build.sh all
```

产物：

```text
main.pdf          毕业论文（设计）正文
attachments.pdf   附件材料册
```

LaTeX 安装、VS Code、Overleaf 和缺包排查见 [docs/setup.md](docs/setup.md)。

## 手动填写

如果你不使用 Agent，也可以直接改这些文件：

```text
extraTex/meta.tex                 学生信息、题目、关键词
extraTex/front/abstract_zh.tex    中文摘要
extraTex/front/abstract_en.tex    英文摘要
extraTex/body/*.tex               正文章节
extraTex/back/references.bib      参考文献
extraTex/back/thanks.tex          致谢
extraTex/attachments/*.tex        附件材料表
```

## 目录结构

```text
.
├── main.tex                         # 论文正文入口
├── attachments.tex                  # 附件材料册入口
├── styles/gcc-thesis.sty            # 广州商学院格式规则
├── extraTex/                        # 论文内容和附件内容
├── docs/agent-skills-workflow.md    # Agent 调用流程
├── docs/setup.md                    # LaTeX 安装和编译说明
├── docs/format-checklist.md         # 格式核对清单
├── docs/compliance-audit.md         # 学校要求映射
├── AGENTS.md                        # 给执行 Agent 的仓库规则
└── AGENT_REVIEW.md                  # 给审核 Agent 的只读审核规则
```

## 适用范围

当前版本优先适配：

- 广州商学院本科毕业论文（设计）撰写基本规范
- 现代信息产业学院 2026 届毕业论文（设计）撰写模板
- 现代信息产业学院毕业论文（设计）论文附件模板
- 广州商学院毕业设计（论文）质量标准（试用）

其他学院如果封面字段、附件表或签名页不同，可以把学院当年模板直接发给 Agent，让它按实际模板局部调整。

## 许可与来源

本项目代码采用 MIT License。

模板工程结构参考了 `huangwb8/ChineseResearchLaTeX` 中的 `thesis-just-bachelor`，该项目同样采用 MIT License。第三方来源和许可说明见 [NOTICE.md](NOTICE.md)。

广州商学院校名、Logo 和学校模板文本属于其各自权利方，本仓库仅用于论文排版学习与非官方模板维护。
