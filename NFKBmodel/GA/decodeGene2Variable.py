def decodeGene2Variable(Individual_gene,SearchRegion):
    X = 10.**(Individual_gene*(SearchRegion[1,:] - SearchRegion[0,:]) + SearchRegion[0,:])
    return X