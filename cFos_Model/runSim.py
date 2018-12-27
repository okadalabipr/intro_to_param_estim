import os
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

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
#constraints
x[V6] = x[V5]
x[Km6] = x[Km5]
x[KimpDUSP] = x[KimDUSP]
x[KexpDUSP] = x[KexDUSP]
x[KimpcFOS] = x[KimFOS]
x[KexpcFOS] = x[KexFOS]
x[p52] = x[p47]
x[m52] = x[m47]
x[p53] = x[p48]
x[p54] = x[p49]
x[m54] = x[m49]
x[p55] = x[p50]
x[p56] = x[p51]
x[m56] = x[m51]

tspan = range(5401)
t = np.array(tspan)/60.
condition = 2

PMEK_cyt  = np.empty((len(tspan),condition))
PERK_cyt  = np.empty((len(tspan),condition))
PRSK_wcl  = np.empty((len(tspan),condition))
PCREB_wcl = np.empty((len(tspan),condition))
DUSPmRNA  = np.empty((len(tspan),condition))
cFosmRNA  = np.empty((len(tspan),condition))
cFosPro   = np.empty((len(tspan),condition))
PcFos     = np.empty((len(tspan),condition))

for i in range(condition):
    if i==0:
        x[Ligand] = x[EGF]
    elif i==1:
        x[Ligand] = x[HRG]

    (T,Y) = odesolve(diffeq,y0,tspan,tuple(x))

    PMEK_cyt[:,i] = Y[:,ppMEKc]
    PERK_cyt[:,i] = Y[:,pERKc] + Y[:,ppERKc]
    PRSK_wcl[:,i] = Y[:,pRSKc] + Y[:,pRSKn]*(x[Vn]/x[Vc])
    PCREB_wcl[:,i] = Y[:,pCREBn]*(x[Vn]/x[Vc])
    DUSPmRNA[:,i] = Y[:,duspmRNAc]
    cFosmRNA[:,i] = Y[:,cfosmRNAc]
    cFosPro[:,i] = (Y[:,pcFOSn] + Y[:,cFOSn])*(x[Vn]/x[Vc]) + Y[:,cFOSc] + Y[:,pcFOSc]
    PcFos[:,i] = Y[:,pcFOSn]*(x[Vn]/x[Vc]) + Y[:,pcFOSc]