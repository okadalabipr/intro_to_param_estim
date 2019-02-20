def get_initial_population_continue(n_population,n_gene,search_idx,search_region,p0_bounds):
    generation = np.load('./FitParam/generation.npy')
    best_indiv = np.load('./FitParam/FitParam%d.npy'%(int(generation)))

    population = np.inf*np.ones((n_population,n_gene+1))

    print('initpop')
    for i in range(n_population):
        while np.isinf(population[i,-1]) or np.isnan(population[i,-1]):
            population[i,:n_gene] = (np.log10(best_indiv*10**(np.random.rand(len(best_indiv))*np.log10(p0_bounds[1]/p0_bounds[0])+np.log10(p0_bounds[0]))) - search_region[0,:])/(search_region[1,:] - search_region[0,:])
            population[i,:n_gene] = np.clip(population[i,:n_gene],0.,1.)
            population[i,-1] = get_fitness(population[i,:n_gene],search_idx,search_region)
        sys.stdout.write('\r%d/%d'%(i+1,n_population))
    sys.stdout.write('\n')

    population = population[np.argsort(population[:,-1]),:]

    return population


def ga_v1_continue(n_generation,n_population,n_children,n_gene,allowable_error,search_idx,search_region,p0_bounds):
    count = np.load('./FitParam/count.npy')
    generation = np.load('./FitParam/generation.npy')
    best_indiv = np.load('./FitParam/FitParam%d.npy'%(int(generation)))
    best_fitness = get_fitness((np.log10(best_indiv) - search_region[0,:])/(search_region[1,:] - search_region[0,:]),search_idx,search_region)

    population = get_initial_population_continue(n_population,n_gene,search_idx,search_region,p0_bounds)

    if best_fitness < population[0,-1]:
        population[0,:n_gene] = (np.log10(best_indiv) - search_region[0,:])/(search_region[1,:] - search_region[0,:])
        population[0,-1] = best_fitness
    else:
        best_indiv = decode_gene2variable(population[0,:n_gene],search_region)
        best_fitness = population[0,-1]
        np.save('./FitParam/FitParam%d.npy'%(int(count)+1),best_indiv)

    print('Generation%d: Best Fitness = %e'%(int(count)+1,population[0,-1]))

    if population[0,-1] <= allowable_error:
        best_indiv = decode_gene2variable(population[0,:n_gene],search_region)
        best_fitness = population[0,-1]
        return best_indiv,best_fitness
    else:
        pass

    for i in range(1,n_generation):
        population = mgg_variant(population,n_population,n_children,n_gene,search_idx,search_region)
        print('Generation%d: Best Fitness = %e'%(i+int(count)+1,population[0,-1]))
        best_indiv = decode_gene2variable(population[0,:n_gene],search_region)

        if population[0,-1] < best_fitness:
            np.save('./FitParam/FitParam%d.npy'%(i+int(count)+1),best_indiv)
            np.save('./FitParam/generation.npy',i+int(count)+1)
        best_fitness = population[0,-1]

        if population[0,-1] <= allowable_error:
            best_indiv = decode_gene2variable(population[0,:n_gene],search_region)
            best_fitness = population[0,-1]
            return best_indiv,best_fitness
        else:
            pass

        np.save('./FitParam/count.npy',i+int(count)+1)

    best_indiv = decode_gene2variable(population[0,:n_gene],search_region)

    best_fitness = population[0,-1]

    return best_indiv,best_fitness


def ga_v2_continue(n_generation,n_population,n_children,n_gene,allowable_error,search_idx,search_region,p0_bounds):

    n_iter = 1
    n0 = np.zeros(2*n_population)

    count = np.load('./FitParam/count.npy')
    generation = np.load('./FitParam/generation.npy')
    best_indiv = np.load('./FitParam/FitParam%d.npy'%(int(generation)))
    best_fitness = get_fitness((np.log10(best_indiv) - search_region[0,:])/(search_region[1,:] - search_region[0,:]),search_idx,search_region)

    population = get_initial_population_continue(n_population,n_gene,search_idx,search_region,p0_bounds)

    if best_fitness < population[0,-1]:
        population[0,:n_gene] = (np.log10(best_indiv) - search_region[0,:])/(search_region[1,:] - search_region[0,:])
        population[0,-1] = best_fitness
    else:
        best_indiv = decode_gene2variable(population[0,:n_gene],search_region)
        best_fitness = population[0,-1]
        np.save('./FitParam/FitParam%d.npy'%(int(count)+1),best_indiv)

    n0[0] = population[0,-1]

    print('Generation%d: Best Fitness = %e'%(int(count)+1,population[0,-1]))

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

        print('Generation%d: Best Fitness = %e'%(i+int(count)+1,population[0,-1]))
        best_indiv = decode_gene2variable(population[0,:n_gene],search_region)

        if population[0,-1] < best_fitness:
            np.save('./FitParam/generation.npy',i+int(count)+1)
            np.save('./FitParam/FitParam%d.npy'%(i+int(count)+1),best_indiv)
        best_fitness = population[0,-1]

        if population[0,-1] <= allowable_error:
            best_indiv = decode_gene2variable(population[0,:n_gene],search_region)
            best_fitness = population[0,-1]
            return best_indiv,best_fitness
        else:
            pass

        np.save('./FitParam/count.npy',i+int(count)+1)

    best_indiv = decode_gene2variable(population[0,:n_gene],search_region)

    best_fitness = population[0,-1]

    return best_indiv,best_fitness