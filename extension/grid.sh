#!/bin/bash
cd "$(dirname "$0")" || exit 1
for q in 0.05 0.01 0.1 0.2 0.3 0.5 0.7 0.9; do echo $q; done | xargs -P 4 -I{} sh -c 'uv run --with numpy --with scipy python3 -I v4_search.py {} 150 v4_q{}.json > log_q{}.txt 2>&1'
