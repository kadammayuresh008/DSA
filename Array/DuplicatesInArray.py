# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans={}
        b=[]
        for i in range(0,len(nums)):
            if(nums[i] not in ans):
                ans[nums[i]]=1
            else:
                b.append(nums[i])
        return b