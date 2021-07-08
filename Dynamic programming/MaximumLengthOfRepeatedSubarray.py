# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0 for i in range(len(nums1)+1)] for j in range(len(nums2)+1)]
        for i in range(0,len(nums2)):
            for j in range(0,len(nums1)):
                if(nums2[i]==nums1[j]):
                    dp[i+1][j+1]=1+dp[i][j]
        return max(max(row) for row in dp)
        