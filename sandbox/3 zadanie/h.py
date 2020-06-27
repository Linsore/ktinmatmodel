import mp
import numpy as np
import tm
import time
def mu(A,B):
    summr = 0
    timemultiprocessing = []
    with tm.time_manager(timemultiprocessing):
        if __name__ == '__main__':
            C = mp.multiproc(A, B)
    summr = sum(timemultiprocessing)
    return summr