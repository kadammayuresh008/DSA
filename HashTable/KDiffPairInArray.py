# https://leetcode.com/problems/k-diff-pairs-in-an-array/


# # Solution 1 (52 of 60 test cases passed)
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         dict1={}
#         for i in range(0,len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if(abs(nums[i]-nums[j])==k):
#                     try:
#                         dict1[(nums[i],nums[j])]+=1
#                     except:
#                         dict1[(nums[i],nums[j])]=1
#         return len(dict1)



# # Solution 2(60 of 60 test cases passed)
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         if(k<0):
#             return 0
#         dict1={i:nums.count(i) for i in nums}
#         ans=0
#         for i in dict1:
#             if(k==0):
#                 if(dict1[i]>=2):
#                     ans+=1
#             else:
#                 if(i+k in dict1):
#                     ans+=1
#                 else:
#                     continue
#         return ans

