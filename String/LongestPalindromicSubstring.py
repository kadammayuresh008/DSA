# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s)==1):
            return s
        else:
            longest=""
            for i in range(0,len(s)-1):
                char=s[i]
                for j in range(len(s)-1,i,-1):
                    if(s[j]==char):
                        x=s[i:j+1]
                        if(x==x[::-1]):
                            if(len(x)>len(longest)):
                                longest=x
            if(longest==""):
                return s[0]
            else:
                return longest