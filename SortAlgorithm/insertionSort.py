def insertion_sort(arr):
    for i in range(0,len(arr)):
        pos=i
        temp=arr[i]
        j=i
        while(j>0 and temp<arr[j-1]):
            arr[j]=arr[j-1]
            pos=j-1
            j-=1
        if(pos!=i):
            arr[pos],temp=temp,arr[pos]
        
    
arr=[1,4,2,5,3,7,6,8]
insertion_sort(arr)
print(arr)