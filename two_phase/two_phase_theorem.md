# Exact two-phase minimum for the renewal family

Date: 26 October 2026. Status: proved below; independent checking requested. No all-architecture optimum is asserted.

## Theorem

Fix \(0<q<1\), and write
\[
s=1+q,\quad b=2q/s,\quad c=1+q+q^2,\quad D=1-q.
\]
Consider all irreducible three-state continuous-time Markov chains with one state labelled A and two states labelled B whose complete observed stationary law is the alternating-renewal law with A dwell \(\operatorname{Exp}(s)\) and B-dwell transform
\[
\widehat f(z)=(bz+c)/(z^2+2sz+c).
\]
The minimum stationary entropy-production rate is
\[
\boxed{(1-q)\log(1/q).}
\]
It is attained, uniquely up to swapping the two B states, by
\[
Q_q=\begin{pmatrix}-s&1&q\\q&-s&1\\1&q&-s\end{pmatrix},\qquad \pi=(1/3,1/3,1/3).
\]
Here ordinary reversal applies to even variables, natural logarithms are used, and Boltzmann's constant is one. The reverse of this ring equals the original ring after swapping the B states.

More generally the same lower bound holds for any finite exact realization with **at most two B-labelled states**, regardless of the number of A-labelled states: the attributed stationary-flux reset replacement contracts its entropy into the three-state class. This extension depends on the exact alternating-renewal law, not merely on the marginal A dwell being exponential.

## 1. Exhaustive two-phase parametrisation

Write the B subgenerator, entrance row, and exits as
\[
S=\begin{pmatrix}-(x+u)&u\\v&-(y+v)\end{pmatrix},\quad
\alpha=(a_0,1-a_0),\quad t=(x,y)^T.
\]
The target rational function has reduced degree two: its poles are \(-\ell,-H\), with \(\ell=s-\sqrt q\), \(H=s+\sqrt q\), and both residues are nonzero for \(q<1\). Therefore every two-state representation is minimal and its characteristic polynomial is exactly the target denominator. Equal exits would make the dwell exponential and are excluded. Relabel so \(x<y\). Matching trace, determinant and \(f(0)\) gives
\[
u=\frac{x^2-2sx+c}{y-x},\qquad
v=-\frac{y^2-2sy+c}{y-x},\qquad
\alpha=\left(\frac{y-b}{y-x},\frac{b-x}{y-x}\right).
\tag{1}
\]
Since \(0<b<\ell<H\), nonnegativity is equivalent to
\[
0\le x\le b,\qquad \ell\le y\le H.
\tag{2}
\]
Indeed \(\alpha t=b\) requires \(x\le b\le y\), hence \(x<\ell\); \(v\ge0\) then places \(y\in[\ell,H]\), and \(u>0\) follows automatically. Conversely these constraints give a transient subgenerator with the required transform.

Every boundary point of (2) has infinite entropy: \(x=0\) or \(x=b\) deletes exactly one direction of a positive boundary flux, while \(y=\ell\) or \(y=H\) makes \(v=0<u\). All states are used, and all stationary masses remain positive. It therefore suffices to minimise over the open rectangle.

The mean B dwell is \(2/s\), so the stationary cycle intensity is \(r_0=s/3\), and its occupation vector per cycle is
\[
\beta=\alpha(-S)^{-1}
=\left(\frac{2y/s-1}{y-x},\frac{1-2x/s}{y-x}\right).
\]
The stationary distribution is \(\pi=(1/3,r_0\beta_1,r_0\beta_2)\).

The dimensionless clockwise current per cycle is
\[
j=\alpha_1-\beta_1x
=\frac{x+y-b-2xy/s}{y-x}>0.
\]
By stationarity this is also \(\beta_1u-\beta_2v=\beta_2y-\alpha_2\). The rate of entropy production is consequently
\[
\sigma=\frac{s}{3}j\,\mathcal A,\qquad
\mathcal A=\log\frac{\alpha_1uy}{\alpha_2vx}.
\tag{3}
\]

## 2. Coordinates centred on the uniform ring

