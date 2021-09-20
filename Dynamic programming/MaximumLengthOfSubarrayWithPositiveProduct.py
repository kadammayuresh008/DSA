
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


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n=len(nums)
        pos=[0]*n
        neg=[0]*n
        
        if nums[0]>0:
            pos[0]=1
        if nums[0]<0:
            neg[0]=1
        res=pos[0]
        for i in range(1,n):
            if(nums[i]>0):
                pos[i]=pos[i-1]+1
                if(neg[i-1]>0):
                    neg[i]=neg[i-1]+1
                else:
                    neg[i]=0
            elif(nums[i]<0):
                if(neg[i-1]>0):
                    pos[i]=neg[i-1]+1
                else:
                    pos[i]=0
                neg[i]=pos[i-1]+1
            res=max(res,pos[i])
        return res