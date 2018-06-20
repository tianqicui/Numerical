#Exercise 4.3
#a)
import numpy as np
def f(x):
    return x*(x-1)
delta = 1e-2
x = 1
diff = (f(x+delta)-f(x))/delta
print(delta,diff)

#b)
import numpy as np
def f(x):
    return x*(x-1)
delta = np.array([1e-4,1e-6,1e-8,1e-10,1e-12,1e-14])
x = 1
diff = (f(x+delta)-f(x))/delta
print(delta,diff)