# Exercise 10.7
from numpy.random import random

# Definition of function
def f(r):
    if sum(r**2)<=1:
        return 1
    else:
        return 0

# Algorithm of Monte-Carlo method
def MC(N,dim,a,b):
    I = 0
    for i in range(N):
        r = (b-a)*random(dim) + a
        I += g(r)
    return ((b-a)**dim)/N*I

# Number of points
N = 1000000
# Dimension of hypersphere
dim = 10
# Lower and upper bound of hyperrectangles
a, b = -1.0, 1.0
# Calculate the volume of hypersphere
V = MC(N,dim,a,b)
print("The estimated volume of this 10-dimension hypersphere of unit radius is ",V,".")

# We list the result for each run:
# 2.562048
# 2.557952
# 2.525184
# 2.414592
# 2.551808
# Compared with the exact value (pi)**5/120 = 2.550164..., we find that we get good results by using Monte Carlo method.