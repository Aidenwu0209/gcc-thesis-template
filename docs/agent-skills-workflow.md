# Agent Skills 工作流

本页说明如何把 `gcc-thesis-template` 和科研写作相关 Agent Skills 组合起来使用。目标是让毕业论文不只停留在“排版模板”，而是形成一条可由 Agent 执行的工作链：

```text
选题澄清
→ 分节起草
→ 图表和实验材料整理
→ 论文内容精修
→ LaTeX 编译
→ 学校格式审核
```

本仓库已经内置 [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) 中和毕业论文最相关的三个类别：

```text
skills/orchestra-research/AI-Research-SKILLs/20-ml-paper-writing
skills/orchestra-research/AI-Research-SKILLs/21-research-ideation
skills/orchestra-research/AI-Research-SKILLs/22-agent-native-research-artifact
```

这三个类别来自 Orchestra Research 的 MIT 开源仓库，已随本仓库一起提供，用户不需要单独安装才能让 Agent 阅读这些 Skill 文件。完整上游仓库有 98 个 Skills，覆盖训练、推理、RAG、MLOps、多模态等更广范围；本模板只内置毕业论文高相关子集，当前约 1.8 MB，保留了相关 Skill 的 references 和 templates 以保证可用性。

## 推荐 Skill 组合

| Skill | 在本仓库中的角色 | 适合什么时候用 |
|---|---|---|
| `gcc-thesis-template` | 本仓库自带 Skill，负责广州商学院模板结构、LaTeX 文件分层、编译和格式验收 | 始终作为主入口 |
| `brainstorming-research-ideas` | 结构化选题和问题发现 | 只有模糊 idea，或需要判断选题是否值得做 |
| `creative-thinking-for-research` | 从跨域类比、问题重构等角度扩展选题 | 题目太普通，需要找更有辨识度的切入点 |
| `ml-paper-writing` | 研究型论文结构、引用核验、表格、写作策略 | 选题偏 AI/算法/实验研究，或需要更强论文结构 |
| `systems-paper-writing` | 系统类论文段落结构和评估组织 | 毕设是软件系统、平台、工具链或工程实现 |
| `academic-plotting` | 实验图、架构图、数据图表 | 需要把结果或系统结构变成论文图表 |
| `ara-compiler` | 把论文、代码、日志和笔记整理成带证据的研究包 | 材料很多，需要追踪 claims、evidence、experiments |
| `ara-research-manager` | 会话结束后记录决策、实验、失败和证据 | 长期迭代论文或项目，避免过程材料丢失 |
| `ara-rigor-reviewer` | 从证据、可证伪性、方法严谨性等维度审查 | 提交前做内容严谨性复核 |

## 内置路径

Agent 需要读取 Orchestra Skill 时，直接读这些本地文件：

```text
skills/orchestra-research/AI-Research-SKILLs/21-research-ideation/brainstorming-research-ideas/SKILL.md
skills/orchestra-research/AI-Research-SKILLs/21-research-ideation/creative-thinking-for-research/SKILL.md
skills/orchestra-research/AI-Research-SKILLs/20-ml-paper-writing/ml-paper-writing/SKILL.md
skills/orchestra-research/AI-Research-SKILLs/20-ml-paper-writing/systems-paper-writing/SKILL.md
skills/orchestra-research/AI-Research-SKILLs/20-ml-paper-writing/academic-plotting/SKILL.md
skills/orchestra-research/AI-Research-SKILLs/22-agent-native-research-artifact/compiler/SKILL.md
skills/orchestra-research/AI-Research-SKILLs/22-agent-native-research-artifact/research-manager/SKILL.md
skills/orchestra-research/AI-Research-SKILLs/22-agent-native-research-artifact/rigor-reviewer/SKILL.md
```

如果需要上游全量 Skills，再用 Orchestra 官方安装器：

```bash
npx @orchestra-research/ai-research-skills
```

## 从 0 到初稿的 Skill 链

如果你只有一个 idea，推荐让 Agent 按下面顺序工作：

```text
gcc-thesis-template
→ brainstorming-research-ideas
→ creative-thinking-for-research
→ gcc-thesis-template
→ AGENT_REVIEW.md
```

含义：

