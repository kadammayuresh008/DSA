# https://leetcode.com/problems/remove-k-digits/



class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in range(0,len(num)):
            if(k<=0):
                stack.append(int(num[i]))
            else:
                while(stack!=[] and stack[-1]>int(num[i]) and k>0):
                    stack.pop(-1)
                    k-=1
                stack.append(int(num[i]))
        while(stack and k):
            stack.pop(-1)
            k-=1
        if(stack==[]):
            return "0"
        ans=""
        for i in range(0,len(stack)):
            ans+=str(stack[i])
        return str(int(ans))
        