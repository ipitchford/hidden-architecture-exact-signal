# Prior-art and object-identity gate

**Search date:** 26 October 2026.  
**Status:** bounded literature assessment, not a certification of historical priority.  
**Search record:** `search_queries.json` records the initial 94 literal searches; `search_queries_rerun_all_q.json` adds 14 searches after the all-parameter strengthening, for 108 total. Engine and batch are recorded. Source opens/finds are listed below through stable URLs and passages. Sister agents' independent searches are not included in that count. The structural rerun is documented in `all_q_novelty_rerun.md`.

## 1. Frozen contributions and exclusions

The work has converged on three concrete statements.

**C1 — Exact minimum at minimal hidden dimension.** For every \(0<q<1\), consider the stationary binary alternating-renewal law \(P_q\) whose complete A dwell is exponential with rate \(s=1+q\) and whose complete B dwell has transform
\[
\widehat f_q(z)=\frac{bz+c}{z^2+2sz+c},\qquad
b=\frac{2q}{1+q},\quad c=1+q+q^2.
\]
Among irreducible three-state CTMCs with a deterministic binary labelling that realise this complete stationary law, the minimum entropy-production rate is
\[
V_3(P_q)=(1-q)\log(1/q).
\]
The homogeneous biased three-cycle attains it. The theorem concerns the exact entire observed law, not merely two dwell moments.

**C2 — Strict advantage of an additional hidden state for the whole family.** For every \(0<q<1\), an explicit finite four-state exact realisation has entropy production strictly below \(V_3(P_q)\). The construction inserts a third B phase with exit rate \((1+q)/2\), small positive stationary occupation, and finite rates. All rates are rational for rational q. At \(q=1/20\), a separate compact rational witness has entropy in \((2.773076657,2.773076658)\), while \(V_3=(19/20)\log20>2.845945659\). Thus smallest feasible Markov cardinality does not ensure minimum dissipation, even with an exact complete observation law. No claim of four-state or unrestricted optimality is made for either construction.

**C3 — Complete optimisation from three dwell statistics.** For any stationary finite irreducible CTMC and any nontrivial binary state partition, let \(r\) be the entrance rate into B, \(m\) its mean complete dwell, and \(f_0=f_B(0+)\) its density at zero under stationary entrance sampling. No renewal assumption is made. For \(r,m,f_0>0\), \(rm<1\), and \(k=mf_0<1\),
\[
\sigma(Q)>4r\sqrt{1-k}\,\operatorname{atanh}\sqrt{1-k}
\]
for every finite compatible chain of finite entropy production; the right side is the exact infimum over all such finite chains. Three-state chains with diverging internal mixing approach it. For \(k\ge1\), the exact infimum is zero, attained by a reversible chain with at most three states. At \(f_0=0\), finite-state compatibility requires infinite entropy production.

This is a statistics-constrained theorem. The sharpness sequence changes the full dwell law; it is not an exact-law minimising sequence for \(P_q\), and it does not contradict a compactness theorem whose constraint fixes the complete observation law. For \(P_q\), C3 supplies the explicit lower bound
\[
V_\infty(P_q)\ge \frac23(1-q)\log(1/q).
\]
The exact value and attainment of \(V_\infty(P_q)\) remain unresolved by these results.

## 2. Normalisation and translations

| Object | Convention here | Translation caution |
|---|---|---|
| Generator | Row generator \(Q1=0\) | Some sources use columns; transpose before comparing. |
| Stationarity | Row vector \(\pi Q=0\) | \(\pi_iQ_{ij}\) is a stationary directed flux. |
| Entropy rate | \(\sum_{i<j}(\pi_iQ_{ij}-\pi_jQ_{ji})\log(\pi_iQ_{ij}/\pi_jQ_{ji})\) | This equals the directed relative-entropy sum. Do not add another factor of two. |
| Time and entropy units | Forward ring rate one; \(k_B=1\); natural logarithms | Rescaling all rates rescales both \(r\) and \(\sigma\). |
| Dwell distribution | Complete visit sampled at an entrance to B | This differs from the residual life at a stationary random time. |
| Reversal | Ordinary reversal of even state variables | No odd-variable parity or kinetic-hysteresis interpretation is introduced. |
| Jeffreys divergence | \(J(p,q)=D(p\Vert q)+D(q\Vert p)\) | Sason (2015) calls half of this quantity \(J\). |
| Affinity | \(\mathcal A(p,q)=\sum_i\sqrt{p_iq_i}\) | Squared Hellinger distance is often \(1-\mathcal A\), sometimes twice that. |
| Hidden dimension | B phases; A is one reset state for \(P_q\) | Three total states means two hidden B phases. |

