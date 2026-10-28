"""Exploratory convex fixed-exit scans; NOT a global architecture certificate."""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog, minimize

def solve(q, t):
    t=np.asarray(t,dtype=float); n=len(t); s=1+q; c=1+q+q*q
    pairs=[(i,j) for i in range(n) for j in range(n) if i!=j]
    ix={p:n+k for k,p in enumerate(pairs)}; dim=n+len(pairs)
    mu=np.zeros((n,dim)); mu[:,:n]=np.eye(n)
    beta=t[:,None]*mu
    alpha=beta.copy()
    for (i,j),k in ix.items():
        alpha[i,k]+=1; alpha[j,k]-=1
    eq=np.zeros((n+2,dim)); rhs=np.zeros(n+2)
    eq[0,:n]=1; rhs[0]=2/s
    eq[1,:n]=t; rhs[1]=1
    for i in range(n):
        eq[i+2,i]=-((t[i]-s)**2-q)
        for j in range(n):
            if i!=j: eq[i+2,ix[i,j]]=t[j]-t[i]
    # Interior feasible seed by maximising the common floor.
    obj=np.zeros(dim+1); obj[-1]=-1
    G=np.vstack((np.eye(dim),alpha))
    ub=np.hstack((-G,np.ones((len(G),1))))
    row=np.zeros(dim+1); row[n:dim]=1
    lp=linprog(obj,A_ub=np.vstack((ub,row)),b_ub=np.r_[np.zeros(len(G)),100.],
       A_eq=np.hstack((eq,np.zeros((n+2,1)))),b_eq=rhs,
       bounds=[(0,None)]*(dim+1),method='highs')
    if not lp.success or lp.x[-1]<1e-10:
        return {'q':q,'t':t.tolist(),'feasible':False,'reason':lp.message}
    left=[alpha[i] for i in range(n)]; right=[beta[i] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            x=np.zeros(dim); y=x.copy(); x[ix[i,j]]=1;y[ix[j,i]]=1
            left.append(x);right.append(y)
    left=np.array(left);right=np.array(right)
    def fun(v):
        x=left@v;y=right@v
        x=np.maximum(x,1e-16); y=np.maximum(y,1e-16)
        return s/3*np.sum((x-y)*np.log(x/y))
    def jac(v):
        x=left@v;y=right@v
        x=np.maximum(x,1e-16); y=np.maximum(y,1e-16)
        return s/3*((np.log(x/y)+1-y/x)@left+(np.log(y/x)+1-x/y)@right)
    sol=minimize(fun,lp.x[:-1],jac=jac,method='SLSQP',
        bounds=[(1e-11,None)]*dim,
        constraints=[{'type':'eq','fun':lambda v:eq@v-rhs,'jac':lambda v:eq},
                     {'type':'ineq','fun':lambda v:alpha@v-1e-11,'jac':lambda v:alpha}],
        options={'maxiter':1800,'ftol':1e-11})
    v=sol.x; m=v[:n];L=np.zeros((n,n))
    for (i,j),k in ix.items():L[i,j]=v[k]
    S=L/m[:,None];np.fill_diagonal(S,-t-S.sum(axis=1))
    out={'q':q,'t':t.tolist(),'feasible':True,'success':bool(sol.success),
      'message':sol.message,'sigma':fun(v),'ring_sigma':(1-q)*np.log(1/q),
      'eq_error':float(np.max(np.abs(eq@v-rhs))),'alpha_min':float(np.min(alpha@v)),
      'mu':m.tolist(),'alpha':(alpha@v).tolist(),'S':S.tolist(),'L':L.tolist()}
    return out

if __name__=='__main__':
    out=[]
    for q in [.05,.25,.5,.9]:
        s=1+q; ell=s-np.sqrt(q);H=s+np.sqrt(q);b=2*q/s
        grids=[[q,1.], [q/2,(q+1)/2,1.1], [q,ell,1.],
               [q*.8,.3*q+.2,1.,min(H*.98,1.3)],
               np.linspace(q*.5,H*.97,5),np.linspace(q*.8,H*.98,8)]
        for g in grids:
            t=sorted(set(float(x) for x in g if x<H))
            if len(t)<2:continue
            o=solve(q,t);out.append(o)
            print(json.dumps({k:o.get(k) for k in ['q','t','feasible','success','sigma','ring_sigma','eq_error']}),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
