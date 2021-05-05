
# https://leetcode.com/problems/gas-station/


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas)<sum(cost)): 
            return -1
        else:
            diff=[gas[i]-cost[i] for i in range(0,len(gas))]
            ans=0
            start=0
            for i in range(0,len(diff)):
                ans+=diff[i]
                if(diff[i]>ans):
                    start=i
                    ans=diff[i]
            return start