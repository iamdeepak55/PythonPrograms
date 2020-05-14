def Topten():
    n=1
    while n<=10:
        s=n*n
        yield s
        n+=1
t=Topten()
for i in t:
    print(i)