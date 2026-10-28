import numpy as np
from scipy.optimize import differential_evolution, minimize
import json

def pars(q,X):
 s=1+q;b=2*q/s;c=1+q+q*q;l=s-np.sqrt(q);h=s+np.sqrt(q)
 x=b*X[0];y=l+(h-l)*X[1]
 u=(x*x-2*s*x+c)/(y-x);v=-(y*y-2*s*y+c)/(y-x)
 a=(y-b)/(y-x)
 j=(x+y-b-2*x*y/s)/(y-x)
 sigma=s/3*j*np.log(a*u*y/((1-a)*v*x))
 return dict(q=q,x=x,y=y,u=u,v=v,a=a,j=j,sigma=sigma,ring=(1-q)*np.log(1/q),X=list(X))
for q in [.0001,.001,.01,.05,.1,.25,.5,.75,.9,.99]:
 f=lambda X:pars(q,X)['sigma']
 r=differential_evolution(f,[(1e-8,1-1e-8)]*2,seed=1,tol=1e-12,polish=True)
 print(json.dumps(pars(q,r.x)))
