def getFitness(Individual_gene,SearchRegion):

    tspan = range(5401)

    condition = 2

    PMEK_cyt  = np.empty((len(tspan),condition))
    PERK_cyt  = np.empty((len(tspan),condition))
    PRSK_wcl  = np.empty((len(tspan),condition))
    PCREB_wcl = np.empty((len(tspan),condition))
    DUSPmRNA  = np.empty((len(tspan),condition))
    cFosmRNA  = np.empty((len(tspan),condition))
    cFosPro   = np.empty((len(tspan),condition))
    PcFos     = np.empty((len(tspan),condition))

    (x,y0) = updateParam(Individual_gene,SearchRegion)
    #constraints
    x[V6] = x[V5]
    x[Km6] = x[Km5]
    x[KimpDUSP] = x[KimDUSP]
    x[KexpDUSP] = x[KexDUSP]
    x[KimpcFOS] = x[KimFOS]
    x[KexpcFOS] = x[KexFOS]
    x[p52] = x[p47]
    x[m52] = x[m47]
    x[p53] = x[p48]
    x[p54] = x[p49]
    x[m54] = x[m49]
    x[p55] = x[p50]
    x[p56] = x[p51]
    x[m56] = x[m51]

    for i in range(condition):
        if i==0:
            x[Ligand] = x[EGF]
        elif i==1:
            x[Ligand] = x[HRG]

        (T,Y) = odesolve(diffeq,y0,tspan,tuple(x))
        if T[-1] < tspan[-1]:
            return np.inf

        PMEK_cyt[:,i] = Y[:,ppMEKc]
        PERK_cyt[:,i] = Y[:,pERKc] + Y[:,ppERKc]
        PRSK_wcl[:,i] = Y[:,pRSKc] + Y[:,pRSKn]*(x[Vn]/x[Vc])
        PCREB_wcl[:,i] = Y[:,pCREBn]*(x[Vn]/x[Vc])
        DUSPmRNA[:,i] = Y[:,duspmRNAc]
        cFosmRNA[:,i] = Y[:,cfosmRNAc]
        cFosPro[:,i] = (Y[:,pcFOSn] + Y[:,cFOSn])*(x[Vn]/x[Vc]) + Y[:,cFOSc] + Y[:,pcFOSc]
        PcFos[:,i] = Y[:,pcFOSn]*(x[Vn]/x[Vc]) + Y[:,pcFOSc]

    fit=np.zeros(7)

    #ERK
    norm_max = np.max(PERK_cyt)
    fit[0] = compute_objval_abs(np.append(PERK_cyt[ex_t2,0],PERK_cyt[ex_t2,1])/norm_max,np.append(ex_egf_ERKc_av,ex_hrg_ERKc_av))
    #RSK
    norm_max = np.max(PRSK_wcl)
    fit[1] = compute_objval_abs(np.append(PRSK_wcl[ex_t2,0],PRSK_wcl[ex_t2,1])/norm_max,np.append(ex_egf_RSKw_av,ex_hrg_RSKw_av))
    #CREB
    norm_max = np.max(PCREB_wcl)
    fit[2] = compute_objval_abs(np.append(PCREB_wcl[ex_t3,0],PCREB_wcl[ex_t3,1])/norm_max,np.append(ex_egf_CREBw_av,ex_hrg_CREBw_av))
    #DUSPmRNA
    norm_max = np.max(DUSPmRNA)
    fit[3] = compute_objval_abs(np.append(DUSPmRNA[ex_t5,0],DUSPmRNA[ex_t5,1])/norm_max,np.append(ex_egf_DUSPmRNA_av,ex_hrg_DUSPmRNA_av))
    #cFosmRNA
    norm_max = np.max(cFosmRNA)
    fit[4] = compute_objval_abs(np.append(cFosmRNA[ex_t4,0],cFosmRNA[ex_t4,1])/norm_max,np.append(ex_egf_cFosmRNA_av,ex_hrg_cFosmRNA_av))
    #cFosPro
    norm_max = np.max(cFosPro)
    fit[5] = compute_objval_abs(np.append(cFosPro[ex_t5,0],cFosPro[ex_t5,1])/norm_max,np.append(ex_egf_cFosPro_av,ex_hrg_cFosPro_av))
    #PcFos
    norm_max = np.max(PcFos)
    fit[6] = compute_objval_abs(np.append(PcFos[ex_t2,0],PcFos[ex_t2,1])/norm_max,np.append(ex_egf_PcFos_av,ex_hrg_PcFos_av))

    return np.sum(fit)