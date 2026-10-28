#!/usr/bin/env python3
"""Scientific figures; all curves derive from explicit manuscript generators."""
from pathlib import Path
import json
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.mkdtemp(prefix='hidden_dissipation_mpl_'))
import numpy as np
from scipy.linalg import expm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'paper'/'figures';OUT.mkdir(exist_ok=True)
COL={'plum':'#78465F','teal':'#2B766B','ochre':'#A97932','ink':'#25333B','grey':'#7B8386'}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.labelsize':9,
    'axes.titlesize':10,'legend.fontsize':8,'axes.spines.top':False,'axes.spines.right':False,
    'pdf.fonttype':42,'ps.fonttype':42,'text.color':COL['ink'],'axes.labelcolor':COL['ink'],
    'axes.edgecolor':COL['grey'],'xtick.color':COL['ink'],'ytick.color':COL['ink']})
q=.05;s=1+q
S3=np.array([[-s,1],[q,-s]])
a3=np.array([1/s,q/s]);t3=np.array([q,1.])
S4=np.array([[-79/60,19/15,0],[1/3,-131/60,21/20],[0,1/5,-5/4]])
a4=np.array([683/720,31/1260,3/112]);t4=np.array([1/20,4/5,21/20])
ts=np.linspace(0,8,401)
f3=np.array([a3@expm(t*S3)@t3 for t in ts]);f4=np.array([a4@expm(t*S4)@t4 for t in ts])
maxdiff=float(np.max(np.abs(f3-f4)))
if maxdiff>1e-12:raise RuntimeError('Dwell figure does not agree')
cert=json.loads((ROOT/'results'/'exact_certificate.json').read_text())
sig4=float(cert['four_state_entropy_enclosure'][0]);sig3=(1-q)*np.log(1/q);floor=2*sig3/3
fig,ax=plt.subplots(1,2,figsize=(7.0,3.25),gridspec_kw={'width_ratios':[1.1,1]})
ax[0].plot(ts,f3,color=COL['plum'],lw=2,label='Three-state minimiser')
ax[0].plot(ts[::20],f4[::20],ls='none',marker='o',ms=4,mfc='white',mec=COL['teal'],label='Four-state example')
ax[0].set(xlabel='Complete B-dwell duration',ylabel='Probability density',xlim=(0,8),ylim=(0,.43))
ax[0].set_title('(a) Exactly the same dwell law',loc='left',pad=12)
ax[0].legend(frameon=False,loc='upper right')
values=[floor,sig4,sig3];labels=['All-architecture\nlower bound','Exact four-state\nexample','Three-state\nminimum']
colours=[COL['grey'],COL['teal'],COL['plum']]
ax[1].barh(np.arange(3),values,color=colours,height=.5,alpha=.92)
for i,v in enumerate(values):ax[1].text(v+.045,i,f'{v:.6f}',va='center',fontsize=8)
ax[1].set(yticks=np.arange(3),yticklabels=labels,xlim=(0,3.55),xlabel='Entropy production rate')
ax[1].set_title('(b) Different thermodynamic costs',loc='left',pad=12)
fig.tight_layout(w_pad=2.3)
fig.savefig(OUT/'exact_signal_comparison.pdf',bbox_inches='tight')
fig.savefig(OUT/'exact_signal_comparison.png',dpi=190,bbox_inches='tight');plt.close(fig)

# The sharp statistics-only sequence uses the same r,m,f0 as P_(1/20).
r=s/3;m=2/s;d=(1-q)/s
Ms=np.geomspace(.5,100,240)
cost=r*(4*d*np.arctanh(d)+d*np.log((Ms+d/2)/(Ms-d/2)))
fig,ax=plt.subplots(1,2,figsize=(7.0,3.15))
ax[0].semilogx(Ms,cost,color=COL['teal'],lw=2,label='Three-state family')
ax[0].axhline(floor,color=COL['ochre'],lw=1.4,ls='--',label='Unattained infimum')
ax[0].set(xlabel='Internal-flux parameter M',ylabel='Entropy production rate',ylim=(1.8,2.95))
ax[0].set_title('(a) Sharp cost for three statistics',loc='left',pad=12)
ax[0].legend(frameon=False)
tt=np.linspace(0,3,401)
for M,colour in [(.5,COL['plum']),(2.,COL['teal']),(20.,COL['ochre'])]:
    S=np.array([[-(1+2*M),2*M+d],[2*M-d,-(1+2*M)]])/m
    aa=np.array([(1+d)/2,(1-d)/2]);tv=np.array([(1-d)/m,(1+d)/m])
    ff=np.array([aa@expm(t*S)@tv for t in tt])
    ax[1].plot(tt,ff,color=colour,lw=1.6,label=f'M = {M:g}')
ax[1].plot(tt,np.exp(-tt/m)/m,color=COL['grey'],ls='--',lw=1.5,label='Exponential limit')
ax[1].set(xlabel='Complete B-dwell duration',ylabel='Probability density',xlim=(0,3),ylim=(0,.56))
ax[1].set_title('(b) Full dwell law changes',loc='left',pad=12)
ax[1].legend(frameon=False,fontsize=7.6)
fig.tight_layout(w_pad=2)
fig.savefig(OUT/'statistics_nonattainment.pdf',bbox_inches='tight')
fig.savefig(OUT/'statistics_nonattainment.png',dpi=190,bbox_inches='tight');plt.close(fig)
out={'common_dwell_max_absolute_error':maxdiff,'benchmark_three_state_cost':sig3,
     'benchmark_four_state_cost':sig4,'unrestricted_lower_bound':floor,
     'statistics_family_M_range':[float(Ms[0]),float(Ms[-1])],
     'all_curves_from_explicit_generators':True,
     'colours':COL}
(ROOT/'results'/'figure_values.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
