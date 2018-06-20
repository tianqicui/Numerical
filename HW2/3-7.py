#Exercise 3.7
from numpy import arange
import matplotlib.pyplot as plt
c_real = []
c_imag = []
interval = 1e-4
min = -2
max = -min+interval
N = 1000
for x in arange(min,max,interval):
    for y in arange(min,max,interval):
        c = complex(x,y)
        z = 0
        jud = 0
        for i in range(N):
            if abs(z) > 2:
                jud = 1
                break
            z = z**2+c
        if jud == 0:
            c_real.append(x)
            c_imag.append(y)
scatter(c_real,c_imag,color='k')
xlim(-2,2)
ylim(-2,2)
ax = plt.axes()
ax.set_aspect('equal')
show()