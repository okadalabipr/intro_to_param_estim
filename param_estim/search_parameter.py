import sys
import numpy as np

from .model.name2idx import f_parameter as C
from .model.name2idx import f_variable as V
from .model.param_const import f_params
from .model.initial_condition import initial_values

def search_parameter_index():

    # Write param index for optimization
    search_idx_const = np.array([\
        C.V1,
        C.Km1,
        C.V5,
        C.Km5,
        C.V10,
        C.Km10,
        C.n10,
        C.p11,
        C.p12,
        C.p13,
        C.V14,
        C.Km14,
        C.V15,
        C.Km15,
        C.KimDUSP,
        C.KexDUSP,
        C.V20,
        C.Km20,
        C.V21,
        C.Km21,
        C.V24,
        C.Km24,
        C.V25,
        C.Km25,
        C.KimRSK,
        C.KexRSK,
        C.V27,
        C.Km27,
        C.V28,
        C.Km28,
        C.V29,
        C.Km29,
        C.V30,
        C.Km30,
        C.V31,
        C.Km31,
        C.n31,
        C.p32,
        C.p33,
        C.p34,
        C.V35,
        C.Km35,
        C.V36,
        C.Km36,
        C.V37,
        C.Km37,
        C.KimFOS,
        C.KexFOS,
        C.V42,
        C.Km42,
        C.V43,
        C.Km43,
        C.V44,
        C.Km44,
        C.p47,
        C.m47,
        C.p48,
        C.p49,
        C.m49,
        C.p50,
        C.p51,
        C.m51,
        C.V57,
        C.Km57,
        C.n57,
        C.p58,
        C.p59,
        C.p60,
        C.p61,
        C.KimF,
        C.KexF,
        C.p63,
        C.KF31,
        C.nF31,
        C.a\
    ])

    # initialvalues
    search_idx_init= np.array([
        # V.(variable name)
    ])

    return search_idx_const, search_idx_init


def get_search_region():
    x = f_params()
    y0 = initial_values()

    search_idx = search_parameter_index()

    if len(search_idx[0]) != len(set(search_idx[0])):
        print('Error: Duplicate param name.')
        sys.exit()
    elif len(search_idx[1]) != len(set(search_idx[1])):
        print('Error: Duplicate var name.')
        sys.exit()
    else:
        pass

    search_param = np.empty(len(search_idx[0])+len(search_idx[1]))
    for i in range(len(search_idx[0])):
        search_param[i] = x[search_idx[0][i]]
    for i in range(len(search_idx[1])):
        search_param[i+len(search_idx[0])] = y0[search_idx[1][i]]

    if np.any(search_param == 0.):
        print('Error: search_param must not contain zero.')
        sys.exit()

    search_region = np.zeros((2,len(x)+len(y0)))

    '''
    # Default: 0.1 ~ 10
    for i in range(len(search_idx[0])):
        search_region[0,search_idx[0][i]] = search_param[i]*0.1 # lower bound
        search_region[1,search_idx[0][i]] = search_param[i]*10. # upper bound

    # Default: 0.5 ~ 2
    for i in range(len(search_idx[1])):
        search_region[0,search_idx[1][i]+len(x)] = search_param[i+len(search_idx[0])]*0.5 # lower bound
        search_region[1,search_idx[1][i]+len(x)] = search_param[i+len(search_idx[0])]*2.0 # upper bound
    '''

    # search_region[:,C.param_name] = [lower_bound,upper_bound]
    # search_region[:,V.var_name+len(x)] = [lower_bound,upper_bound]

    search_region[:,C.V1] = [7.33e-2,6.60e-01]
    search_region[:,C.Km1] = [1.83e+2,8.50e+2]
    search_region[:,C.V5] = [6.48e-3,7.20e+1]
    search_region[:,C.Km5] = [6.00e-1,1.60e+04]
    search_region[:,C.V10] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km10] = [np.exp(-10),np.exp(10)]
    search_region[:,C.n10] = [1.00,4.00]
    search_region[:,C.p11] = [8.30e-13,1.44e-2]
    search_region[:,C.p12] = [8.00e-8,5.17e-2]
    search_region[:,C.p13] = [1.38e-7,4.84e-1]
    search_region[:,C.V14] = [4.77e-3,4.77e+1]
    search_region[:,C.Km14] = [2.00e+2,2.00e+6]
    search_region[:,C.V15] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km15] = [np.exp(-10),np.exp(10)]
    search_region[:,C.KimDUSP] = [2.20e-4,5.50e-1]
    search_region[:,C.KexDUSP] = [2.60e-4,6.50e-1]
    search_region[:,C.V20] = [4.77e-3,4.77e+1]
    search_region[:,C.Km20] = [2.00e+2,2.00e+6]
    search_region[:,C.V21] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km21] = [np.exp(-10),np.exp(10)]
    search_region[:,C.V24] = [4.77e-2,4.77e+0]
    search_region[:,C.Km24] = [2.00e+3,2.00e+5]
    search_region[:,C.V25] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km25] = [np.exp(-10),np.exp(10)]
    search_region[:,C.KimRSK] = [2.20e-4,5.50e-1]
    search_region[:,C.KexRSK] = [2.60e-4,6.50e-1]
    search_region[:,C.V27] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km27] = [1.00e+2,1.00e+4]
    search_region[:,C.V28] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km28] = [np.exp(-10),np.exp(10)]
    search_region[:,C.V29] = [4.77e-2,4.77e+0]
    search_region[:,C.Km29] = [2.93e+3,2.93e+5]
    search_region[:,C.V30] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km30] = [np.exp(-10),np.exp(10)]
    search_region[:,C.V31] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km31] = [np.exp(-10),np.exp(10)]
    search_region[:,C.n31] = [1.00,4.00]
    search_region[:,C.p32] = [8.30e-13,1.44e-2]
    search_region[:,C.p33] = [8.00e-8,5.17e-2]
    search_region[:,C.p34] = [1.38e-7,4.84e-1]
    search_region[:,C.V35] = [4.77e-3,4.77e+1]
    search_region[:,C.Km35] = [2.00e+2,2.00e+6]
    search_region[:,C.V36] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km36] = [1.00e+2,1.00e+4]
    search_region[:,C.V37] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km37] = [np.exp(-10),np.exp(10)]
    search_region[:,C.KimFOS] = [2.20e-4,5.50e-1]
    search_region[:,C.KexFOS] = [2.60e-4,6.50e-1]
    search_region[:,C.V42] = [4.77e-3,4.77e+1]
    search_region[:,C.Km42] = [2.00e+2,2.00e+6]
    search_region[:,C.V43] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km43] = [1.00e+2,1.00e+4]
    search_region[:,C.V44] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km44] = [np.exp(-10),np.exp(10)]
    search_region[:,C.p47] = [1.45e-4,1.45e+0]
    search_region[:,C.m47] = [6.00e-3,6.00e+1]
    search_region[:,C.p48] = [2.70e-3,2.70e+1]
    search_region[:,C.p49] = [5.00e-5,5.00e-1]
    search_region[:,C.m49] = [5.00e-3,5.00e+1]
    search_region[:,C.p50] = [3.00e-3,3.00e+1]
    search_region[:,C.p51] = [np.exp(-10),np.exp(10)]
    search_region[:,C.m51] = [np.exp(-10),np.exp(10)]
    search_region[:,C.V57] = [np.exp(-10),np.exp(10)]
    search_region[:,C.Km57] = [np.exp(-10),np.exp(10)]
    search_region[:,C.n57] = [1.00,4.00]
    search_region[:,C.p58] = [8.30e-13,1.44e-2]
    search_region[:,C.p59] = [8.00e-8,5.17e-2]
    search_region[:,C.p60] = [1.38e-7,4.84e-1]
    search_region[:,C.p61] = [np.exp(-10),np.exp(10)]
    search_region[:,C.KimF] = [2.20e-4,5.50e-1]
    search_region[:,C.KexF] = [2.60e-4,6.50e-1]
    search_region[:,C.p63] = [np.exp(-10),np.exp(10)]
    search_region[:,C.KF31] = [np.exp(-10),np.exp(10)]
    search_region[:,C.nF31] = [1.00,4.00]
    search_region[:,C.a] = [1.00e+2,5.00e+2]

    search_region = lin2log(search_idx,search_region,len(x),len(search_param))

    return search_region


