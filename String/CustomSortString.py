class Solution:
    def customSortString(self, order: str, str1: str) -> str:
        ans=""
        dict1={i:str1.count(i) for i in str1}
        for i in range(0,len(order)):
            if(order[i] in dict1):
                for j in range(0,dict1[order[i]]):
                    x=str1.index(order[i])
                    if(x>=0 and x<len(str1)):
                        str1=str1[0:x]+str1[x+1:]
                        ans+=order[i]
        return ans+str1