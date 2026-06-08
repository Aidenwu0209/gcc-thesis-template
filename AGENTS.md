# Agent Instructions for `gcc-thesis-template`

This repository is an Agent-first LaTeX workflow for an unofficial Guangzhou College of Commerce undergraduate thesis template. Treat it as a Vibe Writing scaffold: the student supplies research facts and school requirements; the Agent helps turn an idea or draft into structured thesis files, compiles, verifies, and reports remaining risks.

## Core Goal

Produce two usable thesis artifacts:

- `main.pdf`: undergraduate thesis body.
- `attachments.pdf`: attachment-material booklet with task book, proposal, progress record, defense record, and score sheet.

User intake may come from chat messages, uploaded files, explicit local paths, screenshots, code repositories, Word/Markdown drafts, or existing repository files. Do not require the user to fill a special intake file before starting.

## File Ownership

- Student metadata: edit `extraTex/meta.tex`.
- Abstracts: edit `extraTex/front/abstract_zh.tex` and `extraTex/front/abstract_en.tex`.
- Body chapters: edit `extraTex/body/*.tex`.
- References: edit `extraTex/back/references.bib`.
- Thanks and appendix: edit `extraTex/back/thanks.tex` and `extraTex/back/appendix.tex`.
- Attachment forms: edit `extraTex/attachments/*.tex`.
- Formatting rules: edit `styles/gcc-thesis.sty` only when the school formatting requirement changes.

## Standard Workflow

1. Read `README.md`, `docs/agent-skills-workflow.md`, `docs/format-checklist.md`, `docs/compliance-audit.md`, `main.tex`, `attachments.tex`, and `extraTex/meta.tex`.
   - Use the user's chat content and attached/provided files as the primary intake.
   - If coordinating internal research-writing skills, do not load all skills at once. Select at most 1-3 relevant Skill files for the current stage and report which ones were read.
   - If the request involves installation or compilation failures, also read `docs/setup.md`.
2. Ask for or infer only genuinely missing thesis facts: title, student name, student ID, college, major class, supervisor, dates, keywords, references, and project content.
3. For idea-only requests, produce title candidates, an outline, and an evidence gap list before writing the draft.
4. Update content files first. Avoid changing `styles/gcc-thesis.sty` unless the user explicitly asks for format work or the PDF clearly violates school rules.
5. Run `python3 scripts/check_structure.py`.
6. Run `python3 scripts/doctor.py`. If TeX tools are missing, report the missing environment and stop before pretending PDF validation passed.
7. If the environment is ready, run `bash scripts/build.sh all`.
8. Inspect `main.pdf` and `attachments.pdf`, especially cover, statement, abstract, TOC, first body page, references, thanks, and attachment forms.
9. Fix formatting or content issues and recompile.

## Validation Rules

- No final claim of “fully compliant” without a successful PDF compile and visual inspection.
- Do not fabricate experiments, screenshots, user research, references, signatures, dates, or implemented features. Mark missing evidence as TODO.
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

## Common User Prompt

```text
请调用这个仓库的广州商学院本科毕业论文（设计）工作流。

我会直接在对话里提供 idea、学生信息、专业方向、草稿、代码、截图、参考文献、导师要求和学校补充要求。请先判断题目和目录，再写入模板、整理附件、运行检查，并说明还缺什么真实材料。

不要编造实验数据、系统截图、用户调研、参考文献、导师意见、签字日期或不存在的系统功能。
```
