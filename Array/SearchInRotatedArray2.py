# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/



class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        if(target<=nums[len(nums)//2]):
            if(target in nums[0:len(nums)//2]):
                return True
            else:
                return False
        elif(target>nums[len(nums)//2]):
            if(target in nums[len(nums)//2:]):
                return True
            else:
                return False