import os
import shutil
import re
import warnings
warnings.filterwarnings('ignore')

import genetic_algorithm as ga

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
    shutil.copy(
        './runGA_%d.ipynb'%(nth_paramset),
        './runGA_%d.ipynb'%(nth_paramset+1)
    )


ga.parameter_estimation(nth_paramset)