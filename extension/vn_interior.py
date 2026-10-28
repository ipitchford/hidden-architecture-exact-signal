import sys, os, json; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from core import Stratum
st=Stratum(0.05,int(sys.argv[4]),set()); f,x=st.run(int(sys.argv[1]),seed=int(sys.argv[2]),maxiter=1500)
S,t,a=st.unpack(x)
json.dump({'cost':f,'S':S.tolist(),'t':t.tolist(),'alpha':a.tolist()},open(sys.argv[3],'w'),indent=1)
print(f)
