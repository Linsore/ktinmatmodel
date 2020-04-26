import numpy as np
from multiprocessing import Process, freeze_support, set_start_method, Pool


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
def matrix_multiply(u, v, res):
    for l in range(10000):
        m, n = u.shape
        n, p = v.shape
        for i in range(m):
            for j in range(p):
                res[i, j] = 0
                for k in range(n):
                    res[i, j] += u[i, k] * v[k, j]


u = np.random.random((10, 20))
v = np.random.random((20, 5))
res = np.zeros((u.shape[0], v.shape[1]))


if __name__ == '__main__':
    freeze_support()
    set_start_method('spawn')
    f = Process(target=matrix_multiply(u, v, res))
    f.start()

