def getInitialPopulation(n_population,n_gene,SearchRegion):
    population = np.inf*np.ones((n_population,n_gene+1))

    print('initpop')
    for i in range(n_population):
        while np.isinf(population[i,-1]) or np.isnan(population[i,-1]):
            population[i,:n_gene] = np.random.rand(n_gene)
            population[i,-1] = getFitness(population[i,:n_gene],SearchRegion)
        sys.stdout.write('\r%d/%d'%(i+1,n_population))
    sys.stdout.write('\n')

    population = population[np.argsort(population[:,-1]),:]

    return population
