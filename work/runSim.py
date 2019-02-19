#%%
import os
import glob
import numpy as np
import warnings
warnings.filterwarnings('ignore')

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

using('model/set_param_const.py')
using('model/set_var_enum.py')
using('model/differential_equation.py')
using('model/initial_condition.py')
using('experimental_data.py')
using('linear2log.py')
using('set_param_search.py')
using('simulation.py')

SearchParamIdx = setSearchParamIdx()

x = setParamConst()
y0 = initialValues()

#getBestParam
try:
    generation = np.load('./FitParam/generation.npy')
    X0 = np.load('./FitParam/FitParam%d.npy'%(int(generation)))

    for i in range(len(SearchParamIdx[0])):
        x[SearchParamIdx[0][i]] = X0[i]
    for i in range(len(SearchParamIdx[1])):
        y0[SearchParamIdx[1][i]] = X0[i+len(SearchParamIdx[0])]

except:
    pass

ex = ExperimentalData()
sim = Simulation(x,y0)

if sim.runSimulation(x,y0) == False:
    print('Simulation failed.')
else:
    pass

''' for Spyder
%run -i plotFunc.py
plt.savefig('./Fig/simResult.png',bbox_inches='tight')
plt.show()
'''