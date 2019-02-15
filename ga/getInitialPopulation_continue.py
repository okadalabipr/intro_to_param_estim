def getInitialPopulation_continue(n_population,n_gene,SearchParamIdx,SearchRegion,p0_bounds):
    generation = np.load('../FitParam/generation.npy')
    X0 = np.load('../FitParam/FitParam%d.npy'%(int(generation)))

    population = np.inf*np.ones((n_population,n_gene+1))

    print('initpop')
    for i in range(n_population):
        while np.isinf(population[i,-1]) or np.isnan(population[i,-1]):
            population[i,:n_gene] = (np.log10(X0*10**(np.random.rand(len(X0))*np.log10(p0_bounds[1]/p0_bounds[0])+np.log10(p0_bounds[0]))) - SearchRegion[0,:])/(SearchRegion[1,:] - SearchRegion[0,:])
            population[i,:n_gene] = np.clip(population[i,:n_gene],0.,1.)
            population[i,-1] = getFitness(population[i,:n_gene],SearchParamIdx,SearchRegion)
        sys.stdout.write('\r%d/%d'%(i+1,n_population))
    sys.stdout.write('\n')

    population = population[np.argsort(population[:,-1]),:]

    return population
