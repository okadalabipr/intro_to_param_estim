#Refined Model
def diffeq(t,y,x):

    v1 = x[V1] * x[a] * y[ppMEKc] * y[ERKc] /  ( x[Km1] * (1 + y[pERKc] / x[Km2]) + y[ERKc] )
    v2 = x[V2] * x[a] * y[ppMEKc] * y[pERKc] /  ( x[Km2] * (1 + y[ERKc] / x[Km1]) + y[pERKc] )
    v3 = x[V3] * y[pERKc] /  ( x[Km3] * (1 + y[ppERKc] / x[Km4]) + y[pERKc] )
    v4 = x[V4] * y[ppERKc] /  ( x[Km4]* (1 + y[pERKc] / x[Km3]) + y[ppERKc] )
    v5 = x[V5] * y[pERKn] /  ( x[Km5] * (1 + y[ppERKn] / x[Km6]) + y[pERKn] )
    v6 = x[V6] * y[ppERKn] /  ( x[Km6] * (1 + y[pERKn] / x[Km5]) + y[ppERKn] )
    v7 = x[KimERK] * y[ERKc] - x[KexERK] * (x[Vn]/x[Vc]) * y[ERKn]
    v8 = x[KimpERK] * y[pERKc] - x[KexpERK] * (x[Vn]/x[Vc]) * y[pERKn]
    v9 = x[KimppERK] * y[ppERKc] - x[KexppERK] * (x[Vn]/x[Vc]) * y[ppERKn]
    v10 = x[V10] * y[ppERKn]**x[n10] / ( x[Km10]**x[n10] + y[ppERKn]**x[n10] )
    v11 = x[p11] * y[PreduspmRNAn]
    v12 = x[p12] * y[duspmRNAc]
    v13 = x[p13] * y[duspmRNAc]
    v14 = x[V14] * y[ppERKc] * y[DUSPc] / ( x[Km14] + y[DUSPc] )
    v15 = x[V15] * y[pDUSPc] / ( x[Km15] + y[pDUSPc] )
    v16 = x[p16] * y[DUSPc]
    v17 = x[p17] * y[pDUSPc]
    v18 = x[KimDUSP] * y[DUSPc] - x[KexDUSP] * (x[Vn]/x[Vc]) * y[DUSPn]
    v19 = x[KimpDUSP] * y[pDUSPc] - x[KexpDUSP] * (x[Vn]/x[Vc]) * y[pDUSPn]
    v20 = x[V20] * y[ppERKn] * y[DUSPn] / ( x[Km20] + y[DUSPn] )
    v21 = x[V21] * y[pDUSPn] / ( x[Km21] + y[pDUSPn] )
    v22 = x[p22] * y[DUSPn]
    v23 = x[p23] * y[pDUSPn]
    v24 = x[V24] * y[ppERKc] * y[RSKc] / ( x[Km24] + y[RSKc] )
    v25 = x[V25] * y[pRSKc] / ( x[Km25] + y[pRSKc] )
    v26 = x[KimRSK] * y[pRSKc] - x[KexRSK] * (x[Vn]/x[Vc]) * y[pRSKn]
    v27 = x[V27] * y[pRSKn] * y[CREBn] / ( x[Km27] + y[CREBn] )
    v28 = x[V28] * y[pCREBn] / ( x[Km28] + y[pCREBn] )
    v29 = x[V29] * y[ppERKn] * y[Elk1n] / ( x[Km29] + y[Elk1n] )
    v30 = x[V30] * y[pElk1n] / ( x[Km30] + y[pElk1n] )
    v31 = x[V31] * (y[pCREBn] * y[pElk1n])**x[n31] / ( x[Km31]**x[n31] + (y[pCREBn] * y[pElk1n])**x[n31] + (y[Fn] / x[KF31])**x[nF31] )
    v32 = x[p32] * y[PrecfosmRNAn]
    v33 = x[p33] * y[cfosmRNAc]
    v34 = x[p34] * y[cfosmRNAc]
    v35 = x[V35] * y[ppERKc] * y[cFOSc] / ( x[Km35] + y[cFOSc] )
    v36 = x[V36] * y[pRSKc] * y[cFOSc] / ( x[Km36] + y[cFOSc] )
    v37 = x[V37] * y[pcFOSc] / ( x[Km37] + y[pcFOSc] )
    v38 = x[p38] * y[cFOSc]
    v39 = x[p39] * y[pcFOSc]
    v40 = x[KimFOS] * y[cFOSc] - x[KexFOS] * (x[Vn]/x[Vc]) * y[cFOSn]
    v41 = x[KimpcFOS] * y[pcFOSc] - x[KexpcFOS] * (x[Vn]/x[Vc]) * y[pcFOSn]
    v42 = x[V42] * y[ppERKn] * y[cFOSn] / ( x[Km42] + y[cFOSn] )
    v43 = x[V43] * y[pRSKn] * y[cFOSn] / ( x[Km43] + y[cFOSn] )
    v44 = x[V44] * y[pcFOSn] / ( x[Km44] + y[pcFOSn] )
    v45 = x[p45] * y[cFOSn]
    v46 = x[p46] * y[pcFOSn]
    v47 = x[p47] * y[DUSPn] * y[ppERKn] - x[m47] * y[DUSPn_ppERKn]
    v48 = x[p48] * y[DUSPn_ppERKn]
    v49 = x[p49] * y[DUSPn] * y[pERKn] - x[m49] * y[DUSPn_pERKn]
    v50 = x[p50] * y[DUSPn_pERKn]
    v51 = x[p51] * y[DUSPn] * y[ERKn] - x[m51] * y[DUSPn_ERKn]
    v52 = x[p52] * y[pDUSPn] * y[ppERKn] - x[m52] * y[pDUSPn_ppERKn]
    v53 = x[p53] * y[pDUSPn_ppERKn]
    v54 = x[p54] * y[pDUSPn] * y[pERKn] - x[m54] * y[pDUSPn_pERKn]
    v55 = x[p55] * y[pDUSPn_pERKn]
    v56 = x[p56] * y[pDUSPn] * y[ERKn] - x[m56] * y[pDUSPn_ERKn]
    v57 = x[V57] * y[pcFOSn]**x[n57] / ( x[Km57]**x[n57] + y[pcFOSn]**x[n57] )
    v58 = x[p58] * y[PreFmRNAn]
    v59 = x[p59] * y[FmRNAc]
    v60 = x[p60] * y[FmRNAc]
    v61 = x[p61] * y[Fc]
    v62 = x[KimF] * y[Fc] - x[KexF] * (x[Vn]/x[Vc]) * y[Fn]
    v63 = x[p63] * y[Fn]

    dydt = [0]*len(variable)

    if x[Ligand] == x[EGF]:#EGF=10nM
        if t < 300.:
            dydt[ppMEKc] = 0.00258
        elif t < 600.:
            dydt[ppMEKc] = -0.00111
        elif t < 900.:
            dydt[ppMEKc] = -0.000625
        elif t < 1200.:
            dydt[ppMEKc] = -0.000135
        elif t < 1800.:
            dydt[ppMEKc] = -0.000135
        elif t < 2700.:
            dydt[ppMEKc] = -0.0000480
        elif t < 3600.:
            dydt[ppMEKc] = -0.00000852
        elif t <= 5400.:
            dydt[ppMEKc] = -0.00000728

    elif x[Ligand] == x[HRG]:#HRG=10nM
        if t < 300.:
            dydt[ppMEKc] = 0.00288
        elif t < 600.:
            dydt[ppMEKc] = 0.000451
        elif t < 900.:
            dydt[ppMEKc] = -0.000545
        elif t < 1200.:
            dydt[ppMEKc] = 0.0000522
        elif t < 1800.:
            dydt[ppMEKc] = 0.0000522
        elif t < 2700.:
            dydt[ppMEKc] = 0.0000399
        elif t < 3600.:
            dydt[ppMEKc] = -0.0000500
        elif t <= 5400.:
            dydt[ppMEKc] = -0.0000478
    else:
        sys.exit()

    dydt[CREBn] = -v27 + v28
    dydt[pCREBn] = v27 - v28
    dydt[ERKc] = -v1 + v3 - v7
    dydt[ERKn] = v5 + v7*(x[Vc]/x[Vn]) + v50 -v51 + v55 -v56
    dydt[pERKc] = v1 - v2 -v3 +v4 -v8
    dydt[pERKn] = -v5 + v6 + v8*(x[Vc]/x[Vn]) + v48 - v49 + v53 - v54
    dydt[ppERKc] =  v2 - v4 - v9
    dydt[ppERKn] = -v6 + v9*(x[Vc]/x[Vn]) - v47 - v52
    dydt[Elk1n] = -v29 + v30
    dydt[pElk1n] = v29 - v30
    dydt[cFOSc] = v34 - v35 - v36 + v37 - v38 - v40
    dydt[cFOSn] = v40*(x[Vc]/x[Vn]) - v42 - v43 + v44 - v45
    dydt[pcFOSc] = v35 + v36 - v37 - v39 - v41
    dydt[pcFOSn] = v41*(x[Vc]/x[Vn]) + v42 + v43 - v44 - v46
    dydt[DUSPc] = v13 - v14 + v15 - v16 - v18
    dydt[DUSPn] = v18*(x[Vc]/x[Vn]) - v20 + v21 - v22 - v47 + v48 - v49 + v50 - v51
    dydt[pDUSPc] = v14 - v15 - v17 - v19
    dydt[pDUSPn] = v19*(x[Vc]/x[Vn]) + v20 - v21 - v23 - v52 + v53 - v54 + v55 - v56
    dydt[DUSPn_ERKn] = v51
    dydt[DUSPn_pERKn] = v49 - v50
    dydt[DUSPn_ppERKn] = v47 - v48
    dydt[pDUSPn_ERKn] = v56
    dydt[pDUSPn_pERKn] = v54 - v55
    dydt[pDUSPn_ppERKn] = v52 - v53
    dydt[RSKc] = -v24 + v25
    dydt[pRSKc] = v24 - v25 - v26
    dydt[pRSKn] = v26*(x[Vc]/x[Vn])
    dydt[PrecfosmRNAn] = v31 - v32
    dydt[PreduspmRNAn] = v10 - v11
    dydt[cfosmRNAc] = v32*(x[Vn]/x[Vc]) - v33
    dydt[duspmRNAc] = v11*(x[Vn]/x[Vc]) - v12
    dydt[Fc] = v60 - v61 - v62
    dydt[Fn] = v62*(x[Vc]/x[Vn]) - v63
    dydt[FmRNAc] = v58*(x[Vn]/x[Vc]) - v59
    dydt[PreFmRNAn] = v57 - v58

    return dydt
