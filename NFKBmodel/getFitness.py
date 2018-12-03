def getFitness(Individual_gene,SearchRegion):

    tspan = range(181)#180 min (Unit time: 1min)

    (x,y0) = updateParam(Individual_gene,SearchRegion)

    (T,Y) = odesolve(diffeq,y0,tspan,tuple(x))
    if T[-1] < tspan[-1]:
        return np.inf

    nuclear_NFKB = x[Vnuc]*(Y[:,pnNfk] + Y[:, nNfk] + Y[:,nNfkIkb])

    fit = compute_objval_cs(nuclear_NFKB[ex_t],ex_nuclear_NFKB)

    return fit