import os
import sys
import time
import glob
import re
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def include(src_file):
    src_dir = '../src/'
    if '.py' in src_file:
        with open(src_dir+src_file,'r',encoding='utf-8') as f:
            script = f.read()
            exec(script,globals())
    else:
        files = glob.glob(src_dir+src_file)
        for file in files:
            include(file[len(src_dir):])


include('ga/*')
include('model/f_parameter.py')
include('model/f_variable.py')
include('model/differential_equation.py')
include('model/initial_condition.py')
include('experimental_data.py')
include('search_parameter.py')
include('fitness.py')
include('simulation.py')

nth_paramset = int(re.sub(r'\D','',current_ipynb))

if not os.path.isdir('../FitParam/%d'%(nth_paramset)):
    os.mkdir('../FitParam/%d'%(nth_paramset))
    parameter_estimation(nth_paramset)
else:
    parameter_estimation_continue(nth_paramset)