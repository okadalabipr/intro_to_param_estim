import os
import re
import numpy as np

from model import C, V, f_params, initial_values
from . import plot_func
from .search_parameter import search_parameter_index, update_param
from .observable import observables, NumericalSimulation


def _load_best_param(paramset, x, y0):
    search_idx = search_parameter_index()
    if os.path.isfile('./out/%d/generation.npy' % (paramset)):
        best_generation = np.load(
            './out/%d/generation.npy' % (
                paramset
            )
        )
        best_indiv = np.load(
            './out/%d/fit_param%d.npy' % (
                paramset, int(best_generation)
            )
        )
        
        (x, y0) = update_param(best_indiv, x, y0)

    return x, y0


def _validate(nth_paramset, x, y0):
    # -------------------------------------------------------------------------
    # Validates the dynamical viability of a set of estimated parameter values.
    # -------------------------------------------------------------------------
    sim = NumericalSimulation()
    
    (x, y0) = _load_best_param(nth_paramset, x, y0)

    if sim.simulate(x, y0) is None:
        return sim, True
    else:
        print(
            'Simulation failed.\nparameter_set #%d' % (
                nth_paramset
            )
        )
        return sim, False


def _get_search_param_matrix(n_file, x, y0):
    search_idx = search_parameter_index()
    search_param_matrix = np.empty((n_file, len(search_idx[0])))
    for nth_paramset in range(1, n_file+1):
        if os.path.isfile('./out/%d/generation.npy' % (nth_paramset)):
            best_generation = np.load(
                './out/%d/generation.npy' % (
                    nth_paramset
                )
            )
            best_indiv = np.load(
                './out/%d/fit_param%d.npy' % (
                    nth_paramset, int(best_generation)
                )
            )
        else:
            best_indiv = np.empty(
                len(search_idx[0]) + len(search_idx[1])
            )
            for i, j in enumerate(search_idx[0]):
                best_indiv[i] = x[j]
            for i, j in enumerate(search_idx[1]):
                best_indiv[i+len(search_idx[0])] = y0[j]

        search_param_matrix[nth_paramset-1, :] = best_indiv[:len(search_idx[0])]

    return search_idx, search_param_matrix


def write_best_fit_param(best_paramset, x, y0):

    (x, y0) = _load_best_param(best_paramset, x, y0)
    
    with open('./out/best_fit_param.txt', mode='w') as f:
        f.write(
            '# param set: %d\n' % (
                best_paramset
            )
        )
        f.write(
            '\n### Param. const\n'
        )
        for i in range(C.len_f_params):
            f.write(
                'x[C.%s] = %8.3e\n' % (
                    C.param_names[i], x[i]
                )
            )
        f.write(
            '\n### Non-zero initial conditions\n'
        )
        for i in range(V.len_f_vars):
            if y0[i] != 0:
                f.write(
                    'y0[V.%s] = %8.3e\n' % (
                        V.var_names[i], y0[i]
                    )
                )
                

def simulate_all(viz_type, show_all, stdev):
    """Simulate ODE model with estimated parameter values.
    
    Parameters
    ----------
    viz_type : str
        - 'average': The average of simulation results with parameter sets in "out/"
        - 'best': The best simulation result in "out/", simulation with "best_fit_param"
        - 'original': Simulation with the default parameters and initial values defined in "biomass/model/"
        - 'n(=1, 2, ...)': Use the parameter set in "out/n/"
    show_all : bool
        Whether to show all simulation results
    stdev : bool
        If True, the standard deviation of simulated values will be shown
        (only when viz_type == 'average')
    """
    if not viz_type in ['best', 'average', 'original']:
        try:
            int(viz_type)
        except ValueError:
            print(
                "Avairable viz_type are: 'best','average','original','n(=1, 2, ...)'"
            )

    x = f_params()
    y0 = initial_values()
    sim = NumericalSimulation()

    n_file = 0
    if viz_type != 'original':
        if os.path.isdir('./out'):
            fit_param_files = os.listdir('./out')
            for file in fit_param_files:
                if re.match(r'\d', file):
                    n_file += 1

    simulations_all = np.full(
        (len(observables), n_file, len(sim.t), len(sim.conditions)), np.nan
    )
    if n_file > 0:
        if n_file == 1 and viz_type == 'average':
            viz_type = 'best'
        for i in range(n_file):
            (sim, successful) = _validate(i+1, x, y0)
            if successful:
                for j, _ in enumerate(observables):
                    simulations_all[j, i, :, :] = sim.simulations[j, :, :]

        best_fitness_all = np.empty(n_file)
        for i in range(n_file):
            if os.path.isfile('./out/%d/best_fitness.npy' % (i+1)):
                best_fitness_all[i] = np.load(
                    './out/%d/best_fitness.npy' % (
                        i + 1
                    )
                )
            else:
                best_fitness_all[i] = np.inf

        # global best_paramset
        best_paramset = np.argmin(best_fitness_all) + 1
        write_best_fit_param(best_paramset, x, y0)

        if viz_type == 'average':
            pass
        elif viz_type == 'best':
            sim, _ = _validate(int(best_paramset), x, y0)
        elif int(viz_type) <= n_file:
            sim, _ = _validate(int(viz_type), x, y0)
        else:
            raise ValueError(
                '%d is larger than n_fit_param(%d)' % (
                    int(viz_type), n_file
                )
            )
        if n_file >= 2:
            plot_func.param_range(
                *_get_search_param_matrix(n_file, x, y0), portrait=True
            )
    else:
        if sim.simulate(x, y0) is not None:
            print(
                'Simulation failed.'
            )
    plot_func.timecourse(
        sim, n_file, viz_type, show_all, stdev, simulations_all
    )