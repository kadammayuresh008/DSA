# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

# # Solution 1:(not optimum solution brute force 10/93 test case passed)

# class Solution:
#     def __init__(self):
#         self.min_length=100001
#     def generate(self,arr,i,curr,sum1,n,li):
#         if(i==n):
#             if(curr==sum1):
#                 if(len(li)<self.min_length):
#                     self.min_length=len(li)
#             return 
#         Solution.generate(self,arr,i+1,curr+arr[i],sum1,n,li+[arr[i]])
#         Solution.generate(self,arr,i+1,curr,sum1,n,li)
#     def minOperations(self, nums: List[int], temp: int) -> int:
#         arr=[]
#         while(len(nums)>=2):
#             x=nums.pop(0)
#             y=nums.pop(-1)
#             arr.append(x)
#             arr.append(y)
#         if(nums):
#             arr.append(nums[0])
#         Solution.generate(self,arr,0,0,temp,len(arr),[])
#         if(self.min_length==100001):
#             return -1
#         else:
#             return self.min_length


# Solution 2:()