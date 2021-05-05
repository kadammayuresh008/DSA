# https://leetcode.com/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        starttime=0
        endtime=0
        sum1=0
        for i in customers:
            starttime=max(i[0],endtime)
            endtime=starttime+i[1]
            waiting=endtime-i[0]
            sum1+=waiting
        x=(sum1/len(customers))
        return x