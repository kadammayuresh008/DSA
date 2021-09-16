


dirs=[[0,-1],[0,1],[1,0],[-1,0]]
matrix=[[1,0,0],[0,1,1],[0,1,1]]
visited=[]

ROWS=len(matrix)
COLS=len(matrix[0])

def isvalid(points):
    if((0<=points[0]<ROWS) and (0<=points[1]<COLS)):
        return True
    else:
        return False
    

def dfs(matrix,start):
    queue=[]
    queue.append(start)
    visited.append(start)
    while(queue):
        x=queue.pop(0)
        print(matrix[x[0]][x[1]])
        for i in dirs:
            a=x[0]+i[0]
            b=x[1]+i[1]
            if([a,b] not in visited and isvalid([a,b])==True and matrix[a][b]==1):
                queue.append([a,b])
                visited.append([a,b])
        
    
    

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        if(matrix[i][j]==1):
            dfs(matrix,[i,j])
            print("**********************************")
        else:
            continue



