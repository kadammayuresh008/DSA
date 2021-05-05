# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr=[]
        for i in range(0,m):
            arr.append([0]*n)
        for i in range(0,m):
            for j in range(0,n):
                if(i==0 or j==0):
                    arr[i][j]=1
                else:
                    arr[i][j]=arr[i][j-1]+arr[i-1][j]
        return arr[-1][-1]
                    