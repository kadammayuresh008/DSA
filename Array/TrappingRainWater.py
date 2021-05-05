# https://leetcode.com/problems/trapping-rain-water/



class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        for i in range(1,len(height)-1):
            left=max(height[0:i+1])
            right=max(height[i:])
            res+=min(left,right)-height[i]
        return res