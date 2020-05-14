def Count(l):
    even=0
    odd=0
    for i in l:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=list(map(int,input().strip().split()))
e,o=Count(lst)
print("Even : {} and Odd : {}".format(e,o))
