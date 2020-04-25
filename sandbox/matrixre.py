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
def mult(mode):
    if mode == 1:
        for i in range(1000):
            a = numpy.array([numpy.random.randint(10000, 100000), numpy.random.randint(10000, 100000)])
            b = numpy.array([[numpy.random.randint(10000, 100000),
                              numpy.random.randint(10000, 100000),
                              numpy.random.randint(10000, 100000)],
                             [numpy.random.randint(10000, 100000),
                              numpy.random.randint(10000, 100000),
                              numpy.random.randint(10000, 100000)]])
            c = numpy.dot(a, b)
    return c

    # if mode == 'multiprocessing':
    #  def f(xy, yx):
    #    c = numpy.dot(xy, yx)
    #     return c
    # lock = Lock()
    # p = Process(target=f, args=(lock, x, y))
    # p.start()


mult(1)

# print(mult(a, b, 'sequential'))
