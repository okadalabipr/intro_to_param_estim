def runGA_continue():

    SearchRegion = setSearchRegion()

    n_generation = int(10*np.iinfo(np.int16).max)
    n_population = int(15*SearchRegion.shape[1])
    n_children = 100
    n_gene = SearchRegion.shape[1]
    allowable_error = 0.0

    (X0,BestFitness) = myGA_continue(n_generation,n_population,n_children,n_gene,allowable_error,SearchRegion)


if __name__ == '__main__':
	runGA_continue()