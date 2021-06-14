# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        for i in range(0,len(tokens)):
            if(tokens[i]=="+" or tokens[i]=="-" or tokens[i]=="/" or tokens[i]=="*"):
                x=stack.pop(-1)
                y=stack.pop(-1)
                if(tokens[i]=="+"):
                    stack.append(int(x)+int(y))
                elif(tokens[i]=="-"):
                    stack.append(int(y)-int(x))
                elif(tokens[i]=="*"):
                    stack.append(int(y)*int(x))
                elif(tokens[i]=="/"):
                    if((x<0 and y>0) or (x>0 and y<0) ):
                        ans=-round(abs(y)/abs(x))
                    else:
                         ans=round(abs(y)/abs(x))
                    stack.append(ans)
            else:
                stack.append(int(tokens[i]))
        return int(stack[0])