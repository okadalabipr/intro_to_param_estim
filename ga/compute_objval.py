def compute_objval_abs(simData,exData):#Residual Sum of Squares
    return np.dot((simData-exData),(simData-exData))

def compute_objval_cs(simData,exData):#Cosine similarity
    return cosine(simData,exData)

def compute_objval_cs2(simData_c1,simData_c2,exData_c1,exData_c2):#Cosine similarity
    simData = np.append(simData_c1,simData_c2)
    exData = np.append(exData_c1,exData_c2)
    return cosine(simData,exData)
