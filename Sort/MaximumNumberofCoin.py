
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        if(len(piles)==3):
            return piles[1]
        else:
            sum1=0
            for i in range(0,int(len(piles)/3)*2,2):
                sum1+=piles[i+1]
            return sum1