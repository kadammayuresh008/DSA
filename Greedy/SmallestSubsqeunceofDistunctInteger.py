# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/



class Solution:
    def smallestSubsequence(self, s: str) -> str:
        li=[0]*26
        for i in s:
            li[ord(i)-ord('a')]+=1
        visited=set()
        stack=[]
        for i in range(0,len(s)):
            li[ord(s[i])-ord('a')]-=1
            if(s[i] not in visited):
                while(stack and stack[-1]>s[i] and li[ord(stack[-1])-ord('a')]):
                    visited.remove(stack[-1])
                    stack.pop()
                stack.append(s[i])
                visited.add(s[i])
        return "".join(stack)

