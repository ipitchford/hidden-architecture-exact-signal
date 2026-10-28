#!/usr/bin/env python3
"""Standalone rational certificate for the practical four-state example.

Only Python's standard library is used. Checks remain active under -O.
The determinant/transfer calculation is independent of the ODE annihilator.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def add(a, b):
    n = max(len(a), len(b))
    out = [(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0)) for i in range(n)]
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out

def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out

def determinant_polynomial(a):
    n = len(a)
    out = [F(0)]
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        term = [F((-1)**inv)]
        for i in range(n):
            term = mul(term, a[i][p[i]])
        out = add(out, term)
    return out

def series_interval(x, n=72):
    require(1 <= x <= 2, 'Range-reduced logarithm outside [1,2]')
    v=(x-1)/(x+1); power=v; total=F(0)
    for j in range(n):
        total += power/(2*j+1)
        power *= v*v
    lo=2*total
    return lo, lo+2*power/((2*n+1)*(1-v*v))

def log_interval(x):
    require(x > 0, 'Logarithm argument must be positive')
    if x < 1:
        lo, hi = log_interval(1/x)
        return -hi, -lo
    k=0
    while x > 2:
        x /= 2; k += 1
    lo, hi=series_interval(x)
    l2,h2=series_interval(F(2))
    return lo+k*l2, hi+k*h2

def outward_decimal(x, places, up=False):
    scale=10**places
    n=x.numerator*scale//x.denominator
    if up and F(n, scale) < x:
        n += 1
    sign='-' if n < 0 else ''
    n=abs(n)
    return f'{sign}{n//scale}.{n%scale:0{places}d}'

def main():
    q=F(1,20);s=1+q;b=2*q/s;c=1+q+q*q
    Q=[[-s,F(4781,4800),F(31,1200),F(9,320)],
       [q,-F(79,60),F(19,15),F(0)],
       [F(4,5),F(1,3),-F(131,60),F(21,20)],
       [F(21,20),F(0),F(1,5),-F(5,4)]]
    pi=[F(1,3),F(217,720),F(7,36),F(41,240)]
    require(all(sum(row)==0 for row in Q),'Rows do not sum to zero')
    require(sum(pi)==1 and min(pi)>0,'Invalid stationary probability')
    require(all(sum(pi[i]*Q[i][j] for i in range(4))==0 for j in range(4)), 'Stationarity failed')
    require(all(Q[i][j]>=0 for i in range(4) for j in range(4) if i!=j),'Negative rate')
    require(all(Q[0][i]>0 and Q[i][0]>0 for i in range(1,4)), 'Irreducibility star absent')
    S=[row[1:] for row in Q[1:]]
    t=[row[0] for row in Q[1:]]
    alpha=[v/s for v in Q[0][1:]]
    a=[[[(-S[i][j]), F(i==j)] for j in range(3)] for i in range(3)]
    den=determinant_polynomial(a)
    numerator=[F(0)]
    for j in range(3):
        aj=[[list(v) for v in row] for row in a]
        for i in range(3):
            aj[i][j]=[t[i]]
        numerator=add(numerator,[alpha[j]*v for v in determinant_polynomial(aj)])
    extra=[F(53,20),F(1)]
    require(den==mul(extra,[c,2*s,F(1)]),'Incorrect denominator factorisation')
    require(numerator==mul(extra,[c,b]),'Incorrect exact transfer numerator')
    ep_lo=ep_hi=F(0); flux_rows=[]
    for i in range(4):
        for j in range(i+1,4):
            x=pi[i]*Q[i][j];y=pi[j]*Q[j][i]
            if x==y==0:
                continue
            require(x>0 and y>0,'Infinite entropy edge')
            ratio=max(x,y)/min(x,y); gap=abs(x-y)
            lo,hi=log_interval(ratio)
            ep_lo+=gap*lo;ep_hi+=gap*hi
            flux_rows.append({'edge':[i,j],'forward':str(x),'reverse':str(y),'coefficient':str(gap),'log_argument':str(ratio)})
    lo,hi=log_interval(1/q)
    ring_lo=(1-q)*lo;ring_hi=(1-q)*hi
    require(ep_hi<F(2774,1000)<F(2845,1000)<ring_lo, 'Strict architecture comparison failed')
    require(ring_lo-ep_hi>F(72869002,10**9),'Quantified absolute gap failed')
    require((ring_lo-ep_hi)/ring_hi>F(256,10000),'2.56 percent certificate failed')
    lower=(F(2,3)*ring_lo,F(2,3)*ring_hi)
    out={'status':'PASS','all_checks_use_exact_rational_arithmetic':True,
      'logarithm_method':'72-term atanh series after dyadic reduction, with exact rational remainder',
      'generator':[[str(v) for v in row] for row in Q], 'stationary_distribution':list(map(str,pi)),
      'B_transfer_numerator_ascending':list(map(str,numerator)),
      'B_transfer_denominator_ascending':list(map(str,den)),
      'cancelled_factor_ascending':list(map(str,extra)),
      'four_state_entropy_enclosure':[outward_decimal(ep_lo,25),outward_decimal(ep_hi,25,True)],
      'three_state_minimum_enclosure':[outward_decimal(ring_lo,25),outward_decimal(ring_hi,25,True)],
      'unrestricted_lower_bound_enclosure':[outward_decimal(lower[0],25),outward_decimal(lower[1],25,True)],
      'entropy_saving_lower_bound':outward_decimal(ring_lo-ep_hi,25),
      'fractional_saving_lower_bound':outward_decimal((ring_lo-ep_hi)/ring_hi,25),
      'fluxes':flux_rows,
      'scope':'Exact feasibility and strict comparison to the separately proved three-state minimum; no four-state optimum claimed.'}
    path=ROOT/'results'/'exact_certificate.json';path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','four_state_entropy_enclosure','three_state_minimum_enclosure','unrestricted_lower_bound_enclosure','fractional_saving_lower_bound']},indent=2))

if __name__=='__main__':
    main()
