import os
import sys
import re
import warnings
warnings.filterwarnings('ignore')

from param_estim import genetic_algorithm as ga

def run_ga_continue(nth_paramset):
    if not os.path.isdir('./out/%d'%(nth_paramset)):
        os.mkdir('./out/%d'%(nth_paramset))
        ga.parameter_estimation(nth_paramset)
    else:
        ga.parameter_estimation_continue(nth_paramset)
        
if __name__ == '__main__':
    args = sys.argv
    if 'current_ipynb' in globals():
        nth_paramset = int(re.sub(r'\D','',current_ipynb))
        run_ga_continue(nth_paramset)
    else:
        run_ga_continue(int(args[1]))