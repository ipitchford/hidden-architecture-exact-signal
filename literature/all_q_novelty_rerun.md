# Structural novelty-gate rerun: a profitable fourth state for every parameter

Date: 26 October 2026. This rerun follows the proof simplification in \`../two_phase/all_q_architecture_advantage.md\`.

## Frozen strengthened claim

For every \(q\in(0,1)\), there exists a finite irreducible four-state CTMC with all off-diagonal rates positive whose deterministic binary observation has the entire stationary alternating-renewal law \(P_q\), and whose entropy production is strictly below
\[
V_3(P_q)=(1-q)\log(1/q).
\]
For rational \(q\), the constructive parameter choice gives rational rates. Thus
\[
V_4(P_q)<V_3(P_q)\quad\text{for all }0<q<1.
\]
The construction does not determine \(V_4\) or \(V_\infty\). It proves no infinite hierarchy of strict improvements.

The newly added B phase has exit rate \(z=(1+q)/2\), occupation \(\varepsilon\), and finite internal rate parameter \(M\). Its extra decay mode cancels from the full observed dwell transform. This is not entropy-neutral duplication of a hidden state.

## Decisive formula fingerprint

Put \(u=(1-q)/(1+q)\). The limiting right derivative of entropy per cycle under insertion is
\[
d_\infty=\frac{u^2}{1+u}
\left[3-\frac12\log(1-u^2)-\frac{3\operatorname{atanh}u}{u}\right].
\]
The bracket has the exact power series
\[
\sum_{n=1}^{\infty}\frac{1-4n}{2n(2n+1)}u^{2n},
\]
whose first coefficients are
\[
-\frac12,\ -\frac7{20},\ -\frac{11}{42},\
-\frac5{24},\ -\frac{19}{110},\ -\frac{23}{156}.
\]
The scalar sign inequality is elementary and is not treated as an independent novelty claim. The research claim is its role in an explicitly feasible, law-preserving Markov phase insertion with a strict thermodynamic benefit.

The proof gives finite rational choices
\[
\eta=\frac{u^4}{2(1+u)},\quad
M=2+\frac{4C_0}{\eta},\quad
\varepsilon=\min\{\varepsilon_0,\eta/(2B_0)\},
\]
with \(C_0,B_0,\varepsilon_0\) specified in the proof note. Three exact finite instances are recorded in \`all_q_fingerprints.json\`; each includes the full generator, stationary law, rates, row sums, stationary residual, characteristic-polynomial form, and a hash canonicalised over B-state relabellings.

| \(q\) | \(M\) | \(\varepsilon\) |
|---|---|---|
| \(1/20\) | \(5793698/361\) | \(16983563041/54973714426294727700\) |
| \(1/4\) | \(14818/9\) | \(6561/1379681150500\) |
| \(1/2\) | \(1586\) | \(1/2453201640\) |

These conservative parameters establish existence. The separate compact \(q=1/20\) witness illustrates a materially larger gap.

## Rerun search

Fourteen additional queries are in \`search_queries_rerun_all_q.json\`. They cover:

- PH entropy production with state insertion and extra phases;
- hidden Markov entropy with added states;
- nonminimal and minimal thermodynamic realisations;
- exact atanh/log formula fragments;
- entropy-reducing hidden-state insertion.

Two general web engines were used; primary retrieved sources were inspected. The combined recorded search has 108 queries. No identical all-parameter theorem or equivalent construction was found within this corpus.

The directly relevant prior source, Aznagulov Section 8.7, discusses profitable insertion as a possible route, not as an established all-parameter result.

## Additional source located and scoped

U. Kapustin, A. Ghosal and G. Bisker, *Utilizing time-series measurements for entropy-production estimation in partially observed systems*, Physical Review Research **6**, 023039 (2024).
https://doi.org/10.1103/PhysRevResearch.6.023039
https://arxiv.org/pdf/2212.13487

The full preprint distinguishes complete lumping from a setting in which within-block transitions are observable even though their endpoint identities remain hidden. It uses that additional data to sharpen time-series entropy estimators. It does not optimise architecture at a fixed complete binary law or give the three-statistic initial-density optimum. Its “extra information” is a change of observation protocol, distinct from our addition of unobserved physical states.

The earlier report's strongest conceptual antecedent remains Ehrich (2021), Section 5, which explicitly asks how an exact-data bound changes as additional hidden states/cycles are allowed. The updated theorem provides an exact continuous-time family with strict benefit from one added state.

## Gate disposition

**Theorem and complete constructive proof:** CLEAR TO PROVE within the recorded corpus. No collision was found, but historical priority is not certified.

**Elementary scalar inequality:** no independent novelty claim.

**Existence of unobservable modes and nonminimal PH representations:** known realisation theory, not a novelty unit.

**Thermodynamically beneficial law-preserving insertion for every \(q\in(0,1)\):** the precise proposed contribution.

**Independent mathematical validation:** belongs to the proof audit. This report verifies the prior-art boundary and exact formula fingerprints; it is not a substitute for review of the derivative formula, Taylor remainder bounds or positivity choices.

## Manuscript language

Use: “For every member of the family, a four-state exact realisation dissipates strictly less than every three-state realisation.”

Do not expand this to arbitrary observed laws, arbitrary minimal PH representations, or strict improvement at every cardinality. The equality of path laws must remain explicit; matching a finite set of observables would be a weaker result.

