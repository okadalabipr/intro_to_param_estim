def ENDX(parents,n_gene):#Extended Normal Distribution Crossover
    alpha = (1.-2*0.35**2)**0.5/2.
    beta = 0.35/(n_gene-1)**0.5

    child = np.empty(n_gene+1)

    t1 = (parents[1,:n_gene]-parents[0,:n_gene])/2.
    t2 = np.random.normal(scale=alpha)*(parents[1,:n_gene]-parents[0,:n_gene])
    t3 = np.sum(np.random.normal(scale=beta,size=n_gene)[:,None]*(parents[2:,:n_gene]-(np.sum(parents[2:,:n_gene],axis=0)/n_gene)),axis=0)

    child[:n_gene] = t1 + t2 + t3

    return child
