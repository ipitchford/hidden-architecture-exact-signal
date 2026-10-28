"""Exact Fraction identities and 60-digit entropy checks; no optional dependencies."""
if not __debug__:
    raise RuntimeError('Run without -O: verification uses assertions')
from fractions import Fraction as F
from decimal import Decimal, localcontext
import random, json
from pathlib import Path

def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)
def check(q,x,y):
    s=1+q; b=2*q/s; c=1+q+q*q; D=1-q
    u=(x*x-2*s*x+c)/(y-x); v=-(y*y-2*s*y+c)/(y-x)
    al=((y-b)/(y-x),(b-x)/(y-x))
    be=((2*y/s-1)/(y-x),(1-2*x/s)/(y-x))
    S=((-x-u,u),(v,-y-v))
    assert all(z>0 for z in [x,y,u,v,*al,*be])
    assert S[0][0]+S[1][1]==-2*s
    assert S[0][0]*S[1][1]-u*v==c
    assert al[0]*x+al[1]*y==b
    assert sum(al)==1 and sum(be)==2/s and be[0]*x+be[1]*y==1
    for j in range(2): assert sum(be[i]*S[i][j] for i in range(2))==-al[j]
    # Numerator of alpha(zI-S)^-1*t is exactly b*z+c.
    assert al[0]*(-S[1][1]*x+u*y)+al[1]*(v*x-S[0][0]*y)==c
    Q=((-s,s*al[0],s*al[1]),(x,-x-u,u),(y,v,-y-v))
    pi=(F(1,3),s/3*be[0],s/3*be[1])
    assert sum(pi)==1
    for i in range(3): assert sum(Q[i])==0
    for j in range(3): assert sum(pi[i]*Q[i][j] for i in range(3))==0
    assert sum(Q[i][i] for i in range(3))==-3*s
    assert sum(Q[i][i]*Q[j][j]-Q[i][j]*Q[j][i] for i in range(3) for j in range(i+1,3))==3*c
    # Determinant independently checked by six permutations.
    assert Q[0][0]*Q[1][1]*Q[2][2]+Q[0][1]*Q[1][2]*Q[2][0]+Q[0][2]*Q[1][0]*Q[2][1]-Q[0][2]*Q[1][1]*Q[2][0]-Q[0][1]*Q[1][0]*Q[2][2]-Q[0][0]*Q[1][2]*Q[2][1]==0
    j=(x+y-b-2*x*y/s)/(y-x)
    assert al[0]-be[0]*x==j==be[0]*u-be[1]*v==be[1]*y-al[1]
    aa=s-2*x; hh=2*y-s
    R=(aa-D)/(aa+D);K=(hh-D)/(hh+D)
    assert abs(R)<q and K*K<q
    assert s*j==D*(1+R*K)/(1-R*K)
    affinity_ratio=al[0]*u*y/(al[1]*v*x)
    transformed_ratio=(1-q*R*R)*(1-q*q*K*K)/((q*q-R*R)*(q-K*K))
    assert affinity_ratio==transformed_ratio
    with localcontext() as ctx:
        ctx.prec=60
        entropy=Decimal(0)
        for i in range(3):
            for k in range(i+1,3):
                f=pi[i]*Q[i][k];g=pi[k]*Q[k][i]
                entropy += dec(f-g)*(dec(f)/dec(g)).ln()
        cyc=dec(s*j/3)*dec(affinity_ratio).ln()
        target=dec(D)*dec(1/q).ln()
        err=abs(cyc-entropy)
        assert err<Decimal('1e-53')
        assert cyc-target>=-Decimal('1e-53')
        return {'gap':str(cyc-target),'entropy':str(cyc),'target':str(target),'error':str(err),'opposite_signs':R*K<0}

rng=random.Random(20261026)
records=[]
# Deliberately include the exact benchmark and regimes close to equilibrium.
qs=[F(1,20),F(1,4),F(1,2),F(1,1000),F(99,100)]+[F(rng.randint(1,999),1000) for _ in range(95)]
for q in qs:
    s=1+q;b=2*q/s
    for _ in range(10):
        x=b*F(rng.randint(1,999),1000)
        while True:
            delta=F(rng.randint(-999,999),1000)
            if delta*delta<q:break
        y=s+delta
        records.append(check(q,x,y))
rings=[]
for q in [F(1,20),F(1,4),F(1,2)]:
    result=check(q,q,F(1));result['q']=str(q);rings.append(result)
summary={'description':'Exact two-phase identities and 60-digit entropy comparisons',
         'seed':20261026,'random_models':len(records),'exact_checks':['PH trace and determinant','exact transfer numerator','occupation and entrance equations','generator rows and stationarity','full characteristic polynomial','three equal cycle currents','coordinate domain and rational current identity','exact rational affinity factorisation'],
         'opposite_sign_models':sum(r['opposite_signs'] for r in records),
         'minimum_random_entropy_gap':str(min(Decimal(r['gap']) for r in records)),
         'maximum_direct_vs_cycle_entropy_error':str(max(Decimal(r['error']) for r in records)),
         'ring_instances':rings,'all_assertions_passed':True,
         'scope':'Numerical checks support the analytic proof; no all-dimension optimality follows.'}
path=Path(__file__).with_name('two_phase_checks.json');path.write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
