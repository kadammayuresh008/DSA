# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        if(len(digits)==0):
            return []
        elif(len(digits)==1):
            li=[]
            for i in dict1[digits[0]]:
                li.append(i)
            return li
        elif(len(digits)==2):
            x=dict1[digits[0]]
            y=dict1[digits[1]]
            li=[]
            for i in x:
                for j in y:
                    li.append(i+j)
            return li
        elif(len(digits)==3):
            x=dict1[digits[0]]
            y=dict1[digits[1]]
            z=dict1[digits[2]]
            li=[]
            for i in x:
                for j in y:
                    for k in z:
                        li.append(i+j+k)
            return li
        elif(len(digits)==4):
            x=dict1[digits[0]]
            y=dict1[digits[1]]
            z=dict1[digits[2]]
            w=dict1[digits[3]]
            li=[]
            for i in x:
                for j in y:
                    for k in z:
                        for l in w:
                            li.append(i+j+k+l)
            return li
        