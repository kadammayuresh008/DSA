
# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if(i<j):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]   
        for j in range(len(matrix[0])-2,-1,-1):
            for i in range(0,len(matrix)):
                if(i==0):
                    m1=matrix[i][j]+matrix[i][j+1]
                    m2=matrix[i][j]+matrix[i+1][j+1]
                    matrix[i][j]=min(m1,m2)
                elif(i==len(matrix)-1):
                    m1=matrix[i][j]+matrix[i][j+1]
                    m2=matrix[i][j]+matrix[i-1][j+1]
                    matrix[i][j]=min(m1,m2)
                else:
                    m1=matrix[i][j]+matrix[i][j+1]
                    m2=matrix[i][j]+matrix[i+1][j+1]
                    m3=matrix[i][j]+matrix[i-1][j+1]
                    matrix[i][j]=min(m1,m2,m3)
        min_dis=9999999999999
        for j in range(0,len(matrix)):
            if(matrix[j][0]<min_dis):
                min_dis=matrix[j][0]
            else:
                continue
        return min_dis
        