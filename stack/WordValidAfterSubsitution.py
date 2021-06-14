
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

class Solution:
    def isValid(self, s: str) -> bool:
        t=""
        for i in range(0,len(s)):
            if(s[i]=="a"):
                if(i>len(t)-1):
                    t+="abc"
                elif(i<=len(t)-1):
                    t=t[0:i]+"abc"+t[i:]
        if(s==t):
            return True
        else:
            return False