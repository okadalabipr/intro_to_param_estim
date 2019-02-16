def paramestim_continue():

    SearchRegion = setSearchRegion()
    SearchParamIdx = setSearchParamIdx()

    n_generation = int(10*np.iinfo(np.int16).max)
    n_population = int(3*SearchRegion.shape[1])
    n_children = 50
    n_gene = SearchRegion.shape[1]
    allowable_error = 0.0
    p0_bounds = [0.1, 10.0] # [lower_bounds, upper bounds]

    (X0,BestFitness) = myGAv2_continue(n_generation,n_population,n_children,n_gene,allowable_error,SearchParamIdx,SearchRegion,p0_bounds)