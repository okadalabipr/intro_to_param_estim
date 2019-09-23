import numpy as np
from scipy.spatial.distance import cosine

from .model.name2idx import parameters as C
from .model.name2idx import variables as V
from .model.param_const import f_params
from .model.initial_condition import initial_values
from .observable import dynamics,diff_sim_and_exp
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
        norm_max = np.max(sim.simulations[dynamics['Phosphorylated_ERKc']])
        error[0] = compute_objval_abs(
            *diff_sim_and_exp(
                sim.simulations[dynamics['Phosphorylated_ERKc']],
                exp.data[dynamics['Phosphorylated_ERKc']],
                exp_timepoint=exp.t2,num_condition=sim.condition,
                norm_max_sim=norm_max
            )
        )
        
        # RSK
        norm_max = np.max(sim.simulations[dynamics['Phosphorylated_RSKw']])
        error[1] = compute_objval_abs(
            *diff_sim_and_exp(
                sim.simulations[dynamics['Phosphorylated_RSKw']],
                exp.data[dynamics['Phosphorylated_RSKw']],
                exp_timepoint=exp.t2,num_condition=sim.condition,
                norm_max_sim=norm_max
            )
        )
        # CREB
        norm_max = np.max(sim.simulations[dynamics['Phosphorylated_CREBw']])
        error[2] = compute_objval_abs(
            *diff_sim_and_exp(
                sim.simulations[dynamics['Phosphorylated_CREBw']],
                exp.data[dynamics['Phosphorylated_CREBw']],
                exp_timepoint=exp.t3,num_condition=sim.condition,
                norm_max_sim=norm_max
            )
        )
        # DUSPmRNA
        norm_max = np.max(sim.simulations[dynamics['dusp_mRNA']])
        error[3] = compute_objval_abs(
            *diff_sim_and_exp(
                sim.simulations[dynamics['dusp_mRNA']],
                exp.data[dynamics['dusp_mRNA']],
                exp_timepoint=exp.t5,num_condition=sim.condition,
                norm_max_sim=norm_max
            )
        )
        # cFosmRNA
        norm_max = np.max(sim.simulations[dynamics['cfos_mRNA']])
        error[4] = compute_objval_abs(
            *diff_sim_and_exp(
                sim.simulations[dynamics['cfos_mRNA']],
                exp.data[dynamics['cfos_mRNA']],
                exp_timepoint=exp.t4,num_condition=sim.condition,
                norm_max_sim=norm_max
            )
        )
        # cFosPro
        norm_max = np.max(sim.simulations[dynamics['cFos_Protein']])
        error[5] = compute_objval_abs(
            *diff_sim_and_exp(
                sim.simulations[dynamics['cFos_Protein']],
                exp.data[dynamics['cFos_Protein']],
                exp_timepoint=exp.t5,num_condition=sim.condition,
                norm_max_sim=norm_max
            )
        )
        # PcFos
        norm_max = np.max(sim.simulations[dynamics['Phosphorylated_cFos']])
        error[6] = compute_objval_abs(
            *diff_sim_and_exp(
                sim.simulations[dynamics['Phosphorylated_cFos']],
                exp.data[dynamics['Phosphorylated_cFos']],
                exp_timepoint=exp.t2,num_condition=sim.condition,
                norm_max_sim=norm_max
            )
        )

        return np.sum(error)

    else:

        return np.inf