1. `gcc-thesis-template` 先读取学校模板和仓库结构，确定输出必须落到 `extraTex/` 和 `attachments.tex`。
2. `brainstorming-research-ideas` 用于判断 idea 是问题优先还是方案优先，并收敛成可执行题目。
3. `creative-thinking-for-research` 用于扩展切入点，避免选题过于普通。
4. 回到 `gcc-thesis-template`，把确认后的题目、目录和初稿写入 LaTeX 文件并检查结构。
5. 最后用 `AGENT_REVIEW.md` 做只读审核，检查格式、编译和视觉验收。

## 偏技术/算法选题的 Skill 链

如果毕业设计涉及模型、算法、实验表格或对比指标，可增加：

```text
gcc-thesis-template
→ ml-paper-writing 或 systems-paper-writing
→ academic-plotting
→ ara-rigor-reviewer
→ gcc-thesis-template
→ AGENT_REVIEW.md
```

适用任务：

- 梳理贡献点和技术路线。
- 把实验结果整理成论文表格。
- 检查引用是否需要补充。
- 生成系统架构图、方法流程图或实验流程图。
- 检查图表 caption 是否和正文一致。
- 从证据是否支撑结论的角度复核论文内容。

使用 `ml-paper-writing` 或 `systems-paper-writing` 时要注意：它们偏向会议论文语境。用于本科毕业论文时，应把“目标会议、匿名投稿、页数限制”等约束改成“广州商学院本科毕业论文（设计）、学院模板、导师要求”。

## 过程证据链

如果项目周期较长，或材料包括代码、实验日志、截图、参考文献和多次修改记录，可使用：

```text
ara-compiler
→ ara-research-manager
→ ara-rigor-reviewer
→ gcc-thesis-template
→ AGENT_REVIEW.md
```

适用任务：

- 把代码、论文草稿、实验日志和原始笔记编译成结构化研究材料。
- 记录决策、实验、失败尝试和证据来源。
- 审核结论是否被证据支持。
- 为附件材料、开题报告、进展记录和答辩材料提供依据。

注意：ARA 工作流会生成额外的研究过程材料，适合长期项目；如果只是普通排版，不必使用。

## 图表材料链

如果论文需要系统图、流程图、模块图：

```text
academic-plotting
→ gcc-thesis-template
→ AGENT_REVIEW.md
```

Agent 应输出：

- 图的用途。
- 图中模块。
- 模块之间关系。
- 适合放入论文的文件格式。
- 对应的图题和正文解释。

如果图还没真实设计完成，先保留 TODO，不要生成和系统实现不一致的架构图。

## 给 Agent 的统一提示词

```text
请按 docs/agent-skills-workflow.md 使用本仓库。

优先使用本仓库自带的 gcc-thesis-template Skill。
本仓库已经内置 Orchestra Research 的 thesis-relevant skills 子集，路径在 skills/orchestra-research/AI-Research-SKILLs/。
请按任务读取对应 SKILL.md，而不是要求用户手动安装。

我的目标是：
【从 idea 起稿 / 整理项目材料 / 生成图表 / 审查证据 / 审核格式】

已有材料：
【列出 idea、代码、截图、Word、数据、参考文献、导师要求】

要求：
1. 不要编造实验数据、系统截图、参考文献、导师意见或不存在的功能。
2. 缺少证据的位置用 TODO 标记。
3. 论文内容最终要写入 extraTex/ 对应文件。
4. 运行 scripts/check_structure.py 和 scripts/doctor.py。
5. 环境允许时编译 main.pdf 和 attachments.pdf。
6. 最后说明实际完成了什么、读取了哪些 Skill 文件、哪些地方还需要用户补材料。
```

## 和其他文档的关系

- [idea-to-thesis-workflow.md](idea-to-thesis-workflow.md)：写从 idea 到论文初稿的内容流程。
- [agent-skills-workflow.md](agent-skills-workflow.md)：写哪些 Skill 参与、如何串联。
- [setup.md](setup.md)：写 LaTeX 安装和编译。
- [format-checklist.md](format-checklist.md)：写学校格式核对项。
- [AGENT_REVIEW.md](../AGENT_REVIEW.md)：写独立审核 Agent 的只读检查流程。