The stationary reset merge is a relabelling/application of an existing log-sum construction. It should be credited as such, even though in the special case of an exponential complementary dwell and renewal independence it preserves the complete law.

## 3. Formula and finite-object fingerprints

### 3.1 Exact-law family

The biased ring is
\[
Q_q=\begin{pmatrix}
-(1+q)&1&q\\
q&-(1+q)&1\\
1&q&-(1+q)
\end{pmatrix},\qquad \pi=(1/3,1/3,1/3).
\]
Its characteristic polynomial is
\[
z\{z^2+3(1+q)z+3(1+q+q^2)\}.
\]
The killed B polynomial is \(p(z)=z^2+2(1+q)z+1+q+q^2\). It has roots \(-(1+q)\pm\sqrt q\). The observable transform has no pole cancellation for \(0<q<1\), so its algebraic degree is two.

| \(q\) | Reduced B transform | \((r,m,f_0)\) | \(V_3\) |
|---|---|---|---|
| \(1/20\) | \((800z+8841)/(8400z^2+17640z+8841)\) | \((7/20,40/21,2/21)\) | \((19/20)\log20\) |
| \(1/4\) | \((32z+105)/(80z^2+200z+105)\) | \((5/12,8/5,2/5)\) | \((3/4)\log4\) |
| \(1/2\) | \((8z+21)/(12z^2+36z+21)\) | \((1/2,4/3,2/3)\) | \((1/2)\log2\) |

The minimal-dimension proof reduces to an inequality on
\[
|R|<q,\quad |K|<\sqrt q,\qquad
\frac{1+RK}{1-RK}
\log\frac{(1-qR^2)(1-q^2K^2)}
{(q^2-R^2)(q-K^2)}
\ge 3\log(1/q).
\]
This scalar normal form should be retained in future priority checks.

### 3.2 Exact four-state witness

\[
Q_*=\begin{pmatrix}
-21/20&4781/4800&31/1200&9/320\\
1/20&-79/60&19/15&0\\
4/5&1/3&-131/60&21/20\\
21/20&0&1/5&-5/4
\end{pmatrix},\quad
\pi_*=(1/3,217/720,7/36,41/240).
\]
State 0 is A; states 1–3 are B. The zero pattern has exactly one absent undirected B edge. The lower-right block satisfies \(p(S)1=0\) at \(q=1/20\), and the entrance law has \(\alpha t=2/21\). The transform therefore equals the first row of the table above. The exact entropy is a sum of five rational multiples of logarithms whose positive ratios are
\[
683/31,\quad 560/31,\quad 287/15,\quad 589/100,\quad 245/41.
\]
The sibling audit records exact rational checks and a rigorous logarithm-series interval. This gate concerns prior art, not independent recertification of that audit.

### 3.3 Three-statistic theorem

The key dimensionless fingerprint is
\[
k=mf_0,\qquad
\Phi(k)=4\sqrt{1-k}\operatorname{atanh}\sqrt{1-k}.
\]
Equivalent logarithmic form:
\[
\Phi(k)=2\sqrt{1-k}
\log\frac{1+\sqrt{1-k}}{1-\sqrt{1-k}}.
\]
For the probability inequality, replace \(k\) by \(\mathcal A(p,q)^2\).

Three exact instances with \(r=1/3,m=2\) are:

| \(d=\sqrt{1-k}\) | \(f_0\) | Exact infimum |
|---|---|---|
| \(1/2\) | \(3/8\) | \((1/3)\log3\) |
| \(1/3\) | \(4/9\) | \((2/9)\log2\) |
| \(3/5\) | \(8/25\) | \((4/5)\log2\) |

