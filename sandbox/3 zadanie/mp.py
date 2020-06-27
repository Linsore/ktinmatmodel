import numpy as np
from multiprocessing import Pool, freeze_support


def mult(A, B):
    m, n, p = len(A), len(A[0]), len(B[0])
    result = np.zeros((m, p), 'i')
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result


def multiproc(A, B):
    m, p = len(A), len(B[0])
    processnumber = 4
    partnumber = 50
    part = max(1, m // partnumber)
    with Pool(processnumber) as pool:
        result = pool.starmap(mult, [(A[start:min(start + part, m)], B) for start in range(0, m, part)])
    return np.array(result).reshape((m, p))

