# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min1=9999999999
        for k in range(0,len(nums)):
            i=k+1
            j=len(nums)-1
            while(i<j):
                sum1=nums[i]+nums[j]+nums[k]
                if(abs(target-sum1)< abs(min1)):
                    min1=target-sum1
                    ans=sum1
                if(sum1>target):
                    j-=1
                else:
                    i+=1
            if(min1==0):
                break
        return ans
        