import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
import itertools, numpy as np
from core import Stratum
q=F(1,20); s=1+q; b=2*q/s
def build(t1,t2,t3,S21,a1):
    h=lambda ti:(ti-s)**2-q
    S12=h(t1)/(t2-t1); S32=h(t3)/(t2-t3)
    S23=(h(t2)-S21*(t1-t2))/(t3-t2)
    # alpha: a1+a2+a3=1, a1 t1+a2 t2+a3 t3=b
    a2=(b-a1*t1-(1-a1)*t3)/(t2-t3); a3=1-a1-a2
    t=[t1,t2,t3]; off={(0,1):S12,(1,0):S21,(1,2):S23,(2,1):S32}
    S=[[F(0)]*3 for _ in range(3)]
    for (i,j),v in off.items(): S[i][j]=v
    for i in range(3): S[i][i]=-t[i]-sum(S[i][j] for j in range(3) if j!=i)
    return S,t,[a1,a2,a3]
st=Stratum(0.05,3,set())
def fcost(S,t,a):
    if min(S[0][1],S[1][0],S[1][2],S[2][1],*a,*t)<=0: return np.inf
    return st.cost_full(np.array(S,float),np.array(t,float),np.array(a,float))
x0=dict(t1=1.072372,t2=0.770718,t3=0.048434,S21=0.930773,a1=0.022951)
for D in [20,40,80,100,200,400,1000]:
    best=(np.inf,None)
    cands={k:[F(round(v*D)+d,D) for d in (-1,0,1)] for k,v in x0.items()}
    for combo in itertools.product(*cands.values()):
        S,t,a=build(*combo); c=fcost(S,t,a)
        if c<best[0]: best=(c,combo)
    print(D,best[0],best[1] and [str(x) for x in best[1]])
for D in [1000,2000]:
    cur=[F(round(v*D),D) for v in x0.values()]; cc=fcost(*build(*cur))
    improved=True
    while improved:
        improved=False
        for k in range(5):
            for d in (-1,1):
                tr=list(cur); tr[k]+=F(d,D); c=fcost(*build(*tr))
                if c<cc-1e-13: cur,cc,improved=tr,c,True
    print('CD',D,cc,[str(x) for x in cur])
