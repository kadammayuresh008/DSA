
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibo=[]
        f0=1
        f1=1
        f2=f0+f1
        fibo.append(f0)
        fibo.append(f1)
        while(f2<=k):
            fibo.append(f2)
            f0=f1
            f1=f2
            f2=f0+f1
        ans=0
        for i in range(len(fibo)-1,-1,-1):
            if(fibo[i]<=k):
                ans+=1
                k-=fibo[i]
        return ans