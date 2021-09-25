
# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        x=matrix
        res=0
        for i in x:
            c=0
            a=[l^1 for l in i]
            for j in x:
                if(j==i or j==a):
                    c+=1
                else:
                    continue
            res=max(res,c)
        return res
            