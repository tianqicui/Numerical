#Exercise 6.1
#a)
# With Ohm’s law and the Kirchhoff current law, we have
# (V1-V2)/R+(V1-V3)/R+(V1-V4)/R+(V1-V+)/R=0
# (V2-V1)/R+(V2-V4)/R+(V2-0)/R=0
# (V3-V1)/R+(V3-V4)/R+(V3-V+)/R=0
# (V4-V1)/R+(V4-V2)/R+(V4-V3)/R+(V4-0)/R=0
# or equivalently
# 4V1-V2-V3-V4=V+
# -V1+3V2-V4=0
# -V1+3V3-V4=V+
# -V1-V2-V3+4V4=0

#b)
from numpy import array,empty

A = array([[ 4, -1, -1, -1 ],
           [ -1, 3, 0, -1 ],
           [ -1, 0, 3, -1 ],
           [ -1, -1, -1, 4 ]], float)
v = array([ 5, 0, 5, 0 ],float)
N = len(v)

# Gaussian elimination
for m in range(N):

    # Divide by the diagonal element
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div

    # Now subtract from the lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

# Backsubstitution
x = empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]

print(x)

# By this method we could find that x =  [ 3.          1.66666667  3.33333333  2.        ],
# which means thar V1=3V, V2=(5/3)V, V3=(10/3)V, V4=2V.