Define
\[
a=s-2x,\quad h=2y-s,\quad
R=\frac{a-D}{a+D},\quad K=\frac{h-D}{h+D}.
\]
In the open rectangle,
\[
-q<R<q,\qquad -\sqrt q<K<\sqrt q.
\tag{4}
\]
This follows from \(a\in(D^2/s,s)\), \(h\in(s-2\sqrt q,s+2\sqrt q)\), and \((s-2\sqrt q)(s+2\sqrt q)=D^2\).

Straight algebra reduces (3) to
\[
\sigma=\frac D3\frac{1+RK}{1-RK}\,
\log\frac{(1-qR^2)(1-q^2K^2)}{(q^2-R^2)(q-K^2)}.
\tag{5}
\]
For transparency, the current part is
\[
sj=\frac{D^2+ah}{a+h}=D\frac{1+RK}{1-RK}.
\]
The affinity separates into a function of \(R^2\) and a function of \(K^2\). Both are minimised at zero, where their sum is \(3\log(1/q)\).

## 3. Global inequality

If \(RK\ge0\), both factors in (5) are bounded below by their values at zero. Thus the asserted minimum follows immediately; equality requires \(R=K=0\).

Suppose \(RK<0\). Put
\[
u_0=|R|/q,\quad v_0=|K|/\sqrt q,\quad
\tau=q^{3/2},\quad w=u_0v_0\in(0,1).
\]
The affinity becomes
\[
\mathcal A=-2\log\tau+
\log\frac{1-\tau^2u_0^2}{1-u_0^2}+
\log\frac{1-\tau^2v_0^2}{1-v_0^2}.
\]
Since
\[
\log\frac{1-\tau^2z^2}{1-z^2}
=\sum_{n=1}^{\infty}\frac{1-\tau^{2n}}n z^{2n},
\]
all coefficients are positive. Termwise AM–GM yields
\[
\mathcal A\ge
2\log\frac{1-\tau^2w}{\tau(1-w)}.
\tag{6}
\]
The current factor is \((1-\tau w)/(1+\tau w)\). Set
\[
z=\tau w\in(0,\tau),\qquad
C=\frac{1-\tau}{1+\tau},\qquad
T=\frac{1+z}{1-z}>1.
\]
Here \(0<C<CT<1\), because \(z<\tau\). The lower bound obtained by multiplying (6) by the current factor is
\[
\frac{1-z}{1+z}\,2\log\frac{1-\tau z}{\tau-z}
=\frac4T\operatorname{arctanh}(CT)
>4\operatorname{arctanh}(C)
=2\log(1/\tau).
\tag{7}
\]
The strict step follows from strict increase of \(\operatorname{arctanh}(v)/v\) on \((0,1)\); for example its power series has positive coefficients. Since \(2\log(1/\tau)=3\log(1/q)\), (5) proves the claimed bound, strictly in this case.

Equality is therefore possible only when \(R=K=0\). This gives \(a=h=D\), hence \(x=q\), \(y=1\), \(u=1\), \(v=q\), and \(\alpha=(1/s,q/s)\), exactly the stated ring. This completes the global proof without a numerical optimisation or fixed-dimension compactification assumption.

## 4. Consequences and limits

* Every three-state exact realization of the target has characteristic polynomial \(z(z^2+3sz+3c)\), but this spectral identity is not used as an unproved entropy bound.
* The exact parameterisation and the analytic inequality certify a **physical architecture restriction**. They do not make the two-state PH representation thermodynamically sufficient among all hidden dimensions.
* For \(q=1/20\), the exact minimum within this class is \((19/20)\log20=2.845945659876291\ldots\).
* Any exact higher-dimensional competitor with a strictly smaller entropy rate would refute sufficiency of the minimal three-state realization. No such competitor is constructed in this note.

## Source boundary

The full-PH cancellation equations and general stationary-flux entropy formula are in Aznagulov (2026), Sections 8.5–8.7, https://arxiv.org/html/2609.14623v1. That source does not solve this two-phase optimisation in the inspected text. Skinner–Dunkel (2021) supplies the reset contraction used in the extension. Full-law matching is stronger than optimising the first two dwell moments, as in Skinner–Dunkel's supplementary numerical framework. A bounded formula-level priority search remains part of the paper's evidence audit; the theorem above is an independently derived proof, not a historical-priority certification.
