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