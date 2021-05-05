# https://leetcode.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax=1
        currMin=1
        res=max(nums)
        for i in nums:
            if(i==0):
                currMax=1
                currMin=1
                continue
            temp=currMax*i
            currMax=max(currMax*i,currMin*i,i)
            currMin=min(temp,currMin*i,i)
            res=max(res,currMax)
        return res