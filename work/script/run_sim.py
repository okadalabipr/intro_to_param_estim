import os
import glob
import numpy as np

if not glob.glob('./Fig'):
    os.mkdir('./Fig')


def using(src_file):
    src_dir = '../src/'
    if '.py' in src_file:
        with open(src_dir+src_file,'r',encoding='utf-8') as f:
            script = f.read()
            exec(script,globals())
    else:
        files = glob.glob(src_dir+src_file)
        for file in files:
            using(file[len(src_dir):])


using('model/f_parameter.py')
using('model/f_variable.py')
using('model/differential_equation.py')
using('model/initial_condition.py')
using('experimental_data.py')
using('linear2log.py')
using('search_parameter.py')
using('simulation.py')

search_idx = search_parameter_index()

x = f_params()
y0 = initial_values()

# getBestParam
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