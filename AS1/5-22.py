from cmath import exp
from numpy import pi
from math import factorial

# The function we need to deal with in this problem
def f(z):
    return exp(2*z)

# Amount of the points
N = 10000

# Do the summation according to the formula
for m in range(21):
    fmprime = 0
    for k in range(N):
        # Notice that zk=exp(1j*2*pi*k/N)
        fmprime += f(exp(1j*2*pi*k/N))*exp(-1j*2*pi*k*m/N)*factorial(m)/N
    # Notice that the summation may be a complex caused by inaccurancy, we could use its real part (or absolute value) as it must be real.
    # The accurate values are all integers, and we could use "round" command on our values to compare with them.
    # The 0-th derivative is just the value at z=0 of function f(z) itself.
    print("The calculated value of the",m,"-th derivative of this function is",round(real(fmprime)),", while the accurate value is",2**m,".")