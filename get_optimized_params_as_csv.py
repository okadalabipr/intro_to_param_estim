import os
import re
import csv
import numpy as np

from param_estim.name2idx import C, V
from param_estim.set_search_param import get_search_index

def get_param():
    # -------------------------------------------
    # Get optimized parameters as CSV file format
    # -------------------------------------------

    n_file = 0
    fitparam_files = os.listdir('./out')
    for file in fitparam_files:
        if re.match(r'\d',file):
            n_file += 1

    search_idx = get_search_index()

    if len(search_idx[0]) > 0:
        optimized_params = np.empty(
            (len(search_idx[0])+2, n_file+1), dtype='<U21'
        )
        for i, param_index in enumerate(search_idx[0]):
            for j in range(n_file):
                generation = np.load(
                    './out/{:d}/generation.npy'.format(
                        j + 1
                    )
                )
                best_indiv = np.load(
                    './out/{:d}/fit_param{:d}.npy'.format(
                        j + 1, int(generation)
                    )
                )
                error = np.load(
                    './out/{:d}/best_fitness.npy'.format(
                        j + 1
                    )
                )
                optimized_params[0, 0] = ''
                optimized_params[1, 0] = '*Error*'
                optimized_params[i+2, 0] = C.NAMES[param_index]
                optimized_params[0, j+1] = str(j+1)
                optimized_params[1, j+1] = '{:8.3e}'.format(error)
                optimized_params[i+2, j+1] = '{:8.3e}'.format(best_indiv[i])

        with open('optimized_params.csv', 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(optimized_params)

    if len(search_idx[1]) > 0:
        optimized_initials = np.empty(
            (len(search_idx[1])+2, n_file+1), dtype='<U21'
        )
        for i, specie_index in enumerate(search_idx[1]):
            for j in range(n_file):
                generation = np.load(
                    './out/{:d}/generation.npy'.format(
                        j + 1
                    )
                )
                best_indiv = np.load(
                    './out/{:d}/fit_param{:d}.npy'.format(
                        j + 1, int(generation)
                    )
                )
                error = np.load(
                    './out/{:d}/best_fitness.npy'.format(
                        j + 1
                    )
                )
                optimized_initials[0, 0] = ''
                optimized_initials[1, 0] = '*Error*'
                optimized_initials[i+2, 0] = V.NAMES[specie_index]
                optimized_initials[0, j+1] = str(j+1)
                optimized_initials[1, j+1] = '{:8.3e}'.format(error)
                optimized_initials[i+2, j+1] = \
                    '{:8.3e}'.format(best_indiv[i+len(search_idx[0])])

        with open('optimized_inital_varlues.csv', 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(optimized_initials)


if __name__ == '__main__':
    get_param()