#!/usr/bin/env bash
set -euo pipefail

target="${1:-all}"

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

case "$target" in
  main)
    build_with_biber main
    ;;
  attachments)
    build_xelatex_only attachments
    ;;
  all)
    build_with_biber main
    build_xelatex_only attachments
    ;;
  *)
    echo "Usage: bash scripts/build.sh [main|attachments|all]" >&2
    exit 2
    ;;
esac
