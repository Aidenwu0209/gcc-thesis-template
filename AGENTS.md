# Agent Instructions for `gcc-thesis-template`

This repository is an Agent-first LaTeX workflow for an unofficial Guangzhou College of Commerce undergraduate thesis template. Treat it as a Vibe Writing scaffold: the student supplies research facts and school requirements; the Agent helps turn an idea or draft into structured thesis files, compiles, verifies, and reports remaining risks.

## Core Goal

Produce one usable thesis artifact by default:

- `main.pdf`: undergraduate thesis body.

`attachments.pdf` is optional. Do not work on attachment forms, scoring sheets, signatures, or review comments unless the user explicitly asks for them.

User intake may come from chat messages, uploaded files, explicit local paths, screenshots, code repositories, Word/Markdown drafts, or existing repository files. Do not require the user to fill a special intake file before starting.

## File Ownership

- Student metadata: edit `extraTex/meta.tex`.
- Abstracts: edit `extraTex/front/abstract_zh.tex` and `extraTex/front/abstract_en.tex`.
- Body chapters: edit `extraTex/body/*.tex`.
- References: edit `extraTex/back/references.bib`.
- Thanks and appendix: edit `extraTex/back/thanks.tex` and `extraTex/back/appendix.tex`.
- Optional attachment forms: edit `extraTex/attachments/*.tex` only when requested.
- Formatting rules: edit `styles/gcc-thesis.sty` only when the school formatting requirement changes.

## Standard Workflow

1. Read `README.md`, `docs/agent-skills-workflow.md`, `docs/format-checklist.md`, `docs/compliance-audit.md`, `main.tex`, and `extraTex/meta.tex`.
   - Use the user's chat content and attached/provided files as the primary intake.
   - If coordinating internal research-writing skills, do not load all skills at once. Select at most 1-3 relevant Skill files for the current stage and report which ones were read.
   - If the request involves installation or compilation failures, also read `docs/setup.md`.
2. Ask for or infer only genuinely missing thesis facts: title, student name, student ID, college, major class, supervisor, dates, keywords, references, and project content.
3. For idea-only requests, produce title candidates, an outline, and an evidence gap list before writing the draft.
4. Update content files first. Avoid changing `styles/gcc-thesis.sty` unless the user explicitly asks for format work or the PDF clearly violates school rules.
5. Run `python3 scripts/check_structure.py`.
6. Run `python3 scripts/doctor.py`. If TeX tools are missing, report the missing environment and stop before pretending PDF validation passed.
7. If the environment is ready, run `bash scripts/build.sh main`.
8. Inspect `main.pdf`, especially cover, statement, abstract, TOC, first body page, references, and thanks.
9. Fix formatting or content issues and recompile.

## Validation Rules

- No final claim of “fully compliant” without a successful PDF compile and visual inspection.
- Do not fabricate experiments, screenshots, user research, references, signatures, dates, or implemented features. Mark missing evidence as TODO.
- Simulated data, sample screenshots, or placeholder results may be used only for demonstration, and must be explicitly labeled as simulated/sample/placeholder in the thesis body.
- If `xelatex` or `biber` is unavailable, say that only static checks were completed.
- Keep generated PDFs and LaTeX cache out of commits unless the user explicitly asks to publish release assets.
- For school Logo and official texts, keep the repository wording “unofficial” and preserve the license caveat in `README.md` and `NOTICE.md`.
- When the user asks for an independent audit or review, follow `AGENT_REVIEW.md` and default to read-only findings before making edits.

## Build Commands

```bash
python3 scripts/check_structure.py
python3 scripts/doctor.py
bash scripts/build.sh main
bash scripts/build.sh attachments
bash scripts/build.sh all
```

## Review Entry

For independent compliance review, hand `AGENT_REVIEW.md` to another Agent. That file defines the severity scale, required commands, PDF inspection pages, and report format.

## Common User Prompts

```text
请帮我使用 https://github.com/Aidenwu0209/gcc-thesis-template。
如果当前环境没有这个仓库，请先下载；如果已经打开仓库，请直接使用当前目录。
接下来我会给你一个明确任务，请只按这个任务执行，不要自动扩展成完整论文生成。
```

```text
我的任务是：只做 LaTeX 排版和学校格式检查。

我会提供学生信息、论文正文或草稿、参考文献和学校补充要求。请不要重写正文、不要生成新题目、不要扩写论文；只把材料放进模板，修 LaTeX、引用、格式和编译问题。
```

```text
我的任务是：把已有草稿和项目材料整理成广州商学院本科毕业论文（设计）模板。

请保留真实内容，按模板拆分到 extraTex/。缺少证据的位置标 TODO，不要编造。
```

```text
我的任务是：从一个 idea 生成可继续修改的论文初稿。

请先判断选题是否适合本科毕业论文（设计），输出题目建议、论文目录和材料缺口清单。等我确认题目和目录后，再写入 extraTex/。
```

```text
请只做快速检查，不要修改正文内容。

请运行 python3 scripts/check_structure.py 和 python3 scripts/doctor.py。环境允许时再运行 bash scripts/build.sh main。最后告诉我哪些检查通过、哪些检查失败、是否生成了 main.pdf、还缺什么环境或材料。
```
