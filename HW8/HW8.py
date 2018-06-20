# Session 8 In-class Activity 
from numpy import array,linspace
from scipy.optimize import leastsq

# Import data of P/yr, a/AU and occurence from reference
P = array([100/365,1,2.8,5.2,11.2])
a = array([0.42,1,2,3,5])
Occ = array([0.8625,1.95,3.95,4.6,7.25])

# Define linear fitting function
def model(x,coeffs):
    return coeffs[0] + coeffs[1] * x

# Define function of residuals
def residuals(coeffs,y,x):
    return y - model(x, coeffs)

# Make an initial guess
coeffs = array([1, 1])

# Do linear fitting of occurence vs P, and occurence vs a, respectively
coeffs1,flag = leastsq(residuals, coeffs, args=(Occ, P))
coeffs2,flag = leastsq(residuals, coeffs, args=(Occ, a))

# Inout points need to be interpolated
P0 = array([50/365,200/365,500/365,3000/365,4300/365])
a0 = P0**(2/3)
print(a0)

# Calculate occurence in two linear models
Occ1 = coeffs1[0] + coeffs1[1] * P0
Occ2 = coeffs2[0] + coeffs2[1] * a0
print(Occ1,Occ2)

#a)
# The occurance of giant planets is 1.57, 1.79, 2.24, 5.96, 7.90, respectively.

#b)
# The semimajor axes that correspond to the orbital periods are 0.26AU, 0.67AU, 1.23AU, 4.07AU, 5.18AU, respectively.

#c)
# The occurance of giant planets is 0.99, 1.53, 2.30, 6.15, 7.65, respectively.

#d)
# The answers to (a) and (c) do not agree with each other. As the relationship between P and A is nonlinear(A=P^(2/3)).
# which indicates that a linear model of occurance and P is nonlinear of occurance and a, vice visa.
# So we coud conclude that when use interpolation methods, two models will generate different results.

#e)
# The cumulative percentage of the Sun is 7.90 (by model in part a)) or 7.65 (by model in part c)).

#f)
# The solar system is not special. Kepler's Third Law is also available for other star systems.