


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        setfirst=0
        setlast=0
        posfirst=-1
        poslast=-1
        lower=0
        upper=len(nums)-1
        while(lower<=upper):
            mid=(lower+upper)//2
            if(target<nums[mid]):
                upper=mid-1
            elif(nums[mid]<target):
                lower=mid+1
            else:
                poslast=mid
                x=nums[poslast]
                i=0
                while(nums[poslast-i]==x and poslast-i>0):
                    i+=1
                posfirst1=poslast-i+1
                i=0
                while(nums[poslast+i]==x and poslast+i<len(nums)-1):
                    i+=1
                posfirst2=poslast+i-1
                return [min(posfirst1,poslast,posfirst2),max(posfirst1,poslast,posfirst2)]
        return [min(posfirst1,poslast,posfirst2),max(posfirst1,poslast,posfirst2)]