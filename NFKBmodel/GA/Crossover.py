def Crossover(parents,n_gene):
    maxitr = np.iinfo(np.int8).max
    flg = True
    for i in range(maxitr):
        child = ENDX(parents,n_gene)
        if 0. <= np.min(child[:n_gene]) and np.max(child[:n_gene]) <= 1.:
            flg = False
            break
    if flg == True: 
        child[:n_gene] = np.clip(child[:n_gene],0.,1.)
    child[-1] = np.inf
    return child
