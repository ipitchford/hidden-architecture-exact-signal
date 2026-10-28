"""Right-annihilator (R) stratum search for 1A+nB exact realisations of P_q.
Feasible set (generic): p(S)1=0 [R] or alpha p(S)=0 [L]; L is the time reversal of R
(same cost), so searching R suffices. With t=-S1, p(S)1=0 <=> for each row i:
  sum_{j!=i} S_ij (t_j - t_i) = (t_i - s)^2 - q      (row-decoupled, linear in S)
plus alpha 1 = 1, alpha t = b."""
import numpy as np, itertools, json, sys
from scipy.optimize import minimize

def J(x,y):
    if x==0 and y==0: return 0.0
    if x<=0 or y<=0: return np.inf
    return (x-y)*np.log(x/y)

class Stratum:
    def __init__(s_, q, n, zero_edges):
        s_.q=q; s_.n=n; s_.s=1+q; s_.b=2*q/(1+q); s_.r=(1+q)/3
        # edges: ('A',i) or (i,j) i<j
        s_.zA=[i for i in range(n) if ('A',i) in zero_edges]
        s_.zB=[(i,j) for (i,j) in itertools.combinations(range(n),2) if (i,j) in zero_edges]
        s_.offd=[(i,j) for i in range(n) for j in range(n) if i!=j and (min(i,j),max(i,j)) not in s_.zB]
        s_.tidx=[i for i in range(n) if i not in s_.zA]
        s_.nv=len(s_.tidx)+len(s_.offd)+len(s_.tidx)
    def unpack(s_,p):
        n=s_.n; e=np.exp(np.clip(p,-60,60)); k=0
        t=np.zeros(n); a=np.zeros(n); S=np.zeros((n,n))
        for i in s_.tidx: t[i]=e[k]; k+=1
        for (i,j) in s_.offd: S[i,j]=e[k]; k+=1
        for i in s_.tidx: a[i]=e[k]; k+=1
        S-=np.diag(S.sum(1)+t); return S,t,a
    def eqs(s_,p):
        S,t,a=s_.unpack(p); n=s_.n; out=[]
        for i in range(n):
            out.append(sum(S[i,j]*(t[j]-t[i]) for j in range(n) if j!=i)-((t[i]-s_.s)**2-s_.q))
        out.append(a.sum()-1); out.append(a@t-s_.b); return np.array(out)
    def cost_full(s_,S,t,a):
        n=s_.n
        try: mu=np.linalg.solve(-S.T,a)
        except Exception: return np.inf
        if np.any(mu<=0): return np.inf
        c=sum(J(a[i],mu[i]*t[i]) for i in range(n))
        c+=sum(J(mu[i]*S[i,j],mu[j]*S[j,i]) for i in range(n) for j in range(i+1,n))
        return s_.r*c
    def cost(s_,p):
        v=s_.cost_full(*s_.unpack(p)); return v if np.isfinite(v) else 1e3
    def run(s_,starts,seed,maxiter=500):
        rng=np.random.default_rng(seed); best=(np.inf,None)
        for k in range(starts):
            p0=rng.normal(0,1.2,s_.nv)
            try:
                res=minimize(s_.cost,p0,method='SLSQP',constraints={'type':'eq','fun':s_.eqs},
                             options={'maxiter':maxiter,'ftol':1e-14})
            except Exception: continue
            if np.max(abs(s_.eqs(res.x)))<1e-9 and res.fun<best[0]-1e-12 and res.fun<1e2:
                best=(res.fun,res.x)
        return best

def connected(n,zero):
    nodes=['A']+list(range(n)); adj={v:set() for v in nodes}
    for i in range(n):
        if ('A',i) not in zero: adj['A'].add(i); adj[i].add('A')
    for i,j in itertools.combinations(range(n),2):
        if (i,j) not in zero: adj[i].add(j); adj[j].add(i)
    seen={'A'}; st=['A']
    while st:
        v=st.pop()
        for w in adj[v]:
            if w not in seen: seen.add(w); st.append(w)
    return len(seen)==n+1

def all_edges(n): return [('A',i) for i in range(n)]+list(itertools.combinations(range(n),2))

def strata(n,maxzero):
    E=all_edges(n)
    for k in range(maxzero+1):
        for Z in itertools.combinations(E,k):
            if connected(n,set(Z)): yield set(Z)
