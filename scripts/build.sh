#!/usr/bin/env bash
set -euo pipefail

build_with_biber() {
  local job="$1"
  xelatex -interaction=nonstopmode "${job}.tex"
  biber "$job"
  xelatex -interaction=nonstopmode "${job}.tex"
  xelatex -interaction=nonstopmode "${job}.tex"
}

build_xelatex_only() {
  local job="$1"
  xelatex -interaction=nonstopmode "${job}.tex"
  xelatex -interaction=nonstopmode "${job}.tex"
}

build_with_biber main
build_xelatex_only attachments
