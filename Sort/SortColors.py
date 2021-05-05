# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i=1 
        count=1
        while(count<=len(nums)):
            if(nums[-i]==0):
                s=nums.pop(-i)
                nums.insert(0,s)
                count+=1
            elif(nums[-i]==1):
                count+=1
                i+=1
            else:
                s=nums.pop(-i)
                nums.append(s)
                count+=1
                i+=1