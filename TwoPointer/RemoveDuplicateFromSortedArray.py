
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if(n<3):
            return n
        else:
            s,f=2,2
            while(f<n):
                if(nums[s-2]!=nums[f]):
                    nums[s]=nums[f]
                    s+=1
                f+=1
            return s