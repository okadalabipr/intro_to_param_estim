import os
import glob
import numpy as np

try:
    os.listdir('./Fig')
except:
    os.mkdir('./Fig')
finally:
    os.chdir('../src')

def using(file):
    if '.py' in file:
        with open(file,'r',encoding='utf-8') as f:
            script = f.read()
            exec(script,globals())
    else:
        files = glob.glob(file)
        for file in files:
            using(file)


using('model/f_parameter.py')
using('model/f_variable.py')
using('model/differential_equation.py')
using('model/initial_condition.py')
using('experimental_data.py')
using('linear2log.py')
using('search_parameter.py')
using('simulation.py')

os.chdir('../work')

search_idx = search_parameter_index()

x = f_params()
y0 = initial_values()

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