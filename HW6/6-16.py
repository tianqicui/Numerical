#Exercise 6.16
#a)
# We use M, m and s to stand for masses of the earth, the moon, and the satelite, respectively.
# We use R and r to stand for distances from the center of the earth to the center of the moon and the satelite, respectively.
# We also use w stand for common angular velocity of the moon and the satelite.
# Consider the forces acted on the satelite.
# There is a gravitational force between the earth and the satelite, with the direction to the earth.
# There is also a gravitational force between the moon and the satelite, with the direction opposite to the earth.
# Sum of the two forces is the cause of centripetal force that keeps the satellite in its orbit.
# So we have GMs/(r^2)-Gms/((R-r))^2)=s(w^2)r
# Or equivalently, GM/(r^2)-Gm/((R-r))^2)=(w^2)r

#b)
# Input the parameters
G = 6.674e-11
m = 5.974e24
M = 7.348e22
R = 3.844e8
w = 2.662e-6

# Define the function of r and its derivative
def f(r):
    return G*M/(r**2)-G*m/((R-r)**2)-(w**2)*r

def fprime(r):
    return -2*G*M/(r**3)+2*G*m/((R-r)**3)-w**2

# Algorithms of Newton's method
def Newton(r,acc):
    while True:
        delta = f(r)/fprime(r)
        r -= delta
        if abs(delta) < acc:
            break
    return r

# Solve for the location of satelite
acc = 1e5
r = 0.5*R
sol =  Newton(r,acc)
print ("The distance from the earth to the L1 point is around:", sol, "m")

# By Newton's method, we could calulate that the distance from the earth to the L1 point is around 384328852.39479876 m.
# We find that this value 3.843e8 m is very close to the distance from the center of the earth to the center of the moon R = 3.844e8 m.