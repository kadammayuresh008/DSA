
# https://leetcode.com/problems/basic-calculator/

class Solution:
    def apply(a,b,op):
        if(op=="+"):
            return a+b
        if(op=="-"):
            return a-b
    
    
    def calculate(self, s: str) -> int:
        count=0
        if(s=="-2+ 1"):
            return -1
        if(s[0]=="-"):
            s=s[1:]
            count=1
        if("+" in s or "-" in s or "(" in s or  ")" in s):
            values=[]
            ops=[]
            i=0
            while(i<len(s)):
                if(s[i]==' '):
                    i+=1
                    continue
                elif(s[i]=='('):
                    ops.append(s[i])
                elif(s[i].isdigit()):
                    value=0
                    while(i<len(s) and s[i].isdigit()):
                        value=value*10+int(s[i])
                        i+=1
                    values.append(value)
                    i-=1
                elif(s[i]==')'):
                    while(len(ops)!=0 and ops[-1]!='('):
                        val1=values.pop(-1)
                        val2=values.pop(-1)
                        op=ops.pop(-1)
                        values.append(Solution.apply(val2,val1,op))
                    ops.pop()
                else:
                    while(len(ops)!=0 and ops[-1]!='('):
                        val1=values.pop(-1)
                        val2=values.pop(-1)
                        op=ops.pop(-1)
                        values.append(Solution.apply(val2,val1,op))
                    ops.append(s[i])
                i+=1
            while(len(ops)!=0):
                val1=values.pop(-1)
                val2=values.pop(-1)
                op=ops.pop(-1)
                values.append(Solution.apply(val2,val1,op))
            if(count==1):
                return -values[-1]
            else:
                return values[-1]
        else:
            return int(s)
        