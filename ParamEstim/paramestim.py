import os
import sys
import time
import glob
import numpy as np
import warnings
warnings.filterwarnings('ignore')

try:
    files = os.listdir('../FitParam/')
    for file in files:
        if '.npy' in file:
            os.remove('../FitParam/%s'%(file))
except:
    os.mkdir('../FitParam')

def using(file):
    if '.py' in file:
        with open(file,'r',encoding='utf-8') as f:
            script = f.read()
            exec(script,globals())
    else:
        files = glob.glob(file)
        for file in files:
            using(file)

using('../GA/*')
using('../Model/setParamConst.py')
using('../Model/setVarEnum.py')
using('../Model/initialValues.py')
using('../Model/diffeq.py')
using('../Model/expData.py')
using('../Model/fitness.py')
using('../Model/setSearchParam.py')
using('../solver.py')


def paramestim():

    SearchRegion = setSearchRegion()
    SearchParamIdx = setSearchParamIdx()

    n_generation = np.iinfo(np.int16).max
    n_population = int(3*SearchRegion.shape[1])
    n_children = 50
    n_gene = SearchRegion.shape[1]
    allowable_error = 0.0

    (X0,BestFitness) = myGAv2(n_generation,n_population,n_children,n_gene,allowable_error,SearchParamIdx,SearchRegion)


if __name__ == '__main__':
	paramestim()