
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, matrix: List[List[int]]) -> int:
        sum1=0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                curr=matrix[i][j]
                if(j>0):   
                    left=matrix[i][j-1]
                else:
                    left=curr
                if(j<len(matrix[i])-1):
                     right=matrix[i][j+1]
                else:
                    right=curr
                if(i>0):
                     up=matrix[i-1][j]
                else:
                    up=curr
                if(i<len(matrix)-1):
                     down=matrix[i+1][j]
                else:
                    down=curr
                # cacluate left
                for k in range(j-1,-1,-1):
                    if(matrix[i][k]>left):
                        left=matrix[i][k]
                # calculate right
                for k in range(j+1,len(matrix[0])):
                    if(matrix[i][k]>right):
                        right=matrix[i][k]
                # calculate up
                for k in range(i-1,-1,-1):
                    if(matrix[k][j]>up):
                        up=matrix[k][j]
                # calculate down
                for k in range(i+1,len(matrix)):
                    if(matrix[k][j]>down):
                        down=matrix[k][j]
                vertical=max(up,down)
                horizontal=max(right,left)
                matrix[i][j]=max(min(vertical,horizontal),curr)
                sum1+=abs(matrix[i][j]-curr)
        return sum1
        