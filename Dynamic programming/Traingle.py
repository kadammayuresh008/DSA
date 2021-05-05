
# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        sumtri=[]
        for i in range(1,len(triangle)+1):
            sumtri.append([0]*i)
        for i in range(0,len(sumtri)):
            if(i==0):
                sumtri[i][0]=triangle[i][0]
            else:
                for j in range(0,len(sumtri[i])):
                    if(j==0):
                        sumtri[i][j]=triangle[i][j]+sumtri[i-1][j]
                    elif(j==len(sumtri[i])-1):
                        sumtri[i][j]=triangle[i][j]+sumtri[i-1][j-1]
                    else:
                        sumtri[i][j]=min(triangle[i][j]+sumtri[i-1][j-1],triangle[i][j]+sumtri[i-1][j])
        return (min(sumtri[-1]))
            