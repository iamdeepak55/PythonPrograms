from functools import reduce
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i=0

def greet():
    global i
    i+=1
    print("Hi",i)
    if i+4<sys.getrecursionlimit():
           greet()
greet()

p=lambda a,b:a**b

print(p(5,3))
l=[2,3,4,5,6,7,8,9]
even=list(filter(lambda a:a%2==0,l))
print(even)
double=list(map(lambda n:n*2,even))
print(double)
sum=reduce(lambda a,b:a+b,double)
print(sum)
l1=[0 for i in range(0,10)]
l2=[0]*10
print(l2)
print(l1)