import matrixre
import matrix
import time

number = 10

start = time.time()
matrixre.test(number)
end =  time.time()

py_time = end - start
print("Python time = {}".format(py_time))

start = time.time()
matrix.test(number)
end =  time.time()

cy_time = end - start
print("Cython time = {}".format(cy_time))

print("Speedup = {}".format(py_time / cy_time))