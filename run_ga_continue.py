import os
import re
import warnings
warnings.filterwarnings('ignore')

from param_estim import genetic_algorithm as ga

nth_paramset = int(re.sub(r'\D','',current_ipynb))

if not os.path.isdir('../FitParam/%d'%(nth_paramset)):
    os.mkdir('../FitParam/%d'%(nth_paramset))
    ga.parameter_estimation(nth_paramset)
else:
    ga.parameter_estimation_continue(nth_paramset)