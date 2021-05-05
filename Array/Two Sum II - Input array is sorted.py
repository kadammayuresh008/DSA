# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(0,len(numbers)):
            if(target-numbers[i] in dict1):
                return [dict1[target-numbers[i]],i+1]
            else:
                dict1[numbers[i]]=i+1
        return -1
        