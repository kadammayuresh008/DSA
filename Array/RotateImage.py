# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                if(i<j):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(0,len(matrix)):
            matrix[i]=matrix[i][::-1]
        return matrix