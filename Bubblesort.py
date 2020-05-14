def BubbleSort(arr):
    c=0
    for i in range(len(arr)):
        c=c+1
        for j in range(len(arr)-c):
            if arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr

arr=list(map(int,input().strip().split()))
print(BubbleSort(arr))

