import numpy


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        # print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


@benchmark
def mult():
    a = numpy.random.random((1500, 2000))
    b = numpy.random.random((2000, 1500))
    c = numpy.dot(a, b)
    return c


mult()
