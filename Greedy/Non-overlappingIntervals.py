# https://leetcode.com/problems/non-overlapping-intervals/


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        length=len(intervals)
        intervals.sort(key=lambda x:x[1])
        i=0
        while(i<len(intervals)-1):
            if(intervals[i+1][0]<intervals[i][1]):
                intervals.pop(i+1)
            else:
                i+=1
        return length-len(intervals)
        