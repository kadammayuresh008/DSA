



# https://leetcode.com/problems/generate-parentheses/


# Solution1:Recursive solution
class Solution:
    def generate(li):
        li2=[]
        for j in li:
            for k in range(0,len(j)):
                s=j[0:k]+"()"+j[k:]
                if s not in li2:
                    li2.append(s)
        return li2
    def generateParenthesis(self, n: int) -> List[str]:
        li=["()"]
        for i in range(0,n-1):
            li=Solution.generate(li)
        return li



        
        