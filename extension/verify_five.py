"""Standard-library-only exact certificate for a rational five-state (1A+4B) realisation of P_{1/20}.
State 0 is labelled A; states 1..4 are labelled B. All arithmetic is rational."""
from fractions import Fraction as F
q=F(1,20); s=1+q; b=2*q/s
Q=[[F(-21,20),F(1113,80000),F(1701,80000),F(50952901,51480000),F(129029,5148000)],
   [F(139,125),F(-63247,46500),F(11539,46500),F(0),F(0)],
   [F(463,500),F(897,1000),F(-1257919,469000),F(0),F(100733,117250)],
   [F(6,125),F(0),F(0),F(-246223,160875),F(238501,160875)],
   [F(1383,2000),F(0),F(2323,1000),F(33907,46800),F(-54683,14625)]]
n=5; ok=True
def check(name,cond):
    global ok; ok&=bool(cond); print(('ok   ' if cond else 'FAIL ')+name)
check('row sums zero',all(sum(r)==0 for r in Q))
check('off-diagonals nonnegative',all(Q[i][j]>=0 for i in range(n) for j in range(n) if i!=j))
check('zeros come in reciprocal pairs',all((Q[i][j]==0)==(Q[j][i]==0) for i in range(n) for j in range(n) if i!=j))
check('A holding rate 21/20',-Q[0][0]==s)
m=n-1
S=[r[1:] for r in Q[1:]]; t=[Q[i][0] for i in range(1,n)]; alpha=[x/s for x in Q[0][1:]]
one=[F(1)]*m
def mv(M,v): return [sum(M[i][j]*v[j] for j in range(m)) for i in range(m)]
def vm(v,M): return [sum(v[i]*M[i][j] for i in range(m)) for j in range(m)]
dot=lambda u,v: sum(x*y for x,y in zip(u,v))
# mu = alpha(-S)^{-1}: solve mu(-S)=alpha, i.e. (-S)^T mu^T = alpha^T by exact elimination
A=[[-S[j][i] for j in range(m)]+[alpha[i]] for i in range(m)]
for c in range(m):
    p=next(r for r in range(c,m) if A[r][c]!=0); A[c],A[p]=A[p],A[c]
    for r in range(m):
        if r!=c and A[r][c]!=0:
            f=A[r][c]/A[c][c]; A[r]=[x-f*y for x,y in zip(A[r],A[c])]
mu=[A[i][m]/A[i][i] for i in range(m)]
check('alpha 1 = 1',sum(alpha)==1)
check('S 1 = -t',mv(S,one)==[-x for x in t])
check('mu S = -alpha',vm(mu,S)==[-x for x in alpha])
check('mu 1 = 40/21',sum(mu)==F(40,21))
check('mu t = 1',dot(mu,t)==1)
check('alpha t = 2/21',dot(alpha,t)==F(2,21))
S1=mv(S,one); S2=mv(S,S1)
check('(S^2+(21/10)S+(421/400)I)1 = 0',all(S2[i]+F(21,10)*S1[i]+F(421,400)==0 for i in range(m)))
check('mu > 0',all(x>0 for x in mu))
r=s/3; pi=[F(1,3)]+[r*x for x in mu]
check('pi sums to 1',sum(pi)==1)
check('pi Q = 0',all(sum(pi[i]*Q[i][j] for i in range(n))==0 for j in range(n)))
print('pi =',[str(x) for x in pi]); print('mu =',[str(x) for x in mu])
# rational log enclosures: log x = 2 sum v^{2j+1}/(2j+1) + R_N, 0<R_N<=2v^{2N+1}/((2N+1)(1-v^2)), x>1
def logser(x,N=60):
    v=(x-1)/(x+1); lo=sum(2*v**(2*j+1)/(2*j+1) for j in range(N))
    return lo, lo+2*v**(2*N+1)/((2*N+1)*(1-v*v))
L2=logser(F(2))
def logenc(x):
    if x==1: return F(0),F(0)
    if x<1: lo,hi=logenc(1/x); return -hi,-lo
    k=0
    while x>=2: x/=2; k+=1          # dyadic range reduction, x in [1,2)
    lo,hi=logser(x); return lo+k*L2[0], hi+k*L2[1]
lo=hi=F(0); terms=0
for i in range(n):
    for j in range(i+1,n):
        x,y=pi[i]*Q[i][j],pi[j]*Q[j][i]
        if x==0 and y==0: continue
        c=x-y; l,h=logenc(x/y)
        if c>=0: lo+=c*l; hi+=c*h
        else: lo+=c*h; hi+=c*l
        terms+=1
print('present unoriented edges:',terms)
check('stated enclosure 2.746985402969 < sigma < 2.746985402970',lo>F(2746985402969,10**12) and hi<F(2746985402970,10**12))
print('sigma in [%.12f, %.12f]'%(float(lo),float(hi)))
check('sigma upper < 2.7470',hi<F(27470,10000))
check('sigma upper < 2.7659977 (below the improved four-state certificate)',hi<F(27659977,10**7))
l20=logenc(F(20)); V3lo=F(19,20)*l20[0]
print('certified gap to V3 = (19/20)log20 exceeds %.9f'%float(V3lo-hi))
check('sigma < V3',hi<V3lo)
print('PASS' if ok else 'FAIL')
raise SystemExit(0 if ok else 1)
