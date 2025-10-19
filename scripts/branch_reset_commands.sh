#!/usr/bin/env bash
set -euo pipefail

BASE="origin/pack/P-FND-0001"
BR="bank-reset/v4.5.2"

git fetch origin
git checkout -B "$BR" "$BASE"

# Archive current q-files if present
if [ -d q ]; then
  mkdir -p docs/PARKED
  ts=$(date +%Y%m%d-%H%M%S)
  git mv -f q "docs/PARKED/q-archive-$ts" || true
fi

# Expect the kit to be unzipped at repo root beforehand:
#   unzip -o ~/Downloads/fresh-start-kit-v4.5.2.zip -d .

git add -A docs/FOUNDATIONS/QUESTION_BANK.md graph/questions.yaml docs/TRACE/trace_map.yaml
git commit -m "v4.5.2: reset bank/graph/trace (archive legacy q/* under docs/PARKED)"
git push -u origin "$BR"
git diff --name-status origin/pack/P-FND-0001..origin/"$BR"
echo "Open PR: base=pack/P-FND-0001, head=$BR"
