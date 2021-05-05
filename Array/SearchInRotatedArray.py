# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        u=len(nums)-1
        while(l<=u):
            mid=l+(u-l)//2
            if(nums[mid]==target):
                return mid
            if(nums[mid]<nums[u]):
                if(nums[mid]<target<=nums[u]):
                    l=mid+1
                else:
                    u=mid-1
            else:
                if(nums[l]<=target<nums[mid]):
                    u=mid-1
                else:
                    l=mid+1
        return -1