import os
import sys
import time
import glob
import re
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def using(src_file):
    src_dir = '../../src/'
    if '.py' in src_file:
        with open(src_dir+src_file,'r',encoding='utf-8') as f:
            script = f.read()
            exec(script,globals())
    else:
        files = glob.glob(src_dir+src_file)
        for file in files:
            using(file[len(src_dir):])


using('ga/*')
using('model/f_parameter.py')
using('model/f_variable.py')
using('model/differential_equation.py')
using('model/initial_condition.py')
using('experimental_data.py')
using('search_parameter.py')
using('fitness.py')
using('simulation.py')

n_fitparam = int(re.sub(r'\D','',current_ipynb))

if not os.path.isdir('../FitParam/%d'%(n_fitparam)):
    os.mkdir('../FitParam/%d'%(n_fitparam))
    parameter_estimation(n_fitparam)
else:
    parameter_estimation_continue(n_fitparam)