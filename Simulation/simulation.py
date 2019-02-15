import os
import glob
import numpy as np
import warnings
warnings.filterwarnings('ignore')

if not glob.glob('../Fig'):
    os.mkdir('../Fig')
else:
    pass

def using(file):
    with open(file,'r',encoding='utf-8') as f:
        script = f.read()
        exec(script,globals())

using('../Model/setParamConst.py')
using('../Model/setVarEnum.py')
using('../Model/initialValues.py')
using('../Model/diffeq.py')
using('../Model/expData.py')
using('../Model/setSearchParam.py')
using('../solver.py')

SearchParamIdx = setSearchParamIdx()

x = setParamConst()
y0 = initialValues()

#getBestParam
try:
    generation = np.load('../FitParam/generation.npy')
    X0 = np.load('../FitParam/FitParam%d.npy'%(int(generation)))

    for i in range(len(SearchParamIdx[0])):
        x[SearchParamIdx[0][i]] = X0[i]
    for i in range(len(SearchParamIdx[1])):
        y0[SearchParamIdx[1][i]] = X0[i+len(SearchParamIdx[0])]

except:
    pass

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