import json, math
from fractions import Fraction as F
q=F(1,20); s=1+q; b=2*q/s
j=json.load(open('v5_interior_seed1.json'))
h=lambda ti:(ti-s)**2-q
def build(p):
    t0,t1,t2,t3,S10,S31,a0,a1=p; t=[t0,t1,t2,t3]
    S=[[F(0)]*4 for _ in range(4)]
    S[0][1]=h(t0)/(t1-t0)
    S[2][3]=h(t2)/(t3-t2)
    S[1][0]=S10; S[1][3]=(h(t1)-S10*(t0-t1))/(t3-t1)
    S[3][1]=S31; S[3][2]=(h(t3)-S31*(t1-t3))/(t2-t3)
    for i in range(4): S[i][i]=-t[i]-sum(S[i][k] for k in range(4) if k!=i)
    # a2,a3 from a0+a1+a2+a3=1, sum a t = b
    R1=1-a0-a1; R2=b-a0*t0-a1*t1
    a3=(R2-R1*t2)/(t3-t2); a2=R1-a3
    return S,t,[a0,a1,a2,a3]
def solve(M,v):  # float solve v^T M^-1 small gauss
    n=len(v); A=[[M[j][i] for j in range(n)]+[v[i]] for i in range(n)]
    for c in range(n):
        p=max(range(c,n),key=lambda r:abs(A[r][c])); A[c],A[p]=A[p],A[c]
        for r in range(n):
            if r!=c:
                f=A[r][c]/A[c][c]; A[r]=[x-f*y for x,y in zip(A[r],A[c])]
    return [A[i][n]/A[i][i] for i in range(n)]
def cost(p):
    S,t,a=build(p); n=4
    Sf=[[float(x) for x in r] for r in S]; af=[float(x) for x in a]; tf=[float(x) for x in t]
    if min(af)<=0 or min(tf)<=0: return math.inf
    for i in range(n):
        for k in range(n):
            if i!=k and Sf[i][k]<0: return math.inf
    mu=solve([[-x for x in r] for r in Sf],af)
    if min(mu)<=0: return math.inf
    J=lambda x,y:0 if x==0 and y==0 else ((x-y)*math.log(x/y) if x>0 and y>0 else math.inf)
    c=sum(J(af[i],mu[i]*tf[i]) for i in range(n))+sum(J(mu[i]*Sf[i][k],mu[k]*Sf[k][i]) for i in range(n) for k in range(i+1,n))
    return float(s/3)*c
x0=[j['t'][0],j['t'][1],j['t'][2],j['t'][3],j['S'][1][0],j['S'][3][1],j['alpha'][0],j['alpha'][1]]
for D in [1000,4000]:
    cur=[F(round(v*D),D) for v in x0]; cc=cost(cur); imp=True
    while imp:
        imp=False
        for k in range(8):
            for d in (-1,1):
                tr=list(cur); tr[k]+=F(d,D); c=cost(tr)
                if c<cc-1e-13: cur,cc,imp=tr,c,True
    print(D,cc,[str(x) for x in cur])
S,t,a=build(cur)
json.dump({'Q':[[str(-s)]+[str(s*x) for x in a]]+[[str(t[i])]+[str(x) for x in S[i]] for i in range(4)]},open('Q5_rational.json','w'),indent=1)
