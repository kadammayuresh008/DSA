# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        str1=""
        for i in range(0,len(s)):
            if(s[i]!="]"):
                stack.append(s[i])
            else:
                str1=""
                top=len(stack)-1
                while(stack[top]!="["):
                    top-=1
                    str1+=stack.pop(-1)
                stack.pop(-1)
                top=len(stack)-1
                num=""
                while(ord(stack[top])>=48 and ord(stack[top])<=57):
                    top-=1
                    num+=stack.pop(-1)
                    if(top<0 or len(stack[top])>1 or stack[top]=="["):
                        break
                num=num[::-1]
                str2=""
                for i in range(0,int(num)):
                    str2+=str1
                stack.append(str2)
        ans=""
        for i in range(0,len(stack)):
            ans+=stack[i][::-1]
        return ans