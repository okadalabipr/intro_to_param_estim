def myGA_continue(n_generation,n_population,n_children,n_gene,allowable_error,SearchRegion):
    count = np.load('../FitParam/count.npy')
    generation = np.load('../FitParam/generation.npy')
    X0 = np.load('../FitParam/FitParam%d.npy'%(int(generation)))
    BestFitness = getFitness((np.log10(X0) - SearchRegion[0,:])/(SearchRegion[1,:] - SearchRegion[0,:]),SearchRegion)

    population = getInitialPopulation(n_population,n_gene,SearchRegion)

    if BestFitness < population[0,-1]:
        population[0,:n_gene] = (np.log10(X0) - SearchRegion[0,:])/(SearchRegion[1,:] - SearchRegion[0,:])
        population[0,-1] = BestFitness
    else:
        X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)
        BestFitness = population[0,-1]
        np.save('../FitParam/FitParam%d.npy'%(int(count)+1),X0)

    print('Generation%d: Best Fitness = %e'%(int(count)+1,population[0,-1]))

    if population[0,-1] <= allowable_error:
        X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)
        BestFitness = population[0,-1]
        return X0,BestFitness
    else:
        pass

    for i in range(1,n_generation):
        population = MGGvariant(population,n_population,n_children,n_gene,SearchRegion)
        print('Generation%d: Best Fitness = %e'%(i+int(count)+1,population[0,-1]))
        X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)

        if population[0,-1] < BestFitness:
            np.save('../FitParam/FitParam%d.npy'%(i+int(count)+1),X0)
            np.save('../FitParam/generation.npy',i+int(count)+1)
        BestFitness = population[0,-1]

        if population[0,-1] <= allowable_error:
            X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)
            BestFitness = population[0,-1]
            return X0,BestFitness
        else:
            pass

        np.save('../FitParam/count.npy',i+int(count)+1)

    X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)

    BestFitness = population[0,-1]

    return X0,BestFitness