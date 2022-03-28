
def countNumberofInlands(matrix,i,j):
    global visited
    if(i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]=="1" or visited[i][j]==1):
        return
    visited[i][j]=1
    countNumberofInlands(matrix,i+1,j)
    countNumberofInlands(matrix,i-1,j)
    countNumberofInlands(matrix,i,j+1)
    countNumberofInlands(matrix,i,j-1)


matrix=[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
visited=[[0 for i in range(0,len(matrix[0]))] for j in range(0,len(matrix))]
count=0
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        if(matrix[i][j]=="0" and visited[i][j]==0):
            countNumberofInlands(matrix,0,j)
            count+=1 
        else:
            continue 
print("The number of Islands are:",count)






