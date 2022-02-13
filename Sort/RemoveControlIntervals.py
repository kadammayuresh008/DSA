# https://leetcode.com/problems/remove-covered-intervals/


# class Solution:
#     def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
#         i=0
#         intervals.sort()
#         while(i<len(intervals)-1):
#             if(intervals[i+1][0]<=intervals[i][0] and intervals[i+1][1]>=intervals[i][1]):
#                 intervals[i][0]=min(intervals[i][0],intervals[i+1][0])
#                 intervals[i][1]=max(intervals[i][1],intervals[i+1][1])
#                 intervals.pop(i+1)
#             elif(intervals[i+1][0]>=intervals[i][0] and intervals[i+1][1]<=intervals[i][1]):
#                 intervals[i][0]=min(intervals[i][0],intervals[i+1][0])
#                 intervals[i][1]=max(intervals[i][1],intervals[i+1][1])
#                 intervals.pop(i+1)
#             else:
#                 i+=1
#         return len(intervals)