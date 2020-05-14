def toString(list):
    return ''.join(list)

def Permut(a,l,r):
    if(l==r):
        print(toString(a))
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            Permut(a,l+1,r)
            a[l],a[i]=a[i],a[l]
if __name__=="__main__":
    s=list(input())
    r=len(s)-1
    Permut(s,0,r)