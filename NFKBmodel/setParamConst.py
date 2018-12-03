constant = [\
    'uptake',# 1.0000
    'TNF',# 1.0000
    'trigger_iIkk',# 0.0041
    'deact_TNFR',# 0.0010
    'deact_ppIkk',# 0.1660
    'deact_pnNfk',# 1000.0000
    'act_Ikk_by_TNF',# 0.0714
    'act_pIkk',# 0.0648
    'act_Ikb_by_Ikk',# 0.3980
    'act_Nfk_by_Ikk',# 0.6438
    'act_Nfk_by_Ikk_complex',# 0.2816
    'act_Ikb_complex',# 1.3897
    'form_complex',# 2.8390
    'form_complex_nuc',# 1000.0000
    'ext_nNfkIkb',# 1000.0000
    'Vnuc',# 1.0000
    'split_NfkpIkb',# 0.0811
    'split_NfkIkb',# 1.0000
    'int_Nfk',# 0.0100
    'int_Ikb',# 0.1226
    'eta_int_pNfk',# 17.9585
    'degrad_Ikb',# 0.6308
    'degrad_mIkb',# 0.0313
    'degrad_RnaA20',# 0.0089
    'degrad_A20',# 0.0116
    'prod_Ikb',# 1.0000
    'prod_mIkb_by_nNfk',# 0.0047
    'build_RnaA20',# 1.0000
    'build_A20',# 0.0006
    'shuttle_RnaA20'\
    ]

myEnum('constant')

def setParamConst():
    x = [0]*len(constant)

    x[uptake] = 3.22e+00
    x[TNF] = 1.00e+00
    x[trigger_iIkk] = 6.76e-04
    x[deact_TNFR] = 2.09e-02
    x[deact_ppIkk] = 5.41e-02
    x[deact_pnNfk] = 4.12e+02
    x[act_Ikk_by_TNF] = 5.34e-01
    x[act_pIkk] = 1.07e-03
    x[act_Ikb_by_Ikk] = 1.83e-02
    x[act_Nfk_by_Ikk] = 5.92e-02
    x[act_Nfk_by_Ikk_complex] = 1.45e-02
    x[act_Ikb_complex] = 1.97e-02
    x[form_complex] = 1.55e+00
    x[form_complex_nuc] = 1.29e+01
    x[ext_nNfkIkb] = 1.04e+04
    x[Vnuc] = 1.00e+00
    x[split_NfkpIkb] = 4.23e+00
    x[split_NfkIkb] = 1.37e-01
    x[int_Nfk] = 2.93e-02
    x[int_Ikb] = 8.16e-01
    x[eta_int_pNfk] = 6.70e+01
    x[degrad_Ikb] = 1.81e+00
    x[degrad_mIkb] = 3.55e-02
    x[degrad_RnaA20] = 4.83e-01
    x[degrad_A20] = 2.27e-02
    x[prod_Ikb] = 1.12e+00
    x[prod_mIkb_by_nNfk] = 6.69e-03
    x[build_RnaA20] = 2.50e-02
    x[build_A20] = 4.98e-05
    x[shuttle_RnaA20] = 1.29e-02

    return x

'''original(no-DCF)
x[uptake] = 1.0000
x[TNF] = 1.0000
x[trigger_iIkk] = 0.0041
x[deact_TNFR] = 0.0010
x[deact_ppIkk] = 0.1660
x[deact_pnNfk] = 1000.0000
x[act_Ikk_by_TNF] = 0.0714
x[act_pIkk] = 0.0648
x[act_Ikb_by_Ikk] = 0.3980
x[act_Nfk_by_Ikk] = 0.6438
x[act_Nfk_by_Ikk_complex] = 0.2816
x[act_Ikb_complex] = 1.3897
x[form_complex] = 2.8390
x[form_complex_nuc] = 1000.0000
x[ext_nNfkIkb] = 1000.0000
x[Vnuc] = 1.0000
x[split_NfkpIkb] = 0.0811
x[split_NfkIkb] = 1.0000
x[int_Nfk] = 0.0100
x[int_Ikb] = 0.1226
x[eta_int_pNfk] = 17.9585
x[degrad_Ikb] = 0.6308
x[degrad_mIkb] = 0.0313
x[degrad_RnaA20] = 0.0089
x[degrad_A20] = 0.0116
x[prod_Ikb] = 1.0000
x[prod_mIkb_by_nNfk] = 0.0047
x[build_RnaA20] = 1.0000
x[build_A20] = 0.0006
x[shuttle_RnaA20] = 0.0311
'''


'''DCF
uptake = 1.0000
TNF = 1.0000
trigger_iIkk = 0.0195
deact_TNFR = 0.0010
deact_ppIkk = 0.1660
deact_pnNfk = 1000.0000
act_Ikk_by_TNF = 0.0347
act_pIkk = 0.1603
act_Ikb_by_Ikk = 0.1562
act_Nfk_by_Ikk = 0.6438
act_Nfk_by_Ikk_complex = 0.2816
act_Ikb_complex = 1.3897
form_complex = 2.8390
form_complex_nuc = 1000.0000
ext_nNfkIkb = 1000.0000
Vnuc = 1.0000
split_NfkpIkb = 0.0811
split_NfkIkb = 1.0000
int_Nfk = 0.0100
int_Ikb = 0.1226
eta_int_pNfk = 17.9585
degrad_Ikb = 0.6308
degrad_mIkb = 0.0053
degrad_RnaA20 = 0.0089
degrad_A20 = 0.0116
prod_Ikb = 1.0000
prod_mIkb_by_nNfk = 0.0020
build_RnaA20 = 1.0000
build_A20 = 0.0006
shuttle_RnaA20 = 0.0119
'''