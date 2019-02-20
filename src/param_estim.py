def parameter_estimation():

    search_region = set_search_region()
    search_idx = set_search_idx()

    n_generation = np.iinfo(np.int16).max
    n_population = int(3*search_region.shape[1])
    n_children = 50
    n_gene = search_region.shape[1]
    allowable_error = 0.0

    (X0,BestFitness) = ga_v2(n_generation,n_population,n_children,n_gene,allowable_error,search_idx,search_region)


def parameter_estimation_continue():

    search_region = set_search_region()
    search_idx = set_search_idx()

    n_generation = int(10*np.iinfo(np.int16).max)
    n_population = int(3*search_region.shape[1])
    n_children = 50
    n_gene = search_region.shape[1]
    allowable_error = 0.0
    p0_bounds = [0.1, 10.0] # [lower_bounds, upper bounds]

    (X0,BestFitness) = ga_v2_continue(n_generation,n_population,n_children,n_gene,allowable_error,search_idx,search_region,p0_bounds)