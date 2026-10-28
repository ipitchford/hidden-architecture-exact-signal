# Strict advantage from one extra hidden phase for every parameter

Date: 26 October 2026. Independently derived analytic proof; requires independent audit before publication. This note proves a finite architecture separation, not the all-architecture minimum or nonattainment.

## Theorem

For every \(0<q<1\), the binary alternating-renewal law \(P_q\) defined in `two_phase_theorem.md` has a four-state, strictly positive-rate exact realization with stationary entropy production strictly less than
\[
V_3(P_q)=(1-q)\log(1/q).
\]
Consequently \(V_4(P_q)<V_3(P_q)\) throughout this family. The extra state is labelled B. All rates in the construction are finite. For rational q, the displayed parameter choice produces rational rates.

Here \(V_n\) denotes the infimum over all finite exact deterministic-observation realizations with at most n states. There is no realization with fewer than three states, and a three-state realization must have one A state and two B states, since a single B state would give an exponential B dwell.

## 1. Exact family of four-state generators

Use the notation
\[
s=1+q,\quad D=1-q,\quad z=s/2,\quad u=D/s,\quad b=2q/s.
\]
Let \(M\ge2\) and \(\varepsilon>0\) be chosen below. The B states, ordered \(x,y,w\), have exit rates
\[
t=(q,1,z)^T
\]
and occupation times per observed cycle
\[
\mu_x=\mu_y=m=1/s-\varepsilon/2,\qquad\mu_w=\varepsilon.
\]
Define four positive constants
\[
A=M/2,\quad B=sM/4,\quad C=qM/2+u,\quad E=sM/4+D/2.
\]
Specify the directed internal fluxes per cycle by
\[
L_{xw}=\varepsilon A,\quad L_{wx}=\varepsilon B,\quad
L_{yw}=\varepsilon C,\quad L_{wy}=\varepsilon E,
\]
\[
L_{xy}=m-\varepsilon A/2,\qquad
L_{yx}=qm-\varepsilon C/2.
\tag{1}
\]
Set \(S_{ij}=L_{ij}/\mu_i\) for \(i\ne j\), and
\(S_{ii}=-t_i-\sum_{j\ne i}S_{ij}\). The entrance distribution is
\[
\alpha_x=\frac1s-\frac q s\varepsilon,\qquad
\alpha_y=\frac q s-\frac q s\varepsilon,\qquad
\alpha_w=\frac{2q}s\varepsilon.
\tag{2}
\]
The full generator and stationary law are
\[
Q=\begin{pmatrix}-s&s\alpha\\t&S\end{pmatrix},\qquad
\pi=(1/3,(s/3)\mu).
\tag{3}
\]

### Exact-law verification

One has \(\mu\mathbf1=2/s\), \(\mu t=1\), \(\alpha\mathbf1=1\), and direct flux balance gives \(\mu S=-\alpha\). In particular (3) is stationary.

Let \(F(v)=v^2-2sv+c\), with \(c=1+q+q^2\). Then
\[
F(q)=D,\quad F(1)=-qD,\quad F(z)=D^2/4.
\]
The fluxes (1) obey, for each B state i,
\[
\sum_{j\ne i}L_{ij}(t_j-t_i)=\mu_i F(t_i).
\tag{4}
\]
For x and y this follows by cancellation of the two terms proportional to A or C. For w it follows from \(E-B=D/2\). Dividing (4) by \(\mu_i\) gives
\(S t=c\mathbf1-2st\), hence
\[
(S^2+2sS+cI)\mathbf1=0.
\]
Also \(\alpha t=b\), directly from (2). Therefore the survival function \(g(v)=\alpha e^{Sv}\mathbf1\) solves
\(g''+2sg'+cg=0\), with \(g(0)=1\), \(g'(0)=-b\). Its density has transform exactly \((b\lambda+c)/(\lambda^2+2s\lambda+c)\). The unique A state resets every cycle, giving the complete alternating-renewal law, not only its moments.

The explicit choices below make every off-diagonal rate and entrance positive. The strictly positive exits imply transience of S, and the positive A–B star implies irreducibility of Q.

## 2. First variation of entropy

Write \(J(a,b)=(a-b)\log(a/b)\). The entropy per cycle is
\[
\Phi(\varepsilon)=\sum_i J(\alpha_i,\mu_i t_i)
 +\sum_{i<j}J(L_{ij},L_{ji}),\qquad
\sigma=(s/3)\Phi.
\]
At \(\varepsilon=0\), the absent w state leaves the optimal three-state ring. Terms involving w are exactly linear in \(\varepsilon\), by homogeneity of J. The remaining terms are smooth for sufficiently small \(\varepsilon\).

