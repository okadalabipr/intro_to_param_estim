import os
import sys
import re
import warnings
warnings.filterwarnings('ignore')

from param_estim import optimize,optimize_continue

def run_ga_continue(nth_paramset):
    if not os.path.isdir('./out/%d'%(nth_paramset)):
        os.mkdir('./out/%d'%(nth_paramset))
        optimize(nth_paramset)
    else:
        optimize_continue(nth_paramset)
        
if __name__ == '__main__':
    args = sys.argv
    if 'current_ipynb' in globals():
        nth_paramset = int(re.sub(r'\D','',current_ipynb))
        run_ga_continue(nth_paramset)
    else:
        run_ga_continue(int(args[1]))