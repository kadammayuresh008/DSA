# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:]=nums[k+1:]+nums[0:k+1]