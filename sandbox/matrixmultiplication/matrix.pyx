
import numpy as np
cimport numpy as np
cdef np.ndarray u
cdef np.ndarray v
cdef np.ndarray res
cdef int i, j, k, n, m, p


def matrix_multiply():
    u = np.random.random((1000, 2000))
    v = np.random.random((2000, 1500))
    res = np.zeros((u.shape[0], v.shape[1]))

    m, n = u.shape
    n, p = v.shape
    for i in range(m):
        for j in range(p):
            res[i, j] = 0
            for k in range(n):
                res[i, j] += u[i, k] * v[k, j]
    return res




matrix_multiply()