import os
import sys
import shutil
import re
import multiprocessing
import warnings
warnings.filterwarnings('ignore')

from param_estim import optimize


def run_ga(nth_paramset):
    if not os.path.isdir('./out'):
        os.mkdir('./out')
    try:
        files = os.listdir('./out/%d'%(nth_paramset))
        for file in files:
            if any(map(file.__contains__,('.npy','.log'))):
                os.remove('./out/%d/%s'%(nth_paramset,file))
    except:
        os.mkdir('./out/%d'%(nth_paramset))

    if os.path.isfile('./runGA_%d.ipynb'%(nth_paramset)) \
        and not os.path.isfile('./runGA_%d.ipynb'%(nth_paramset+1)):
        shutil.copy(
            './runGA_%d.ipynb'%(nth_paramset),
            './runGA_%d.ipynb'%(nth_paramset+1)
        )

    optimize(nth_paramset)
    
if __name__ == '__main__':
    args = sys.argv
    if 'current_ipynb' in globals():
        nth_paramset = int(re.sub(r'\D','',current_ipynb))
        run_ga(nth_paramset)
    else:
        if len(args) == 2:
            run_ga(int(args[1]))
        elif len(args) == 3:
            n_proc = max(1, multiprocessing.cpu_count() - 1)
            p = multiprocessing.Pool(processes=n_proc)
            p.map(run_ga, range(int(args[1]),int(args[2])+1))
            p.close()