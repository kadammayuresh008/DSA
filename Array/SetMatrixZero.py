# https://leetcode.com/problems/set-matrix-zeroes/


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=set()
        cols=set()
        m=len(matrix)
        n=len(matrix[0])
        for i in range(0,m):
            for j in range(0,n):
                if(matrix[i][j]==0):
                    rows.add(i)
                    cols.add(j)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if(i in rows or j in cols):
                    matrix[i][j]=0
                else:
                    continue
        return matrix
        