def lin2log(SearchRegion,n_paramConst,n_SearchParam):

    (SearchConstIdx,SearchInitIdx) = setSearchParamIdx()

    difference = list(set(np.where(np.any(SearchRegion != 0.,axis=0) == True)[0]) ^ set(np.append(SearchConstIdx,n_paramConst+SearchInitIdx)))
    if len(difference) > 0:
        for i in range(len(difference)):
            if difference[i] <= n_paramConst:
                print('Set "%s" in both SearchConstIdx and SearchRegion'%(constant[difference[i]]))
            else:
                print('Set "%s" in both SearchInitIdx and SearchRegion'%(variable[difference[i]-n_paramConst]))
        sys.exit()

    SearchRegion = SearchRegion[:,np.any(SearchRegion != 0.,axis=0)]
    if n_SearchParam != SearchRegion.shape[1]:
        print('Error: SearchRegion[lb,ub] must be positive.')
        sys.exit()

    return np.log10(SearchRegion)