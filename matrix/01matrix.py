# https://leetcode.com/problems/01-matrix/

# Solution 1: dfs solution


class Solution:
    dRow = [ 1,0, 0, -1]
    dCol = [ 0,-1, 1, 0]


    def isValid(row, col,ROW,COL,vis):
        if (row < 0 or col < 0 or row >= ROW or col >= COL):
            return False
        if (vis[row][col]):
            return False
        return True

    def DFS(row, col, grid,vis,ROW,COL,dis,ans,count_zero):
        counter=[]
        irow=row 
        icol=col
        st = []
        st.append([row, col])
        while (len(st) > 0):
            curr = st[len(st)-1]
            st.remove(curr)
            row = curr[0]
            col = curr[1]
            if (Solution.isValid(row, col,ROW,COL,vis) == False):
                continue
            vis[row][col] = True
            if(grid[row][col]==0):
                counter.append(abs(irow-row)+abs(icol-col))
                if(len(counter)==count_zero):
                    ans[irow][icol]=min(counter)
                    return 
            for i in range(4):
                adjx = row + Solution.dRow[i]
                adjy = col + Solution.dCol[i]
                st.append([adjx, adjy])
                
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        grid = mat        
        ROW=len(grid)
        COL=len(grid[0])
        count_zero=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j]==0):
                    count_zero+=1
        ans = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==0):
                    continue
                else:
                    vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
                    Solution.DFS(i, j, grid,vis,ROW,COL,0,ans,count_zero)
        return ans
        

# Solution 2 : DP solution



class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans=[[sys.maxsize for i in range(0,len(mat[0]))] for j in range(0,len(mat))]
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                if(mat[i][j]==0):
                    ans[i][j]=0
                else:
                    left=ans[i][j-1] if j>0 else sys.maxsize
                    up=ans[i-1][j] if i>0 else sys.maxsize
                    ans[i][j]=min(left,up)+1
        for i in range(len(mat)-1,-1,-1):
            for j in range(len(mat[0])-1,-1,-1):
                if(mat[i][j]==0):
                    ans[i][j]=0
                else:
                    right=ans[i][j+1] if j<len(mat[0])-1 else sys.maxsize
                    down=ans[i+1][j] if i<len(mat)-1 else sys.maxsize
                    ans[i][j]=min(ans[i][j],right+1,down+1)
        return ans