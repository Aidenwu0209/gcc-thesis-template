#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

required_files = [
    "main.tex",
    "attachments.tex",
    "styles/gcc-thesis.sty",
    "extraTex/@config.tex",
    "extraTex/meta.tex",
    "extraTex/front/statement.tex",
    "extraTex/front/abstract_zh.tex",
    "extraTex/front/abstract_en.tex",
    "extraTex/body/chapter-01.tex",
    "extraTex/body/chapter-02.tex",
    "extraTex/body/chapter-03.tex",
    "extraTex/body/chapter-04.tex",
    "extraTex/back/appendix.tex",
    "extraTex/back/references.bib",
    "extraTex/back/thanks.tex",
    "extraTex/attachments/catalog.tex",
    "extraTex/attachments/task_book.tex",
    "extraTex/attachments/proposal.tex",
    "extraTex/attachments/progress_record.tex",
    "extraTex/attachments/defense_record.tex",
    "extraTex/attachments/score_sheet.tex",
    "assets/branding/gcc_logo.png",
    "README.md",
    "AGENTS.md",
    "AGENT_REVIEW.md",
    "docs/idea-to-thesis-workflow.md",
    "docs/agent-skills-workflow.md",
    "docs/setup.md",
    "docs/format-checklist.md",
    "docs/compliance-audit.md",
    "LICENSE",
    "scripts/doctor.py",
    "skills/gcc-thesis-template/SKILL.md",
    "skills/orchestra-research/README.md",
    "skills/orchestra-research/AI-Research-SKILLs/LICENSE",
    "skills/orchestra-research/AI-Research-SKILLs/20-ml-paper-writing/ml-paper-writing/SKILL.md",
    "skills/orchestra-research/AI-Research-SKILLs/20-ml-paper-writing/academic-plotting/SKILL.md",
    "skills/orchestra-research/AI-Research-SKILLs/20-ml-paper-writing/systems-paper-writing/SKILL.md",
    "skills/orchestra-research/AI-Research-SKILLs/21-research-ideation/brainstorming-research-ideas/SKILL.md",
    "skills/orchestra-research/AI-Research-SKILLs/21-research-ideation/creative-thinking-for-research/SKILL.md",
    "skills/orchestra-research/AI-Research-SKILLs/22-agent-native-research-artifact/compiler/SKILL.md",
    "skills/orchestra-research/AI-Research-SKILLs/22-agent-native-research-artifact/research-manager/SKILL.md",
    "skills/orchestra-research/AI-Research-SKILLs/22-agent-native-research-artifact/rigor-reviewer/SKILL.md",
]

required_style_markers = [
    "top=2.5cm",
    "bottom=2.5cm",
    "left=2cm",
    "right=2cm",
    "bindingoffset=0.5cm",
    "style=gb7714-2015",
    "\\pagenumbering{Roman}",
    "\\pagenumbering{arabic}",
]

missing = [path for path in required_files if not (ROOT / path).exists()]
if missing:
    print("Missing required files:")
    for path in missing:
        print(f"  - {path}")
    sys.exit(1)

combined = "\n".join((ROOT / path).read_text(encoding="utf-8") for path in [
    "main.tex",
    "attachments.tex",
    "styles/gcc-thesis.sty",
    "extraTex/@config.tex",
])

missing_markers = [marker for marker in required_style_markers if marker not in combined]
if missing_markers:
    print("Missing required style markers:")
    for marker in missing_markers:
        print(f"  - {marker}")
    sys.exit(1)

print("Structure check passed.")
