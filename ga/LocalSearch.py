def LocalSearch(ip,population,n_population,n_children,n_gene,SearchRegion):
    idx = [True]*n_population
    idx[ip[0]] = False

    children = np.empty((n_children,n_gene+1))

    for i in range(n_children):
        ip[1:] = np.random.choice(np.arange(n_population)[idx],n_gene+1,replace=False)
        children[i,:] = Mutation(population[ip,:],n_gene,SearchRegion)

    family = np.empty((n_children+1,n_gene+1))

    family[:n_children,:] = children
    family[n_children,:] = population[ip[0],:]
    family = family[np.argsort(family[:,-1]),:]

    population[ip[0],:] = family[0,:]#Elite

    population = population[np.argsort(population[:,-1]),:]

    return ip,population

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

def NDM(parents,n_gene):#Normal Distribution Mutation
    gamma = 0.35/n_gene**0.5

    child = np.empty(n_gene+1)

    t2 = np.sum(np.random.normal(scale=gamma,size=n_gene+1)[:,None]*(parents[1:,:n_gene]-(np.sum(parents[1:,:n_gene],axis=0)/(n_gene+1))),axis=0)

    child[:n_gene] = parents[0,:n_gene] + t2

    return child