Put \(\Lambda=\log(1/q)\), \(h_+=\Lambda+D\), \(h_-=-\Lambda-D/q\). Differentiating the three old edges gives
\[
\begin{aligned}
d_M:=\Phi'(0+)
={}&h_+\left(-1-\frac q s-\frac M4\right)
 +h_-\left(-q-\frac12-\frac{qM}4\right)\\
&+J(b,z)+J(M/2,sM/4)\\
&+J(qM/2+u,sM/4+D/2).
\end{aligned}
\tag{5}
\]
The coefficients proportional to M cancel in the large-M limit. Taylor expansion of only the last J term, at \((qM/2,zM/2)\), gives
\[
\begin{aligned}
d_\infty:=\lim_{M\to\infty}d_M
={}&-\frac34D\Lambda
 +\frac{D^2}{4}\left(1+\frac1q+\frac1z\right)\\
&+\frac{D^2}{4z}\left(\frac12\Lambda+\log z-\frac{D^2}{2q}\right)\\
={}&\frac{u^2}{1+u}
\left[3-\frac12\log(1-u^2)
-\frac{3\operatorname{arctanh}u}{u}\right].
\end{aligned}
\tag{6}
\]
The last equality uses \(q=(1-u)/(1+u)\), \(D=2u/(1+u)\), and \(z=1/(1+u)\).

For \(0<u<1\), the bracket has the convergent series
\[
\sum_{n=1}^{\infty}
\frac{1-4n}{2n(2n+1)}u^{2n}<0.
\tag{7}
\]
Thus \(d_\infty<0\). This already proves existence of a finite sufficiently large M and a positive sufficiently small \(\varepsilon\) with strictly lower entropy. The next section makes both choices explicit and supplies a strict algebraic decrease bound.

## 3. Explicit finite parameters and a quantified decrease

Define positive rational functions of q:
\[
\eta=\frac{u^4}{2(1+u)},\qquad
C_0=\left(q+z+u+\frac D2\right)
\left(\frac u q+\frac{D}{2z}\right)^2,
\qquad M=2+\frac{4C_0}{\eta}.
\tag{8}
\]
Equation (7) gives \(d_\infty\le-\eta\). The Hessian identity
\[
v^T\nabla^2J(x,y)v=(x+y)\left(\frac{v_1}x-\frac{v_2}y\right)^2
\tag{9}
\]
applied to the last term in (5), with baseline \((qM/2,zM/2)\) and offset \((u,D/2)\), gives
\[
0\le d_M-d_\infty\le C_0/M<\eta/4.
\]
Indeed, along the segment in the Taylor integral, x and y are at least \(qM/2\) and \(zM/2\), while x+y is at most \((q+z)M/2+u+D/2\); using \(M/2\ge1\) in (9) gives a remainder at most \(C_0/M\). Hence \(d_M<-3\eta/4\).

Next put
\[
B_0=4\left[
\left(q+\frac s2\right)^2+
\left(1+\frac s2\right)^2+
\left\{\frac s2\left(M+2+\frac u q\right)\right\}^2
\right],
\]
\[
\varepsilon_0=\frac{2q}{s[q(M+2)+2u]},\qquad
\varepsilon=\min\left\{\varepsilon_0,\frac{\eta}{2B_0}\right\}>0.
\tag{10}
\]
For \(0\le v\le\varepsilon_0\), each of the six old directed fluxes is at least half its value at zero. All these fluxes decrease with v, so the sum of the two fluxes on each old edge is at most its initial value 1. Their relative absolute slopes are respectively
\[
q+s/2,\qquad 1+s/2,\qquad
(s/2)(M+2+u/q).
\]
Consequently (9) gives \(\Phi''(v)\le B_0\). The new edges contribute no second derivative. Taylor's theorem and (10) yield
\[
\Phi(\varepsilon)-\Phi(0)
\le d_M\varepsilon+\frac{B_0}2\varepsilon^2
< -\frac{\eta\varepsilon}{2}<0.
\tag{11}
\]
Every rate in (3) is therefore finite and positive, the law is exact, and
\[
\sigma(Q)<(1-q)\log(1/q)-\frac{s\eta\varepsilon}{6}.
\]
This proves the theorem constructively. The parameter choice is conservative and is intended for a proof; the separate modest-rate rational example at q=1/20 gives a much larger practical separation.

## 4. The extra hidden mode

The B subgenerator has one extra decay rate
\[
\kappa=1+sM/2+
\frac{\varepsilon(sM/2+u)}{2m}.
\]
Its characteristic polynomial is
\((\lambda+\kappa)(\lambda^2+2s\lambda+c)\), while that of Q is
\[
\lambda(\lambda+\kappa)(\lambda^2+3s\lambda+3c).
\]
The quadratic factors follow from the exact transfer law; their degree is two, and the remaining root follows from the trace. Since \(M\ge2\), \(\kappa>1+q+\sqrt q\), so the added mode is distinct. It cancels from the observed dwell transform while enabling strict dissipation reduction. This is not a balanced clone that leaves entropy unchanged.

## Scope

The result proves a strict finite-state separation for every member of the family. It does not locate the four-state minimum, decide the all-finite-state infimum, prove nonattainment, or claim a universal per-state thermodynamic cost. The generator coefficients and entropy inequalities are completely explicit; no numerical optimisation is used in the theorem.
