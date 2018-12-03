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