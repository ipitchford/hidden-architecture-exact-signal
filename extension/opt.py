import numpy as np, sys
from scipy.optimize import minimize
q=1/20; s=1+q; b=2*q/s; c=1+q+q*q; m=2/s; r=s/3; f1=c-4*q
LB=2/3*(1-q)*np.log(1/q)
def J(x,y): return (x-y)*np.log(x/y)
def unpack(x,n):
    a=np.exp(x[:n]); a/=a.sum()
    t=np.exp(x[n:2*n]); W=np.exp(x[2*n:]).reshape(n,n-1)
    S=np.zeros((n,n))
    for i in range(n):
        S[i,[j for j in range(n) if j!=i]]=W[i]
    S[np.diag_indices(n)]=-(S.sum(1)+t)
    return a,t,S
def stats(x,n):
    a,t,S=unpack(x,n); mu=np.linalg.solve(-S.T,a)
    return a,t,S,mu
def sig(x,n):
    a,t,S,mu=stats(x,n); v=sum(J(a[i],mu[i]*t[i]) for i in range(n))
    for i in range(n):
        for j in range(i+1,n): v+=J(mu[i]*S[i,j],mu[j]*S[j,i])
    return r*v
def cons(x,n,use1):
    a,t,S,mu=stats(x,n); C=[mu.sum()-m, a@t-b]
    if use1: C.append(a@S@t-f1)
    return np.array(C)
n=int(sys.argv[1]); use1=int(sys.argv[2]); rng=np.random.default_rng(n*7+use1)
best=np.inf
for trial in range(int(sys.argv[3])):
    x0=rng.normal(0,2,2*n+n*(n-1))
    try:
        res=minimize(sig,x0,args=(n,),constraints={'type':'eq','fun':cons,'args':(n,use1)},method='SLSQP',options={'maxiter':3000,'ftol':1e-12},bounds=[(-25,25)]*len(x0))
    except Exception: continue
    if res.success and np.max(abs(cons(res.x,n,use1)))<1e-7 and res.fun<best:
        best=res.fun; bx=res.x
print(n,use1,best,'LB',LB,'ring',(1-q)*np.log(1/q))
a,t,S,mu=stats(bx,n); print('alpha',a,'\nt',t,'\nS',S,'\nmu',mu,'f1',a@S@t)
