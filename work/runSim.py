#%%
import os
import glob
import numpy as np

if not glob.glob('./Fig'):
    os.mkdir('./Fig')
else:
    pass


def using(file):
    os.chdir('../src')
    if '.py' in file:
        with open(file,'r',encoding='utf-8') as f:
            script = f.read()
            exec(script,globals())
    else:
        files = glob.glob(file)
        for file in files:
            using(file)
    os.chdir('../work')


using('model/param_const.py')
using('model/param_var.py')
using('model/differential_equation.py')
using('model/initial_condition.py')
using('experimental_data.py')
using('linear2log.py')
using('param_search.py')
using('simulation.py')

search_idx = set_search_idx()

x = set_param_const()
y0 = set_initial_condition()

#getBestParam
try:
    generation = np.load('./FitParam/generation.npy')
    best_indiv = np.load('./FitParam/FitParam%d.npy'%(int(generation)))

    for i in range(len(search_idx[0])):
        x[search_idx[0][i]] = best_indiv[i]
    for i in range(len(search_idx[1])):
        y0[search_idx[1][i]] = best_indiv[i+len(search_idx[0])]

except:
    pass

exp = ExperimentalData()
sim = Simulation(x,y0)

if sim.run_simulation(x,y0) is None:
    pass
else:
    print('Simulation failed.')

''' for Spyder
%run -i plot_func.py
plt.savefig('./Fig/simResult.png',bbox_inches='tight')
plt.show()
'''