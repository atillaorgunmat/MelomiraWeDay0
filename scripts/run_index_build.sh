#!/usr/bin/env bash
set -euo pipefail
python3 tools/build_question_index.py --qdir q --graph graph/questions.yaml --out dist
python3 tools/validate_question_chain.py --qdir q --graph graph/questions.yaml
