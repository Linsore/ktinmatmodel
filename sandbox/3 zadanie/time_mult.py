import numpy as np
import matrix
import CythonMatrix
import MAtrixnumpy
import time
import opencl
import matplotlib.pyplot as plt
import tm
import mp
from multiprocessing import freeze_support

def multiply(n):
    g = 5
    summb = 0
    summa = 0
    summc = 0
    summd = 0
    summr = 0
    A = np.random.random((n, n))
    B = np.random.random((n, n))
    out = np.zeros((n, n))

    for i in range(g):
        '''
        timemultiprocessing = []
        with tm.time_manager(timemultiprocessing):
            if __name__ == '__main__':
                freeze_support()
                her.multiproc(A, B)
        summr += sum(timemultiprocessing)/len(timemultiprocessing)
        '''
        start = time.time()
        CythonMatrix.matmul(A, B, out)
        end = time.time()
        cy_time = end - start
        summb += cy_time

        start1 = time.time()
        matrix.matmul(A, B, out)
        end1 = time.time()
        py_time = end1 - start1
        summa += py_time

        start2 = time.time()
        MAtrixnumpy.mult(A,B,out)
        end2 = time.time()
        nump_time = end2 - start2
        summc += nump_time

        start3 = time.time()
        opencl.mult(A, B, out)
        end3 = time.time()
        cl_time = end3 - start3
        summd += cl_time

    return (summa/g, summd/g, summc/g, summb/g, summr/g)


py = list()
OCL = list()
nup = list()
Cy = list()
OCL1 = list()
nup1 = list()
Cy1 = list()
t = list()
mpr = list()
n = 0
for ind in range(4):
    n += 50
    k = multiply(n)
    t.append(n)
    py.append(k[0])
    OCL.append(k[1])
    nup.append(k[2])
    Cy.append(k[3])
    #mpr.append(k[4])
    OCL1.append(k[0]/k[1])
    #nup1.append(k[0]/k[2])
    Cy1.append(k[0]/k[3])
fig, ax = plt.subplots()
ax.plot(t, py, color='green')
ax.plot(t, OCL, color='blue' )
ax.plot(t, nup, color='red')
ax.plot(t, Cy, color='yellow')
#ax.plot(t, mpr, color='purple')

ax.set(xlabel='N', ylabel='время в секундах')
ax.grid()

fig1, ax1 = plt.subplots()
ax1.plot(t, OCL1, color='blue')
#ax1.plot(t, nup1, color='red')
ax1.plot(t, Cy1, color='yellow')
ax1.set(xlabel='N', ylabel='Ускорение в Н раз')
ax1.grid()
fig.savefig("GRaphics.png")
fig1.savefig("Uluchsenie")
plt.show()