The sharpness family has
\[
\alpha=((1+d)/2,(1-d)/2),\quad
\mu=(m/2,m/2),\quad
t=((1-d)/m,(1+d)/m)^T,
\]
\[
S_M=m^{-1}
\begin{pmatrix}
-(1+2M)&2M+d\\
2M-d&-(1+2M)
\end{pmatrix},\quad M>d/2.
\]
Its entropy is
\[
r\left[4d\operatorname{atanh}d+
d\log\frac{M+d/2}{M-d/2}\right].
\]
Its complete dwell transform is
\[
\frac{(1-d^2)mz+1+4M+d^2}
{m^2z^2+2m(1+2M)z+1+4M+d^2}.
\]
These formulas distinguish finite-statistic sharpness from fixed-transform optimisation.

## 4. Cross-domain aliases searched

The 108-query combined corpus includes phase-type representations, two-phase PH canonical forms, minimal positive realisation, rational transfer functions, hidden Markov realisation, state splitting/expansion/insertion, stationary reset and intertwining, exact waiting-time laws, two- and three-state entropy minimisation, fixed-spectrum entropy, unicyclic affinity/coherence, initial waiting density, density at zero, immediate return, entrance/exit distributions, Jeffreys/Bhattacharyya/Hellinger/affinity comparisons, and symmetric divergence inequalities.

Relevant translations checked:

- A PH “entropy optimisation” may optimise an information entropy of representation probabilities rather than stationary thermodynamic entropy production. These objectives are not interchangeable.
- “Two-phase fitting” sometimes means a two-stage fitting algorithm, not two Markov phases.
- A sharp Jeffreys bound in total variation is not automatically the needed affinity bound. The relation \(\mathrm{TV}\le\sqrt{1-\mathcal A^2}\) has the wrong direction for that substitution.
- Spectral coherence versus cycle-affinity bounds may be saturated by a homogeneous ring while still failing to prove an exact entropy minimum under the full observed-law constraint.
- Repeated or unobservable hidden eigenmodes are distinct from the observable transform's algebraic degree. Pole counting alone does not establish microscopic state cardinality.
- Discrete-time masked networks and continuous-time binary dwell observations are related inference settings, but their feasible classes must be compared explicitly.

No natural combinatorial integer sequence or representation-theoretic named kernel emerged. OEIS was therefore not used as a source of a substantive comparison. The relevant finite fingerprints are rational transfer functions, matrices and variational formulas, not an asserted new sequence.

## 5. Closest inspected sources

### 5.1 Ehrich (2021): direct architecture question

J. Ehrich, *Tightest bound on hidden entropy production from partially observed dynamics*, Journal of Statistical Mechanics (2021), 083214. Full preprint:
https://arxiv.org/html/2105.08803v2
https://doi.org/10.1088/1742-5468/ac150e

Section 4 assumes that the correct hidden-state count is known. Section 5 explicitly asks whether the exact-data bound decreases when additional hidden states and cycles are allowed. The displayed construction treats discrete-time masked Markov chains; the conclusion anticipates a continuous-time analogue. This is the closest conceptual antecedent to C2. Our proposed result supplies an exact continuous-time counterexample to minimal-cardinality sufficiency; it does not contradict Ehrich's cardinality-conditioned theorem. Mere nonidentifiability of entropy among same-law models was already present there and is not our novelty claim.

**Load-bearing passages:** Section 4 opening; Section 5 paragraphs containing “correct number of hidden states” and “more and more hidden states and cycles”; Eq. (29), \(CH^{n-2}B\), for full observable statistics.

### 5.2 Nitzan, Ghosal and Bisker (2023): topology assumptions

E. Nitzan, A. Ghosal, G. Bisker, *Universal bounds on entropy production inferred from observed statistics*, Physical Review Research **5**, 043251.
https://doi.org/10.1103/PhysRevResearch.5.043251
https://arxiv.org/pdf/2212.01783

Their optimisation constrains observed statistics on a hypothesised topology. Numerical tests involving simplified topologies yield useful bounds in their examples; the conclusion explicitly leaves universality of that procedure unresolved. C2 addresses the complete-observation-law version of the architectural issue. It does not falsify their numerical examples or establish that their finite-moment estimator fails: a weaker data constraint can lower a restricted optimum.

