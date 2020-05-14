def SelectionSort(a):

    for i in range(len(a)):
       minpos=i

       for j in range(i,len(a)):
           if a[j]<a[minpos]:
               minpos=j

       temp=a[i]
       a[i]=a[minpos]
       a[minpos]=temp
    return a

arr=list(map(int,input().strip().split()))
print(SelectionSort(arr))





