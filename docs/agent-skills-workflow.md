# Agent 调用流程

这个文件只说明一条路线：用户把仓库交给 Agent，把 idea 和材料直接发在对话里；Agent 自行完成选题判断、初稿生成、附件整理、编译检查和审核。

用户不需要理解仓库里有哪些内部能力，也不需要手动选择能力模块。它们是给 Agent 使用的，不是给用户学习的菜单。

## 1. 打开仓库

用 Codex / Claude Code / Cursor 打开本仓库。也可以先下载：

```bash
git clone https://github.com/Aidenwu0209/gcc-thesis-template.git
cd gcc-thesis-template
```

## 2. 复制启动语

把下面这段话复制给 Agent：

```text
请调用这个仓库的广州商学院本科毕业论文（设计）工作流。

我会直接在对话里提供 idea、学生信息、专业方向、草稿、代码、截图、参考文献、导师要求和学校补充要求。请你按一条主路径完成：

1. 先判断我的选题是否适合本科毕业论文（设计），给出最稳妥的论文题目、目录和材料缺口清单。
2. 基于我提供的真实材料生成论文初稿，并写入 extraTex/ 对应文件。
3. 整理附件材料；缺少签字、日期、评语或证据的位置保留 TODO。
4. 运行 python3 scripts/check_structure.py 和 python3 scripts/doctor.py。
5. 环境允许时编译 main.pdf 和 attachments.pdf，并按 AGENT_REVIEW.md 做审核。

约束：不要编造实验数据、系统截图、用户调研、参考文献、导师意见、签字日期或不存在的系统功能。每一步完成后说明已经产出什么、还缺什么真实材料。
```

## 3. 直接补充材料

随后在对话里继续给材料即可。可以是文字，也可以是文件、截图、代码路径或参考文献。

推荐这样发：

```text
我的 idea 是：
【写你的想法】

学生信息：
【姓名、学号、学院、专业班级、指导教师；不知道就写暂缺】

专业方向：
【例如软件工程、数据分析、AI 应用、信息系统等】

已经有的材料：
【草稿、截图、代码、测试记录、参考文献、导师要求；没有就写暂无】

请先判断题目和目录，再告诉我还缺什么。
```

Agent 第一轮应输出：

- 推荐题目和题目风险。
- 论文目录。
- 每章能写什么。
- 每章缺什么真实材料。
- 已经写入或准备写入哪些 `extraTex/` 文件。

## 4. 让 Agent 写入模板

确认题目和目录后，让 Agent 继续：

```text
按刚才确认的题目和目录，把论文初稿写入模板。缺少真实证据的位置保留 TODO，不要编造。
```

Agent 应写入：

```text
extraTex/meta.tex
extraTex/front/abstract_zh.tex
extraTex/front/abstract_en.tex
extraTex/body/*.tex
extraTex/back/references.bib
extraTex/back/thanks.tex
extraTex/attachments/*.tex
```

## 5. 编译和审核

每次大改后让 Agent 运行：

```bash
python3 scripts/check_structure.py
python3 scripts/doctor.py
```

如果环境可用，再运行：

```bash
bash scripts/build.sh all
```

最终应得到：

```text
main.pdf          毕业论文（设计）正文
attachments.pdf   附件材料册
```

编译成功后，让 Agent 按 `AGENT_REVIEW.md` 做一次只读审核。没有成功编译和逐页检查 PDF 前，不能声称“完全符合学校要求”。

## Agent 内部规则

这部分是给 Agent 看的：

- 用户输入来自对话、上传文件、明确给出的本地路径或仓库已有内容；不要要求用户先填写额外入口文件。
- 每个阶段只读取必要的仓库说明和能力文件；不要一次性加载全部能力。
- 先做题目、目录和缺口清单，再写初稿。
- 真实材料不足的位置保留 `TODO`。
- 不要编造实验数据、系统截图、用户调研、参考文献、导师意见、签字日期或不存在的系统功能。
