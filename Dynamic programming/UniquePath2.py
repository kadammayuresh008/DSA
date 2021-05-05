


# https://leetcode.com/problems/unique-paths-ii/


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if(obstacleGrid[0][0]==1):
            return 0
        else:
            i=len(obstacleGrid)
            j=len(obstacleGrid[0])
            arr=[]
            for m in range(0,i):
                arr.append([0]*j)
            for m in range(0,i):
                for n in range(0,j):
                    if(m==0 and n==0):
                        arr[m][n]=1
                    elif(m==0 and n!=0):
                        if(obstacleGrid[m][n]==1):
                            arr[m][n]=0
                        else:
                            arr[m][n]=arr[m][n-1]
                    elif(m!=0 and n==0):
                        if(obstacleGrid[m][n]==1):
                            arr[m][n]=0
                        else:
                            arr[m][n]=arr[m-1][n]
                    else:
                        if(obstacleGrid[m][n]==1):
                            arr[m][n]=0
                        else:
                            arr[m][n]=arr[m-1][n]+arr[m][n-1]
            return arr[-1][-1]
                
        