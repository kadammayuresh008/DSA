# https://leetcode.com/problems/longest-consecutive-sequence/


# o(nlogn) Solution


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(nums!=[]):
            nums.sort()
            max1=1
            count=1
            for i in range(0,len(nums)-1):
                if(nums[i+1]==nums[i]+1):
                    count+=1
                elif(nums[i+1]==nums[i]):
                    continue
                else:
                    count=1
                if(count>max1):
                    max1=count
            return max1
        return 0
            


