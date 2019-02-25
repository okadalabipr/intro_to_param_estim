def lin2log(search_idx,search_region,n_param_const,n_search_param):

    difference = list(set(np.where(np.any(search_region != 0.,axis=0))[0]) ^ set(np.append(search_idx[0],n_param_const+search_idx[1])))
    if len(difference) > 0:
        for i in range(len(difference)):
            if difference[i] <= n_param_const:
                print('Set "%s" in both search_idx_const and search_region'%(F_P[int(difference[i])]))
            else:
                print('Set "%s" in both search_idx_init and search_region'%(F_V[int(difference[i]-n_param_const)]))
        sys.exit()

    search_region = search_region[:,np.any(search_region != 0.,axis=0)]
    if n_search_param != search_region.shape[1]:
        print('Error: search_region[lb,ub] must be positive.')
        sys.exit()

    return np.log10(search_region)