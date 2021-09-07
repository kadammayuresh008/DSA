
# https://leetcode.com/problems/array-nesting/

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max1=0
        for i in range(0,len(nums)):
            ans=nums[i]
            count=0
            while(nums[ans]!=-1):
                x=nums[ans]
                nums[ans]=-1
                ans=x
                count+=1
            if(count>max1):
                max1=count
        return max1