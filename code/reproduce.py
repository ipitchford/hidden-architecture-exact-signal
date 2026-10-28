#!/usr/bin/env python3
"""Reproduce analytic-support certificates; optionally rebuild figures/PDF."""
import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--figures',action='store_true',help='Rebuild the three scientific figures (NumPy/SciPy/Matplotlib).')
parser.add_argument('--pdf',action='store_true',help='Rebuild manuscript with pdflatex, using existing figures.')
args=parser.parse_args()
if not __debug__:
    raise RuntimeError('Run verification without Python -O.')
logs=ROOT/'results'/'reproduction_logs';logs.mkdir(parents=True,exist_ok=True)
checks=['code/exact_certificate.py','two_phase/verify_two_phase.py',
        'two_phase/audit_four_state.py','two_phase/verify_all_q_construction.py',
        'global_bound/boundary_checks.py','extension/verify_improved.py','extension/verify_five.py']
if (ROOT/'review'/'referee_checks.py').exists():
    checks.append('review/referee_checks.py')
results=[]
for relative in checks:
    source=ROOT/relative;started=time.monotonic()
    result=subprocess.run([sys.executable,str(source)],cwd=ROOT,capture_output=True,text=True)
    log=logs/(source.stem+'.txt');log.write_text(result.stdout+result.stderr)
    record={'script':relative,'exit_code':result.returncode,
            'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'seconds':round(time.monotonic()-started,3),
            'log':str(log.relative_to(ROOT))}
    results.append(record)
    print(relative+': '+('PASS' if result.returncode==0 else 'FAIL'),flush=True)
    if result.returncode:
        raise RuntimeError('Verification failed; inspect '+str(log))
if args.figures:
    subprocess.run([sys.executable,str(ROOT/'code'/'make_figures.py')],cwd=ROOT,check=True)
    subprocess.run([sys.executable,str(ROOT/'code'/'make_networks.py')],cwd=ROOT,check=True)
if args.pdf:
    if not shutil.which('pdflatex'):
        raise RuntimeError('pdflatex is required for --pdf')
    for n in range(1,4):
        result=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','manuscript.tex'],cwd=ROOT/'paper',capture_output=True,text=True)
        (logs/f'latex_pass_{n}.txt').write_text(result.stdout+result.stderr)
        if result.returncode:
            raise RuntimeError('LaTeX build failed; inspect reproduction log')
out={'status':'PASS','python':platform.python_version(),'checks':results,
     'claims':'Computations support the written analytic proofs; finite parameter checks are not the universal proof.',
     'optional_figures_rebuilt':args.figures,'optional_pdf_rebuilt':args.pdf}
for package in ['numpy','scipy','matplotlib']:
    try:out[package]=importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:pass
(ROOT/'results'/'reproduction_summary.json').write_text(json.dumps(out,indent=2)+'\n')
print('All requested reproduction steps passed.',flush=True)
