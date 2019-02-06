def setSearchParamIdx():

    # Write param index for optimization
    SearchConstIdx = np.array([\
        V1,
        Km1,
        #V2,
        #Km2,
        #V3,
        #Km3,
        #V4,
        #Km4,
        V5,
        Km5,
        #V6,
        #Km6,
        #KimERK,
        #KexERK,
        #KimpERK,
        #KexpERK,
        #KimppERK,
        #KexppERK,
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
        #p16,
        #p17,
        KimDUSP,
        KexDUSP,
        #KimpDUSP,
        #KexpDUSP,
        V20,
        Km20,
        V21,
        Km21,
        #p22,
        #p23,
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
        #p38,
        #p39,
        KimFOS,
        KexFOS,
        #KimpcFOS,
        #KexpcFOS,
        V42,
        Km42,
        V43,
        Km43,
        V44,
        Km44,
        #p45,
        #p46,
        p47,
        m47,
        p48,
        p49,
        m49,
        p50,
        p51,
        m51,
        #p52,
        #m52,
        #p53,
        #p54,
        #m54,
        #p55,
        #p56,
        #m56,
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
        #
        a\
    ])

    #initialvalues(not necessary)
    SearchInitIdx= np.array([])

    return SearchConstIdx, SearchInitIdx

def setSearchRegion():
    x = setParamConst()
    y0 = initialValues()

    (SearchConstIdx,SearchInitIdx) = setSearchParamIdx()

    SearchParam = np.empty(len(SearchConstIdx)+len(SearchInitIdx))
    for i in range(len(SearchConstIdx)):
        SearchParam[i] = x[SearchConstIdx[i]]
    for i in range(len(SearchInitIdx)):
        SearchParam[i+len(SearchConstIdx)] = y0[SearchInitIdx[i]]

    if np.any(SearchParam == 0.):
        print('Error: SearchParam must not contain zero.')
        sys.exit()

    SearchRegion = np.zeros((2,len(x)+len(y0)))
    '''
    # Default: 0.1 ~ 10
    for i in range(len(SearchConstIdx)):
        SearchRegion[0,SearchConstIdx[i]] = SearchParam[i]*0.1 # lower bound
        SearchRegion[1,SearchConstIdx[i]] = SearchParam[i]*10. # upper bound
    for i in range(len(SearchInitIdx)):
        SearchRegion[0,SearchInitIdx[i]+len(x)] = SearchParam[i+len(SearchConstIdx)]*0.1 # lower bound
        SearchRegion[1,SearchInitIdx[i]+len(x)] = SearchParam[i+len(SearchConstIdx)]*10. # upper bound
    '''

    # SearchRegion[:,param_name] = [lower_bound,upper_bound]

    SearchRegion[:,V1] = [7.33e-2,6.60e-01]
    SearchRegion[:,Km1] = [1.83e+2,8.50e+2]
    SearchRegion[:,V5] = [6.48e-3,7.20e+1]
    SearchRegion[:,Km5] = [6.00e-1,1.60e+04]
    SearchRegion[:,V10] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km10] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,n10] = [1.00,4.00]
    SearchRegion[:,p11] = [8.30e-13,1.44e-2]
    SearchRegion[:,p12] = [8.00e-8,5.17e-2]
    SearchRegion[:,p13] = [1.38e-7,4.84e-1]
    SearchRegion[:,V14] = [4.77e-3,4.77e+1]
    SearchRegion[:,Km14] = [2.00e+2,2.00e+6]
    SearchRegion[:,V15] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km15] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,KimDUSP] = [2.20e-4,5.50e-1]
    SearchRegion[:,KexDUSP] = [2.60e-4,6.50e-1]
    SearchRegion[:,V20] = [4.77e-3,4.77e+1]
    SearchRegion[:,Km20] = [2.00e+2,2.00e+6]
    SearchRegion[:,V21] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km21] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,V24] = [4.77e-2,4.77e+0]
    SearchRegion[:,Km24] = [2.00e+3,2.00e+5]
    SearchRegion[:,V25] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km25] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,KimRSK] = [2.20e-4,5.50e-1]
    SearchRegion[:,KexRSK] = [2.60e-4,6.50e-1]
    SearchRegion[:,V27] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km27] = [1.00e+2,1.00e+4]
    SearchRegion[:,V28] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km28] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,V29] = [4.77e-2,4.77e+0]
    SearchRegion[:,Km29] = [2.93e+3,2.93e+5]
    SearchRegion[:,V30] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km30] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,V31] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km31] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,n31] = [1.00,4.00]
    SearchRegion[:,p32] = [8.30e-13,1.44e-2]
    SearchRegion[:,p33] = [8.00e-8,5.17e-2]
    SearchRegion[:,p34] = [1.38e-7,4.84e-1]
    SearchRegion[:,V35] = [4.77e-3,4.77e+1]
    SearchRegion[:,Km35] = [2.00e+2,2.00e+6]
    SearchRegion[:,V36] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km36] = [1.00e+2,1.00e+4]
    SearchRegion[:,V37] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km37] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,KimFOS] = [2.20e-4,5.50e-1]
    SearchRegion[:,KexFOS] = [2.60e-4,6.50e-1]
    SearchRegion[:,V42] = [4.77e-3,4.77e+1]
    SearchRegion[:,Km42] = [2.00e+2,2.00e+6]
    SearchRegion[:,V43] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km43] = [1.00e+2,1.00e+4]
    SearchRegion[:,V44] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km44] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,p47] = [1.45e-4,1.45e+0]
    SearchRegion[:,m47] = [6.00e-3,6.00e+1]
    SearchRegion[:,p48] = [2.70e-3,2.70e+1]
    SearchRegion[:,p49] = [5.00e-5,5.00e-1]
    SearchRegion[:,m49] = [5.00e-3,5.00e+1]
    SearchRegion[:,p50] = [3.00e-3,3.00e+1]
    SearchRegion[:,p51] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,m51] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,V57] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,Km57] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,n57] = [1.00,4.00]
    SearchRegion[:,p58] = [8.30e-13,1.44e-2]
    SearchRegion[:,p59] = [8.00e-8,5.17e-2]
    SearchRegion[:,p60] = [1.38e-7,4.84e-1]
    SearchRegion[:,p61] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,KimF] = [2.20e-4,5.50e-1]
    SearchRegion[:,KexF] = [2.60e-4,6.50e-1]
    SearchRegion[:,p63] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,KF31] = [np.exp(-10),np.exp(10)]
    SearchRegion[:,nF31] = [1.00,4.00]
    SearchRegion[:,a] = [1.00e+2,5.00e+2]

    SearchRegion = lin2log(SearchRegion,len(x),len(SearchParam))

    return SearchRegion