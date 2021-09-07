# https://leetcode.com/problems/insert-interval/


# solution 1
class Solution:
    def insert(self, A: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals=[]
        if(A==[]):
            intervals.append(newInterval)
        else:
            count=0
            for i in A:
                if(i[0]<newInterval[0]):
                    intervals.append(i)
                else:
                    if(count==0):
                        intervals.append(newInterval)
                        count=1
                    intervals.append(i)
            if(count==0):
                intervals.append(newInterval)
        i=0
        while(i<len(intervals)-1):
            if(intervals[i+1][0]<=intervals[i][1]):
                intervals[i][0]=min(intervals[i][0],intervals[i+1][0])
                intervals[i][1]=max(intervals[i][1],intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i+=1
        return intervals



# Solution 2

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        i=0
        while(i<len(intervals)-1):
            if(intervals[i+1][0]<=intervals[i][1]):
                intervals[i][0]=min(intervals[i][0],intervals[i+1][0])
                intervals[i][1]=max(intervals[i][1],intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i+=1
        return intervals