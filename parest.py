import os
import sys
import shutil
import re
import warnings
warnings.filterwarnings('ignore')

from param_estim import genetic_algorithm as ga

if not os.path.isdir('./work/FitParam'):
    os.mkdir('./work/FitParam')

def parest(nth_paramset):
    try:
        files = os.listdir('../FitParam/%d'%(nth_paramset))
        for file in files:
            if any(map(file.__contains__,('.npy','.log','.txt'))):
                os.remove('../FitParam/%d/%s'%(nth_paramset,file))
    except:
        os.mkdir('../FitParam/%d'%(nth_paramset))

    if not os.path.isfile('./runGA_%d.ipynb'%(nth_paramset+1)):
        shutil.copy(
            './runGA_%d.ipynb'%(nth_paramset),
            './runGA_%d.ipynb'%(nth_paramset+1)
        )
        
    ga.parameter_estimation(nth_paramset)
    
    
if __name__ == '__main__':
    args = sys.argv
    if args[1].isdigit():
        os.chdir('work/runGA')
        parest(int(args[1]))
    else:
        print('Argument is not digit')