import os
import sys
import time
import glob
import shutil
import re
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def include(pyfile):
    if '.py' in pyfile:
        with open('../../'+pyfile,'r',encoding='utf-8') as f:
            script = f.read()
            exec(script,globals())
    else:
        files = glob.glob('../../'+pyfile)
        for file in files:
            include(file[len('../../'):])


include('ga/*')
include('src/model/f_parameter.py')
include('src/model/f_variable.py')
include('src/model/differential_equation.py')
include('src/model/initial_condition.py')
include('src/experimental_data.py')
include('src/search_parameter.py')
include('src/fitness.py')
include('src/simulation.py')

nth_paramset = int(re.sub(r'\D','',current_ipynb))

if not os.path.isdir('../FitParam'):
    os.mkdir('../FitParam')

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