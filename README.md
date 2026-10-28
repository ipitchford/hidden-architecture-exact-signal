# Hidden architecture and the thermodynamic cost of an exact stochastic signal

Evidence Press research candidate, version 1.0.0-candidate (28 October 2026). Author: Anonymous.
DOI [10.5281/zenodo.23721621](https://doi.org/10.5281/zenodo.23721621) (concept DOI
[10.5281/zenodo.23721620](https://doi.org/10.5281/zenodo.23721620)). Repository:
<https://github.com/ipitchford/hidden-architecture-exact-signal>. Release page:
<https://evidencepress.org/releases/hidden-architecture-exact-signal/>.
**Status: unrefereed candidate; internal AI-assisted review only** (see [STATUS.md](STATUS.md)).
Agents start at [AI_INDEX.md](AI_INDEX.md).
Read `paper/manuscript.pdf` for the complete stand-alone paper.

## The question in one paragraph

Experiments often see only a coarse two-level signal (a channel open or shut, a motor bound
or unbound) produced by a hidden Markov network of unknown size. A common way to bound the
network's dissipation is to fit the smallest hidden model that reproduces the signal and
minimise entropy production over it. This paper shows, with an exact example, that the
smallest model can overstate the least possible dissipation: a four-state mechanism can
produce exactly the same signal as every three-state mechanism while dissipating strictly
less. It also gives a sharp lower bound that holds for hidden networks of any size.

## Results

For the binary alternating-renewal family with A dwell Exp(1+q) and B dwell transform

`[(2q/(1+q))z + 1+q+q²] / [z² + 2(1+q)z + 1+q+q²]`, 0<q<1,

the paper proves:

1. Three states are the fewest that can produce the signal, and the exact global three-state
   entropy minimum is `(1−q) log(1/q)`, uniquely attained by the homogeneous driven ring up to
   B-state exchange. The bound extends to any number of A states with at most two B states.
2. For **every** 0<q<1, an explicit finite four-state model reproduces the complete stationary
   observed law and dissipates strictly less. Rational q admits rational rates.
3. At q=1/20 a simple rational four-state example has certified cost `2.7730766578…`, an
   improved four-state example `2.7659977105…`, and a rational five-state example
   `2.7469854029…`, all below the three-state minimum `2.8459456598…`.
4. Over **all** finite hidden architectures matching only the stationary entrance intensity r,
   mean complete B dwell m and initial dwell density f0, the exact entropy infimum is
   `4r sqrt(1−m f0) atanh(sqrt(1−m f0))` when 0<m f0<1. No finite model attains this positive
   value, but three-state models approach it. When m f0≥1, a reversible model with at most three
   states attains zero.
5. For the fixed complete law, `(2/3)(1−q) log(1/q) ≤ V∞(Pq) ≤ V4(Pq) < V3(Pq)`. At q=1/20 the
   floor 1.8973 is about 108 times the earlier certified floor for this benchmark.

Numerical exploration (discovery evidence, not proof; Section 6 of the paper) puts the
four-state optimum at q=1/20 at about 2.765996, within 2×10⁻⁶ of the improved rational model,
and indicates that a fifth state lowers the cost further.
The exact values of V4 and V∞, and finite attainment of V∞ under a fixed complete law, remain
open.

## Reproduce

The mathematical certificates use Python 3.11 or later and its standard library:

```bash
python3 code/reproduce.py
```

To replay everything from a fresh temporary copy and compare the regenerated records with the
shipped ones, then run six semantic negative controls (standard library only):

```bash
python3 -I -B replay_all.py
python3 -I -B negative_controls.py
```

Rebuild the figures and PDF when NumPy, SciPy, Matplotlib and a LaTeX installation with
`pdflatex` are available:

```bash
python3 code/reproduce.py --figures --pdf
```

Do not use `python -O` for the whole suite: some independent checks deliberately use
assertions and reject optimisation mode. The central `code/exact_certificate.py` and
`extension/verify_improved.py` also work with `-O`, because their checks explicitly raise or
print failures.

## Contents

- `paper/manuscript.tex`, `paper/manuscript.pdf`: authoritative complete paper.
- `paper/figures/`: vector PDF and PNG figures; `code/make_networks.py` draws Figure 1.
- `code/`: exact certificate, reproduction driver and figure scripts.
- `results/`: exact certificate output, figure values, reproduction record and logs.
- `two_phase/`: proof notes and exact/high-precision checks for the three-state minimum and
  the all-q construction.
- `global_bound/`: the sharp three-statistic theorem and its checks.
- `extension/`: exact certificates for the improved four-state and the five-state rational
  models, the numerical search code and its JSON outputs.

- `literature/`: bounded primary-source novelty audit, recorded queries and fingerprints.
- `audit/`: frozen initial target, claim map and provenance record.
- `review/`: independent mathematical checks and the public review record
  (`REVISION_RESPONSE.md`).
- `exploration/`: earlier discovery calculations, including unsuccessful optimiser runs.

## Provenance and licence

The manuscript, derivations and checks were developed with AI assistance. Internal review was
AI-assisted and is not external peer review or independent human reproduction. A bounded
literature search does not establish historical priority. Text and figures are released under
CC0-1.0; code under the MIT licence.
