from numpy import *
a=array([
    [4,5,6,7,5,9],[5,6,7,8,9,2]
])
m=matrix('1,2,3;4,5,6;7,8,9')
m1=matrix('1,2,3;4,5,6;7,8,9')
print(a.ndim,a.dtype,a.shape,a.size)
b=a.flatten()
c=b.reshape(2,2,3)
print(b)
print(c)
print(m)
print(diagonal(m))
print(m.min())
print(m.max())
print(m*m1)