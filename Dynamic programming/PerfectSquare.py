# https://leetcode.com/problems/perfect-squares/



# # Solution 1 (Recursive Approach) (128/588 test case passed)
# class Solution:
#     def __init__(self):
#         self.min1=10000000
#     def generate(self,li,arr,curr,sum1,n,i):
#         if(i==n):
#             if(curr==sum1):
#                 if(len(li)<self.min1):
#                     self.min1=len(li)
#             return 
#         if(curr>sum1):
#             return 
#         Solution.generate(self,li+[arr[i]],arr,curr+arr[i],sum1,n,i)
#         Solution.generate(self,li,arr,curr,sum1,n,i+1)
#     def numSquares(self, n: int) -> int:
#         li=[]
#         i=1
#         while(i*i<=n):
#             li.append(i*i)
#             i+=1
#         Solution.generate(self,[],li,0,n,len(li),0)
#         return self.min1



# Solution 2 (Dynamic Programming)(518/588 test case passed)
# class Solution:    
#     def numSquares(self, n: int) -> int:
#         li=[]
#         i=1
#         while(i*i<=n):
#             li.append(i*i)
#             i+=1
#         dp=[[0 for i in range(0,n+1)] for j in range(0,len(li)+1)]
#         for i in range(0,len(dp[0])):
#             dp[1][i]=i
#         for i in range(2,len(dp)):
#             for j in range(0,len(dp[0])):
#                 if(j<li[i-1]):
#                     continue
#                 else:
#                     temp=int(math.floor(math.sqrt(j-li[i-1])))
#                     dp[i][j]=dp[min(i,temp)][j-li[i-1]]+1
#         min1=1000001
#         for i in range(1,len(dp)):
#             if(dp[i][-1]<min1):
#                 min1=dp[i][-1]
#             else:
#                 continue
#         return min1

