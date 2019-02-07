def Converging(ip,population,n_population,n_gene,SearchRegion):
    children = np.empty((10,n_gene+1))

    for i in range(10):
        ip[2:] = np.random.choice(n_population,n_gene,replace=False)
        children[i,:] = Crossover(population[ip,:],n_gene)

    family = np.empty((12,n_gene+1))
    family[:10,:] = children
    family[10,:] = population[ip[0],:]
    family[11,:] = population[ip[1],:]

    family = family[np.argsort(family[:,-1]),:]

    population[ip[0],:] = family[0,:]#Best, either of parents
    population[ip[1],:] = family[np.random.randint(low=1,high=12,dtype=np.int),:]#Random

    if np.isinf(population[ip[1],-1]):
        population[ip[1],-1] = getFitness(population[ip[1],:n_gene],SearchRegion)

    population = population[np.argsort(population[:,-1]),:]

    return ip, population

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

def ENDX(parents,n_gene):#Extended Normal Distribution Crossover
    alpha = (1.-2*0.35**2)**0.5/2.
    beta = 0.35/(n_gene-1)**0.5

    child = np.empty(n_gene+1)

    t1 = (parents[1,:n_gene]-parents[0,:n_gene])/2.
    t2 = np.random.normal(scale=alpha)*(parents[1,:n_gene]-parents[0,:n_gene])
    t3 = np.sum(np.random.normal(scale=beta,size=n_gene)[:,None]*(parents[2:,:n_gene]-(np.sum(parents[2:,:n_gene],axis=0)/n_gene)),axis=0)

    child[:n_gene] = t1 + t2 + t3

    return child
