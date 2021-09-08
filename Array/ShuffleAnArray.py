
# https://leetcode.com/problems/shuffle-an-array/

import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums=nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums=list(self.nums)
        b=[]
        while(nums):
            x=random.randint(0,len(nums)-1)
            nums[x],nums[-1]=nums[-1],nums[x]
            b.append(nums.pop())
        return b
    
    
 

