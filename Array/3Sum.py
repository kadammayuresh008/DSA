# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dict1={}
        ans=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                x=nums[i]+nums[j]
                if(-x in dict1 and dict1[-x][0]!=i and dict1[-x][1]!=j):
                    if(nums[i]+nums[j]+nums[dict1[-x][0]]==0):
                        ans.append([nums[i],nums[j],nums[dict1[-x][0]]])
                else:
                    dict1[x]=[i,j]
            print(dict1)
        return ans
                    