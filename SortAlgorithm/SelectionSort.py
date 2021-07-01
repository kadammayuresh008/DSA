def selection_sort(arr):
    for i in range(0,len(arr)-1):
        pos=i 
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[pos]):
                pos=j 
        # pos=arr.index(min(arr[i:]))
        arr[pos],arr[i]=arr[i],arr[pos]
arr=[1,4,2,5,3,7,6,8]
selection_sort(arr)
print(arr)