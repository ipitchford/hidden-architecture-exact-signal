exec(open('hidden_dissipation_paper_20261026/two_phase/explore.py').read().split('for q in')[0])
q=.05
r=differential_evolution(lambda X:pars(q,X)['j'],[(1e-8,1-1e-8)]*2,seed=1)
print(pars(q,r.x))
for X in [(.2,.2),(.9,.9),(.1,.7)]: print(pars(q,X))
