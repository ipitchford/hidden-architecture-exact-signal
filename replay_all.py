#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Replay every exact certificate and check from a fresh temporary copy of this
package (code/reproduce.py) and compare the regenerated records with the
shipped ones. Timing and interpreter fields are excluded from the comparison.
Standard library only. Exit status 0 means every record was reproduced.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECORDS = ['results/exact_certificate.json', 'two_phase/two_phase_checks.json',
           'two_phase/four_state_audit.json', 'two_phase/all_q_checks.json',
           'global_bound/boundary_checks.json', 'review/referee_checks.json']
LOGS = ['exact_certificate', 'verify_improved', 'verify_five', 'verify_two_phase',
        'audit_four_state', 'verify_all_q_construction', 'boundary_checks', 'referee_checks']
VOLATILE = {'seconds', 'python', 'platform', 'elapsed', 'timestamp'}


def strip(x):
    if isinstance(x, dict):
        return {k: strip(v) for k, v in x.items() if k not in VOLATILE}
    if isinstance(x, list):
        return [strip(v) for v in x]
    return x


def main():
    bad = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / 'pkg'
        shutil.copytree(HERE, root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        r = subprocess.run([sys.executable, '-B', str(root / 'code' / 'reproduce.py')], cwd=root,
                           capture_output=True, text=True)
        print(r.stdout.strip())
        if r.returncode:
            print(r.stderr[-2000:])
            bad.append('reproduce.py failed')
        for rec in RECORDS:
            a = strip(json.loads((HERE / rec).read_text()))
            b = strip(json.loads((root / rec).read_text()))
            same = a == b
            print(f'{"PASS" if same else "FAIL"}: {rec} reproduced')
            if not same:
                bad.append(rec)
        for name in LOGS:
            a = (HERE / 'results' / 'reproduction_logs' / f'{name}.txt').read_text()
            b = (root / 'results' / 'reproduction_logs' / f'{name}.txt').read_text()
            same = a == b
            print(f'{"PASS" if same else "FAIL"}: {name} output identical')
            if not same:
                bad.append(name)
    print('REPLAY PASSED' if not bad else f'REPLAY FAILED: {bad}')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
