
# https://leetcode.com/problems/best-sightseeing-pair/


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ret=0
        maxVal=0
        for i in range(0,len(values)):
            ret=max(ret,values[i]+maxVal-i)
            maxVal=max(maxVal,i+values[i])
        return ret