def get_initial_population(n_population,n_gene,search_idx,search_region):
    population = np.inf*np.ones((n_population,n_gene+1))

    print('initpop')
    for i in range(n_population):
        while np.isinf(population[i,-1]) or np.isnan(population[i,-1]):
            population[i,:n_gene] = np.random.rand(n_gene)
            population[i,-1] = get_fitness(population[i,:n_gene],search_idx,search_region)
        sys.stdout.write('\r%d/%d'%(i+1,n_population))
    sys.stdout.write('\n')

    population = population[np.argsort(population[:,-1]),:]

    return population


def ga_v1(n_generation,n_population,n_children,n_gene,allowable_error,search_idx,search_region):

    population = get_initial_population(n_population,n_gene,search_idx,search_region)
    print('Generation%d: Best Fitness = %e'%(1,population[0,-1]))
    best_indiv = decode_gene2variable(population[0,:n_gene],search_region)

    best_fitness = population[0,-1]

    np.save('./FitParam/generation.npy',1)
    np.save('./FitParam/FitParam1',best_indiv)

    if population[0,-1] <= allowable_error:
        best_indiv = decode_gene2variable(population[0,:n_gene],search_region)
        best_fitness = population[0,-1]
        return best_indiv,best_fitness
    else:
        pass

    for i in range(1,n_generation):
        population = mgg_variant(population,n_population,n_children,n_gene,search_idx,search_region)
        print('Generation%d: Best Fitness = %e'%(i+1,population[0,-1]))
        best_indiv = decode_gene2variable(population[0,:n_gene],search_region)

        if population[0,-1] < best_fitness:
            np.save('./FitParam/FitParam%d.npy'%(i+1),best_indiv)
            np.save('./FitParam/generation.npy',i+1)
        best_fitness = population[0,-1]

        if population[0,-1] <= allowable_error:
            best_indiv = decode_gene2variable(population[0,:n_gene],search_region)
            best_fitness = population[0,-1]
            return best_indiv,best_fitness
        else:
            pass

        np.save('./FitParam/count.npy',i+1)

    best_indiv = decode_gene2variable(population[0,:n_gene],search_region)

    best_fitness = population[0,-1]

    return best_indiv,best_fitness


def ga_v2(n_generation,n_population,n_children,n_gene,allowable_error,search_idx,search_region):

    n_iter = 1
    n0 = np.zeros(2*n_population)

    population = get_initial_population(n_population,n_gene,search_idx,search_region)
    n0[0] = population[0,-1]
    print('Generation%d: Best Fitness = %e'%(1,population[0,-1]))
    best_indiv = decode_gene2variable(population[0,:n_gene],search_region)
    best_fitness = population[0,-1]

    np.save('./FitParam/generation.npy',1)
    np.save('./FitParam/FitParam1.npy',best_indiv)

    if population[0,-1] <= allowable_error:
        best_indiv = decode_gene2variable(population[0,:n_gene],search_region)
        best_fitness = population[0,-1]
        return best_indiv,best_fitness
    else:
        pass

    for i in range(1,n_generation):
        ip = np.random.choice(n_population,n_gene+2,replace=False) # m=n+2
        ip, population = converging(ip,population,n_population,n_gene,search_idx,search_region)
        ip, population = local_search(ip,population,n_population,n_children,n_gene,search_idx,search_region)
        for j in range(n_iter-1):
            ip = np.random.choice(n_population,n_gene+2,replace=False)
            ip,population = converging(ip,population,n_population,n_gene,search_idx,search_region)
        if i%len(n0) == 0:
            n0 = np.zeros(len(n0))
        else:
            pass

        n0[i%len(n0)] = population[0,-1]

        if i%(len(n0)-1) == 0:
            if n0[0] == n0[len(n0)-1]:
                n_iter *= 2
            else:
                n_iter = 1

        print('Generation%d: Best Fitness = %e'%(i+1,population[0,-1]))
        best_indiv = decode_gene2variable(population[0,:n_gene],search_region)

        if population[0,-1] < best_fitness:
            np.save('./FitParam/generation.npy',i+1)
            np.save('./FitParam/FitParam%d.npy'%(i+1),best_indiv)
        best_fitness = population[0,-1]

        if population[0,-1] <= allowable_error:
            best_indiv = decode_gene2variable(population[0,:n_gene],search_region)
            best_fitness = population[0,-1]
            return best_indiv,best_fitness
        else:
            pass

        np.save('./FitParam/count.npy',i+1)

    best_indiv = decode_gene2variable(population[0,:n_gene],search_region)

    best_fitness = population[0,-1]

    return best_indiv,best_fitness
