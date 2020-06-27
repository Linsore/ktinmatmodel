import time
from contextlib import contextmanager


class TimeManager:
    def __init__(self):
        self.time = 0

    def __enter__(self):
        self.time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.time = time.time() - self.time
        print("Time in TimeManager object = " + str(self.time))


@contextmanager
def time_manager(timebuffer = []):
    try:
        saved_time = time.time()
        yield saved_time
    finally:
        saved_time = time.time() - saved_time
        #print("Time in time_manager function = " + str(saved_time))
        timebuffer.append(saved_time)