from timeit import default_timer


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
def schet(x):
    z = 2
    while x < 1000000:
        x += 1
        z *= 2


class Timer:

    def __init__(self, timer=default_timer):
        self.timer = default_timer

    def __enter__(self):
        self.start = self.timer()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = self.timer()
        print('Время выполнения:', self.end - self.start)


def test(x):  # функция которая выполняется и мы считаем ее время
    z = 2
    while x < 1000000:
        x += 1
        z *= 2


with Timer():  # на основе класса
    test(1)

context_time = schet(1)
print(context_time)  # на основе декоратора
