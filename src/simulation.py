import numpy as np
from scipy.integrate import ode

from .model.name2idx import f_parameter as C
from .model.name2idx import f_variable as V
from .model.differential_equation import diffeq

def solveode(diffeq,y0,tspan,args):
    sol = ode(diffeq)
    sol.set_integrator('vode',method='bdf',min_step=1e-8,with_jacobian=True)
    sol.set_initial_value(y0,tspan[0])
    sol.set_f_params(args)

    T = [tspan[0]]
    Y = [y0]

    while sol.successful() and sol.t < tspan[-1]:
        # sol.integrate(tspan[-1],step=True)
        sol.integrate(sol.t+1.)
        T.append(sol.t)
        Y.append(sol.y)

    return np.array(T),np.array(Y)


class Simulation(object):

    tspan = range(5401) # Unit time: 1 sec.
    condition = 2

    t = np.array(tspan)/60. # sec. -> min. (plot_func.py)

    PMEK_cyt  = np.empty((len(tspan),condition))
    PERK_cyt  = np.empty((len(tspan),condition))
    PRSK_wcl  = np.empty((len(tspan),condition))
    PCREB_wcl = np.empty((len(tspan),condition))
    DUSPmRNA  = np.empty((len(tspan),condition))
    cFosmRNA  = np.empty((len(tspan),condition))
    cFosPro   = np.empty((len(tspan),condition))
    PcFos     = np.empty((len(tspan),condition))

    def __init__(self,x,y0):
        self.x = x
        self.y0 = y0

    @classmethod
    def numerical_integration(cls,x,y0):

        for i in range(cls.condition):
            if i==0:
                x[C.Ligand] = x[C.EGF]
            elif i==1:
                x[C.Ligand] = x[C.HRG]

            (T,Y) = solveode(diffeq,y0,cls.tspan,tuple(x))

            if T[-1] < cls.tspan[-1]:
                return False
            else:
                cls.PMEK_cyt[:,i] = Y[:,V.ppMEKc]
                cls.PERK_cyt[:,i] = Y[:,V.pERKc] + Y[:,V.ppERKc]
                cls.PRSK_wcl[:,i] = Y[:,V.pRSKc] + Y[:,V.pRSKn]*(x[C.Vn]/x[C.Vc])
                cls.PCREB_wcl[:,i] = Y[:,V.pCREBn]*(x[C.Vn]/x[C.Vc])
                cls.DUSPmRNA[:,i] = Y[:,V.duspmRNAc]
                cls.cFosmRNA[:,i] = Y[:,V.cfosmRNAc]
                cls.cFosPro[:,i] = (Y[:,V.pcFOSn] + Y[:,V.cFOSn])*(x[C.Vn]/x[C.Vc]) + Y[:,V.cFOSc] + Y[:,V.pcFOSc]
                cls.PcFos[:,i] = Y[:,V.pcFOSn]*(x[C.Vn]/x[C.Vc]) + Y[:,V.pcFOSc]
