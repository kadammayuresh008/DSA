def bubble_sort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[i]):
                arr[j],arr[i]=arr[i],arr[j]
arr=[1,4,2,5,3,7,6,8]
bubble_sort(arr)
print(arr)