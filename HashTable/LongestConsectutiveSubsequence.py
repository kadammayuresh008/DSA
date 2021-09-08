
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        max_length=0
        for i in nums:
            if(i-1 not in set1):
                length=0
                while(i+length in set1):
                    length+=1
                max_length=max(length,max_length)
            else:
                continue
        return max_length
        