**Load-bearing passages:** topology/optimisation setup in Section III A; simplified-topology study in Section III D; conclusion discussing removal of hidden states and unknown general validity.

### 5.3 Skinner and Dunkel (2021): moments and reset merge

D. J. Skinner, J. Dunkel, *Estimating entropy production from waiting time distributions*, Physical Review Letters **127**, 198101.
https://doi.org/10.1103/PhysRevLett.127.198101
https://arxiv.org/html/2105.08681v2

The supplementary construction merges one observed block into a single state by summing stationary fluxes, preserves detailed dynamics in the other block and its dwell distribution, and contracts entropy via log-sum. Their numerical/analytic optimisation uses specified dwell moments, not the entire rational transform of \(P_q\). The exact reset-law corollary needed here follows from this construction and should not be presented as a new merge theorem.

**Load-bearing passages:** supplementary Lemma 2 and Eq. (A14); two-hidden-phase flux objective Eq. (A28); small-entropy moment-constrained asymptotics.

### 5.4 Skinner and Dunkel (2021): two-step observable optimisation

D. J. Skinner, J. Dunkel, *Improved bounds on entropy production in living systems*, PNAS **118**, e2024300118.
https://doi.org/10.1073/pnas.2024300118
https://math.mit.edu/~dunkel/Papers/2020SkDu_EPR.pdf

The appendix constructs optimal simplified networks for prescribed one- and two-step coarse transition statistics. Its analytic symmetric example, Eqs. (A28)–(A29), has the same square-root/logarithm shape:
\[
4\sqrt{2p-1}\log\frac{1+\sqrt{2p-1}}{1-\sqrt{2p-1}}.
\]
The constraint is a three-label two-step transition count, not binary complete-dwell \((r,m,f_0)\). The displayed optimum is attained with finite rates. Thus the scalar functional shape and optimisation philosophy have antecedents; the new candidate is the specific dwell-statistic optimisation, general partition scope, and nonattainment theorem.

**Load-bearing passages:** definition of observable sets \(O_1,O_2\); appendix “Analytic verification”, Eqs. (A28)–(A29).

### 5.5 Aznagulov (2026): full-law exact realisations

M. Aznagulov, *Thermodynamic Realizability of Hidden Markov Processes: Attainment, Observable Certificates, and the Price of Architecture*, preprint.
https://arxiv.org/html/2609.14623v1

The inspected source gives fixed-cardinality compactness/attainment, an architecture penalty framework, the same rational \(P_q\) target, and finite cancellation constraints for higher PH representations. It exhibits a four-phase algebraic example showing that overly restrictive annihilator tests miss some exact realisations. It does not, in the inspected sections, prove C1, C2, or C3. The compactness argument was inspected for a specific flaw; none was identified in those passages, but this report is not a complete independent proof audit.

**Load-bearing passages:** Sections 8.3–8.7, especially two-phase law/cancellation identities, and the fixed-cardinality compactification proof. The exact positive all-dimension optimum remains a stated question; our work does not settle it.

### 5.6 Existing Evidence Press candidate: collision with zero-cost and stability claims

Anonymous, *An architecture-independent dissipation floor for alternating-renewal observations*, v1.1, unrefereed candidate, 3 October 2026.
https://github.com/ipitchford/hidden-dissipation-floor/blob/main/PAPER.tex
https://evidencepress.org/releases/hidden-dissipation-floor/

This earlier package already treats the zero-floor classification through positive exponential mixtures, an architecture-independent positive floor obtained from persistence covariances, and robustness to bounded observational error. Those statements are not new here. Its \(q=1/20\) numerical certificate is much smaller than the proposed closed-form C3 bound, but a quantitative improvement alone must be stated on the correct observable/infinite-resolution assumptions.

**Load-bearing passages:** abstract; zero-cost classification theorem; additive-reversibilisation certificate; robustness section. The inspected manuscript does not contain the three-statistic sharp optimisation or C2.

### 5.7 Amann–Schmiedl–Seifert; Jia–Chen; Wu–Jia

