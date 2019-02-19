from scipy.integrate import ode

def odesolve(diffeq,y0,tspan,args):
    sol = ode(diffeq)
    sol.set_integrator('vode',method='bdf',min_step=1e-8,with_jacobian=True)
    sol.set_initial_value(y0,tspan[0])
    sol.set_f_params(args)

    T = [tspan[0]]
    Y = [y0]

    while sol.successful() and sol.t < tspan[-1]:
        #sol.integrate(tspan[-1],step=True)
        sol.integrate(sol.t+1.)
        T.append(sol.t)
        Y.append(sol.y)

    return np.array(T),np.array(Y)

class Simulation(object):

    tspan = range(5401)
    condition = 2

    t = np.array(tspan)/60.

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
    def runSimulation(cls,x,y0):

        for i in range(cls.condition):
            if i==0:
                x[Ligand] = x[EGF]
            elif i==1:
                x[Ligand] = x[HRG]

            (T,Y) = odesolve(diffeq,y0,cls.tspan,tuple(x))

            if T[-1] < cls.tspan[-1]:
                return False
            else:
                cls.PMEK_cyt[:,i] = Y[:,ppMEKc]
                cls.PERK_cyt[:,i] = Y[:,pERKc] + Y[:,ppERKc]
                cls.PRSK_wcl[:,i] = Y[:,pRSKc] + Y[:,pRSKn]*(x[Vn]/x[Vc])
                cls.PCREB_wcl[:,i] = Y[:,pCREBn]*(x[Vn]/x[Vc])
                cls.DUSPmRNA[:,i] = Y[:,duspmRNAc]
                cls.cFosmRNA[:,i] = Y[:,cfosmRNAc]
                cls.cFosPro[:,i] = (Y[:,pcFOSn] + Y[:,cFOSn])*(x[Vn]/x[Vc]) + Y[:,cFOSc] + Y[:,pcFOSc]
                cls.PcFos[:,i] = Y[:,pcFOSn]*(x[Vn]/x[Vc]) + Y[:,pcFOSc]
