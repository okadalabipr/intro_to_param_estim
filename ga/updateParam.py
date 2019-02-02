def updateParam(Individual_gene,SearchRegion):

    x = setParamConst()
    y0 = initialValues()

    (SearchConstIdx,SearchInitIdx) = setSearchParamIdx()

    X = decodeGene2Variable(Individual_gene,SearchRegion)

    for i in range(len(SearchConstIdx)):
        x[SearchConstIdx[i]] = X[i]
    for i in range(len(SearchInitIdx)):
        y0[SearchInitIdx[i]] = X[i+len(SearchConstIdx)]

    return x, y0
