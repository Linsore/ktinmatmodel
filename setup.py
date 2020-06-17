import numpy as np
import matrix
import CythonMatrix
import MAtrixnumpy
import time
n = 100
summb = 0
summa = 0
summc = 0
A = np.random.random((n, n))
B = np.random.random((n, n))
out = np.zeros((n, n))
for i in range(1):
    start = time.time()
    CythonMatrix.matmul(A, B, out)
    end = time.time()
    cy_time = end - start
    summb += cy_time
print("Cython time = {}".format(summb))
for i in range(1):
    start = time.time()
    matrix.matmul(A, B, out)
    end = time.time()
    py_time = end - start
    summa += py_time
print("Python time = {}".format(summa))
for i in range(1):
    start = time.time()
    MAtrixnumpy.mult(A,B,out)
    end = time.time()
    py_time = end - start
    summc += py_time

print("Numpy time = {}".format(summc))
