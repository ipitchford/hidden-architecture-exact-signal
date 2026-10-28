#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Semantic negative controls for the exact certificates.

Each control copies the package to a temporary directory, applies one plausible
corruption to a certificate script (a wrong rational rate, or an overstated
claimed bound) and requires that script to FAIL. Each unmodified script must
PASS first. Standard library only. Exit status 0 means every corruption was
rejected.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTROLS = [
    ('practical Q_* rate perturbed', 'code/exact_certificate.py', 'F(4781,4800)', 'F(4782,4800)'),
    ('practical Q_* saving overstated', 'code/exact_certificate.py', 'F(72869002,10**9)', 'F(82869002,10**9)'),
    ('improved Q_sharp rate perturbed', 'extension/verify_improved.py', 'F(483,20000)', 'F(484,20000)'),
    ('improved Q_sharp cost understated', 'extension/verify_improved.py', 'hi<F(27670,10000)', 'hi<F(27650,10000)'),
    ('five-state Q_5 rate perturbed', 'extension/verify_five.py', 'F(1113,80000)', 'F(1114,80000)'),
    ('five-state Q_5 cost understated', 'extension/verify_five.py', 'hi<F(27659977,10**7)', 'hi<F(27459977,10**7)'),
]


def run(root, rel):
    return subprocess.run([sys.executable, '-B', str(root / rel)], cwd=root,
                          capture_output=True, text=True).returncode


def main():
    bad = []
    with tempfile.TemporaryDirectory() as tmp:
        for k, (name, rel, old, new) in enumerate(CONTROLS):
            root = Path(tmp) / f'c{k}'
            shutil.copytree(HERE, root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            if run(root, rel) != 0:
                print(f'FAIL: unmodified {rel} not accepted'); bad.append(f'baseline {rel}'); continue
            src = (root / rel).read_text()
            if src.count(old) != 1:
                print(f'FAIL: corruption site for {name} not unique'); bad.append(name); continue
            (root / rel).write_text(src.replace(old, new))
            rejected = run(root, rel) != 0
            print(f'{"PASS" if rejected else "FAIL"}: {name} rejected')
            if not rejected:
                bad.append(name)
    print('ALL NEGATIVE CONTROLS PASSED' if not bad else f'NEGATIVE CONTROLS FAILED: {bad}')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
