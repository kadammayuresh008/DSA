# https://leetcode.com/problems/min-cost-climbing-stairs/


# Partially solving case:
# Solution 1

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sum1=0
        i=len(cost)
        while(i>1):
            x=min(cost[i-1],cost[i-2])
            sum1+=x
            if(x==cost[i-1] and x!=cost[i-2]):
                i-=1
            elif(x!=cost[i-1] and x==cost[i-2]):
                i-=2
            else:
                i-=2
        sum2=0
        j=-1
        while(j<len(cost)-2):
            x=min(cost[j+1],cost[j+2])
            sum2+=x
            if(x==cost[j+1] and x!=cost[j+2]):
                j+=1
            elif(x!=cost[j+1] and x==cost[j+2]):
                j+=2
            else:
                j+=2
        return min(sum1,sum2)
                
        

# Solution 2: Dynamic Programming



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*len(cost)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(dp)):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])
        





