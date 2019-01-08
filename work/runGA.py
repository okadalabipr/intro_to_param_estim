import numpy as np
import glob
import sys
import time
import os
import warnings
warnings.filterwarnings('ignore')

files = os.listdir('../FitParam/')
for file in files:
    if '.npy' in file:
        os.remove('../FitParam/%s'%(file))

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

    SearchRegion=np.empty((2,len(SearchParam)))

    SearchRegion[0,:] = SearchParam*0.01#lower bound
    SearchRegion[1,:] = SearchParam*100.#upper bound

    #Hill coefficient
    Hill_C = [n10,n31,n57,nF31]
    HillIdx = [0]*len(Hill_C)
    for i in range(len(Hill_C)):
        HillIdx[i] = SearchConstIdx.index(Hill_C[i])
    SearchRegion[0,HillIdx] = 1.#lower bound
    SearchRegion[1,HillIdx] = 3.#upper bound

    SearchRegion = np.log10(SearchRegion)

    n_generation = np.iinfo(np.int16).max
    n_population = int(3*len(SearchParam))
    n_children = 50
    n_gene = len(SearchParam)
    allowable_error = 0.0

    (X0,BestFitness) = myGAv2(n_generation,n_population,n_children,n_gene,allowable_error,SearchRegion)


if __name__ == '__main__':
	main()