"""Exact generator identities and 120-digit checks of explicit all-q construction."""
if not __debug__:
    raise RuntimeError('Run without -O: verification uses assertions')
from fractions import Fraction as F
from decimal import Decimal, localcontext
from pathlib import Path
import json

def d(v):return Decimal(v.numerator)/Decimal(v.denominator)
def J(x,y):
    if not x and not y:return Decimal(0)
    return (d(x)-d(y))*(d(x)/d(y)).ln()
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def det3(A):
 return A[0][0]*A[1][1]*A[2][2]+A[0][1]*A[1][2]*A[2][0]+A[0][2]*A[1][0]*A[2][1]-A[0][2]*A[1][1]*A[2][0]-A[0][1]*A[1][0]*A[2][2]-A[0][0]*A[1][2]*A[2][1]

def check(q):
 s=1+q;D=1-q;z=s/2;u=D/s;b=2*q/s;c=1+q+q*q
 eta=u**4/(2*(1+u));C0=(q+z+u+D/2)*(u/q+D/(2*z))**2
 M=2+4*C0/eta
 B0=4*((q+s/2)**2+(1+s/2)**2+(s/2*(M+2+u/q))**2)
 e0=2*q/(s*(q*(M+2)+2*u));e=min(e0,eta/(2*B0))
 m=1/s-e/2;mu=[m,m,e];t=[q,F(1),z]
 A=M/2;B=s*M/4;C=q*M/2+u;E=s*M/4+D/2
 L=[[F(0),m-e*A/2,e*A],[q*m-e*C/2,F(0),e*C],[e*B,e*E,F(0)]]
 S=[[L[i][j]/mu[i] if i!=j else F(0) for j in range(3)] for i in range(3)]
 for i in range(3):S[i][i]=-t[i]-sum(S[i])
 alpha=[1/s-q*e/s,q/s-q*e/s,2*q*e/s]
 pi=[F(1,3)]+[s*v/3 for v in mu]
 Q=[[-s]+[s*v for v in alpha]]+[[t[i]]+S[i] for i in range(3)]
 assert sum(mu)==2/s and sum(mu[i]*t[i] for i in range(3))==1
 assert sum(alpha)==1 and sum(alpha[i]*t[i] for i in range(3))==b
 assert all(v>0 for v in mu+alpha+pi)
 assert all(Q[i][j]>0 for i in range(4) for j in range(4) if i!=j)
 assert all(sum(row)==0 for row in Q)
 assert all(sum(mu[i]*S[i][j] for i in range(3))==-alpha[j] for j in range(3))
 assert all(sum(pi[i]*Q[i][j] for i in range(4))==0 for j in range(4))
 assert all(sum(S[i][j]*t[j] for j in range(3))==c-2*s*t[i] for i in range(3))
 kap=1+s*M/2+e*(s*M/2+u)/(2*m)
 assert -sum(S[i][i] for i in range(3))==2*s+kap
 assert sum(S[i][i]*S[j][j]-S[i][j]*S[j][i] for i in range(3) for j in range(i+1,3))==c+2*s*kap
 assert -det3(S)==c*kap
 assert C0/M<eta/4
 assert e<=e0 and e<=eta/(2*B0)
 # All three old edge flux pairs stay above half their respective zero values.
 assert alpha[0]>=1/(2*s) and mu[0]*q>=q/(2*s)
 assert alpha[1]>=q/(2*s) and mu[1]>=1/(2*s)
 assert L[0][1]>=1/(2*s) and L[1][0]>=q/(2*s)
 with localcontext() as ctx:
    ctx.prec=120
    Log=d(1/q).ln(); hp=Log+d(D);hn=-Log-d(D/q)
    dm=hp*d(-1-q/s-M/4)+hn*d(-q-F(1,2)-q*M/4)+J(b,z)+J(M/2,s*M/4)+J(q*M/2+u,s*M/4+D/2)
    di1=-d(3*D/4)*Log+d(D*D/4)*d(1+1/q+1/z)+d(D*D/(4*z))*(Log/2+d(z).ln()-d(D*D/(2*q)))
    U=d(u);atanh=((1+U)/(1-U)).ln()/2
    di2=U*U/(1+U)*(3-(1-U*U).ln()/2-3*atanh/U)
    assert abs(di1-di2)<Decimal('1e-110')
    assert di2<=-d(eta)
    assert dm-di2>=0 and dm-di2<=d(C0/M)
    assert dm<-3*d(eta)/4
    phi=sum(J(alpha[i],mu[i]*t[i]) for i in range(3))+sum(J(L[i][j],L[j][i]) for i in range(3) for j in range(i+1,3))
    ring=d(D)*Log;entropy=d(s/3)*phi;gap=ring-entropy
    direct=sum(J(pi[i]*Q[i][j],pi[j]*Q[j][i]) for i in range(4) for j in range(i+1,4))
    assert abs(direct-entropy)<Decimal('1e-105')
    guarantee=d(s*eta*e/6)
    assert gap>guarantee>0
    return {'q':str(q),'M':str(d(M)),'epsilon':str(d(e)),
      'eta':str(d(eta)),'derivative':str(dm),'derivative_limit':str(di2),
      'derivative_remainder_bound':str(d(C0/M)),
      'entropy':str(entropy),'ring_entropy':str(ring),'entropy_decrease':str(gap),
      'rigorous_symbolic_decrease_bound':str(guarantee),
      'all_rational_generator_checks_passed':True,'all_high_precision_inequality_checks_passed':True}

cases=[F(1,1000),F(1,20),F(1,4),F(1,2),F(3,4),F(99,100),F(999,1000)]
out={'precision_decimal_digits':120,'description':'Constructive all-q architecture advantage: exact identities plus numerical checks of analytic inequalities','cases':[check(q) for q in cases],'scope':'Finite sample checks support the separate analytic all-q proof; interval-certified benchmark is in four_state_audit.json.'}
Path(__file__).with_name('all_q_checks.json').write_text(json.dumps(out,indent=2)+'\n')
for row in out['cases']:
 print(json.dumps({k:row[k] for k in ['q','M','epsilon','entropy_decrease','rigorous_symbolic_decrease_bound']}))
