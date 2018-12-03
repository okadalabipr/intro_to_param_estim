def myGA(n_generation,n_population,n_children,n_gene,allowable_error,SearchRegion):
    np.save('./FitParam/generation.npy',int(0))
    np.save('./FitParam/FitParam0.npy',SearchParam)
    population = getInitialPopulation(n_population,n_gene,SearchRegion)
    print('Generation%d: Best Fitness = %e'%(1,population[0,-1]))
    X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)
    BestFitness = population[0,-1]
    np.save('./FitParam/generation.npy',int(1))
    np.save('./FitParam/FitParam1',X0)
    if population[0,-1] <= allowable_error:
        X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)
        BestFitness = population[0,-1]
        return X0,BestFitness
    else:
        pass
    for i in range(1,n_generation):
        population = MGGvariant(population,n_population,n_children,n_gene,SearchRegion)
        print('Generation%d: Best Fitness = %e'%(i+1,population[0,-1]))
        X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)
        if population[0,-1] < BestFitness:
            np.save('./FitParam/FitParam%d.npy'%(i+1),X0)
            np.save('./FitParam/generation.npy',int(i+1))
        BestFitness = population[0,-1]
        if population[0,-1] <= allowable_error:
            X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)
            BestFitness = population[0,-1]
            return X0,BestFitness
        else:
            pass
    X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)
    BestFitness = population[0,-1]
    return X0,BestFitness