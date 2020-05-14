from numpy import *

a=array([1,2,3,4,5.0,4],int)
a=a+5
b=array([1,2,3,4,5.0,4],int)
c=b.view() #shallow copy
d=b.copy() #deep copy
print(id(d))
print(id(c))
print(id(b))
print(a,a.dtype)
print(sin(a),cos(a),log(a),sqrt(a))
print(sum(a),max(a),min(a),sort(a),unique(a))
print(concatenate([a,b]))
l=linspace(0,20,20)
print(l,l.dtype)
l1=logspace(1,5,5)
print("%.3f"%l1[4])

z=zeros(5,int)
o=ones(8)
print(z,o)