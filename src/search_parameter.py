def search_parameter_index():

    # Write param index for optimization
    search_idx_const = np.array([\
        V1,
        Km1,
        V5,
        Km5,
        V10,
        Km10,
        n10,
        p11,
        p12,
        p13,
        V14,
        Km14,
        V15,
        Km15,
        KimDUSP,
        KexDUSP,
        V20,
        Km20,
        V21,
        Km21,
        V24,
        Km24,
        V25,
        Km25,
        KimRSK,
        KexRSK,
        V27,
        Km27,
        V28,
        Km28,
        V29,
        Km29,
        V30,
        Km30,
        V31,
        Km31,
        n31,
        p32,
        p33,
        p34,
        V35,
        Km35,
        V36,
        Km36,
        V37,
        Km37,
        KimFOS,
        KexFOS,
        V42,
        Km42,
        V43,
        Km43,
        V44,
        Km44,
        p47,
        m47,
        p48,
        p49,
        m49,
        p50,
        p51,
        m51,
        V57,
        Km57,
        n57,
        p58,
        p59,
        p60,
        p61,
        KimF,
        KexF,
        p63,
        KF31,
        nF31,
        a\
    ])

    # initialvalues
    search_idx_init= np.array([])

    return search_idx_const, search_idx_init


def get_search_region():
    x = f_params()
    y0 = initial_values()

    search_idx = search_parameter_index()

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
    for i in range(len(search_idx[1])):
        search_region[0,search_idx[1][i]+len(x)] = search_param[i+len(search_idx[0])]*0.1 # lower bound
        search_region[1,search_idx[1][i]+len(x)] = search_param[i+len(search_idx[0])]*10. # upper bound
    '''

    # search_region[:,param_name] = [lower_bound,upper_bound]

    search_region[:,V1] = [7.33e-2,6.60e-01]
    search_region[:,Km1] = [1.83e+2,8.50e+2]
    search_region[:,V5] = [6.48e-3,7.20e+1]
    search_region[:,Km5] = [6.00e-1,1.60e+04]
    search_region[:,V10] = [np.exp(-10),np.exp(10)]
    search_region[:,Km10] = [np.exp(-10),np.exp(10)]
    search_region[:,n10] = [1.00,4.00]
    search_region[:,p11] = [8.30e-13,1.44e-2]
    search_region[:,p12] = [8.00e-8,5.17e-2]
    search_region[:,p13] = [1.38e-7,4.84e-1]
    search_region[:,V14] = [4.77e-3,4.77e+1]
    search_region[:,Km14] = [2.00e+2,2.00e+6]
    search_region[:,V15] = [np.exp(-10),np.exp(10)]
    search_region[:,Km15] = [np.exp(-10),np.exp(10)]
    search_region[:,KimDUSP] = [2.20e-4,5.50e-1]
    search_region[:,KexDUSP] = [2.60e-4,6.50e-1]
    search_region[:,V20] = [4.77e-3,4.77e+1]
    search_region[:,Km20] = [2.00e+2,2.00e+6]
    search_region[:,V21] = [np.exp(-10),np.exp(10)]
    search_region[:,Km21] = [np.exp(-10),np.exp(10)]
    search_region[:,V24] = [4.77e-2,4.77e+0]
    search_region[:,Km24] = [2.00e+3,2.00e+5]
    search_region[:,V25] = [np.exp(-10),np.exp(10)]
    search_region[:,Km25] = [np.exp(-10),np.exp(10)]
    search_region[:,KimRSK] = [2.20e-4,5.50e-1]
    search_region[:,KexRSK] = [2.60e-4,6.50e-1]
    search_region[:,V27] = [np.exp(-10),np.exp(10)]
    search_region[:,Km27] = [1.00e+2,1.00e+4]
    search_region[:,V28] = [np.exp(-10),np.exp(10)]
    search_region[:,Km28] = [np.exp(-10),np.exp(10)]
    search_region[:,V29] = [4.77e-2,4.77e+0]
    search_region[:,Km29] = [2.93e+3,2.93e+5]
    search_region[:,V30] = [np.exp(-10),np.exp(10)]
    search_region[:,Km30] = [np.exp(-10),np.exp(10)]
    search_region[:,V31] = [np.exp(-10),np.exp(10)]
    search_region[:,Km31] = [np.exp(-10),np.exp(10)]
    search_region[:,n31] = [1.00,4.00]
    search_region[:,p32] = [8.30e-13,1.44e-2]
    search_region[:,p33] = [8.00e-8,5.17e-2]
    search_region[:,p34] = [1.38e-7,4.84e-1]
    search_region[:,V35] = [4.77e-3,4.77e+1]
    search_region[:,Km35] = [2.00e+2,2.00e+6]
    search_region[:,V36] = [np.exp(-10),np.exp(10)]
    search_region[:,Km36] = [1.00e+2,1.00e+4]
    search_region[:,V37] = [np.exp(-10),np.exp(10)]
    search_region[:,Km37] = [np.exp(-10),np.exp(10)]
    search_region[:,KimFOS] = [2.20e-4,5.50e-1]
    search_region[:,KexFOS] = [2.60e-4,6.50e-1]
    search_region[:,V42] = [4.77e-3,4.77e+1]
    search_region[:,Km42] = [2.00e+2,2.00e+6]
    search_region[:,V43] = [np.exp(-10),np.exp(10)]
    search_region[:,Km43] = [1.00e+2,1.00e+4]
    search_region[:,V44] = [np.exp(-10),np.exp(10)]
    search_region[:,Km44] = [np.exp(-10),np.exp(10)]
    search_region[:,p47] = [1.45e-4,1.45e+0]
    search_region[:,m47] = [6.00e-3,6.00e+1]
    search_region[:,p48] = [2.70e-3,2.70e+1]
    search_region[:,p49] = [5.00e-5,5.00e-1]
    search_region[:,m49] = [5.00e-3,5.00e+1]
    search_region[:,p50] = [3.00e-3,3.00e+1]
    search_region[:,p51] = [np.exp(-10),np.exp(10)]
    search_region[:,m51] = [np.exp(-10),np.exp(10)]
    search_region[:,V57] = [np.exp(-10),np.exp(10)]
    search_region[:,Km57] = [np.exp(-10),np.exp(10)]
    search_region[:,n57] = [1.00,4.00]
    search_region[:,p58] = [8.30e-13,1.44e-2]
    search_region[:,p59] = [8.00e-8,5.17e-2]
    search_region[:,p60] = [1.38e-7,4.84e-1]
    search_region[:,p61] = [np.exp(-10),np.exp(10)]
    search_region[:,KimF] = [2.20e-4,5.50e-1]
    search_region[:,KexF] = [2.60e-4,6.50e-1]
    search_region[:,p63] = [np.exp(-10),np.exp(10)]
    search_region[:,KF31] = [np.exp(-10),np.exp(10)]
    search_region[:,nF31] = [1.00,4.00]
    search_region[:,a] = [1.00e+2,5.00e+2]

    search_region = lin2log(search_idx,search_region,len(x),len(search_param))

    return search_region