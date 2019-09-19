import numpy as np
from scipy.spatial.distance import cosine

from .model.name2idx import f_parameter as C
from .model.name2idx import f_variable as V
from .model.param_const import f_params
from .model.initial_condition import initial_values
from .simulation import Simulation
from .experimental_data import ExperimentalData
from .genetic_algorithm.converter import decode_gene2variable

def compute_objval_abs(sim_data,exp_data):  # Residual Sum of Squares

    return np.dot((sim_data-exp_data),(sim_data-exp_data))


def compute_objval_cs(sim_data,exp_data):  # Cosine similarity

    return cosine(sim_data,exp_data)


# Define an objective function to be minimized.
def objective(individual_gene,search_idx,search_region):
    # update_param
    x = f_params()
    y0 = initial_values()

    indiv = decode_gene2variable(individual_gene,search_region)

    for i,j in enumerate(search_idx[0]):
        x[j] = indiv[i]
    for i,j in enumerate(search_idx[1]):
        y0[j] = indiv[i+len(search_idx[0])]
        
    # constraints
    x[C.V6] = x[C.V5]
    x[C.Km6] = x[C.Km5]
    x[C.KimpDUSP] = x[C.KimDUSP]
    x[C.KexpDUSP] = x[C.KexDUSP]
    x[C.KimpcFOS] = x[C.KimFOS]
    x[C.KexpcFOS] = x[C.KexFOS]
    x[C.p52] = x[C.p47]
    x[C.m52] = x[C.m47]
    x[C.p53] = x[C.p48]
    x[C.p54] = x[C.p49]
    x[C.m54] = x[C.m49]
    x[C.p55] = x[C.p50]
    x[C.p56] = x[C.p51]
    x[C.m56] = x[C.m51]

    exp = ExperimentalData()
    sim = Simulation()

    if sim.simulate(x,y0) is None:
      error = np.zeros(7)

      # ERK
      norm_max = np.max(sim.PERK_cyt)
      error[0] = compute_objval_abs(
          np.r_[sim.PERK_cyt[exp.t2,0],sim.PERK_cyt[exp.t2,1]]/norm_max,
          np.r_[exp.egf_ERKc_av,exp.hrg_ERKc_av]
      )
      # RSK
      norm_max = np.max(sim.PRSK_wcl)
      error[1] = compute_objval_abs(
          np.r_[sim.PRSK_wcl[exp.t2,0],sim.PRSK_wcl[exp.t2,1]]/norm_max,
          np.r_[exp.egf_RSKw_av,exp.hrg_RSKw_av]
      )
      # CREB
      norm_max = np.max(sim.PCREB_wcl)
      error[2] = compute_objval_abs(
          np.r_[sim.PCREB_wcl[exp.t3,0],sim.PCREB_wcl[exp.t3,1]]/norm_max,
          np.r_[exp.egf_CREBw_av,exp.hrg_CREBw_av]
      )
      # DUSPmRNA
      norm_max = np.max(sim.DUSPmRNA)
      error[3] = compute_objval_abs(
          np.r_[sim.DUSPmRNA[exp.t5,0],sim.DUSPmRNA[exp.t5,1]]/norm_max,
          np.r_[exp.egf_DUSPmRNA_av,exp.hrg_DUSPmRNA_av]
      )
      # cFosmRNA
      norm_max = np.max(sim.cFosmRNA)
      error[4] = compute_objval_abs(
          np.r_[sim.cFosmRNA[exp.t4,0],sim.cFosmRNA[exp.t4,1]]/norm_max,
          np.r_[exp.egf_cFosmRNA_av,exp.hrg_cFosmRNA_av]
      )
      # cFosPro
      norm_max = np.max(sim.cFosPro)
      error[5] = compute_objval_abs(
          np.r_[sim.cFosPro[exp.t5,0],sim.cFosPro[exp.t5,1]]/norm_max,
          np.r_[exp.egf_cFosPro_av,exp.hrg_cFosPro_av]
      )
      # PcFos
      norm_max = np.max(sim.PcFos)
      error[6] = compute_objval_abs(
          np.r_[sim.PcFos[exp.t2,0],sim.PcFos[exp.t2,1]]/norm_max,
          np.r_[exp.egf_PcFos_av,exp.hrg_PcFos_av]
      )

      return np.sum(error)

    else:

      return np.inf