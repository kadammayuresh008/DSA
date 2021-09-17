
# https://leetcode.com/problems/single-number-ii/

# Solution1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1={}
        for i in range(0,len(nums)):
            if(nums[i] not in dict1):
                dict1[nums[i]]=1
            else:
                dict1[nums[i]]+=1
        for j in dict1:
            if(dict1[j]==1):
                return j

# solution 2



                