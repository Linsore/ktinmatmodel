import matrixre
import matrix
import time
import multiproccesmatrix

summa = 0
summc = 0
summb = 0
print('[x*y] x [y*m] = [x*m] x = 1000 y =2000 m = 1500')
for i in range(10):
    start = time.time()
    matrixre.mult()
    end = time.time()
    py_time = end - start
    summa += py_time

print("Python time = {}".format(summa/10))
for i in range(10):
    start = time.time()
    multiproccesmatrix.matrix_multiply()
    end = time.time()
    mu_time = end - start
    summc += mu_time

print("Multiprocessing time = {}".format(summc/10))

for i in range(10):
    start = time.time()
    matrix.matrix_multiply()
    end = time.time()
    cy_time = end - start
    summb += cy_time
print("Cython time = {}".format(summb/10))
