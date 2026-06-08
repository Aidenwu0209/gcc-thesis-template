# LaTeX 环境、编译和排错

本页记录 `gcc-thesis-template` 的本地环境安装、编译命令和常见排错。只想看工作流时，先读 [README.md](../README.md)。

## 最小要求

- TeX Live / MacTeX / MiKTeX
- XeLaTeX
- Biber
- Python 3

关键 LaTeX 包：

```text
ctex
fandol
fontspec
xeCJK
geometry
setspace
graphicx
xcolor
array
fancyhdr
titlesec
titletoc
enumitem
caption
booktabs
longtable
tabularx
multirow
verbatim
indentfirst
etoolbox
amsmath
amssymb
hyperref
biblatex
biblatex-gb7714-2015
```

检查环境：

```bash
python3 scripts/doctor.py
```

## macOS

完整安装，最省心：

```bash
brew install --cask mactex
```

MacTeX 体积较大，但最不容易缺包。

轻量安装：

```bash
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install \
  ctex fandol fontspec xecjk geometry setspace fancyhdr titlesec titletoc enumitem \
  caption booktabs tools multirow graphics xcolor indentfirst etoolbox \
  amsmath amsfonts hyperref biblatex biblatex-gb7714-2015 biber latexmk
```

BasicTeX 体积小，但如果后续编译提示缺包，需要继续用 `tlmgr install <包名>` 补装。

安装后如果命令行找不到 `xelatex`，重开终端，或确认 `/Library/TeX/texbin` 已加入 `PATH`。

## Ubuntu / Debian / WSL

```bash
sudo apt update
sudo apt install texlive-xetex texlive-lang-chinese texlive-latex-recommended texlive-latex-extra texlive-bibtex-extra biber latexmk
```

## Windows

推荐安装 TeX Live 或 MiKTeX，并确保 `xelatex` 与 `biber` 在 PowerShell / CMD 的 `PATH` 中可用。

安装后检查：

```powershell
xelatex --version
biber --version
python scripts/doctor.py
```

## Overleaf

可以上传本仓库 zip 到 Overleaf，编译器选择 **XeLaTeX**。

- 正文入口选择 `main.tex`。
- 附件材料册入口选择 `attachments.tex`。
- 如果参考文献没有自动刷新，手动 Recompile 两到三次，或检查 Overleaf 是否启用了 Biber。

## 编译命令

推荐使用脚本：

```bash
bash scripts/build.sh all
```

只编正文或附件：

```bash
bash scripts/build.sh main
bash scripts/build.sh attachments
```

手动编译正文：

```bash
xelatex -interaction=nonstopmode main.tex
biber main
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

手动编译附件：

```bash
xelatex -interaction=nonstopmode attachments.tex
xelatex -interaction=nonstopmode attachments.tex
```

## VS Code / LaTeX Workshop

用 VS Code 打开：

```text
gcc-thesis-template.code-workspace
```

LaTeX Workshop 中提供三个 recipe：

- `gcc-thesis-template`：编译正文和附件。
- `gcc-main-only`：只编译 `main.tex`。
- `gcc-attachments-only`：只编译 `attachments.tex`。

使用前需要先安装 VS Code 扩展 LaTeX Workshop，并确保本机命令行可以运行 `xelatex` 和 `biber`。

## 常见问题

### `xelatex`、`biber` 或 `kpsewhich` not found

说明本机 TeX 工具链还没有安装，或安装后没有进入 `PATH`。先按本页对应系统安装，再重新打开终端。

### 缺少某个 `.sty`

如果使用 BasicTeX，运行：

```bash
sudo tlmgr install <包名>
```

然后重新运行：

```bash
python3 scripts/doctor.py
```

### 参考文献没有出现

正文需要至少经过：

```bash
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

推荐直接使用：

```bash
bash scripts/build.sh main
```

### 不能宣称完全合规

如果只通过了源码检查，没有成功生成 PDF 并逐页检查，就只能说“静态检查通过”或“已按学校要求实现到可编译检查阶段”，不能说“完全符合学校要求”。
