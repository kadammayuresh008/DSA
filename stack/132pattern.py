# https://leetcode.com/problems/132-pattern/

class Solution(object):
    def find132pattern(self, nums):
        min1=[nums[0]]
        for i in range(1,len(nums)):
            min1.append(min(nums[i],min1[i-1]))
        stack=[]
        for j in range(len(nums)-1,-1,-1):
            while(len(stack)>0 and stack[-1]<=min1[j]):
                stack.pop()
            if(len(stack)>0 and stack[-1]<nums[j]):
                return True
            stack.append(nums[j])
        return False