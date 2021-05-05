# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split(" ")
        a=""
        for i in range(len(x)-1,-1,-1):
            if(x[i]==''):
                continue
            else:
                a+=x[i]+" "
        return a.strip()