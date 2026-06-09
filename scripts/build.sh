#!/usr/bin/env bash
set -euo pipefail

target="${1:-main}"

build_with_biber() {
  local job="$1"
  xelatex -interaction=nonstopmode "${job}.tex"
  biber "$job"
  xelatex -interaction=nonstopmode "${job}.tex"
  xelatex -interaction=nonstopmode "${job}.tex"
}

clean_job() {
  local job="$1"
  rm -f "${job}".{aux,bbl,bcf,blg,log,out,run.xml,toc}
}

case "$target" in
  main)
    build_with_biber main
    ;;
  attachments)
    build_with_biber attachments
    ;;
  all)
    build_with_biber main
    build_with_biber attachments
    ;;
  clean)
    clean_job main
    clean_job attachments
    ;;
  *)
    echo "Usage: bash scripts/build.sh [main|attachments|all|clean]" >&2
    exit 2
    ;;
esac
