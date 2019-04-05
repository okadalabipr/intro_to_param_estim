def initial_values():
    y0 = [0]*len(F_V)

    y0[ERKc] = 9.60e+02
    y0[RSKc] = 3.53e+02
    y0[CREBn] = 1.00e+03
    y0[Elk1n] = 1.51e+03

    return y0