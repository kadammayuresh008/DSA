# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(i==0 and j==0):
                    continue
                elif(i==0 and j!=0):
                    grid[i][j]=grid[i][j]+grid[i][j-1]
                elif(j==0 and i!=0):
                    grid[i][j]=grid[i][j]+grid[i-1][j]
                else:
                    grid[i][j]=grid[i][j]+min(grid[i][j-1],grid[i-1][j])
        return grid[-1][-1]