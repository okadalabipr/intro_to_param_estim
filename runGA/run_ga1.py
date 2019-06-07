import os
import sys
import time
import glob
import shutil
import re
import numpy as np
import warnings
warnings.filterwarnings('ignore')


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


using('ga/*')
using('model/f_parameter.py')
using('model/f_variable.py')
using('model/differential_equation.py')
using('model/initial_condition.py')
using('experimental_data.py')
using('search_parameter.py')
using('fitness.py')
using('simulation.py')

nth_paramset = int(re.sub(r'\D','',current_ipynb))

try:
    files = os.listdir('../FitParam/%d'%(nth_paramset))
    for file in files:
        if '.npy' in file:
            os.remove('../FitParam/%d/%s'%(nth_paramset,file))
except:
    os.mkdir('../FitParam/%d'%(nth_paramset))

if not os.path.isfile('./runGA_%d.ipynb'%(nth_paramset+1)):
    shutil.copy('./runGA_%d.ipynb'%(nth_paramset),'./runGA_%d.ipynb'%(nth_paramset+1))

parameter_estimation(nth_paramset)