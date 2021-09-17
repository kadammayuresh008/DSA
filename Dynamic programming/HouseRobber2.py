# https://leetcode.com/problems/house-robber-ii/submissions/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if(nums==[]):
            return 0
        elif(len(nums)==1):
            return nums[0]
        elif(len(nums)==2):
            return max(nums[0],nums[1])
        elif(len(nums)==3):
            return max(nums[0],nums[1],nums[2])
        else:
            dp=[[nums[0]],[0]]
            for i in range(1,len(nums)):
                dp[0].append(dp[1][i-1]+nums[i])
                dp[1].append(max(dp[0][i-1],dp[1][i-1]))
            sum1=dp[1][-1]
            nums=nums[::-1]
            dp1=[[nums[0]],[0]]
            for i in range(1,len(nums)):
                dp1[0].append(dp1[1][i-1]+nums[i])
                dp1[1].append(max(dp1[0][i-1],dp1[1][i-1]))
            return max(dp[1][-1],dp1[1][-1])
        