# https://leetcode.com/problems/next-greater-element-ii/




class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums)):
            count=0
            j=(i+1)%len(nums)
            while(i!=j):
                if(nums[j]>nums[i]):
                    count=1
                    ans.append(nums[j])
                    break
                j=(j+1)%len(nums)
            if(count==0):
                ans.append(-1)
        return ans
        