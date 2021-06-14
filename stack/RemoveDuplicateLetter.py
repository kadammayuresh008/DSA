# https://leetcode.com/problems/remove-duplicate-letters/



class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        li=[0]*26
        for i in s:
            li[ord(i)-ord('a')]+=1
        visited=set()
        stack=[]
        for i in range(0,len(s)):
            li[ord(s[i])-ord('a')]-=1
            if(s[i] not in visited):
                while(stack and s[i]<stack[-1] and li[ord(stack[-1])-ord('a')]):
                    visited.remove(stack[-1])
                    stack.pop()
                visited.add(s[i])
                stack.append(s[i])
        return "".join(stack)