def bestParam():
    x = setParamConst()
    y0 = initialValues()


    generation = np.load('../FitParam/generation.npy')
    X0 = np.load('../FitParam/FitParam%d.npy'%(int(generation)))#

    for i in range(len(SearchConstIdx)):
        x[SearchConstIdx[i]] = X0[i]
    for i in range(len(SearchInitIdx)):
        y0[SearchInitIdx[i]] = X0[i+len(SearchConstIdx)]

    return x, y0
