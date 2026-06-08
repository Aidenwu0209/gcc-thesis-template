#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
import sys
from dataclasses import dataclass


COMMANDS = ["xelatex", "biber", "kpsewhich"]

TEX_FILES = [
    "ctexbook.cls",
    "FandolSong-Regular.otf",
    "fontspec.sty",
    "xeCJK.sty",
    "geometry.sty",
    "setspace.sty",
    "graphicx.sty",
    "xcolor.sty",
    "array.sty",
    "fancyhdr.sty",
    "titlesec.sty",
    "titletoc.sty",
    "enumitem.sty",
    "caption.sty",
    "booktabs.sty",
    "longtable.sty",
    "tabularx.sty",
    "multirow.sty",
    "verbatim.sty",
    "indentfirst.sty",
    "etoolbox.sty",
    "amsmath.sty",
    "amssymb.sty",
    "hyperref.sty",
    "biblatex.sty",
    "gb7714-2015.bbx",
]


@dataclass
class Check:
    name: str
    ok: bool
    detail: str


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def check_command(command: str) -> Check:
    path = shutil.which(command)
    if path:
        return Check(command, True, path)
    return Check(command, False, "not found in PATH")


def check_tex_file(filename: str) -> Check:
    kpsewhich = shutil.which("kpsewhich")
    if not kpsewhich:
        return Check(filename, False, "kpsewhich is unavailable")
    proc = run([kpsewhich, filename])
    path = proc.stdout.strip()
    if proc.returncode == 0 and path:
        return Check(filename, True, path)
    return Check(filename, False, "not found by kpsewhich")


def print_install_hints() -> None:
    print("\nInstall hints:")
    print("  macOS full install:   brew install --cask mactex")
    print("  macOS small install:  brew install --cask basictex && sudo tlmgr update --self")
    print("  Ubuntu/Debian:        sudo apt install texlive-xetex texlive-lang-chinese texlive-latex-recommended texlive-latex-extra texlive-bibtex-extra biber latexmk")
    print("  TeX Live tlmgr:       tlmgr install ctex fandol fontspec xecjk geometry setspace fancyhdr titlesec titletoc enumitem caption booktabs tools multirow graphics xcolor indentfirst etoolbox amsmath amsfonts hyperref biblatex biblatex-gb7714-2015 biber")
    print("  Windows:              install TeX Live or MiKTeX, then ensure xelatex and biber are in PATH")


def main() -> int:
    checks: list[Check] = []
    checks.extend(check_command(command) for command in COMMANDS)

    if shutil.which("kpsewhich"):
        checks.extend(check_tex_file(filename) for filename in TEX_FILES)

    width = max(len(check.name) for check in checks)
    failures = [check for check in checks if not check.ok]

    for check in checks:
        status = "OK" if check.ok else "MISS"
        print(f"{status:<4} {check.name:<{width}}  {check.detail}")

    if failures:
        print_install_hints()
        print(f"\nEnvironment check failed: {len(failures)} missing item(s).")
        return 1

    print("\nEnvironment check passed. You can run: bash scripts/build.sh")
    return 0


if __name__ == "__main__":
    sys.exit(main())
