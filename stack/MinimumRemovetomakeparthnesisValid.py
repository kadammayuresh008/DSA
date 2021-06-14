# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/



class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in range(0,len(s)):
            if(s[i]==")"):
                str1=s[i]
                while(stack!=[] and stack[-1]!="("):
                    ans=stack.pop()
                    str1=ans+str1
                if(stack!=[] and stack[-1]=="("):
                    ans=stack.pop()
                    str1=ans+str1
                    stack.append(str1)
                elif(stack==[]):
                    stack.append(str1[:-1])       
            else:
                stack.append(s[i])
        str2=""
        while(stack!=[]):
            x=stack.pop()
            if(x!="("):
                str2=x+str2
        return str2