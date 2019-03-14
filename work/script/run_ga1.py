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

def using(src_file):
    if '.py' in src_file:
        with open('../src/'+src_file,'r',encoding='utf-8') as f:
            script = f.read()
            exec(script,globals())
    else:
        files = glob.glob('../src/'+src_file)
        for file in files:
            using(file[len('../src/'):])

using('ga/*')
using('model/f_parameter.py')
using('model/f_variable.py')
using('model/differential_equation.py')
using('model/initial_condition.py')
using('experimental_data.py')
using('linear2log.py')
using('search_parameter.py')
using('fitness.py')
using('simulation.py')
using('estimation.py')

parameter_estimation()