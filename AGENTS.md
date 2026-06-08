# Agent Instructions for `gcc-thesis-template`

This repository is an Agent-first LaTeX workflow for an unofficial Guangzhou College of Commerce undergraduate thesis template. Treat it as a Vibe Writing scaffold: the student supplies research facts and school requirements; the Agent helps turn an idea or draft into structured thesis files, compiles, verifies, and reports remaining risks.

## Core Goal

Produce two usable thesis artifacts:

- `main.pdf`: undergraduate thesis body.
- `attachments.pdf`: attachment-material booklet with task book, proposal, progress record, defense record, and score sheet.

When the user only has an idea, first produce a realistic thesis direction, outline, evidence gap list, and TODO-marked draft by following `docs/idea-to-thesis-workflow.md`.

## File Ownership

- Student metadata: edit `extraTex/meta.tex`.
- Abstracts: edit `extraTex/front/abstract_zh.tex` and `extraTex/front/abstract_en.tex`.
- Body chapters: edit `extraTex/body/*.tex`.
- References: edit `extraTex/back/references.bib`.
- Thanks and appendix: edit `extraTex/back/thanks.tex` and `extraTex/back/appendix.tex`.
- Attachment forms: edit `extraTex/attachments/*.tex`.
- Formatting rules: edit `styles/gcc-thesis.sty` only when the school formatting requirement changes.

## Standard Workflow

1. Read `README.md`, `docs/format-checklist.md`, `docs/compliance-audit.md`, `main.tex`, `attachments.tex`, and `extraTex/meta.tex`.
   - If the request starts from only an idea, also read `docs/idea-to-thesis-workflow.md`.
   - If the request involves Orchestra Research skills, research ideation, paper-writing helpers, academic plotting, research artifacts, or rigor review, also read `docs/agent-skills-workflow.md`.
   - Do not load all Orchestra Skills at once. Select at most 1-3 relevant Skill files for the current stage and report which ones were read.
   - If the request involves installation or compilation failures, also read `docs/setup.md`.
2. Ask for or infer the missing thesis facts: title, student name, student ID, college, major class, supervisor, dates, keywords, references, and project content.
3. Update content files first. Avoid changing `styles/gcc-thesis.sty` unless the user explicitly asks for format work or the PDF clearly violates school rules.
4. Run `python3 scripts/check_structure.py`.
5. Run `python3 scripts/doctor.py`. If TeX tools are missing, report the missing environment and stop before pretending PDF validation passed.
6. If the environment is ready, run `bash scripts/build.sh`.
7. Inspect `main.pdf` and `attachments.pdf`, especially cover, statement, abstract, TOC, first body page, references, thanks, and attachment forms.
8. Fix formatting or content issues and recompile.

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

## Common User Prompts

```text
请用这个模板把我的毕业论文整理成广州商学院现代信息产业学院格式，先更新 meta、摘要、正文和参考文献，然后编译并检查 PDF。
```

```text
请只根据学校格式要求修样式，不改我的正文内容；修完后编译 main.pdf 和 attachments.pdf 并说明检查结果。
```

```text
请帮我把 Word/Markdown 草稿迁移到这个模板，保留研究事实，按章节拆分到 extraTex/body/。
```

```text
请根据我的毕业设计 idea 执行 docs/idea-to-thesis-workflow.md，先判断选题、生成目录和缺口清单，再把不编造事实的论文初稿写入 extraTex/。
```

```text
请根据 docs/agent-skills-workflow.md 选择合适的 Orchestra Skill 链处理我的毕业论文；优先读取 skills/orchestra-research/AI-Research-SKILLs/ 里的本地 Skill 文件。
```

```text
请不要一次性加载所有 Orchestra Skills。先读 gcc-thesis-template 和 docs/agent-skills-workflow.md，再按当前阶段选择 1-3 个最相关的 Skill。
```
