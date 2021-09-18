# https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/


# solution 1:
# Greedy Method o(n) solution

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        for j in range(0,len(cost)):
            cost[j]=[cost[j],s[j]]
        i=0
        sum1=0
        while(i<len(cost)-1):
            if(cost[i][1]==cost[i+1][1]):
                x=min(cost[i][0],cost[i+1][0])
                sum1+=x
                if(x==cost[i][0]):
                    cost.pop(i)
                else:
                    cost.pop(i+1)
            else:
                i+=1
        return sum1
            




# solution 2:
# Using Stack(Efficient method)
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        stack=[]
        sum1=0
        for i in range(0,len(s)):
            if(stack==[]):
                stack.append([s[i],cost[i]])
            else:
                x=stack[-1]
                if(x[0]==s[i]):
                    if(x[1]<cost[i]):
                        x=stack.pop(-1)
                        sum1+=x[1]
                        stack.append([s[i],cost[i]])
                    else:
                        sum1+=cost[i]
                else:
                    stack.append([s[i],cost[i]])
        return sum1
            
                
            
        