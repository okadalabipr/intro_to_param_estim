from scipy.spatial.distance import cosine

def compute_objval_abs(simData,expData):#Residual Sum of Squares
    return np.dot((simData-expData),(simData-expData))

def compute_objval_cs(simData,expData):#Cosine similarity
    return cosine(simData,expData)

def compute_objval_cs2(simData_c1,simData_c2,expData_c1,expData_c2):#Cosine similarity
    simData = np.append(simData_c1,simData_c2)
    expData = np.append(expData_c1,expData_c2)
    return cosine(simData,expData)
