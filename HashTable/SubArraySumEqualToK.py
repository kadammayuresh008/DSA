

# https://leetcode.com/problems/subarray-sum-equals-k/


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        sum1=0
        dict1={0:1}
        for i in nums:
            sum1+=i
            if(sum1-k in dict1):
                count+=dict1[sum1-k]
            if(sum1 in dict1):
                dict1[sum1]+=1
            else:
                dict1[sum1]=1
        return count
        