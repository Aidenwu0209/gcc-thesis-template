# Agent Instructions for `gcc-thesis-template`

This repository is an Agent-first LaTeX workflow for an unofficial Guangzhou College of Commerce undergraduate thesis template. Treat it as a Vibe Writing scaffold: the student supplies research facts and school requirements; the Agent updates sources, compiles, verifies, and reports remaining risks.

## Core Goal

Produce two usable thesis artifacts:

- `main.pdf`: undergraduate thesis body.
- `attachments.pdf`: attachment-material booklet with task book, proposal, progress record, defense record, and score sheet.

## File Ownership

- Student metadata: edit `extraTex/meta.tex`.
- Abstracts: edit `extraTex/front/abstract_zh.tex` and `extraTex/front/abstract_en.tex`.
- Body chapters: edit `extraTex/body/*.tex`.
- References: edit `extraTex/back/references.bib`.
- Thanks and appendix: edit `extraTex/back/thanks.tex` and `extraTex/back/appendix.tex`.
- Attachment forms: edit `extraTex/attachments/*.tex`.
- Formatting rules: edit `styles/gcc-thesis.sty` only when the school formatting requirement changes.

## Standard Workflow

1. Read `README.md`, `docs/format-checklist.md`, `main.tex`, `attachments.tex`, and `extraTex/meta.tex`.
2. Ask for or infer the missing thesis facts: title, student name, student ID, college, major class, supervisor, dates, keywords, references, and project content.
3. Update content files first. Avoid changing `styles/gcc-thesis.sty` unless the user explicitly asks for format work or the PDF clearly violates school rules.
4. Run `python3 scripts/check_structure.py`.
5. Run `python3 scripts/doctor.py`. If TeX tools are missing, report the missing environment and stop before pretending PDF validation passed.
6. If the environment is ready, run `bash scripts/build.sh`.
7. Inspect `main.pdf` and `attachments.pdf`, especially cover, statement, abstract, TOC, first body page, references, thanks, and attachment forms.
8. Fix formatting or content issues and recompile.

## Validation Rules

- No final claim of “fully compliant” without a successful PDF compile and visual inspection.
- If `xelatex` or `biber` is unavailable, say that only static checks were completed.
- Keep generated PDFs and LaTeX cache out of commits unless the user explicitly asks to publish release assets.
- For school Logo and official texts, keep the repository wording “unofficial” and preserve the license caveat in `README.md` and `NOTICE.md`.

## Build Commands

```bash
python3 scripts/check_structure.py
python3 scripts/doctor.py
bash scripts/build.sh main
bash scripts/build.sh attachments
bash scripts/build.sh all
```

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

