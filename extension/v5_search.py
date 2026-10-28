import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json, numpy as np
from core import *
q=0.05; res=[]
for Z in strata(4,2):
    st=Stratum(q,4,Z); f,x=st.run(400 if not Z else 40,seed=len(res)+11,maxiter=800)
    rec={'zero_edges':sorted(map(str,Z)),'best':None if x is None else f}
    if x is not None:
        S,t,a=st.unpack(x); rec.update(S=S.tolist(),t=t.tolist(),alpha=a.tolist())
    res.append(rec); print(rec['zero_edges'],rec['best'],flush=True)
res.sort(key=lambda r: np.inf if r['best'] is None else r['best'])
json.dump({'q':q,'family':'1A+4B, right-annihilator stratum p(S)1=0 (reversal covers alpha p(S)=0)','V5_est':res[0]['best'],'strata':res},open('v5_q0.05.json','w'),indent=1)
print('BEST',res[0]['best'],res[0]['zero_edges'])
