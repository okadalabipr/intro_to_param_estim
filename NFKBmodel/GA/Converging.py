def Converging(ip,population,n_population,n_children,n_gene,SearchRegion):
    children = np.empty((n_children,n_gene+1))
    for i in range(n_children):
        ip[2:] = np.random.choice(n_population,n_gene,replace=False)
        children[i,:] = Crossover(population[ip,:],n_gene)
    family = np.empty((n_children+2,n_gene+1))
    family[:n_children,:] = children
    family[n_children,:] = population[ip[0],:]
    family[n_children+1,:] = population[ip[1],:]
    family = family[np.argsort(family[:,-1]),:]
    population[ip[0],:] = family[0,:]#Best, either of parents
    population[ip[1],:] = family[np.random.randint(low=1,high=n_children+2,dtype=np.int),:]#Random
    if np.isinf(population[ip[1],-1]):
        population[ip[1],-1] = getFitness(population[ip[1],:n_gene],SearchRegion)
    population = population[np.argsort(population[:,-1]),:]
    return ip, population