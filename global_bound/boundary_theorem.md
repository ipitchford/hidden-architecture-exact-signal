# The exact dissipation cost of a suppressed immediate-return density

Date: 26 October 2026. Internal research proof; no external peer review or priority certification. Ordinary even-variable reversal, natural logarithms and Boltzmann constant one are used throughout.

## Scope

This note solves the optimisation over all finite hidden chains subject to three observable statistics: the entrance rate `r` into a visible block `B`, its mean complete dwell `m`, and its complete-dwell density at zero `f0`. It does **not** solve the optimisation subject to a fixed complete observed law. The difference is essential: the positive statistics-only optimum below is approached by sending a rate to infinity at fixed dimension while the full dwell distribution changes.

The theorem needs no renewal independence and no assumption that the complementary block has an exponential dwell. It holds for every finite irreducible stationary continuous-time Markov chain and deterministic binary partition.

## Theorem 1: architecture-independent boundary certificate

Let `Q` be a finite irreducible row generator with stationary distribution `pi`, and partition the states into nonempty blocks `A,B`. Let

\[
\sigma(Q)=\sum_{i<j}(\pi_iQ_{ij}-\pi_jQ_{ji})
\log\frac{\pi_iQ_{ij}}{\pi_jQ_{ji}}.
\]

Let `r` be the stationary rate of A-to-B crossings, `m` the mean duration of a complete B dwell, and `f0=f_B(0)` the right limit at zero of its density under stationary entrance sampling. Put `k=m f0`. If `0<k<1`, then

\[
\boxed{\quad \sigma(Q)\geq 4r\sqrt{1-k}\,
\operatorname{artanh}\sqrt{1-k}.\quad}
\tag{1}
\]

In fact the inequality is strict for each finite chain of finite entropy production when `k<1`. If `f0=0`, every compatible finite chain has infinite entropy production. For `k>=1`, the universal bound supplied by these three statistics is zero.

### Proof

For each microscopic B state define

\[
t_i=\sum_{a\in A}Q_{ia},\qquad
\mu_i=\pi_i/r,\qquad
\alpha_i=\frac{\sum_{a\in A}\pi_aQ_{ai}}r,
\qquad \beta_i=\mu_i t_i.
\tag{2}
\]

Stationary flow balance across the cut makes `alpha` and `beta` probability distributions. The killed generator is `S=Q_BB`; the complete dwell density under its stationary entrance law is

\[
f_B(u)=\alpha e^{uS}t,
\qquad f0=\sum_i\alpha_i t_i.
\tag{3}
\]

Microscopic stationarity gives `pi_B S=-r alpha`, hence `mu=alpha(-S)^{-1}`. The killed chain is transient because Q is finite irreducible and A is nonempty. Integration of its survival function therefore gives `mu 1=m`; equivalently `m=pi(B)/r`. This identity uses occupation per entrance and does not require consecutive dwell times to be independent.

Write `J(p,q)=sum_i(p_i-q_i) log(p_i/q_i)` for unnormalised Jeffreys divergence. Applying the log-sum inequality in both directions to all edges joining A to a given B state yields

\[
\sigma(Q)\geq \sigma_{\partial B}(Q)
\geq rJ(\alpha,\beta).
\tag{4}
\]

The Bhattacharyya affinity satisfies the Cauchy--Schwarz bound

\[
\mathcal A(\alpha,\beta)
=\sum_i\sqrt{\mu_i}\sqrt{\alpha_i t_i}
\leq \sqrt{m f0}=\sqrt{k}.
\tag{5}
\]

For probability vectors `p,q` of affinity `a`, the sharp inequality

\[
J(p,q)\geq \Phi(a),\qquad
\Phi(a)=4\sqrt{1-a^2}\operatorname{artanh}\sqrt{1-a^2}
\tag{6}
\]

is proved below. The function `Phi` is decreasing on `(0,1]`, so (4)--(6) give (1). The probability inequality is a classical type of symmetric-divergence comparison; the proof is included rather than relying on a potentially mismatched normalisation.

For strictness, equality in (1) would require every B-internal entropy contribution to vanish, since (4) discards their nonnegative sum. Thus every internal stationary B flux equals its reverse. Microscopic stationarity then implies `alpha_i=beta_i` for every i. Cauchy--Schwarz gives

