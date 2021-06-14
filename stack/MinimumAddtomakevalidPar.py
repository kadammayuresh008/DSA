# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        list1=[]
        for i in range(0,len(s)):
            if(s[i]=="("):
                list1.append(s[i])
            elif(s[i]==")"):
                if(len(list1)-1>=0):
                    if(list1[len(list1)-1]=="("):
                        list1.pop(len(list1)-1)
                    else:
                        list1.append(s[i])
                else:
                    list1.append(s[i])
        return len(list1)