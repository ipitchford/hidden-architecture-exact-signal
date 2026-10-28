# Assurance

Each row is a separate kind of assurance; no row implies another.

| Dimension | State | Evidence |
|---|---|---|
| Availability | Public GitHub release and Zenodo DOI 10.5281/zenodo.23721621 | Release assets, [SHA256SUMS](SHA256SUMS) |
| Written proofs | Complete proofs in the manuscript | `paper/manuscript.pdf`, Sections 2–5 and Appendices A–C |
| Exact certificates | Rational arithmetic, standard library | `code/exact_certificate.py` (practical four-state example), `extension/verify_improved.py`, `extension/verify_five.py`, `two_phase/verify_all_q_construction.py` |
| Supporting checks | Exact and high-precision | `two_phase/verify_two_phase.py`, `two_phase/audit_four_state.py`, `global_bound/boundary_checks.py`, `review/referee_checks.py` |
| Numerical results | Labelled as discovery evidence, not proof | `extension/` searches and JSON outputs; `exploration/` |
| Internal replay | Passed | `replay_all.py` reruns `code/reproduce.py` in a fresh temporary copy and compares every regenerated record and log ([REPLAY_RECEIPT.md](REPLAY_RECEIPT.md)) |
| Semantic negative controls | Passed | `negative_controls.py`: six corruptions (a rational rate in each of the three exact generators; an overstated saving or understated cost bound in each) must each be rejected |
| Optimised mode | Partial by design | The three self-checking certificates pass under `python -O`; `code/reproduce.py` refuses `-O` because some supporting checks use `assert` |
| Internal AI-assisted review | Done | Five simulated reviewer roles and an adversarial review by a different AI model, one revision round, a verification re-review, a targeted proof audit and a second different-model audit ([review/REVISION_RESPONSE.md](review/REVISION_RESPONSE.md)). This is not peer review. |
| Independent reproduction by an unaffiliated party | Not established | |
| Specialist (human) review | Not established | |
| Editorial peer review | Not established | |
| Formal verification | Not attempted | No proof assistant was used |
| Novelty | Bounded search only | [RESEARCH_GATES.json](RESEARCH_GATES.json), `literature/` |
| Citations | Every DOI resolved and its title matched | [CITATION_AUDIT.md](CITATION_AUDIT.md) |

## Scope and limits

* The fixed-statistics theorem constrains only (r, m, f_0); its approaching sequences change the full dwell law and are not exact-law sequences for P_q.
* Estimating f_0 from real data needs further assumptions (the missed-events problem); no statistical coverage or experimental calibration is given.
* A byte-identical replay shows that the shipped records are what the shipped programs produce. It does not by itself show that the programs implement the manuscript's definitions; that rests on the written proofs and the negative controls.
