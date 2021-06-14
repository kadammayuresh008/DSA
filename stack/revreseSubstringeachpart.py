# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in range(0,len(s)):
            if(s[i]==")"):
                str1=""
                while(stack!=[] and stack[-1]!="("):
                    x=stack.pop()
                    str1+=x
                str1=str1[::-1]
                stack.pop()
                stack.append(str1)
            else:
                stack.append(s[i])
        str1=""
        while(stack!=[]):
            str1+=stack.pop()
        return str1[::-1]
        