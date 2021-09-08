# https://leetcode.com/problems/largest-number/

class Solution:
    def compareNumber(self,a,b):
        m=str(a)
        n=str(b)
        if(int(m+n)>int(n+m)):
            return False
        else:
            return True
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(Solution.compareNumber(self,nums[i],nums[j])==True):
                    nums[i],nums[j]=nums[j],nums[i]
                else:
                    continue
        str1=""
        for i in nums:
            str1+=str(i)
        return str(int(str1))
                    