# Status

Version 1.0.0-candidate (28 October 2026). DOI [10.5281/zenodo.23721621](https://doi.org/10.5281/zenodo.23721621) (concept DOI [10.5281/zenodo.23721620](https://doi.org/10.5281/zenodo.23721620)). Scholarly creator: Anonymous.

**This is an unrefereed research candidate.** No journal and no named human specialist has reviewed it. The only checking was internal and AI-assisted (see [review/REVISION_RESPONSE.md](review/REVISION_RESPONSE.md)). That is not peer review, independent reproduction or formal verification.

**Question.** If a two-level stochastic signal is known exactly, does the smallest hidden Markov model that reproduces it also give the least possible dissipation (entropy production)?

**Answer.** No. For the binary alternating-renewal family P_q (0 < q < 1) studied in `paper/manuscript.pdf`:

* **Proved in writing, with exact rational checks**
  * Three hidden states are the fewest that realise P_q, and the exact three-state minimum is V_3(P_q) = (1−q) log(1/q), attained uniquely (up to B-state exchange) by the homogeneous driven ring. The bound extends to any number of A states with at most two B states.
  * For every 0 < q < 1 an explicit finite four-state realisation of the complete stationary observed law dissipates strictly less: V_4(P_q) < V_3(P_q). Rational q gives rational rates.
  * Over all finite hidden architectures matching only the entrance intensity r, mean complete B dwell m and initial dwell density f_0, the exact entropy infimum is 4r√(1−m f_0) artanh√(1−m f_0) when 0 < m f_0 < 1. No finite model attains it; three-state models approach it. When m f_0 ≥ 1 a reversible model with at most three states attains zero.
  * Hence (2/3)(1−q) log(1/q) ≤ V_∞(P_q) ≤ V_4(P_q) < V_3(P_q). At q = 1/20 the floor 1.8973 is about 108 times the floor certified for this benchmark in the earlier Evidence Press candidate (DOI 10.5281/zenodo.23118474).
* **Exact rational certificates at q = 1/20**: a simple four-state example with cost 2.7730766578…, an improved four-state example 2.7659977105… and a five-state example 2.7469854029…, all below the three-state minimum 2.8459456598….
* **Numerical exploration only (not proof)**: the four-state optimum at q = 1/20 is about 2.765996, and a fifth state lowers the cost further (Section 6 of the paper; `extension/`).
* **Open**: the exact values of V_4(P_q) and V_∞(P_q), and whether a finite model attains V_∞ under the fixed complete law.

**What is not claimed.** Any four-state or unrestricted optimum; any experimental estimate or statistical coverage; historical priority (the literature search was bounded).
