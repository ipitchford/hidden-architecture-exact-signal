"""Independent referee checks: all-q insertion, exact generator identities.

The proof establishes the quantifiers; these checks test its transcription.
Python standard library only. No optimisation is used.
"""
from fractions import Fraction as F
from decimal import Decimal as D, localcontext
from pathlib import Path
import json

def dec(x):
    if isinstance(x,F): return D(x.numerator)/D(x.denominator)
    return D(x)

def j(x,y):
    x,y=dec(x),dec(y)
    if x==y==0:return D(0)
    if min(x,y)<=0:raise ValueError('one-way or negative flux')
    return (x-y)*(x/y).ln()

def dj(x,y,dx,dy):
    x,y,dx,dy=map(dec,(x,y,dx,dy))
    return dx*((x/y).ln()+1-y/x)+dy*((y/x).ln()+1-x/y)

def derivative(q,M):
    s=1+q; d=1-q; u=d/s
    aa=M/2;bb=s*M/4;cc=q*M/2+u;ee=s*M/4+d/2
    return (dj(1/s,q/s,-q/s,-q/2)+dj(q/s,1/s,-q/s,-F(1,2))
            +j(2*q/s,s/2)
            +dj(1/s,q/s,-F(1,2)-M/4,-q/2-q*M/4-u/2)
            +j(aa,bb)+j(ee,cc))

def matmul(a,b):
    return [[sum((a[i][k]*b[k][l] for k in range(len(b))),F(0))
             for l in range(len(b[0]))] for i in range(len(a))]

def instance(q,M,eps):
    s=1+q;d=1-q;u=d/s
    mu=[1/s-eps/2,eps,1/s-eps/2]
    t=[q,s/2,F(1)]
    L=[[F(0)]*3 for _ in range(3)]
    L[0][1]=eps*M/2;L[1][0]=eps*s*M/4
    L[2][1]=eps*(q*M/2+u);L[1][2]=eps*(s*M/4+d/2)
    L[0][2]=mu[0]-eps*M/4;L[2][0]=q*mu[2]-eps*(q*M/4+u/2)
    S=[[L[i][k]/mu[i] for k in range(3)] for i in range(3)]
    for i in range(3):S[i][i]=-t[i]-sum(S[i])
    alpha=[-sum((mu[i]*S[i][k] for i in range(3)),F(0)) for k in range(3)]
    expected=[(1-q*eps)/s,2*q*eps/s,q*(1-eps)/s]
    assert alpha==expected and all(x>0 for x in alpha+mu+t)
    assert all(L[i][k]>0 for i in range(3) for k in range(3) if i!=k)
    assert sum(mu)==2/s and sum(alpha)==1 and sum(mu[i]*t[i] for i in range(3))==1
    assert sum(alpha[i]*t[i] for i in range(3))==2*q/s
    S2=matmul(S,S);c=1+q+q*q
    annihilator=[sum(S2[i])+2*s*sum(S[i])+c for i in range(3)]
    assert annihilator==[0,0,0]
    r=s/3
    pi=[F(1,3)]+[r*x for x in mu]
    Q=[[-s]+[s*x for x in alpha]]+[[t[i]]+S[i] for i in range(3)]
    assert all(sum(row)==0 for row in Q)
    assert all(sum(pi[i]*Q[i][k] for i in range(4))==0 for k in range(4))
    sig=sum((j(pi[i]*Q[i][k],pi[k]*Q[k][i]) for i in range(4) for k in range(i+1,4)),D(0))
    ring=dec(d)*(D(1)/dec(q)).ln()
    return sig,ring

def main():
    cases=[];explicit=[]
    with localcontext() as ctx:
        ctx.prec=90
        for q in [F(1,100),F(1,20),F(1,4),F(1,2),F(3,4),F(9,10),F(99,100),F(999,1000)]:
            s=1+q;d=1-q;u=d/s; ud=dec(u)
            lim=ud*ud/(1+ud)*(3-(1-ud*ud).ln()/2-3*((1+ud)/(1-ud)).ln()/(2*ud))
            other=dec(d*d/(2*s))*(3+dec(s/2).ln()-dec((1+2*q)/d)*(D(1)/dec(q)).ln())
            assert abs(lim-other)<D('1e-80') and lim<0
            M=F(1)
            while derivative(q,M)>=lim/2:
                M*=10
                assert M<10**14
            a=F(1,2)+M/4;b=q/2+q*M/4+u/2
            bound=min(F(1),2/s,(1/s)/a,(q/s)/b)
            eps=bound/F(100)
            sig,ring=instance(q,M,eps)
            while sig>=ring:
                eps/=10
                assert eps>F(1,10**40)
                sig,ring=instance(q,M,eps)
            der=derivative(q,M)
            sigsmall,_=instance(q,M,eps/1000)
            rate=(sigsmall-ring)/dec(eps/1000)/(dec(s)/3)
            cases.append({'q':str(q),'M':str(M),'epsilon':str(eps),
                'derivative_per_cycle':str(der),'derivative_limit':str(lim),
                'small_epsilon_quotient':str(rate),'entropy_gap':str(ring-sig),
                'exact_generator_stationarity_and_annihilator':True})
            # Independently check the conservative constructive constants.
            z=s/2;eta=u**4/(2*(1+u))
            C0=(q+z+u+d/2)*(u/q+d/(2*z))**2
            Mc=2+4*C0/eta
            B0=4*((q+s/2)**2+(1+s/2)**2+(s/2*(Mc+2+u/q))**2)
            eps0=2*q/(s*(q*(Mc+2)+2*u))
            epsc=min(eps0,eta/(2*B0))
            ds=derivative(q,Mc)
            sc,rc=instance(q,Mc,epsc)
            target=dec(s*eta*epsc/6)
            assert lim<=-dec(eta) and ds< -3*dec(eta)/4
            assert D(0)<=ds-lim<=dec(C0/Mc)
            assert rc-sc>target>0
            explicit.append({'q':str(q),'M':str(Mc),'epsilon':str(epsc),
                'certified_analytic_lower_gap_decimal':str(target),
                'direct_90_digit_gap':str(rc-sc),'checks_passed':True})
    out={'checks':'passed','precision':90,'cases':cases,'explicit_constants':explicit,
         'interpretation':'Finite-instance diagnostics and exact rational structural checks; analytical proof carries universal quantifiers.'}
    Path(__file__).with_name('referee_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
