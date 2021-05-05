# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer1=0
        for pointer2 in range(pointer1+1,len(nums)):
            if(nums[pointer1]!=nums[pointer2]):
                pointer1+=1 
                nums[pointer1]=nums[pointer2]
        return pointer1+1