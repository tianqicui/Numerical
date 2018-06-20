#Exercise 4.2
#a)
from math import sqrt
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
delta = b*b-4*a*c
if delta < 0:
    print("No real number solutions")
else:
    x1=(-b+sqrt(delta))/(2*a)
    x2=(-b-sqrt(delta))/(2*a)
    print(x1,x2)

#b)
from math import sqrt
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
delta = b*b-4*a*c
if delta < 0:
    print("No real number solutions")
else:
    x1=2*c/(-b-sqrt(delta))
    x2=2*c/(-b+sqrt(delta))
    print(x1,x2)

#c)
from math import sqrt
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
delta = b*b-4*a*c
if delta < 0:
    print("No real number solutions")
else:
    if b > 0:
        x1=(-b-sqrt(delta))/(2*a)
        x2=2*c/(-b-sqrt(delta))
    else:
        x1=(-b+sqrt(delta))/(2*a)
        x2=2*c/(-b+sqrt(delta))
    print(x1,x2)