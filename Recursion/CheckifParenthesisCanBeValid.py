
# Solution 1:Recursion

class Solution:
    def validParenthesis(self,s):
        stack=[]
        for i in s:
            if(i=="("):
                stack.append("(")
            else:
                if(stack and stack[-1]=="("):
                    stack.pop(-1)
                else:
                    return False
        if(stack==[]):
            return True
        else:
            return False
    def generate(self,s,ind,n,locked):
        if(ind==n):
            return False
        else:
            if(locked[ind]==1):
                return 
            else:
                if(s[ind]=="("):
                    s1=s[0:ind]+")"+s[ind+1:]
                else:
                    s1=s[0:ind]+"("+s[ind+1:]
                if(Solution.validParenthesis(self,s1)==True):
                    return True
                else:
                    return Solution.generate(self,s1,ind+1,n,locked)
                if(Solution.validParenthesis(self,s)==True):
                    return True
                else:
                    return Solution.generate(self,s,ind+1,n,locked)
                    
    def canBeValid(self, s: str, locked: str) -> bool:
        if(len(s)%2!=0):
            return False
        else:
            if(Solution.validParenthesis(self,s)==True):
                return True
            else:
                x=Solution.generate(self,s,0,len(s),locked)
                return x
            
        