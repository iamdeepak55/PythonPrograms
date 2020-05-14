pos=-1
def BinSearch(list,n):
    u=len(list)-1
    l=0
    while l<=u:
        mid = (u + l) // 2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
list=[4,7,9,55,77,88,152]
n=1
if BinSearch(list,n):
    print("Found at",pos+1)
else:
    print("Not Found")




