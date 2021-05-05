# https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=99999999999
        right=0
        sum1=0
        for i in range(0,len(nums)):
            sum1+=nums[i]
            while(sum1>=target):
                ans=min(ans,i+1-right)
                sum1-=nums[right]
                right+=1
        if(ans==99999999999):
            return 0
        else:
            return ans