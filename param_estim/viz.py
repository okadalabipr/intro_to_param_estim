import os
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from . import model
from . import plot_func
from .search_parameter import search_parameter_index, write_bestFitParam
from .simulation import Simulation

def visualize_result(viz_type,show_all,stdev):
    if not viz_type in ['best','average','original']:
        try:
            int(viz_type)
        except ValueError:
            print("Error: viz_type ∈ {'best','average','original',int(1~n_fitparam)}")

    x = model.f_params()
    y0 = model.initial_values()
    sim = Simulation(x,y0)

    n_file = 0
    if viz_type == 'original':
        pass
    else:
        fitparam_files = os.listdir('./FitParam')
        for file in fitparam_files:
            if re.match(r'\d',file):
                n_file += 1

    PMEK_cyt_all  = np.empty((n_file,len(sim.tspan),sim.condition))
    PERK_cyt_all  = np.empty((n_file,len(sim.tspan),sim.condition))
    PRSK_wcl_all  = np.empty((n_file,len(sim.tspan),sim.condition))
    PCREB_wcl_all = np.empty((n_file,len(sim.tspan),sim.condition))
    DUSPmRNA_all  = np.empty((n_file,len(sim.tspan),sim.condition))
    cFosmRNA_all  = np.empty((n_file,len(sim.tspan),sim.condition))
    cFosPro_all   = np.empty((n_file,len(sim.tspan),sim.condition))
    PcFos_all     = np.empty((n_file,len(sim.tspan),sim.condition))

    if n_file > 0:
        for i in range(n_file):
            sim = run_simulation(i+1,sim,x,y0)

            PMEK_cyt_all[i,:,:]  = sim.PMEK_cyt
            PERK_cyt_all[i,:,:]  = sim.PERK_cyt
            PRSK_wcl_all[i,:,:]  = sim.PRSK_wcl
            PCREB_wcl_all[i,:,:] = sim.PCREB_wcl
            DUSPmRNA_all[i,:,:]  = sim.DUSPmRNA
            cFosmRNA_all[i,:,:]  = sim.cFosmRNA
            cFosPro_all[i,:,:]   = sim.cFosPro
            PcFos_all[i,:,:]     = sim.PcFos

        best_fitness_all = np.empty(n_file)
        for i in range(n_file):
            if os.path.isfile('./FitParam/%d/BestFitness.npy'%(i+1)):
                best_fitness_all[i] = np.load('./FitParam/%d/BestFitness.npy'%(i+1))
            else:
                best_fitness_all[i] = np.inf

        # global best_paramset
        best_paramset = np.argmin(best_fitness_all) + 1
        write_bestFitParam(best_paramset)

        if viz_type == 'average':
            pass
        elif viz_type == 'best':
            sim = run_simulation(int(best_paramset),sim,x,y0)
        elif int(viz_type) <= n_file:
            sim = run_simulation(int(viz_type),sim,x,y0)
        else:
            raise ValueError(
                '%d is larger than n_fitparam(%d)'%(int(viz_type),n_file)
            )

        if n_file == 1:
            pass
        else:
            save_param_range(n_file,x,y0)

    else:
        if sim.numerical_integration(x,y0) is None:
            pass
        else:
            print('Simulation failed.')

    plot_func.timecourse(sim,n_file,viz_type,show_all,stdev,
        PMEK_cyt_all,
        PERK_cyt_all,
        PRSK_wcl_all,
        PCREB_wcl_all,
        DUSPmRNA_all,
        cFosmRNA_all,
        cFosPro_all,
        PcFos_all
    )


def run_simulation(nth_paramset,sim,x,y0):
    search_idx = search_parameter_index()

    # get_best_param
    try:
        generation = np.load('./FitParam/%d/generation.npy'%(nth_paramset))
        best_indiv = np.load('./FitParam/%d/FitParam%d.npy'%(nth_paramset,int(generation)))

        for i in range(len(search_idx[0])):
            x[search_idx[0][i]] = best_indiv[i]
        for i in range(len(search_idx[1])):
            y0[search_idx[1][i]] = best_indiv[i+len(search_idx[0])]

    except:
        pass

    if sim.numerical_integration(x,y0) is None:
        pass
    else:
        print('Simulation failed.\nparameter_set #%d'%(nth_paramset))

    return sim


def save_param_range(n_file,x,y0):
    search_idx = search_parameter_index()
    search_param_matrix = np.empty((n_file,len(search_idx[0])))

    for nth_paramset in range(1,n_file+1):
        try:
            generation = np.load('./FitParam/%d/generation.npy'%(nth_paramset))
            best_indiv = np.load('./FitParam/%d/FitParam%d.npy'%(nth_paramset,int(generation)))
        except:
            best_indiv = np.empty(len(search_idx[0])+len(search_idx[1]))
            for i in range(len(search_idx[0])):
                best_indiv[i] = x[search_idx[0][i]]
            for i in range(len(search_idx[1])):
                best_indiv[i+len(search_idx[0])] = y0[search_idx[1][i]]

        search_param_matrix[nth_paramset-1,:] = best_indiv[:len(search_idx[0])]

    # ==========================================================================
    # seaborn.boxenplot

    fig = plt.figure(figsize=(8,24))
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().yaxis.set_ticks_position('left')
    plt.gca().xaxis.set_ticks_position('bottom')

    ax = sns.boxenplot(data=search_param_matrix,
        orient='h',
        linewidth=0.5,
        palette='Set2'
    )

    ax.set_xlabel('Parameter value')
    ax.set_ylabel('')
    ax.set_yticklabels([model.C.F_P[i] for i in search_idx[0]])
    ax.set_xscale('log')

    plt.savefig('./Fig/param_range.pdf',bbox_inches='tight')
    plt.close(fig)
    # ==========================================================================