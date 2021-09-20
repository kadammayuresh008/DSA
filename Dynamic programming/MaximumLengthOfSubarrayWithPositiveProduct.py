
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

# Solution1
# Solved 110/112 test cases

class Solution:
    def getMaxLen(self, ans: List[int]) -> int:
        if(0 in ans):
            num=[]
            li=[]
            for i in ans:
                if(i==0):
                    num.append(li)
                    li=[]
                else:
                    li.append(i)
            num.append(li)
        else:
            num=[ans]
        max2=0
        for nums in num:
            dp=[[0 for i in range(0,len(nums))] for j in range(0,len(nums))]
            max1=0
            for i in range(0,len(dp)):
                for j in range(0,len(dp[0])):
                    if(i<j):
                        continue
                    elif(i==j):
                        dp[i][j]=nums[i]
                    else:
                        dp[i][j]=dp[i-1][j]*nums[i]
                    if(dp[i][j]>0):
                        ans=abs(i-j+1)
                        if(ans>max1):
                            max1=ans
            if(max1>max2):
                max2=max1
        return max2



# Solution 2:(Efficient Solution)


