def UNDX(parents,n_gene):#Unimodal Normal Distribution Crossover
    child = np.empty(n_gene+1)
    alpha = 0.5
    beta = 0.35/(n_gene**0.5)
    p1 = parents[0,:n_gene]
    p2 = parents[1,:n_gene]
    p3 = parents[2,:n_gene]
    d1 = np.linalg.norm(p2-p1)
    d2 = np.linalg.norm((p3-p1) - (np.dot((p3-p1),(p2-p1))/(d1**2))*(p2-p1))
    e1 = p1/d1
    t = np.random.normal(scale=beta,size=n_gene)*d2
    t = t - np.dot(t,e1)*e1
    t = t + np.random.normal(scale=alpha)*d1*e1

    child[:n_gene] = t + (parents[0,:n_gene]+parents[1,:n_gene])/2
    return child