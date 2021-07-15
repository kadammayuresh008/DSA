# https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        i=2
        nums.sort()
        if(len(nums)<3):
            return 0
        count=0
        while(i<len(nums)):
            R=i-1
            L=0
            while(L<R):
                if(nums[L]+nums[R]>nums[i]):
                    count+=R-L
                    R-=1
                else:
                    L+=1
            i+=1
        return count
            
        