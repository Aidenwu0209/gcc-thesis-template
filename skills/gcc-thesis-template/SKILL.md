---
name: gcc-thesis-template
description: Use this skill when turning an idea into a Guangzhou College of Commerce thesis draft, or when formatting, migrating, compiling, or validating a thesis or attachment-material booklet with this repository.
---

# Guangzhou College of Commerce Thesis Template Skill

This skill turns `Aidenwu0209/gcc-thesis-template` into an Agent-led Vibe Writing workflow.

## When To Use

Use this skill when the user wants to:

- Fill or revise a Guangzhou College of Commerce undergraduate thesis.
- Turn a graduation-project idea into a thesis title, outline, evidence gap list, and TODO-marked draft.
- Coordinate vendored Orchestra Research Skills for research ideation, paper-writing support, academic plotting, research artifacts, and rigor review.
- Convert Word, Markdown, PDF, screenshots, or code-project notes into the template.
- Compile `main.pdf` or `attachments.pdf`.
- Check whether the thesis follows the school format.
- Repair LaTeX formatting, references, page numbering, cover fields, or attachment forms.
- Run an independent Agent review using `AGENT_REVIEW.md`.

## Workflow

1. Read `README.md`, `AGENTS.md`, `docs/format-checklist.md`, and `docs/compliance-audit.md`.
   - Treat the user's chat messages, uploaded files, explicit local paths, screenshots, code repositories, Word/Markdown drafts, and existing repository files as intake.
   - Do not require the user to fill a special intake file before starting.
   - If coordinating internal research-writing Skills, read `docs/agent-skills-workflow.md`, then select at most 1-3 relevant local Skill files under `skills/orchestra-research/AI-Research-SKILLs/`.
   - If handling installation or compilation setup, read `docs/setup.md`.
2. Inspect `extraTex/meta.tex` and update all available student, title, date, and keyword fields.
3. Put content in the correct layer:
   - `extraTex/front/` for statements and abstracts.
   - `extraTex/body/` for thesis chapters.
   - `extraTex/back/` for appendix, bibliography, and thanks.
   - `extraTex/attachments/` for task/proposal/progress/defense/score forms.
4. Keep school-format logic in `styles/gcc-thesis.sty`; edit it only for format changes.
5. Run:

```bash
python3 scripts/check_structure.py
python3 scripts/doctor.py
```

6. If the environment is ready, compile:

```bash
bash scripts/build.sh all
```

7. Inspect both generated PDFs. Check at least:
   - Cover page.
   - Originality statement and copyright authorization.
   - Chinese abstract, English abstract, and TOC.
   - First body page.
   - Figure/table captions.
   - References and thanks.
   - Attachment forms.

## Rules

- Do not claim full compliance unless PDF compilation and visual inspection both succeeded.
- Do not fabricate experiments, screenshots, user research, references, signatures, dates, or implemented features. Mark missing evidence as TODO.
- If `scripts/doctor.py` fails, report the missing TeX tool or package.
- Do not commit generated PDFs or LaTeX cache unless explicitly asked.
- Preserve the unofficial-template disclaimer and license caveat.
- Keep the student-facing source files easy to edit; avoid hiding thesis content inside style macros.
- If the user asks for review/audit rather than editing, read `AGENT_REVIEW.md` and produce findings first.
