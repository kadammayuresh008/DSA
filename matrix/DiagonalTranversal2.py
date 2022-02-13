# # Solution 1:(52/56 test case passed)
# class Solution:
#     def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
#         ans=[]
#         i=0
#         while(i<len(nums)):
#             start=i
#             j=0
#             while(j<len(nums[0])):
#                 try:
#                     ans.append(nums[start][j])
#                 except:
#                     temp=1
#                 j+=1
#                 if(start==0):
#                     break
#                 start-=1
#             i+=1
#         j=1
#         while(j<len(nums[0])):
#             start=j
#             i=len(nums)-1
#             while(i>=0):
#                 try:
#                     ans.append(nums[i][start])
#                 except:
#                     temp=1
#                 i-=1
#                 if(start==len(nums[0])-1):
#                     break
#                 start+=1
#             j+=1
#         return ans



# Solution 2: all test case passed


# class Solution:
#     def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
#         dict1={}
#         for i in range(0,len(nums)):
#             for j in range(0,len(nums[i])):
#                 x=nums[i][j]
#                 if(i+j not in dict1):
#                     dict1[i+j]=[x]
#                 else:
#                     dict1[i+j].append(x)
#         ans=[]
#         for i in dict1:
#             for j in range(len(dict1[i])-1,-1,-1):
#                 ans.append(dict1[i][j])
#         return ans