def write_bestFitParam(best_paramset):
        
    x = f_params()
    y0 = initial_values()

    search_idx = search_parameter_index()

    try:
        generation = np.load('./FitParam/%d/generation.npy'%(best_paramset))
        best_indiv = np.load('./FitParam/%d/FitParam%d.npy'%(best_paramset,int(generation)))

        for i in range(len(search_idx[0])):
            x[search_idx[0][i]] = best_indiv[i]
        for i in range(len(search_idx[1])):
            y0[search_idx[1][i]] = best_indiv[i+len(search_idx[0])]

    except:
        pass
    
    with open('bestFitParam.txt', mode='w') as f:
        f.write('# param set: %d\n'%(best_paramset))
        f.write('\n### param_const\n')
        for i in range(C.len_f_params):
            f.write('x[C.%s] = %e\n'%(C.F_P[i],x[i]))
        f.write('\n### initial_values\n')
        for i in range(V.len_f_vars):
            if y0[i] != 0:
                f.write('y0[V.%s] = %e\n'%(V.F_V[i],y0[i]))
                

def lin2log(search_idx,search_region,n_param_const,n_search_param):

        difference = list(
            set(np.where(np.any(search_region != 0.,axis=0))[0])^
            set(np.append(search_idx[0],n_param_const+search_idx[1]))
        )
        if len(difference) > 0:
            for i in range(len(difference)):
                if difference[i] <= n_param_const:
                    print(
                        'Set "%s" in both search_idx_const and search_region'
                        %(C.F_P[int(difference[i])])
                    )
                else:
                    print(
                        'Set "%s" in both search_idx_init and search_region'
                        %(V.F_V[int(difference[i]-n_param_const)])
                    )
            sys.exit()

        search_region = search_region[:,np.any(search_region != 0.,axis=0)]
        if n_search_param != search_region.shape[1]:
            print('Error: search_region[lb,ub] must be positive.')
            sys.exit()

        return np.log10(search_region)