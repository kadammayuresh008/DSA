
# https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:
    def check(str1):
        ans1=0
        ans2=0
        for j in range(0,len(str1)):
            if(str1[j]=='0'):
                ans1+=0
                ans2+=pow(2,len(str1)-1-j)
            else:
                ans2+=0
                ans1+=pow(2,len(str1)-1-j)
        if(ans1>=ans2):
            return False
        else:
            return True
        
    def check_one(str1):
        ans1=0
        ans2=0
        for j in range(0,len(str1)):
            if(str1[j]=='1'):
                ans1+=1
            else:
                ans2+=1
        if(ans1>=ans2):
            return False
        else:
            return True
        
        
    def calculate(str1):
        ans1=0
        for j in range(0,len(str1)):
            if(str1[j]=='0'):
                ans1+=0
            else:
                ans1+=pow(2,len(str1)-1-j)
        return ans1
        
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(0,len(grid)):
            str1=""
            for j in range(0,len(grid[0])):
                str1+=str(grid[i][j])
            x=Solution.check(str1)
            if(x==True):
                for j in range(0,len(grid[0])):
                    if(grid[i][j]==1):
                        grid[i][j]=0
                    else:
                        grid[i][j]=1
        for i in range(0,len(grid[0])):
            str1=""
            for j in range(0,len(grid)):
                str1+=str(grid[j][i])
            x=Solution.check_one(str1)
            if(x==True):
                for j in range(0,len(grid)):
                    if(grid[j][i]==1):
                        grid[j][i]=0
                    else:
                        grid[j][i]=1
        sum1=0
        for i in range(0,len(grid)):
            str1=""
            for j in range(0,len(grid[0])):
                str1+=str(grid[i][j])
            sum1+=Solution.calculate(str1)
        return sum1
            
                
                
        