A. Amann, T. Schmiedl, U. Seifert, *Can one identify nonequilibrium in a three-state system by analyzing two-state trajectories?*, JCP **132**, 041102 (2010).
https://doi.org/10.1063/1.3294567

C. Jia, Y. Chen, *A second perspective on the Amann–Schmiedl–Seifert criterion for non-equilibrium in a three-state system*, JPA **48**, 205001 (2015).
https://doi.org/10.1088/1751-8113/48/20/205001

B. Wu, C. Jia, *Parameter Inference and Nonequilibrium Identification for Markov Networks Based on Coarse-Grained Observations*, PRL **134**, 087103 (2025).
https://doi.org/10.1103/PhysRevLett.134.087103
https://arxiv.org/html/2406.19586v2

The 2010 full author manuscript and 2025 full preprint were inspected; the 2015 item was checked at metadata/abstract level only. These works concern parameter identifiability and qualitative nonequilibrium detection under topology assumptions. They are relevant to the three-state observation setting, but no exact-law entropy minimum equal to C1 or architecture counterexample equal to C2 was found. The 2025 spectral statistics use generic distinct-mode and nonzero-residue assumptions; they do not justify counting hidden states from poles in a nonminimal representation.

### 5.8 Spectral and oscillation bounds

A. C. Barato, U. Seifert, *Coherence of biochemical oscillations is bounded by driving force and network topology*, PRE **95**, 062409 (2017).
https://doi.org/10.1103/PhysRevE.95.062409
https://arxiv.org/pdf/1701.05848

L. Oberreiter, U. Seifert, A. C. Barato, *Universal minimal cost of coherent biochemical oscillations*, PRE **106**, 014106 (2022).
https://doi.org/10.1103/PhysRevE.106.014106
https://arxiv.org/pdf/2112.01607

A. Kolchinsky, N. Ohga, S. Ito, *Thermodynamic bound on spectral perturbations, with applications to oscillations and relaxation dynamics*, PRResearch **6**, 013082 (2024).
https://doi.org/10.1103/PhysRevResearch.6.013082

The first addresses coherence versus affinity/topology; the second discusses cost versus coherence with an explicitly limited low-coherence regime in the inspected version; the third also uses kinetic activity quantities. Homogeneous-ring saturation appears in this literature. None of these inspected bounds by itself identifies the exact-law constrained three-state feasible set or proves C1. A broad claim about a new homogeneous-ring extremum would be inappropriate.

### 5.9 Probability-divergence antecedents

I. Sason, *Tight Bounds for Symmetric Divergence Measures and a Refined Bound for Lossless Source Coding*, IEEE Transactions on Information Theory **61**(2), 701–707 (2015).
https://doi.org/10.1109/TIT.2014.2387065
https://arxiv.org/html/1403.7164v7

This source proves sharp Jeffreys-versus-total-variation bounds and sharp affinity-versus-total-variation bounds, drawing on Gilardoni's symmetric \(f\)-divergence theory. Its Jeffreys normalisation is one half of ours. The exact affinity-constrained inequality used in C3 was not located in this paper, and cannot be obtained by substituting the TV upper bound into its Jeffreys lower bound. The manuscript should include its short Jensen proof and make no standalone novelty claim for a probability-divergence comparison. A precise earliest source for this special comparison remains a bounded bibliographic uncertainty.

### 5.10 PH realisation literature

A. Mészáros and M. Telek, *A two-phase MAP fitting method with APH interarrival time distribution*, Winter Simulation Conference (2012).
https://informs-sim.org/wsc12papers/includes/files/inv252.pdf

Y. Liu, D. Yao, H. Zhang, *A non-convex optimization approach of searching algebraic degree phase-type representations for general phase-type distributions*, Advances in Applied Probability **57**(3), 1101–1137 (2025).
https://doi.org/10.1017/apr.2024.72

The former full text and the latter abstract were inspected. These are useful naming leads for distribution-preserving realisation, positivity and algebraic degree. Mészáros–Telek Section 4.2 explicitly optimises entropies of entry and exit probability vectors, not stationary entropy production. Neither inspected item establishes the thermodynamic optimum considered here. The latter source was not read in full, so this is a limited scope comparison.

### 5.11 Review coverage

