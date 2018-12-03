def Mutation(parents,n_gene,SearchRegion):
    maxitr = np.iinfo(np.int8).max
    flg = True
    for i in range(maxitr):
        child = NDM(parents,n_gene)
        if 0. <= np.min(child[:n_gene]) and np.max(child[:n_gene]) <= 1.:
            flg = False
            break
    if flg == True:
        child[:n_gene] = np.clip(child[:n_gene],0.,1.)
    child[-1] = getFitness(child[:n_gene],SearchRegion)
    return child
