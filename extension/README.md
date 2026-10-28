# Extension: improved four-state certificate and numerical exploration

- `verify_improved.py`, `verify_five.py` (standard library only; print PASS): exact certificates for the
  improved four-state generator (cost 2.765997710528...) and five-state generator Q_5 (cost 2.746985402969...) at q=1/20.
- `core.py`, `v4_search.py`, `grid.sh`, `table.py`: multi-start SLSQP search over one-A,
  three-B exact realisations on the stratum p(S)1=0 (all patterns of up to three absent
  edge pairs); outputs `v4_q*.json` and Table 2 of the paper.
- `v5_search.py`: the same search with four B states at q=1/20; output `v5_q0.05.json`.
- `build_rational.py`: rounding of the numerical optimum to the rational Q_sharp.
- `opt.py`, `opt2.py`, `relax_*.txt`: minimisation constrained only by r, m and the first
  K derivatives of the dwell density at zero (Section 6, last paragraph).

All optimisation output is discovery evidence, not proof. Run the searches from this
directory with NumPy and SciPy available, e.g. `python3 v4_search.py 0.05 150 out.json`.
- `v5_interior.py`, `vn_interior.py`, `build5.py`, `Q5_rational.json`, `v5_interior_seed1.json`:
  five- and six-state interior searches and the rounding that produced Q_5.
