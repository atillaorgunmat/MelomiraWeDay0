#!/usr/bin/env bash
set -euo pipefail

python3 tools/graph_lint.py
python3 tools/bank_integrity_lint.py || true
