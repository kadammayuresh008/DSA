
# https://leetcode.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[0 for i in range(0,len(t)+1)] for j in range(0,len(s)+1)]
        for i in range(0,len(dp)):
            for j in range(0,len(dp[0])):
                if(j==0):
                    dp[i][j]=1
                elif(i==0):
                    dp[i][j]=0
                else:
                    if(s[i-1]==t[j-1]):
                        dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
                    else:
                        dp[i][j]=dp[i-1][j]
        return dp[-1][-1]