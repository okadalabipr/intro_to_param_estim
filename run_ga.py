import os
import sys
import shutil
import re
import warnings
warnings.filterwarnings('ignore')

from param_estim import optimize


def run_ga(nth_paramset):
    if not os.path.isdir('./out'):
        os.mkdir('./out')
    try:
        files = os.listdir('./out/%d'%(nth_paramset))
        for file in files:
            if any(map(file.__contains__,('.npy','.txt'))):
                os.remove('./out/%d/%s'%(nth_paramset,file))
    except:
        os.mkdir('./out/%d'%(nth_paramset))

    if not os.path.isfile('./runGA_%d.ipynb'%(nth_paramset+1)):
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
        run_ga(int(args[1]))