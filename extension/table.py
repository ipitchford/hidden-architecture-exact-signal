import json,glob,math
rows=[]
for f in glob.glob('v4_q*.json'):
    j=json.load(open(f)); rows.append((j['q'],j['V3'],j['V4_est'],j['LB'],j['best_stratum']))
rows.sort()
print(r"\begin{tabular}{@{}rcccc@{}}\toprule")
print(r"$q$ & $V_3$ (proved) & $V_4$ (numerical) & saving & floor $\tfrac23V_3$ (proved)\\\midrule")
for q,v3,v4,lb,z in rows:
    print(f"{q:g} & {v3:.5f} & {v4:.5f} & {100*(v3-v4)/v3:.2f}\\% & {lb:.5f}\\\\")
print(r"\bottomrule\end{tabular}")
for r in rows: print('%',r[0],r[4])
