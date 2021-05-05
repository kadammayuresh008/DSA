# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        pres=[]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                x=s[i:j]
                if(x==x[::-1]):
                    count+=1
        return count