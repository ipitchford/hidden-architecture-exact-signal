# Independent cross-audit of the two-phase theorem

Date: 26 October 2026. Internal mathematical review of `../two_phase/two_phase_theorem.md`; no external human review or proof-assistant certification.

**Verdict: no flaw found in the global analytical argument.** The restriction to at most two B states is correctly maintained and must not be dropped.

## Load-bearing checks

1. The target has reduced denominator degree two for `0<q<1`. With `ell=s-sqrt(q)`, `H=s+sqrt(q)`, `c=ell H` and `b<ell`, its numerator at the two denominator roots is `ell(H-b)>0` and `H(ell-b)>0`. Thus cancellation does not occur. For two B states the killed generator's characteristic polynomial must consequently equal the target denominator.

2. Nonnegativity of the exhaustive parameterisation is exactly the rectangle `0<=x<=b`, `ell<=y<=H` after ordering `x<y`. The inequalities `b<ell`, `ell>s/2`, and `b<s/2` are strict for `q<1`. They ensure both occupation weights are positive even on the boundary. Equal exits would give an exponential dwell and are correctly excluded.

3. Each boundary face has a positive flux with missing reverse: `x=0`, `x=b`, or `v=0` at either endpoint of y. Hence boundary entropy is infinite; no zero-occupation boundary exception was found.

4. The Möbius coordinates have exactly the stated intervals: `-q<R<q`, `-sqrt(q)<K<sqrt(q)`. The direct current identity `s j=(D^2+a h)/(a+h)` proves positivity, avoiding any assumed cycle orientation.

5. When `RK>=0`, both factors in the entropy formula have their minima at the origin. If one of R,K is nonzero, the affinity is strictly above its origin value, so equality is unique.

6. For `RK<0`, the positive-coefficient expansion and termwise AM--GM are valid for all interior `u0,v0 in (0,1)`. They yield `2 log[(1-tau^2 w)/(tau(1-w))]`. The change `z=tau w`, `C=(1-tau)/(1+tau)`, `T=(1+z)/(1-z)` has `C<CT<1`; the final monotonicity of `atanh(v)/v` is strict. This proves the claimed global lower bound, not merely a local minimum.

7. The extension to arbitrarily many A states and at most two B states uses the full alternating-renewal law and exponential A dwells in the reset replacement. These hypotheses are present. The reset replacement is an attributed corollary of a known flux merge, not an original principal theorem.

8. For a total of three states, a representation with two A states and one B state is impossible because a single B state gives an exponential B dwell; a two-state total model is likewise impossible. Thus the stated minimum is indeed the minimum over all exact three-state models with the fixed visible labels, not just a chosen topology.

## Editorial suggestions

- Add the short numerator-at-poles argument in item 1 if the proof is to be fully stand-alone.
- State explicitly in the three-state theorem or corollary why two A states and one B state cannot realise the nonexponential target.
- Use a distinct letter for the occupation vector per cycle, since `beta` is the exit distribution in the new boundary theorem; `mu` avoids a dangerous notation collision.
- The global infimum can be bounded below by the boundary theorem and above by a strict four-state competitor. Neither the two-phase theorem nor this cross-audit determines it or its attainment.

The companion mathematical manipulations were checked directly against the formulas; no numerical scan is being treated as a proof.
