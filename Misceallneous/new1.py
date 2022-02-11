

# num=int(input())
# dict1=[0 for i in range(0,9)]
# while(num>0):
#     rem=num%10
#     num=num//10
#     dict1[rem]+=1
# count=0
# for i in dict1:
#     if(i%2!=0):
#         count+=1
#     else:
#         continue
# if(count==0 or count==1):
#     str1=""
#     for i in range(0,9):
#         if(dict1[i]%2!=0):
#             str1=str1+str(i)*dict1[i]
#             dict1[i]=0
#         else:
#             continue
#     for i in range(0,9):
#         length=dict1[i]//2
#         str1=str(i)*length+str1+str(i)*length
#     print(str1)
# else:
#     print("Palindrome not found")


# topological sort 

# graph={
#     0:[1,3],
#     1:[2,3],
#     2:[3,4,5],
#     3:[4,5],
#     4:[5],
#     5:[],
# }

# ans=[]
# while(graph):
#     temp=[]
#     for i in graph:
#         if(graph[i]==[]):
#             x=i
#             temp.append(x)
#             ans.append(x)
#     for i in temp:
#         del graph[i]
#         for j in graph:
#             if(x in graph[j]):
#                 graph[j].remove(x)
#             else:
#                 continue
# print(ans[::-1])

# class Node:
 
#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# def height(root):
#     if(root==None):
#         return 0 
#     return 1+max(height(root.left),height(root.right))
    
    
# def diameter(root):
#     if(root==None):
#         return 0 
    
#     lheight=height(root.left)
#     rheight=height(root.right)
    
#     ldiameter=diameter(root.left)
#     rdiameter=diameter(root.right)
    
#     return max(lheight+rheight+1,ldiameter,rdiameter)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# x=height(root)
# y=diameter(root)
# print(x)
# print(y)

def generate(li,n,k,i,arr,temp):
    if(i==n):
        print(arr)
        return 
    if(k==0):
        k=temp
        return 
    generate(li,n,k-1,i,arr+[li[i]],temp)
    generate(li,n,k,i+1,arr,temp)
n=3
m=3
k=2
li=[i+1 for i in range(0,m)]
generate(li,n,k,0,[],k)
print(li)


