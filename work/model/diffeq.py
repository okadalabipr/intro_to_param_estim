#Refined Model
def diffeq(t,y,x):

    v = [0]*64 #Rate equations

    v[1] = x[V1] * x[a] * y[ppMEKc] * y[ERKc] /  ( x[Km1] * (1 + y[pERKc] / x[Km2]) + y[ERKc] )
    v[2] = x[V2] * x[a] * y[ppMEKc] * y[pERKc] /  ( x[Km2] * (1 + y[ERKc] / x[Km1]) + y[pERKc] )
    v[3] = x[V3] * y[pERKc] /  ( x[Km3] * (1 + y[ppERKc] / x[Km4]) + y[pERKc] )
    v[4] = x[V4] * y[ppERKc] /  ( x[Km4]* (1 + y[pERKc] / x[Km3]) + y[ppERKc] )
    v[5] = x[V5] * y[pERKn] /  ( x[Km5] * (1 + y[ppERKn] / x[Km6]) + y[pERKn] )
    v[6] = x[V6] * y[ppERKn] /  ( x[Km6] * (1 + y[pERKn] / x[Km5]) + y[ppERKn] )
    v[7] = x[KimERK] * y[ERKc] - x[KexERK] * (x[Vn]/x[Vc]) * y[ERKn]
    v[8] = x[KimpERK] * y[pERKc] - x[KexpERK] * (x[Vn]/x[Vc]) * y[pERKn]
    v[9] = x[KimppERK] * y[ppERKc] - x[KexppERK] * (x[Vn]/x[Vc]) * y[ppERKn]
    v[10] = x[V10] * y[ppERKn]**x[n10] / ( x[Km10]**x[n10] + y[ppERKn]**x[n10] )
    v[11] = x[p11] * y[PreduspmRNAn]
    v[12] = x[p12] * y[duspmRNAc]
    v[13] = x[p13] * y[duspmRNAc]
    v[14] = x[V14] * y[ppERKc] * y[DUSPc] / ( x[Km14] + y[DUSPc] )
    v[15] = x[V15] * y[pDUSPc] / ( x[Km15] + y[pDUSPc] )
    v[16] = x[p16] * y[DUSPc]
    v[17] = x[p17] * y[pDUSPc]
    v[18] = x[KimDUSP] * y[DUSPc] - x[KexDUSP] * (x[Vn]/x[Vc]) * y[DUSPn]
    v[19] = x[KimpDUSP] * y[pDUSPc] - x[KexpDUSP] * (x[Vn]/x[Vc]) * y[pDUSPn]
    v[20] = x[V20] * y[ppERKn] * y[DUSPn] / ( x[Km20] + y[DUSPn] )
    v[21] = x[V21] * y[pDUSPn] / ( x[Km21] + y[pDUSPn] )
    v[22] = x[p22] * y[DUSPn]
    v[23] = x[p23] * y[pDUSPn]
    v[24] = x[V24] * y[ppERKc] * y[RSKc] / ( x[Km24] + y[RSKc] )
    v[25] = x[V25] * y[pRSKc] / ( x[Km25] + y[pRSKc] )
    v[26] = x[KimRSK] * y[pRSKc] - x[KexRSK] * (x[Vn]/x[Vc]) * y[pRSKn]
    v[27] = x[V27] * y[pRSKn] * y[CREBn] / ( x[Km27] + y[CREBn] )
    v[28] = x[V28] * y[pCREBn] / ( x[Km28] + y[pCREBn] )
    v[29] = x[V29] * y[ppERKn] * y[Elk1n] / ( x[Km29] + y[Elk1n] )
    v[30] = x[V30] * y[pElk1n] / ( x[Km30] + y[pElk1n] )
    v[31] = x[V31] * (y[pCREBn] * y[pElk1n])**x[n31] / ( x[Km31]**x[n31] + (y[pCREBn] * y[pElk1n])**x[n31] + (y[Fn] / x[KF31])**x[nF31] )
    v[32] = x[p32] * y[PrecfosmRNAn]
    v[33] = x[p33] * y[cfosmRNAc]
    v[34] = x[p34] * y[cfosmRNAc]
    v[35] = x[V35] * y[ppERKc] * y[cFOSc] / ( x[Km35] + y[cFOSc] )
    v[36] = x[V36] * y[pRSKc] * y[cFOSc] / ( x[Km36] + y[cFOSc] )
    v[37] = x[V37] * y[pcFOSc] / ( x[Km37] + y[pcFOSc] )
    v[38] = x[p38] * y[cFOSc]
    v[39] = x[p39] * y[pcFOSc]
    v[40] = x[KimFOS] * y[cFOSc] - x[KexFOS] * (x[Vn]/x[Vc]) * y[cFOSn]
    v[41] = x[KimpcFOS] * y[pcFOSc] - x[KexpcFOS] * (x[Vn]/x[Vc]) * y[pcFOSn]
    v[42] = x[V42] * y[ppERKn] * y[cFOSn] / ( x[Km42] + y[cFOSn] )
    v[43] = x[V43] * y[pRSKn] * y[cFOSn] / ( x[Km43] + y[cFOSn] )
    v[44] = x[V44] * y[pcFOSn] / ( x[Km44] + y[pcFOSn] )
    v[45] = x[p45] * y[cFOSn]
    v[46] = x[p46] * y[pcFOSn]
    v[47] = x[p47] * y[DUSPn] * y[ppERKn] - x[m47] * y[DUSPn_ppERKn]
    v[48] = x[p48] * y[DUSPn_ppERKn]
    v[49] = x[p49] * y[DUSPn] * y[pERKn] - x[m49] * y[DUSPn_pERKn]
    v[50] = x[p50] * y[DUSPn_pERKn]
    v[51] = x[p51] * y[DUSPn] * y[ERKn] - x[m51] * y[DUSPn_ERKn]
    v[52] = x[p52] * y[pDUSPn] * y[ppERKn] - x[m52] * y[pDUSPn_ppERKn]
    v[53] = x[p53] * y[pDUSPn_ppERKn]
    v[54] = x[p54] * y[pDUSPn] * y[pERKn] - x[m54] * y[pDUSPn_pERKn]
    v[55] = x[p55] * y[pDUSPn_pERKn]
    v[56] = x[p56] * y[pDUSPn] * y[ERKn] - x[m56] * y[pDUSPn_ERKn]
    v[57] = x[V57] * y[pcFOSn]**x[n57] / ( x[Km57]**x[n57] + y[pcFOSn]**x[n57] )
    v[58] = x[p58] * y[PreFmRNAn]
    v[59] = x[p59] * y[FmRNAc]
    v[60] = x[p60] * y[FmRNAc]
    v[61] = x[p61] * y[Fc]
    v[62] = x[KimF] * y[Fc] - x[KexF] * (x[Vn]/x[Vc]) * y[Fn]
    v[63] = x[p63] * y[Fn]

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

    dydt[CREBn] = -v[27] + v[28]
    dydt[pCREBn] = v[27] - v[28]
    dydt[ERKc] = -v[1] + v[3] - v[7]
    dydt[ERKn] = v[5] + v[7]*(x[Vc]/x[Vn]) + v[50] -v[51] + v[55] -v[56]
    dydt[pERKc] = v[1] - v[2] -v[3] +v[4]-v[8]
    dydt[pERKn] = -v[5] + v[6] + v[8]*(x[Vc]/x[Vn]) + v[48] - v[49] + v[53] - v[54]
    dydt[ppERKc] =  v[2] - v[4] - v[9]
    dydt[ppERKn] = -v[6] + v[9]*(x[Vc]/x[Vn]) - v[47] - v[52]
    dydt[Elk1n] = -v[29] + v[30]
    dydt[pElk1n] = v[29] - v[30]
    dydt[cFOSc] = v[34] - v[35] - v[36] + v[37] - v[38] - v[40]
    dydt[cFOSn] = v[40]*(x[Vc]/x[Vn]) - v[42] - v[43] + v[44] - v[45]
    dydt[pcFOSc] = v[35] + v[36] - v[37] - v[39] - v[41]
    dydt[pcFOSn] = v[41]*(x[Vc]/x[Vn]) + v[42] + v[43] - v[44] - v[46]
    dydt[DUSPc] = v[13] - v[14] + v[15] - v[16] - v[18]
    dydt[DUSPn] = v[18]*(x[Vc]/x[Vn]) - v[20] + v[21] - v[22] - v[47] + v[48] - v[49] + v[50] - v[51]
    dydt[pDUSPc] = v[14] - v[15] - v[17] - v[19]
    dydt[pDUSPn] = v[19]*(x[Vc]/x[Vn]) + v[20] - v[21] - v[23] - v[52] + v[53] - v[54] + v[55] - v[56]
    dydt[DUSPn_ERKn] = v[51]
    dydt[DUSPn_pERKn] = v[49] - v[50]
    dydt[DUSPn_ppERKn] = v[47] - v[48]
    dydt[pDUSPn_ERKn] = v[56]
    dydt[pDUSPn_pERKn] = v[54] - v[55]
    dydt[pDUSPn_ppERKn] = v[52] - v[53]
    dydt[RSKc] = -v[24] + v[25]
    dydt[pRSKc] = v[24] - v[25] - v[26]
    dydt[pRSKn] = v[26]*(x[Vc]/x[Vn])
    dydt[PrecfosmRNAn] = v[31] - v[32]
    dydt[PreduspmRNAn] = v[10] - v[11]
    dydt[cfosmRNAc] = v[32]*(x[Vn]/x[Vc]) - v[33]
    dydt[duspmRNAc] = v[11]*(x[Vn]/x[Vc]) - v[12]
    dydt[Fc] = v[60] - v[61] - v[62]
    dydt[Fn] = v[62]*(x[Vc]/x[Vn]) - v[63]
    dydt[FmRNAc] = v[58]*(x[Vn]/x[Vc]) - v[59]
    dydt[PreFmRNAn] = v[57] - v[58]

    return dydt