import numpy
import array


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
def mult(x, y, mode):
    from multiprocessing import Process, Lock

    if mode == 'sequential':
        c = numpy.dot(x, y)
        return c

    # if mode == 'multiprocessing':
    #  def f(xy, yx):
    #    c = numpy.dot(xy, yx)
    #     return c
    # lock = Lock()
    # p = Process(target=f, args=(lock, x, y))
    # p.start()

    if mode == 'cython': # не совсем понятно тут перемножение рандомных матриц
        def matrix_multiply(u, v, res):
            m, n = u.shape
            n, p = v.shape
            for i in range(m):
                for j in range(p):
                    res[i, j] = 0
                    for k in range(n):
                        res[i, j] += u[i, k] * v[k, j]
            return res

        u = numpy.random.random((10, 20))
        v = numpy.random.random((20, 5))
        res = numpy.zeros((u.shape[0], v.shape[1]))
        return matrix_multiply(u, v, res)


a = numpy.array([10000, 20000])
b = numpy.array([[10000, 10000, 10000], [100000, 1000000, 1000000]])

mult(a, b, 'sequential')
mult(a, b, 'cython')
# print(mult(a, b, 'sequential'))
