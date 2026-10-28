# Replay receipt

Producer-side replay for 1.0.0-candidate, 28 October 2026, macOS (Apple silicon), Python 3.11.14 via `uv run python3 -I -B`.

| Command | Result |
|---|---|
| `python3 -I -B replay_all.py` | PASS: all eight checks in `code/reproduce.py` pass in a fresh temporary copy; six result JSON records and eight check logs regenerated identically (timing and interpreter fields excluded) |
| `python3 -I -B negative_controls.py` | PASS: six corruptions rejected, each after its unmodified certificate passed |
| `python3 -I -B -O` on `code/exact_certificate.py`, `extension/verify_improved.py`, `extension/verify_five.py` | PASS |
| `pdflatex` (three passes) of `paper/manuscript.tex` | 20 pages, no undefined references |

The publisher also replayed the frozen archive from a fresh extraction before tagging; GitHub Actions repeats the replay, negative controls and optimised-mode checks on every push. This is producer replay, not independent reproduction.
