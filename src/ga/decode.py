def decodeGene2Variable(Individual_gene,SearchRegion):
    return 10.**(Individual_gene*(SearchRegion[1,:] - SearchRegion[0,:]) + SearchRegion[0,:])

def updateParam(Individual_gene,SearchParamIdx,SearchRegion):

    x = setParamConst()
    y0 = initialValues()

    X = decodeGene2Variable(Individual_gene,SearchRegion)

    for i in range(len(SearchParamIdx[0])):
        x[SearchParamIdx[0][i]] = X[i]
    for i in range(len(SearchParamIdx[1])):
        y0[SearchParamIdx[1][i]] = X[i+len(SearchParamIdx[0])]

    return x, y0