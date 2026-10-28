# Review record and revision response (version 1.0 release)

This file is the public record of the internal review round carried out before release.
It keeps every substantive objection and how it was handled. The reviews were AI-assisted:
five simulated reviewer roles (editor, methodology, domain, cross-disciplinary perspective,
devil's advocate) plus one adversarial mathematical review by a different AI model. They are
internal checking, not external peer review, and agreement between models is not proof.

## What the reviewers checked and found

- **Correctness.** No reviewer found a mathematical error. The rational four-state generator,
  its stationary vector, the annihilator identity, the dwell transform and the entropy value
  2.7730766578354... were recomputed exactly by four reviewers. The two-phase parametrisation,
  master formula and AM-GM/artanh step were rechecked symbolically and on random samples. The
  all-q construction and every Appendix B bound were rechecked at seven values of q from 1e-4
  to 0.999. Theorem 2's inequality sigma >= r J(alpha, beta) was tested on 3000 random chains
  with several A states and no renewal independence: no violation beyond rounding.
- **Clean replay.** The shipped certificate suite (`code/reproduce.py`) was rerun from a fresh
  extraction of the handoff archive: all six certificate scripts passed, and all manifest
  hashes matched.

## Objections and responses

| # | Objection | Response |
|---|---|---|
| 1 | Relation to Aznagulov (arXiv:2609.14623) under-specified: that paper proves V_n is attained at fixed n, defines the architecture penalty G_kappa, and asks whether growing architecture can drive cost to its infimum. | New paragraph "Relation to the two closest sources" and comparison table (Table 1). States that V_4(P_q) is therefore an attained minimum, that the optimal architecture in G_kappa exceeds three states once kappa < V_3 - V_4, and that profitable insertion was raised there only as a possible route. |
| 2 | No quantitative comparison with the earlier Evidence Press floor; mutable GitHub link. | Quoted the earlier certified floor 0.017568198744 at q = 1/20; the new floor 1.8973 is about 108 times larger. Citation now uses the Zenodo DOI 10.5281/zenodo.23118474. |
| 3 | "V_4 <= V_3" is trivial; what is the content? | Introduction now says explicitly that adding states can never raise the minimum and that the content is strict decrease. |
| 4 | Missing waiting-time inference literature. | Added Martinez et al. 2019, van der Meer-Ertel-Seifert 2022, Harunari et al. 2022, Hartich-Godec 2021, van der Meer-Deguenther-Seifert 2023, Deguenther et al. 2024 (all Crossref-verified). |
| 5 | Positive-realisation theory and phase-type order are classical; cancellation is not new. | Added Benvenuti-Farina 2004 and O'Cinneide 1990, and stated that the new point is that an admissible cancelled mode can lower the entropy functional, not cancellation itself. |
| 6 | The artanh lemma should be placed against related information-theory and TUR literature. | Added a sentence linking the function 4d artanh d to the entropy of a single biased link and to optimal thermodynamic uncertainty relations (Shiraishi 2021); the lemma is presented as a reproved tool, not a priority claim. |
| 7 | Many-A-state case should be part of Theorem 1; reset replacement should be a formal lemma. | Theorem 1 now states the bound for any number of A states with at most two B states; Appendix A now opens with Lemma (reset replacement) and explains why one B state is impossible. |
| 8 | "Strictly positive rates" wording could be read as applying to Q_*, which has one absent reciprocal pair. | Reworded. |
| 9 | Full-law equality: why does the residual-life (initial segment) law also match? | Added the standard equilibrium age/residual-life argument. |
| 10 | Appendix B constants are valid but give a tiny saving (epsilon about 1e-20 to 6e-32). | Stated plainly that Appendix B is existential and that the size of the saving should be judged from the explicit example and the new numerical section. |
| 11 | Appendix C does not state the truncation order. | Now states dyadic reduction, N = 72 terms, enclosure width below 1e-24, endpoints printed by the certificate. |
| 12 | Theorem 4 nonattainment is a one-line corollary of Theorem 2. | Acknowledged in the text; the new content is sharpness and the three-state approach. |
| 13 | Readability for non-specialists: needs plain-language framing, roadmap, network diagram, notation clean-up. | Added a plain-language opening, a roadmap, Table 1, a new Figure 1 drawing both mechanisms, a physical-units illustration, and renamed clashing symbols (dwell age is now theta; the all-q constant is now nu). |
| 14 | Initial dwell density is an instantaneous statistic; relation to finite time resolution. | Linked to the classical missed-events problem in single-channel recording (Hawkes, Jalali and Colquhoun 1990); no finite-resolution theorem is claimed. |
| 15 | Is the paper's competitor near the four-state optimum? Does a fifth state help? Can more local statistics sharpen the floor? | New Section 6 (numerical exploration, separated from the proofs); see below. |

## Extension work in this round

See Section 6 of the paper and the `extension/` folder. All numerical optimisation there is
discovery evidence, not proof. Exact claims in that section are backed by rational
certificates that print PASS.
