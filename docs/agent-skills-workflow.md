# Agent 调用流程

这个文件只说明如何把仓库交给 Agent。用户可以让 Agent 先下载仓库，也可以在已经打开的仓库里继续工作；关键是一次只给一个明确任务。

用户不需要理解仓库里有哪些内部能力，也不需要手动选择能力模块。它们是给 Agent 使用的，不是给用户学习的菜单。

## 1. 把仓库交给 Agent

可以直接复制：

```text
请帮我使用 https://github.com/Aidenwu0209/gcc-thesis-template。
如果当前环境没有这个仓库，请先下载；如果已经打开仓库，请直接使用当前目录。
接下来我会给你一个明确任务，请只按这个任务执行，不要自动扩展成完整论文生成。
```

如果你已经自己下载，也可以用：

```bash
git clone https://github.com/Aidenwu0209/gcc-thesis-template.git
cd gcc-thesis-template
```

## 2. 只选一个任务

不要把下面三个任务混在一起。你这次想做什么，就复制哪一个。

### 只做排版和格式检查

```text
我的任务是：只做 LaTeX 排版和学校格式检查。

我会提供学生信息、论文正文或草稿、参考文献和学校补充要求。请不要重写正文、不要生成新题目、不要扩写论文；只把材料放进模板，修 LaTeX、引用、格式和编译问题。完成后运行 python3 scripts/check_structure.py 和 python3 scripts/doctor.py。环境允许时只编译需要的 PDF，并说明哪些格式还不能确认。
```

### 整理已有草稿或项目材料

```text
我的任务是：把已有草稿和项目材料整理成广州商学院本科毕业论文（设计）模板。

我会提供草稿、代码说明、截图、测试记录、参考文献、学生信息和导师要求。请保留真实内容，按模板拆分到 extraTex/，补齐摘要、正文结构、参考文献和附件 TODO。缺少证据的位置标 TODO，不要编造。整理后运行 python3 scripts/check_structure.py 和 python3 scripts/doctor.py；环境允许时编译 PDF。
```

### 从 idea 生成论文初稿

```text
我的任务是：从一个 idea 生成可继续修改的论文初稿。

我会提供 idea、专业方向、已有材料和限制条件。请先判断选题是否适合本科毕业论文（设计），输出题目建议、论文目录和材料缺口清单。等我确认题目和目录后，再把初稿写入 extraTex/。不要编造实验数据、系统截图、用户调研、参考文献、导师意见、签字日期或不存在的系统功能。
```

## 3. 继续补材料

后续直接在对话里继续补充文字、文件、截图、代码路径或参考文献即可。Agent 应只围绕你选定的任务继续推进。

如果 Agent 第一轮需要确认，应只问必要问题：

- 只排版：缺哪些模板字段、参考文献或编译环境。
- 整理材料：哪些内容能写入模板，哪些材料还缺证据。
- 从 idea 起稿：题目是否可行、目录是否确认、哪些材料必须补。

## 4. 写入模板

Agent 应按任务需要写入对应文件。只排版时，不应主动改写正文。

常见写入位置：

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
- 如果用户只有 idea，先输出候选题目、目录和缺口清单，再进入初稿。
- 如果用户只要排版，优先保留正文内容，不主动重写论文。
- 真实材料不足的位置保留 `TODO`。
- 不要编造实验数据、系统截图、用户调研、参考文献、导师意见、签字日期或不存在的系统功能。
