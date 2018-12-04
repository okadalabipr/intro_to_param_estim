from scipy.spatial.distance import cosine

def compute_objval_abs(simData,exData):#Residual Sum of Squares
    return np.dot((simData-exData),(simData-exData))

def compute_objval_cs(simData,exData):#Cosine similarity
    return cosine(simData,exData)

def compute_objval_cs2(simData_egf,simData_hrg,exData_egf,exData_hrg):#Cosine similarity
    simData = np.append(simData_egf,simData_hrg)
    exData = np.append(exData_egf,exData_hrg)
    return cosine(simData,exData)