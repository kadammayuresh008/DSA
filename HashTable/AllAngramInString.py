
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char=0
        for i in p:
            char+=hash(i)
        x=len(p)
        ans=[]
        j=x
        sum1=0
        for i in s[0:j]:
            sum1+=hash(i)
        if(sum1==char):
            ans.append(0)
        for i in range(0,len(s)-x):
            sum1+=(-hash(s[i])+hash(s[j]))
            if(sum1==char):
                ans.append(i+1)
            j+=1
        return ans