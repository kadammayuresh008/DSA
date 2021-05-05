
# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        ans=n//7
        ans1=n%7
        sum1=0
        for i in range(1,ans+1):
            sum1+=(7/2)*(2*(i)+6)
        sum1+=(ans1/2)*(2*(ans+1)+(ans1-1))
        return int(sum1)