import numpy as np
import math

def prob(x, y, k, N, i, twoD = True):
    xdif = x - x[i]
    ydif = y - y[i]
    probxy = 0
    if twoD:
        dsq = np.array([xdif[j]**2 + ydif[j]**2 for j in range(len(x))])
        dsq = np.delete(dsq, i)
        nndxysq = np.partition(dsq, k)[k]
        probxy = 1 / (N*math.pi*nndxysq)
    xdif = np.delete(xdif, i)
    ydif = np.delete(ydif, i)
    nndx = np.partition(np.absolute(xdif), k)[k]
    nndy = np.partition(np.absolute(ydif), k)[k]
    probx = 1 / (N*nndx*2)
    proby = 1 / (N*nndy*2)
    if twoD:
        return [probxy, probx, proby]
    return[probx, proby]

def rep(x, y, xr, yr, k, N, i):
    prob1 = prob(x, y, k, N, i)
    prob2 = prob(xr, yr, k, N, i, twoD = False)
    return np.array([-math.log2(prob1[0]), -math.log2(prob1[1]), -math.log2(prob1[2]), -math.log2(prob2[0]), -math.log2(prob2[1])])