\[
1=(\sum_i\mu_i t_i)^2
\leq (\sum_i\mu_i)(\sum_i\mu_i t_i^2)=m f0,
\]

contradicting `k<1`. If the chain has infinite entropy, equality with a finite right-hand side is impossible as well.

Finally, finite entropy implies that every used boundary edge has its reverse. Some such edge exists by irreducibility, hence at least one B state has both `alpha_i>0` and `t_i>0`; therefore `f0>0`. This proves the assertion at zero. ∎

### Proof of the sharp affinity--Jeffreys inequality

When the divergence is finite, put `w_i=(p_i+q_i)/2`, `u_i=(p_i-q_i)/(p_i+q_i)` on indices of positive total mass, and `z_i=sqrt(1-u_i^2)`. Then `sum w_i=1`,

\[
\mathcal A=\sum_iw_i z_i,\qquad
J=\sum_iw_i\Phi(z_i).
\]

For `0<z<1`, write `d=sqrt(1-z^2)`. Direct differentiation gives

\[
\Phi'(z)=-4\left(\frac{z}{d}\operatorname{artanh}d+\frac1z\right)<0,
\]

\[
\Phi''(z)=\frac4{d^3}
\left(\frac d{1-d^2}-\operatorname{artanh}d\right)>0.
\]

The final positivity follows by differentiation of the bracket: its derivative is `2d^2/(1-d^2)^2`, and its value at zero is zero. The continuous endpoint at `z=1` is `Phi(1)=0`; `Phi(z)` tends to infinity at zero. Jensen's inequality proves (6), with boundary cases obtained by limits. Equality is attained by

\[
p=((1+d)/2,(1-d)/2),\qquad
q=((1-d)/2,(1+d)/2).
\]

Here the affinity is `sqrt(1-d^2)` and `J=4d atanh d`. ∎

## Theorem 2: exact optimisation and positive nonattainment for three statistics

Fix `r,m,f0` with `r>0`, `m>0`, `0<rm<1`, `f0>0`; let `C(r,m,f0)` be the class of finite irreducible stationary binary-labelled chains with precisely these three B statistics. Then

\[
\inf_{Q\in C(r,m,f0)}\sigma(Q)=
\begin{cases}
4r\sqrt{1-mf0}\operatorname{artanh}\sqrt{1-mf0},&mf0<1,\\
0,&mf0\geq1.
\end{cases}
\tag{7}
\]

For `mf0<1`, no finite chain attains this infimum, but three-state chains approach it. For `mf0>=1`, a reversible chain with at most three states attains it.

### Sharp positive branch

Let `d=sqrt(1-mf0) in (0,1)` and choose any `M>d/2`. Use one A state and two B states. Set

\[
\mu=(m/2,m/2),\quad
\alpha=((1+d)/2,(1-d)/2),\quad
t=((1-d)/m,(1+d)/m)^{\mathsf T},
\tag{8}
\]

\[
S_M=\frac1m
\begin{pmatrix}
-(1+2M)&2M+d\\
2M-d&-(1+2M)
\end{pmatrix},\qquad
s_A=\frac r{1-rm},
\tag{9}
\]

\[
Q_M=\begin{pmatrix}-s_A&s_A\alpha\\t&S_M\end{pmatrix}.
\tag{10}
\]

All rates on its three unoriented edges are positive. The exact identities

\[
-S_M\mathbf1=t,\qquad \mu S_M=-\alpha,
\]

give the stationary distribution `(1-rm,r m/2,r m/2)`, crossing rate `r`, mean dwell `m`, and `f_B(0)=(1-d^2)/m=f0`. Its two B boundary fluxes per cycle are `alpha` and the reversed vector `beta=((1-d)/2,(1+d)/2)`. Its B-internal fluxes per cycle are `M+d/2` and `M-d/2`. Therefore

\[
\sigma(Q_M)=r\left[
4d\operatorname{artanh}d+
d\log\frac{M+d/2}{M-d/2}\right].
\tag{11}
\]

Letting `M` tend to infinity gives (7); Theorem 1 proves nonattainment.

The complete dwell transform is

