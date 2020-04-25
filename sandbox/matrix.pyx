import numpy as np
cimport numpy as np


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


@benchmark
def cy_dot_product(mode):
    def matrix_multiply(u, v, res):
        m, n = u.shape
        n, p = v.shape
        for i in range(m):
            for j in range(p):
                res[i, j] = 0
                for k in range(n):
                    res[i, j] += u[i, k] * v[k, j]
        return res
    cdef np.ndarray u
    cdef np.ndarray v
    cdef np.ndarray res
    cdef int i, j, k, n, m, p
    u = np.random.random((10, 20))
    v = np.random.random((20, 5))
    res = np.zeros((u.shape[0], v.shape[1]))
    for i in range(1000):
        matrix_multiply(u,v,res)



cy_dot_product(1)