def NDM(parents,n_gene):#Normal Distribution Mutation
    gamma = 0.35/n_gene**0.5

    child = np.empty(n_gene+1)

    t2 = np.sum(np.random.normal(scale=gamma,size=n_gene+1)[:,None]*(parents[1:,:n_gene]-(np.sum(parents[1:,:n_gene],axis=0)/(n_gene+1))),axis=0)

    child[:n_gene] = parents[0,:n_gene] + t2

    return child
