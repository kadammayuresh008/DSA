# https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dict1={}
        for i in range(0,len(s)-9):
            x=s[i:i+10]
            if(x not in dict1):
                dict1[x]=1
            else:
                dict1[x]+=1
        ans=[]
        for i in dict1:
            if(dict1[i]>1):
                ans.append(i)
            else:
                continue
        return ans
        