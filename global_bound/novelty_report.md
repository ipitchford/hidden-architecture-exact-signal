# Bounded novelty audit: boundary density and exact three-statistic cost

Date: 26 October 2026. This report covers the additional derivation in `boundary_theorem.md`. It supplements the project's independent literature audit, which has additional searches and source comparisons.

## Frozen claim and outcome

The precise theorem is in `target.yaml`: exact minimum entropy production over all finite stationary binary-labelled CTMCs when only the entrance rate r, mean complete B dwell m, and density f_B(0) are fixed. For k=mf_B(0)<1 the infimum is `4r sqrt(1-k) atanh sqrt(1-k)`, is positive and unattained, and is approached by a fixed three-state family. For k>=1 the zero optimum is attained reversibly. This is not fixed-full-law nonattainment.

**Outcome by unit:**

- Log-sum stationary-flux merge: COLLISION / established method, attributed to Skinner--Dunkel (2021).
- Phase-type entrance density and occupation identities: classical Markov-chain calculations.
- Sharp affinity--Jeffreys comparison: standard symmetric-divergence territory; its exact historical origin has not been established. No novelty claim; complete Jensen proof included.
- Exact optimisation over `(r,m,f_B(0))`, including unattainment and sharp three-state sequence: BOUNDED UNCERTAINTY. No identical statement or construction was found in this search. An additional independent audit is in progress in the wider project.
- New use for the full-law benchmark: explicit consequence, reducing its all-architecture lower/upper ratio to at most 3/2 before higher-phase improvement; no sharp global-optimum claim.

## Exact query families executed

Routine and stronger search engines were both used. Queries (verbatim):

1. `"phase-type" "entropy production" minimum`
2. `"hidden" "dissipation" "attainment" phase type`
3. `"phase type" "reversible" "minimum" entropy`
4. `"minimum entropy production" "waiting time" "hidden" Markov`
5. `"phase-type" thermodynamic uncertainty entropy`
6. `"waiting time distributions" "optimal" "Skinner" "Dunkel"`
7. `"entropy production" "waiting time" "density at zero"`
8. `"entropy production" "Bhattacharyya" "waiting"`
9. `"entropy production" "initial" "dwell" "mean"`
10. `"Jeffreys" "Bhattacharyya" sharp bound`
11. `"entropy production" "waiting" "zero" "mean" "short-time"`
12. `"entropy production" "f(0)" waiting`
13. `"dissipation" "dwell" "initial density"`
14. `"entropy production" "arctanh" "waiting"`

The exact affinity identity and rational fast-mixing transform were additionally supplied to the project's independent literature agent for formula-level searches. These 14 queries are not an exhaustive census.

## Primary sources inspected and boundaries

1. Skinner, D. J., & Dunkel, J. (2021). *Estimating entropy production from waiting time distributions*. Physical Review Letters, 127, 198101. https://doi.org/10.1103/PhysRevLett.127.198101 ; primary full text https://arxiv.org/html/2105.08681v2 . Main Eqs. (3)--(4) formulate optimisations with complete dwell laws or low-order dwell moments; supplementary Lemma 2 supplies stationary-flux merging. The inspected text does not establish the new exact `(r,m,f0)` formula. The HTML rendering date is not its publication date.

2. Anonymous. (2026, October 3). *An architecture-independent dissipation floor for alternating-renewal observations* (Version 1.1) [Unrefereed research candidate]. Evidence Press. https://github.com/ipitchford/hidden-dissipation-floor/blob/main/PAPER.tex . Inspected complete main theorem, path-reversibilisation certificate, two-clock information projection, and zero-cost dichotomy. That work already proves a positive all-dimension floor and classifies zero cost in the renewal class. It does not give the exact boundary-statistics optimum derived here. Its general spectral zero-cost theorem is not claimed as new in this project.

3. Aznagulov, M. (2026). *Thermodynamic realizability of hidden Markov processes: Attainment, observable certificates, and the price of architecture* [Preprint]. https://arxiv.org/html/2609.14623v1 . Main architecture-price framework and exact benchmark inspected. The new fast-rate nonattainment at fixed statistics does not refute its fixed-complete-law attainment claim: f_B(0) is not continuous under the fast-rate law limit. The source's compactification theorem was not relied upon or independently re-audited here.

4. Nitzan, E. (2023). *Universal bounds on entropy production inferred from observed statistics* [Master's thesis, Tel Aviv University]. https://biskerlab.com/wp-content/uploads/2023/12/Universal-bounds-on-entropy-production-rate-inferred-from-observed-statistics.pdf . Introduction and optimisation scope inspected. This source studies fitted constraints on transition rates and waiting-time moments; no exact boundary-density formula identified in the inspected portions. The complete 66-page thesis was not line-by-line audited.

5. Sason, I. (2015). *Tight bounds for symmetric divergence measures and a refined bound for lossless source coding*. IEEE Transactions on Information Theory, 61(2), 701--707. https://doi.org/10.1109/TIT.2014.2387065 . Official author/institutional metadata and abstract identified, but one full-text retrieval timed out. It is a pointer to symmetric f-divergence theory, not used as a verified citation for the exact affinity inequality. In particular, a sharp total-variation bound cannot simply be substituted for a sharp affinity bound in the wrong direction.

## Claim language

Permitted: “We derive the exact optimum for these three prescribed statistics”; “no identical theorem was located in the bounded search”; “the methods use classical probability inequalities”.

Forbidden: “first”, “previously unknown”, “solves the all-architecture exact-law infimum”, or “experimental lower confidence bound”.

No author enquiry or external peer review was conducted. Negative search evidence is limited by indexing, terminology and inspected-source coverage.
