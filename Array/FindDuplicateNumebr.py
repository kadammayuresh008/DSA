# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict1={}
        for i in range(0,len(nums)):
            if(nums[i] in dict1):
                return nums[i]
            else:
                dict1[nums[i]]=i