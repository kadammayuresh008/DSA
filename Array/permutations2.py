# https://leetcode.com/problems/permutations-ii/

from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        x=permutations(nums)
        ans=[]
        for i in list(x):
            y=list(i)
            if(y not in ans):
                ans.append(y)
            else:
                continue
        return ans