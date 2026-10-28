import numpy as np
from scipy.optimize import minimize

def J(x,y):
 if x<=0 or y<=0:return 1e30
 return (x-y)*np.log(x/y)
def get(q,z,vals):
 D=1-q;s=1+q;a=(1-z)/D;b=(z-q)/D;F=z*z-2*s*z+1+q+q*q
 A,B,C=vals;E=(F/D+b*B)/a;k=z+B+E-A-C
 L=np.log(1/q);m=L+D;n=-L-D/q
 S1=-a*s+q*b-1+(a-b)*A+a*C-B
 S2=a-b*s-q+b*A+(b-a)*C-E
 return m*S1+n*S2+J(k,z)+J(A,B)+J(C,E),E,k
for q in [.01,.05,.1,.25,.5,.75,.9,.99]:
 D=1-q;s=1+q
 best=(1e99,None)
 for frac in np.linspace(.02,.98,25):
  z=q+frac*D
  for start in [[1.,.1,.1],[1.,1.,1.],[.1,1.,.1]]:
   r=minimize(lambda x:get(q,z,x)[0],start,method='SLSQP',bounds=[(1e-10,100)]*3,constraints=[{'type':'ineq','fun':lambda x:get(q,z,x)[1]},{'type':'ineq','fun':lambda x:get(q,z,x)[2]}],options={'maxiter':300,'ftol':1e-11})
   if r.success and r.fun<best[0]:best=(r.fun,dict(z=z,frac=frac,A=r.x[0],B=r.x[1],C=r.x[2],E=get(q,z,r.x)[1],k=get(q,z,r.x)[2]))
 print(q,best,flush=True)
