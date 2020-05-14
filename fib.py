def fib(n):
    if n<0:
        return "invalid input"
    elif n==1:
        return  0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def fibo(n):
    a=0
    b=1
    if n<0:
        print("invalid input")
    elif n==1:
        print(a,end=" ")
    else:
        print(a,b,end=" ")
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=" ")


x=int(input())
print(fib(x))
fibo(x)
