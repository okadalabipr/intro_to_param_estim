def decode_gene2variable(individual_gene,search_region):

    return 10.**(individual_gene*(search_region[1,:] - search_region[0,:]) + search_region[0,:])


def update_param(individual_gene,search_idx,search_region):

    x = set_param_const()
    y0 = set_initial_condition()

    X = decode_gene2variable(individual_gene,search_region)

    for i in range(len(search_idx[0])):
        x[search_idx[0][i]] = X[i]
    for i in range(len(search_idx[1])):
        y0[search_idx[1][i]] = X[i+len(search_idx[0])]

    return x, y0