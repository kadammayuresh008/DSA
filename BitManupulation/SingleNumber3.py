
# https://leetcode.com/problems/single-number-iii/


# Solution 1
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        sum1=0
        for i in range(0,len(nums)):
            sum1^=nums[i]
        for i in range(0,len(nums)):
            ans=sum1^nums[i]
            if(ans in nums):
                return [ans,nums[i]]
            else:
                continue 

# Solution 2

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        sum1=0
        for i in range(0,len(nums)):
            sum1^=nums[i]
        for i in range(0,len(nums)):
            ans=sum1^nums[i]
            if(ans in nums):
                return [ans,nums[i]]
            else:
                continue
        

