import math

def max_heapify(A,i):
    left=2*i+1
    right=2*i+2
    if(left<=len(A) and A[left]>A[i]):
        largest=left 
    else:
        largest=i 
    if(right<=len(A) and A[right]>A[i]):
        largest=right
    else:
        largest=i 
    if(largest!=i):
        A[i],A[largest]=A[largest],A[i]
        max_heapify(A,largest)
        
        
def min_heapify(A,i):
    left=2*i+1
    right=2*i+2 
    if(right<=len(A) and A[right]<A[i]):
        smallest=right
    else:
        smallest=i 
    if(left<=len(A) and A[left]<A[i]):
        smallest=left
    else:
        smallest=i 
    if(smallest!=i):
        A[smallest],A[i]=A[i],A[smallest]
        min_heapify(A,smallest)

A=[1,4,6,8,10,12,14]
n=math.floor(len(A)/2)
for i in range(int(n)-1,-1,-1):
    max_heapify(A,i)
print(A)
A=[1,4,6,8,10,12,14]
n=math.floor(len(A)/2)
for i in range(int(n)-1,-1,-1):
    min_heapify(A,i)
print(A)





