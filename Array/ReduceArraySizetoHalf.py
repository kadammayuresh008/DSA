
# https://leetcode.com/problems/reduce-array-size-to-the-half/submissions/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dict1={}
        for i in arr:
            if(i not in dict1):
                dict1[i]=1
            else:
                dict1[i]+=1
        D1 = dict(OrderedDict(sorted(dict1.items(), key = lambda t: t[1],reverse=True)))
        len1=len(arr)/2
        ans=0
        for i in D1:
            len1-=D1[i]
            ans+=1
            if(len1<=0):
                break 
        return ans