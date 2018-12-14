import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def using(filename):
        with open(filename,'r',encoding='utf-8') as f:
            script = f.read()
        exec(script,globals())

using('./GA/odesolve.py')
using('./GA/bestParam.py')
using('./GA/myEnum.py')
using('setParamConst.py')
using('setVarEnum.py')
using('initialValues.py')
using('diffeq.py')
using('setSearchParam.py')
using('experimental_data.py')

(x,y0) = bestParam()

tspan = range(181)#Unit time: 1 min
t = np.array(tspan)

(T,Y) = odesolve(diffeq,y0,tspan,tuple(x))


nuclear_NFKB = x[Vnuc]*(Y[:,pnNfk] + Y[:,nNfk] + Y[:,nNfkIkb])
nuclear_NFKB = nuclear_NFKB/np.max(nuclear_NFKB)
