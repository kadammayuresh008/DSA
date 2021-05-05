
# https://leetcode.com/problems/top-k-frequent-elements/


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if(k==len(nums)):
            return nums
        else:
            c=Counter(nums)
            return heapq.nlargest(k, c.keys(), key=c.get)