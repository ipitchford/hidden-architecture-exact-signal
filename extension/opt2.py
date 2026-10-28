import numpy as np, sys
from scipy.optimize import minimize
q=1/20; s=1+q; b=2*q/s; c=1+q+q*q; m=2/s; r=s/3
# Markov params h_k = f^(k)(0): F=(b z + c)/(z^2+2 s z + c) -> h_k recurrence h_{k} = -2s h_{k-1} - c h_{k-2}, h0=b, h1=c-2 s b
h=[b,c-2*s*b]
for k in range(2,20): h.append(-2*s*h[-1]-c*h[-2])
exec(open('opt.py').read().split('n=int')[0].split('def cons')[0].split('q=1/20')[0])
src=open('opt.py').read(); exec(src[src.index('def J'):src.index('def cons')])
def cons(x,n,K):
    a,t,S,mu=stats(x,n); C=[mu.sum()-m]; v=t.copy()
    for k in range(K): C.append((a@v-h[k])/max(1,abs(h[k]))); v=S@v
    return np.array(C)
n=int(sys.argv[1]); K=int(sys.argv[2]); rng=np.random.default_rng(n*31+K)
best=np.inf
for trial in range(int(sys.argv[3])):
    x0=rng.normal(0,2,2*n+n*(n-1))
    try: res=minimize(sig,x0,args=(n,),constraints={'type':'eq','fun':cons,'args':(n,K)},method='SLSQP',options={'maxiter':4000,'ftol':1e-13},bounds=[(-30,30)]*len(x0))
    except Exception: continue
    if np.isfinite(res.fun) and np.max(abs(cons(res.x,n,K)))<1e-8 and res.fun<best: best=res.fun; bx=res.x
print(n,K,best)
if len(sys.argv)>4:
    a,t,S,mu=stats(bx,n); np.set_printoptions(precision=5,suppress=True); print(a,t,mu,S,sep='\n')
