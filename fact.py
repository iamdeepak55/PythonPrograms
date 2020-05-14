def fact(n):
    if n==0:
        return 1
    else:
        f=1
        for i in range(1,n+1):
            f=f*i
        return f
def fact1(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact1(n-1)
x=5
r=fact(x)
print(r)
res=fact1(x)
print(res)


