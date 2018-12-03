def initialValues():
    #initialValues
    y0 = [0]*len(variable)

    y0[TNFR]     = 0.
    y0[Ikk]      = 1.
    y0[pIkk]     = 0.
    y0[ppIkk]    = 0.
    y0[iIkk]     = 0.
    y0[NfkIkb]   = 1.
    y0[NfkpIkb]  = 0.
    y0[pNfkIkb]  = 0.
    y0[pNfk]     = 0.
    y0[Nfk]      = 0.
    y0[pIkb]     = 0.
    y0[Ikb]      = 0.
    y0[mIkb]     = 0.
    y0[nIkb]     = 0.
    y0[pnNfk]    = 0.
    y0[nNfk]     = 0.
    y0[nNfkIkb]  = 0.
    y0[RnaA20_1] = 0.
    y0[RnaA20]   = 0.
    y0[A20]      = 0.

    return y0