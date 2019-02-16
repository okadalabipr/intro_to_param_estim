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

def myGA_continue(n_generation,n_population,n_children,n_gene,allowable_error,SearchParamIdx,SearchRegion,p0_bounds):
    count = np.load('../FitParam/count.npy')
    generation = np.load('../FitParam/generation.npy')
    X0 = np.load('../FitParam/FitParam%d.npy'%(int(generation)))
    BestFitness = getFitness((np.log10(X0) - SearchRegion[0,:])/(SearchRegion[1,:] - SearchRegion[0,:]),SearchParamIdx,SearchRegion)

    population = getInitialPopulation_continue(n_population,n_gene,SearchParamIdx,SearchRegion,p0_bounds)

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
        population = MGGvariant(population,n_population,n_children,n_gene,SearchParamIdx,SearchRegion)
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

def myGAv2_continue(n_generation,n_population,n_children,n_gene,allowable_error,SearchParamIdx,SearchRegion,p0_bounds):

    N_iter = 1
    N0 = np.zeros(2*n_population)

    count = np.load('../FitParam/count.npy')
    generation = np.load('../FitParam/generation.npy')
    X0 = np.load('../FitParam/FitParam%d.npy'%(int(generation)))
    BestFitness = getFitness((np.log10(X0) - SearchRegion[0,:])/(SearchRegion[1,:] - SearchRegion[0,:]),SearchParamIdx,SearchRegion)

    population = getInitialPopulation_continue(n_population,n_gene,SearchParamIdx,SearchRegion,p0_bounds)

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
        ip, population = Converging(ip,population,n_population,n_gene,SearchParamIdx,SearchRegion)
        ip, population = LocalSearch(ip,population,n_population,n_children,n_gene,SearchParamIdx,SearchRegion)
        for j in range(N_iter-1):
            ip = np.random.choice(n_population,n_gene+2,replace=False)
            ip,population = Converging(ip,population,n_population,n_gene,SearchParamIdx,SearchRegion)
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