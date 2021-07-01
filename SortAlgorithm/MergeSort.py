def merge(arr,l,mid,r):
    left=[0]*(mid-l+1)
    right=[0]*(r-mid)
    for i in range(0,mid-l+1):
        left[i]=arr[l+i]
    for j in range(0,r-mid):
        right[j]=arr[mid+1+j]
    i=0
    j=0
    k=l
    while(i<mid-l+1 and j<r-mid):
        if(left[i]<right[j]):
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while(j<r-mid):
        arr[k]=right[j]
        j+=1 
        k+=1 
    while(i<mid-l+1):
        arr[k]=left[i]
        i+=1
        k+=1 
def merge_sort(arr,l,h):
    if(l<h):
        mid=int((l+h)/2)
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,h)
        merge(arr,l,mid,h)
arr=[1,4,2,5,3,7,6,8]
merge_sort(arr,0,len(arr)-1)
print(arr)