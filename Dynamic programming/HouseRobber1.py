
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[[nums[0]],[0]]
        for i in range(1,len(nums)):
            dp[0].append(dp[1][i-1]+nums[i])
            dp[1].append(max(dp[0][i-1],dp[1][i-1]))
        return max(dp[0][-1],dp[1][-1])