U. Seifert, *Universal bounds on entropy production from fluctuating coarse-grained trajectories*, preprint corresponding to a 2026 review.
https://arxiv.org/html/2512.07772v1

Sections III.1 and V identify the optimisation, state-lumping and waiting-time strands. It was used to locate primary sources, particularly Ehrich. This review is not a substitute for the primary comparisons above.

## 6. Contribution-unit adjudication

| Unit | Gate decision | Reason and permitted scope |
|---|---|---|
| Qualitative irreversibility despite reversible binary observations | COLLISION | Already established in the cited inference literature. |
| Full-law entropy minimisation as a research programme | COLLISION | Explicit in Ehrich and related work. |
| Reset merge by stationary flux aggregation and log-sum | COLLISION | Skinner–Dunkel provides the construction. Special full-law preservation is an application. |
| Zero all-dimension floor iff positive exponential mixtures; robust covariance floor | COLLISION | Existing Evidence Press candidate addresses these. |
| C1 exact three-state minimum for all \(0<q<1\) | CLEAR TO PROVE within this recorded corpus | No identical exact-law minimisation located; proof and audit remain separate obligations. |
| C2 exact four-state model below every three-state model for every \(0<q<1\) | CLEAR TO PROVE within this recorded corpus | Directly sharpens an architecture question raised by Ehrich; no exact collision found after the structural rerun. |
| C3 exact infimum and nonattainment from \((r,m,f_0)\) for arbitrary binary partitions | CLEAR TO PROVE within this recorded corpus | Neither full theorem nor equivalent initial-density formulation found. |
| Sharp affinity–Jeffreys inequality as an independent theorem | BOUNDED UNCERTAINTY | Classical divergence-comparison context; exact earliest attribution not resolved. Do not advertise as new. |
| Reproducible exact rational witness and logarithm certificate | Independent verification artefact | Valuable evidence; it does not prove historical novelty. |
| Exact all-architecture optimum for \(P_q\) | NOT ESTABLISHED | C1–C3 bracket it but do not determine it or prove attainment. |

“Clear to prove” is the skill's bounded disposition, not a statement that no earlier proof exists.

## 7. Language for the manuscript

**Supported:**

- “We prove the exact three-state minimum for this complete observation law and construct an exact four-state realisation with strictly smaller dissipation.”
- “Minimal state cardinality is therefore insufficient to guarantee a universal dissipation lower bound, even with exact observable statistics.”
- “For arbitrary binary partitions, we solve the optimisation constrained by the crossing rate, mean dwell, and density at zero.”
- “This gives a continuous-time example addressing the architecture dependence explicitly raised in earlier model-fitting work.”
- “The divergence lemma is proved for completeness with the normalisation used here.”

**Unsupported or misleading:**

- “First ever,” “previously unknown,” or “no one has considered” based only on the search.
- “The global hidden-dissipation problem is solved.”
- “The four-state realisation is the global optimum.”
- “Ehrich/Nitzan's theorem is false.” Their scope and constraints differ.
- “A finite-dimensional minimiser does not exist for the exact observed law.” Nonattainment here fixes only three statistics.
- “The bound is robust to finite sampling or finite time resolution.” \(f_0\) is an infinitesimal statistic; no statistical guarantee has been proved.
- “The new proof introduces Jeffreys/Bhattacharyya bounds.” The probability inequality is deliberately not a novelty unit.
- Claims of publication quality or guaranteed prestigious publication as an inference from the existence of a proof.

## 8. Remaining bibliographic limits

The search used two general web/full-text engines, arXiv HTML/PDF, publisher pages, author-hosted manuscripts, and the named public source repositories. It did not exhaust MathSciNet, zbMATH, Web of Science, unpublished work, conference talks, or non-English literature. No author enquiry was made. The 2015 Jia–Chen and 2025 Liu–Yao–Zhang works were not read in full. The earliest exact affinity–Jeffreys comparison remains unidentified.

The final manuscript can proceed with bounded contribution language because the main claims have precise proofs and explicitly separated antecedents. Before external submission, a domain expert should review C1's global parameterisation and equality cases, C2's full stationary-law identity, C3's entrance-sampling convention and boundary cases, and the novelty boundary against the PH and thermodynamic-inference literatures.

