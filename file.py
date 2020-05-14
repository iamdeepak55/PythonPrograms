f=open('Mydata','r')
f1=open('abc','w')
for d in f:
    f1.write(d)
f1.close()
f1=open('abc','r')
print(f1.read())