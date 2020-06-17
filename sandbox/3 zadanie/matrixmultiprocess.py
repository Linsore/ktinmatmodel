import numpy as np
from multiprocessing import Process, freeze_support, set_start_method, Pool
import threading
import time
def matmul_partitioned(start, end, A, B, out):
    for i in range(start, end):
        for j in range(B.shape[1]):
            s = 0
            for k in range(A.shape[1]):
                s += A[i, k] * B[k, j]
            out[i, j] = s

n = 100
A = np.random.random((n, n))
B = np.random.random((n, n))
C = np.zeros((n, n))
N = len(A)
'''a = threading.Thread ( target = matmul_partitioned , args =(0 , N //2 , A , B , C ))
b = threading.Thread ( target = matmul_partitioned , args =( N //2 , N , A , B , C ))
start = time.time()
a.start()
b.start()
a.join()
b.join()
end = time.time()
print(start-end)'''
if __name__ == '__main__':
    p = Process(target=matmul_partitioned, args=(0, N//2, A, B, C))
    g = Process(target=matmul_partitioned, args=(N//2, N, A, B, C))
    start = time.time()
    p.start()
    g.start()
    p.join()
    g.join()
    end = time.time()
    print(end-start)
