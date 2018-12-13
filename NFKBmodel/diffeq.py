#diffeq
def diffeq(t,y,x):

    dydt = [0]*len(variable)

    dydt[TNFR] = x[uptake]*x[TNF] - x[deact_TNFR]*y[TNFR]
    dydt[Ikk] = -(x[act_Ikk_by_TNF]*y[TNFR]*y[Ikk]) + (x[trigger_iIkk]*y[iIkk])
    dydt[pIkk] = (x[act_Ikk_by_TNF]*y[TNFR]*y[Ikk]) - (x[act_pIkk]*y[pIkk])
    dydt[ppIkk] = (x[act_pIkk]*y[pIkk]) - (x[deact_ppIkk]*y[ppIkk])
    dydt[iIkk] = (x[deact_ppIkk]*y[ppIkk]) - (x[trigger_iIkk]*y[iIkk])
    dydt[NfkIkb] = -((x[act_Ikb_by_Ikk])*y[pIkk]*y[NfkIkb]) - ((x[act_Nfk_by_Ikk])*y[pIkk]*y[NfkIkb]) + (x[form_complex]*y[Nfk]*y[Ikb]) + (x[ext_nNfkIkb]*y[nNfkIkb])*(x[Vnuc]/1.)
    dydt[NfkpIkb] = ((x[act_Ikb_by_Ikk])*y[pIkk]*y[NfkIkb]) - ((x[act_Nfk_by_Ikk_complex])*y[pIkk]*y[NfkpIkb]) - (x[split_NfkpIkb]*y[NfkpIkb])
    dydt[pNfkIkb] = -((x[act_Ikb_complex])*y[pNfkIkb]) - ((x[act_Ikb_by_Ikk])*y[pIkk]*y[pNfkIkb]) + ((x[act_Nfk_by_Ikk])*y[pIkk]*y[NfkIkb])
    dydt[pNfkpIkb] = ((x[act_Ikb_complex])*y[pNfkIkb]) + ((x[act_Ikb_by_Ikk])*y[pIkk]*y[pNfkIkb]) + ((x[act_Nfk_by_Ikk_complex])*y[pIkk]*y[NfkpIkb]) - (x[split_NfkIkb]*y[pNfkpIkb])
    dydt[pNfk] = (x[split_NfkIkb]*y[pNfkpIkb]) - ((x[int_Nfk]*x[eta_int_pNfk])*y[pNfk])
    dydt[Nfk] = (x[split_NfkpIkb]*y[NfkpIkb]) - (x[form_complex]*y[Nfk]*y[Ikb]) - ((x[int_Nfk])*y[Nfk])
    dydt[pIkb] = (x[split_NfkpIkb]*y[NfkpIkb]) + (x[split_NfkIkb]*y[pNfkpIkb]) - (x[degrad_Ikb]*y[pIkb])
    dydt[Ikb] = -(x[form_complex]*y[Nfk]*y[Ikb]) + (x[prod_Ikb]*y[mIkb]) - (x[int_Ikb]*y[Ikb])
    dydt[mIkb] = (x[prod_mIkb_by_nNfk]*y[nNfk]) - (x[degrad_mIkb]*y[mIkb])
    dydt[nIkb] = (x[int_Ikb]*y[Ikb])*(1./x[Vnuc]) - (x[form_complex_nuc]*y[nNfk]*y[nIkb])
    dydt[pnNfk] = ((x[int_Nfk]*x[eta_int_pNfk])*y[pNfk])*(1./x[Vnuc]) - (x[deact_pnNfk]*y[pnNfk])
    dydt[nNfk] = ((x[int_Nfk])*y[Nfk])*(1./x[Vnuc]) + (x[deact_pnNfk]*y[pnNfk]) - (x[form_complex_nuc]*y[nNfk]*y[nIkb])
    dydt[nNfkIkb] = (x[form_complex_nuc]*y[nNfk]*y[nIkb]) - (x[ext_nNfkIkb]*y[nNfkIkb])
    dydt[RnaA20_1] = (x[build_RnaA20]*y[nNfk]) - (x[shuttle_RnaA20]*y[RnaA20_1])
    dydt[RnaA20] = (x[shuttle_RnaA20]*y[RnaA20_1]) - (x[degrad_RnaA20]*y[RnaA20])
    dydt[A20] = (x[build_A20]*y[RnaA20]) - (x[degrad_A20]*y[A20])

    return dydt
