def myGAv2_continue(n_generation,n_population,n_children,n_gene,allowable_error,SearchRegion,p0_bounds):

    N_iter = 1
    N0 = np.zeros(2*n_population)

    count = np.load('../FitParam/count.npy')
    generation = np.load('../FitParam/generation.npy')
    X0 = np.load('../FitParam/FitParam%d.npy'%(int(generation)))
    BestFitness = getFitness((np.log10(X0) - SearchRegion[0,:])/(SearchRegion[1,:] - SearchRegion[0,:]),SearchRegion)

    population = getInitialPopulation_continue(n_population,n_gene,SearchRegion,p0_bounds)

    if BestFitness < population[0,-1]:
        population[0,:n_gene] = (np.log10(X0) - SearchRegion[0,:])/(SearchRegion[1,:] - SearchRegion[0,:])
        population[0,-1] = BestFitness
    else:
        X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)
        BestFitness = population[0,-1]
        np.save('../FitParam/FitParam%d.npy'%(int(count)+1),X0)

    N0[0] = population[0,-1]

    print('Generation%d: Best Fitness = %e'%(int(count)+1,population[0,-1]))

    if population[0,-1] <= allowable_error:
        X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)
        BestFitness = population[0,-1]
        return X0,BestFitness
    else:
        pass

    for i in range(1,n_generation):
        ip = np.random.choice(n_population,n_gene+2,replace=False)# m=n+2
        ip, population = Converging(ip,population,n_population,n_gene,SearchRegion)
        ip, population = LocalSearch(ip,population,n_population,n_children,n_gene,SearchRegion)
        for j in range(N_iter-1):
            ip = np.random.choice(n_population,n_gene+2,replace=False)
            ip,population = Converging(ip,population,n_population,n_gene,SearchRegion)
        if i%len(N0) == 0:
            N0 = np.zeros(len(N0))
        else:
            pass

        N0[i%len(N0)] = population[0,-1]

        if i%(len(N0)-1) == 0:
            if N0[0] == N0[len(N0)-1]:
                N_iter *= 2
            else:
                N_iter = 1

        print('Generation%d: Best Fitness = %e'%(i+int(count)+1,population[0,-1]))
        X0 = decodeGene2Variable(population[0,:n_gene],SearchRegion)

        if population[0,-1] < BestFitness:
            np.save('../FitParam/generation.npy',i+int(count)+1)
            np.save('../FitParam/FitParam%d.npy'%(i+int(count)+1),X0)
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