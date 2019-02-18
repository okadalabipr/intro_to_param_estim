import os
import sys
import time
import glob
import numpy as np
import warnings
warnings.filterwarnings('ignore')

try:
    files = os.listdir('./FitParam/')
    for file in files:
        if '.npy' in file:
            os.remove('./FitParam/%s'%(file))
except:
    os.mkdir('./FitParam')

def using(file):
    os.chdir('../src')
    if '.py' in file:
        with open(file,'r',encoding='utf-8') as f:
            script = f.read()
            exec(script,globals())
    else:
        files = glob.glob(file)
        for file in files:
            using(file)
    os.chdir('../work')

using('ga/*')
using('model/set_constant.py')
using('model/set_variable.py')
using('model/differential_equation.py')
using('model/initial_condition.py')
using('model/experimental_data.py')
using('solver.py')
using('lin2log.py')
using('set_search_parameter.py')
using('fitness.py')

def ParamEstim():

    SearchRegion = setSearchRegion()
    SearchParamIdx = setSearchParamIdx()

    n_generation = np.iinfo(np.int16).max
    n_population = int(3*SearchRegion.shape[1])
    n_children = 50
    n_gene = SearchRegion.shape[1]
    allowable_error = 0.0

    (X0,BestFitness) = myGAv2(n_generation,n_population,n_children,n_gene,allowable_error,SearchParamIdx,SearchRegion)

def ParamEstim_continue():

    SearchRegion = setSearchRegion()
    SearchParamIdx = setSearchParamIdx()

    n_generation = int(10*np.iinfo(np.int16).max)
    n_population = int(3*SearchRegion.shape[1])
    n_children = 50
    n_gene = SearchRegion.shape[1]
    allowable_error = 0.0
    p0_bounds = [0.1, 10.0] # [lower_bounds, upper bounds]

    (X0,BestFitness) = myGAv2_continue(n_generation,n_population,n_children,n_gene,allowable_error,SearchParamIdx,SearchRegion,p0_bounds)