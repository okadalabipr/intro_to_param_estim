from scipy.spatial.distance import cosine

def compute_objval_abs(simData,expData):#Residual Sum of Squares
    return np.dot((simData-expData),(simData-expData))

def compute_objval_cs(simData,expData):#Cosine similarity
    return cosine(simData,expData)