# https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count=0
        dict1={}
        for i in nums1:
            for j in nums2:
                x=i+j
                if(x not in dict1):
                    dict1[x]=1
                else:
                    dict1[x]+=1
        for i in nums3:
            for j in nums4:
                x=i+j
                if(-x in dict1):
                    count+=dict1[-x]
                else:
                    continue
        return count