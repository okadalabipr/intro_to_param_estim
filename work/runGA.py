#%%
import os
import sys
import time
import glob
import numpy as np
import warnings
warnings.filterwarnings('ignore')

try:
    files = os.listdir('./FitParam/')
    for file in files:
        if '.npy' in file:
            os.remove('./FitParam/%s'%(file))
except:
    os.mkdir('./FitParam')


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


using('ga/*')
using('model/param_const.py')
using('model/param_var.py')
using('model/differential_equation.py')
using('model/initial_condition.py')
using('experimental_data.py')
using('linear2log.py')
using('param_search.py')
using('fitness.py')
using('simulation.py')
using('estimation.py')

parameter_estimation()