import numpy as np
import glob
import sys
import time
import os
import warnings
warnings.filterwarnings('ignore')

files = os.listdir('./FitParam/')
for file in files:
    if '.npy' in file:
        os.remove('./FitParam/%s'%(file))

def using(file):
        if '.py' in file:
            with open(file,'r') as f:
                script = f.read()
                exec(script,globals())
        else:
            files = glob.glob(file)
            for file in files:
                using(file)

using ('./GA/*')
using('setParamConst.py')
using('setVarEnum.py')
using('initialValues.py')
using('diffeq.py')
using('setSearchParam.py')
using('getFitness.py')
using('experimental_data.py')

def main():

    SearchRegion=np.empty((2,len(SearchParam)))

    SearchRegion[0,:] = SearchParam*0.01#lower bound
    SearchRegion[1,:] = SearchParam*100.#upper bound
    SearchRegion = np.log10(SearchRegion)

    n_generation = np.iinfo(np.int16).max
    n_population = int(3*len(SearchParam))
    n_children = 50
    n_gene = len(SearchParam)
    allowable_error = 0.0

    (X0,BestFitness) = myGA(n_generation,n_population,n_children,n_gene,allowable_error,SearchRegion)


if __name__ == '__main__':
	main()