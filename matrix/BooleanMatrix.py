# # Solution 1 (dfs)
# #User function Template for python3


# #Function to modify the matrix such that if a matrix cell matrix[i][j]
# #is 1 then all the cells in its ith row and jth column will become 1.

# def dfs(temp,i,j,m,n,prev):
#     if(i<0 or j<0 or j>=n or i>=m):
#         return 
#     if(prev==-1):
#         dfs(temp,i+1,j,m,n,"D")
#         dfs(temp,i,j+1,m,n,"R")
#         dfs(temp,i-1,j,m,n,"U")
#         dfs(temp,i,j-1,m,n,"L")
#     temp[i][j]=1
#     if(prev=="D"):
#         dfs(temp,i+1,j,m,n,"D")
#     if(prev=="R"):
#         dfs(temp,i,j+1,m,n,"R")
#     if(prev=="U"):
#         dfs(temp,i-1,j,m,n,"U")
#     if(prev=="L"):
#         dfs(temp,i,j-1,m,n,"L")
        
    
    
# def booleanMatrix(matrix):
#     # code here 
#     m,n=len(matrix),len(matrix[0])
#     temp=[[0 for i in range(0,n)]for j in range(0,m)]
#     for i in range(0,m):
#         for j in range(0,n):
#             if(matrix[i][j]==1):
#                 temp[i][j]=1
#     for i in range(0,m):
#         for j in range(0,n):
#             if(matrix[i][j]==1):
#                 dfs(temp,i,j,m,n,-1)
#     for i in range(0,m):
#         for j in range(0,n):
#             matrix[i][j]=temp[i][j]
    

# #{ 
# #  Driver Code Starts
# #Initial Template for Python 3

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         r,c = map(int, input().strip().split())
#         matrix = []
#         for i in range(r):
#             line = [int(x) for x in input().strip().split()]
#             matrix.append(line)
#         booleanMatrix(matrix)
#         for i in range(r):
#             for j in range(c):
#                 print(matrix[i][j], end=' ')
#             print()


# # } Driver Code Ends



# # Solution 2 using set


# def booleanMatrix(li):
#     xco=set()
#     yco=set()
#     for k in range(0,len(li)):
#         for j in range(0,len(li[k])):
#             if(li[k][j]==1):
#                 xco.add(k)
#                 yco.add(j)
#     for k in range(0,len(li)):
#         for j in range(0,len(li[k])):
#             if(k in xco or j in yco):
#                 li[k][j]=1


