# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/



class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(0,len(nums)):
            nums[i]=[int(nums[i]),nums[i]]
        nums.sort(key=lambda x:x[0],reverse=True)
        return nums[k-1][1]
            