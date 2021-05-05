


# https://leetcode.com/problems/delete-columns-to-make-sorted/



class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for i in range(0,len(strs[0])):
            ans=[]
            for j in strs:
                ans.append(j[i])
            x=ans.copy()
            ans.sort()
            if(x!=ans):
                count+=1
            else:
                continue
        return count
                