\[
\widehat f_M(z)=
\frac{(1-d^2)mz+(1+4M+d^2)}
{m^2z^2+2m(1+2M)z+(1+4M+d^2)}.
\tag{12}
\]

It tends to `(1+mz)^{-1}` as `M` grows. The limiting exponential has density `1/m` at zero, while every member of the sequence has density `(1-d^2)/m`. Thus evaluation of the density at zero is not continuous under this limit. The nonattainment statement is not a counterexample to any attainment theorem requiring a fixed complete observation law.

The derivative also exposes the shrinking short-time layer:

\[
f_M'(0)=\frac{-1+3d^2+4Md^2}{m^2}\longrightarrow\infty.
\]

### Sharp zero branch

If `k=mf0=1`, a two-state reversible chain with rates `s_A=r/(1-rm)` and `1/m` suffices. If `k>1`, put

\[
w_2=\frac1{4k-3},\quad w_1=1-w_2,\quad
\mu=m(w_1,w_2),\quad
t=\left(\frac1{2m},\frac{2k-1}{m}\right)^{\mathsf T}.
\]

Use `S=-diag(t)`, `alpha_i=mu_i t_i`, and the reset construction (10). The identities `alpha 1=1`, `mu 1=m`, and `alpha t=k/m=f0` hold directly. All A-to-B fluxes equal their reverses; there are no internal B edges. The chain is irreducible and reversible with zero cost. ∎

## Corollary for the exact renewal benchmark

For `P_q`, `0<q<1`, the observed statistics are

\[
r=\frac{1+q}{3},\quad m=\frac2{1+q},\quad
f0=\frac{2q}{1+q},\quad d=\frac{1-q}{1+q}.
\]

Therefore every finite exact realisation obeys

\[
\sigma(Q)>\frac23(1-q)\log(1/q),
\qquad
V_\infty(P_q)\geq\frac23(1-q)\log(1/q).
\tag{13}
\]

The strict inequality applies to each finite model; it does not make the all-dimension infimum strictly greater than the displayed constant. At `q=1/20` the constant is `1.897297106584194...`. At `q=1/4` it is `0.693147180559945...`, and at `q=1/2` it is `0.231049060186648...`.

The original three-state ring occurs in the statistics-sharp family at `M=1/2`, with `m=2/(1+q)` and `s_A=1+q`. It saturates the boundary part of the certificate, while its B-internal edge contributes the remaining one third of its total cost. Increasing `M` keeps the three statistics but changes the complete observed law, so it cannot be used as an exact competitor for `P_q`.

Together with the ring upper bound, (13) proves for every `0<q<1`

\[
\frac23(1-q)\log(1/q)\leq V_\infty(P_q)
\leq(1-q)\log(1/q).
\]

Thus increasing hidden architecture can save at most one third of the ring's dissipation. It also determines the asymptotic orders `V_inf(P_q)=Theta((1-q)^2)` as `q` tends to one, and `V_inf(P_q)=Theta(log(1/q))` as `q` tends to zero. The precise coefficients and exact optimum remain unresolved.

For a general block, the stationary persistence function `H(t)=Prob(Y_u=B for all 0<=u<=t)` obeys `H(0)=rm`, `H'(0)=-r`, `H''(0)=r f0`. Hence `k=H(0)H''(0)/H'(0)^2`. The certificate quantitatively penalises failure of local log-convexity of persistence at zero.

## Reproducibility and claim boundaries

`boundary_checks.py` independently checks stationary occupation identities for random nonrenewal partitions, the probability inequality, the exact rational sharpness families, and finite-cost versus one-way-edge controls. These are diagnostics, not replacements for the proofs.

The theorem is stronger in scope than renewal-only bounds but uses an infinitesimal observable `f_B(0)`. It is not directly a finite-resolution estimator or a confidence bound. No conclusion about rate-limited or sampled experimental data follows without additional analysis.

The argument uses classical log-sum, Cauchy--Schwarz and a symmetric-divergence inequality. The new candidate contribution is their exact optimisation consequence for `(r,m,f_B(0))`, and its use to constrain the complete-law architecture problem. A bounded prior-art search is recorded separately. No assertion of historical priority is justified.
