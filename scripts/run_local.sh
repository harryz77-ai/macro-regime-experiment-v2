#!/usr/bin/env bash
set -euo pipefail
python -m unittest discover -s tests -p 'test_*.py'
python runner.py \
  --previous-regime auto \
  --output reports/latest.md \
  --json-output data/latest.json \
  --history-csv data/history.csv \
  --start 2020-01-01 \
  --period 5y
