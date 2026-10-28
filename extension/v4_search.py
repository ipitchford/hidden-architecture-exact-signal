import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sys, json, numpy as np
from core import *
q=float(sys.argv[1]); starts=int(sys.argv[2]); out=sys.argv[3]
res=[]
for Z in strata(3,3):
    st=Stratum(q,3,Z); f,x=st.run(starts,seed=hash(str(sorted(map(str,Z))))%2**31)
    rec={'zero_edges':sorted(map(str,Z)),'dim':st.nv-5,'best':None if x is None else f}
    if x is not None:
        S,t,a=st.unpack(x); rec.update(S=S.tolist(),t=t.tolist(),alpha=a.tolist())
    res.append(rec); print(rec['zero_edges'],rec['best'],flush=True)
res.sort(key=lambda r: np.inf if r['best'] is None else r['best'])
V3=(1-q)*np.log(1/q)
json.dump({'q':q,'starts_per_stratum':starts,'V3':V3,'LB':2/3*V3,'V4_est':res[0]['best'],'best_stratum':res[0]['zero_edges'],'strata':res},open(out,'w'),indent=1)
print('BEST',res[0]['best'],res[0]['zero_edges'])
