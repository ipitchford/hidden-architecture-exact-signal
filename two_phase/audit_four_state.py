"""Independent exact audit of the coordinator's four-state competitor."""
if not __debug__:
    raise RuntimeError('Run without -O: verification uses assertions')
from fractions import Fraction as F
from decimal import Decimal,localcontext
from pathlib import Path
import json
Q=[[-F(21,20),F(4781,4800),F(31,1200),F(9,320)],
   [F(1,20),-F(79,60),F(19,15),F(0)],
   [F(4,5),F(1,3),-F(131,60),F(21,20)],
   [F(21,20),F(0),F(1,5),-F(5,4)]]
pi=[F(1,3),F(217,720),F(7,36),F(41,240)]
s=F(21,20);q=F(1,20);b=F(2,21);c=F(421,400)
alpha=[F(683,720),F(31,1260),F(3,112)]
mu=[F(31,36),F(5,9),F(41,84)]
S=[row[1:] for row in Q[1:]];t=[Q[i][0] for i in range(1,4)]
assert sum(pi)==1 and all(v>0 for v in pi)
assert all(sum(row)==0 for row in Q)
assert all(Q[i][j]>=0 for i in range(4) for j in range(4) if i!=j)
assert all(sum(pi[i]*Q[i][j] for i in range(4))==0 for j in range(4))
assert sum(alpha)==1 and sum(mu)==F(40,21)
assert all(Q[0][i+1]==s*alpha[i] for i in range(3))
assert all(mu[i]*s/3==pi[i+1] for i in range(3))
assert all(sum(mu[i]*S[i][j] for i in range(3))==-alpha[j] for j in range(3))
assert sum(alpha[i]*t[i] for i in range(3))==b
S1=[sum(row) for row in S]
S21=[sum(S[i][j]*S1[j] for j in range(3)) for i in range(3)]
assert all(S21[i]+2*s*S1[i]+c==0 for i in range(3))
# Strict killing in every phase guarantees transience by row diagonal dominance.
assert all(z>0 for z in t)
# Connected bidirectional star through A guarantees irreducibility.
assert all(Q[0][i]>0 and Q[i][0]>0 for i in range(1,4))
# An independent rational resolvent solve at four points checks the reduced transform.
def solve(A,bv):
    A=[list(row)+[v] for row,v in zip(A,bv)]
    n=len(A)
    for j in range(n):
        k=next(k for k in range(j,n) if A[k][j])
        A[j],A[k]=A[k],A[j]
        v=A[j][j];A[j]=[x/v for x in A[j]]
        for i in range(n):
            if i!=j:
                v=A[i][j];A[i]=[x-v*y for x,y in zip(A[i],A[j])]
    return [row[-1] for row in A]
for z in [F(0),F(1,10),F(1),F(10)]:
    X=solve([[z*(i==j)-S[i][j] for j in range(3)] for i in range(3)],t)
    assert sum(alpha[i]*X[i] for i in range(3))==(b*z+c)/(z*z+2*s*z+c)
# Rigorous rational logarithm bounds for ratios >=1.
def log_interval(r,N=300):
    assert r>=1
    w=(r-1)/(r+1);w2=w*w
    wpow=w;total=F(0)
    for k in range(N):
        total+=wpow/F(2*k+1)
        wpow*=w2
    lo=2*total
    rem=2*wpow/(F(2*N+1)*(1-w2))
    return lo,lo+rem
lo=hi=F(0);edges=[]
for i in range(4):
 for j in range(i+1,4):
    f=pi[i]*Q[i][j];g=pi[j]*Q[j][i]
    if f==g==0:continue
    assert min(f,g)>0
    r=max(f,g)/min(f,g);dif=abs(f-g)
    l,h=log_interval(r);lo+=dif*l;hi+=dif*h
    edges.append({'edge':[i,j],'fluxes':[str(f),str(g)],'log_ratio':str(r)})
rl,rh=log_interval(F(20));rl*=F(19,20);rh*=F(19,20)
assert F(2773076657,10**9)<lo<hi<F(2773076658,10**9)
assert lo<hi<rl<rh
assert rl-hi>F(72,1000)
def d(x):
 with localcontext() as ctx:
    ctx.prec=60
    return str(Decimal(x.numerator)/Decimal(x.denominator))
out={'all_exact_checks_passed':True,'generator':[[str(x) for x in row] for row in Q],
     'pi':[str(x) for x in pi],'alpha':[str(x) for x in alpha],'mu':[str(x) for x in mu],
     'annihilator':'(S^2+2sS+cI)1=0 exactly','initial_density':'alpha*t=2/21 exactly',
     'transform':'(800z+8841)/(21(400z^2+840z+421))',
     'entropy_rationally_certified_decimal_bracket':['2.773076657','2.773076658'],
     'entropy_series_lower_approximation':d(lo),'entropy_series_upper_approximation':d(hi),
     'entropy_interval_width':d(hi-lo),'ring_minus_competitor_lower_bound':d(rl-hi),
     'method':'Rational atanh series with N=300, exact explicit geometric remainder bound',
     'edges':edges,'scope':'Exact feasible strict improvement; no four-state global minimum asserted.'}
Path(__file__).with_name('four_state_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
