# # Approach1(Brute Force) TLE at case 23
# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         zero=0
#         one=0
#         count=[[0,0] for i in range(0,len(nums))]
#         for i in range(0,len(nums)):
#             if(nums[i]==0):
#                 zero+=1
#             else:
#                 one+=1
#             count[i]=[zero,one]
#         max1=0
#         for i in range(0,len(count)):
#             if(count[i][0]==count[i][1]):
#                 max1=max(max1,i+1)
#             else:
#                 continue
#         for i in range(0,len(count)-1):
#             for j in range(i+1,len(count)):
#                 diff0=abs(count[j][0]-count[i][0])
#                 diff1=abs(count[j][1]-count[i][1])
#                 if(diff0==diff1):
#                     if(j-i>max1):
#                         max1=j-i
#                     else:
#                         continue
#                 else:
#                     continue
#         return max1
            
            
            
        

# Approach2
# Using two pointer(526/564 cases passed)

# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         one=0
#         zero=0
#         for i in range(0,len(nums)):
#             if(nums[i]==0):
#                 zero+=1
#             else:
#                 one+=1
#         i=0
#         j=len(nums)-1
#         temp=0
#         while(one!=zero):
#             if(one>zero):
#                 if(nums[i]==1):
#                     i+=1
#                     one-=1
#                 elif(nums[j]==1):
#                     j-=1
#                     one-=1
#                 else:
#                     temp=1
#                     j-=1
#             elif(zero>one):
#                 if(nums[i]==0):
#                     i+=1
#                     zero-=1
#                 elif(nums[j]==0):
#                     j-=1
#                     zero-=1
#                 else:
#                     temp=1
#                     j-=1
#         if(temp==1):
#             return j-i
#         else:
#             return j-i+1




# Approach3(all test case passed)
# hashmap Solution
# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         dict1={0:-1}
#         count=0
#         max1=0
#         for i in range(0,len(nums)):
#             if(nums[i]==0):
#                 count-=1
#             else:
#                 count+=1
#             if(count in dict1):
#                 max1=max(max1,i-dict1[count])
#             else:
#                 dict1[count]=i
#         return max1