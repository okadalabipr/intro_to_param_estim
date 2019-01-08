def MGGvariant(population,n_population,n_children,n_gene,SearchRegion):#Minimal Generation Gap selection for UNDX
    ip = [0]*3
    ip[:2] = np.random.choice(n_population,2,replace=False)
    idx = [True]*n_population
    idx[ip[0]] = False
    idx[ip[1]] = False

    children = np.empty((n_children,n_gene+1))

    for i in range(n_children):
        ip[2] = np.random.choice(np.arange(n_population)[idx])
        children[i,:] = getNewChild(population[ip,:],n_gene,SearchRegion)

    family = np.empty((n_children+2,n_gene+1))

    family[:n_children,:] = children
    family[n_children,:] = population[ip[0],:]
    family[n_children+1,:] = population[ip[1],:]

    family = family[np.argsort(family[:,-1]),:]

    population[ip[0],:] = family[0,:]#Elite
    ic1 = RankSelection(n_children+2)
    population[ip[1],:] = family[ic1,:]#Rank-based Roulette Selection

    population = population[np.argsort(population[:,-1]),:]

    return population

def getNewChild(parents,n_gene,SearchRegion):
    maxitr = np.iinfo(np.int8).max

    flg = True
    for i in range(maxitr):
        child = UNDX(parents,n_gene)
        if 0. <= np.min(child[:n_gene]) and np.max(child[:n_gene]) <= 1.:
            flg = False
            break

    if flg == True:
        child[:n_gene] = np.clip(child[:n_gene],0.,1.)

    child[-1] = getFitness(child[:n_gene],SearchRegion)

    return child

def UNDX(parents,n_gene):#Unimodal Normal Distribution Crossover
    child = np.empty(n_gene+1)
    alpha = 0.5
    beta = 0.35/(n_gene**0.5)

    p1 = parents[0,:n_gene]
    p2 = parents[1,:n_gene]
    p3 = parents[2,:n_gene]
    d1 = np.linalg.norm(p2-p1)
    d2 = np.linalg.norm((p3-p1) - (np.dot((p3-p1),(p2-p1))/(d1**2))*(p2-p1))
    e1 = p1/d1

    t = np.random.normal(scale=beta,size=n_gene)*d2
    t = t - np.dot(t,e1)*e1
    t = t + np.random.normal(scale=alpha)*d1*e1


    child[:n_gene] = t + (parents[0,:n_gene]+parents[1,:n_gene])/2.

    return child

def RankSelection(n_family):
    ranking = np.repeat(np.arange(1,n_family),np.arange(1,n_family)[-1::-1])

    np.random.shuffle(ranking)

    idx = np.random.randint(len(ranking))
    ic1 = ranking[idx]

    return ic1
