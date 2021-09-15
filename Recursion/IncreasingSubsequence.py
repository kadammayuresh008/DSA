# https://leetcode.com/problems/increasing-subsequences/


# Solution 1 : Recursive Solution with Optimization

class Solution:
    def check_increasing(nums):
        for i in range(0,len(nums)-1):
            if(nums[i+1]<nums[i]):
                return False
        return True
    
    def generate_combination(self,nums,i,combs):
        if(i==len(nums)):
            return combs
        ans=[]
        for j in combs:
            x=j+[nums[i]]
            if(Solution.check_increasing(x)==True):
                ans.append(x)
            else:
                continue
        combs+=ans
        return Solution.generate_combination(self,nums,i+1,combs)
    
        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        x=Solution.generate_combination(self,nums,0,[[]])
        dir1=[]
        for i in x:
            if(len(i)<2 or i in dir1):
                continue
            else:
                dir1.append(i)
        return dir1
        


# Solution 2:Backtracking


