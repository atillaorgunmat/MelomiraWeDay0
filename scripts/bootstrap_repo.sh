#!/usr/bin/env bash
set -euo pipefail

: "${REPO_URL:?Usage: REPO_URL=https://github.com/<user>/MelomiraWeDay0 ./scripts/bootstrap_repo.sh}"

git init
git checkout -b pack/P-FND-0001
git add .
git commit -m "init: MelomiraWeDay0 Day-0 skeleton per solo governance (Option A)"
git remote add origin "$REPO_URL" || true
git push -u origin pack/P-FND-0001
