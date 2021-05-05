# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i=0
        li=intervals
        li.sort()
        while(i<len(li)-1):
            if(li[i][1]>=li[i+1][0]):
                li[i][0]=min(li[i][0],li[i+1][0])
                li[i][1]=max(li[i][1],li[i+1][1])
                li.pop(i+1)
            else:
                i+=1
        return li