# Agent navigation

## Identity

- Release slug: `hidden-architecture-exact-signal`. Version `1.0.0-candidate`, tag `v1.0.0-candidate`.
- DOI 10.5281/zenodo.23721621; concept DOI 10.5281/zenodo.23721620.
- Repository: https://github.com/ipitchford/hidden-architecture-exact-signal
- Release page: https://evidencepress.org/releases/hidden-architecture-exact-signal/
- Scholarly creator: Anonymous. Status: unrefereed candidate ([STATUS.md](STATUS.md)).
- Manuscript: [PDF](paper/manuscript.pdf) (20 pages) and [LaTeX source](paper/manuscript.tex). Figures: [paper/figures/](paper/figures/).
- Overview and claims: [README.md](README.md), [CLAIMS.json](CLAIMS.json), [ASSURANCE.md](ASSURANCE.md), [review/REVISION_RESPONSE.md](review/REVISION_RESPONSE.md) (public review record).
- Sources and provenance: [PROVENANCE.md](PROVENANCE.md), [SOURCES.md](SOURCES.md), [CITATION_AUDIT.md](CITATION_AUDIT.md), [RESEARCH_GATES.json](RESEARCH_GATES.json), [literature/novelty_report.md](literature/novelty_report.md).
- Citation and licences: [CITATION.cff](CITATION.cff), [.zenodo.json](.zenodo.json), [LICENSES.md](LICENSES.md), [PUBLIC_DOMAIN.md](PUBLIC_DOMAIN.md).

## Scientific map

**Setting.** A continuous-time Markov chain on hidden states, each labelled A or B, is watched only through its label. P_q (0 < q < 1) is the stationary alternating-renewal law with A dwell Exp(1+q) and B dwell transform [(2q/(1+q))z + 1+q+q²]/[z² + 2(1+q)z + 1+q+q²]. V_n(P) is the least entropy-production rate over n-state realisations of the complete law P; V_∞ is the infimum over all finite sizes.

**Results.**
- Three states are minimal and V_3(P_q) = (1−q) log(1/q), uniquely attained by the driven ring. Theorem 1, **proved**; checks [two_phase/verify_two_phase.py](two_phase/verify_two_phase.py), scope lemma in Appendix A.
- V_4(P_q) < V_3(P_q) for every q. Theorem 1, **proved**; explicit construction checked by [two_phase/verify_all_q_construction.py](two_phase/verify_all_q_construction.py).
- At q = 1/20: rational Q_* with σ = 2.7730766578… ([code/exact_certificate.py](code/exact_certificate.py)), improved four-state 2.7659977105… ([extension/verify_improved.py](extension/verify_improved.py)), five-state 2.7469854029… ([extension/verify_five.py](extension/verify_five.py)); all **exact certificates**, below V_3 = 2.8459456598….
- Short-dwell bound σ > 4r√(1−k) artanh√(1−k), k = m f_0 < 1, any finite architecture, no renewal assumption. Theorem 2, **proved**; checks [global_bound/boundary_checks.py](global_bound/boundary_checks.py).
- That bound is the exact infimum under fixed (r, m, f_0) and is not attained; zero is attained for k ≥ 1. Theorem 5, **proved**; notes [global_bound/boundary_theorem.md](global_bound/boundary_theorem.md).
- Bracket (2/3)(1−q) log(1/q) ≤ V_∞ ≤ V_4 < V_3; at q = 1/20 the floor 1.8973 is about 108× the earlier Evidence Press floor (doi:10.5281/zenodo.23118474). Corollary 4, **proved**.
- V_4(P_{1/20}) ≈ 2.765996 and a fifth state helps: **numerical only**, [extension/README.md](extension/README.md).

**Do not read:**
- the four-state examples as optima (V_4 and V_∞ are open);
- the fixed-statistics sharpness sequences as exact-law sequences for P_q;
- any result as an experimental estimate or with statistical coverage;
- internal AI-assisted review as peer review.

## Code and replay

All certificates use the Python standard library and run in seconds. [replay_all.py](replay_all.py) reruns [code/reproduce.py](code/reproduce.py) in a fresh temporary copy and compares every record and log; [negative_controls.py](negative_controls.py) applies six corruptions that must each be rejected. Results: [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md), [results/](results/). CI: [.github/workflows/replay.yml](.github/workflows/replay.yml).

## Useful next research question

Certify V_4(P_{1/20}) (numerically about 2.765996), and decide whether V_∞(P_q) is attained by a finite model under the fixed complete law (Section 7).
