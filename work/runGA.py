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

using('../ga/*')
using('../work/model/setParamConst.py')
using('../work/model/setVarEnum.py')
using('../work/model/initialValues.py')
using('../work/model/diffeq.py')
using('../work/model/expData.py')
using('../work/model/getFitness.py')
using('../work/model/setSearchParam.py')

def main():

    SearchRegion = setSearchRegion()

    n_generation = np.iinfo(np.int16).max
    n_population = int(3*SearchRegion.shape[1])
    n_children = 50
    n_gene = SearchRegion.shape[1]
    allowable_error = 0.0

    (X0,BestFitness) = myGAv2(n_generation,n_population,n_children,n_gene,allowable_error,SearchRegion)


if __name__ == '__main__':
	main()