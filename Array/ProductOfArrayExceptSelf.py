# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[]
        sum1=1
        for k in range(0,len(nums)):
            sum1*=nums[k]
        for j in range(0,len(nums)):
            if(nums[j]==0):
                mul=1
                for i in range(0,len(nums)):
                    if(j==i):
                        continue
                    else:
                        mul*=nums[i]
                arr.append(mul)
            else:
                arr.append(int(sum1/nums[j]))
        return arr