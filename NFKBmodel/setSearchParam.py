def setSearchParam():
    x = setParamConst()
    y0 = initialValues()

    #write param index for optimization
    SearchConstIdx=[\
        uptake,
        #TNF,
        trigger_iIkk,
        deact_TNFR,
        deact_ppIkk,
        deact_pnNfk,
        act_Ikk_by_TNF,
        act_pIkk,
        act_Ikb_by_Ikk,
        act_Nfk_by_Ikk,
        act_Nfk_by_Ikk_complex,
        act_Ikb_complex,
        form_complex,
        form_complex_nuc,
        ext_nNfkIkb,
        #Vnuc,
        split_NfkpIkb,
        split_NfkIkb,
        int_Nfk,
        int_Ikb,
        eta_int_pNfk,
        degrad_Ikb,
        degrad_mIkb,
        degrad_RnaA20,
        degrad_A20,
        prod_Ikb,
        prod_mIkb_by_nNfk,
        build_RnaA20,
        build_A20,
        shuttle_RnaA20\
        ]

    #initialvalues(not necessary)
    SearchInitIdx= []

    SearchParam = np.empty(len(SearchConstIdx)+len(SearchInitIdx))
    for i in range(len(SearchConstIdx)):
        SearchParam[i] = x[SearchConstIdx[i]]
    for i in range(len(SearchInitIdx)):
        SearchParam[i+len(SearchConstIdx)] = y0[SearchInitIdx[i]]

    return SearchConstIdx, SearchInitIdx, SearchParam

SearchConstIdx, SearchInitIdx, SearchParam = setSearchParam()

if np.any(SearchParam == 0.):
    print('Error: SearchParam must not contain zero.')
    sys.exit()
